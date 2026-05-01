"""Video operations wrapper for LLMHub SDK."""

from typing import Optional

from llmhub_generated.api.v2_video_operations_api import V2VideoOperationsApi
from llmhub_generated.models.v2_video_generate_request import V2VideoGenerateRequest
from llmhub_generated.models.v2_video_describe_request import V2VideoDescribeRequest
from llmhub_generated.models.v2_video_extend_request import V2VideoExtendRequest
from llmhub_generated.models.v2_video_interpolate_request import V2VideoInterpolateRequest
from llmhub_generated.models.v2_video_remix_request import V2VideoRemixRequest
from llmhub_generated.models.v2_base_response import V2BaseResponse
from llmhub_generated.exceptions import ApiException

from llmhub.exceptions import (
    LLMHubError,
    AuthenticationError,
    RateLimitError,
    ValidationError,
    ServerError
)


class VideoOperations:
    """
    Video operations for LLMHub API.

    Provides methods for video generation, editing, description,
    and project management.
    """

    def __init__(self, api_client, api_key: str):
        """
        Initialize VideoOperations.

        Args:
            api_client: The API client instance from llmhub_generated
            api_key: The API key for authentication
        """
        self._api = V2VideoOperationsApi(api_client)
        self._api_key = api_key

    def generate(
        self,
        prompt: str,
        prompt_image: Optional[str] = None,
        duration: Optional[int] = None,
        aspect_ratio: Optional[str] = None,
        include_audio: Optional[bool] = None,
        provider: Optional[str] = None,
        model: Optional[str] = None,
        max_tokens: Optional[int] = None,
        temperature: Optional[float] = None
    ) -> V2BaseResponse:
        """
        Generate a video from text prompt and/or image.

        Args:
            prompt: Video generation prompt (10-5000 characters)
            prompt_image: Optional URL to image for video generation
            duration: Video duration in seconds (1-30)
            aspect_ratio: Video aspect ratio (e.g., '16:9', '9:16', '1:1')
            include_audio: Whether to include audio in the video
            provider: Optional provider override (e.g., 'runway', 'pika')
            model: Optional model override
            max_tokens: Maximum tokens for generation (100-16000)
            temperature: Sampling temperature (0.0-2.0)

        Returns:
            V2BaseResponse with video URL and metadata

        Example:
            >>> response = client.video.generate(
            ...     prompt="A serene mountain landscape with flowing water",
            ...     duration=10,
            ...     aspect_ratio="16:9",
            ...     include_audio=True
            ... )
            >>> print(response.video_url)
        """
        try:
            request = V2VideoGenerateRequest(
                prompt=prompt,
                prompt_image=prompt_image,
                duration=duration,
                aspect_ratio=aspect_ratio,
                include_audio=include_audio,
                provider=provider,
                model=model,
                max_tokens=max_tokens,
                temperature=temperature
            )
            return self._api.generate_video_api_v2_video_generate_post(
                x_api_key=self._api_key,
                v2_video_generate_request=request
            )
        except ApiException as e:
            raise self._convert_exception(e)

    def describe(
        self,
        video_url: str,
        detail_level: Optional[str] = None,
        provider: Optional[str] = None,
        model: Optional[str] = None
    ) -> V2BaseResponse:
        """
        Generate a text description of a video.

        Args:
            video_url: URL to the video to describe
            detail_level: Level of detail ('brief', 'detailed', 'comprehensive')
            provider: Optional provider override
            model: Optional model override

        Returns:
            V2BaseResponse with video description

        Example:
            >>> response = client.video.describe(
            ...     video_url="https://example.com/video.mp4",
            ...     detail_level="detailed"
            ... )
            >>> print(response.content)
        """
        try:
            request = V2VideoDescribeRequest(
                video_url=video_url,
                detail_level=detail_level,
                provider=provider,
                model=model
            )
            return self._api.describe_video_api_v2_video_describe_post(
                x_api_key=self._api_key,
                v2_video_describe_request=request
            )
        except ApiException as e:
            raise self._convert_exception(e)

    def clip(
        self,
        video_url: str,
        start_time: Optional[float] = None,
        end_time: Optional[float] = None,
        provider: Optional[str] = None,
        model: Optional[str] = None
    ) -> V2BaseResponse:
        """
        Create clips from a video.

        Args:
            video_url: URL to the source video
            start_time: Start time in seconds
            end_time: End time in seconds
            provider: Optional provider override
            model: Optional model override

        Returns:
            V2BaseResponse with clip URLs

        Example:
            >>> response = client.video.clip(
            ...     video_url="https://example.com/video.mp4",
            ...     start_time=10.5,
            ...     end_time=25.0
            ... )
            >>> print(response.clip_url)
        """
        try:
            # Note: Request model will be inferred from API spec
            # Using dynamic request construction
            request_data = {
                "video_url": video_url,
                "provider": provider,
                "model": model
            }
            if start_time is not None:
                request_data["start_time"] = start_time
            if end_time is not None:
                request_data["end_time"] = end_time

            return self._api.create_video_clips_api_v2_video_clip_post(
                x_api_key=self._api_key,
                body=request_data
            )
        except ApiException as e:
            raise self._convert_exception(e)

    def extend(
        self,
        video_url: str,
        extension_duration: Optional[int] = None,
        direction: Optional[str] = None,
        provider: Optional[str] = None,
        model: Optional[str] = None
    ) -> V2BaseResponse:
        """
        Extend a video by generating additional frames.

        Args:
            video_url: URL to the video to extend
            extension_duration: Duration to extend in seconds
            direction: Extension direction ('forward', 'backward', 'both')
            provider: Optional provider override
            model: Optional model override

        Returns:
            V2BaseResponse with extended video URL

        Example:
            >>> response = client.video.extend(
            ...     video_url="https://example.com/video.mp4",
            ...     extension_duration=5,
            ...     direction="forward"
            ... )
        """
        try:
            request = V2VideoExtendRequest(
                video_url=video_url,
                extension_duration=extension_duration,
                direction=direction,
                provider=provider,
                model=model
            )
            return self._api.extend_video_api_v2_video_extend_post(
                x_api_key=self._api_key,
                v2_video_extend_request=request
            )
        except ApiException as e:
            raise self._convert_exception(e)

    def interpolate(
        self,
        video_url: str,
        target_fps: Optional[int] = None,
        provider: Optional[str] = None,
        model: Optional[str] = None
    ) -> V2BaseResponse:
        """
        Interpolate video frames for smoother playback.

        Args:
            video_url: URL to the video to interpolate
            target_fps: Target frames per second
            provider: Optional provider override
            model: Optional model override

        Returns:
            V2BaseResponse with interpolated video URL

        Example:
            >>> response = client.video.interpolate(
            ...     video_url="https://example.com/video.mp4",
            ...     target_fps=60
            ... )
        """
        try:
            request = V2VideoInterpolateRequest(
                video_url=video_url,
                target_fps=target_fps,
                provider=provider,
                model=model
            )
            return self._api.interpolate_video_api_v2_video_interpolate_post(
                x_api_key=self._api_key,
                v2_video_interpolate_request=request
            )
        except ApiException as e:
            raise self._convert_exception(e)

    def remix(
        self,
        video_url: str,
        remix_prompt: Optional[str] = None,
        remix_strength: Optional[float] = None,
        provider: Optional[str] = None,
        model: Optional[str] = None
    ) -> V2BaseResponse:
        """
        Remix/transform a video with AI-guided modifications.

        Args:
            video_url: URL to the video to remix
            remix_prompt: Text prompt describing desired changes
            remix_strength: Strength of remix transformation (0.0-1.0)
            provider: Optional provider override
            model: Optional model override

        Returns:
            V2BaseResponse with remixed video URL

        Example:
            >>> response = client.video.remix(
            ...     video_url="https://example.com/video.mp4",
            ...     remix_prompt="Make it look like a vintage film",
            ...     remix_strength=0.7
            ... )
        """
        try:
            request = V2VideoRemixRequest(
                video_url=video_url,
                remix_prompt=remix_prompt,
                remix_strength=remix_strength,
                provider=provider,
                model=model
            )
            return self._api.remix_video_api_v2_video_remix_post(
                x_api_key=self._api_key,
                v2_video_remix_request=request
            )
        except ApiException as e:
            raise self._convert_exception(e)

    def get_project_clips(
        self,
        project_id: str
    ) -> V2BaseResponse:
        """
        Get all clips for a video project.

        Args:
            project_id: The project ID to retrieve clips for

        Returns:
            V2BaseResponse with project clips

        Example:
            >>> response = client.video.get_project_clips(
            ...     project_id="proj_12345"
            ... )
            >>> for clip in response.clips:
            ...     print(f"{clip.name}: {clip.url}")
        """
        try:
            return self._api.get_project_clips_api_v2_video_clips_project_id_get(
                x_api_key=self._api_key,
                project_id=project_id
            )
        except ApiException as e:
            raise self._convert_exception(e)

    def share_project(
        self,
        project_id: str,
        share_settings: Optional[dict] = None
    ) -> V2BaseResponse:
        """
        Share a video project with specific settings.

        Args:
            project_id: The project ID to share
            share_settings: Optional sharing settings (permissions, expiration, etc.)

        Returns:
            V2BaseResponse with share link and settings

        Example:
            >>> response = client.video.share_project(
            ...     project_id="proj_12345",
            ...     share_settings={"public": True, "allow_download": False}
            ... )
            >>> print(response.share_url)
        """
        try:
            request_data = {"share_settings": share_settings} if share_settings else {}
            return self._api.share_project_api_v2_video_share_project_id_post(
                x_api_key=self._api_key,
                project_id=project_id,
                body=request_data
            )
        except ApiException as e:
            raise self._convert_exception(e)

    def handle_webhook(
        self,
        webhook_data: dict
    ) -> V2BaseResponse:
        """
        Handle video processing webhooks from providers.

        Args:
            webhook_data: Webhook payload data from video provider

        Returns:
            V2BaseResponse with acknowledgment

        Example:
            >>> # Typically called by video provider callback
            >>> response = client.video.handle_webhook(
            ...     webhook_data={"event": "video.completed", "project_id": "proj_12345"}
            ... )
        """
        try:
            return self._api.handle_webhook_api_v2_video_webhook_post(
                x_api_key=self._api_key,
                body=webhook_data
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
