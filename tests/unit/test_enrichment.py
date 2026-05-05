"""Unit tests for EnrichmentOperations."""

import pytest
from unittest.mock import Mock, patch
from llmhub.enrichment import EnrichmentOperations
from llmhub.exceptions import (
    ValidationError,
    AuthenticationError,
    RateLimitError,
    NotFoundError,
    ServerError
)
from llmhub_generated.exceptions import ApiException


@pytest.fixture
def enrichment_ops(mock_api_key):
    """Create EnrichmentOperations instance for testing."""
    mock_client = Mock()
    return EnrichmentOperations(mock_client, mock_api_key)


@pytest.fixture
def mock_response():
    """Create a mock successful response."""
    response = Mock()
    response.success = True
    response.company_name = "Anthropic"
    response.industry = "AI Research"
    response.email = "john@example.com"
    response.score = 95
    response.valid = True
    return response


class TestEnrichCompany:
    """Tests for enrich_company() method."""

    def test_enrich_company_success(self, enrichment_ops, mock_response):
        """Test successful company enrichment."""
        with patch.object(
            enrichment_ops._api,
            'enrich_company_api_v2_enrichment_company_post',
            return_value=mock_response
        ):
            response = enrichment_ops.enrich_company(
                domain="anthropic.com"
            )
            assert response.success is True
            assert response.company_name == "Anthropic"

    def test_enrich_company_with_provider(self, enrichment_ops, mock_response):
        """Test company enrichment with provider."""
        with patch.object(
            enrichment_ops._api,
            'enrich_company_api_v2_enrichment_company_post',
            return_value=mock_response
        ):
            response = enrichment_ops.enrich_company(
                domain="example.com",
                provider="hunter"
            )
            assert response.success is True


class TestEnrichLead:
    """Tests for enrich_lead() method."""

    def test_enrich_lead_with_email(self, enrichment_ops, mock_response):
        """Test lead enrichment with email."""
        with patch.object(
            enrichment_ops._api,
            'enrich_lead_api_v2_enrichment_lead_post',
            return_value=mock_response
        ):
            response = enrichment_ops.enrich_lead(
                email="john@example.com"
            )
            assert response.success is True

    def test_enrich_lead_with_name_domain(self, enrichment_ops, mock_response):
        """Test lead enrichment with name and domain."""
        with patch.object(
            enrichment_ops._api,
            'enrich_lead_api_v2_enrichment_lead_post',
            return_value=mock_response
        ):
            response = enrichment_ops.enrich_lead(
                first_name="John",
                last_name="Doe",
                domain="example.com"
            )
            assert response.success is True


class TestFindEmail:
    """Tests for find_email() method."""

    def test_find_email_success(self, enrichment_ops, mock_response):
        """Test successful email finding."""
        with patch.object(
            enrichment_ops._api,
            'find_email_api_v2_enrichment_email_finder_post',
            return_value=mock_response
        ):
            response = enrichment_ops.find_email(
                domain="anthropic.com",
                first_name="Dario",
                last_name="Amodei"
            )
            assert response.success is True
            assert response.email is not None

    def test_find_email_with_provider(self, enrichment_ops, mock_response):
        """Test email finding with provider."""
        with patch.object(
            enrichment_ops._api,
            'find_email_api_v2_enrichment_email_finder_post',
            return_value=mock_response
        ):
            response = enrichment_ops.find_email(
                domain="example.com",
                first_name="Jane",
                last_name="Smith",
                provider="hunter"
            )
            assert response.success is True


class TestVerifyEmail:
    """Tests for verify_email() method."""

    def test_verify_email_success(self, enrichment_ops, mock_response):
        """Test successful email verification."""
        with patch.object(
            enrichment_ops._api,
            'verify_email_api_v2_enrichment_email_verify_post',
            return_value=mock_response
        ):
            response = enrichment_ops.verify_email(
                email="john@example.com"
            )
            assert response.success is True
            assert response.valid is True

    def test_verify_email_with_provider(self, enrichment_ops, mock_response):
        """Test email verification with provider."""
        with patch.object(
            enrichment_ops._api,
            'verify_email_api_v2_enrichment_email_verify_post',
            return_value=mock_response
        ):
            response = enrichment_ops.verify_email(
                email="test@domain.com",
                provider="hunter"
            )
            assert response.success is True


