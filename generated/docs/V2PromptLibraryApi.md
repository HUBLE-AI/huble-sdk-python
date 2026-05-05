# llmhub_generated.V2PromptLibraryApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_template_api_v2_prompts_post**](V2PromptLibraryApi.md#create_template_api_v2_prompts_post) | **POST** /api/v2/prompts | Create Template
[**delete_template_api_v2_prompts_template_id_delete**](V2PromptLibraryApi.md#delete_template_api_v2_prompts_template_id_delete) | **DELETE** /api/v2/prompts/{template_id} | Delete Template
[**get_template_api_v2_prompts_template_id_get**](V2PromptLibraryApi.md#get_template_api_v2_prompts_template_id_get) | **GET** /api/v2/prompts/{template_id} | Get Template
[**list_template_versions_api_v2_prompts_template_id_versions_get**](V2PromptLibraryApi.md#list_template_versions_api_v2_prompts_template_id_versions_get) | **GET** /api/v2/prompts/{template_id}/versions | List Template Versions
[**list_templates_api_v2_prompts_get**](V2PromptLibraryApi.md#list_templates_api_v2_prompts_get) | **GET** /api/v2/prompts | List Templates
[**search_templates_api_v2_prompts_search_get**](V2PromptLibraryApi.md#search_templates_api_v2_prompts_search_get) | **GET** /api/v2/prompts/search | Search Templates
[**test_template_api_v2_prompts_template_id_test_post**](V2PromptLibraryApi.md#test_template_api_v2_prompts_template_id_test_post) | **POST** /api/v2/prompts/{template_id}/test | Test Template
[**update_template_api_v2_prompts_template_id_put**](V2PromptLibraryApi.md#update_template_api_v2_prompts_template_id_put) | **PUT** /api/v2/prompts/{template_id} | Update Template


# **create_template_api_v2_prompts_post**
> PromptTemplateResponse create_template_api_v2_prompts_post(x_api_key, prompt_template_create)

Create Template

Create a new prompt template

The template will be owned by the current API client.
Can be made public or kept private.

### Example


```python
import llmhub_generated
from llmhub_generated.models.prompt_template_create import PromptTemplateCreate
from llmhub_generated.models.prompt_template_response import PromptTemplateResponse
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
    api_instance = llmhub_generated.V2PromptLibraryApi(api_client)
    x_api_key = 'x_api_key_example' # str | 
    prompt_template_create = llmhub_generated.PromptTemplateCreate() # PromptTemplateCreate | 

    try:
        # Create Template
        api_response = api_instance.create_template_api_v2_prompts_post(x_api_key, prompt_template_create)
        print("The response of V2PromptLibraryApi->create_template_api_v2_prompts_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V2PromptLibraryApi->create_template_api_v2_prompts_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**|  | 
 **prompt_template_create** | [**PromptTemplateCreate**](PromptTemplateCreate.md)|  | 

### Return type

[**PromptTemplateResponse**](PromptTemplateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_template_api_v2_prompts_template_id_delete**
> delete_template_api_v2_prompts_template_id_delete(template_id, x_api_key)

Delete Template

Delete (soft delete) a prompt template

Only the owner can delete a template.
Sets is_active=false instead of actual deletion.

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
    api_instance = llmhub_generated.V2PromptLibraryApi(api_client)
    template_id = 'template_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | 

    try:
        # Delete Template
        api_instance.delete_template_api_v2_prompts_template_id_delete(template_id, x_api_key)
    except Exception as e:
        print("Exception when calling V2PromptLibraryApi->delete_template_api_v2_prompts_template_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**|  | 
 **x_api_key** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_template_api_v2_prompts_template_id_get**
> PromptTemplateResponse get_template_api_v2_prompts_template_id_get(template_id, x_api_key)

Get Template

Get a specific prompt template by ID

Returns:
    Template details if accessible (public or owned by client)

### Example


```python
import llmhub_generated
from llmhub_generated.models.prompt_template_response import PromptTemplateResponse
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
    api_instance = llmhub_generated.V2PromptLibraryApi(api_client)
    template_id = 'template_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | 

    try:
        # Get Template
        api_response = api_instance.get_template_api_v2_prompts_template_id_get(template_id, x_api_key)
        print("The response of V2PromptLibraryApi->get_template_api_v2_prompts_template_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V2PromptLibraryApi->get_template_api_v2_prompts_template_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**|  | 
 **x_api_key** | **str**|  | 

### Return type

[**PromptTemplateResponse**](PromptTemplateResponse.md)

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

# **list_template_versions_api_v2_prompts_template_id_versions_get**
> object list_template_versions_api_v2_prompts_template_id_versions_get(template_id, x_api_key)

List Template Versions

List all versions of a prompt template

Only accessible to template owner.

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
    api_instance = llmhub_generated.V2PromptLibraryApi(api_client)
    template_id = 'template_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | 

    try:
        # List Template Versions
        api_response = api_instance.list_template_versions_api_v2_prompts_template_id_versions_get(template_id, x_api_key)
        print("The response of V2PromptLibraryApi->list_template_versions_api_v2_prompts_template_id_versions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V2PromptLibraryApi->list_template_versions_api_v2_prompts_template_id_versions_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**|  | 
 **x_api_key** | **str**|  | 

### Return type

**object**

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

# **list_templates_api_v2_prompts_get**
> List[PromptTemplateResponse] list_templates_api_v2_prompts_get(x_api_key, template_type=template_type, is_public=is_public)

List Templates

List all accessible prompt templates

Returns:
    - Public templates (is_public=true)
    - Templates owned by the current client

### Example


```python
import llmhub_generated
from llmhub_generated.models.prompt_template_response import PromptTemplateResponse
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
    api_instance = llmhub_generated.V2PromptLibraryApi(api_client)
    x_api_key = 'x_api_key_example' # str | 
    template_type = 'template_type_example' # str | Filter by template type (optional)
    is_public = True # bool | Filter by public status (optional)

    try:
        # List Templates
        api_response = api_instance.list_templates_api_v2_prompts_get(x_api_key, template_type=template_type, is_public=is_public)
        print("The response of V2PromptLibraryApi->list_templates_api_v2_prompts_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V2PromptLibraryApi->list_templates_api_v2_prompts_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**|  | 
 **template_type** | **str**| Filter by template type | [optional] 
 **is_public** | **bool**| Filter by public status | [optional] 

### Return type

[**List[PromptTemplateResponse]**](PromptTemplateResponse.md)

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

# **search_templates_api_v2_prompts_search_get**
> List[PromptTemplateResponse] search_templates_api_v2_prompts_search_get(q, x_api_key, template_type=template_type, is_public=is_public, limit=limit, offset=offset)

Search Templates

Search prompt templates by keyword and filters.

Visibility: searches across the caller's own templates plus public ones.
Match is a case-insensitive substring across `template_name` and `description`.

### Example


```python
import llmhub_generated
from llmhub_generated.models.prompt_template_response import PromptTemplateResponse
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
    api_instance = llmhub_generated.V2PromptLibraryApi(api_client)
    q = 'q_example' # str | Keyword to match in template_name and description
    x_api_key = 'x_api_key_example' # str | 
    template_type = 'template_type_example' # str | Filter by template type (optional)
    is_public = True # bool | Filter by public status (optional)
    limit = 50 # int | Max rows to return (optional) (default to 50)
    offset = 0 # int | Offset for pagination (optional) (default to 0)

    try:
        # Search Templates
        api_response = api_instance.search_templates_api_v2_prompts_search_get(q, x_api_key, template_type=template_type, is_public=is_public, limit=limit, offset=offset)
        print("The response of V2PromptLibraryApi->search_templates_api_v2_prompts_search_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V2PromptLibraryApi->search_templates_api_v2_prompts_search_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| Keyword to match in template_name and description | 
 **x_api_key** | **str**|  | 
 **template_type** | **str**| Filter by template type | [optional] 
 **is_public** | **bool**| Filter by public status | [optional] 
 **limit** | **int**| Max rows to return | [optional] [default to 50]
 **offset** | **int**| Offset for pagination | [optional] [default to 0]

### Return type

[**List[PromptTemplateResponse]**](PromptTemplateResponse.md)

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

# **test_template_api_v2_prompts_template_id_test_post**
> object test_template_api_v2_prompts_template_id_test_post(template_id, x_api_key, request_body)

Test Template

Test a prompt template with sample variables

Returns the rendered prompt without calling the LLM.
Useful for testing variable substitution.

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
    api_instance = llmhub_generated.V2PromptLibraryApi(api_client)
    template_id = 'template_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | 
    request_body = None # Dict[str, object] | 

    try:
        # Test Template
        api_response = api_instance.test_template_api_v2_prompts_template_id_test_post(template_id, x_api_key, request_body)
        print("The response of V2PromptLibraryApi->test_template_api_v2_prompts_template_id_test_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V2PromptLibraryApi->test_template_api_v2_prompts_template_id_test_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**|  | 
 **x_api_key** | **str**|  | 
 **request_body** | [**Dict[str, object]**](object.md)|  | 

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

# **update_template_api_v2_prompts_template_id_put**
> PromptTemplateResponse update_template_api_v2_prompts_template_id_put(template_id, x_api_key, prompt_template_update)

Update Template

Update an existing prompt template

Only the owner can update a template.
Creates a new version if system_prompt or user_prompt_template changes.

### Example


```python
import llmhub_generated
from llmhub_generated.models.prompt_template_response import PromptTemplateResponse
from llmhub_generated.models.prompt_template_update import PromptTemplateUpdate
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
    api_instance = llmhub_generated.V2PromptLibraryApi(api_client)
    template_id = 'template_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | 
    prompt_template_update = llmhub_generated.PromptTemplateUpdate() # PromptTemplateUpdate | 

    try:
        # Update Template
        api_response = api_instance.update_template_api_v2_prompts_template_id_put(template_id, x_api_key, prompt_template_update)
        print("The response of V2PromptLibraryApi->update_template_api_v2_prompts_template_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V2PromptLibraryApi->update_template_api_v2_prompts_template_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**|  | 
 **x_api_key** | **str**|  | 
 **prompt_template_update** | [**PromptTemplateUpdate**](PromptTemplateUpdate.md)|  | 

### Return type

[**PromptTemplateResponse**](PromptTemplateResponse.md)

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

