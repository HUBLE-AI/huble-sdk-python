# llmhub_generated.SEPAPaymentsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_sepa_mandate_api_v1_billing_sepa_org_id_activate_post**](SEPAPaymentsApi.md#activate_sepa_mandate_api_v1_billing_sepa_org_id_activate_post) | **POST** /api/v1/billing/sepa/{org_id}/activate | Activate Sepa Mandate
[**delete_sepa_info_api_v1_billing_sepa_org_id_delete**](SEPAPaymentsApi.md#delete_sepa_info_api_v1_billing_sepa_org_id_delete) | **DELETE** /api/v1/billing/sepa/{org_id} | Delete Sepa Info
[**get_sepa_info_api_v1_billing_sepa_org_id_get**](SEPAPaymentsApi.md#get_sepa_info_api_v1_billing_sepa_org_id_get) | **GET** /api/v1/billing/sepa/{org_id} | Get Sepa Info
[**save_sepa_info_api_v1_billing_sepa_org_id_post**](SEPAPaymentsApi.md#save_sepa_info_api_v1_billing_sepa_org_id_post) | **POST** /api/v1/billing/sepa/{org_id} | Save Sepa Info
[**validate_sepa_api_v1_billing_sepa_validate_post**](SEPAPaymentsApi.md#validate_sepa_api_v1_billing_sepa_validate_post) | **POST** /api/v1/billing/sepa/validate | Validate Sepa


# **activate_sepa_mandate_api_v1_billing_sepa_org_id_activate_post**
> object activate_sepa_mandate_api_v1_billing_sepa_org_id_activate_post(org_id, session_token=session_token)

Activate Sepa Mandate

Activate SEPA mandate after customer signature.

**Permissions:**
- Super Admin: Can activate any organization's mandate
- Org Admin: Can activate own organization's mandate only

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
    api_instance = llmhub_generated.SEPAPaymentsApi(api_client)
    org_id = 56 # int | 
    session_token = 'session_token_example' # str |  (optional)

    try:
        # Activate Sepa Mandate
        api_response = api_instance.activate_sepa_mandate_api_v1_billing_sepa_org_id_activate_post(org_id, session_token=session_token)
        print("The response of SEPAPaymentsApi->activate_sepa_mandate_api_v1_billing_sepa_org_id_activate_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SEPAPaymentsApi->activate_sepa_mandate_api_v1_billing_sepa_org_id_activate_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **int**|  | 
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

# **delete_sepa_info_api_v1_billing_sepa_org_id_delete**
> object delete_sepa_info_api_v1_billing_sepa_org_id_delete(org_id, session_token=session_token)

Delete Sepa Info

Delete (deactivate) SEPA payment method for an organization.

**Permissions:**
- Super Admin: Can delete any organization's SEPA
- Org Admin: Can delete own organization's SEPA only

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
    api_instance = llmhub_generated.SEPAPaymentsApi(api_client)
    org_id = 56 # int | 
    session_token = 'session_token_example' # str |  (optional)

    try:
        # Delete Sepa Info
        api_response = api_instance.delete_sepa_info_api_v1_billing_sepa_org_id_delete(org_id, session_token=session_token)
        print("The response of SEPAPaymentsApi->delete_sepa_info_api_v1_billing_sepa_org_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SEPAPaymentsApi->delete_sepa_info_api_v1_billing_sepa_org_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **int**|  | 
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

# **get_sepa_info_api_v1_billing_sepa_org_id_get**
> SEPAListResponse get_sepa_info_api_v1_billing_sepa_org_id_get(org_id, session_token=session_token)

Get Sepa Info

Get SEPA payment method for an organization.

**Permissions:**
- Super Admin: All organizations
- Super Dev: Assigned organizations only
- Org Admin/User: Own organization only

### Example

* Bearer Authentication (HTTPBearer):

```python
import llmhub_generated
from llmhub_generated.models.sepa_list_response import SEPAListResponse
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
    api_instance = llmhub_generated.SEPAPaymentsApi(api_client)
    org_id = 56 # int | 
    session_token = 'session_token_example' # str |  (optional)

    try:
        # Get Sepa Info
        api_response = api_instance.get_sepa_info_api_v1_billing_sepa_org_id_get(org_id, session_token=session_token)
        print("The response of SEPAPaymentsApi->get_sepa_info_api_v1_billing_sepa_org_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SEPAPaymentsApi->get_sepa_info_api_v1_billing_sepa_org_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **int**|  | 
 **session_token** | **str**|  | [optional] 

### Return type

[**SEPAListResponse**](SEPAListResponse.md)

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

# **save_sepa_info_api_v1_billing_sepa_org_id_post**
> SEPAResponse save_sepa_info_api_v1_billing_sepa_org_id_post(org_id, sepa_create_request, session_token=session_token)

Save Sepa Info

Create or update SEPA payment method for an organization.

**Permissions:**
- Super Admin: Can manage any organization
- Org Admin: Can manage own organization only

Note: Super Dev and User roles cannot modify SEPA information.

### Example

* Bearer Authentication (HTTPBearer):

```python
import llmhub_generated
from llmhub_generated.models.sepa_create_request import SEPACreateRequest
from llmhub_generated.models.sepa_response import SEPAResponse
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
    api_instance = llmhub_generated.SEPAPaymentsApi(api_client)
    org_id = 56 # int | 
    sepa_create_request = llmhub_generated.SEPACreateRequest() # SEPACreateRequest | 
    session_token = 'session_token_example' # str |  (optional)

    try:
        # Save Sepa Info
        api_response = api_instance.save_sepa_info_api_v1_billing_sepa_org_id_post(org_id, sepa_create_request, session_token=session_token)
        print("The response of SEPAPaymentsApi->save_sepa_info_api_v1_billing_sepa_org_id_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SEPAPaymentsApi->save_sepa_info_api_v1_billing_sepa_org_id_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **int**|  | 
 **sepa_create_request** | [**SEPACreateRequest**](SEPACreateRequest.md)|  | 
 **session_token** | **str**|  | [optional] 

### Return type

[**SEPAResponse**](SEPAResponse.md)

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

# **validate_sepa_api_v1_billing_sepa_validate_post**
> SEPAValidateResponse validate_sepa_api_v1_billing_sepa_validate_post(sepa_validate_request, session_token=session_token)

Validate Sepa

Validate IBAN and BIC without saving.

**Permissions:** Any authenticated user

### Example

* Bearer Authentication (HTTPBearer):

```python
import llmhub_generated
from llmhub_generated.models.sepa_validate_request import SEPAValidateRequest
from llmhub_generated.models.sepa_validate_response import SEPAValidateResponse
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
    api_instance = llmhub_generated.SEPAPaymentsApi(api_client)
    sepa_validate_request = llmhub_generated.SEPAValidateRequest() # SEPAValidateRequest | 
    session_token = 'session_token_example' # str |  (optional)

    try:
        # Validate Sepa
        api_response = api_instance.validate_sepa_api_v1_billing_sepa_validate_post(sepa_validate_request, session_token=session_token)
        print("The response of SEPAPaymentsApi->validate_sepa_api_v1_billing_sepa_validate_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SEPAPaymentsApi->validate_sepa_api_v1_billing_sepa_validate_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sepa_validate_request** | [**SEPAValidateRequest**](SEPAValidateRequest.md)|  | 
 **session_token** | **str**|  | [optional] 

### Return type

[**SEPAValidateResponse**](SEPAValidateResponse.md)

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