class TestSearchDomainEmails:
    """Tests for search_domain_emails() method."""

    def test_search_domain_emails_success(self, enrichment_ops, mock_response):
        """Test successful domain email search."""
        mock_response.emails = [
            Mock(first_name="John", last_name="Doe", email="john@example.com"),
            Mock(first_name="Jane", last_name="Smith", email="jane@example.com")
        ]
        with patch.object(
            enrichment_ops._api,
            'search_domain_emails_api_v2_enrichment_domain_search_post',
            return_value=mock_response
        ):
            response = enrichment_ops.search_domain_emails(
                domain="example.com",
                limit=50
            )
            assert response.success is True
            assert len(response.emails) == 2

    def test_search_domain_emails_with_filters(self, enrichment_ops, mock_response):
        """Test domain email search with filters."""
        with patch.object(
            enrichment_ops._api,
            'search_domain_emails_api_v2_enrichment_domain_search_post',
            return_value=mock_response
        ):
            response = enrichment_ops.search_domain_emails(
                domain="anthropic.com",
                department="engineering",
                seniority="senior",
                limit=20,
                offset=10
            )
            assert response.success is True


class TestDiscoverCompanies:
    """Tests for discover_companies() method."""

    def test_discover_companies_success(self, enrichment_ops, mock_response):
        """Test successful company discovery."""
        mock_response.companies = [
            Mock(name="Company A", domain="companya.com"),
            Mock(name="Company B", domain="companyb.com")
        ]
        with patch.object(
            enrichment_ops._api,
            'discover_companies_api_v2_enrichment_discover_post',
            return_value=mock_response
        ):
            response = enrichment_ops.discover_companies(
                query="AI research San Francisco"
            )
            assert response.success is True
            assert len(response.companies) == 2

    def test_discover_companies_with_limit(self, enrichment_ops, mock_response):
        """Test company discovery with limit."""
        with patch.object(
            enrichment_ops._api,
            'discover_companies_api_v2_enrichment_discover_post',
            return_value=mock_response
        ):
            response = enrichment_ops.discover_companies(
                query="fintech startups",
                limit=10
            )
            assert response.success is True


class TestCombinedEnrichment:
    """Tests for combined_enrichment() method."""

    def test_combined_enrichment_success(self, enrichment_ops, mock_response):
        """Test successful combined enrichment."""
        with patch.object(
            enrichment_ops._api,
            'combined_enrichment_api_v2_enrichment_combined_post',
            return_value=mock_response
        ):
            response = enrichment_ops.combined_enrichment(
                email="john@example.com",
                domain="example.com"
            )
            assert response.success is True

    def test_combined_enrichment_selective(self, enrichment_ops, mock_response):
        """Test combined enrichment with selective flags."""
        with patch.object(
            enrichment_ops._api,
            'combined_enrichment_api_v2_enrichment_combined_post',
            return_value=mock_response
        ):
            response = enrichment_ops.combined_enrichment(
                email="jane@company.com",
                enrich_company=True,
                enrich_lead=False
            )
            assert response.success is True


class TestCreateLead:
    """Tests for create_lead() method."""

    def test_create_lead_success(self, enrichment_ops, mock_response):
        """Test successful lead creation."""
        mock_response.lead_id = "lead_12345"
        with patch.object(
            enrichment_ops._api,
            'create_lead_api_v2_enrichment_leads_post',
            return_value=mock_response
        ):
            response = enrichment_ops.create_lead(
                email="prospect@company.com",
                first_name="Jane",
                last_name="Smith"
            )
            assert response.success is True
            assert response.lead_id == "lead_12345"

    def test_create_lead_with_metadata(self, enrichment_ops, mock_response):
        """Test lead creation with metadata."""
        with patch.object(
            enrichment_ops._api,
            'create_lead_api_v2_enrichment_leads_post',
            return_value=mock_response
        ):
            response = enrichment_ops.create_lead(
                email="lead@company.com",
                company="Acme Corp",
                position="VP Engineering",
                metadata={"source": "webinar", "score": 85}
            )
            assert response.success is True


class TestGetLead:
    """Tests for get_lead() method."""

    def test_get_lead_success(self, enrichment_ops, mock_response):
        """Test successful lead retrieval."""
        with patch.object(
            enrichment_ops._api,
            'get_lead_api_v2_enrichment_leads_lead_id_get',
            return_value=mock_response
        ):
            response = enrichment_ops.get_lead(
                lead_id="lead_12345"
            )
            assert response.success is True


