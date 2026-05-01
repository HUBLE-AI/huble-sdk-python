"""OpenAI-shaped chat completions for LLMHub SDK.

Wraps ``POST /api/v2/chat/completions`` — same handler as ``/agent/chat`` on
the backend but logged separately so usage stats can distinguish OpenAI
SDK clients from agent-shape clients.

The return type mimics the OpenAI Python SDK's ``ChatCompletion``: nested
attribute access (``r.choices[0].message.tool_calls[0].function.name``)
plus dict-style fallback (``r["usage"]["prompt_tokens"]``). This lets
callers built around ``openai.OpenAI()`` swap base_url to HUBLE without
touching response-handling code.
"""

import json
from typing import Any, Dict, List, Optional, Union

import urllib3
from urllib3.exceptions import HTTPError

from llmhub._shape import huble_to_openai_chat_completion
from llmhub.exceptions import LLMHubError, convert_api_exception


_CHAT_PATH = "/api/v2/chat/completions"


# ---------------------------------------------------------------------------
# Response objects — attribute access mirrors openai.ChatCompletion
# ---------------------------------------------------------------------------

class _ToolFunction:
    __slots__ = ("name", "arguments")

    def __init__(self, raw: Dict[str, Any]):
        self.name = raw.get("name") or ""
        # OpenAI SDK keeps arguments as a JSON string; preserve that.
        args = raw.get("arguments")
        self.arguments = args if isinstance(args, str) else json.dumps(args or {})


class _ToolCall:
    __slots__ = ("id", "type", "function", "index")

    def __init__(self, raw: Dict[str, Any]):
        self.id = raw.get("id") or ""
        self.type = raw.get("type") or "function"
        self.function = _ToolFunction(raw.get("function") or {})
        self.index = raw.get("index", 0)


class _Message:
    __slots__ = ("role", "content", "tool_calls", "refusal")

    def __init__(self, raw: Dict[str, Any]):
        self.role = raw.get("role") or "assistant"
        self.content = raw.get("content")
        self.refusal = raw.get("refusal")
        tcs = raw.get("tool_calls")
        # Always set the attribute — None when no tool calls — so
        # `hasattr(msg, "tool_calls")` is True (NOCA relies on this).
        self.tool_calls = [_ToolCall(t) for t in tcs] if tcs else None


class _Choice:
    __slots__ = ("index", "message", "finish_reason", "logprobs")

    def __init__(self, raw: Dict[str, Any]):
        self.index = int(raw.get("index", 0))
        self.message = _Message(raw.get("message") or {})
        self.finish_reason = raw.get("finish_reason") or "stop"
        self.logprobs = raw.get("logprobs")


class _Usage:
    __slots__ = ("prompt_tokens", "completion_tokens", "total_tokens")

    def __init__(self, raw: Dict[str, Any]):
        self.prompt_tokens = int(raw.get("prompt_tokens") or 0)
        self.completion_tokens = int(raw.get("completion_tokens") or 0)
        self.total_tokens = int(raw.get("total_tokens") or 0)


class ChatCompletion:
    """OpenAI-shape ``chat.completion`` response.

    Usage::

        resp = client.chat.completions.create(model="...", messages=[...])
        text = resp.choices[0].message.content
        for tc in resp.choices[0].message.tool_calls or []:
            args = json.loads(tc.function.arguments)
        print(resp.usage.total_tokens, resp.cost_usd)
    """

    __slots__ = (
        "id", "object", "created", "model", "choices", "usage",
        # HUBLE bookkeeping passed through (not in OpenAI's shape).
        "cost_usd", "provider_used", "log_id", "provider_metadata",
        "generation_time_ms",
        "raw",
    )

    def __init__(self, raw: Dict[str, Any]):
        self.raw = raw
        self.id = raw.get("id") or ""
        self.object = raw.get("object") or "chat.completion"
        self.created = int(raw.get("created") or 0)
        self.model = raw.get("model") or ""
        self.choices = [_Choice(c) for c in (raw.get("choices") or [])]
        self.usage = _Usage(raw.get("usage") or {})
        self.cost_usd = raw.get("cost_usd")
        self.provider_used = raw.get("provider_used")
        self.log_id = raw.get("log_id")
        self.provider_metadata = raw.get("provider_metadata")
        self.generation_time_ms = raw.get("generation_time_ms")

    def __getitem__(self, key: str) -> Any:
        return self.raw[key]

    def get(self, key: str, default: Any = None) -> Any:
        return self.raw.get(key, default)

    def model_dump(self) -> Dict[str, Any]:
        """Pydantic-style dict export — returns the underlying raw payload."""
        return dict(self.raw)


