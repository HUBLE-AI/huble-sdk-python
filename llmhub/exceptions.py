"""Custom exceptions for LLMHub SDK."""

from typing import Optional


class LLMHubError(Exception):
    """Base exception for all LLMHub errors."""
    pass


class AuthenticationError(LLMHubError):
    """Invalid API key or authentication failure."""
    pass


class RateLimitError(LLMHubError):
    """Rate limit exceeded."""

    def __init__(self, message: str, retry_after: Optional[int] = None):
        """Initialize RateLimitError.

        Args:
            message: Error message
            retry_after: Seconds to wait before retrying (parsed from Retry-After header)
        """
        super().__init__(message)
        self.retry_after = retry_after


class ProviderError(LLMHubError):
    """Provider-specific error (a configured upstream LLM provider returned an error)."""
    pass


class ValidationError(LLMHubError):
    """Request validation error (4xx other than 401/403/404/429)."""
    pass


class NotFoundError(LLMHubError):
    """Resource not found error (404)."""
    pass


class ServerError(LLMHubError):
    """Server-side error (5xx)."""
    pass


def convert_api_exception(e) -> Exception:
    """Translate any API-layer exception to a typed LLMHub exception.

    Accepts either:
    - ``llmhub_generated.exceptions.ApiException`` (from the urllib3 generated layer)
    - ``urllib3.exceptions.HTTPError`` subclass (from direct calls in agent/chat modules)
    - any object with ``.status`` (int-like) and optionally ``.headers`` (mapping)

    Returns the appropriate SDK exception subclass, NEVER raises.

    Status → exception map:
        401, 403  → AuthenticationError
        404       → NotFoundError
        422       → ValidationError
        429       → RateLimitError(retry_after=…)  (parses Retry-After header)
        4xx other → ValidationError
        5xx       → ServerError
        anything  → LLMHubError
    """
    status = getattr(e, "status", None)
    if status is None:
        # urllib3.exceptions.HTTPError-style — try to dig out a code
        status = getattr(e, "code", None) or 500
    try:
        status = int(status)
    except (TypeError, ValueError):
        status = 500

    message = str(e) or "API error"

    if status in (401, 403):
        return AuthenticationError(
            "Invalid API key or insufficient permissions" if status == 401
            else f"Forbidden: {message}"
        )
    if status == 404:
        return NotFoundError(f"Not found: {message}")
    if status == 429:
        retry_after = None
        headers = getattr(e, "headers", None) or {}
        # `headers` may be a dict, urllib3 HTTPHeaderDict, or similar — both .get and __contains__ work.
        ra = headers.get("Retry-After") if hasattr(headers, "get") else None
        if ra is not None:
            try:
                retry_after = int(ra)
            except (TypeError, ValueError):
                pass
        return RateLimitError(f"Rate limit exceeded: {message}", retry_after=retry_after)
    if 400 <= status < 500:
        return ValidationError(f"Request validation error ({status}): {message}")
    if 500 <= status < 600:
        return ServerError(f"Server error ({status}): {message}")
    return LLMHubError(f"API error ({status}): {message}")
