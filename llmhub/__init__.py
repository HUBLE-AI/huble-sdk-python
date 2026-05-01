"""LLMHub Python SDK.

Official Python SDK for LLMHub - Unified access to 18+ AI providers.
"""

from llmhub.client import LLMHub
from llmhub.agent import AgentOperations, AgentChatResponse
from llmhub.chat import ChatOperations, ChatCompletion
from llmhub._shape import huble_to_openai_chat_completion
from llmhub.exceptions import (
    LLMHubError,
    AuthenticationError,
    RateLimitError,
    ProviderError,
    ValidationError,
    NotFoundError,
    ServerError,
    convert_api_exception,
)

__version__ = "0.2.0"
__all__ = [
    "LLMHub",
    "AgentOperations",
    "AgentChatResponse",
    "ChatOperations",
    "ChatCompletion",
    "huble_to_openai_chat_completion",
    "LLMHubError",
    "AuthenticationError",
    "RateLimitError",
    "ProviderError",
    "ValidationError",
    "NotFoundError",
    "ServerError",
    "convert_api_exception",
]