# ---------------------------------------------------------------------------
# Operations
# ---------------------------------------------------------------------------

class _Urllib3HTTPError:
    """Adapter giving urllib3 responses the .status/.headers/.body surface
    expected by :func:`convert_api_exception`."""

    def __init__(self, status: int, headers: Any, body: str):
        self.status = status
        self.headers = headers
        self.body = body

    def __str__(self) -> str:
        return self.body or f"HTTP {self.status}"


class _Completions:
    """Namespace exposing ``client.chat.completions.create(...)``."""

    def __init__(self, parent: "ChatOperations"):
        self._parent = parent

    def create(
        self,
        *,
        messages: List[Dict[str, Any]],
        model: Optional[str] = None,
        provider: Optional[str] = None,
        tools: Optional[List[Dict[str, Any]]] = None,
        tool_choice: Optional[Union[str, Dict[str, Any]]] = None,
        max_tokens: Optional[int] = 1024,
        temperature: Optional[float] = None,
        provider_options: Optional[Dict[str, Dict[str, Any]]] = None,
        timeout: float = 120.0,
        **extra: Any,
    ) -> ChatCompletion:
        """OpenAI SDK drop-in for ``chat.completions.create``.

        Args:
            messages: OpenAI-shape conversation. Backend also accepts
                Anthropic shape but this method is for OpenAI parity.
            model: Model id. Backend supplies a default per provider.
            provider: Optional provider override (extension over OpenAI's
                surface — OpenAI's SDK has no provider concept).
            tools: OpenAI-shape function tool definitions.
            tool_choice: ``"auto"`` | ``"none"`` | ``"required"`` |
                ``{"type":"function", "function":{"name":...}}``.
            max_tokens: Generation cap. Default 1024.
            temperature: Sampling temperature.
            provider_options: Vendor-specific knobs keyed by provider.
            timeout: Seconds.
            **extra: Forwarded verbatim — accommodates future params (e.g.
                ``top_p``, ``stop``, ``response_format``) without an SDK
                bump. Keys with ``None`` values are dropped.

        Returns:
            :class:`ChatCompletion` in OpenAI shape.
        """
        body: Dict[str, Any] = {"messages": messages, "shape": "openai"}
        if model is not None:
            body["model"] = model
        if provider is not None:
            body["provider"] = provider
        if tools is not None:
            body["tools"] = tools
        if tool_choice is not None:
            body["tool_choice"] = tool_choice
        if max_tokens is not None:
            body["max_tokens"] = max_tokens
        if temperature is not None:
            body["temperature"] = temperature
        if provider_options is not None:
            body["provider_options"] = provider_options
        for k, v in extra.items():
            if v is not None:
                body[k] = v

        url = self._parent._base_url + _CHAT_PATH
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "X-API-Key": self._parent._api_key,
        }

        try:
            resp = self._parent._http.request(
                "POST", url,
                body=json.dumps(body).encode("utf-8"),
                headers=headers,
                timeout=urllib3.Timeout(total=timeout),
                retries=False,
            )
        except HTTPError as e:
            raise convert_api_exception(e) from e

        if resp.status >= 400:
            try:
                text = resp.data.decode("utf-8", errors="replace")
            except Exception:
                text = ""
            raise convert_api_exception(_Urllib3HTTPError(resp.status, resp.headers, text))

        try:
            data = json.loads(resp.data.decode("utf-8"))
        except (ValueError, UnicodeDecodeError) as e:
            raise LLMHubError(f"Invalid JSON response from {_CHAT_PATH}: {e}") from e

        # Backend currently returns the wrapped agent shape. Unwrap to OpenAI.
        unwrapped = huble_to_openai_chat_completion(data)
        return ChatCompletion(unwrapped)


class ChatOperations:
    """``client.chat.completions.create(...)`` namespace."""

    def __init__(self, base_url: str, api_key: str, http: Optional[urllib3.PoolManager] = None):
        self._base_url = base_url.rstrip("/")
        self._api_key = api_key
        self._http = http or urllib3.PoolManager()
        self.completions = _Completions(self)
