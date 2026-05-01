"""Unit tests for ChatOperations / chat.completions.create — mock urllib3."""

from __future__ import annotations

import json
from unittest.mock import Mock

import pytest

from llmhub.chat import ChatOperations, ChatCompletion
from llmhub.exceptions import (
    AuthenticationError,
    NotFoundError,
    RateLimitError,
    ServerError,
    ValidationError,
    LLMHubError,
)


def _mock_response(status, body=None, headers=None):
    resp = Mock()
    resp.status = status
    if isinstance(body, dict):
        resp.data = json.dumps(body).encode("utf-8")
    elif isinstance(body, str):
        resp.data = body.encode("utf-8")
    else:
        resp.data = b""
    resp.headers = headers or {}
    return resp


@pytest.fixture
def http():
    return Mock()


@pytest.fixture
def chat(http, mock_api_key, mock_base_url):
    return ChatOperations(mock_base_url, mock_api_key, http=http)


@pytest.mark.unit
class TestChatCompletionsCreate:
    def test_unwraps_huble_response_to_openai_shape(self, chat, http):
        http.request.return_value = _mock_response(200, {
            "success": True,
            "content": "hello there",
            "tool_calls": None,
            "stop_reason": "stop",
            "provider_used": "melious",
            "model_used": "deepseek-v3.2",
            "input_tokens": 7,
            "output_tokens": 3,
            "tokens_used": 10,
            "cost_usd": 0.00012,
        })

        resp = chat.completions.create(
            model="deepseek-v3.2",
            messages=[{"role": "user", "content": "hi"}],
        )

        assert isinstance(resp, ChatCompletion)
        assert resp.choices[0].message.role == "assistant"
        assert resp.choices[0].message.content == "hello there"
        assert resp.choices[0].message.tool_calls is None
        assert resp.choices[0].finish_reason == "stop"
        assert resp.usage.prompt_tokens == 7
        assert resp.usage.completion_tokens == 3
        assert resp.usage.total_tokens == 10
        assert resp.cost_usd == 0.00012
        assert resp.provider_used == "melious"
        assert resp.model == "deepseek-v3.2"

    def test_already_openai_shape_passes_through(self, chat, http):
        # If backend ever returns OpenAI shape directly, we should not double-wrap.
        http.request.return_value = _mock_response(200, {
            "id": "chatcmpl-x", "object": "chat.completion",
            "created": 1234, "model": "gpt-4o-mini",
            "choices": [{"index": 0,
                         "message": {"role": "assistant", "content": "hi"},
                         "finish_reason": "stop"}],
            "usage": {"prompt_tokens": 1, "completion_tokens": 2, "total_tokens": 3},
        })

        resp = chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": "hi"}],
        )
        assert resp.id == "chatcmpl-x"
        assert resp.choices[0].message.content == "hi"
        assert resp.usage.total_tokens == 3

    def test_url_headers_and_body_payload(self, chat, http):
        http.request.return_value = _mock_response(200, {
            "content": "ok", "stop_reason": "stop", "provider_used": "melious",
            "model_used": "deepseek-v3.2",
        })
        chat.completions.create(
            model="deepseek-v3.2",
            messages=[{"role": "user", "content": "hi"}],
            temperature=0.5,
            tools=[{"type": "function", "function": {"name": "f", "parameters": {}}}],
            tool_choice="auto",
        )

        args, kwargs = http.request.call_args
        assert args[0] == "POST"
        assert args[1].endswith("/api/v2/chat/completions")
        assert kwargs["headers"]["X-API-Key"] == "sk_test_1234567890abcdefghijklmnopqrstuvwxyz"
        sent = json.loads(kwargs["body"])
        assert sent["model"] == "deepseek-v3.2"
        assert sent["temperature"] == 0.5
        assert sent["tool_choice"] == "auto"
        assert sent["shape"] == "openai"  # forced by chat.completions
        assert sent["tools"][0]["function"]["name"] == "f"

    def test_provider_override_forwarded(self, chat, http):
        http.request.return_value = _mock_response(200, {"content":"ok","stop_reason":"stop"})
        chat.completions.create(
            messages=[{"role":"user","content":"x"}], provider="claude",
        )
        sent = json.loads(http.request.call_args.kwargs["body"])
        assert sent["provider"] == "claude"

    def test_extra_kwargs_forwarded_when_not_none(self, chat, http):
        http.request.return_value = _mock_response(200, {"content":"ok","stop_reason":"stop"})
        chat.completions.create(
            messages=[{"role":"user","content":"x"}],
            top_p=0.9, stop=["END"], response_format={"type": "json_object"},
            stream=None,  # None is dropped
        )
        sent = json.loads(http.request.call_args.kwargs["body"])
        assert sent["top_p"] == 0.9
        assert sent["stop"] == ["END"]
        assert sent["response_format"] == {"type": "json_object"}
        assert "stream" not in sent

    def test_tool_calls_attribute_access(self, chat, http):
        """NOCA's tool_adapter_openai walks .tool_calls[i].function.name —
        verify we actually expose that nested attribute path."""
        http.request.return_value = _mock_response(200, {
            "content": "checking",
            "tool_calls": [{
                "id": "call_x", "type": "function",
                "function": {"name": "search", "arguments": '{"q":"hubble"}'},
            }],
            "stop_reason": "tool_calls",
            "model_used": "claude-haiku-4-5",
            "input_tokens": 5, "output_tokens": 3, "tokens_used": 8,
        })
        resp = chat.completions.create(
            model="claude-haiku-4-5",
            messages=[{"role":"user","content":"q"}],
            tools=[{"type":"function","function":{"name":"search","parameters":{}}}],
        )

        assert resp.choices[0].finish_reason == "tool_calls"
        msg = resp.choices[0].message
        assert hasattr(msg, "tool_calls")
        assert msg.tool_calls is not None
        tc = msg.tool_calls[0]
        assert tc.id == "call_x"
        assert tc.type == "function"
        assert tc.function.name == "search"
        assert json.loads(tc.function.arguments) == {"q": "hubble"}

    def test_tool_call_arguments_serialized_when_dict(self, chat, http):
        """OpenAI's SDK keeps arguments as a JSON string. If backend ever
        gives us a dict, we must re-serialize to a string for parity."""
        http.request.return_value = _mock_response(200, {
            "content": "x",
            "tool_calls": [{"id": "c1", "type": "function",
                            "function": {"name": "f", "arguments": {"a": 1}}}],
            "stop_reason": "tool_calls",
        })
        resp = chat.completions.create(
            model="x", messages=[{"role":"user","content":"q"}])
        args = resp.choices[0].message.tool_calls[0].function.arguments
        assert isinstance(args, str)
        assert json.loads(args) == {"a": 1}

    def test_dict_style_access(self, chat, http):
        http.request.return_value = _mock_response(200, {
            "content": "ok", "stop_reason": "stop",
            "input_tokens": 2, "output_tokens": 1, "tokens_used": 3,
        })
        resp = chat.completions.create(model="x", messages=[{"role":"user","content":"q"}])
        assert resp["usage"]["total_tokens"] == 3
        assert resp.get("nope", "default") == "default"
        dump = resp.model_dump()
        assert dump["usage"]["total_tokens"] == 3

    # ---- Error mapping --------------------------------------------------

    def test_401_authentication(self, chat, http):
        http.request.return_value = _mock_response(401, {"detail":"bad"})
        with pytest.raises(AuthenticationError):
            chat.completions.create(model="x", messages=[{"role":"user","content":"q"}])

    def test_404_not_found(self, chat, http):
        http.request.return_value = _mock_response(404, {"detail":"no"})
        with pytest.raises(NotFoundError):
            chat.completions.create(model="x", messages=[{"role":"user","content":"q"}])

    def test_422_validation(self, chat, http):
        http.request.return_value = _mock_response(422, {"detail":"bad shape"})
        with pytest.raises(ValidationError):
            chat.completions.create(model="x", messages=[{"role":"user","content":"q"}])

    def test_429_rate_limit(self, chat, http):
        http.request.return_value = _mock_response(
            429, {"detail":"slow"}, headers={"Retry-After":"45"})
        with pytest.raises(RateLimitError) as info:
            chat.completions.create(model="x", messages=[{"role":"user","content":"q"}])
        assert info.value.retry_after == 45

    def test_500_server(self, chat, http):
        http.request.return_value = _mock_response(500, {"detail":"boom"})
        with pytest.raises(ServerError):
            chat.completions.create(model="x", messages=[{"role":"user","content":"q"}])

    def test_invalid_json(self, chat, http):
        http.request.return_value = _mock_response(200, "<html>oops</html>")
        with pytest.raises(LLMHubError):
            chat.completions.create(model="x", messages=[{"role":"user","content":"q"}])
