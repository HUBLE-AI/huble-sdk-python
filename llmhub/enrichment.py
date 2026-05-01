"""B2B enrichment operations wrapper for LLMHub SDK."""

from typing import Optional, List

from llmhub_generated.api.v2_b2_b_enrichment_api import V2B2BEnrichmentApi
from llmhub_generated.models.v2_base_response import V2BaseResponse
from llmhub_generated.exceptions import ApiException

from llmhub.exceptions import (
    LLMHubError,
    AuthenticationError,
    RateLimitError,
    ValidationError,
    ServerError
)


class EnrichmentOperations:
    """
    B2B enrichment operations for LLMHub API.

    Provides methods for company/lead enrichment, email discovery,
    and lead management using Hunter.io and other B2B data providers.
    """

    def __init__(self, api_client, api_key: str):
        """
        Initialize EnrichmentOperations.

        Args:
            api_client: The API client instance from llmhub_generated
            api_key: The API key for authentication
        """
        self._api = V2B2BEnrichmentApi(api_client)
        self._api_key = api_key

    def enrich_company(
        self,
        domain: str,
        provider: Optional[str] = None
    ) -> V2BaseResponse:
        """
        Enrich company information from domain.

        Args:
            domain: Company domain (e.g., 'anthropic.com')
            provider: Optional provider override (e.g., 'hunter')

        Returns:
            V2BaseResponse with company data (name, industry, size, social profiles, etc.)

        Example:
            >>> response = client.enrichment.enrich_company(
            ...     domain="anthropic.com"
            ... )
            >>> print(f"{response.company_name} - {response.industry}")
        """
        try:
            request_data = {"domain": domain}
            if provider:
                request_data["provider"] = provider

            return self._api.enrich_company_api_v2_enrich_company_post(
                x_api_key=self._api_key,
                body=request_data
            )
        except ApiException as e:
            raise self._convert_exception(e)

    def enrich_lead(
        self,
        email: Optional[str] = None,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
        domain: Optional[str] = None,
        provider: Optional[str] = None
    ) -> V2BaseResponse:
        """
        Enrich lead/contact information.

        Args:
            email: Contact email address
            first_name: Contact first name
            last_name: Contact last name
            domain: Company domain
            provider: Optional provider override

        Returns:
            V2BaseResponse with enriched lead data

        Example:
            >>> response = client.enrichment.enrich_lead(
            ...     email="john@example.com"
            ... )
            >>> print(f"{response.first_name} {response.last_name} - {response.position}")
        """
        try:
            request_data = {}
            if email:
                request_data["email"] = email
            if first_name:
                request_data["first_name"] = first_name
            if last_name:
                request_data["last_name"] = last_name
            if domain:
                request_data["domain"] = domain
            if provider:
                request_data["provider"] = provider

            return self._api.enrich_lead_api_v2_enrich_lead_post(
                x_api_key=self._api_key,
                body=request_data
            )
        except ApiException as e:
            raise self._convert_exception(e)

    def find_email(
        self,
        domain: str,
        first_name: str,
        last_name: str,
        provider: Optional[str] = None
    ) -> V2BaseResponse:
        """
        Find email address for a person at a company.

        Args:
            domain: Company domain
            first_name: Person's first name
            last_name: Person's last name
            provider: Optional provider override (e.g., 'hunter')

        Returns:
            V2BaseResponse with email address and confidence score

        Example:
            >>> response = client.enrichment.find_email(
            ...     domain="anthropic.com",
            ...     first_name="Dario",
            ...     last_name="Amodei"
            ... )
            >>> print(f"Email: {response.email} (confidence: {response.score})")
        """
        try:
            request_data = {
                "domain": domain,
                "first_name": first_name,
                "last_name": last_name
            }
            if provider:
                request_data["provider"] = provider

            return self._api.find_email_api_v2_enrich_email_finder_post(
                x_api_key=self._api_key,
                body=request_data
            )
        except ApiException as e:
            raise self._convert_exception(e)

    def verify_email(
        self,
        email: str,
        provider: Optional[str] = None
    ) -> V2BaseResponse:
        """
        Verify if an email address is valid and deliverable.

        Args:
            email: Email address to verify
            provider: Optional provider override (e.g., 'hunter')

        Returns:
            V2BaseResponse with verification status and details

        Example:
            >>> response = client.enrichment.verify_email(
            ...     email="john@example.com"
            ... )
            >>> print(f"Valid: {response.valid}, Status: {response.status}")
        """
        try:
            request_data = {"email": email}
            if provider:
                request_data["provider"] = provider

            return self._api.verify_email_api_v2_enrich_email_verify_post(
                x_api_key=self._api_key,
                body=request_data
            )
        except ApiException as e:
            raise self._convert_exception(e)

    def search_domain_emails(
        self,
        domain: str,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        department: Optional[str] = None,
        seniority: Optional[str] = None,
        provider: Optional[str] = None
    ) -> V2BaseResponse:
        """
        Search for all email addresses at a domain.

        Args:
            domain: Company domain to search
            limit: Maximum number of results
            offset: Pagination offset
            department: Filter by department (e.g., 'engineering', 'sales')
            seniority: Filter by seniority (e.g., 'senior', 'executive')
            provider: Optional provider override (e.g., 'hunter')

        Returns:
            V2BaseResponse with list of email addresses and metadata

        Example:
            >>> response = client.enrichment.search_domain_emails(
            ...     domain="anthropic.com",
            ...     department="engineering",
            ...     limit=50
            ... )
            >>> for email in response.emails:
            ...     print(f"{email.first_name} {email.last_name}: {email.email}")
        """
        try:
            request_data = {"domain": domain}
            if limit is not None:
                request_data["limit"] = limit
            if offset is not None:
                request_data["offset"] = offset
            if department:
                request_data["department"] = department
            if seniority:
                request_data["seniority"] = seniority
            if provider:
                request_data["provider"] = provider

            return self._api.search_domain_emails_api_v2_enrich_domain_search_post(
                x_api_key=self._api_key,
                body=request_data
            )
        except ApiException as e:
            raise self._convert_exception(e)

    def discover_companies(
        self,
        query: str,
        limit: Optional[int] = None,
        provider: Optional[str] = None
    ) -> V2BaseResponse:
        """
        Discover companies matching search criteria.

        Args:
            query: Search query (company name, industry, location, etc.)
            limit: Maximum number of results
            provider: Optional provider override

        Returns:
            V2BaseResponse with list of matching companies

        Example:
            >>> response = client.enrichment.discover_companies(
            ...     query="AI research San Francisco",
            ...     limit=20
            ... )
            >>> for company in response.companies:
            ...     print(f"{company.name} - {company.domain}")
        """
        try:
            request_data = {"query": query}
            if limit is not None:
                request_data["limit"] = limit
            if provider:
                request_data["provider"] = provider

            return self._api.discover_companies_api_v2_enrich_discover_post(
                x_api_key=self._api_key,
                body=request_data
            )
        except ApiException as e:
            raise self._convert_exception(e)

    def combined_enrichment(
        self,
        email: Optional[str] = None,
        domain: Optional[str] = None,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
        enrich_company: bool = True,
        enrich_lead: bool = True,
        provider: Optional[str] = None
    ) -> V2BaseResponse:
        """
        Perform combined company and lead enrichment in one call.

        Args:
            email: Contact email address
            domain: Company domain
            first_name: Contact first name
            last_name: Contact last name
            enrich_company: Whether to enrich company data
            enrich_lead: Whether to enrich lead data
            provider: Optional provider override

        Returns:
            V2BaseResponse with combined company and lead data

        Example:
            >>> response = client.enrichment.combined_enrichment(
            ...     email="john@example.com",
            ...     domain="example.com"
            ... )
            >>> print(f"Company: {response.company_name}")
            >>> print(f"Contact: {response.first_name} {response.last_name}")
        """
        try:
            request_data = {
                "enrich_company": enrich_company,
                "enrich_lead": enrich_lead
            }
            if email:
                request_data["email"] = email
            if domain:
                request_data["domain"] = domain
            if first_name:
                request_data["first_name"] = first_name
            if last_name:
                request_data["last_name"] = last_name
            if provider:
                request_data["provider"] = provider

            return self._api.combined_enrichment_api_v2_enrich_combined_post(
                x_api_key=self._api_key,
                body=request_data
            )
        except ApiException as e:
            raise self._convert_exception(e)

    def create_lead(
        self,
        email: str,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
        company: Optional[str] = None,
        position: Optional[str] = None,
        metadata: Optional[dict] = None
    ) -> V2BaseResponse:
        """
        Create a new lead in the system.

        Args:
            email: Lead email address (required)
            first_name: Lead first name
            last_name: Lead last name
            company: Company name
            position: Job position/title
            metadata: Additional lead metadata (custom fields)

        Returns:
            V2BaseResponse with created lead data including lead_id

        Example:
            >>> response = client.enrichment.create_lead(
            ...     email="prospect@company.com",
            ...     first_name="Jane",
            ...     last_name="Smith",
            ...     company="Acme Corp",
            ...     position="VP Engineering"
            ... )
            >>> print(f"Lead created with ID: {response.lead_id}")
        """
        try:
            request_data = {"email": email}
            if first_name:
                request_data["first_name"] = first_name
            if last_name:
                request_data["last_name"] = last_name
            if company:
                request_data["company"] = company
            if position:
                request_data["position"] = position
            if metadata:
                request_data["metadata"] = metadata

            return self._api.create_lead_api_v2_enrich_leads_post(
                x_api_key=self._api_key,
                body=request_data
            )
        except ApiException as e:
            raise self._convert_exception(e)

    def get_lead(
        self,
        lead_id: str
    ) -> V2BaseResponse:
        """
        Get a lead by ID.

        Args:
            lead_id: The lead ID to retrieve

        Returns:
            V2BaseResponse with lead data

        Example:
            >>> response = client.enrichment.get_lead(
            ...     lead_id="lead_12345"
            ... )
            >>> print(f"{response.first_name} {response.last_name} - {response.email}")
        """
        try:
            return self._api.get_lead_api_v2_enrich_leads_lead_id_get(
                x_api_key=self._api_key,
                lead_id=lead_id
            )
        except ApiException as e:
            raise self._convert_exception(e)

    def list_leads(
        self,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        company: Optional[str] = None,
        status: Optional[str] = None
    ) -> V2BaseResponse:
        """
        List all leads with optional filtering.

        Args:
            limit: Maximum number of results
            offset: Pagination offset
            company: Filter by company name
            status: Filter by lead status

        Returns:
            V2BaseResponse with list of leads

        Example:
            >>> response = client.enrichment.list_leads(
            ...     company="Acme Corp",
            ...     limit=100
            ... )
            >>> for lead in response.leads:
            ...     print(f"{lead.email} - {lead.status}")
        """
        try:
            params = {}
            if limit is not None:
                params["limit"] = limit
            if offset is not None:
                params["offset"] = offset
            if company:
                params["company"] = company
            if status:
                params["status"] = status

            return self._api.list_leads_api_v2_enrich_leads_get(
                x_api_key=self._api_key,
                **params
            )
        except ApiException as e:
            raise self._convert_exception(e)

    def update_lead(
        self,
        lead_id: str,
        email: Optional[str] = None,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
        company: Optional[str] = None,
        position: Optional[str] = None,
        status: Optional[str] = None,
        metadata: Optional[dict] = None
    ) -> V2BaseResponse:
        """
        Update an existing lead.

        Args:
            lead_id: The lead ID to update
            email: Updated email address
            first_name: Updated first name
            last_name: Updated last name
            company: Updated company name
            position: Updated position
            status: Updated status
            metadata: Updated metadata (custom fields)

        Returns:
            V2BaseResponse with updated lead data

        Example:
            >>> response = client.enrichment.update_lead(
            ...     lead_id="lead_12345",
            ...     status="qualified",
            ...     position="Senior VP Engineering"
            ... )
        """
        try:
            request_data = {}
            if email:
                request_data["email"] = email
            if first_name:
                request_data["first_name"] = first_name
            if last_name:
                request_data["last_name"] = last_name
            if company:
                request_data["company"] = company
            if position:
                request_data["position"] = position
            if status:
                request_data["status"] = status
            if metadata:
                request_data["metadata"] = metadata

            return self._api.update_lead_api_v2_enrich_leads_lead_id_put(
                x_api_key=self._api_key,
                lead_id=lead_id,
                body=request_data
            )
        except ApiException as e:
            raise self._convert_exception(e)

    def delete_lead(
        self,
        lead_id: str
    ) -> V2BaseResponse:
        """
        Delete a lead by ID.

        Args:
            lead_id: The lead ID to delete

        Returns:
            V2BaseResponse with deletion confirmation

        Example:
            >>> response = client.enrichment.delete_lead(
            ...     lead_id="lead_12345"
            ... )
            >>> print(f"Lead deleted: {response.success}")
        """
        try:
            return self._api.delete_lead_api_v2_enrich_leads_lead_id_delete(
                x_api_key=self._api_key,
                lead_id=lead_id
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
        elif status == 404:
            from llmhub.exceptions import NotFoundError
            return NotFoundError(f"Resource not found: {message}")
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
