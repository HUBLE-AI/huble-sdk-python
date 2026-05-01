"""Audio operations wrapper for LLMHub SDK."""

from typing import Optional

from llmhub_generated.api.v2_audio_operations_api import V2AudioOperationsApi
from llmhub_generated.models.v2_base_response import V2BaseResponse
from llmhub_generated.exceptions import ApiException

from llmhub.exceptions import (
    LLMHubError,
    AuthenticationError,
    RateLimitError,
    ValidationError,
    ServerError
)


class AudioOperations:
    """
    Audio operations for LLMHub API.

    Provides methods for audio transcription, synthesis (TTS),
    enhancement, and source separation.
    """

    def __init__(self, api_client, api_key: str):
        """
        Initialize AudioOperations.

        Args:
            api_client: The API client instance from llmhub_generated
            api_key: The API key for authentication
        """
        self._api = V2AudioOperationsApi(api_client)
        self._api_key = api_key

    def transcribe(
        self,
        audio_url: str,
        language: Optional[str] = None,
        provider: Optional[str] = None,
        model: Optional[str] = None
    ) -> V2BaseResponse:
        """
        Transcribe audio to text (Speech-to-Text).

        Args:
            audio_url: URL to the audio file to transcribe
            language: Language code for transcription (e.g., 'en', 'es')
            provider: Optional provider override (e.g., 'assemblyai', 'deepgram')
            model: Optional model override

        Returns:
            V2BaseResponse with transcribed text

        Example:
            >>> response = client.audio.transcribe(
            ...     audio_url="https://example.com/audio.mp3",
            ...     language="en"
            ... )
            >>> print(response.content)
        """
        try:
            request_data = {"audio_url": audio_url}
            if language is not None:
                request_data["language"] = language
            if provider is not None:
                request_data["provider"] = provider
            if model is not None:
                request_data["model"] = model

            return self._api.transcribe_audio_api_v2_audio_transcribe_post(
                x_api_key=self._api_key,
                body=request_data
            )
        except ApiException as e:
            raise self._convert_exception(e)

    def synthesize(
        self,
        text: str,
        voice: Optional[str] = None,
        language: Optional[str] = None,
        provider: Optional[str] = None,
        model: Optional[str] = None
    ) -> V2BaseResponse:
        """
        Synthesize text to speech (Text-to-Speech / TTS).

        Args:
            text: Text to convert to speech
            voice: Voice ID or name (provider-specific)
            language: Language code (e.g., 'en-US', 'es-ES')
            provider: Optional provider override (e.g., 'elevenlabs')
            model: Optional model override

        Returns:
            V2BaseResponse with audio URL

        Example:
            >>> response = client.audio.synthesize(
            ...     text="Hello, how are you today?",
            ...     voice="adam",
            ...     language="en-US"
            ... )
            >>> print(response.audio_url)
        """
        try:
            request_data = {"text": text}
            if voice is not None:
                request_data["voice"] = voice
            if language is not None:
                request_data["language"] = language
            if provider is not None:
                request_data["provider"] = provider
            if model is not None:
                request_data["model"] = model

            return self._api.synthesize_audio_api_v2_audio_synthesize_post(
                x_api_key=self._api_key,
                body=request_data
            )
        except ApiException as e:
            raise self._convert_exception(e)

    def enhance(
        self,
        audio_url: str,
        enhancement_type: Optional[str] = None,
        provider: Optional[str] = None,
        model: Optional[str] = None
    ) -> V2BaseResponse:
        """
        Enhance audio quality (noise reduction, clarity improvement).

        Args:
            audio_url: URL to the audio file to enhance
            enhancement_type: Type of enhancement (e.g., 'denoise', 'clarify', 'restore')
            provider: Optional provider override
            model: Optional model override

        Returns:
            V2BaseResponse with enhanced audio URL

        Example:
            >>> response = client.audio.enhance(
            ...     audio_url="https://example.com/noisy.mp3",
            ...     enhancement_type="denoise"
            ... )
        """
        try:
            request_data = {"audio_url": audio_url}
            if enhancement_type is not None:
                request_data["enhancement_type"] = enhancement_type
            if provider is not None:
                request_data["provider"] = provider
            if model is not None:
                request_data["model"] = model

            return self._api.enhance_audio_api_v2_audio_enhance_post(
                x_api_key=self._api_key,
                body=request_data
            )
        except ApiException as e:
            raise self._convert_exception(e)

    def separate(
        self,
        audio_url: str,
        separation_type: Optional[str] = None,
        provider: Optional[str] = None,
        model: Optional[str] = None
    ) -> V2BaseResponse:
        """
        Separate audio into individual sources (vocals, instruments, etc.).

        Args:
            audio_url: URL to the audio file to separate
            separation_type: Type of separation (e.g., 'vocals', 'drums', 'bass')
            provider: Optional provider override
            model: Optional model override

        Returns:
            V2BaseResponse with separated audio tracks

        Example:
            >>> response = client.audio.separate(
            ...     audio_url="https://example.com/song.mp3",
            ...     separation_type="vocals"
            ... )
        """
        try:
            request_data = {"audio_url": audio_url}
            if separation_type is not None:
                request_data["separation_type"] = separation_type
            if provider is not None:
                request_data["provider"] = provider
            if model is not None:
                request_data["model"] = model

            return self._api.separate_audio_api_v2_audio_separate_post(
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
