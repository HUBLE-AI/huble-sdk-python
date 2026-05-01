# llmhub_generated.InvitationsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_invitation_api_v1_invitations_invitation_id_delete**](InvitationsApi.md#cancel_invitation_api_v1_invitations_invitation_id_delete) | **DELETE** /api/v1/invitations/{invitation_id} | Cancel Invitation
[**cancel_invitation_api_v1_invitations_invitation_id_delete_0**](InvitationsApi.md#cancel_invitation_api_v1_invitations_invitation_id_delete_0) | **DELETE** /api/v1/invitations/{invitation_id} | Cancel Invitation
[**get_sent_invitations_api_v1_invitations_sent_get**](InvitationsApi.md#get_sent_invitations_api_v1_invitations_sent_get) | **GET** /api/v1/invitations/sent | Get Sent Invitations
[**get_sent_invitations_api_v1_invitations_sent_get_0**](InvitationsApi.md#get_sent_invitations_api_v1_invitations_sent_get_0) | **GET** /api/v1/invitations/sent | Get Sent Invitations
[**send_invitations_api_v1_invitations_send_post**](InvitationsApi.md#send_invitations_api_v1_invitations_send_post) | **POST** /api/v1/invitations/send | Send Invitations
[**send_invitations_api_v1_invitations_send_post_0**](InvitationsApi.md#send_invitations_api_v1_invitations_send_post_0) | **POST** /api/v1/invitations/send | Send Invitations


# **cancel_invitation_api_v1_invitations_invitation_id_delete**
> cancel_invitation_api_v1_invitations_invitation_id_delete(invitation_id, session_token=session_token)

Cancel Invitation

Cancel a pending invitation

Only the inviter can cancel their own invitations.

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
    api_instance = llmhub_generated.InvitationsApi(api_client)
    invitation_id = 56 # int | 
    session_token = 'session_token_example' # str |  (optional)

    try:
        # Cancel Invitation
        api_instance.cancel_invitation_api_v1_invitations_invitation_id_delete(invitation_id, session_token=session_token)
    except Exception as e:
        print("Exception when calling InvitationsApi->cancel_invitation_api_v1_invitations_invitation_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invitation_id** | **int**|  | 
 **session_token** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_invitation_api_v1_invitations_invitation_id_delete_0**
> cancel_invitation_api_v1_invitations_invitation_id_delete_0(invitation_id, session_token=session_token)

Cancel Invitation

Cancel a pending invitation

Only the inviter can cancel their own invitations.

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
    api_instance = llmhub_generated.InvitationsApi(api_client)
    invitation_id = 56 # int | 
    session_token = 'session_token_example' # str |  (optional)

    try:
        # Cancel Invitation
        api_instance.cancel_invitation_api_v1_invitations_invitation_id_delete_0(invitation_id, session_token=session_token)
    except Exception as e:
        print("Exception when calling InvitationsApi->cancel_invitation_api_v1_invitations_invitation_id_delete_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invitation_id** | **int**|  | 
 **session_token** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sent_invitations_api_v1_invitations_sent_get**
> InvitationListResponse get_sent_invitations_api_v1_invitations_sent_get(session_token=session_token)

Get Sent Invitations

Get list of invitations sent by current user

### Example

* Bearer Authentication (HTTPBearer):

```python
import llmhub_generated
from llmhub_generated.models.invitation_list_response import InvitationListResponse
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
    api_instance = llmhub_generated.InvitationsApi(api_client)
    session_token = 'session_token_example' # str |  (optional)

    try:
        # Get Sent Invitations
        api_response = api_instance.get_sent_invitations_api_v1_invitations_sent_get(session_token=session_token)
        print("The response of InvitationsApi->get_sent_invitations_api_v1_invitations_sent_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvitationsApi->get_sent_invitations_api_v1_invitations_sent_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_token** | **str**|  | [optional] 

### Return type

[**InvitationListResponse**](InvitationListResponse.md)

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

# **get_sent_invitations_api_v1_invitations_sent_get_0**
> InvitationListResponse get_sent_invitations_api_v1_invitations_sent_get_0(session_token=session_token)

Get Sent Invitations

Get list of invitations sent by current user

### Example

* Bearer Authentication (HTTPBearer):

```python
import llmhub_generated
from llmhub_generated.models.invitation_list_response import InvitationListResponse
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
    api_instance = llmhub_generated.InvitationsApi(api_client)
    session_token = 'session_token_example' # str |  (optional)

    try:
        # Get Sent Invitations
        api_response = api_instance.get_sent_invitations_api_v1_invitations_sent_get_0(session_token=session_token)
        print("The response of InvitationsApi->get_sent_invitations_api_v1_invitations_sent_get_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvitationsApi->get_sent_invitations_api_v1_invitations_sent_get_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_token** | **str**|  | [optional] 

### Return type

[**InvitationListResponse**](InvitationListResponse.md)

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

# **send_invitations_api_v1_invitations_send_post**
> SendInvitationsResponse send_invitations_api_v1_invitations_send_post(send_invitations_request, session_token=session_token)

Send Invitations

Send invitations to potential users

- Creates invitation records in database
- Sends email to each invitee
- Returns count of successful sends

When invitee registers, the inviter automatically becomes their Super-Dev.

### Example

* Bearer Authentication (HTTPBearer):

```python
import llmhub_generated
from llmhub_generated.models.send_invitations_request import SendInvitationsRequest
from llmhub_generated.models.send_invitations_response import SendInvitationsResponse
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
    api_instance = llmhub_generated.InvitationsApi(api_client)
    send_invitations_request = llmhub_generated.SendInvitationsRequest() # SendInvitationsRequest | 
    session_token = 'session_token_example' # str |  (optional)

    try:
        # Send Invitations
        api_response = api_instance.send_invitations_api_v1_invitations_send_post(send_invitations_request, session_token=session_token)
        print("The response of InvitationsApi->send_invitations_api_v1_invitations_send_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvitationsApi->send_invitations_api_v1_invitations_send_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **send_invitations_request** | [**SendInvitationsRequest**](SendInvitationsRequest.md)|  | 
 **session_token** | **str**|  | [optional] 

### Return type

[**SendInvitationsResponse**](SendInvitationsResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_invitations_api_v1_invitations_send_post_0**
> SendInvitationsResponse send_invitations_api_v1_invitations_send_post_0(send_invitations_request, session_token=session_token)

Send Invitations

Send invitations to potential users

- Creates invitation records in database
- Sends email to each invitee
- Returns count of successful sends

When invitee registers, the inviter automatically becomes their Super-Dev.

### Example

* Bearer Authentication (HTTPBearer):

```python
import llmhub_generated
from llmhub_generated.models.send_invitations_request import SendInvitationsRequest
from llmhub_generated.models.send_invitations_response import SendInvitationsResponse
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
    api_instance = llmhub_generated.InvitationsApi(api_client)
    send_invitations_request = llmhub_generated.SendInvitationsRequest() # SendInvitationsRequest | 
    session_token = 'session_token_example' # str |  (optional)

    try:
        # Send Invitations
        api_response = api_instance.send_invitations_api_v1_invitations_send_post_0(send_invitations_request, session_token=session_token)
        print("The response of InvitationsApi->send_invitations_api_v1_invitations_send_post_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvitationsApi->send_invitations_api_v1_invitations_send_post_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **send_invitations_request** | [**SendInvitationsRequest**](SendInvitationsRequest.md)|  | 
 **session_token** | **str**|  | [optional] 

### Return type

[**SendInvitationsResponse**](SendInvitationsResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

