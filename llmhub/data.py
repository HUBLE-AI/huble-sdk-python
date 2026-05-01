"""Data operations wrapper for LLMHub SDK."""

from typing import List, Optional

from llmhub_generated.api.v2_data_operations_api import V2DataOperationsApi
from llmhub_generated.models.v2_data_embed_request import V2DataEmbedRequest
from llmhub_generated.models.v2_data_rerank_request import V2DataRerankRequest
from llmhub_generated.models.v2_embeddings_response import V2EmbeddingsResponse
from llmhub_generated.models.v2_base_response import V2BaseResponse
from llmhub_generated.exceptions import ApiException

from llmhub.exceptions import (
    LLMHubError,
    AuthenticationError,
    RateLimitError,
    ValidationError,
    ServerError
)


class DataOperations:
    """
    Data operations for LLMHub API.

    Provides methods for generating embeddings and reranking documents.
    """

    def __init__(self, api_client, api_key: str):
        """
        Initialize DataOperations.

        Args:
            api_client: The API client instance from llmhub_generated
            api_key: The API key for authentication
        """
        self._api = V2DataOperationsApi(api_client)
        self._api_key = api_key

    def embed(
        self,
        texts: List[str],
        model: Optional[str] = None,
        provider: Optional[str] = None
    ) -> V2EmbeddingsResponse:
        """
        Generate embeddings for multiple texts.

        Note: This is an alias for embeddings.generate() for convenience.

        Args:
            texts: List of texts to embed
            model: Optional model override
            provider: Optional provider override

        Returns:
            V2EmbeddingsResponse with embeddings

        Example:
            >>> response = client.data.embed(
            ...     texts=["Document 1", "Document 2", "Document 3"]
            ... )
            >>> embeddings = response.embeddings
        """
        try:
            if not texts or not isinstance(texts, list):
                raise ValidationError("texts must be a non-empty list")
            if not all(isinstance(t, str) for t in texts):
                raise ValidationError("all items in texts must be strings")

            request = V2DataEmbedRequest(
                texts=texts,
                model=model,
                provider=provider
            )
            return self._api.generate_embeddings_api_v2_data_embed_post(
                x_api_key=self._api_key,
                v2_data_embed_request=request
            )
        except ApiException as e:
            raise self._convert_exception(e)
        except ValidationError:
            raise

    def rerank(
        self,
        query: str,
        documents: List[str],
        top_k: Optional[int] = None,
        provider: Optional[str] = None,
        model: Optional[str] = None
    ) -> V2BaseResponse:
        """
        Rerank documents based on relevance to a query.

        Args:
            query: Search query
            documents: List of document texts to rerank
            top_k: Number of top results to return
            provider: Optional provider override
            model: Optional model override

        Returns:
            V2BaseResponse with reranked documents

        Example:
            >>> response = client.data.rerank(
            ...     query="machine learning",
            ...     documents=["Doc about ML", "Doc about cooking", "Doc about AI"],
            ...     top_k=2
            ... )
            >>> for doc in response.ranked_documents:
            ...     print(f"{doc.text}: score={doc.score}")
        """
        try:
            request = V2DataRerankRequest(
                query=query,
                documents=documents,
                top_k=top_k,
                provider=provider,
                model=model
            )
            return self._api.rerank_documents_api_v2_data_rerank_post(
                x_api_key=self._api_key,
                v2_data_rerank_request=request
            )
        except ApiException as e:
            raise self._convert_exception(e)

    def _convert_exception(self, e: ApiException) -> Exception:
        """Convert API exceptions to SDK exceptions."""
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
