"""Pure-function tests for llmhub/_shape.py."""

import pytest

from llmhub._shape import huble_to_openai_chat_completion


@pytest.mark.unit
class TestHubleToOpenaiChatCompletion:
    def test_idempotent_when_already_openai_shape(self):
        already = {
            "choices": [{"index": 0, "message": {"role": "assistant", "content": "hi"},
                         "finish_reason": "stop"}],
            "usage": {"prompt_tokens": 1, "completion_tokens": 2, "total_tokens": 3},
        }
        assert huble_to_openai_chat_completion(already) is already

    def test_unwraps_basic_response(self):
        raw = {
            "success": True,
            "content": "hello world",
            "tool_calls": None,
            "stop_reason": "stop",
            "provider_used": "melious",
            "model_used": "deepseek-v3.2",
            "input_tokens": 10,
            "output_tokens": 5,
            "tokens_used": 15,
            "cost_usd": 0.0001,
        }
        out = huble_to_openai_chat_completion(raw)

        assert out["object"] == "chat.completion"
        assert out["model"] == "deepseek-v3.2"
        assert out["choices"][0]["message"]["role"] == "assistant"
        assert out["choices"][0]["message"]["content"] == "hello world"
        assert "tool_calls" not in out["choices"][0]["message"]
        assert out["choices"][0]["finish_reason"] == "stop"
        assert out["usage"] == {
            "prompt_tokens": 10, "completion_tokens": 5, "total_tokens": 15,
        }
        # HUBLE-specific bookkeeping preserved
        assert out["cost_usd"] == 0.0001
        assert out["provider_used"] == "melious"

    def test_tool_calls_passed_through(self):
        raw = {
            "content": "checking",
            "tool_calls": [{
                "id": "call_x", "type": "function",
                "function": {"name": "get_weather", "arguments": '{"city":"Hamburg"}'},
            }],
            "stop_reason": "tool_calls",
            "model_used": "claude-haiku-4-5",
            "input_tokens": 20, "output_tokens": 8, "tokens_used": 28,
        }
        out = huble_to_openai_chat_completion(raw)

        msg = out["choices"][0]["message"]
        assert msg["content"] == "checking"
        assert msg["tool_calls"][0]["id"] == "call_x"
        assert msg["tool_calls"][0]["function"]["name"] == "get_weather"
        assert out["choices"][0]["finish_reason"] == "tool_calls"

    def test_empty_content_normalised_to_empty_string(self):
        raw = {"content": None, "stop_reason": "tool_calls"}
        out = huble_to_openai_chat_completion(raw)
        assert out["choices"][0]["message"]["content"] == ""

    def test_missing_stop_reason_defaults_to_stop(self):
        raw = {"content": "hi"}
        out = huble_to_openai_chat_completion(raw)
        assert out["choices"][0]["finish_reason"] == "stop"

    def test_missing_token_counts_default_to_zero(self):
        raw = {"content": "hi"}
        out = huble_to_openai_chat_completion(raw)
        assert out["usage"] == {
            "prompt_tokens": 0, "completion_tokens": 0, "total_tokens": 0,
        }

    def test_non_dict_input_returned_as_is(self):
        assert huble_to_openai_chat_completion(None) is None
        assert huble_to_openai_chat_completion("not a dict") == "not a dict"
        assert huble_to_openai_chat_completion(42) == 42
