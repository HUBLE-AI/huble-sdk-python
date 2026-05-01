"""Shape conversion helpers — pure functions, no I/O.

HUBLE returns its agent/chat results in a wrapped shape::

    {
      "content": "…",
      "tool_calls": [{...}] | null,
      "stop_reason": "stop" | "tool_calls" | "length",
      "input_tokens": …, "output_tokens": …, "tokens_used": …,
      "cost_usd": …, "model_used": …, "provider_used": …,
      ...
    }

OpenAI's ``chat.completions`` SDK returns a nested ``ChatCompletion``::

    {
      "id": "...", "object": "chat.completion", "created": ...,
      "model": "...",
      "choices": [{
        "index": 0,
        "message": {"role": "assistant", "content": "...", "tool_calls": [...]?},
        "finish_reason": "stop" | "tool_calls" | "length",
      }],
      "usage": {"prompt_tokens": …, "completion_tokens": …, "total_tokens": …},
    }

This module bridges the two so the SDK can expose an OpenAI-shape result
from HUBLE's wrapped response, and so NOCA can replace its in-tree
``_huble_to_openai_shape()`` helper with an SDK import.
"""

from typing import Any, Dict


def huble_to_openai_chat_completion(raw: Any) -> Dict[str, Any]:
    """Convert HUBLE's wrapped chat response to OpenAI ``chat.completion`` shape.

    Idempotent: a payload that is already in OpenAI shape (``"choices"`` key
    present) is returned unchanged.

    Args:
        raw: Decoded JSON from ``/api/v2/chat/completions`` or
             ``/api/v2/agent/chat``.

    Returns:
        Dict in OpenAI ``chat.completion`` shape. Bookkeeping fields HUBLE
        adds (``cost_usd``, ``provider_used``, ``log_id``,
        ``provider_metadata``) are preserved at the top level for callers
        that want them — the OpenAI SDK simply ignores unknown keys.
    """
    if not isinstance(raw, dict):
        return raw
    if "choices" in raw:
        return raw

    message: Dict[str, Any] = {
        "role": "assistant",
        "content": raw.get("content") or "",
    }
    tool_calls = raw.get("tool_calls")
    if tool_calls:
        message["tool_calls"] = tool_calls

    return {
        "id": raw.get("log_id") or "",
        "object": "chat.completion",
        "created": 0,
        "model": raw.get("model_used") or "",
        "choices": [{
            "index": 0,
            "message": message,
            "finish_reason": raw.get("stop_reason") or "stop",
        }],
        "usage": {
            "prompt_tokens": int(raw.get("input_tokens") or 0),
            "completion_tokens": int(raw.get("output_tokens") or 0),
            "total_tokens": int(raw.get("tokens_used") or 0),
        },
        # HUBLE-specific bookkeeping passed through verbatim.
        "cost_usd": raw.get("cost_usd"),
        "provider_used": raw.get("provider_used"),
        "log_id": raw.get("log_id"),
        "provider_metadata": raw.get("provider_metadata"),
        "generation_time_ms": raw.get("generation_time_ms"),
    }
