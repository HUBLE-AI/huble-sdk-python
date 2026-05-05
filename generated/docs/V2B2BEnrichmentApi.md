# llmhub_generated.V2B2BEnrichmentApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**combined_enrichment_api_v2_enrichment_combined_post**](V2B2BEnrichmentApi.md#combined_enrichment_api_v2_enrichment_combined_post) | **POST** /api/v2/enrichment/combined | Combined Enrichment
[**create_lead_api_v2_enrichment_leads_post**](V2B2BEnrichmentApi.md#create_lead_api_v2_enrichment_leads_post) | **POST** /api/v2/enrichment/leads | Create Lead
[**delete_lead_api_v2_enrichment_leads_lead_id_delete**](V2B2BEnrichmentApi.md#delete_lead_api_v2_enrichment_leads_lead_id_delete) | **DELETE** /api/v2/enrichment/leads/{lead_id} | Delete Lead
[**discover_companies_api_v2_enrichment_discover_post**](V2B2BEnrichmentApi.md#discover_companies_api_v2_enrichment_discover_post) | **POST** /api/v2/enrichment/discover | Discover Companies
[**enrich_company_api_v2_enrichment_company_post**](V2B2BEnrichmentApi.md#enrich_company_api_v2_enrichment_company_post) | **POST** /api/v2/enrichment/company | Enrich Company
[**enrich_lead_api_v2_enrichment_lead_post**](V2B2BEnrichmentApi.md#enrich_lead_api_v2_enrichment_lead_post) | **POST** /api/v2/enrichment/lead | Enrich Lead
[**find_email_api_v2_enrichment_email_finder_post**](V2B2BEnrichmentApi.md#find_email_api_v2_enrichment_email_finder_post) | **POST** /api/v2/enrichment/email-finder | Find Email
[**get_lead_api_v2_enrichment_leads_lead_id_get**](V2B2BEnrichmentApi.md#get_lead_api_v2_enrichment_leads_lead_id_get) | **GET** /api/v2/enrichment/leads/{lead_id} | Get Lead
[**list_leads_api_v2_enrichment_leads_get**](V2B2BEnrichmentApi.md#list_leads_api_v2_enrichment_leads_get) | **GET** /api/v2/enrichment/leads | List Leads
[**search_domain_emails_api_v2_enrichment_domain_search_post**](V2B2BEnrichmentApi.md#search_domain_emails_api_v2_enrichment_domain_search_post) | **POST** /api/v2/enrichment/domain-search | Search Domain Emails
[**update_lead_api_v2_enrichment_leads_lead_id_put**](V2B2BEnrichmentApi.md#update_lead_api_v2_enrichment_leads_lead_id_put) | **PUT** /api/v2/enrichment/leads/{lead_id} | Update Lead
[**verify_email_api_v2_enrichment_email_verify_post**](V2B2BEnrichmentApi.md#verify_email_api_v2_enrichment_email_verify_post) | **POST** /api/v2/enrichment/email-verify | Verify Email


# **combined_enrichment_api_v2_enrichment_combined_post**
> V2EnrichmentResponse combined_enrichment_api_v2_enrichment_combined_post(x_api_key, v2_combined_enrichment_request)

Combined Enrichment

Combined person + company enrichment in single API call

**Most comprehensive endpoint** - Get complete B2B intelligence

**Use case:** Full prospect context for AI-powered personalized outreach

**Data returned:**
- **Person data:** Name, position, seniority, location, timezone, social profiles (100+ attributes)
- **Company data:** Industry, tech stack, funding, employee count, headquarters

**Input:** Email OR LinkedIn handle

**Perfect for:** LLM-powered sales automation where you need maximum context

### Example


```python
import llmhub_generated
from llmhub_generated.models.v2_combined_enrichment_request import V2CombinedEnrichmentRequest
from llmhub_generated.models.v2_enrichment_response import V2EnrichmentResponse
from llmhub_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = llmhub_generated.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with llmhub_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = llmhub_generated.V2B2BEnrichmentApi(api_client)
    x_api_key = 'x_api_key_example' # str | 
    v2_combined_enrichment_request = llmhub_generated.V2CombinedEnrichmentRequest() # V2CombinedEnrichmentRequest | 

    try:
        # Combined Enrichment
        api_response = api_instance.combined_enrichment_api_v2_enrichment_combined_post(x_api_key, v2_combined_enrichment_request)
        print("The response of V2B2BEnrichmentApi->combined_enrichment_api_v2_enrichment_combined_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V2B2BEnrichmentApi->combined_enrichment_api_v2_enrichment_combined_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**|  | 
 **v2_combined_enrichment_request** | [**V2CombinedEnrichmentRequest**](V2CombinedEnrichmentRequest.md)|  | 

### Return type

[**V2EnrichmentResponse**](V2EnrichmentResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_lead_api_v2_enrichment_leads_post**
> V2EnrichmentResponse create_lead_api_v2_enrichment_leads_post(x_api_key, v2_lead_create_request)

Create Lead

Create new lead in Hunter.io

**Use case:** Store discovered leads for future enrichment and tracking

### Example


```python
import llmhub_generated
from llmhub_generated.models.v2_enrichment_response import V2EnrichmentResponse
from llmhub_generated.models.v2_lead_create_request import V2LeadCreateRequest
from llmhub_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = llmhub_generated.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with llmhub_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = llmhub_generated.V2B2BEnrichmentApi(api_client)
    x_api_key = 'x_api_key_example' # str | 
    v2_lead_create_request = llmhub_generated.V2LeadCreateRequest() # V2LeadCreateRequest | 

    try:
        # Create Lead
        api_response = api_instance.create_lead_api_v2_enrichment_leads_post(x_api_key, v2_lead_create_request)
        print("The response of V2B2BEnrichmentApi->create_lead_api_v2_enrichment_leads_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V2B2BEnrichmentApi->create_lead_api_v2_enrichment_leads_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**|  | 
 **v2_lead_create_request** | [**V2LeadCreateRequest**](V2LeadCreateRequest.md)|  | 

### Return type

[**V2EnrichmentResponse**](V2EnrichmentResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_lead_api_v2_enrichment_leads_lead_id_delete**
> V2BaseResponse delete_lead_api_v2_enrichment_leads_lead_id_delete(lead_id, x_api_key)

Delete Lead

Delete lead from Hunter.io

### Example


```python
import llmhub_generated
from llmhub_generated.models.v2_base_response import V2BaseResponse
from llmhub_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = llmhub_generated.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with llmhub_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = llmhub_generated.V2B2BEnrichmentApi(api_client)
    lead_id = 'lead_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | 

    try:
        # Delete Lead
        api_response = api_instance.delete_lead_api_v2_enrichment_leads_lead_id_delete(lead_id, x_api_key)
        print("The response of V2B2BEnrichmentApi->delete_lead_api_v2_enrichment_leads_lead_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V2B2BEnrichmentApi->delete_lead_api_v2_enrichment_leads_lead_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lead_id** | **str**|  | 
 **x_api_key** | **str**|  | 

### Return type

[**V2BaseResponse**](V2BaseResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **discover_companies_api_v2_enrichment_discover_post**
> V2EnrichmentResponse discover_companies_api_v2_enrichment_discover_post(x_api_key, v2_discover_request)

Discover Companies

Discover companies using natural language queries

**Use case:** Find relevant B2B prospects at scale using plain language

**Example queries:**
- "US-based Software companies with 100-500 employees"
- "European fintech startups founded after 2020"
- "Healthcare companies in California"

### Example


```python
import llmhub_generated
from llmhub_generated.models.v2_discover_request import V2DiscoverRequest
from llmhub_generated.models.v2_enrichment_response import V2EnrichmentResponse
from llmhub_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = llmhub_generated.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with llmhub_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = llmhub_generated.V2B2BEnrichmentApi(api_client)
    x_api_key = 'x_api_key_example' # str | 
    v2_discover_request = llmhub_generated.V2DiscoverRequest() # V2DiscoverRequest | 

    try:
        # Discover Companies
        api_response = api_instance.discover_companies_api_v2_enrichment_discover_post(x_api_key, v2_discover_request)
        print("The response of V2B2BEnrichmentApi->discover_companies_api_v2_enrichment_discover_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V2B2BEnrichmentApi->discover_companies_api_v2_enrichment_discover_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**|  | 
 **v2_discover_request** | [**V2DiscoverRequest**](V2DiscoverRequest.md)|  | 

### Return type

[**V2EnrichmentResponse**](V2EnrichmentResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enrich_company_api_v2_enrichment_company_post**
> V2EnrichmentResponse enrich_company_api_v2_enrichment_company_post(x_api_key, v2_company_enrichment_request)

Enrich Company

Enrich company profile with firmographic and technographic data

**Use case:** Get complete company intelligence for account-based marketing

**Data returned:**
- Company name, legal name, description
- Industry, sector classification
- Founding year, employee count
- Headquarters, addresses with coordinates
- Technology stack (50+ technologies)
- Funding information
- Social media profiles
- Traffic rank

**Input:** Company domain

### Example


```python
import llmhub_generated
from llmhub_generated.models.v2_company_enrichment_request import V2CompanyEnrichmentRequest
from llmhub_generated.models.v2_enrichment_response import V2EnrichmentResponse
from llmhub_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = llmhub_generated.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with llmhub_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = llmhub_generated.V2B2BEnrichmentApi(api_client)
    x_api_key = 'x_api_key_example' # str | 
    v2_company_enrichment_request = llmhub_generated.V2CompanyEnrichmentRequest() # V2CompanyEnrichmentRequest | 

    try:
        # Enrich Company
        api_response = api_instance.enrich_company_api_v2_enrichment_company_post(x_api_key, v2_company_enrichment_request)
        print("The response of V2B2BEnrichmentApi->enrich_company_api_v2_enrichment_company_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V2B2BEnrichmentApi->enrich_company_api_v2_enrichment_company_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**|  | 
 **v2_company_enrichment_request** | [**V2CompanyEnrichmentRequest**](V2CompanyEnrichmentRequest.md)|  | 

### Return type

[**V2EnrichmentResponse**](V2EnrichmentResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enrich_lead_api_v2_enrichment_lead_post**
> V2EnrichmentResponse enrich_lead_api_v2_enrichment_lead_post(x_api_key, v2_lead_enrichment_request)

Enrich Lead

Enrich person profile with 100+ attributes

**Use case:** Get comprehensive person data for personalized outreach

**Data returned:**
- Full name, position, seniority
- Location, timezone
- Social profiles (LinkedIn, Twitter, GitHub, Facebook)
- Employment history
- Email provider info

**Input:** Email OR LinkedIn handle

### Example


```python
import llmhub_generated
from llmhub_generated.models.v2_enrichment_response import V2EnrichmentResponse
from llmhub_generated.models.v2_lead_enrichment_request import V2LeadEnrichmentRequest
from llmhub_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = llmhub_generated.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with llmhub_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = llmhub_generated.V2B2BEnrichmentApi(api_client)
    x_api_key = 'x_api_key_example' # str | 
    v2_lead_enrichment_request = llmhub_generated.V2LeadEnrichmentRequest() # V2LeadEnrichmentRequest | 

    try:
        # Enrich Lead
        api_response = api_instance.enrich_lead_api_v2_enrichment_lead_post(x_api_key, v2_lead_enrichment_request)
        print("The response of V2B2BEnrichmentApi->enrich_lead_api_v2_enrichment_lead_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V2B2BEnrichmentApi->enrich_lead_api_v2_enrichment_lead_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**|  | 
 **v2_lead_enrichment_request** | [**V2LeadEnrichmentRequest**](V2LeadEnrichmentRequest.md)|  | 

### Return type

[**V2EnrichmentResponse**](V2EnrichmentResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_email_api_v2_enrichment_email_finder_post**
> V2EnrichmentResponse find_email_api_v2_enrichment_email_finder_post(x_api_key, v2_email_finder_request)

Find Email

Find verified professional email for specific person

**Use case:** Locate decision-maker contact information for targeted outreach

**Inputs:**
- Domain + (First name + Last name) OR Full name OR LinkedIn handle

**Returns:** Email with confidence score, position, social profiles

### Example


```python
import llmhub_generated
from llmhub_generated.models.v2_email_finder_request import V2EmailFinderRequest
from llmhub_generated.models.v2_enrichment_response import V2EnrichmentResponse
from llmhub_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = llmhub_generated.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with llmhub_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = llmhub_generated.V2B2BEnrichmentApi(api_client)
    x_api_key = 'x_api_key_example' # str | 
    v2_email_finder_request = llmhub_generated.V2EmailFinderRequest() # V2EmailFinderRequest | 

    try:
        # Find Email
        api_response = api_instance.find_email_api_v2_enrichment_email_finder_post(x_api_key, v2_email_finder_request)
        print("The response of V2B2BEnrichmentApi->find_email_api_v2_enrichment_email_finder_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V2B2BEnrichmentApi->find_email_api_v2_enrichment_email_finder_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**|  | 
 **v2_email_finder_request** | [**V2EmailFinderRequest**](V2EmailFinderRequest.md)|  | 

### Return type

[**V2EnrichmentResponse**](V2EnrichmentResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_lead_api_v2_enrichment_leads_lead_id_get**
> V2EnrichmentResponse get_lead_api_v2_enrichment_leads_lead_id_get(lead_id, x_api_key)

Get Lead

Get specific lead by ID

### Example


```python
import llmhub_generated
from llmhub_generated.models.v2_enrichment_response import V2EnrichmentResponse
from llmhub_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = llmhub_generated.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with llmhub_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = llmhub_generated.V2B2BEnrichmentApi(api_client)
    lead_id = 'lead_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | 

    try:
        # Get Lead
        api_response = api_instance.get_lead_api_v2_enrichment_leads_lead_id_get(lead_id, x_api_key)
        print("The response of V2B2BEnrichmentApi->get_lead_api_v2_enrichment_leads_lead_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V2B2BEnrichmentApi->get_lead_api_v2_enrichment_leads_lead_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lead_id** | **str**|  | 
 **x_api_key** | **str**|  | 

### Return type

[**V2EnrichmentResponse**](V2EnrichmentResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_leads_api_v2_enrichment_leads_get**
> V2EnrichmentResponse list_leads_api_v2_enrichment_leads_get(x_api_key, offset=offset, limit=limit)

List Leads

List stored leads from Hunter.io account

**Use case:** Retrieve and sync leads stored in Hunter.io

### Example


```python
import llmhub_generated
from llmhub_generated.models.v2_enrichment_response import V2EnrichmentResponse
from llmhub_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = llmhub_generated.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with llmhub_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = llmhub_generated.V2B2BEnrichmentApi(api_client)
    x_api_key = 'x_api_key_example' # str | 
    offset = 0 # int |  (optional) (default to 0)
    limit = 10 # int |  (optional) (default to 10)

    try:
        # List Leads
        api_response = api_instance.list_leads_api_v2_enrichment_leads_get(x_api_key, offset=offset, limit=limit)
        print("The response of V2B2BEnrichmentApi->list_leads_api_v2_enrichment_leads_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V2B2BEnrichmentApi->list_leads_api_v2_enrichment_leads_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**|  | 
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 10]

### Return type

[**V2EnrichmentResponse**](V2EnrichmentResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_domain_emails_api_v2_enrichment_domain_search_post**
> V2EnrichmentResponse search_domain_emails_api_v2_enrichment_domain_search_post(x_api_key, v2_domain_search_request)

Search Domain Emails

Find all email addresses for a company domain

**Use case:** Build comprehensive contact lists for account-based marketing

**Filters available:**
- Email type (personal/generic)
- Seniority (junior/senior/executive)
- Department (engineering/sales/marketing/hr/finance)

**Returns:** Email list with confidence scores, positions, LinkedIn profiles

### Example


```python
import llmhub_generated
from llmhub_generated.models.v2_domain_search_request import V2DomainSearchRequest
from llmhub_generated.models.v2_enrichment_response import V2EnrichmentResponse
from llmhub_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = llmhub_generated.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with llmhub_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = llmhub_generated.V2B2BEnrichmentApi(api_client)
    x_api_key = 'x_api_key_example' # str | 
    v2_domain_search_request = llmhub_generated.V2DomainSearchRequest() # V2DomainSearchRequest | 

    try:
        # Search Domain Emails
        api_response = api_instance.search_domain_emails_api_v2_enrichment_domain_search_post(x_api_key, v2_domain_search_request)
        print("The response of V2B2BEnrichmentApi->search_domain_emails_api_v2_enrichment_domain_search_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V2B2BEnrichmentApi->search_domain_emails_api_v2_enrichment_domain_search_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**|  | 
 **v2_domain_search_request** | [**V2DomainSearchRequest**](V2DomainSearchRequest.md)|  | 

### Return type

[**V2EnrichmentResponse**](V2EnrichmentResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_lead_api_v2_enrichment_leads_lead_id_put**
> V2EnrichmentResponse update_lead_api_v2_enrichment_leads_lead_id_put(lead_id, x_api_key, v2_lead_update_request)

Update Lead

Update existing lead in Hunter.io

### Example


```python
import llmhub_generated
from llmhub_generated.models.v2_enrichment_response import V2EnrichmentResponse
from llmhub_generated.models.v2_lead_update_request import V2LeadUpdateRequest
from llmhub_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = llmhub_generated.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with llmhub_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = llmhub_generated.V2B2BEnrichmentApi(api_client)
    lead_id = 'lead_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | 
    v2_lead_update_request = llmhub_generated.V2LeadUpdateRequest() # V2LeadUpdateRequest | 

    try:
        # Update Lead
        api_response = api_instance.update_lead_api_v2_enrichment_leads_lead_id_put(lead_id, x_api_key, v2_lead_update_request)
        print("The response of V2B2BEnrichmentApi->update_lead_api_v2_enrichment_leads_lead_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V2B2BEnrichmentApi->update_lead_api_v2_enrichment_leads_lead_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lead_id** | **str**|  | 
 **x_api_key** | **str**|  | 
 **v2_lead_update_request** | [**V2LeadUpdateRequest**](V2LeadUpdateRequest.md)|  | 

### Return type

[**V2EnrichmentResponse**](V2EnrichmentResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_email_api_v2_enrichment_email_verify_post**
> V2EnrichmentResponse verify_email_api_v2_enrichment_email_verify_post(x_api_key, v2_email_verifier_request)

Verify Email

Verify email address validity and deliverability

**Use case:** Clean email lists and reduce bounce rates before campaigns

**Validation checks:**
- Format validation (regexp)
- Disposable email detection
- MX records check
- SMTP server verification
- Gibberish detection
- Webmail classification

**Returns:** Status (valid/invalid/risky/unknown) + confidence score (0-100)

### Example


```python
import llmhub_generated
from llmhub_generated.models.v2_email_verifier_request import V2EmailVerifierRequest
from llmhub_generated.models.v2_enrichment_response import V2EnrichmentResponse
from llmhub_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = llmhub_generated.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with llmhub_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = llmhub_generated.V2B2BEnrichmentApi(api_client)
    x_api_key = 'x_api_key_example' # str | 
    v2_email_verifier_request = llmhub_generated.V2EmailVerifierRequest() # V2EmailVerifierRequest | 

    try:
        # Verify Email
        api_response = api_instance.verify_email_api_v2_enrichment_email_verify_post(x_api_key, v2_email_verifier_request)
        print("The response of V2B2BEnrichmentApi->verify_email_api_v2_enrichment_email_verify_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V2B2BEnrichmentApi->verify_email_api_v2_enrichment_email_verify_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**|  | 
 **v2_email_verifier_request** | [**V2EmailVerifierRequest**](V2EmailVerifierRequest.md)|  | 

### Return type

[**V2EnrichmentResponse**](V2EnrichmentResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

