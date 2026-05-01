# llmhub_generated.PublicWebsiteApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_api_call_categories_api_public_apicalls_get**](PublicWebsiteApi.md#get_api_call_categories_api_public_apicalls_get) | **GET** /api/public/apicalls | Get Api Call Categories
[**get_capabilities_public_api_public_capabilities_get**](PublicWebsiteApi.md#get_capabilities_public_api_public_capabilities_get) | **GET** /api/public/capabilities | Get Capabilities Public
[**get_category_endpoints_api_public_apicalls_category_get**](PublicWebsiteApi.md#get_category_endpoints_api_public_apicalls_category_get) | **GET** /api/public/apicalls/{category} | Get Category Endpoints
[**get_endpoint_detail_public_api_public_endpoints_endpoint_id_get**](PublicWebsiteApi.md#get_endpoint_detail_public_api_public_endpoints_endpoint_id_get) | **GET** /api/public/endpoints/{endpoint_id} | Get Endpoint Detail Public
[**get_model_detail_public_api_public_models_model_key_get**](PublicWebsiteApi.md#get_model_detail_public_api_public_models_model_key_get) | **GET** /api/public/models/{model_key} | Get Model Detail Public
[**get_models_public_api_public_models_get**](PublicWebsiteApi.md#get_models_public_api_public_models_get) | **GET** /api/public/models | Get Models Public
[**get_platform_stats_api_public_stats_get**](PublicWebsiteApi.md#get_platform_stats_api_public_stats_get) | **GET** /api/public/stats | Get Platform Stats
[**get_pricing_catalog_api_public_pricing_get**](PublicWebsiteApi.md#get_pricing_catalog_api_public_pricing_get) | **GET** /api/public/pricing | Get Pricing Catalog
[**get_provider_detail_public_api_public_providers_provider_key_get**](PublicWebsiteApi.md#get_provider_detail_public_api_public_providers_provider_key_get) | **GET** /api/public/providers/{provider_key} | Get Provider Detail Public
[**get_providers_public_api_public_providers_get**](PublicWebsiteApi.md#get_providers_public_api_public_providers_get) | **GET** /api/public/providers | Get Providers Public


# **get_api_call_categories_api_public_apicalls_get**
> Dict[str, object] get_api_call_categories_api_public_apicalls_get()

Get Api Call Categories

PUBLIC - Get all API call categories with endpoint counts.

### Example


```python
import llmhub_generated
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
    api_instance = llmhub_generated.PublicWebsiteApi(api_client)

    try:
        # Get Api Call Categories
        api_response = api_instance.get_api_call_categories_api_public_apicalls_get()
        print("The response of PublicWebsiteApi->get_api_call_categories_api_public_apicalls_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicWebsiteApi->get_api_call_categories_api_public_apicalls_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**Dict[str, object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_capabilities_public_api_public_capabilities_get**
> Dict[str, object] get_capabilities_public_api_public_capabilities_get()

Get Capabilities Public

PUBLIC - Get AI capabilities/model types offered.

### Example


```python
import llmhub_generated
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
    api_instance = llmhub_generated.PublicWebsiteApi(api_client)

    try:
        # Get Capabilities Public
        api_response = api_instance.get_capabilities_public_api_public_capabilities_get()
        print("The response of PublicWebsiteApi->get_capabilities_public_api_public_capabilities_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicWebsiteApi->get_capabilities_public_api_public_capabilities_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**Dict[str, object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_category_endpoints_api_public_apicalls_category_get**
> Dict[str, object] get_category_endpoints_api_public_apicalls_category_get(category)

Get Category Endpoints

PUBLIC - Get all endpoints in a specific category.

### Example


```python
import llmhub_generated
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
    api_instance = llmhub_generated.PublicWebsiteApi(api_client)
    category = 'category_example' # str | 

    try:
        # Get Category Endpoints
        api_response = api_instance.get_category_endpoints_api_public_apicalls_category_get(category)
        print("The response of PublicWebsiteApi->get_category_endpoints_api_public_apicalls_category_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicWebsiteApi->get_category_endpoints_api_public_apicalls_category_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category** | **str**|  | 

### Return type

**Dict[str, object]**

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

# **get_endpoint_detail_public_api_public_endpoints_endpoint_id_get**
> Dict[str, object] get_endpoint_detail_public_api_public_endpoints_endpoint_id_get(endpoint_id)

Get Endpoint Detail Public

PUBLIC - Get full endpoint documentation for CallCard page.
Returns endpoint details including description, parameters, code examples,
response example, rate limits, and related endpoints.

### Example


```python
import llmhub_generated
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
    api_instance = llmhub_generated.PublicWebsiteApi(api_client)
    endpoint_id = 'endpoint_id_example' # str | 

    try:
        # Get Endpoint Detail Public
        api_response = api_instance.get_endpoint_detail_public_api_public_endpoints_endpoint_id_get(endpoint_id)
        print("The response of PublicWebsiteApi->get_endpoint_detail_public_api_public_endpoints_endpoint_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicWebsiteApi->get_endpoint_detail_public_api_public_endpoints_endpoint_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint_id** | **str**|  | 

### Return type

**Dict[str, object]**

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

# **get_model_detail_public_api_public_models_model_key_get**
> Dict[str, object] get_model_detail_public_api_public_models_model_key_get(model_key)

Get Model Detail Public

PUBLIC - Get detailed model information including provider and pricing.

### Example


```python
import llmhub_generated
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
    api_instance = llmhub_generated.PublicWebsiteApi(api_client)
    model_key = 'model_key_example' # str | 

    try:
        # Get Model Detail Public
        api_response = api_instance.get_model_detail_public_api_public_models_model_key_get(model_key)
        print("The response of PublicWebsiteApi->get_model_detail_public_api_public_models_model_key_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicWebsiteApi->get_model_detail_public_api_public_models_model_key_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model_key** | **str**|  | 

### Return type

**Dict[str, object]**

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

# **get_models_public_api_public_models_get**
> Dict[str, object] get_models_public_api_public_models_get()

Get Models Public

PUBLIC - Get list of all available models.

### Example


```python
import llmhub_generated
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
    api_instance = llmhub_generated.PublicWebsiteApi(api_client)

    try:
        # Get Models Public
        api_response = api_instance.get_models_public_api_public_models_get()
        print("The response of PublicWebsiteApi->get_models_public_api_public_models_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicWebsiteApi->get_models_public_api_public_models_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**Dict[str, object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_platform_stats_api_public_stats_get**
> Dict[str, object] get_platform_stats_api_public_stats_get()

Get Platform Stats

PUBLIC - Get high-level platform statistics for homepage.

### Example


```python
import llmhub_generated
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
    api_instance = llmhub_generated.PublicWebsiteApi(api_client)

    try:
        # Get Platform Stats
        api_response = api_instance.get_platform_stats_api_public_stats_get()
        print("The response of PublicWebsiteApi->get_platform_stats_api_public_stats_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicWebsiteApi->get_platform_stats_api_public_stats_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**Dict[str, object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pricing_catalog_api_public_pricing_get**
> Dict[str, object] get_pricing_catalog_api_public_pricing_get()

Get Pricing Catalog

PUBLIC - Get complete API pricing catalog for marketing website.
Returns all active endpoints with pricing and category metadata.

### Example


```python
import llmhub_generated
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
    api_instance = llmhub_generated.PublicWebsiteApi(api_client)

    try:
        # Get Pricing Catalog
        api_response = api_instance.get_pricing_catalog_api_public_pricing_get()
        print("The response of PublicWebsiteApi->get_pricing_catalog_api_public_pricing_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicWebsiteApi->get_pricing_catalog_api_public_pricing_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**Dict[str, object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_provider_detail_public_api_public_providers_provider_key_get**
> Dict[str, object] get_provider_detail_public_api_public_providers_provider_key_get(provider_key)

Get Provider Detail Public

PUBLIC - Get detailed provider information including models.

### Example


```python
import llmhub_generated
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
    api_instance = llmhub_generated.PublicWebsiteApi(api_client)
    provider_key = 'provider_key_example' # str | 

    try:
        # Get Provider Detail Public
        api_response = api_instance.get_provider_detail_public_api_public_providers_provider_key_get(provider_key)
        print("The response of PublicWebsiteApi->get_provider_detail_public_api_public_providers_provider_key_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicWebsiteApi->get_provider_detail_public_api_public_providers_provider_key_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_key** | **str**|  | 

### Return type

**Dict[str, object]**

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

# **get_providers_public_api_public_providers_get**
> Dict[str, object] get_providers_public_api_public_providers_get()

Get Providers Public

PUBLIC - Get list of LLM providers for website display.
Returns active providers with model counts.

### Example


```python
import llmhub_generated
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
    api_instance = llmhub_generated.PublicWebsiteApi(api_client)

    try:
        # Get Providers Public
        api_response = api_instance.get_providers_public_api_public_providers_get()
        print("The response of PublicWebsiteApi->get_providers_public_api_public_providers_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicWebsiteApi->get_providers_public_api_public_providers_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**Dict[str, object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

