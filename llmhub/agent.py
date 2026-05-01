"""Agent chat operations for LLMHub SDK.

Wraps ``POST /api/v2/agent/chat`` — multi-turn chat with tool-use, accepting
either OpenAI-shape or Anthropic-shape input and mirroring the request shape
on the response (overridable via ``response_shape``).

Implementation note: this endpoint is NOT in the generated/ urllib3 layer
because the OpenAPI spec the SDK was generated from predates the agent
endpoint. We use ``urllib3.PoolManager`` directly here, matching the same
HTTP transport the generated layer uses.
"""

import json
from typing import Any, Dict, List, Optional, Union

import urllib3
from urllib3.exceptions import HTTPError

from llmhub.exceptions import LLMHubError, convert_api_exception


_AGENT_PATH = "/api/v2/agent/chat"


class AgentChatResponse:
    """Response object for ``client.agent.chat()``.

    Mirrors the canonical pivot fields from ``V2AgentChatResponse``. Accessed
    as attributes (``resp.content``, ``resp.tool_calls``…) and indexable
    (``resp["cost_usd"]``) for parity with dict-based callers.

    Attributes:
        content: ``str`` (OpenAI shape) or ``list[dict]`` of content blocks
            (Anthropic shape). May be empty when the model goes straight to
            a tool call.
        tool_calls: List of OpenAI-shape tool calls (``[{id, type, function:
            {name, arguments}}, …]``) when ``shape="openai"``. Always
            ``None`` in Anthropic shape (the tool_use blocks live inside
            ``content`` instead).
        stop_reason: ``"stop"`` | ``"tool_calls"`` | ``"length"`` (OpenAI)
            or ``"end_turn"`` | ``"tool_use"`` | ``"max_tokens"`` (Anthropic).
        provider_used: Resolved provider name (``"melious"``, ``"claude"``…).
        model_used: Resolved model id.
        input_tokens / output_tokens / tokens_used: Token counts.
        cost_usd: Total billed cost for this call.
        generation_time_ms: Wall-clock latency including provider call.
        log_id: UUID string of the billing log row, if persisted.
        provider_metadata: Provider-specific extras (rate-limit hints,
            cache stats, environment_impact for Melious, …).
        shape: Echoes the rendered shape, ``"openai"`` or ``"anthropic"``.
        raw: The full decoded JSON response (escape hatch for callers that
            need fields not exposed as attributes).
    """

    __slots__ = (
        "success", "content", "tool_calls", "stop_reason",
        "provider_used", "model_used",
        "input_tokens", "output_tokens", "tokens_used",
        "cost_usd", "generation_time_ms", "log_id",
        "provider_metadata", "shape", "raw",
    )

    def __init__(self, raw: Dict[str, Any]):
        self.raw = raw
        self.success = bool(raw.get("success", True))
        self.content = raw.get("content")
        self.tool_calls = raw.get("tool_calls")
        self.stop_reason = raw.get("stop_reason") or "stop"
        self.provider_used = raw.get("provider_used") or ""
        self.model_used = raw.get("model_used") or ""
        self.input_tokens = int(raw.get("input_tokens") or 0)
        self.output_tokens = int(raw.get("output_tokens") or 0)
        self.tokens_used = int(raw.get("tokens_used") or 0)
        self.cost_usd = float(raw.get("cost_usd") or 0.0)
        self.generation_time_ms = int(raw.get("generation_time_ms") or 0)
        self.log_id = raw.get("log_id")
        self.provider_metadata = raw.get("provider_metadata") or {}
        self.shape = raw.get("shape") or "openai"

    def __getitem__(self, key: str) -> Any:
        return self.raw[key]

    def get(self, key: str, default: Any = None) -> Any:
        return self.raw.get(key, default)

    def __repr__(self) -> str:
        snippet = ""
        if isinstance(self.content, str):
            snippet = self.content[:60].replace("\n", " ")
        return (
            f"AgentChatResponse(provider={self.provider_used!r}, "
            f"model={self.model_used!r}, stop_reason={self.stop_reason!r}, "
            f"tokens={self.tokens_used}, cost_usd={self.cost_usd}, "
            f"content={snippet!r}…)"
        )


