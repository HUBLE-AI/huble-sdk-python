# llmhub_generated.V2AgentMultiTurnToolsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**agent_chat_api_v2_agent_chat_post**](V2AgentMultiTurnToolsApi.md#agent_chat_api_v2_agent_chat_post) | **POST** /api/v2/agent/chat | Agent Chat
[**chat_completions_api_v2_chat_completions_post**](V2AgentMultiTurnToolsApi.md#chat_completions_api_v2_chat_completions_post) | **POST** /api/v2/chat/completions | Chat Completions


# **agent_chat_api_v2_agent_chat_post**
> V2AgentChatResponse agent_chat_api_v2_agent_chat_post(x_api_key, v2_agent_chat_request)

Agent Chat

Multi-turn chat with tool-use. Canonical endpoint.

### Example


```python
import llmhub_generated
from llmhub_generated.models.v2_agent_chat_request import V2AgentChatRequest
from llmhub_generated.models.v2_agent_chat_response import V2AgentChatResponse
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
    api_instance = llmhub_generated.V2AgentMultiTurnToolsApi(api_client)
    x_api_key = 'x_api_key_example' # str | 
    v2_agent_chat_request = llmhub_generated.V2AgentChatRequest() # V2AgentChatRequest | 

    try:
        # Agent Chat
        api_response = api_instance.agent_chat_api_v2_agent_chat_post(x_api_key, v2_agent_chat_request)
        print("The response of V2AgentMultiTurnToolsApi->agent_chat_api_v2_agent_chat_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V2AgentMultiTurnToolsApi->agent_chat_api_v2_agent_chat_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**|  | 
 **v2_agent_chat_request** | [**V2AgentChatRequest**](V2AgentChatRequest.md)|  | 

### Return type

[**V2AgentChatResponse**](V2AgentChatResponse.md)

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

# **chat_completions_api_v2_chat_completions_post**
> V2AgentChatResponse chat_completions_api_v2_chat_completions_post(x_api_key, v2_agent_chat_request)

Chat Completions

OpenAI SDK drop-in alias.

Same handler as /agent/chat — `openai.OpenAI(base_url=...).chat.completions.create()`
will hit this path. We log under a separate endpoint label so usage stats can
distinguish SDK clients from agent-shape clients.

### Example


```python
import llmhub_generated
from llmhub_generated.models.v2_agent_chat_request import V2AgentChatRequest
from llmhub_generated.models.v2_agent_chat_response import V2AgentChatResponse
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
    api_instance = llmhub_generated.V2AgentMultiTurnToolsApi(api_client)
    x_api_key = 'x_api_key_example' # str | 
    v2_agent_chat_request = llmhub_generated.V2AgentChatRequest() # V2AgentChatRequest | 

    try:
        # Chat Completions
        api_response = api_instance.chat_completions_api_v2_chat_completions_post(x_api_key, v2_agent_chat_request)
        print("The response of V2AgentMultiTurnToolsApi->chat_completions_api_v2_chat_completions_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V2AgentMultiTurnToolsApi->chat_completions_api_v2_chat_completions_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**|  | 
 **v2_agent_chat_request** | [**V2AgentChatRequest**](V2AgentChatRequest.md)|  | 

### Return type

[**V2AgentChatResponse**](V2AgentChatResponse.md)

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

