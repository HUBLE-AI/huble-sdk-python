"""Prompt library operations wrapper for LLMHub SDK."""

from typing import Optional, Dict, Any

from llmhub_generated.api.v2_prompt_library_api import V2PromptLibraryApi
from llmhub_generated.models.v2_base_response import V2BaseResponse
from llmhub_generated.exceptions import ApiException

from llmhub.exceptions import (
    LLMHubError,
    AuthenticationError,
    RateLimitError,
    ValidationError,
    ServerError,
    NotFoundError
)


class PromptOperations:
    """
    Prompt library operations for LLMHub API.

    Provides methods for creating, managing, and testing
    reusable prompt templates with version control.
    """

    def __init__(self, api_client, api_key: str):
        """
        Initialize PromptOperations.

        Args:
            api_client: The API client instance from llmhub_generated
            api_key: The API key for authentication
        """
        self._api = V2PromptLibraryApi(api_client)
        self._api_key = api_key

    def create_template(
        self,
        name: str,
        template_text: str,
        description: Optional[str] = None,
        variables: Optional[Dict[str, Any]] = None,
        tags: Optional[list] = None,
        is_public: bool = False
    ) -> V2BaseResponse:
        """
        Create a new prompt template.

        Args:
            name: Template name (unique identifier)
            template_text: The prompt template text with {variable} placeholders
            description: Template description
            variables: Variable definitions with types and defaults
            tags: Tags for categorization
            is_public: Whether template is public (visible to all) or private

        Returns:
            V2BaseResponse with created template data including template_id

        Example:
            >>> response = client.prompts.create_template(
            ...     name="product_description",
            ...     template_text="Write a {tone} product description for {product_name}",
            ...     description="Generate product descriptions",
            ...     variables={"tone": "professional", "product_name": ""},
            ...     tags=["marketing", "e-commerce"]
            ... )
            >>> print(f"Template created: {response.template_id}")
        """
        try:
            request_data = {
                "name": name,
                "template_text": template_text,
                "is_public": is_public
            }
            if description:
                request_data["description"] = description
            if variables:
                request_data["variables"] = variables
            if tags:
                request_data["tags"] = tags

            return self._api.create_template_api_v2_prompts_post(
                x_api_key=self._api_key,
                body=request_data
            )
        except ApiException as e:
            raise convert_api_exception(e)

    def get_template(
        self,
        template_id: str
    ) -> V2BaseResponse:
        """
        Get a prompt template by ID.

        Args:
            template_id: The template ID to retrieve

        Returns:
            V2BaseResponse with template data

        Example:
            >>> response = client.prompts.get_template(
            ...     template_id="tmpl_12345"
            ... )
            >>> print(f"{response.name}: {response.template_text}")
        """
        try:
            return self._api.get_template_api_v2_prompts_template_id_get(
                x_api_key=self._api_key,
                template_id=template_id
            )
        except ApiException as e:
            raise convert_api_exception(e)

    def list_templates(
        self,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        tags: Optional[list] = None,
        is_public: Optional[bool] = None
    ) -> V2BaseResponse:
        """
        List all prompt templates with optional filtering.

        Args:
            limit: Maximum number of results
            offset: Pagination offset
            tags: Filter by tags
            is_public: Filter by public/private status

        Returns:
            V2BaseResponse with list of templates

        Example:
            >>> response = client.prompts.list_templates(
            ...     tags=["marketing"],
            ...     limit=50
            ... )
            >>> for template in response.templates:
            ...     print(f"{template.name} ({template.usage_count} uses)")
        """
        try:
            params = {}
            if limit is not None:
                params["limit"] = limit
            if offset is not None:
                params["offset"] = offset
            if tags:
                params["tags"] = tags
            if is_public is not None:
                params["is_public"] = is_public

            return self._api.list_templates_api_v2_prompts_get(
                x_api_key=self._api_key,
                **params
            )
        except ApiException as e:
            raise convert_api_exception(e)

    def update_template(
        self,
        template_id: str,
        name: Optional[str] = None,
        template_text: Optional[str] = None,
        description: Optional[str] = None,
        variables: Optional[Dict[str, Any]] = None,
        tags: Optional[list] = None,
        is_public: Optional[bool] = None
    ) -> V2BaseResponse:
        """
        Update an existing prompt template.

        Creates a new version while preserving history.

        Args:
            template_id: The template ID to update
            name: Updated template name
            template_text: Updated template text
            description: Updated description
            variables: Updated variable definitions
            tags: Updated tags
            is_public: Updated public/private status

        Returns:
            V2BaseResponse with updated template data

        Example:
            >>> response = client.prompts.update_template(
            ...     template_id="tmpl_12345",
            ...     template_text="Write a {tone} and {length} product description for {product_name}",
            ...     variables={"tone": "professional", "length": "brief", "product_name": ""}
            ... )
            >>> print(f"Template updated to version {response.version}")
        """
        try:
            request_data = {}
            if name:
                request_data["name"] = name
            if template_text:
                request_data["template_text"] = template_text
            if description:
                request_data["description"] = description
            if variables:
                request_data["variables"] = variables
            if tags:
                request_data["tags"] = tags
            if is_public is not None:
                request_data["is_public"] = is_public

            return self._api.update_template_api_v2_prompts_template_id_put(
                x_api_key=self._api_key,
                template_id=template_id,
                body=request_data
            )
        except ApiException as e:
            raise convert_api_exception(e)

    def delete_template(
        self,
        template_id: str
    ) -> V2BaseResponse:
        """
        Delete a prompt template.

        Args:
            template_id: The template ID to delete

        Returns:
            V2BaseResponse with deletion confirmation

        Example:
            >>> response = client.prompts.delete_template(
            ...     template_id="tmpl_12345"
            ... )
            >>> print(f"Template deleted: {response.success}")
        """
        try:
            return self._api.delete_template_api_v2_prompts_template_id_delete(
                x_api_key=self._api_key,
                template_id=template_id
            )
        except ApiException as e:
            raise convert_api_exception(e)

    def list_template_versions(
        self,
        template_id: str
    ) -> V2BaseResponse:
        """
        List all versions of a prompt template.

        Args:
            template_id: The template ID to get versions for

        Returns:
            V2BaseResponse with list of template versions

        Example:
            >>> response = client.prompts.list_template_versions(
            ...     template_id="tmpl_12345"
            ... )
            >>> for version in response.versions:
            ...     print(f"v{version.version}: {version.created_at} ({version.usage_count} uses)")
        """
        try:
            return self._api.list_template_versions_api_v2_prompts_template_id_versions_get(
                x_api_key=self._api_key,
                template_id=template_id
            )
        except ApiException as e:
            raise convert_api_exception(e)

    def test_template(
        self,
        template_id: str,
        variables: Dict[str, Any],
        provider: Optional[str] = None,
        model: Optional[str] = None,
        max_tokens: Optional[int] = None,
        temperature: Optional[float] = None
    ) -> V2BaseResponse:
        """
        Test a prompt template with variable substitution.

        Renders the template with provided variables and optionally
        executes it against an LLM provider.

        Args:
            template_id: The template ID to test
            variables: Variable values for template substitution
            provider: Optional provider to execute test with (e.g., 'claude', 'openai')
            model: Optional model override
            max_tokens: Maximum tokens for generation
            temperature: Sampling temperature

        Returns:
            V2BaseResponse with rendered prompt and optional LLM response

        Example:
            >>> response = client.prompts.test_template(
            ...     template_id="tmpl_12345",
            ...     variables={"tone": "enthusiastic", "product_name": "SmartWidget Pro"},
            ...     provider="claude",
            ...     max_tokens=500
            ... )
            >>> print(f"Rendered: {response.rendered_prompt}")
            >>> print(f"Output: {response.content}")
        """
        try:
            request_data = {"variables": variables}
            if provider:
                request_data["provider"] = provider
            if model:
                request_data["model"] = model
            if max_tokens is not None:
                request_data["max_tokens"] = max_tokens
            if temperature is not None:
                request_data["temperature"] = temperature

            return self._api.test_template_api_v2_prompts_template_id_test_post(
                x_api_key=self._api_key,
                template_id=template_id,
                body=request_data
            )
        except ApiException as e:
            raise convert_api_exception(e)

