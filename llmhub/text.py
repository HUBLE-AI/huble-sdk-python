"""Text operations wrapper for LLMHub SDK."""

from typing import Optional, List

from llmhub_generated.api.v2_text_operations_api import V2TextOperationsApi
from llmhub_generated.models.v2_text_generate_request import V2TextGenerateRequest
from llmhub_generated.models.v2_text_translate_request import V2TextTranslateRequest
from llmhub_generated.models.v2_text_summarize_request import V2TextSummarizeRequest
from llmhub_generated.models.v2_text_rewrite_request import V2TextRewriteRequest
from llmhub_generated.models.v2_text_expand_request import V2TextExpandRequest
from llmhub_generated.models.v2_text_condense_request import V2TextCondenseRequest
from llmhub_generated.models.v2_text_analyze_request import V2TextAnalyzeRequest
from llmhub_generated.models.v2_text_classify_request import V2TextClassifyRequest
from llmhub_generated.models.v2_text_extract_request import V2TextExtractRequest
from llmhub_generated.models.v2_text_compare_request import V2TextCompareRequest
from llmhub_generated.models.v2_base_response import V2BaseResponse
from llmhub_generated.exceptions import ApiException

from llmhub.exceptions import (
    LLMHubError,
    AuthenticationError,
    RateLimitError,
    ProviderError,
    ValidationError,
    NotFoundError,
    ServerError
)