class _Urllib3HTTPError:
    """Adapter that gives a urllib3 response a ``.status``/``.headers``/``str()``
    surface compatible with :func:`convert_api_exception`."""

    def __init__(self, status: int, headers: Any, body: str):
        self.status = status
        self.headers = headers
        self.body = body

    def __str__(self) -> str:
        return self.body or f"HTTP {self.status}"


class AgentOperations:
    """Agent chat — ``POST /api/v2/agent/chat``."""

    def __init__(self, base_url: str, api_key: str, http: Optional[urllib3.PoolManager] = None):
        """Initialize AgentOperations.

        Args:
            base_url: Base URL of the HUBLE API (no trailing slash; the
                client strips it).
            api_key: ``X-API-Key`` value for V2 auth.
            http: Optional injected ``urllib3.PoolManager``. Useful for
                tests; defaults to a module-private pool.
        """
        self._base_url = base_url.rstrip("/")
        self._api_key = api_key
        self._http = http or urllib3.PoolManager()

    def chat(
        self,
        messages: List[Dict[str, Any]],
        *,
        provider: Optional[str] = None,
        model: Optional[str] = None,
        tools: Optional[List[Dict[str, Any]]] = None,
        tool_choice: Optional[Union[str, Dict[str, Any]]] = None,
        system: Optional[str] = None,
        max_tokens: Optional[int] = 1024,
        temperature: Optional[float] = None,
        shape: Optional[str] = None,
        response_shape: Optional[str] = None,
        provider_options: Optional[Dict[str, Dict[str, Any]]] = None,
        timeout: float = 120.0,
    ) -> AgentChatResponse:
        """Multi-turn chat with optional tool-use.

        Args:
            messages: Conversation messages. Either OpenAI shape
                (``{role, content, tool_calls?, tool_call_id?}``) or Anthropic
                shape (``{role, content: [{type:"text"|"tool_use"|
                "tool_result", …}]}``). Auto-detected when ``shape`` is None.
            provider: Provider override (``"melious"``, ``"claude"``,
                ``"openai"``, …). Falls back to backend default.
            model: Model id within the chosen provider. Backend supplies a
                sensible default per provider when omitted.
            tools: Tool definitions. OpenAI shape (``[{type:"function",
                function:{name, parameters}}]``) or Anthropic shape
                (``[{name, description, input_schema}]``). Auto-detected.
            tool_choice: ``"auto"`` | ``"none"`` | ``"required"`` |
                ``{"type":"function", "function":{"name":...}}`` |
                ``{"type":"any"|"tool", "name":...}`` (Anthropic).
            system: Top-level system prompt (Anthropic-style). Alternative
                to a leading ``{"role":"system", …}`` message.
            max_tokens: Cap on generated tokens. Default 1024; floor 1.
            temperature: Sampling temperature 0.0–2.0.
            shape: Force-declare wire shape ``"openai"`` or ``"anthropic"``
                instead of auto-detecting.
            response_shape: Render response in this shape regardless of
                request shape. Defaults to mirror ``shape``.
            provider_options: Vendor-specific knobs keyed by provider name,
                e.g. ``{"anthropic": {"thinking": {...}}}``.
            timeout: Seconds. Default 120 — agent loops with tool execution
                can be slow.

        Returns:
            :class:`AgentChatResponse`

        Raises:
            AuthenticationError: 401 / 403.
            NotFoundError: 404.
            ValidationError: 422 / other 4xx.
            RateLimitError: 429 (with ``retry_after``).
            ServerError: 5xx.
            LLMHubError: Anything else (network, decode failures).
        """
        body: Dict[str, Any] = {"messages": messages}
        if provider is not None:
            body["provider"] = provider
        if model is not None:
            body["model"] = model
        if tools is not None:
            body["tools"] = tools
        if tool_choice is not None:
            body["tool_choice"] = tool_choice
        if system is not None:
            body["system"] = system
        if max_tokens is not None:
            body["max_tokens"] = max_tokens
        if temperature is not None:
            body["temperature"] = temperature
        if shape is not None:
            body["shape"] = shape
        if response_shape is not None:
            body["response_shape"] = response_shape
        if provider_options is not None:
            body["provider_options"] = provider_options

        url = self._base_url + _AGENT_PATH
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "X-API-Key": self._api_key,
        }

        try:
            resp = self._http.request(
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
            raise LLMHubError(f"Invalid JSON response from {_AGENT_PATH}: {e}") from e

        return AgentChatResponse(data)
