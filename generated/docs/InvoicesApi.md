# llmhub_generated.InvoicesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**download_invoice_pdf_api_v1_billing_invoices_invoice_id_pdf_get**](InvoicesApi.md#download_invoice_pdf_api_v1_billing_invoices_invoice_id_pdf_get) | **GET** /api/v1/billing/invoices/{invoice_id}/pdf | Download Invoice Pdf
[**generate_invoice_api_v1_billing_invoices_generate_org_id_year_month_post**](InvoicesApi.md#generate_invoice_api_v1_billing_invoices_generate_org_id_year_month_post) | **POST** /api/v1/billing/invoices/generate/{org_id}/{year}/{month} | Generate Invoice
[**get_invoice_api_v1_billing_invoices_invoice_id_get**](InvoicesApi.md#get_invoice_api_v1_billing_invoices_invoice_id_get) | **GET** /api/v1/billing/invoices/{invoice_id} | Get Invoice
[**issue_invoice_api_v1_billing_invoices_invoice_id_issue_post**](InvoicesApi.md#issue_invoice_api_v1_billing_invoices_invoice_id_issue_post) | **POST** /api/v1/billing/invoices/{invoice_id}/issue | Issue Invoice
[**list_invoices_api_v1_billing_invoices_get**](InvoicesApi.md#list_invoices_api_v1_billing_invoices_get) | **GET** /api/v1/billing/invoices | List Invoices
[**update_invoice_status_api_v1_billing_invoices_invoice_id_status_patch**](InvoicesApi.md#update_invoice_status_api_v1_billing_invoices_invoice_id_status_patch) | **PATCH** /api/v1/billing/invoices/{invoice_id}/status | Update Invoice Status


# **download_invoice_pdf_api_v1_billing_invoices_invoice_id_pdf_get**
> object download_invoice_pdf_api_v1_billing_invoices_invoice_id_pdf_get(invoice_id, session_token=session_token)

Download Invoice Pdf

Download invoice PDF.

**Permissions:**
- Super Admin: All invoices
- Super Dev: Invoices for assigned organizations
- Org Admin/User: Own organization invoices only

### Example

* Bearer Authentication (HTTPBearer):

```python
import llmhub_generated
from llmhub_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = llmhub_generated.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = llmhub_generated.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with llmhub_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = llmhub_generated.InvoicesApi(api_client)
    invoice_id = 'invoice_id_example' # str | 
    session_token = 'session_token_example' # str |  (optional)

    try:
        # Download Invoice Pdf
        api_response = api_instance.download_invoice_pdf_api_v1_billing_invoices_invoice_id_pdf_get(invoice_id, session_token=session_token)
        print("The response of InvoicesApi->download_invoice_pdf_api_v1_billing_invoices_invoice_id_pdf_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->download_invoice_pdf_api_v1_billing_invoices_invoice_id_pdf_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **str**|  | 
 **session_token** | **str**|  | [optional] 

### Return type

**object**

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_invoice_api_v1_billing_invoices_generate_org_id_year_month_post**
> InvoiceResponse generate_invoice_api_v1_billing_invoices_generate_org_id_year_month_post(org_id, year, month, notes=notes, session_token=session_token)

Generate Invoice

Generate a monthly invoice for an organization.

**Permissions:**
- Super Admin: Can generate for any organization
- Org Admin: Can generate for own organization only

Note: Super Dev and User roles cannot generate invoices.

### Example

* Bearer Authentication (HTTPBearer):

```python
import llmhub_generated
from llmhub_generated.models.invoice_response import InvoiceResponse
from llmhub_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = llmhub_generated.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = llmhub_generated.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with llmhub_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = llmhub_generated.InvoicesApi(api_client)
    org_id = 56 # int | 
    year = 56 # int | 
    month = 56 # int | 
    notes = 'notes_example' # str | Optional notes for the invoice (optional)
    session_token = 'session_token_example' # str |  (optional)

    try:
        # Generate Invoice
        api_response = api_instance.generate_invoice_api_v1_billing_invoices_generate_org_id_year_month_post(org_id, year, month, notes=notes, session_token=session_token)
        print("The response of InvoicesApi->generate_invoice_api_v1_billing_invoices_generate_org_id_year_month_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->generate_invoice_api_v1_billing_invoices_generate_org_id_year_month_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **int**|  | 
 **year** | **int**|  | 
 **month** | **int**|  | 
 **notes** | **str**| Optional notes for the invoice | [optional] 
 **session_token** | **str**|  | [optional] 

### Return type

[**InvoiceResponse**](InvoiceResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoice_api_v1_billing_invoices_invoice_id_get**
> InvoiceResponse get_invoice_api_v1_billing_invoices_invoice_id_get(invoice_id, session_token=session_token)

Get Invoice

Get invoice details by ID.

**Permissions:**
- Super Admin: All invoices
- Super Dev: Invoices for assigned organizations
- Org Admin/User: Own organization invoices only

### Example

* Bearer Authentication (HTTPBearer):

```python
import llmhub_generated
from llmhub_generated.models.invoice_response import InvoiceResponse
from llmhub_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = llmhub_generated.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = llmhub_generated.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with llmhub_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = llmhub_generated.InvoicesApi(api_client)
    invoice_id = 'invoice_id_example' # str | 
    session_token = 'session_token_example' # str |  (optional)

    try:
        # Get Invoice
        api_response = api_instance.get_invoice_api_v1_billing_invoices_invoice_id_get(invoice_id, session_token=session_token)
        print("The response of InvoicesApi->get_invoice_api_v1_billing_invoices_invoice_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->get_invoice_api_v1_billing_invoices_invoice_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **str**|  | 
 **session_token** | **str**|  | [optional] 

### Return type

[**InvoiceResponse**](InvoiceResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_invoice_api_v1_billing_invoices_invoice_id_issue_post**
> InvoiceResponse issue_invoice_api_v1_billing_invoices_invoice_id_issue_post(invoice_id, session_token=session_token)

Issue Invoice

Issue a draft invoice. This generates the PDF if not already generated.

**Permissions:**
- Super Admin: Can issue any invoice
- Org Admin: Can issue own organization invoices only

### Example

* Bearer Authentication (HTTPBearer):

```python
import llmhub_generated
from llmhub_generated.models.invoice_response import InvoiceResponse
from llmhub_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = llmhub_generated.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = llmhub_generated.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with llmhub_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = llmhub_generated.InvoicesApi(api_client)
    invoice_id = 'invoice_id_example' # str | 
    session_token = 'session_token_example' # str |  (optional)

    try:
        # Issue Invoice
        api_response = api_instance.issue_invoice_api_v1_billing_invoices_invoice_id_issue_post(invoice_id, session_token=session_token)
        print("The response of InvoicesApi->issue_invoice_api_v1_billing_invoices_invoice_id_issue_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->issue_invoice_api_v1_billing_invoices_invoice_id_issue_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **str**|  | 
 **session_token** | **str**|  | [optional] 

### Return type

[**InvoiceResponse**](InvoiceResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_invoices_api_v1_billing_invoices_get**
> InvoiceListResponse list_invoices_api_v1_billing_invoices_get(org_id=org_id, status=status, year=year, page=page, page_size=page_size, session_token=session_token)

List Invoices

List invoices with optional filtering.

**Permissions:**
- Super Admin: All organizations
- Super Dev: Assigned organizations only
- Org Admin: Own organization only
- User: Own organization only (read-only)

### Example

* Bearer Authentication (HTTPBearer):

```python
import llmhub_generated
from llmhub_generated.models.invoice_list_response import InvoiceListResponse
from llmhub_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = llmhub_generated.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = llmhub_generated.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with llmhub_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = llmhub_generated.InvoicesApi(api_client)
    org_id = 56 # int | Filter by organization ID (optional)
    status = 'status_example' # str | Filter by status (draft, issued, paid, overdue, cancelled) (optional)
    year = 56 # int | Filter by year (optional)
    page = 1 # int | Page number (optional) (default to 1)
    page_size = 20 # int | Items per page (optional) (default to 20)
    session_token = 'session_token_example' # str |  (optional)

    try:
        # List Invoices
        api_response = api_instance.list_invoices_api_v1_billing_invoices_get(org_id=org_id, status=status, year=year, page=page, page_size=page_size, session_token=session_token)
        print("The response of InvoicesApi->list_invoices_api_v1_billing_invoices_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->list_invoices_api_v1_billing_invoices_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **int**| Filter by organization ID | [optional] 
 **status** | **str**| Filter by status (draft, issued, paid, overdue, cancelled) | [optional] 
 **year** | **int**| Filter by year | [optional] 
 **page** | **int**| Page number | [optional] [default to 1]
 **page_size** | **int**| Items per page | [optional] [default to 20]
 **session_token** | **str**|  | [optional] 

### Return type

[**InvoiceListResponse**](InvoiceListResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_invoice_status_api_v1_billing_invoices_invoice_id_status_patch**
> InvoiceResponse update_invoice_status_api_v1_billing_invoices_invoice_id_status_patch(invoice_id, invoice_status_update_request, session_token=session_token)

Update Invoice Status

Update invoice status.

Valid transitions:
- draft -> issued, cancelled
- issued -> paid, overdue, cancelled
- overdue -> paid, cancelled
- paid -> (final state)
- cancelled -> (final state)

**Permissions:**
- Super Admin: Can update any invoice
- Org Admin: Can update own organization invoices only

Note: Super Dev and User roles cannot modify invoices.

### Example

* Bearer Authentication (HTTPBearer):

```python
import llmhub_generated
from llmhub_generated.models.invoice_response import InvoiceResponse
from llmhub_generated.models.invoice_status_update_request import InvoiceStatusUpdateRequest
from llmhub_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = llmhub_generated.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = llmhub_generated.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with llmhub_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = llmhub_generated.InvoicesApi(api_client)
    invoice_id = 'invoice_id_example' # str | 
    invoice_status_update_request = llmhub_generated.InvoiceStatusUpdateRequest() # InvoiceStatusUpdateRequest | 
    session_token = 'session_token_example' # str |  (optional)

    try:
        # Update Invoice Status
        api_response = api_instance.update_invoice_status_api_v1_billing_invoices_invoice_id_status_patch(invoice_id, invoice_status_update_request, session_token=session_token)
        print("The response of InvoicesApi->update_invoice_status_api_v1_billing_invoices_invoice_id_status_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->update_invoice_status_api_v1_billing_invoices_invoice_id_status_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **str**|  | 
 **invoice_status_update_request** | [**InvoiceStatusUpdateRequest**](InvoiceStatusUpdateRequest.md)|  | 
 **session_token** | **str**|  | [optional] 

### Return type

[**InvoiceResponse**](InvoiceResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

