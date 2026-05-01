# llmhub_generated.AuthenticationApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**forgot_password_api_v1_auth_forgot_password_post**](AuthenticationApi.md#forgot_password_api_v1_auth_forgot_password_post) | **POST** /api/v1/auth/forgot-password | Forgot Password
[**forgot_password_api_v1_auth_forgot_password_post_0**](AuthenticationApi.md#forgot_password_api_v1_auth_forgot_password_post_0) | **POST** /api/v1/auth/forgot-password | Forgot Password
[**get_current_user_info_api_v1_auth_me_get**](AuthenticationApi.md#get_current_user_info_api_v1_auth_me_get) | **GET** /api/v1/auth/me | Get Current User Info
[**get_current_user_info_api_v1_auth_me_get_0**](AuthenticationApi.md#get_current_user_info_api_v1_auth_me_get_0) | **GET** /api/v1/auth/me | Get Current User Info
[**get_oauth_providers_api_v1_auth_oauth_providers_get**](AuthenticationApi.md#get_oauth_providers_api_v1_auth_oauth_providers_get) | **GET** /api/v1/auth/oauth/providers | Get Oauth Providers
[**get_oauth_providers_api_v1_auth_oauth_providers_get_0**](AuthenticationApi.md#get_oauth_providers_api_v1_auth_oauth_providers_get_0) | **GET** /api/v1/auth/oauth/providers | Get Oauth Providers
[**login_api_v1_auth_login_post**](AuthenticationApi.md#login_api_v1_auth_login_post) | **POST** /api/v1/auth/login | Login
[**login_api_v1_auth_login_post_0**](AuthenticationApi.md#login_api_v1_auth_login_post_0) | **POST** /api/v1/auth/login | Login
[**logout_api_v1_auth_logout_post**](AuthenticationApi.md#logout_api_v1_auth_logout_post) | **POST** /api/v1/auth/logout | Logout
[**logout_api_v1_auth_logout_post_0**](AuthenticationApi.md#logout_api_v1_auth_logout_post_0) | **POST** /api/v1/auth/logout | Logout
[**oauth_callback_api_v1_auth_oauth_provider_callback_get**](AuthenticationApi.md#oauth_callback_api_v1_auth_oauth_provider_callback_get) | **GET** /api/v1/auth/oauth/{provider}/callback | Oauth Callback
[**oauth_callback_api_v1_auth_oauth_provider_callback_get_0**](AuthenticationApi.md#oauth_callback_api_v1_auth_oauth_provider_callback_get_0) | **GET** /api/v1/auth/oauth/{provider}/callback | Oauth Callback
[**oauth_login_api_v1_auth_oauth_provider_get**](AuthenticationApi.md#oauth_login_api_v1_auth_oauth_provider_get) | **GET** /api/v1/auth/oauth/{provider} | Oauth Login
[**oauth_login_api_v1_auth_oauth_provider_get_0**](AuthenticationApi.md#oauth_login_api_v1_auth_oauth_provider_get_0) | **GET** /api/v1/auth/oauth/{provider} | Oauth Login
[**oauth_register_api_v1_auth_oauth_provider_register_post**](AuthenticationApi.md#oauth_register_api_v1_auth_oauth_provider_register_post) | **POST** /api/v1/auth/oauth/{provider}/register | Oauth Register
[**oauth_register_api_v1_auth_oauth_provider_register_post_0**](AuthenticationApi.md#oauth_register_api_v1_auth_oauth_provider_register_post_0) | **POST** /api/v1/auth/oauth/{provider}/register | Oauth Register
[**refresh_token_api_v1_auth_refresh_post**](AuthenticationApi.md#refresh_token_api_v1_auth_refresh_post) | **POST** /api/v1/auth/refresh | Refresh Token
[**refresh_token_api_v1_auth_refresh_post_0**](AuthenticationApi.md#refresh_token_api_v1_auth_refresh_post_0) | **POST** /api/v1/auth/refresh | Refresh Token
[**register_api_v1_auth_register_post**](AuthenticationApi.md#register_api_v1_auth_register_post) | **POST** /api/v1/auth/register | Register
[**register_api_v1_auth_register_post_0**](AuthenticationApi.md#register_api_v1_auth_register_post_0) | **POST** /api/v1/auth/register | Register
[**resend_verification_email_api_v1_auth_resend_verification_post**](AuthenticationApi.md#resend_verification_email_api_v1_auth_resend_verification_post) | **POST** /api/v1/auth/resend-verification | Resend Verification Email
[**resend_verification_email_api_v1_auth_resend_verification_post_0**](AuthenticationApi.md#resend_verification_email_api_v1_auth_resend_verification_post_0) | **POST** /api/v1/auth/resend-verification | Resend Verification Email
[**reset_password_api_v1_auth_reset_password_post**](AuthenticationApi.md#reset_password_api_v1_auth_reset_password_post) | **POST** /api/v1/auth/reset-password | Reset Password
[**reset_password_api_v1_auth_reset_password_post_0**](AuthenticationApi.md#reset_password_api_v1_auth_reset_password_post_0) | **POST** /api/v1/auth/reset-password | Reset Password
[**verify_email_api_v1_auth_verify_email_token_get**](AuthenticationApi.md#verify_email_api_v1_auth_verify_email_token_get) | **GET** /api/v1/auth/verify-email/{token} | Verify Email
[**verify_email_api_v1_auth_verify_email_token_get_0**](AuthenticationApi.md#verify_email_api_v1_auth_verify_email_token_get_0) | **GET** /api/v1/auth/verify-email/{token} | Verify Email
[**verify_token_api_v1_auth_verify_get**](AuthenticationApi.md#verify_token_api_v1_auth_verify_get) | **GET** /api/v1/auth/verify | Verify Token
[**verify_token_api_v1_auth_verify_get_0**](AuthenticationApi.md#verify_token_api_v1_auth_verify_get_0) | **GET** /api/v1/auth/verify | Verify Token


# **forgot_password_api_v1_auth_forgot_password_post**
> object forgot_password_api_v1_auth_forgot_password_post(email)

Forgot Password

Request password reset email

Sends a password reset link to the user's email address.
Returns success even if email doesn't exist (security best practice).

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
    api_instance = llmhub_generated.AuthenticationApi(api_client)
    email = 'email_example' # str | 

    try:
        # Forgot Password
        api_response = api_instance.forgot_password_api_v1_auth_forgot_password_post(email)
        print("The response of AuthenticationApi->forgot_password_api_v1_auth_forgot_password_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->forgot_password_api_v1_auth_forgot_password_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**|  | 

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

# **forgot_password_api_v1_auth_forgot_password_post_0**
> object forgot_password_api_v1_auth_forgot_password_post_0(email)

Forgot Password

Request password reset email

Sends a password reset link to the user's email address.
Returns success even if email doesn't exist (security best practice).

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
    api_instance = llmhub_generated.AuthenticationApi(api_client)
    email = 'email_example' # str | 

    try:
        # Forgot Password
        api_response = api_instance.forgot_password_api_v1_auth_forgot_password_post_0(email)
        print("The response of AuthenticationApi->forgot_password_api_v1_auth_forgot_password_post_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->forgot_password_api_v1_auth_forgot_password_post_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**|  | 

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

# **get_current_user_info_api_v1_auth_me_get**
> UserResponse get_current_user_info_api_v1_auth_me_get(session_token=session_token)

Get Current User Info

Get current authenticated user information

Returns detailed information about the currently logged-in user,
including roles and organization.

### Example

* Bearer Authentication (HTTPBearer):

```python
import llmhub_generated
from llmhub_generated.models.user_response import UserResponse
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
    api_instance = llmhub_generated.AuthenticationApi(api_client)
    session_token = 'session_token_example' # str |  (optional)

    try:
        # Get Current User Info
        api_response = api_instance.get_current_user_info_api_v1_auth_me_get(session_token=session_token)
        print("The response of AuthenticationApi->get_current_user_info_api_v1_auth_me_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->get_current_user_info_api_v1_auth_me_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_token** | **str**|  | [optional] 

### Return type

[**UserResponse**](UserResponse.md)

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

# **get_current_user_info_api_v1_auth_me_get_0**
> UserResponse get_current_user_info_api_v1_auth_me_get_0(session_token=session_token)

Get Current User Info

Get current authenticated user information

Returns detailed information about the currently logged-in user,
including roles and organization.

### Example

* Bearer Authentication (HTTPBearer):

```python
import llmhub_generated
from llmhub_generated.models.user_response import UserResponse
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
    api_instance = llmhub_generated.AuthenticationApi(api_client)
    session_token = 'session_token_example' # str |  (optional)

    try:
        # Get Current User Info
        api_response = api_instance.get_current_user_info_api_v1_auth_me_get_0(session_token=session_token)
        print("The response of AuthenticationApi->get_current_user_info_api_v1_auth_me_get_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->get_current_user_info_api_v1_auth_me_get_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_token** | **str**|  | [optional] 

### Return type

[**UserResponse**](UserResponse.md)

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

# **get_oauth_providers_api_v1_auth_oauth_providers_get**
> object get_oauth_providers_api_v1_auth_oauth_providers_get()

Get Oauth Providers

Get list of configured OAuth providers

Returns list of available OAuth providers that can be used for authentication.

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
    api_instance = llmhub_generated.AuthenticationApi(api_client)

    try:
        # Get Oauth Providers
        api_response = api_instance.get_oauth_providers_api_v1_auth_oauth_providers_get()
        print("The response of AuthenticationApi->get_oauth_providers_api_v1_auth_oauth_providers_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->get_oauth_providers_api_v1_auth_oauth_providers_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_oauth_providers_api_v1_auth_oauth_providers_get_0**
> object get_oauth_providers_api_v1_auth_oauth_providers_get_0()

Get Oauth Providers

Get list of configured OAuth providers

Returns list of available OAuth providers that can be used for authentication.

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
    api_instance = llmhub_generated.AuthenticationApi(api_client)

    try:
        # Get Oauth Providers
        api_response = api_instance.get_oauth_providers_api_v1_auth_oauth_providers_get_0()
        print("The response of AuthenticationApi->get_oauth_providers_api_v1_auth_oauth_providers_get_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->get_oauth_providers_api_v1_auth_oauth_providers_get_0: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **login_api_v1_auth_login_post**
> TokenResponse login_api_v1_auth_login_post(login_request)

Login

Login with email and password

**Note:** Password authentication is not yet fully implemented.
Use GitHub OAuth for authentication.

### Example


```python
import llmhub_generated
from llmhub_generated.models.login_request import LoginRequest
from llmhub_generated.models.token_response import TokenResponse
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
    api_instance = llmhub_generated.AuthenticationApi(api_client)
    login_request = llmhub_generated.LoginRequest() # LoginRequest | 

    try:
        # Login
        api_response = api_instance.login_api_v1_auth_login_post(login_request)
        print("The response of AuthenticationApi->login_api_v1_auth_login_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->login_api_v1_auth_login_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login_request** | [**LoginRequest**](LoginRequest.md)|  | 

### Return type

[**TokenResponse**](TokenResponse.md)

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

# **login_api_v1_auth_login_post_0**
> TokenResponse login_api_v1_auth_login_post_0(login_request)

Login

Login with email and password

**Note:** Password authentication is not yet fully implemented.
Use GitHub OAuth for authentication.

### Example


```python
import llmhub_generated
from llmhub_generated.models.login_request import LoginRequest
from llmhub_generated.models.token_response import TokenResponse
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
    api_instance = llmhub_generated.AuthenticationApi(api_client)
    login_request = llmhub_generated.LoginRequest() # LoginRequest | 

    try:
        # Login
        api_response = api_instance.login_api_v1_auth_login_post_0(login_request)
        print("The response of AuthenticationApi->login_api_v1_auth_login_post_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->login_api_v1_auth_login_post_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login_request** | [**LoginRequest**](LoginRequest.md)|  | 

### Return type

[**TokenResponse**](TokenResponse.md)

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

# **logout_api_v1_auth_logout_post**
> object logout_api_v1_auth_logout_post(session_token=session_token)

Logout

Logout and invalidate current session

Clears session cookie and invalidates tokens.

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
    api_instance = llmhub_generated.AuthenticationApi(api_client)
    session_token = 'session_token_example' # str |  (optional)

    try:
        # Logout
        api_response = api_instance.logout_api_v1_auth_logout_post(session_token=session_token)
        print("The response of AuthenticationApi->logout_api_v1_auth_logout_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->logout_api_v1_auth_logout_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **logout_api_v1_auth_logout_post_0**
> object logout_api_v1_auth_logout_post_0(session_token=session_token)

Logout

Logout and invalidate current session

Clears session cookie and invalidates tokens.

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
    api_instance = llmhub_generated.AuthenticationApi(api_client)
    session_token = 'session_token_example' # str |  (optional)

    try:
        # Logout
        api_response = api_instance.logout_api_v1_auth_logout_post_0(session_token=session_token)
        print("The response of AuthenticationApi->logout_api_v1_auth_logout_post_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->logout_api_v1_auth_logout_post_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **oauth_callback_api_v1_auth_oauth_provider_callback_get**
> object oauth_callback_api_v1_auth_oauth_provider_callback_get(provider, code, state=state)

Oauth Callback

OAuth callback endpoint

Handles the redirect from OAuth provider after user authorizes.

**This endpoint is called by the OAuth provider, not directly by the client.**

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
    api_instance = llmhub_generated.AuthenticationApi(api_client)
    provider = 'provider_example' # str | 
    code = 'code_example' # str | 
    state = 'state_example' # str |  (optional)

    try:
        # Oauth Callback
        api_response = api_instance.oauth_callback_api_v1_auth_oauth_provider_callback_get(provider, code, state=state)
        print("The response of AuthenticationApi->oauth_callback_api_v1_auth_oauth_provider_callback_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->oauth_callback_api_v1_auth_oauth_provider_callback_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | 
 **code** | **str**|  | 
 **state** | **str**|  | [optional] 

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

# **oauth_callback_api_v1_auth_oauth_provider_callback_get_0**
> object oauth_callback_api_v1_auth_oauth_provider_callback_get_0(provider, code, state=state)

Oauth Callback

OAuth callback endpoint

Handles the redirect from OAuth provider after user authorizes.

**This endpoint is called by the OAuth provider, not directly by the client.**

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
    api_instance = llmhub_generated.AuthenticationApi(api_client)
    provider = 'provider_example' # str | 
    code = 'code_example' # str | 
    state = 'state_example' # str |  (optional)

    try:
        # Oauth Callback
        api_response = api_instance.oauth_callback_api_v1_auth_oauth_provider_callback_get_0(provider, code, state=state)
        print("The response of AuthenticationApi->oauth_callback_api_v1_auth_oauth_provider_callback_get_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->oauth_callback_api_v1_auth_oauth_provider_callback_get_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | 
 **code** | **str**|  | 
 **state** | **str**|  | [optional] 

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

# **oauth_login_api_v1_auth_oauth_provider_get**
> object oauth_login_api_v1_auth_oauth_provider_get(provider)

Oauth Login

Initiate OAuth flow for a provider

Redirects user to OAuth provider's authorization page.

**Supported providers:** github, google (coming soon), linkedin (coming soon)

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
    api_instance = llmhub_generated.AuthenticationApi(api_client)
    provider = 'provider_example' # str | 

    try:
        # Oauth Login
        api_response = api_instance.oauth_login_api_v1_auth_oauth_provider_get(provider)
        print("The response of AuthenticationApi->oauth_login_api_v1_auth_oauth_provider_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->oauth_login_api_v1_auth_oauth_provider_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | 

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

# **oauth_login_api_v1_auth_oauth_provider_get_0**
> object oauth_login_api_v1_auth_oauth_provider_get_0(provider)

Oauth Login

Initiate OAuth flow for a provider

Redirects user to OAuth provider's authorization page.

**Supported providers:** github, google (coming soon), linkedin (coming soon)

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
    api_instance = llmhub_generated.AuthenticationApi(api_client)
    provider = 'provider_example' # str | 

    try:
        # Oauth Login
        api_response = api_instance.oauth_login_api_v1_auth_oauth_provider_get_0(provider)
        print("The response of AuthenticationApi->oauth_login_api_v1_auth_oauth_provider_get_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->oauth_login_api_v1_auth_oauth_provider_get_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | 

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

# **oauth_register_api_v1_auth_oauth_provider_register_post**
> TokenResponse oauth_register_api_v1_auth_oauth_provider_register_post(provider, register_request)

Oauth Register

Complete OAuth registration with organization details

After OAuth callback returns registration_required, call this endpoint
to complete registration and create the organization.

### Example


```python
import llmhub_generated
from llmhub_generated.models.register_request import RegisterRequest
from llmhub_generated.models.token_response import TokenResponse
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
    api_instance = llmhub_generated.AuthenticationApi(api_client)
    provider = 'provider_example' # str | 
    register_request = llmhub_generated.RegisterRequest() # RegisterRequest | 

    try:
        # Oauth Register
        api_response = api_instance.oauth_register_api_v1_auth_oauth_provider_register_post(provider, register_request)
        print("The response of AuthenticationApi->oauth_register_api_v1_auth_oauth_provider_register_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->oauth_register_api_v1_auth_oauth_provider_register_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | 
 **register_request** | [**RegisterRequest**](RegisterRequest.md)|  | 

### Return type

[**TokenResponse**](TokenResponse.md)

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

# **oauth_register_api_v1_auth_oauth_provider_register_post_0**
> TokenResponse oauth_register_api_v1_auth_oauth_provider_register_post_0(provider, register_request)

Oauth Register

Complete OAuth registration with organization details

After OAuth callback returns registration_required, call this endpoint
to complete registration and create the organization.

### Example


```python
import llmhub_generated
from llmhub_generated.models.register_request import RegisterRequest
from llmhub_generated.models.token_response import TokenResponse
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
    api_instance = llmhub_generated.AuthenticationApi(api_client)
    provider = 'provider_example' # str | 
    register_request = llmhub_generated.RegisterRequest() # RegisterRequest | 

    try:
        # Oauth Register
        api_response = api_instance.oauth_register_api_v1_auth_oauth_provider_register_post_0(provider, register_request)
        print("The response of AuthenticationApi->oauth_register_api_v1_auth_oauth_provider_register_post_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->oauth_register_api_v1_auth_oauth_provider_register_post_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | 
 **register_request** | [**RegisterRequest**](RegisterRequest.md)|  | 

### Return type

[**TokenResponse**](TokenResponse.md)

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

# **refresh_token_api_v1_auth_refresh_post**
> TokenResponse refresh_token_api_v1_auth_refresh_post(refresh_token_request)

Refresh Token

Refresh access token using refresh token

Generates a new access token and refresh token pair.
The old refresh token is invalidated.

### Example


```python
import llmhub_generated
from llmhub_generated.models.refresh_token_request import RefreshTokenRequest
from llmhub_generated.models.token_response import TokenResponse
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
    api_instance = llmhub_generated.AuthenticationApi(api_client)
    refresh_token_request = llmhub_generated.RefreshTokenRequest() # RefreshTokenRequest | 

    try:
        # Refresh Token
        api_response = api_instance.refresh_token_api_v1_auth_refresh_post(refresh_token_request)
        print("The response of AuthenticationApi->refresh_token_api_v1_auth_refresh_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->refresh_token_api_v1_auth_refresh_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **refresh_token_request** | [**RefreshTokenRequest**](RefreshTokenRequest.md)|  | 

### Return type

[**TokenResponse**](TokenResponse.md)

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

# **refresh_token_api_v1_auth_refresh_post_0**
> TokenResponse refresh_token_api_v1_auth_refresh_post_0(refresh_token_request)

Refresh Token

Refresh access token using refresh token

Generates a new access token and refresh token pair.
The old refresh token is invalidated.

### Example


```python
import llmhub_generated
from llmhub_generated.models.refresh_token_request import RefreshTokenRequest
from llmhub_generated.models.token_response import TokenResponse
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
    api_instance = llmhub_generated.AuthenticationApi(api_client)
    refresh_token_request = llmhub_generated.RefreshTokenRequest() # RefreshTokenRequest | 

    try:
        # Refresh Token
        api_response = api_instance.refresh_token_api_v1_auth_refresh_post_0(refresh_token_request)
        print("The response of AuthenticationApi->refresh_token_api_v1_auth_refresh_post_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->refresh_token_api_v1_auth_refresh_post_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **refresh_token_request** | [**RefreshTokenRequest**](RefreshTokenRequest.md)|  | 

### Return type

[**TokenResponse**](TokenResponse.md)

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

# **register_api_v1_auth_register_post**
> TokenResponse register_api_v1_auth_register_post(register_request)

Register

Register a new user with email and password

- If org_name is provided: Creates user with organization (user becomes org_admin)
- If org_name is not provided: Creates individual user (can join/create org later)
- If invitation_token is provided: Inviter becomes user's Super-Dev

### Example


```python
import llmhub_generated
from llmhub_generated.models.register_request import RegisterRequest
from llmhub_generated.models.token_response import TokenResponse
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
    api_instance = llmhub_generated.AuthenticationApi(api_client)
    register_request = llmhub_generated.RegisterRequest() # RegisterRequest | 

    try:
        # Register
        api_response = api_instance.register_api_v1_auth_register_post(register_request)
        print("The response of AuthenticationApi->register_api_v1_auth_register_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->register_api_v1_auth_register_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **register_request** | [**RegisterRequest**](RegisterRequest.md)|  | 

### Return type

[**TokenResponse**](TokenResponse.md)

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

# **register_api_v1_auth_register_post_0**
> TokenResponse register_api_v1_auth_register_post_0(register_request)

Register

Register a new user with email and password

- If org_name is provided: Creates user with organization (user becomes org_admin)
- If org_name is not provided: Creates individual user (can join/create org later)
- If invitation_token is provided: Inviter becomes user's Super-Dev

### Example


```python
import llmhub_generated
from llmhub_generated.models.register_request import RegisterRequest
from llmhub_generated.models.token_response import TokenResponse
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
    api_instance = llmhub_generated.AuthenticationApi(api_client)
    register_request = llmhub_generated.RegisterRequest() # RegisterRequest | 

    try:
        # Register
        api_response = api_instance.register_api_v1_auth_register_post_0(register_request)
        print("The response of AuthenticationApi->register_api_v1_auth_register_post_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->register_api_v1_auth_register_post_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **register_request** | [**RegisterRequest**](RegisterRequest.md)|  | 

### Return type

[**TokenResponse**](TokenResponse.md)

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

# **resend_verification_email_api_v1_auth_resend_verification_post**
> object resend_verification_email_api_v1_auth_resend_verification_post(session_token=session_token)

Resend Verification Email

Resend email verification link

Authenticated users can request a new verification email if they lost the original.

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
    api_instance = llmhub_generated.AuthenticationApi(api_client)
    session_token = 'session_token_example' # str |  (optional)

    try:
        # Resend Verification Email
        api_response = api_instance.resend_verification_email_api_v1_auth_resend_verification_post(session_token=session_token)
        print("The response of AuthenticationApi->resend_verification_email_api_v1_auth_resend_verification_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->resend_verification_email_api_v1_auth_resend_verification_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **resend_verification_email_api_v1_auth_resend_verification_post_0**
> object resend_verification_email_api_v1_auth_resend_verification_post_0(session_token=session_token)

Resend Verification Email

Resend email verification link

Authenticated users can request a new verification email if they lost the original.

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
    api_instance = llmhub_generated.AuthenticationApi(api_client)
    session_token = 'session_token_example' # str |  (optional)

    try:
        # Resend Verification Email
        api_response = api_instance.resend_verification_email_api_v1_auth_resend_verification_post_0(session_token=session_token)
        print("The response of AuthenticationApi->resend_verification_email_api_v1_auth_resend_verification_post_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->resend_verification_email_api_v1_auth_resend_verification_post_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **reset_password_api_v1_auth_reset_password_post**
> object reset_password_api_v1_auth_reset_password_post(token, new_password)

Reset Password

Reset password using token from email

Users provide the token from their email and a new password.

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
    api_instance = llmhub_generated.AuthenticationApi(api_client)
    token = 'token_example' # str | 
    new_password = 'new_password_example' # str | 

    try:
        # Reset Password
        api_response = api_instance.reset_password_api_v1_auth_reset_password_post(token, new_password)
        print("The response of AuthenticationApi->reset_password_api_v1_auth_reset_password_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->reset_password_api_v1_auth_reset_password_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**|  | 
 **new_password** | **str**|  | 

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

# **reset_password_api_v1_auth_reset_password_post_0**
> object reset_password_api_v1_auth_reset_password_post_0(token, new_password)

Reset Password

Reset password using token from email

Users provide the token from their email and a new password.

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
    api_instance = llmhub_generated.AuthenticationApi(api_client)
    token = 'token_example' # str | 
    new_password = 'new_password_example' # str | 

    try:
        # Reset Password
        api_response = api_instance.reset_password_api_v1_auth_reset_password_post_0(token, new_password)
        print("The response of AuthenticationApi->reset_password_api_v1_auth_reset_password_post_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->reset_password_api_v1_auth_reset_password_post_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**|  | 
 **new_password** | **str**|  | 

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

# **verify_email_api_v1_auth_verify_email_token_get**
> object verify_email_api_v1_auth_verify_email_token_get(token)

Verify Email

Verify email address using token from email

Users click the link in their verification email to verify their account.

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
    api_instance = llmhub_generated.AuthenticationApi(api_client)
    token = 'token_example' # str | 

    try:
        # Verify Email
        api_response = api_instance.verify_email_api_v1_auth_verify_email_token_get(token)
        print("The response of AuthenticationApi->verify_email_api_v1_auth_verify_email_token_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->verify_email_api_v1_auth_verify_email_token_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**|  | 

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

# **verify_email_api_v1_auth_verify_email_token_get_0**
> object verify_email_api_v1_auth_verify_email_token_get_0(token)

Verify Email

Verify email address using token from email

Users click the link in their verification email to verify their account.

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
    api_instance = llmhub_generated.AuthenticationApi(api_client)
    token = 'token_example' # str | 

    try:
        # Verify Email
        api_response = api_instance.verify_email_api_v1_auth_verify_email_token_get_0(token)
        print("The response of AuthenticationApi->verify_email_api_v1_auth_verify_email_token_get_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->verify_email_api_v1_auth_verify_email_token_get_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**|  | 

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

# **verify_token_api_v1_auth_verify_get**
> object verify_token_api_v1_auth_verify_get(session_token=session_token)

Verify Token

Verify if current token is valid

Simple endpoint to check if the user's access token is still valid.
Returns 200 if valid, 401 if invalid/expired.

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
    api_instance = llmhub_generated.AuthenticationApi(api_client)
    session_token = 'session_token_example' # str |  (optional)

    try:
        # Verify Token
        api_response = api_instance.verify_token_api_v1_auth_verify_get(session_token=session_token)
        print("The response of AuthenticationApi->verify_token_api_v1_auth_verify_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->verify_token_api_v1_auth_verify_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **verify_token_api_v1_auth_verify_get_0**
> object verify_token_api_v1_auth_verify_get_0(session_token=session_token)

Verify Token

Verify if current token is valid

Simple endpoint to check if the user's access token is still valid.
Returns 200 if valid, 401 if invalid/expired.

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
    api_instance = llmhub_generated.AuthenticationApi(api_client)
    session_token = 'session_token_example' # str |  (optional)

    try:
        # Verify Token
        api_response = api_instance.verify_token_api_v1_auth_verify_get_0(session_token=session_token)
        print("The response of AuthenticationApi->verify_token_api_v1_auth_verify_get_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->verify_token_api_v1_auth_verify_get_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

