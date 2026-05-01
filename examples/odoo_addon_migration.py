"""Migration example — replace raw `requests` with the HUBLE SDK.

Reference: NOCA's `customers/KJ_V18/addons/llm/llm_base/model/llm_huble.py`
talks to HUBLE via raw `requests.post(...)` with manual response unwrapping
and per-call status-code handling. This file shows the equivalent using
the SDK.

Both blocks below are runnable; pick the AFTER block for new code.

================================================================================
BEFORE — raw requests (current NOCA shape)
================================================================================
"""

# --- BEFORE: ~80 lines of HTTP plumbing for two endpoints ----------------

import logging
import requests

_logger = logging.getLogger(__name__)


def discovery_before(base_url: str, api_key: str) -> list:
    """Fetch model catalog. Manual status-code handling, manual JSON parsing,
    manual fallback between `data.models` and `data.data` shapes."""
    headers = {"X-API-Key": api_key, "Content-Type": "application/json"}
    response = requests.get(f"{base_url}/api/v2/discovery/models", headers=headers, timeout=30)
    response.raise_for_status()
    data = response.json()
    raw_models = data.get("models") or data.get("data") or []
    result = []
    for m in raw_models:
        identifier = m.get("key") or m.get("id") or m.get("model")
        if identifier:
            result.append({"model": identifier, "info": m})
    return result


def chat_before(base_url: str, api_key: str, prompt: str, system: str = None) -> str:
    """Single-shot chat via /api/v2/chat/completions. Builds payload by
    hand, manually unwraps `content`, manually handles HTTPError."""
    headers = {"X-API-Key": api_key, "Content-Type": "application/json"}
    messages = []
    if system:
        messages.append({"role": "system", "content": system})
    messages.append({"role": "user", "content": prompt})

    payload = {
        "messages": messages,
        "model": "deepseek-v3.2",
        "temperature": 0.7,
        "max_tokens": 4096,
    }
    try:
        response = requests.post(
            f"{base_url}/api/v2/chat/completions",
            headers=headers, json=payload, timeout=120,
        )
        response.raise_for_status()
        result = response.json()
        # chat/completions returns wrapped shape with `content` at top level
        return result.get("content") or ""
    except requests.HTTPError as e:
        body = e.response.text[:500] if e.response is not None else ""
        status = e.response.status_code if e.response is not None else "unknown"
        _logger.error("[Huble] /chat/completions %s: %s", status, body)
        raise


def chat_with_tools_before(base_url: str, api_key: str, messages: list, tools: list) -> dict:
    """Tool-using chat. Caller now also has to know that HUBLE's wrapped
    response (`{content, tool_calls, stop_reason, …}`) needs flattening to
    OpenAI's `chat.completion` shape (`{choices:[{message:{...}}], usage:…}`)
    before any OpenAI-shaped tool adapter can consume it. NOCA does this in
    a private `_huble_to_openai_shape()` helper."""
    headers = {"X-API-Key": api_key, "Content-Type": "application/json"}
    payload = {
        "messages": messages,
        "tools": tools,
        "tool_choice": "auto",
        "model": "claude-haiku-4-5",
        "max_tokens": 1024,
    }
    response = requests.post(
        f"{base_url}/api/v2/chat/completions",
        headers=headers, json=payload, timeout=120,
    )
    response.raise_for_status()
    raw = response.json()

    # Manual unwrap — exactly the helper that lives in NOCA today.
    if "choices" in raw:
        return raw  # already OpenAI-shaped
    message = {"role": "assistant", "content": raw.get("content") or ""}
    if raw.get("tool_calls"):
        message["tool_calls"] = raw["tool_calls"]
    return {
        "choices": [{
            "index": 0, "message": message,
            "finish_reason": raw.get("stop_reason") or "stop",
        }],
        "usage": {
            "prompt_tokens": raw.get("input_tokens", 0) or 0,
            "completion_tokens": raw.get("output_tokens", 0) or 0,
            "total_tokens": raw.get("tokens_used", 0) or 0,
        },
        "cost_usd": raw.get("cost_usd"),
        "model": raw.get("model_used"),
    }


# --- AFTER: same three operations, SDK-driven ----------------------------

"""
================================================================================
AFTER — SDK
================================================================================
"""

from llmhub import LLMHub


def discovery_after(client: LLMHub) -> list:
    """One call. The SDK handles the response shape variants and surfaces
    typed exceptions (NotFoundError / AuthenticationError / …)."""
    return client.discovery.get_models()


def chat_after(client: LLMHub, prompt: str, system: str = None) -> str:
    """Single-shot chat. The SDK builds the messages list, posts, unwraps
    the response, and converts errors to typed exceptions."""
    messages = []
    if system:
        messages.append({"role": "system", "content": system})
    messages.append({"role": "user", "content": prompt})

    resp = client.chat.completions.create(
        model="deepseek-v3.2",
        messages=messages,
        temperature=0.7,
        max_tokens=4096,
    )
    return resp.choices[0].message.content or ""


def chat_with_tools_after(client: LLMHub, messages: list, tools: list) -> "ChatCompletion":
    """Tool-using chat. The SDK returns an OpenAI-shape ChatCompletion —
    hand it directly to any OpenAI-shaped tool adapter (e.g. NOCA's
    `tool_adapter_openai`) without any conversion."""
    return client.chat.completions.create(
        model="claude-haiku-4-5",
        messages=messages,
        tools=tools,
        tool_choice="auto",
        max_tokens=1024,
    )


# --- Diff summary --------------------------------------------------------

"""
What goes away in NOCA after the migration:

  llm_base/model/llm_huble.py
    - 151 lines down to ~30 lines (config + thin call dispatch)
    - delete _huble_base_url / _huble_headers (SDK manages these)
    - delete _call_huble / _huble_to_openai_shape (SDK provides them)
    - delete the `import requests` and per-call HTTPError branches

  llm_agent_builder/models/llm_agent_provider.py
    - delete the local _huble_to_openai_shape() helper
      (replace with `from llmhub import huble_to_openai_chat_completion`,
      or skip the helper entirely and use `client.chat.completions.create()`
      which already returns OpenAI shape)
    - tool_adapter_openai.py keeps working unchanged — the SDK's
      ChatCompletion exposes the same attribute path
      `resp.choices[0].message.tool_calls[i].function.{name,arguments}`

Setup in the addon (one-time, e.g. in __init__ of the provider model):

    from llmhub import LLMHub

    self._huble_client = LLMHub(
        api_key=llm_provider.x_api_key,
        base_url=llm_provider.x_endpoint or "http://localhost:4000",
    )

The same client instance handles discovery, single-shot chat, and
tool-using chat.
"""


if __name__ == "__main__":  # pragma: no cover
    # Tiny demo (requires LLMHUB_API_KEY in env).
    client = LLMHub()  # picks up env vars
    print("Models:", len(client.discovery.get_models()))
    print(chat_after(client, "Reply with: hello"))
