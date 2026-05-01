"""Moderation operations wrapper for LLMHub SDK."""

from typing import Optional, List

from llmhub_generated.api.v2_moderation_api import V2ModerationApi
from llmhub_generated.models.v2_base_response import V2BaseResponse
from llmhub_generated.exceptions import ApiException

from llmhub.exceptions import (
    LLMHubError,
    AuthenticationError,
    RateLimitError,
    ValidationError,
    ServerError
)


class ModerationOperations:
    """
    Moderation operations for LLMHub API.

    Provides methods for content moderation, toxicity analysis,
    and content type detection.
    """

    def __init__(self, api_client, api_key: str):
        """
        Initialize ModerationOperations.

        Args:
            api_client: The API client instance from llmhub_generated
            api_key: The API key for authentication
        """
        self._api = V2ModerationApi(api_client)
        self._api_key = api_key

    def moderate(
        self,
        content: str,
        categories: Optional[List[str]] = None,
        provider: Optional[str] = None,
        model: Optional[str] = None
    ) -> V2BaseResponse:
        """
        Moderate content for policy violations.

        Args:
            content: Text content to moderate
            categories: Specific categories to check (e.g., ['hate', 'violence', 'sexual'])
            provider: Optional provider override
            model: Optional model override

        Returns:
            V2BaseResponse with moderation results

        Example:
            >>> response = client.moderation.moderate(
            ...     content="User-generated text to check",
            ...     categories=["hate", "harassment", "violence"]
            ... )
            >>> print(response.flagged)
        """
        try:
            request_data = {"content": content}
            if categories is not None:
                request_data["categories"] = categories
            if provider is not None:
                request_data["provider"] = provider
            if model is not None:
                request_data["model"] = model

            return self._api.moderate_content_api_v2_moderation_moderate_post(
                x_api_key=self._api_key,
                body=request_data
            )
        except ApiException as e:
            raise self._convert_exception(e)

    def detect(
        self,
        content: str,
        detection_types: Optional[List[str]] = None,
        provider: Optional[str] = None,
        model: Optional[str] = None
    ) -> V2BaseResponse:
        """
        Detect specific content types in text.

        Args:
            content: Text content to analyze
            detection_types: Types to detect (e.g., ['pii', 'spam', 'profanity'])
            provider: Optional provider override
            model: Optional model override

        Returns:
            V2BaseResponse with detection results

        Example:
            >>> response = client.moderation.detect(
            ...     content="Email me at john@example.com",
            ...     detection_types=["pii", "email"]
            ... )
        """
        try:
            request_data = {"content": content}
            if detection_types is not None:
                request_data["detection_types"] = detection_types
            if provider is not None:
                request_data["provider"] = provider
            if model is not None:
                request_data["model"] = model

            return self._api.detect_content_types_api_v2_moderation_detect_post(
                x_api_key=self._api_key,
                body=request_data
            )
        except ApiException as e:
            raise self._convert_exception(e)

    def analyze_toxicity(
        self,
        content: str,
        attributes: Optional[List[str]] = None,
        provider: Optional[str] = None,
        model: Optional[str] = None
    ) -> V2BaseResponse:
        """
        Analyze toxicity levels in content.

        Args:
            content: Text content to analyze
            attributes: Specific toxicity attributes (e.g., ['threat', 'insult', 'profanity'])
            provider: Optional provider override (e.g., 'perspective')
            model: Optional model override

        Returns:
            V2BaseResponse with toxicity scores

        Example:
            >>> response = client.moderation.analyze_toxicity(
            ...     content="Potentially toxic comment",
            ...     attributes=["toxicity", "severe_toxicity", "threat"]
            ... )
            >>> print(response.scores)
        """
        try:
            request_data = {"content": content}
            if attributes is not None:
                request_data["attributes"] = attributes
            if provider is not None:
                request_data["provider"] = provider
            if model is not None:
                request_data["model"] = model

            return self._api.analyze_toxicity_api_v2_moderation_analyze_toxicity_post(
                x_api_key=self._api_key,
                body=request_data
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
