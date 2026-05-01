# llmhub_generated.V2ERPConnectorsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authenticate_odoo_api_v2_connector_odoo_authenticate_post**](V2ERPConnectorsApi.md#authenticate_odoo_api_v2_connector_odoo_authenticate_post) | **POST** /api/v2/connector/odoo/authenticate | Authenticate Odoo
[**discover_odoo_models_api_v2_connector_odoo_discover_models_post**](V2ERPConnectorsApi.md#discover_odoo_models_api_v2_connector_odoo_discover_models_post) | **POST** /api/v2/connector/odoo/discover-models | Discover Odoo Models
[**list_odoo_databases_api_v2_connector_odoo_list_databases_post**](V2ERPConnectorsApi.md#list_odoo_databases_api_v2_connector_odoo_list_databases_post) | **POST** /api/v2/connector/odoo/list-databases | List Odoo Databases
[**pull_odoo_records_api_v2_connector_odoo_pull_records_post**](V2ERPConnectorsApi.md#pull_odoo_records_api_v2_connector_odoo_pull_records_post) | **POST** /api/v2/connector/odoo/pull-records | Pull Odoo Records
[**search_odoo_models_api_v2_connector_odoo_search_models_post**](V2ERPConnectorsApi.md#search_odoo_models_api_v2_connector_odoo_search_models_post) | **POST** /api/v2/connector/odoo/search-models | Search Odoo Models


# **authenticate_odoo_api_v2_connector_odoo_authenticate_post**
> object authenticate_odoo_api_v2_connector_odoo_authenticate_post(x_api_key, odoo_authenticate_request)

Authenticate Odoo

Test Odoo credentials via XML-RPC authenticate.

Returns uid and odoo_version on success.

### Example


```python
import llmhub_generated
from llmhub_generated.models.odoo_authenticate_request import OdooAuthenticateRequest
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
    api_instance = llmhub_generated.V2ERPConnectorsApi(api_client)
    x_api_key = 'x_api_key_example' # str | 
    odoo_authenticate_request = llmhub_generated.OdooAuthenticateRequest() # OdooAuthenticateRequest | 

    try:
        # Authenticate Odoo
        api_response = api_instance.authenticate_odoo_api_v2_connector_odoo_authenticate_post(x_api_key, odoo_authenticate_request)
        print("The response of V2ERPConnectorsApi->authenticate_odoo_api_v2_connector_odoo_authenticate_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V2ERPConnectorsApi->authenticate_odoo_api_v2_connector_odoo_authenticate_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**|  | 
 **odoo_authenticate_request** | [**OdooAuthenticateRequest**](OdooAuthenticateRequest.md)|  | 

### Return type

**object**

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

# **discover_odoo_models_api_v2_connector_odoo_discover_models_post**
> object discover_odoo_models_api_v2_connector_odoo_discover_models_post(x_api_key, odoo_discover_models_request)

Discover Odoo Models

Discover available Odoo models with record counts.

Returns tiered model list (Tier 1 always included, Tier 2 conditional on installed apps).

### Example


```python
import llmhub_generated
from llmhub_generated.models.odoo_discover_models_request import OdooDiscoverModelsRequest
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
    api_instance = llmhub_generated.V2ERPConnectorsApi(api_client)
    x_api_key = 'x_api_key_example' # str | 
    odoo_discover_models_request = llmhub_generated.OdooDiscoverModelsRequest() # OdooDiscoverModelsRequest | 

    try:
        # Discover Odoo Models
        api_response = api_instance.discover_odoo_models_api_v2_connector_odoo_discover_models_post(x_api_key, odoo_discover_models_request)
        print("The response of V2ERPConnectorsApi->discover_odoo_models_api_v2_connector_odoo_discover_models_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V2ERPConnectorsApi->discover_odoo_models_api_v2_connector_odoo_discover_models_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**|  | 
 **odoo_discover_models_request** | [**OdooDiscoverModelsRequest**](OdooDiscoverModelsRequest.md)|  | 

### Return type

**object**

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

# **list_odoo_databases_api_v2_connector_odoo_list_databases_post**
> object list_odoo_databases_api_v2_connector_odoo_list_databases_post(x_api_key, odoo_list_databases_request)

List Odoo Databases

List available databases on an Odoo instance.

Returns empty list if db listing is disabled (list_db = False in odoo.conf).

### Example


```python
import llmhub_generated
from llmhub_generated.models.odoo_list_databases_request import OdooListDatabasesRequest
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
    api_instance = llmhub_generated.V2ERPConnectorsApi(api_client)
    x_api_key = 'x_api_key_example' # str | 
    odoo_list_databases_request = llmhub_generated.OdooListDatabasesRequest() # OdooListDatabasesRequest | 

    try:
        # List Odoo Databases
        api_response = api_instance.list_odoo_databases_api_v2_connector_odoo_list_databases_post(x_api_key, odoo_list_databases_request)
        print("The response of V2ERPConnectorsApi->list_odoo_databases_api_v2_connector_odoo_list_databases_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V2ERPConnectorsApi->list_odoo_databases_api_v2_connector_odoo_list_databases_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**|  | 
 **odoo_list_databases_request** | [**OdooListDatabasesRequest**](OdooListDatabasesRequest.md)|  | 

### Return type

**object**

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

# **pull_odoo_records_api_v2_connector_odoo_pull_records_post**
> object pull_odoo_records_api_v2_connector_odoo_pull_records_post(x_api_key, odoo_pull_records_request)

Pull Odoo Records

Pull records from an Odoo model in batches.

For large models prefer ESB (async sync via RabbitMQ) over this HTTP endpoint.
Default timeout: 300s.

### Example


```python
import llmhub_generated
from llmhub_generated.models.odoo_pull_records_request import OdooPullRecordsRequest
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
    api_instance = llmhub_generated.V2ERPConnectorsApi(api_client)
    x_api_key = 'x_api_key_example' # str | 
    odoo_pull_records_request = llmhub_generated.OdooPullRecordsRequest() # OdooPullRecordsRequest | 

    try:
        # Pull Odoo Records
        api_response = api_instance.pull_odoo_records_api_v2_connector_odoo_pull_records_post(x_api_key, odoo_pull_records_request)
        print("The response of V2ERPConnectorsApi->pull_odoo_records_api_v2_connector_odoo_pull_records_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V2ERPConnectorsApi->pull_odoo_records_api_v2_connector_odoo_pull_records_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**|  | 
 **odoo_pull_records_request** | [**OdooPullRecordsRequest**](OdooPullRecordsRequest.md)|  | 

### Return type

**object**

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

# **search_odoo_models_api_v2_connector_odoo_search_models_post**
> object search_odoo_models_api_v2_connector_odoo_search_models_post(x_api_key, odoo_search_models_request)

Search Odoo Models

Search Odoo ir.model for non-transient models matching query.

Returns list of {model_name, display_name} for Tier 3 custom model selection.

### Example


```python
import llmhub_generated
from llmhub_generated.models.odoo_search_models_request import OdooSearchModelsRequest
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
    api_instance = llmhub_generated.V2ERPConnectorsApi(api_client)
    x_api_key = 'x_api_key_example' # str | 
    odoo_search_models_request = llmhub_generated.OdooSearchModelsRequest() # OdooSearchModelsRequest | 

    try:
        # Search Odoo Models
        api_response = api_instance.search_odoo_models_api_v2_connector_odoo_search_models_post(x_api_key, odoo_search_models_request)
        print("The response of V2ERPConnectorsApi->search_odoo_models_api_v2_connector_odoo_search_models_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V2ERPConnectorsApi->search_odoo_models_api_v2_connector_odoo_search_models_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**|  | 
 **odoo_search_models_request** | [**OdooSearchModelsRequest**](OdooSearchModelsRequest.md)|  | 

### Return type

**object**

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

