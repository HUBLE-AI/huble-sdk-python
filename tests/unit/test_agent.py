"""Unit tests for AgentOperations — mock urllib3.PoolManager, no I/O."""

from __future__ import annotations

import json
from unittest.mock import Mock

import pytest

from llmhub.agent import AgentOperations, AgentChatResponse
from llmhub.exceptions import (
    AuthenticationError,
    NotFoundError,
    RateLimitError,
    ServerError,
    ValidationError,
    LLMHubError,
)


def _mock_response(status: int, body: dict | str | None = None, headers: dict | None = None):
    """Build a fake urllib3 HTTPResponse exposing .status / .data / .headers."""
    resp = Mock()
    resp.status = status
    if isinstance(body, dict):
        resp.data = json.dumps(body).encode("utf-8")
    elif isinstance(body, str):
        resp.data = body.encode("utf-8")
    elif body is None:
        resp.data = b""
    else:
        resp.data = body
    resp.headers = headers or {}
    return resp


@pytest.fixture
def http():
    return Mock()


@pytest.fixture
def agent(http, mock_api_key, mock_base_url):
    return AgentOperations(mock_base_url, mock_api_key, http=http)


@pytest.mark.unit
class TestAgentChat:
    def test_minimal_request_posts_to_agent_chat(self, agent, http):
        http.request.return_value = _mock_response(200, {
            "success": True,
            "content": "hello",
            "tool_calls": None,
            "stop_reason": "stop",
            "provider_used": "melious",
            "model_used": "deepseek-v3.2",
            "input_tokens": 5,
            "output_tokens": 2,
            "tokens_used": 7,
            "cost_usd": 0.0001,
            "shape": "openai",
        })

        result = agent.chat(messages=[{"role": "user", "content": "hi"}])

        assert isinstance(result, AgentChatResponse)
        assert result.content == "hello"
        assert result.tool_calls is None
        assert result.stop_reason == "stop"
        assert result.provider_used == "melious"
        assert result.tokens_used == 7
        assert result.cost_usd == 0.0001

        # Verify URL + headers
        args, kwargs = http.request.call_args
        assert args[0] == "POST"
        assert args[1].endswith("/api/v2/agent/chat")
        assert kwargs["headers"]["X-API-Key"] == "sk_test_1234567890abcdefghijklmnopqrstuvwxyz"
        assert kwargs["headers"]["Content-Type"] == "application/json"

        sent = json.loads(kwargs["body"])
        assert sent == {"messages": [{"role": "user", "content": "hi"}], "max_tokens": 1024}

    def test_all_params_serialized(self, agent, http):
        http.request.return_value = _mock_response(200, {
            "stop_reason": "stop", "provider_used": "claude", "model_used": "claude-haiku-4-5",
        })

        agent.chat(
            messages=[{"role": "user", "content": "weather?"}],
            provider="claude",
            model="claude-haiku-4-5",
            tools=[{"type": "function", "function": {"name": "get_weather", "parameters": {}}}],
            tool_choice="auto",
            system="Be concise.",
            max_tokens=512,
            temperature=0.3,
            shape="openai",
            response_shape="anthropic",
            provider_options={"anthropic": {"thinking": {"type": "enabled"}}},
        )

        sent = json.loads(http.request.call_args.kwargs["body"])
        assert sent["provider"] == "claude"
        assert sent["model"] == "claude-haiku-4-5"
        assert sent["tools"][0]["function"]["name"] == "get_weather"
        assert sent["tool_choice"] == "auto"
        assert sent["system"] == "Be concise."
        assert sent["max_tokens"] == 512
        assert sent["temperature"] == 0.3
        assert sent["shape"] == "openai"
        assert sent["response_shape"] == "anthropic"
        assert sent["provider_options"]["anthropic"]["thinking"]["type"] == "enabled"

    def test_tool_calls_returned(self, agent, http):
        http.request.return_value = _mock_response(200, {
            "content": "checking",
            "tool_calls": [{
                "id": "call_x",
                "type": "function",
                "function": {"name": "get_weather", "arguments": '{"city":"Hamburg"}'},
            }],
            "stop_reason": "tool_calls",
            "provider_used": "claude",
            "model_used": "claude-haiku-4-5",
        })

        result = agent.chat(
            messages=[{"role": "user", "content": "weather?"}],
            tools=[{"type": "function", "function": {"name": "get_weather", "parameters": {}}}],
        )

        assert result.stop_reason == "tool_calls"
        assert result.tool_calls[0]["id"] == "call_x"
        assert result.tool_calls[0]["function"]["name"] == "get_weather"

    def test_anthropic_shape_response(self, agent, http):
        http.request.return_value = _mock_response(200, {
            "content": [
                {"type": "text", "text": "checking"},
                {"type": "tool_use", "id": "tu_1", "name": "search", "input": {"q": "hubble"}},
            ],
            "tool_calls": None,
            "stop_reason": "tool_use",
            "provider_used": "claude",
            "model_used": "claude-haiku-4-5",
            "shape": "anthropic",
        })

        result = agent.chat(
            messages=[{"role": "user", "content": [{"type": "text", "text": "hi"}]}],
            response_shape="anthropic",
        )

        assert result.shape == "anthropic"
        assert isinstance(result.content, list)
        assert result.content[1]["type"] == "tool_use"
        assert result.tool_calls is None

    # ---- Error mapping --------------------------------------------------

    def test_401_raises_authentication_error(self, agent, http):
        http.request.return_value = _mock_response(401, {"detail": "bad key"})
        with pytest.raises(AuthenticationError):
            agent.chat(messages=[{"role": "user", "content": "hi"}])

    def test_403_raises_authentication_error(self, agent, http):
        http.request.return_value = _mock_response(403, {"detail": "forbidden"})
        with pytest.raises(AuthenticationError):
            agent.chat(messages=[{"role": "user", "content": "hi"}])

    def test_404_raises_not_found(self, agent, http):
        http.request.return_value = _mock_response(404, {"detail": "no route"})
        with pytest.raises(NotFoundError):
            agent.chat(messages=[{"role": "user", "content": "hi"}])

    def test_422_raises_validation_error(self, agent, http):
        http.request.return_value = _mock_response(422, {"detail": "bad shape"})
        with pytest.raises(ValidationError):
            agent.chat(messages=[{"role": "user", "content": "hi"}])

    def test_429_raises_rate_limit_with_retry_after(self, agent, http):
        http.request.return_value = _mock_response(
            429, {"detail": "throttled"}, headers={"Retry-After": "30"},
        )
        with pytest.raises(RateLimitError) as exc_info:
            agent.chat(messages=[{"role": "user", "content": "hi"}])
        assert exc_info.value.retry_after == 30

    def test_500_raises_server_error(self, agent, http):
        http.request.return_value = _mock_response(500, {"detail": "boom"})
        with pytest.raises(ServerError):
            agent.chat(messages=[{"role": "user", "content": "hi"}])

    def test_invalid_json_raises_llmhub_error(self, agent, http):
        http.request.return_value = _mock_response(200, "<html>not json</html>")
        with pytest.raises(LLMHubError):
            agent.chat(messages=[{"role": "user", "content": "hi"}])

    def test_network_error_raises_typed_exception(self, agent, http):
        from urllib3.exceptions import HTTPError
        http.request.side_effect = HTTPError("connection reset")
        with pytest.raises(LLMHubError):
            agent.chat(messages=[{"role": "user", "content": "hi"}])


@pytest.mark.unit
class TestAgentChatResponse:
    def test_attribute_access_and_dict_lookup(self):
        raw = {
            "success": True,
            "content": "hello world",
            "tool_calls": None,
            "stop_reason": "stop",
            "provider_used": "melious",
            "model_used": "deepseek-v3.2",
            "input_tokens": 10,
            "output_tokens": 4,
            "tokens_used": 14,
            "cost_usd": 0.00012,
            "generation_time_ms": 800,
            "log_id": "550e8400-e29b-41d4-a716-446655440000",
            "provider_metadata": {"environment_impact": {"co2_g": 0.4}},
            "shape": "openai",
        }
        r = AgentChatResponse(raw)
        assert r.content == "hello world"
        assert r.cost_usd == 0.00012
        assert r["provider_metadata"]["environment_impact"]["co2_g"] == 0.4
        assert r.get("missing", "default") == "default"
        assert "AgentChatResponse(" in repr(r)

    def test_defaults_on_missing_fields(self):
        r = AgentChatResponse({})
        assert r.content is None
        assert r.tool_calls is None
        assert r.stop_reason == "stop"
        assert r.input_tokens == 0
        assert r.cost_usd == 0.0
        assert r.shape == "openai"