class TextOperations:
    """
    Text operations for LLMHub API.

    Provides methods for text generation, translation, summarization,
    analysis, and other text-based AI operations.
    """

    def __init__(self, api_client, api_key: str):
        """
        Initialize TextOperations.

        Args:
            api_client: The API client instance from llmhub_generated
            api_key: The API key for authentication
        """
        self._api = V2TextOperationsApi(api_client)
        self._api_key = api_key

    def generate(
        self,
        prompt: str,
        system_prompt: Optional[str] = None,
        provider: Optional[str] = None,
        model: Optional[str] = None,
        max_tokens: Optional[int] = None,
        temperature: Optional[float] = None
    ) -> V2BaseResponse:
        """
        Generate text from a prompt.

        Uses intelligent provider routing to select the best LLM provider
        automatically, or you can specify a provider and model.

        Args:
            prompt: The input prompt for text generation
            system_prompt: Optional system prompt for context
            provider: Optional provider override (e.g., 'claude', 'openai', 'groq')
            model: Optional model override (e.g., 'claude-3-5-sonnet-20241022')
            max_tokens: Maximum tokens to generate
            temperature: Temperature for generation (0.0-1.0)

        Returns:
            V2BaseResponse with generated content, cost, and metadata

        Raises:
            AuthenticationError: Invalid API key
            RateLimitError: Rate limit exceeded
            ProviderError: Provider-specific error
            ValidationError: Invalid request parameters
            LLMHubError: Other API errors

        Example:
            >>> client = LLMHub(api_key="sk_...")
            >>> response = client.text.generate(
            ...     prompt="Write a haiku about coding",
            ...     temperature=0.7
            ... )
            >>> print(response.content)
            >>> print(f"Cost: ${response.cost_usd:.4f}")
            >>> print(f"Provider: {response.provider_used}")
        """
        try:
            request = V2TextGenerateRequest(
                prompt=prompt,
                system_prompt=system_prompt,
                provider=provider,
                model=model,
                max_tokens=max_tokens,
                temperature=temperature
            )
            return self._api.generate_text_api_v2_text_generate_post(
                x_api_key=self._api_key,
                v2_text_generate_request=request
            )
        except ApiException as e:
            raise self._convert_exception(e)

    def translate(
        self,
        text: str,
        target_language: str,
        source_language: str = "auto",
        provider: Optional[str] = None,
        model: Optional[str] = None
    ) -> V2BaseResponse:
        """
        Translate text between languages.

        Args:
            text: Text to translate
            target_language: Target language code (e.g., 'es', 'fr', 'de', 'ja')
            source_language: Source language code (default: "auto" for auto-detection)
            provider: Optional provider override
            model: Optional model override

        Returns:
            V2BaseResponse with translated content

        Raises:
            AuthenticationError: Invalid API key
            ValidationError: Invalid language code or parameters
            LLMHubError: Other API errors

        Example:
            >>> response = client.text.translate(
            ...     text="Hello, how are you?",
            ...     target_language="es"
            ... )
            >>> print(response.content)  # "Hola, ¿cómo estás?"
        """
        try:
            request = V2TextTranslateRequest(
                text=text,
                target_language=target_language,
                source_language=source_language,
                provider=provider,
                model=model
            )
            return self._api.translate_text_api_v2_text_translate_post(
                x_api_key=self._api_key,
                v2_text_translate_request=request
            )
        except ApiException as e:
            raise self._convert_exception(e)

    def summarize(
        self,
        text: str,
        summary_length: Optional[str] = None,
        provider: Optional[str] = None,
        model: Optional[str] = None
    ) -> V2BaseResponse:
        """
        Summarize long text into a concise summary.

        Args:
            text: Text to summarize
            summary_length: Desired summary length ('short', 'medium', 'long')
            provider: Optional provider override
            model: Optional model override

        Returns:
            V2BaseResponse with summarized content

        Raises:
            AuthenticationError: Invalid API key
            ValidationError: Invalid parameters
            LLMHubError: Other API errors

        Example:
            >>> long_text = "..." # Long article
            >>> response = client.text.summarize(
            ...     text=long_text,
            ...     summary_length="short"
            ... )
            >>> print(response.content)
        """
        try:
            request = V2TextSummarizeRequest(
                text=text,
                summary_length=summary_length,
                provider=provider,
                model=model
            )
            return self._api.summarize_text_api_v2_text_summarize_post(
                x_api_key=self._api_key,
                v2_text_summarize_request=request
            )
        except ApiException as e:
            raise self._convert_exception(e)

    def rewrite(
        self,
        text: str,
        style: Optional[str] = None,
        provider: Optional[str] = None,
        model: Optional[str] = None
    ) -> V2BaseResponse:
        """
        Rewrite or paraphrase text.

        Args:
            text: Text to rewrite
            style: Desired style ('formal', 'casual', 'professional', 'creative')
            provider: Optional provider override
            model: Optional model override

        Returns:
            V2BaseResponse with rewritten content

        Example:
            >>> response = client.text.rewrite(
            ...     text="This is a test.",
            ...     style="formal"
            ... )
        """
        try:
            request = V2TextRewriteRequest(
                text=text,
                style=style,
                provider=provider,
                model=model
            )
            return self._api.rewrite_text_api_v2_text_rewrite_post(
                x_api_key=self._api_key,
                v2_text_rewrite_request=request
            )
        except ApiException as e:
            raise self._convert_exception(e)

    def expand(
        self,
        text: str,
        provider: Optional[str] = None,
        model: Optional[str] = None
    ) -> V2BaseResponse:
        """
        Expand brief text into more detailed content.

        Args:
            text: Brief text to expand
            provider: Optional provider override
            model: Optional model override

        Returns:
            V2BaseResponse with expanded content

        Example:
            >>> response = client.text.expand(
            ...     text="AI is transforming industries."
            ... )
        """
        try:
            request = V2TextExpandRequest(
                text=text,
                provider=provider,
                model=model
            )
            return self._api.expand_text_api_v2_text_expand_post(
                x_api_key=self._api_key,
                v2_text_expand_request=request
            )
        except ApiException as e:
            raise self._convert_exception(e)

    def condense(
        self,
        text: str,
        provider: Optional[str] = None,
        model: Optional[str] = None
    ) -> V2BaseResponse:
        """
        Condense text to key points.

        Args:
            text: Text to condense
            provider: Optional provider override
            model: Optional model override

        Returns:
            V2BaseResponse with condensed content

        Example:
            >>> response = client.text.condense(
            ...     text="Long detailed explanation..."
            ... )
        """
        try:
            request = V2TextCondenseRequest(
                text=text,
                provider=provider,
                model=model
            )
            return self._api.condense_text_api_v2_text_condense_post(
                x_api_key=self._api_key,
                v2_text_condense_request=request
            )
        except ApiException as e:
            raise self._convert_exception(e)

    def analyze(
        self,
        text: str,
        analysis_type: Optional[str] = None,
        provider: Optional[str] = None,
        model: Optional[str] = None
    ) -> V2BaseResponse:
        """
        Analyze text for sentiment, tone, entities, etc.

        Args:
            text: Text to analyze
            analysis_type: Type of analysis ('sentiment', 'tone', 'entities', 'all')
            provider: Optional provider override
            model: Optional model override

        Returns:
            V2BaseResponse with analysis results

        Example:
            >>> response = client.text.analyze(
            ...     text="I love this product!",
            ...     analysis_type="sentiment"
            ... )
        """
        try:
            request = V2TextAnalyzeRequest(
                text=text,
                analysis_type=analysis_type,
                provider=provider,
                model=model
            )
            return self._api.analyze_text_api_v2_text_analyze_post(
                x_api_key=self._api_key,
                v2_text_analyze_request=request
            )
        except ApiException as e:
            raise self._convert_exception(e)

    def classify(
        self,
        text: str,
        categories: List[str],
        provider: Optional[str] = None,
        model: Optional[str] = None
    ) -> V2BaseResponse:
        """
        Classify text into categories.

        Args:
            text: Text to classify
            categories: List of possible categories (required)
            provider: Optional provider override
            model: Optional model override

        Returns:
            V2BaseResponse with classification results

        Example:
            >>> response = client.text.classify(
            ...     text="This is a support ticket about billing",
            ...     categories=["billing", "technical", "general"]
            ... )
        """
        try:
            request = V2TextClassifyRequest(
                text=text,
                categories=categories,
                provider=provider,
                model=model
            )
            return self._api.classify_text_api_v2_text_classify_post(
                x_api_key=self._api_key,
                v2_text_classify_request=request
            )
        except ApiException as e:
            raise self._convert_exception(e)

    def extract(
        self,
        text: str,
        extract_types: Optional[List[str]] = None,
        provider: Optional[str] = None,
        model: Optional[str] = None
    ) -> V2BaseResponse:
        """
        Extract entities, keywords, or data from text.

        Args:
            text: Text to extract from
            extract_types: Types to extract ('entities', 'keywords', 'dates', 'all')
            provider: Optional provider override
            model: Optional model override

        Returns:
            V2BaseResponse with extracted data

        Example:
            >>> response = client.text.extract(
            ...     text="John Smith works at Acme Corp in New York.",
            ...     extract_types=["entities"]
            ... )
        """
        try:
            request = V2TextExtractRequest(
                text=text,
                extract_types=extract_types,
                provider=provider,
                model=model
            )
            return self._api.extract_from_text_api_v2_text_extract_post(
                x_api_key=self._api_key,
                v2_text_extract_request=request
            )
        except ApiException as e:
            raise self._convert_exception(e)

    def compare(
        self,
        text1: str,
        text2: str,
        comparison_aspects: Optional[List[str]] = None,
        provider: Optional[str] = None,
        model: Optional[str] = None
    ) -> V2BaseResponse:
        """
        Compare two texts for similarity, differences, etc.

        Args:
            text1: First text to compare
            text2: Second text to compare
            comparison_aspects: Specific aspects to compare (e.g., ['similarity', 'tone', 'style'])
            provider: Optional provider override
            model: Optional model override

        Returns:
            V2BaseResponse with comparison results

        Example:
            >>> response = client.text.compare(
            ...     text1="Original version",
            ...     text2="Modified version",
            ...     comparison_aspects=["differences", "similarity"]
            ... )
        """
        try:
            # API expects texts as a list
            request = V2TextCompareRequest(
                texts=[text1, text2],
                comparison_aspects=comparison_aspects,
                provider=provider,
                model=model
            )
            return self._api.compare_texts_api_v2_text_compare_post(
                x_api_key=self._api_key,
                v2_text_compare_request=request
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
        elif status == 404:
            return NotFoundError("Resource not found")
        elif status == 422:
            return ValidationError(f"Validation error: {message}")
        elif status == 429:
            # Extract retry_after from headers if available
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
