"""Discovery operations wrapper for LLMHub SDK."""

from typing import Optional

from llmhub_generated.api.v2_discovery_api import V2DiscoveryApi
from llmhub_generated.exceptions import ApiException

from llmhub.exceptions import (
    LLMHubError,
    AuthenticationError,
    RateLimitError,
    ServerError
)


class DiscoveryOperations:
    """
    Discovery operations for LLMHub API.

    Provides methods to discover available providers, models, and the full catalog.
    """

    def __init__(self, api_client, api_key: str):
        """
        Initialize DiscoveryOperations.

        Args:
            api_client: The API client instance from llmhub_generated
            api_key: The API key for authentication
        """
        self._api = V2DiscoveryApi(api_client)
        self._api_key = api_key

    def get_catalog(self):
        """
        Get the complete catalog of available providers and models.

        Returns the full catalog including all providers, their models,
        capabilities, and pricing information.

        Returns:
            Complete catalog response with providers and models

        Raises:
            AuthenticationError: Invalid API key
            LLMHubError: Other API errors

        Example:
            >>> catalog = client.discovery.get_catalog()
            >>> for provider in catalog.providers:
            ...     print(f"{provider.name}: {len(provider.models)} models")
        """
        try:
            return self._api.get_catalog_api_v2_discovery_catalog_get(
                x_api_key=self._api_key
            )
        except ApiException as e:
            raise convert_api_exception(e)

    def get_providers(self):
        """
        Get list of available providers.

        Returns:
            List of available providers

        Raises:
            AuthenticationError: Invalid API key
            LLMHubError: Other API errors

        Example:
            >>> providers = client.discovery.get_providers()
            >>> for provider in providers:
            ...     print(f"{provider.name}: {provider.description}")
        """
        try:
            return self._api.get_providers_api_v2_discovery_providers_get(
                x_api_key=self._api_key,
            )
        except ApiException as e:
            raise convert_api_exception(e)

    def get_models(
        self,
        provider: Optional[str] = None,
        model_type: Optional[str] = None,
    ):
        """
        Get list of available models.

        Args:
            provider: Filter by provider name (e.g., 'claude', 'openai').
            model_type: Filter by model type (e.g., 'text', 'image', 'audio').

        Returns:
            List of available models with pricing and capabilities

        Raises:
            AuthenticationError: Invalid API key
            LLMHubError: Other API errors

        Example:
            >>> models = client.discovery.get_models(
            ...     provider="claude",
            ...     model_type="text",
            ... )
            >>> for model in models:
            ...     print(f"{model.name}: ${model.price_per_1k_tokens}")
        """
        try:
            return self._api.get_models_api_v2_discovery_models_get(
                x_api_key=self._api_key,
                provider=provider,
                model_type=model_type,
            )
        except ApiException as e:
            raise convert_api_exception(e)

