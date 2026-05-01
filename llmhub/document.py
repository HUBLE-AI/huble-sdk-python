"""Document operations wrapper for LLMHub SDK."""

from typing import List, Optional

from llmhub_generated.api.v2_document_operations_api import V2DocumentOperationsApi
from llmhub_generated.models.v2_document_parse_request import V2DocumentParseRequest
from llmhub_generated.models.v2_document_extract_request import V2DocumentExtractRequest
from llmhub_generated.models.v2_document_classify_request import V2DocumentClassifyRequest
from llmhub_generated.models.v2_document_compare_request import V2DocumentCompareRequest
from llmhub_generated.models.v2_document_generate_request import V2DocumentGenerateRequest
from llmhub_generated.models.v2_document_structure_request import V2DocumentStructureRequest
from llmhub_generated.models.v2_base_response import V2BaseResponse
from llmhub_generated.exceptions import ApiException

from llmhub.exceptions import (
    LLMHubError,
    AuthenticationError,
    RateLimitError,
    ValidationError,
    ServerError
)


class DocumentOperations:
    """
    Document operations for LLMHub API.

    Provides methods for document parsing, extraction, classification,
    comparison, generation, and structuring.
    """

    def __init__(self, api_client, api_key: str):
        """
        Initialize DocumentOperations.

        Args:
            api_client: The API client instance from llmhub_generated
            api_key: The API key for authentication
        """
        self._api = V2DocumentOperationsApi(api_client)
        self._api_key = api_key

    def parse(
        self,
        document_url: str,
        provider: Optional[str] = None,
        model: Optional[str] = None
    ) -> V2BaseResponse:
        """
        Parse a document and extract its text content.

        Supports PDF, DOCX, TXT, and other common document formats.

        Args:
            document_url: URL to the document to parse
            provider: Optional provider override
            model: Optional model override

        Returns:
            V2BaseResponse with extracted text content

        Raises:
            AuthenticationError: Invalid API key
            ValidationError: Invalid document URL or unsupported format
            LLMHubError: Other API errors

        Example:
            >>> response = client.document.parse(
            ...     document_url="https://example.com/document.pdf"
            ... )
            >>> print(response.content)  # Extracted text
        """
        try:
            request = V2DocumentParseRequest(
                document_url=document_url,
                provider=provider,
                model=model
            )
            return self._api.parse_document_api_v2_document_parse_post(
                x_api_key=self._api_key,
                v2_document_parse_request=request
            )
        except ApiException as e:
            raise self._convert_exception(e)

    def extract(
        self,
        document_url: str,
        extract_types: Optional[List[str]] = None,
        provider: Optional[str] = None,
        model: Optional[str] = None
    ) -> V2BaseResponse:
        """
        Extract structured data from a document.

        Args:
            document_url: URL to the document to extract from
            extract_types: Types of data to extract (e.g., ['tables', 'images', 'metadata'])
            provider: Optional provider override
            model: Optional model override

        Returns:
            V2BaseResponse with extracted structured data

        Example:
            >>> response = client.document.extract(
            ...     document_url="https://example.com/report.pdf",
            ...     extract_types=["tables", "figures"]
            ... )
        """
        try:
            request = V2DocumentExtractRequest(
                document_url=document_url,
                extract_types=extract_types,
                provider=provider,
                model=model
            )
            return self._api.extract_from_document_api_v2_document_extract_post(
                x_api_key=self._api_key,
                v2_document_extract_request=request
            )
        except ApiException as e:
            raise self._convert_exception(e)

    def classify(
        self,
        document_url: str,
        categories: List[str],
        provider: Optional[str] = None,
        model: Optional[str] = None
    ) -> V2BaseResponse:
        """
        Classify a document into predefined categories.

        Args:
            document_url: URL to the document to classify
            categories: List of possible categories (required)
            provider: Optional provider override
            model: Optional model override

        Returns:
            V2BaseResponse with classification results

        Example:
            >>> response = client.document.classify(
            ...     document_url="https://example.com/contract.pdf",
            ...     categories=["contract", "invoice", "report", "other"]
            ... )
        """
        try:
            request = V2DocumentClassifyRequest(
                document_url=document_url,
                categories=categories,
                provider=provider,
                model=model
            )
            return self._api.classify_document_api_v2_document_classify_post(
                x_api_key=self._api_key,
                v2_document_classify_request=request
            )
        except ApiException as e:
            raise self._convert_exception(e)

    def compare(
        self,
        document_url1: str,
        document_url2: str,
        comparison_aspects: Optional[List[str]] = None,
        provider: Optional[str] = None,
        model: Optional[str] = None
    ) -> V2BaseResponse:
        """
        Compare two documents for similarities and differences.

        Args:
            document_url1: URL to first document
            document_url2: URL to second document
            comparison_aspects: Specific aspects to compare (e.g., ['content', 'structure'])
            provider: Optional provider override
            model: Optional model override

        Returns:
            V2BaseResponse with comparison results

        Example:
            >>> response = client.document.compare(
            ...     document_url1="https://example.com/v1.pdf",
            ...     document_url2="https://example.com/v2.pdf",
            ...     comparison_aspects=["content", "metadata"]
            ... )
        """
        try:
            # API expects document_urls as a list
            request = V2DocumentCompareRequest(
                document_urls=[document_url1, document_url2],
                comparison_aspects=comparison_aspects,
                provider=provider,
                model=model
            )
            return self._api.compare_documents_api_v2_document_compare_post(
                x_api_key=self._api_key,
                v2_document_compare_request=request
            )
        except ApiException as e:
            raise self._convert_exception(e)

    def generate(
        self,
        prompt: str,
        document_type: Optional[str] = None,
        provider: Optional[str] = None,
        model: Optional[str] = None
    ) -> V2BaseResponse:
        """
        Generate a document from a prompt.

        Args:
            prompt: Description of the document to generate
            document_type: Type of document (e.g., 'report', 'letter', 'memo')
            provider: Optional provider override
            model: Optional model override

        Returns:
            V2BaseResponse with generated document content

        Example:
            >>> response = client.document.generate(
            ...     prompt="Create a quarterly sales report",
            ...     document_type="report"
            ... )
        """
        try:
            request = V2DocumentGenerateRequest(
                prompt=prompt,
                document_type=document_type,
                provider=provider,
                model=model
            )
            return self._api.generate_document_api_v2_document_generate_post(
                x_api_key=self._api_key,
                v2_document_generate_request=request
            )
        except ApiException as e:
            raise self._convert_exception(e)

    def structure(
        self,
        document_url: str,
        structure_type: Optional[str] = None,
        provider: Optional[str] = None,
        model: Optional[str] = None
    ) -> V2BaseResponse:
        """
        Analyze and return the structure of a document.

        Args:
            document_url: URL to the document to structure
            structure_type: Type of structure to extract (e.g., 'outline', 'hierarchy')
            provider: Optional provider override
            model: Optional model override

        Returns:
            V2BaseResponse with document structure

        Example:
            >>> response = client.document.structure(
            ...     document_url="https://example.com/book.pdf",
            ...     structure_type="outline"
            ... )
        """
        try:
            request = V2DocumentStructureRequest(
                document_url=document_url,
                structure_type=structure_type,
                provider=provider,
                model=model
            )
            return self._api.structure_document_api_v2_document_structure_post(
                x_api_key=self._api_key,
                v2_document_structure_request=request
            )
        except ApiException as e:
            raise self._convert_exception(e)

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
