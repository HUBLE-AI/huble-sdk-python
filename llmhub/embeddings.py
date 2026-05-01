"""Embeddings operations wrapper for LLMHub SDK."""

from typing import List, Optional

from llmhub_generated.api.v2_embeddings_api import V2EmbeddingsApi
from llmhub_generated.models.v2_embeddings_request import V2EmbeddingsRequest
from llmhub_generated.models.v2_embeddings_response import V2EmbeddingsResponse
from llmhub_generated.exceptions import ApiException

from llmhub.exceptions import (
    LLMHubError,
    AuthenticationError,
    RateLimitError,
    ValidationError,
    ServerError
)


class EmbeddingsOperations:
    """
    Embeddings operations for LLMHub API.

    Provides methods for generating vector embeddings from text,
    useful for semantic search, similarity matching, and clustering.
    """

    def __init__(self, api_client, api_key: str):
        """
        Initialize EmbeddingsOperations.

        Args:
            api_client: The API client instance from llmhub_generated
            api_key: The API key for authentication
        """
        self._api = V2EmbeddingsApi(api_client)
        self._api_key = api_key

    def generate(
        self,
        texts: List[str],
        model: Optional[str] = None,
        provider: Optional[str] = None
    ) -> V2EmbeddingsResponse:
        """
        Generate vector embeddings for one or more texts.

        Embeddings are dense vector representations of text that capture
        semantic meaning, enabling similarity comparisons and semantic search.

        Args:
            texts: List of texts to generate embeddings for
            model: Optional model override (e.g., 'voyage-2', 'text-embedding-3-small')
            provider: Optional provider override (e.g., 'voyageai', 'openai', 'cohere')

        Returns:
            V2EmbeddingsResponse with embeddings array, dimensions, and metadata

        Raises:
            AuthenticationError: Invalid API key
            ValidationError: Invalid request parameters (e.g., empty texts)
            RateLimitError: Rate limit exceeded
            LLMHubError: Other API errors

        Example:
            >>> client = LLMHub(api_key="sk_...")
            >>> response = client.embeddings.generate(
            ...     texts=["Hello world", "Machine learning is great"],
            ...     model="voyage-2"
            ... )
            >>> print(f"Generated {len(response.embeddings)} embeddings")
            >>> print(f"Dimensions: {response.dimensions}")
            >>> print(f"Cost: ${response.cost_usd:.4f}")
            >>>
            >>> # Access individual embeddings
            >>> for i, embedding in enumerate(response.embeddings):
            ...     print(f"Text {i+1}: {len(embedding)} dimensions")

        Example (Single Text):
            >>> response = client.embeddings.generate(texts=["Hello world"])
            >>> embedding = response.embeddings[0]
            >>> # Use embedding for similarity search, clustering, etc.

        Example (Batch Processing):
            >>> texts = ["Text 1", "Text 2", "Text 3", ...]
            >>> response = client.embeddings.generate(texts=texts)
            >>> embeddings = response.embeddings
            >>> # Process batch of embeddings
        """
        try:
            # Validate inputs
            if not texts or not isinstance(texts, list):
                raise ValidationError("texts must be a non-empty list")

            if len(texts) == 0:
                raise ValidationError("texts list cannot be empty")

            if not all(isinstance(t, str) for t in texts):
                raise ValidationError("all items in texts must be strings")

            request = V2EmbeddingsRequest(
                texts=texts,
                model=model,
                provider=provider
            )
            return self._api.generate_embeddings_api_v2_embeddings_generate_post(
                x_api_key=self._api_key,
                v2_embeddings_request=request
            )
        except ApiException as e:
            raise self._convert_exception(e)
        except ValidationError:
            # Re-raise our validation errors
            raise

    def _convert_exception(self, e: ApiException) -> Exception:
        """
        Convert API exceptions to SDK exceptions.

        Args:
            e: ApiException from generated client

        Returns:
            Appropriate SDK exception
        """
        status = getattr(e, 'status', 500)
        message = str(e)

        if status == 401:
            return AuthenticationError("Invalid API key or authentication failed")
        elif status == 403:
            return AuthenticationError("Access forbidden - check API key permissions")
        elif status == 422:
            return ValidationError(f"Validation error: {message}")
        elif status == 429:
            retry_after = None
            if hasattr(e, 'headers') and 'Retry-After' in e.headers:
                try:
                    retry_after = int(e.headers['Retry-After'])
                except (ValueError, TypeError):
                    pass
            return RateLimitError("Rate limit exceeded", retry_after=retry_after)
        elif 500 <= status < 600:
            return ServerError(f"Server error: {message}")
        else:
            return LLMHubError(f"API error: {message}")
