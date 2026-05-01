"""Main LLMHub client."""

import os
from typing import Optional

from llmhub_generated import Configuration, ApiClient

from llmhub.exceptions import LLMHubError
from llmhub.text import TextOperations
from llmhub.embeddings import EmbeddingsOperations
from llmhub.document import DocumentOperations
from llmhub.audio import AudioOperations
from llmhub.video import VideoOperations
from llmhub.image import ImageOperations
from llmhub.moderation import ModerationOperations
from llmhub.enrichment import EnrichmentOperations
from llmhub.discovery import DiscoveryOperations
from llmhub.prompts import PromptOperations
from llmhub.data import DataOperations


# Sensible default for local-development HUBLE: backend listens on :4000.
# Earlier default was localhost:8000, which never matched a real HUBLE.
DEFAULT_BASE_URL = "http://localhost:4000"


class LLMHub:
    """Main LLMHub client for interacting with the LLMHub API.

    Available Operations:
        - text: Text generation, translation, summarization, etc.
        - embeddings: Generate vector embeddings for text
        - document: Parse, extract, and classify documents
        - audio: Transcribe, synthesize, enhance audio
        - video: Generate, describe, edit video
        - image: Generate, edit, analyze images
        - moderation: Content moderation and toxicity analysis
        - enrichment: B2B data enrichment (Hunter.io)
        - discovery: Discover available providers and models
        - prompts: Manage reusable prompt templates
        - data: Data operations (embed, rerank)

    Configuration precedence:
        1. Explicit constructor arguments
        2. Environment variables: ``LLMHUB_API_KEY``, ``LLMHUB_BASE_URL``
        3. Defaults (base_url only — api_key has no default)

    Example:
        >>> # Explicit
        >>> client = LLMHub(api_key="mgw_...", base_url="https://api.huble.app")
        >>>
        >>> # From environment
        >>> client = LLMHub()
        >>>
        >>> response = client.text.generate(prompt="Hello")
        >>> print(response.content, response.cost_usd)
    """

    def __init__(
        self,
        api_key: Optional[str] = None,
        base_url: Optional[str] = None,
    ):
        """Initialize LLMHub client.

        Args:
            api_key: Your LLMHub API key. If not provided, falls back to
                ``LLMHUB_API_KEY`` env var.
            base_url: Base URL for the LLMHub API. If not provided, falls back
                to ``LLMHUB_BASE_URL`` env var, then to ``http://localhost:4000``.

        Raises:
            ValueError: If api_key is empty (after env-var fallback).
        """
        api_key = api_key or os.environ.get("LLMHUB_API_KEY")
        base_url = base_url or os.environ.get("LLMHUB_BASE_URL") or DEFAULT_BASE_URL

        if not api_key or not isinstance(api_key, str) or len(api_key.strip()) == 0:
            raise ValueError(
                "API key is required: pass api_key= or set LLMHUB_API_KEY env var"
            )

        self.api_key = api_key
        self.base_url = base_url.rstrip("/")

        # Configure the generated urllib3-based client (used by existing wrappers).
        self.config = Configuration()
        self.config.host = self.base_url
        self._client = ApiClient(self.config)

        # Operation modules.
        self.text = TextOperations(self._client, self.api_key)
        self.embeddings = EmbeddingsOperations(self._client, self.api_key)
        self.document = DocumentOperations(self._client, self.api_key)
        self.audio = AudioOperations(self._client, self.api_key)
        self.video = VideoOperations(self._client, self.api_key)
        self.image = ImageOperations(self._client, self.api_key)
        self.moderation = ModerationOperations(self._client, self.api_key)
        self.enrichment = EnrichmentOperations(self._client, self.api_key)
        self.discovery = DiscoveryOperations(self._client, self.api_key)
        self.prompts = PromptOperations(self._client, self.api_key)
        self.data = DataOperations(self._client, self.api_key)

    def __repr__(self) -> str:
        return f"LLMHub(base_url='{self.base_url}')"