class TestListLeads:
    """Tests for list_leads() method."""

    def test_list_leads_success(self, enrichment_ops, mock_response):
        """Test successful leads listing."""
        mock_response.leads = [
            Mock(email="lead1@company.com", status="qualified"),
            Mock(email="lead2@company.com", status="contacted")
        ]
        with patch.object(
            enrichment_ops._api,
            'list_leads_api_v2_enrichment_leads_get',
            return_value=mock_response
        ):
            response = enrichment_ops.list_leads()
            assert response.success is True
            assert len(response.leads) == 2

    def test_list_leads_with_filters(self, enrichment_ops, mock_response):
        """Test leads listing with filters."""
        with patch.object(
            enrichment_ops._api,
            'list_leads_api_v2_enrichment_leads_get',
            return_value=mock_response
        ):
            response = enrichment_ops.list_leads(
                company="Acme Corp",
                status="qualified",
                limit=100,
                offset=0
            )
            assert response.success is True


class TestUpdateLead:
    """Tests for update_lead() method."""

    def test_update_lead_success(self, enrichment_ops, mock_response):
        """Test successful lead update."""
        with patch.object(
            enrichment_ops._api,
            'update_lead_api_v2_enrichment_leads_lead_id_put',
            return_value=mock_response
        ):
            response = enrichment_ops.update_lead(
                lead_id="lead_12345",
                status="qualified"
            )
            assert response.success is True

    def test_update_lead_multiple_fields(self, enrichment_ops, mock_response):
        """Test lead update with multiple fields."""
        with patch.object(
            enrichment_ops._api,
            'update_lead_api_v2_enrichment_leads_lead_id_put',
            return_value=mock_response
        ):
            response = enrichment_ops.update_lead(
                lead_id="lead_12345",
                position="Senior VP Engineering",
                status="qualified",
                metadata={"score": 95}
            )
            assert response.success is True


class TestDeleteLead:
    """Tests for delete_lead() method."""

    def test_delete_lead_success(self, enrichment_ops, mock_response):
        """Test successful lead deletion."""
        with patch.object(
            enrichment_ops._api,
            'delete_lead_api_v2_enrichment_leads_lead_id_delete',
            return_value=mock_response
        ):
            response = enrichment_ops.delete_lead(
                lead_id="lead_12345"
            )
            assert response.success is True


class TestEnrichmentErrorHandling:
    """Tests for error handling."""

    def test_authentication_error(self, enrichment_ops):
        """Test authentication error conversion."""
        api_exception = ApiException(status=401, reason="Unauthorized")
        with patch.object(
            enrichment_ops._api,
            'enrich_company_api_v2_enrichment_company_post',
            side_effect=api_exception
        ):
            with pytest.raises(AuthenticationError):
                enrichment_ops.enrich_company(domain="example.com")

    def test_not_found_error(self, enrichment_ops):
        """Test not found error conversion."""
        api_exception = ApiException(status=404, reason="Not found")
        with patch.object(
            enrichment_ops._api,
            'get_lead_api_v2_enrichment_leads_lead_id_get',
            side_effect=api_exception
        ):
            with pytest.raises(NotFoundError):
                enrichment_ops.get_lead(lead_id="nonexistent")

    def test_validation_error(self, enrichment_ops):
        """Test validation error conversion."""
        api_exception = ApiException(status=422, reason="Validation failed")
        with patch.object(
            enrichment_ops._api,
            'verify_email_api_v2_enrichment_email_verify_post',
            side_effect=api_exception
        ):
            with pytest.raises(ValidationError):
                enrichment_ops.verify_email(email="invalid")

    def test_rate_limit_error(self, enrichment_ops):
        """Test rate limit error conversion."""
        api_exception = ApiException(status=429, reason="Rate limit exceeded")
        api_exception.headers = {'Retry-After': '180'}
        with patch.object(
            enrichment_ops._api,
            'find_email_api_v2_enrichment_email_finder_post',
            side_effect=api_exception
        ):
            with pytest.raises(RateLimitError) as exc_info:
                enrichment_ops.find_email(
                    domain="example.com",
                    first_name="John",
                    last_name="Doe"
                )
            assert exc_info.value.retry_after == 180

    def test_server_error(self, enrichment_ops):
        """Test server error conversion."""
        api_exception = ApiException(status=500, reason="Internal server error")
        with patch.object(
            enrichment_ops._api,
            'create_lead_api_v2_enrichment_leads_post',
            side_effect=api_exception
        ):
            with pytest.raises(ServerError):
                enrichment_ops.create_lead(email="test@example.com")
