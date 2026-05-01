# llmhub_generated.AdminApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_client_api_v1_admin_clients_post**](AdminApi.md#create_client_api_v1_admin_clients_post) | **POST** /api/v1/admin/clients | Create Client
[**create_dynamic_provider_api_v1_admin_providers_create_post**](AdminApi.md#create_dynamic_provider_api_v1_admin_providers_create_post) | **POST** /api/v1/admin/providers/create | Create Dynamic Provider
[**create_model_type_api_v1_admin_model_types_post**](AdminApi.md#create_model_type_api_v1_admin_model_types_post) | **POST** /api/v1/admin/model-types | Create Model Type
[**delete_client_api_v1_admin_clients_client_id_delete**](AdminApi.md#delete_client_api_v1_admin_clients_client_id_delete) | **DELETE** /api/v1/admin/clients/{client_id} | Delete Client
[**delete_model_type_api_v1_admin_model_types_type_id_delete**](AdminApi.md#delete_model_type_api_v1_admin_model_types_type_id_delete) | **DELETE** /api/v1/admin/model-types/{type_id} | Delete Model Type
[**delete_provider_api_key_api_v1_admin_providers_provider_key_api_key_delete**](AdminApi.md#delete_provider_api_key_api_v1_admin_providers_provider_key_api_key_delete) | **DELETE** /api/v1/admin/providers/{provider_key}/api-key | Delete Provider Api Key
[**delete_test_history_item_api_v1_admin_test_history_log_id_delete**](AdminApi.md#delete_test_history_item_api_v1_admin_test_history_log_id_delete) | **DELETE** /api/v1/admin/test-history/{log_id} | Delete Test History Item
[**get_all_models_api_v1_admin_models_get**](AdminApi.md#get_all_models_api_v1_admin_models_get) | **GET** /api/v1/admin/models | Get All Models
[**get_billing_stats_api_v1_admin_billing_stats_get**](AdminApi.md#get_billing_stats_api_v1_admin_billing_stats_get) | **GET** /api/v1/admin/billing/stats | Get Billing Stats
[**get_budget_forecast_api_v1_admin_organizations_org_id_budget_forecast_get**](AdminApi.md#get_budget_forecast_api_v1_admin_organizations_org_id_budget_forecast_get) | **GET** /api/v1/admin/organizations/{org_id}/budget-forecast | Get Budget Forecast
[**get_client_costs_api_v1_admin_billing_by_client_get**](AdminApi.md#get_client_costs_api_v1_admin_billing_by_client_get) | **GET** /api/v1/admin/billing/by-client | Get Client Costs
[**get_client_health_api_v1_admin_organizations_org_id_client_health_get**](AdminApi.md#get_client_health_api_v1_admin_organizations_org_id_client_health_get) | **GET** /api/v1/admin/organizations/{org_id}/client-health | Get Client Health
[**get_client_stats_api_v1_admin_clients_client_id_stats_get**](AdminApi.md#get_client_stats_api_v1_admin_clients_client_id_stats_get) | **GET** /api/v1/admin/clients/{client_id}/stats | Get Client Stats
[**get_clients_api_v1_admin_clients_get**](AdminApi.md#get_clients_api_v1_admin_clients_get) | **GET** /api/v1/admin/clients | Get Clients
[**get_cost_optimization_api_v1_admin_organizations_org_id_cost_optimization_get**](AdminApi.md#get_cost_optimization_api_v1_admin_organizations_org_id_cost_optimization_get) | **GET** /api/v1/admin/organizations/{org_id}/cost-optimization | Get Cost Optimization
[**get_daily_costs_api_v1_admin_billing_daily_get**](AdminApi.md#get_daily_costs_api_v1_admin_billing_daily_get) | **GET** /api/v1/admin/billing/daily | Get Daily Costs
[**get_daily_system_metrics_api_v1_admin_system_daily_metrics_get**](AdminApi.md#get_daily_system_metrics_api_v1_admin_system_daily_metrics_get) | **GET** /api/v1/admin/system/daily-metrics | Get Daily System Metrics
[**get_dashboard_stats_api_v1_admin_stats_get**](AdminApi.md#get_dashboard_stats_api_v1_admin_stats_get) | **GET** /api/v1/admin/stats | Get Dashboard Stats
[**get_endpoint_catalog_pricing_api_v1_admin_pricing_endpoints_get**](AdminApi.md#get_endpoint_catalog_pricing_api_v1_admin_pricing_endpoints_get) | **GET** /api/v1/admin/pricing/endpoints | Get Endpoint Catalog Pricing
[**get_growth_metrics_api_v1_admin_system_growth_metrics_get**](AdminApi.md#get_growth_metrics_api_v1_admin_system_growth_metrics_get) | **GET** /api/v1/admin/system/growth-metrics | Get Growth Metrics
[**get_margin_analysis_api_v1_admin_billing_margin_analysis_get**](AdminApi.md#get_margin_analysis_api_v1_admin_billing_margin_analysis_get) | **GET** /api/v1/admin/billing/margin-analysis | Get Margin Analysis
[**get_model_types_api_v1_admin_model_types_get**](AdminApi.md#get_model_types_api_v1_admin_model_types_get) | **GET** /api/v1/admin/model-types | Get Model Types
[**get_model_usage_stats_api_v1_admin_system_model_usage_get**](AdminApi.md#get_model_usage_stats_api_v1_admin_system_model_usage_get) | **GET** /api/v1/admin/system/model-usage | Get Model Usage Stats
[**get_org_analytics_api_v1_admin_organizations_org_id_analytics_get**](AdminApi.md#get_org_analytics_api_v1_admin_organizations_org_id_analytics_get) | **GET** /api/v1/admin/organizations/{org_id}/analytics | Get Org Analytics
[**get_organization_rankings_api_v1_admin_system_organization_rankings_get**](AdminApi.md#get_organization_rankings_api_v1_admin_system_organization_rankings_get) | **GET** /api/v1/admin/system/organization-rankings | Get Organization Rankings
[**get_organizations_api_v1_admin_billing_organizations_get**](AdminApi.md#get_organizations_api_v1_admin_billing_organizations_get) | **GET** /api/v1/admin/billing/organizations | Get Organizations
[**get_provider_costs_api_v1_admin_billing_by_provider_get**](AdminApi.md#get_provider_costs_api_v1_admin_billing_by_provider_get) | **GET** /api/v1/admin/billing/by-provider | Get Provider Costs
[**get_provider_detail_api_v1_admin_providers_provider_key_detail_get**](AdminApi.md#get_provider_detail_api_v1_admin_providers_provider_key_detail_get) | **GET** /api/v1/admin/providers/{provider_key}/detail | Get Provider Detail
[**get_provider_models_api_v1_admin_providers_provider_id_models_get**](AdminApi.md#get_provider_models_api_v1_admin_providers_provider_id_models_get) | **GET** /api/v1/admin/providers/{provider_id}/models | Get Provider Models
[**get_provider_models_detailed_api_v1_admin_providers_provider_key_models_detailed_get**](AdminApi.md#get_provider_models_detailed_api_v1_admin_providers_provider_key_models_detailed_get) | **GET** /api/v1/admin/providers/{provider_key}/models/detailed | Get Provider Models Detailed
[**get_provider_performance_api_v1_admin_system_provider_performance_get**](AdminApi.md#get_provider_performance_api_v1_admin_system_provider_performance_get) | **GET** /api/v1/admin/system/provider-performance | Get Provider Performance
[**get_provider_templates_api_v1_admin_provider_templates_get**](AdminApi.md#get_provider_templates_api_v1_admin_provider_templates_get) | **GET** /api/v1/admin/provider-templates | Get Provider Templates
[**get_provider_usage_api_v1_admin_providers_provider_key_usage_get**](AdminApi.md#get_provider_usage_api_v1_admin_providers_provider_key_usage_get) | **GET** /api/v1/admin/providers/{provider_key}/usage | Get Provider Usage
[**get_providers_from_registry_api_v1_admin_providers_registry_get**](AdminApi.md#get_providers_from_registry_api_v1_admin_providers_registry_get) | **GET** /api/v1/admin/providers/registry | Get Providers From Registry
[**get_providers_list_api_v1_admin_providers_get**](AdminApi.md#get_providers_list_api_v1_admin_providers_get) | **GET** /api/v1/admin/providers | Get Providers List
[**get_revenue_metrics_api_v1_admin_billing_revenue_get**](AdminApi.md#get_revenue_metrics_api_v1_admin_billing_revenue_get) | **GET** /api/v1/admin/billing/revenue | Get Revenue Metrics
[**get_system_audit_logs_api_v1_admin_system_audit_logs_get**](AdminApi.md#get_system_audit_logs_api_v1_admin_system_audit_logs_get) | **GET** /api/v1/admin/system/audit-logs | Get System Audit Logs
[**get_system_health_api_v1_admin_system_health_get**](AdminApi.md#get_system_health_api_v1_admin_system_health_get) | **GET** /api/v1/admin/system/health | Get System Health
[**get_system_overview_api_v1_admin_system_overview_get**](AdminApi.md#get_system_overview_api_v1_admin_system_overview_get) | **GET** /api/v1/admin/system/overview | Get System Overview
[**get_team_insights_api_v1_admin_organizations_org_id_team_insights_get**](AdminApi.md#get_team_insights_api_v1_admin_organizations_org_id_team_insights_get) | **GET** /api/v1/admin/organizations/{org_id}/team-insights | Get Team Insights
[**get_test_history_api_v1_admin_test_history_get**](AdminApi.md#get_test_history_api_v1_admin_test_history_get) | **GET** /api/v1/admin/test-history | Get Test History
[**get_user_achievements_api_v1_admin_users_me_achievements_get**](AdminApi.md#get_user_achievements_api_v1_admin_users_me_achievements_get) | **GET** /api/v1/admin/users/me/achievements | Get User Achievements
[**get_user_activity_api_v1_admin_users_me_activity_get**](AdminApi.md#get_user_activity_api_v1_admin_users_me_activity_get) | **GET** /api/v1/admin/users/me/activity | Get User Activity
[**get_user_daily_activity_api_v1_admin_users_me_daily_activity_get**](AdminApi.md#get_user_daily_activity_api_v1_admin_users_me_daily_activity_get) | **GET** /api/v1/admin/users/me/daily-activity | Get User Daily Activity
[**get_user_overview_api_v1_admin_users_me_overview_get**](AdminApi.md#get_user_overview_api_v1_admin_users_me_overview_get) | **GET** /api/v1/admin/users/me/overview | Get User Overview
[**get_user_preferences_api_v1_admin_users_me_preferences_get**](AdminApi.md#get_user_preferences_api_v1_admin_users_me_preferences_get) | **GET** /api/v1/admin/users/me/preferences | Get User Preferences
[**regenerate_api_key_api_v1_admin_clients_client_id_regenerate_key_post**](AdminApi.md#regenerate_api_key_api_v1_admin_clients_client_id_regenerate_key_post) | **POST** /api/v1/admin/clients/{client_id}/regenerate-key | Regenerate Api Key
[**register_provider_api_v1_admin_providers_provider_key_register_post**](AdminApi.md#register_provider_api_v1_admin_providers_provider_key_register_post) | **POST** /api/v1/admin/providers/{provider_key}/register | Register Provider
[**test_prompt_api_v1_admin_test_prompt_post**](AdminApi.md#test_prompt_api_v1_admin_test_prompt_post) | **POST** /api/v1/admin/test-prompt | Test Prompt
[**test_provider_api_key_api_v1_admin_providers_provider_key_test_key_post**](AdminApi.md#test_provider_api_key_api_v1_admin_providers_provider_key_test_key_post) | **POST** /api/v1/admin/providers/{provider_key}/test-key | Test Provider Api Key
[**toggle_model_api_v1_admin_models_model_id_toggle_post**](AdminApi.md#toggle_model_api_v1_admin_models_model_id_toggle_post) | **POST** /api/v1/admin/models/{model_id}/toggle | Toggle Model
[**update_client_api_v1_admin_clients_client_id_patch**](AdminApi.md#update_client_api_v1_admin_clients_client_id_patch) | **PATCH** /api/v1/admin/clients/{client_id} | Update Client
[**update_endpoint_pricing_api_v1_admin_pricing_endpoints_endpoint_id_patch**](AdminApi.md#update_endpoint_pricing_api_v1_admin_pricing_endpoints_endpoint_id_patch) | **PATCH** /api/v1/admin/pricing/endpoints/{endpoint_id} | Update Endpoint Pricing
[**update_model_api_v1_admin_models_model_id_patch**](AdminApi.md#update_model_api_v1_admin_models_model_id_patch) | **PATCH** /api/v1/admin/models/{model_id} | Update Model
[**update_model_type_api_v1_admin_model_types_type_id_patch**](AdminApi.md#update_model_type_api_v1_admin_model_types_type_id_patch) | **PATCH** /api/v1/admin/model-types/{type_id} | Update Model Type
[**update_provider_api_key_api_v1_admin_providers_provider_key_api_key_put**](AdminApi.md#update_provider_api_key_api_v1_admin_providers_provider_key_api_key_put) | **PUT** /api/v1/admin/providers/{provider_key}/api-key | Update Provider Api Key


# **create_client_api_v1_admin_clients_post**
> Dict[str, object] create_client_api_v1_admin_clients_post(request_body)

Create Client

Create a new API client
Generates a secure API key automatically

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
    api_instance = llmhub_generated.AdminApi(api_client)
    request_body = None # Dict[str, object] | 

    try:
        # Create Client
        api_response = api_instance.create_client_api_v1_admin_clients_post(request_body)
        print("The response of AdminApi->create_client_api_v1_admin_clients_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->create_client_api_v1_admin_clients_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**Dict[str, object]**](object.md)|  | 

### Return type

**Dict[str, object]**

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

# **create_dynamic_provider_api_v1_admin_providers_create_post**
> Dict[str, object] create_dynamic_provider_api_v1_admin_providers_create_post(request_body)

Create Dynamic Provider

Create a completely new LLM provider dynamically from the Web UI

Creates:
1. Provider class file in /src/providers/dynamic/
2. Database entries in llm_providers, llm_models
3. Pricing configuration in provider_pricing.yaml
4. Hot-reloads provider without Docker restart

Request Body:
{
    "provider_key": "mistral_custom",  // Unique key (letters, numbers, underscore)
    "display_name": "Mistral Custom",
    "description": "Custom Mistral API instance",
    "logo_url": "https://...",  // Optional
    "website_url": "https://...",  // Optional
    "template_key": "openai_compatible",  // Template to use
    "base_url": "https://api.mistral.ai/v1",  // API base URL
    "auth_header": "Authorization",  // Auth header name
    "api_key": "sk-...",  // API key to store
    "models": [
        {
            "model_key": "mistral-medium",
            "display_name": "Mistral Medium",
            "cost_input": 2.5,  // Per million tokens
            "cost_output": 7.5,
            "model_type": "text"  // text, multimodal, audio, etc.
        }
    ]
}

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
    api_instance = llmhub_generated.AdminApi(api_client)
    request_body = None # Dict[str, object] | 

    try:
        # Create Dynamic Provider
        api_response = api_instance.create_dynamic_provider_api_v1_admin_providers_create_post(request_body)
        print("The response of AdminApi->create_dynamic_provider_api_v1_admin_providers_create_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->create_dynamic_provider_api_v1_admin_providers_create_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**Dict[str, object]**](object.md)|  | 

### Return type

**Dict[str, object]**

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

# **create_model_type_api_v1_admin_model_types_post**
> Dict[str, object] create_model_type_api_v1_admin_model_types_post(request_body)

Create Model Type

Create a new model type category

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
    api_instance = llmhub_generated.AdminApi(api_client)
    request_body = None # Dict[str, object] | 

    try:
        # Create Model Type
        api_response = api_instance.create_model_type_api_v1_admin_model_types_post(request_body)
        print("The response of AdminApi->create_model_type_api_v1_admin_model_types_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->create_model_type_api_v1_admin_model_types_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**Dict[str, object]**](object.md)|  | 

### Return type

**Dict[str, object]**

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

# **delete_client_api_v1_admin_clients_client_id_delete**
> Dict[str, Optional[str]] delete_client_api_v1_admin_clients_client_id_delete(client_id)

Delete Client

Delete an API client

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
    api_instance = llmhub_generated.AdminApi(api_client)
    client_id = 'client_id_example' # str | 

    try:
        # Delete Client
        api_response = api_instance.delete_client_api_v1_admin_clients_client_id_delete(client_id)
        print("The response of AdminApi->delete_client_api_v1_admin_clients_client_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->delete_client_api_v1_admin_clients_client_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**|  | 

### Return type

**Dict[str, Optional[str]]**

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

# **delete_model_type_api_v1_admin_model_types_type_id_delete**
> Dict[str, Optional[str]] delete_model_type_api_v1_admin_model_types_type_id_delete(type_id)

Delete Model Type

Deactivate a model type (soft delete)

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
    api_instance = llmhub_generated.AdminApi(api_client)
    type_id = 'type_id_example' # str | 

    try:
        # Delete Model Type
        api_response = api_instance.delete_model_type_api_v1_admin_model_types_type_id_delete(type_id)
        print("The response of AdminApi->delete_model_type_api_v1_admin_model_types_type_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->delete_model_type_api_v1_admin_model_types_type_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type_id** | **str**|  | 

### Return type

**Dict[str, Optional[str]]**

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

# **delete_provider_api_key_api_v1_admin_providers_provider_key_api_key_delete**
> Dict[str, Optional[str]] delete_provider_api_key_api_v1_admin_providers_provider_key_api_key_delete(provider_key)

Delete Provider Api Key

DEPRECATED: API keys are managed via .env file

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
    api_instance = llmhub_generated.AdminApi(api_client)
    provider_key = 'provider_key_example' # str | 

    try:
        # Delete Provider Api Key
        api_response = api_instance.delete_provider_api_key_api_v1_admin_providers_provider_key_api_key_delete(provider_key)
        print("The response of AdminApi->delete_provider_api_key_api_v1_admin_providers_provider_key_api_key_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->delete_provider_api_key_api_v1_admin_providers_provider_key_api_key_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_key** | **str**|  | 

### Return type

**Dict[str, Optional[str]]**

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

# **delete_test_history_item_api_v1_admin_test_history_log_id_delete**
> Dict[str, Optional[str]] delete_test_history_item_api_v1_admin_test_history_log_id_delete(log_id)

Delete Test History Item

Delete a specific test history item from playground
Removes the log entry from the database

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
    api_instance = llmhub_generated.AdminApi(api_client)
    log_id = 'log_id_example' # str | 

    try:
        # Delete Test History Item
        api_response = api_instance.delete_test_history_item_api_v1_admin_test_history_log_id_delete(log_id)
        print("The response of AdminApi->delete_test_history_item_api_v1_admin_test_history_log_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->delete_test_history_item_api_v1_admin_test_history_log_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **log_id** | **str**|  | 

### Return type

**Dict[str, Optional[str]]**

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

# **get_all_models_api_v1_admin_models_get**
> Dict[str, object] get_all_models_api_v1_admin_models_get(provider_key=provider_key, model_type=model_type, is_enabled=is_enabled, page=page, page_size=page_size)

Get All Models

Get all LLM models with pagination, optionally filtered by provider, model type, and enabled status
Includes usage count from generation logs

Args:
    provider_key: Filter by provider key
    model_type: Filter by model type(s), comma-separated (e.g., 'text,multimodal')
    is_enabled: Filter by enabled status (true/false)

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
    api_instance = llmhub_generated.AdminApi(api_client)
    provider_key = 'provider_key_example' # str |  (optional)
    model_type = 'model_type_example' # str |  (optional)
    is_enabled = True # bool |  (optional)
    page = 1 # int | Page number (optional) (default to 1)
    page_size = 50 # int | Items per page (optional) (default to 50)

    try:
        # Get All Models
        api_response = api_instance.get_all_models_api_v1_admin_models_get(provider_key=provider_key, model_type=model_type, is_enabled=is_enabled, page=page, page_size=page_size)
        print("The response of AdminApi->get_all_models_api_v1_admin_models_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->get_all_models_api_v1_admin_models_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_key** | **str**|  | [optional] 
 **model_type** | **str**|  | [optional] 
 **is_enabled** | **bool**|  | [optional] 
 **page** | **int**| Page number | [optional] [default to 1]
 **page_size** | **int**| Items per page | [optional] [default to 50]

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

# **get_billing_stats_api_v1_admin_billing_stats_get**
> Dict[str, object] get_billing_stats_api_v1_admin_billing_stats_get(days=days, org_id=org_id, client_name=client_name, session_token=session_token)

Get Billing Stats

Get billing statistics for specified time range
Optionally filtered by organization ID and/or client name

**Requires:** super_admin, super_dev, or org_admin role

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
    api_instance = llmhub_generated.AdminApi(api_client)
    days = 30 # int |  (optional) (default to 30)
    org_id = 56 # int |  (optional)
    client_name = 'client_name_example' # str |  (optional)
    session_token = 'session_token_example' # str |  (optional)

    try:
        # Get Billing Stats
        api_response = api_instance.get_billing_stats_api_v1_admin_billing_stats_get(days=days, org_id=org_id, client_name=client_name, session_token=session_token)
        print("The response of AdminApi->get_billing_stats_api_v1_admin_billing_stats_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->get_billing_stats_api_v1_admin_billing_stats_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **days** | **int**|  | [optional] [default to 30]
 **org_id** | **int**|  | [optional] 
 **client_name** | **str**|  | [optional] 
 **session_token** | **str**|  | [optional] 

### Return type

**Dict[str, object]**

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

# **get_budget_forecast_api_v1_admin_organizations_org_id_budget_forecast_get**
> Dict[str, object] get_budget_forecast_api_v1_admin_organizations_org_id_budget_forecast_get(org_id, session_token=session_token)

Get Budget Forecast

Get budget forecasting and alerts

Includes:
- Current budget status
- Burn rate calculation (cost per day)
- End of month projection
- Days until budget exhausted
- Budget status alerts (healthy/caution/warning/critical)

**Permissions:** Requires org_admin for own org or super_admin for any org

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
    api_instance = llmhub_generated.AdminApi(api_client)
    org_id = 56 # int | 
    session_token = 'session_token_example' # str |  (optional)

    try:
        # Get Budget Forecast
        api_response = api_instance.get_budget_forecast_api_v1_admin_organizations_org_id_budget_forecast_get(org_id, session_token=session_token)
        print("The response of AdminApi->get_budget_forecast_api_v1_admin_organizations_org_id_budget_forecast_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->get_budget_forecast_api_v1_admin_organizations_org_id_budget_forecast_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **int**|  | 
 **session_token** | **str**|  | [optional] 

### Return type

**Dict[str, object]**

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

# **get_client_costs_api_v1_admin_billing_by_client_get**
> Dict[str, object] get_client_costs_api_v1_admin_billing_by_client_get(days=days, org_id=org_id, client_name=client_name, page=page, page_size=page_size, session_token=session_token)

Get Client Costs

Get cost breakdown by client with pagination
Optionally filtered by organization and/or client name

**Requires:** super_admin, super_dev, or org_admin role

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
    api_instance = llmhub_generated.AdminApi(api_client)
    days = 30 # int |  (optional) (default to 30)
    org_id = 56 # int |  (optional)
    client_name = 'client_name_example' # str |  (optional)
    page = 1 # int | Page number (optional) (default to 1)
    page_size = 50 # int | Items per page (optional) (default to 50)
    session_token = 'session_token_example' # str |  (optional)

    try:
        # Get Client Costs
        api_response = api_instance.get_client_costs_api_v1_admin_billing_by_client_get(days=days, org_id=org_id, client_name=client_name, page=page, page_size=page_size, session_token=session_token)
        print("The response of AdminApi->get_client_costs_api_v1_admin_billing_by_client_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->get_client_costs_api_v1_admin_billing_by_client_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **days** | **int**|  | [optional] [default to 30]
 **org_id** | **int**|  | [optional] 
 **client_name** | **str**|  | [optional] 
 **page** | **int**| Page number | [optional] [default to 1]
 **page_size** | **int**| Items per page | [optional] [default to 50]
 **session_token** | **str**|  | [optional] 

### Return type

**Dict[str, object]**

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

# **get_client_health_api_v1_admin_organizations_org_id_client_health_get**
> Dict[str, object] get_client_health_api_v1_admin_organizations_org_id_client_health_get(org_id, session_token=session_token)

Get Client Health

Get API client health and performance metrics

Includes for each client:
- Usage statistics (calls, cost)
- Budget status and percentage
- Health status (healthy/warning/critical/idle/inactive)
- Last used timestamp
- Activity indicators

**Permissions:** Requires org_admin for own org or super_admin for any org

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
    api_instance = llmhub_generated.AdminApi(api_client)
    org_id = 56 # int | 
    session_token = 'session_token_example' # str |  (optional)

    try:
        # Get Client Health
        api_response = api_instance.get_client_health_api_v1_admin_organizations_org_id_client_health_get(org_id, session_token=session_token)
        print("The response of AdminApi->get_client_health_api_v1_admin_organizations_org_id_client_health_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->get_client_health_api_v1_admin_organizations_org_id_client_health_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **int**|  | 
 **session_token** | **str**|  | [optional] 

### Return type

**Dict[str, object]**

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

# **get_client_stats_api_v1_admin_clients_client_id_stats_get**
> Dict[str, object] get_client_stats_api_v1_admin_clients_client_id_stats_get(client_id, session_token=session_token)

Get Client Stats

Get detailed statistics for a specific API client
Includes current month usage, budget status, and top models used

**Permissions:** Requires super_admin or org_admin role

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
    api_instance = llmhub_generated.AdminApi(api_client)
    client_id = 'client_id_example' # str | 
    session_token = 'session_token_example' # str |  (optional)

    try:
        # Get Client Stats
        api_response = api_instance.get_client_stats_api_v1_admin_clients_client_id_stats_get(client_id, session_token=session_token)
        print("The response of AdminApi->get_client_stats_api_v1_admin_clients_client_id_stats_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->get_client_stats_api_v1_admin_clients_client_id_stats_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**|  | 
 **session_token** | **str**|  | [optional] 

### Return type

**Dict[str, object]**

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

# **get_clients_api_v1_admin_clients_get**
> Dict[str, object] get_clients_api_v1_admin_clients_get(page=page, page_size=page_size)

Get Clients

Get all API clients with pagination

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
    api_instance = llmhub_generated.AdminApi(api_client)
    page = 1 # int | Page number (optional) (default to 1)
    page_size = 20 # int | Items per page (optional) (default to 20)

    try:
        # Get Clients
        api_response = api_instance.get_clients_api_v1_admin_clients_get(page=page, page_size=page_size)
        print("The response of AdminApi->get_clients_api_v1_admin_clients_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->get_clients_api_v1_admin_clients_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number | [optional] [default to 1]
 **page_size** | **int**| Items per page | [optional] [default to 20]

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

# **get_cost_optimization_api_v1_admin_organizations_org_id_cost_optimization_get**
> Dict[str, object] get_cost_optimization_api_v1_admin_organizations_org_id_cost_optimization_get(org_id, session_token=session_token)

Get Cost Optimization

Get cost optimization recommendations

Analyzes usage patterns and provides actionable recommendations:
- Provider switching opportunities (e.g., OpenAI → Groq)
- Model optimization suggestions
- Error reduction opportunities
- Potential savings calculations

**Permissions:** Requires org_admin for own org or super_admin for any org

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
    api_instance = llmhub_generated.AdminApi(api_client)
    org_id = 56 # int | 
    session_token = 'session_token_example' # str |  (optional)

    try:
        # Get Cost Optimization
        api_response = api_instance.get_cost_optimization_api_v1_admin_organizations_org_id_cost_optimization_get(org_id, session_token=session_token)
        print("The response of AdminApi->get_cost_optimization_api_v1_admin_organizations_org_id_cost_optimization_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->get_cost_optimization_api_v1_admin_organizations_org_id_cost_optimization_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **int**|  | 
 **session_token** | **str**|  | [optional] 

### Return type

**Dict[str, object]**

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

# **get_daily_costs_api_v1_admin_billing_daily_get**
> Dict[str, object] get_daily_costs_api_v1_admin_billing_daily_get(days=days, org_id=org_id, client_name=client_name, page=page, page_size=page_size, session_token=session_token)

Get Daily Costs

Get daily cost breakdown with pagination
Optionally filtered by organization ID and/or client name
Returns one row per day with all providers aggregated

**Requires:** super_admin, super_dev, or org_admin role

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
    api_instance = llmhub_generated.AdminApi(api_client)
    days = 30 # int |  (optional) (default to 30)
    org_id = 56 # int |  (optional)
    client_name = 'client_name_example' # str |  (optional)
    page = 1 # int | Page number (optional) (default to 1)
    page_size = 100 # int | Items per page (optional) (default to 100)
    session_token = 'session_token_example' # str |  (optional)

    try:
        # Get Daily Costs
        api_response = api_instance.get_daily_costs_api_v1_admin_billing_daily_get(days=days, org_id=org_id, client_name=client_name, page=page, page_size=page_size, session_token=session_token)
        print("The response of AdminApi->get_daily_costs_api_v1_admin_billing_daily_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->get_daily_costs_api_v1_admin_billing_daily_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **days** | **int**|  | [optional] [default to 30]
 **org_id** | **int**|  | [optional] 
 **client_name** | **str**|  | [optional] 
 **page** | **int**| Page number | [optional] [default to 1]
 **page_size** | **int**| Items per page | [optional] [default to 100]
 **session_token** | **str**|  | [optional] 

### Return type

**Dict[str, object]**

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

# **get_daily_system_metrics_api_v1_admin_system_daily_metrics_get**
> object get_daily_system_metrics_api_v1_admin_system_daily_metrics_get(days=days, session_token=session_token)

Get Daily System Metrics

Get daily system metrics for trend analysis

Returns time-series data with daily:
- API call counts
- Revenue totals
- Active client counts
- Success rates

Useful for trend charts and system monitoring

**Required Permission**: super_admin

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
    api_instance = llmhub_generated.AdminApi(api_client)
    days = 30 # int | Number of days to retrieve (optional) (default to 30)
    session_token = 'session_token_example' # str |  (optional)

    try:
        # Get Daily System Metrics
        api_response = api_instance.get_daily_system_metrics_api_v1_admin_system_daily_metrics_get(days=days, session_token=session_token)
        print("The response of AdminApi->get_daily_system_metrics_api_v1_admin_system_daily_metrics_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->get_daily_system_metrics_api_v1_admin_system_daily_metrics_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **days** | **int**| Number of days to retrieve | [optional] [default to 30]
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

# **get_dashboard_stats_api_v1_admin_stats_get**
> Dict[str, object] get_dashboard_stats_api_v1_admin_stats_get(session_token=session_token)

Get Dashboard Stats

Get dashboard statistics
Returns counts and aggregated data for the dashboard
Enhanced with organization-level stats if user has an organization

**Permissions:** Requires super_admin or org_admin role

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
    api_instance = llmhub_generated.AdminApi(api_client)
    session_token = 'session_token_example' # str |  (optional)

    try:
        # Get Dashboard Stats
        api_response = api_instance.get_dashboard_stats_api_v1_admin_stats_get(session_token=session_token)
        print("The response of AdminApi->get_dashboard_stats_api_v1_admin_stats_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->get_dashboard_stats_api_v1_admin_stats_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_token** | **str**|  | [optional] 

### Return type

**Dict[str, object]**

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

# **get_endpoint_catalog_pricing_api_v1_admin_pricing_endpoints_get**
> object get_endpoint_catalog_pricing_api_v1_admin_pricing_endpoints_get(category=category, is_active=is_active, session_token=session_token)

Get Endpoint Catalog Pricing

Get all API endpoint catalog entries with pricing

Returns all V2 API endpoints with their fixed pricing configuration.
Use this endpoint to view and manage per-API-call pricing.

**Required Permission**: super_admin

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
    api_instance = llmhub_generated.AdminApi(api_client)
    category = 'category_example' # str | Filter by category (optional)
    is_active = True # bool | Filter by active status (optional)
    session_token = 'session_token_example' # str |  (optional)

    try:
        # Get Endpoint Catalog Pricing
        api_response = api_instance.get_endpoint_catalog_pricing_api_v1_admin_pricing_endpoints_get(category=category, is_active=is_active, session_token=session_token)
        print("The response of AdminApi->get_endpoint_catalog_pricing_api_v1_admin_pricing_endpoints_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->get_endpoint_catalog_pricing_api_v1_admin_pricing_endpoints_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category** | **str**| Filter by category | [optional] 
 **is_active** | **bool**| Filter by active status | [optional] 
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

# **get_growth_metrics_api_v1_admin_system_growth_metrics_get**
> object get_growth_metrics_api_v1_admin_system_growth_metrics_get(days=days, session_token=session_token)

Get Growth Metrics

Get platform growth metrics (period-over-period comparisons)

Compares current period vs previous period:
- API calls growth
- Revenue growth
- New organizations
- New users

**Required Permission**: super_admin

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
    api_instance = llmhub_generated.AdminApi(api_client)
    days = 30 # int | Period length in days (optional) (default to 30)
    session_token = 'session_token_example' # str |  (optional)

    try:
        # Get Growth Metrics
        api_response = api_instance.get_growth_metrics_api_v1_admin_system_growth_metrics_get(days=days, session_token=session_token)
        print("The response of AdminApi->get_growth_metrics_api_v1_admin_system_growth_metrics_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->get_growth_metrics_api_v1_admin_system_growth_metrics_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **days** | **int**| Period length in days | [optional] [default to 30]
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

# **get_margin_analysis_api_v1_admin_billing_margin_analysis_get**
> object get_margin_analysis_api_v1_admin_billing_margin_analysis_get(days=days, group_by=group_by, session_token=session_token)

Get Margin Analysis

Get margin analysis for API endpoints

Analyze profitability by endpoint or category. Shows revenue vs provider cost
and margin percentage for each.

**Required Permission**: super_admin

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
    api_instance = llmhub_generated.AdminApi(api_client)
    days = 30 # int | Number of days to analyze (optional) (default to 30)
    group_by = 'endpoint' # str | Group by: 'endpoint' or 'category' (optional) (default to 'endpoint')
    session_token = 'session_token_example' # str |  (optional)

    try:
        # Get Margin Analysis
        api_response = api_instance.get_margin_analysis_api_v1_admin_billing_margin_analysis_get(days=days, group_by=group_by, session_token=session_token)
        print("The response of AdminApi->get_margin_analysis_api_v1_admin_billing_margin_analysis_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->get_margin_analysis_api_v1_admin_billing_margin_analysis_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **days** | **int**| Number of days to analyze | [optional] [default to 30]
 **group_by** | **str**| Group by: &#39;endpoint&#39; or &#39;category&#39; | [optional] [default to &#39;endpoint&#39;]
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

# **get_model_types_api_v1_admin_model_types_get**
> Dict[str, object] get_model_types_api_v1_admin_model_types_get(page=page, page_size=page_size)

Get Model Types

Get all model type categories with pagination
Returns all active model types sorted by sort_order

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
    api_instance = llmhub_generated.AdminApi(api_client)
    page = 1 # int | Page number (optional) (default to 1)
    page_size = 50 # int | Items per page (optional) (default to 50)

    try:
        # Get Model Types
        api_response = api_instance.get_model_types_api_v1_admin_model_types_get(page=page, page_size=page_size)
        print("The response of AdminApi->get_model_types_api_v1_admin_model_types_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->get_model_types_api_v1_admin_model_types_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number | [optional] [default to 1]
 **page_size** | **int**| Items per page | [optional] [default to 50]

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

# **get_model_usage_stats_api_v1_admin_system_model_usage_get**
> object get_model_usage_stats_api_v1_admin_system_model_usage_get(days=days, limit=limit, session_token=session_token)

Get Model Usage Stats

Get top models by usage across the platform

Returns list of most-used models with:
- Total API calls
- Total cost
- Average response time
- Client count

Sorted by total calls (highest first)

**Required Permission**: super_admin

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
    api_instance = llmhub_generated.AdminApi(api_client)
    days = 30 # int | Number of days to analyze (optional) (default to 30)
    limit = 15 # int | Number of top models (optional) (default to 15)
    session_token = 'session_token_example' # str |  (optional)

    try:
        # Get Model Usage Stats
        api_response = api_instance.get_model_usage_stats_api_v1_admin_system_model_usage_get(days=days, limit=limit, session_token=session_token)
        print("The response of AdminApi->get_model_usage_stats_api_v1_admin_system_model_usage_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->get_model_usage_stats_api_v1_admin_system_model_usage_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **days** | **int**| Number of days to analyze | [optional] [default to 30]
 **limit** | **int**| Number of top models | [optional] [default to 15]
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

# **get_org_analytics_api_v1_admin_organizations_org_id_analytics_get**
> Dict[str, object] get_org_analytics_api_v1_admin_organizations_org_id_analytics_get(org_id, date_range=date_range, session_token=session_token)

Get Org Analytics

Get comprehensive organization analytics with all KPIs

Includes:
- Team metrics (size, active members)
- Usage statistics (calls, tokens, cost)
- Provider and model breakdowns
- Budget status and forecasting

**Permissions:** Requires org_admin for own org or super_admin for any org

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
    api_instance = llmhub_generated.AdminApi(api_client)
    org_id = 56 # int | 
    date_range = '30d' # str |  (optional) (default to '30d')
    session_token = 'session_token_example' # str |  (optional)

    try:
        # Get Org Analytics
        api_response = api_instance.get_org_analytics_api_v1_admin_organizations_org_id_analytics_get(org_id, date_range=date_range, session_token=session_token)
        print("The response of AdminApi->get_org_analytics_api_v1_admin_organizations_org_id_analytics_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->get_org_analytics_api_v1_admin_organizations_org_id_analytics_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **int**|  | 
 **date_range** | **str**|  | [optional] [default to &#39;30d&#39;]
 **session_token** | **str**|  | [optional] 

### Return type

**Dict[str, object]**

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

# **get_organization_rankings_api_v1_admin_system_organization_rankings_get**
> object get_organization_rankings_api_v1_admin_system_organization_rankings_get(days=days, limit=limit, session_token=session_token)

Get Organization Rankings

Get top organizations ranked by usage and cost

Returns list of organizations with:
- API call counts
- Total cost (revenue)
- Token usage
- Client count

Sorted by total cost (highest first)

**Required Permission**: super_admin

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
    api_instance = llmhub_generated.AdminApi(api_client)
    days = 30 # int | Number of days to analyze (optional) (default to 30)
    limit = 10 # int | Number of top organizations (optional) (default to 10)
    session_token = 'session_token_example' # str |  (optional)

    try:
        # Get Organization Rankings
        api_response = api_instance.get_organization_rankings_api_v1_admin_system_organization_rankings_get(days=days, limit=limit, session_token=session_token)
        print("The response of AdminApi->get_organization_rankings_api_v1_admin_system_organization_rankings_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->get_organization_rankings_api_v1_admin_system_organization_rankings_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **days** | **int**| Number of days to analyze | [optional] [default to 30]
 **limit** | **int**| Number of top organizations | [optional] [default to 10]
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

# **get_organizations_api_v1_admin_billing_organizations_get**
> Dict[str, object] get_organizations_api_v1_admin_billing_organizations_get(page=page, page_size=page_size)

Get Organizations

Get list of all organizations with pagination
Used for filtering billing data by organization

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
    api_instance = llmhub_generated.AdminApi(api_client)
    page = 1 # int | Page number (optional) (default to 1)
    page_size = 50 # int | Items per page (optional) (default to 50)

    try:
        # Get Organizations
        api_response = api_instance.get_organizations_api_v1_admin_billing_organizations_get(page=page, page_size=page_size)
        print("The response of AdminApi->get_organizations_api_v1_admin_billing_organizations_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->get_organizations_api_v1_admin_billing_organizations_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number | [optional] [default to 1]
 **page_size** | **int**| Items per page | [optional] [default to 50]

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

# **get_provider_costs_api_v1_admin_billing_by_provider_get**
> Dict[str, object] get_provider_costs_api_v1_admin_billing_by_provider_get(days=days, org_id=org_id, client_name=client_name, session_token=session_token)

Get Provider Costs

Get cost breakdown by LLM provider
Aggregates costs across the specified date range
Optionally filtered by organization ID and/or client name

**Requires:** super_admin, super_dev, or org_admin role

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
    api_instance = llmhub_generated.AdminApi(api_client)
    days = 30 # int |  (optional) (default to 30)
    org_id = 56 # int |  (optional)
    client_name = 'client_name_example' # str |  (optional)
    session_token = 'session_token_example' # str |  (optional)

    try:
        # Get Provider Costs
        api_response = api_instance.get_provider_costs_api_v1_admin_billing_by_provider_get(days=days, org_id=org_id, client_name=client_name, session_token=session_token)
        print("The response of AdminApi->get_provider_costs_api_v1_admin_billing_by_provider_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->get_provider_costs_api_v1_admin_billing_by_provider_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **days** | **int**|  | [optional] [default to 30]
 **org_id** | **int**|  | [optional] 
 **client_name** | **str**|  | [optional] 
 **session_token** | **str**|  | [optional] 

### Return type

**Dict[str, object]**

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

# **get_provider_detail_api_v1_admin_providers_provider_key_detail_get**
> Dict[str, object] get_provider_detail_api_v1_admin_providers_provider_key_detail_get(provider_key, time_period=time_period, session_token=session_token)

Get Provider Detail

Get detailed provider information including API key (super_admin only)

Returns:
- Provider metadata
- Full API key
- Usage statistics
- Useful links

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
    api_instance = llmhub_generated.AdminApi(api_client)
    provider_key = 'provider_key_example' # str | 
    time_period = '30d' # str | Time period: 7d, 30d, 90d, 1y, all (optional) (default to '30d')
    session_token = 'session_token_example' # str |  (optional)

    try:
        # Get Provider Detail
        api_response = api_instance.get_provider_detail_api_v1_admin_providers_provider_key_detail_get(provider_key, time_period=time_period, session_token=session_token)
        print("The response of AdminApi->get_provider_detail_api_v1_admin_providers_provider_key_detail_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->get_provider_detail_api_v1_admin_providers_provider_key_detail_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_key** | **str**|  | 
 **time_period** | **str**| Time period: 7d, 30d, 90d, 1y, all | [optional] [default to &#39;30d&#39;]
 **session_token** | **str**|  | [optional] 

### Return type

**Dict[str, object]**

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

# **get_provider_models_api_v1_admin_providers_provider_id_models_get**
> Dict[str, object] get_provider_models_api_v1_admin_providers_provider_id_models_get(provider_id, page=page, page_size=page_size)

Get Provider Models

Get all models for a specific provider with pagination

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
    api_instance = llmhub_generated.AdminApi(api_client)
    provider_id = 'provider_id_example' # str | 
    page = 1 # int | Page number (optional) (default to 1)
    page_size = 20 # int | Items per page (optional) (default to 20)

    try:
        # Get Provider Models
        api_response = api_instance.get_provider_models_api_v1_admin_providers_provider_id_models_get(provider_id, page=page, page_size=page_size)
        print("The response of AdminApi->get_provider_models_api_v1_admin_providers_provider_id_models_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->get_provider_models_api_v1_admin_providers_provider_id_models_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_id** | **str**|  | 
 **page** | **int**| Page number | [optional] [default to 1]
 **page_size** | **int**| Items per page | [optional] [default to 20]

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

# **get_provider_models_detailed_api_v1_admin_providers_provider_key_models_detailed_get**
> Dict[str, object] get_provider_models_detailed_api_v1_admin_providers_provider_key_models_detailed_get(provider_key, time_period=time_period, model_types=model_types, page=page, page_size=page_size, session_token=session_token)

Get Provider Models Detailed

Get models for a provider with usage statistics and filtering

Features:
- Filter by model types (multiselect)
- Usage stats per model for time period
- Cost breakdown

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
    api_instance = llmhub_generated.AdminApi(api_client)
    provider_key = 'provider_key_example' # str | 
    time_period = '30d' # str | Time period: 7d, 30d, 90d, 1y, all (optional) (default to '30d')
    model_types = 'model_types_example' # str | Comma-separated model types filter (optional)
    page = 1 # int | Page number (optional) (default to 1)
    page_size = 50 # int | Items per page (optional) (default to 50)
    session_token = 'session_token_example' # str |  (optional)

    try:
        # Get Provider Models Detailed
        api_response = api_instance.get_provider_models_detailed_api_v1_admin_providers_provider_key_models_detailed_get(provider_key, time_period=time_period, model_types=model_types, page=page, page_size=page_size, session_token=session_token)
        print("The response of AdminApi->get_provider_models_detailed_api_v1_admin_providers_provider_key_models_detailed_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->get_provider_models_detailed_api_v1_admin_providers_provider_key_models_detailed_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_key** | **str**|  | 
 **time_period** | **str**| Time period: 7d, 30d, 90d, 1y, all | [optional] [default to &#39;30d&#39;]
 **model_types** | **str**| Comma-separated model types filter | [optional] 
 **page** | **int**| Page number | [optional] [default to 1]
 **page_size** | **int**| Items per page | [optional] [default to 50]
 **session_token** | **str**|  | [optional] 

### Return type

**Dict[str, object]**

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

# **get_provider_performance_api_v1_admin_system_provider_performance_get**
> object get_provider_performance_api_v1_admin_system_provider_performance_get(days=days, session_token=session_token)

Get Provider Performance

Get provider performance metrics across the platform

Returns metrics for each provider:
- Total API calls
- Total cost
- Average response time
- Success rate

Sorted by total calls (highest first)

**Required Permission**: super_admin

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
    api_instance = llmhub_generated.AdminApi(api_client)
    days = 30 # int | Number of days to analyze (optional) (default to 30)
    session_token = 'session_token_example' # str |  (optional)

    try:
        # Get Provider Performance
        api_response = api_instance.get_provider_performance_api_v1_admin_system_provider_performance_get(days=days, session_token=session_token)
        print("The response of AdminApi->get_provider_performance_api_v1_admin_system_provider_performance_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->get_provider_performance_api_v1_admin_system_provider_performance_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **days** | **int**| Number of days to analyze | [optional] [default to 30]
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

# **get_provider_templates_api_v1_admin_provider_templates_get**
> Dict[str, object] get_provider_templates_api_v1_admin_provider_templates_get(page=page, page_size=page_size)

Get Provider Templates

Get available provider templates for creating new providers with pagination

Returns list of templates with their metadata

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
    api_instance = llmhub_generated.AdminApi(api_client)
    page = 1 # int | Page number (optional) (default to 1)
    page_size = 20 # int | Items per page (optional) (default to 20)

    try:
        # Get Provider Templates
        api_response = api_instance.get_provider_templates_api_v1_admin_provider_templates_get(page=page, page_size=page_size)
        print("The response of AdminApi->get_provider_templates_api_v1_admin_provider_templates_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->get_provider_templates_api_v1_admin_provider_templates_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number | [optional] [default to 1]
 **page_size** | **int**| Items per page | [optional] [default to 20]

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

# **get_provider_usage_api_v1_admin_providers_provider_key_usage_get**
> Dict[str, object] get_provider_usage_api_v1_admin_providers_provider_key_usage_get(provider_key, time_period=time_period, group_by=group_by, session_token=session_token)

Get Provider Usage

Get usage aggregations for a provider over time

Returns time-series data for charting

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
    api_instance = llmhub_generated.AdminApi(api_client)
    provider_key = 'provider_key_example' # str | 
    time_period = '30d' # str | Time period: 7d, 30d, 90d, 1y, all (optional) (default to '30d')
    group_by = 'day' # str | Group by: hour, day, month (optional) (default to 'day')
    session_token = 'session_token_example' # str |  (optional)

    try:
        # Get Provider Usage
        api_response = api_instance.get_provider_usage_api_v1_admin_providers_provider_key_usage_get(provider_key, time_period=time_period, group_by=group_by, session_token=session_token)
        print("The response of AdminApi->get_provider_usage_api_v1_admin_providers_provider_key_usage_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->get_provider_usage_api_v1_admin_providers_provider_key_usage_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_key** | **str**|  | 
 **time_period** | **str**| Time period: 7d, 30d, 90d, 1y, all | [optional] [default to &#39;30d&#39;]
 **group_by** | **str**| Group by: hour, day, month | [optional] [default to &#39;day&#39;]
 **session_token** | **str**|  | [optional] 

### Return type

**Dict[str, object]**

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

# **get_providers_from_registry_api_v1_admin_providers_registry_get**
> List[Dict[str, object]] get_providers_from_registry_api_v1_admin_providers_registry_get(session_token=session_token)

Get Providers From Registry

Get all LLM providers dynamically from the provider registry
This endpoint is fully programmatic - new providers appear automatically
Shows ALL registered providers, including unconfigured ones
Also includes stored API keys from database (admin only)

**Permissions:** Optional authentication - admin users see full details

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
    api_instance = llmhub_generated.AdminApi(api_client)
    session_token = 'session_token_example' # str |  (optional)

    try:
        # Get Providers From Registry
        api_response = api_instance.get_providers_from_registry_api_v1_admin_providers_registry_get(session_token=session_token)
        print("The response of AdminApi->get_providers_from_registry_api_v1_admin_providers_registry_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->get_providers_from_registry_api_v1_admin_providers_registry_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_token** | **str**|  | [optional] 

### Return type

**List[Dict[str, object]]**

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

# **get_providers_list_api_v1_admin_providers_get**
> List[Dict[str, object]] get_providers_list_api_v1_admin_providers_get(time_period=time_period, session_token=session_token)

Get Providers List

Get all providers with usage statistics for super admin dashboard

Returns providers with:
- Configuration status
- Model count
- Token usage for time period
- Cost for time period

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
    api_instance = llmhub_generated.AdminApi(api_client)
    time_period = '30d' # str | Time period: 7d, 30d, 90d, 1y, all (optional) (default to '30d')
    session_token = 'session_token_example' # str |  (optional)

    try:
        # Get Providers List
        api_response = api_instance.get_providers_list_api_v1_admin_providers_get(time_period=time_period, session_token=session_token)
        print("The response of AdminApi->get_providers_list_api_v1_admin_providers_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->get_providers_list_api_v1_admin_providers_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **time_period** | **str**| Time period: 7d, 30d, 90d, 1y, all | [optional] [default to &#39;30d&#39;]
 **session_token** | **str**|  | [optional] 

### Return type

**List[Dict[str, object]]**

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

# **get_revenue_metrics_api_v1_admin_billing_revenue_get**
> object get_revenue_metrics_api_v1_admin_billing_revenue_get(days=days, include_breakdown=include_breakdown, session_token=session_token)

Get Revenue Metrics

Get revenue metrics for API call billing

Returns total revenue, provider costs, and margins for the specified period.
Includes breakdown by category and top endpoints by revenue.

**Required Permission**: super_admin

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
    api_instance = llmhub_generated.AdminApi(api_client)
    days = 30 # int | Number of days to analyze (optional) (default to 30)
    include_breakdown = True # bool | Include category/endpoint breakdown (optional) (default to True)
    session_token = 'session_token_example' # str |  (optional)

    try:
        # Get Revenue Metrics
        api_response = api_instance.get_revenue_metrics_api_v1_admin_billing_revenue_get(days=days, include_breakdown=include_breakdown, session_token=session_token)
        print("The response of AdminApi->get_revenue_metrics_api_v1_admin_billing_revenue_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->get_revenue_metrics_api_v1_admin_billing_revenue_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **days** | **int**| Number of days to analyze | [optional] [default to 30]
 **include_breakdown** | **bool**| Include category/endpoint breakdown | [optional] [default to True]
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

# **get_system_audit_logs_api_v1_admin_system_audit_logs_get**
> Dict[str, object] get_system_audit_logs_api_v1_admin_system_audit_logs_get(page=page, page_size=page_size, provider=provider, org_id=org_id, success=success, search=search, start_date=start_date, end_date=end_date, session_token=session_token)

Get System Audit Logs

Get system-wide audit logs (API call logs)

Returns all LLM generation logs across the platform with filtering options.

**Required Permission**: super_admin

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
    api_instance = llmhub_generated.AdminApi(api_client)
    page = 1 # int | Page number (optional) (default to 1)
    page_size = 50 # int | Items per page (optional) (default to 50)
    provider = 'provider_example' # str | Filter by provider (optional)
    org_id = 'org_id_example' # str | Filter by organization ID (optional)
    success = True # bool | Filter by success status (optional)
    search = 'search_example' # str | Search in model, endpoint, error (optional)
    start_date = 'start_date_example' # str | Start date (ISO format) (optional)
    end_date = 'end_date_example' # str | End date (ISO format) (optional)
    session_token = 'session_token_example' # str |  (optional)

    try:
        # Get System Audit Logs
        api_response = api_instance.get_system_audit_logs_api_v1_admin_system_audit_logs_get(page=page, page_size=page_size, provider=provider, org_id=org_id, success=success, search=search, start_date=start_date, end_date=end_date, session_token=session_token)
        print("The response of AdminApi->get_system_audit_logs_api_v1_admin_system_audit_logs_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->get_system_audit_logs_api_v1_admin_system_audit_logs_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number | [optional] [default to 1]
 **page_size** | **int**| Items per page | [optional] [default to 50]
 **provider** | **str**| Filter by provider | [optional] 
 **org_id** | **str**| Filter by organization ID | [optional] 
 **success** | **bool**| Filter by success status | [optional] 
 **search** | **str**| Search in model, endpoint, error | [optional] 
 **start_date** | **str**| Start date (ISO format) | [optional] 
 **end_date** | **str**| End date (ISO format) | [optional] 
 **session_token** | **str**|  | [optional] 

### Return type

**Dict[str, object]**

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

# **get_system_health_api_v1_admin_system_health_get**
> object get_system_health_api_v1_admin_system_health_get(session_token=session_token)

Get System Health

Get system health indicators

Returns real-time health metrics:
- Overall status (healthy/degraded/unhealthy)
- Error rate (last hour)
- Recent API calls and errors
- Active organizations (24h)
- Average response time

**Required Permission**: super_admin

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
    api_instance = llmhub_generated.AdminApi(api_client)
    session_token = 'session_token_example' # str |  (optional)

    try:
        # Get System Health
        api_response = api_instance.get_system_health_api_v1_admin_system_health_get(session_token=session_token)
        print("The response of AdminApi->get_system_health_api_v1_admin_system_health_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->get_system_health_api_v1_admin_system_health_get: %s\n" % e)
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

# **get_system_overview_api_v1_admin_system_overview_get**
> object get_system_overview_api_v1_admin_system_overview_get(days=days, session_token=session_token)

Get System Overview

Get comprehensive system overview metrics

Returns platform-wide KPIs including:
- Organizations (total, active, inactive)
- Users (total, active, inactive)
- API Clients (total, active, inactive)
- API calls and tokens
- Revenue
- Success rate
- Available providers and models

**Required Permission**: super_admin

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
    api_instance = llmhub_generated.AdminApi(api_client)
    days = 30 # int | Number of days to analyze (optional) (default to 30)
    session_token = 'session_token_example' # str |  (optional)

    try:
        # Get System Overview
        api_response = api_instance.get_system_overview_api_v1_admin_system_overview_get(days=days, session_token=session_token)
        print("The response of AdminApi->get_system_overview_api_v1_admin_system_overview_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->get_system_overview_api_v1_admin_system_overview_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **days** | **int**| Number of days to analyze | [optional] [default to 30]
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

# **get_team_insights_api_v1_admin_organizations_org_id_team_insights_get**
> Dict[str, object] get_team_insights_api_v1_admin_organizations_org_id_team_insights_get(org_id, session_token=session_token)

Get Team Insights

Get team activity and productivity metrics

Includes:
- Most active users with usage stats
- Activity heatmap (hourly/daily patterns)
- Team productivity metrics

**Permissions:** Requires org_admin for own org or super_admin for any org

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
    api_instance = llmhub_generated.AdminApi(api_client)
    org_id = 56 # int | 
    session_token = 'session_token_example' # str |  (optional)

    try:
        # Get Team Insights
        api_response = api_instance.get_team_insights_api_v1_admin_organizations_org_id_team_insights_get(org_id, session_token=session_token)
        print("The response of AdminApi->get_team_insights_api_v1_admin_organizations_org_id_team_insights_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->get_team_insights_api_v1_admin_organizations_org_id_team_insights_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **int**|  | 
 **session_token** | **str**|  | [optional] 

### Return type

**Dict[str, object]**

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

# **get_test_history_api_v1_admin_test_history_get**
> Dict[str, object] get_test_history_api_v1_admin_test_history_get(page=page, page_size=page_size)

Get Test History

Get test history from playground with pagination
Returns recent test-prompt calls from generation logs

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
    api_instance = llmhub_generated.AdminApi(api_client)
    page = 1 # int | Page number (optional) (default to 1)
    page_size = 50 # int | Items per page (optional) (default to 50)

    try:
        # Get Test History
        api_response = api_instance.get_test_history_api_v1_admin_test_history_get(page=page, page_size=page_size)
        print("The response of AdminApi->get_test_history_api_v1_admin_test_history_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->get_test_history_api_v1_admin_test_history_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number | [optional] [default to 1]
 **page_size** | **int**| Items per page | [optional] [default to 50]

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

# **get_user_achievements_api_v1_admin_users_me_achievements_get**
> object get_user_achievements_api_v1_admin_users_me_achievements_get(session_token=session_token)

Get User Achievements

Get achievement badges for current user

Returns list of achievements with unlock status based on:
- Total API calls (milestones: 1, 100, 1K, 10K)
- Token processing (1M+ tokens)
- Provider diversity (3+ providers)
- Model exploration (10+ models)

**Required Permission**: Authenticated user

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
    api_instance = llmhub_generated.AdminApi(api_client)
    session_token = 'session_token_example' # str |  (optional)

    try:
        # Get User Achievements
        api_response = api_instance.get_user_achievements_api_v1_admin_users_me_achievements_get(session_token=session_token)
        print("The response of AdminApi->get_user_achievements_api_v1_admin_users_me_achievements_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->get_user_achievements_api_v1_admin_users_me_achievements_get: %s\n" % e)
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

# **get_user_activity_api_v1_admin_users_me_activity_get**
> object get_user_activity_api_v1_admin_users_me_activity_get(limit=limit, session_token=session_token)

Get User Activity

Get recent activity timeline for current user

Returns chronological list of recent API calls with:
- Timestamp
- Provider and model used
- Success status
- Token count and cost

**Required Permission**: Authenticated user

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
    api_instance = llmhub_generated.AdminApi(api_client)
    limit = 50 # int | Number of recent activities (optional) (default to 50)
    session_token = 'session_token_example' # str |  (optional)

    try:
        # Get User Activity
        api_response = api_instance.get_user_activity_api_v1_admin_users_me_activity_get(limit=limit, session_token=session_token)
        print("The response of AdminApi->get_user_activity_api_v1_admin_users_me_activity_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->get_user_activity_api_v1_admin_users_me_activity_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of recent activities | [optional] [default to 50]
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

# **get_user_daily_activity_api_v1_admin_users_me_daily_activity_get**
> object get_user_daily_activity_api_v1_admin_users_me_daily_activity_get(days=days, session_token=session_token)

Get User Daily Activity

Get daily activity data for charts/heatmaps

Returns time-series data with daily:
- API call counts
- Cost totals

Useful for activity heatmaps and trend visualization

**Required Permission**: Authenticated user

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
    api_instance = llmhub_generated.AdminApi(api_client)
    days = 30 # int | Number of days to analyze (optional) (default to 30)
    session_token = 'session_token_example' # str |  (optional)

    try:
        # Get User Daily Activity
        api_response = api_instance.get_user_daily_activity_api_v1_admin_users_me_daily_activity_get(days=days, session_token=session_token)
        print("The response of AdminApi->get_user_daily_activity_api_v1_admin_users_me_daily_activity_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->get_user_daily_activity_api_v1_admin_users_me_daily_activity_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **days** | **int**| Number of days to analyze | [optional] [default to 30]
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

# **get_user_overview_api_v1_admin_users_me_overview_get**
> object get_user_overview_api_v1_admin_users_me_overview_get(days=days, session_token=session_token)

Get User Overview

Get comprehensive overview statistics for current user

Returns personal usage stats including:
- Total API calls
- Token usage (input/output)
- Total cost
- Success rate
- Most used provider and model

**Required Permission**: Authenticated user

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
    api_instance = llmhub_generated.AdminApi(api_client)
    days = 30 # int | Number of days to analyze (optional) (default to 30)
    session_token = 'session_token_example' # str |  (optional)

    try:
        # Get User Overview
        api_response = api_instance.get_user_overview_api_v1_admin_users_me_overview_get(days=days, session_token=session_token)
        print("The response of AdminApi->get_user_overview_api_v1_admin_users_me_overview_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->get_user_overview_api_v1_admin_users_me_overview_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **days** | **int**| Number of days to analyze | [optional] [default to 30]
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

# **get_user_preferences_api_v1_admin_users_me_preferences_get**
> object get_user_preferences_api_v1_admin_users_me_preferences_get(days=days, session_token=session_token)

Get User Preferences

Get user's model and provider preferences

Returns detailed breakdown of:
- Provider usage (calls and cost per provider)
- Top 10 most used models with performance metrics

Helps users understand their usage patterns

**Required Permission**: Authenticated user

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
    api_instance = llmhub_generated.AdminApi(api_client)
    days = 30 # int | Number of days to analyze (optional) (default to 30)
    session_token = 'session_token_example' # str |  (optional)

    try:
        # Get User Preferences
        api_response = api_instance.get_user_preferences_api_v1_admin_users_me_preferences_get(days=days, session_token=session_token)
        print("The response of AdminApi->get_user_preferences_api_v1_admin_users_me_preferences_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->get_user_preferences_api_v1_admin_users_me_preferences_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **days** | **int**| Number of days to analyze | [optional] [default to 30]
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

# **regenerate_api_key_api_v1_admin_clients_client_id_regenerate_key_post**
> Dict[str, object] regenerate_api_key_api_v1_admin_clients_client_id_regenerate_key_post(client_id)

Regenerate Api Key

Regenerate API key for a client

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
    api_instance = llmhub_generated.AdminApi(api_client)
    client_id = 'client_id_example' # str | 

    try:
        # Regenerate Api Key
        api_response = api_instance.regenerate_api_key_api_v1_admin_clients_client_id_regenerate_key_post(client_id)
        print("The response of AdminApi->regenerate_api_key_api_v1_admin_clients_client_id_regenerate_key_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->regenerate_api_key_api_v1_admin_clients_client_id_regenerate_key_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**|  | 

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

# **register_provider_api_v1_admin_providers_provider_key_register_post**
> Dict[str, object] register_provider_api_v1_admin_providers_provider_key_register_post(provider_key)

Register Provider

Register a new provider in the database and discover its models
Creates provider entry in llm_providers table and tests connection

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
    api_instance = llmhub_generated.AdminApi(api_client)
    provider_key = 'provider_key_example' # str | 

    try:
        # Register Provider
        api_response = api_instance.register_provider_api_v1_admin_providers_provider_key_register_post(provider_key)
        print("The response of AdminApi->register_provider_api_v1_admin_providers_provider_key_register_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->register_provider_api_v1_admin_providers_provider_key_register_post: %s\n" % e)
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

# **test_prompt_api_v1_admin_test_prompt_post**
> Dict[str, object] test_prompt_api_v1_admin_test_prompt_post(request_body, session_token=session_token)

Test Prompt

Test a prompt with a specific provider and model
Optional authentication - for admin web UI playground use
Returns simplified response with content, tokens, and cost

Note: Authenticated users have higher rate limits

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
    api_instance = llmhub_generated.AdminApi(api_client)
    request_body = None # Dict[str, object] | 
    session_token = 'session_token_example' # str |  (optional)

    try:
        # Test Prompt
        api_response = api_instance.test_prompt_api_v1_admin_test_prompt_post(request_body, session_token=session_token)
        print("The response of AdminApi->test_prompt_api_v1_admin_test_prompt_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->test_prompt_api_v1_admin_test_prompt_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**Dict[str, object]**](object.md)|  | 
 **session_token** | **str**|  | [optional] 

### Return type

**Dict[str, object]**

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

# **test_provider_api_key_api_v1_admin_providers_provider_key_test_key_post**
> Dict[str, object] test_provider_api_key_api_v1_admin_providers_provider_key_test_key_post(provider_key, request_body=request_body)

Test Provider Api Key

Test provider API key and fetch available models with costs
Returns detailed step-by-step status of the testing process
Accepts optional api_key in request body to test before saving

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
    api_instance = llmhub_generated.AdminApi(api_client)
    provider_key = 'provider_key_example' # str | 
    request_body = None # Dict[str, object] |  (optional)

    try:
        # Test Provider Api Key
        api_response = api_instance.test_provider_api_key_api_v1_admin_providers_provider_key_test_key_post(provider_key, request_body=request_body)
        print("The response of AdminApi->test_provider_api_key_api_v1_admin_providers_provider_key_test_key_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->test_provider_api_key_api_v1_admin_providers_provider_key_test_key_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_key** | **str**|  | 
 **request_body** | [**Dict[str, object]**](object.md)|  | [optional] 

### Return type

**Dict[str, object]**

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

# **toggle_model_api_v1_admin_models_model_id_toggle_post**
> Dict[str, object] toggle_model_api_v1_admin_models_model_id_toggle_post(model_id)

Toggle Model

Toggle model enabled status

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
    api_instance = llmhub_generated.AdminApi(api_client)
    model_id = 'model_id_example' # str | 

    try:
        # Toggle Model
        api_response = api_instance.toggle_model_api_v1_admin_models_model_id_toggle_post(model_id)
        print("The response of AdminApi->toggle_model_api_v1_admin_models_model_id_toggle_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->toggle_model_api_v1_admin_models_model_id_toggle_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model_id** | **str**|  | 

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

# **update_client_api_v1_admin_clients_client_id_patch**
> Dict[str, object] update_client_api_v1_admin_clients_client_id_patch(client_id, request_body)

Update Client

Update API client details
Allows updating: client_name, org_id, contact_email, rate_limit, monthly_budget_eur, is_active

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
    api_instance = llmhub_generated.AdminApi(api_client)
    client_id = 'client_id_example' # str | 
    request_body = None # Dict[str, object] | 

    try:
        # Update Client
        api_response = api_instance.update_client_api_v1_admin_clients_client_id_patch(client_id, request_body)
        print("The response of AdminApi->update_client_api_v1_admin_clients_client_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->update_client_api_v1_admin_clients_client_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**|  | 
 **request_body** | [**Dict[str, object]**](object.md)|  | 

### Return type

**Dict[str, object]**

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

# **update_endpoint_pricing_api_v1_admin_pricing_endpoints_endpoint_id_patch**
> object update_endpoint_pricing_api_v1_admin_pricing_endpoints_endpoint_id_patch(endpoint_id, base_price_eur=base_price_eur, avg_provider_cost_usd=avg_provider_cost_usd, markup_percentage=markup_percentage, is_active=is_active, description=description, session_token=session_token)

Update Endpoint Pricing

Update pricing for an API endpoint

Modify the fixed per-API-call price for a specific endpoint.
Only super_admin can modify endpoint pricing.

**Required Permission**: super_admin

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
    api_instance = llmhub_generated.AdminApi(api_client)
    endpoint_id = 'endpoint_id_example' # str | 
    base_price_eur = 3.4 # float | New base price in EUR (optional)
    avg_provider_cost_usd = 3.4 # float | Average provider cost (optional)
    markup_percentage = 3.4 # float | Markup percentage (optional)
    is_active = True # bool | Active status (optional)
    description = 'description_example' # str | Endpoint description for website (optional)
    session_token = 'session_token_example' # str |  (optional)

    try:
        # Update Endpoint Pricing
        api_response = api_instance.update_endpoint_pricing_api_v1_admin_pricing_endpoints_endpoint_id_patch(endpoint_id, base_price_eur=base_price_eur, avg_provider_cost_usd=avg_provider_cost_usd, markup_percentage=markup_percentage, is_active=is_active, description=description, session_token=session_token)
        print("The response of AdminApi->update_endpoint_pricing_api_v1_admin_pricing_endpoints_endpoint_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->update_endpoint_pricing_api_v1_admin_pricing_endpoints_endpoint_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint_id** | **str**|  | 
 **base_price_eur** | **float**| New base price in EUR | [optional] 
 **avg_provider_cost_usd** | **float**| Average provider cost | [optional] 
 **markup_percentage** | **float**| Markup percentage | [optional] 
 **is_active** | **bool**| Active status | [optional] 
 **description** | **str**| Endpoint description for website | [optional] 
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

# **update_model_api_v1_admin_models_model_id_patch**
> Dict[str, object] update_model_api_v1_admin_models_model_id_patch(model_id, request_body)

Update Model

Update model pricing and configuration

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
    api_instance = llmhub_generated.AdminApi(api_client)
    model_id = 'model_id_example' # str | 
    request_body = None # Dict[str, object] | 

    try:
        # Update Model
        api_response = api_instance.update_model_api_v1_admin_models_model_id_patch(model_id, request_body)
        print("The response of AdminApi->update_model_api_v1_admin_models_model_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->update_model_api_v1_admin_models_model_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model_id** | **str**|  | 
 **request_body** | [**Dict[str, object]**](object.md)|  | 

### Return type

**Dict[str, object]**

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

# **update_model_type_api_v1_admin_model_types_type_id_patch**
> Dict[str, object] update_model_type_api_v1_admin_model_types_type_id_patch(type_id, request_body)

Update Model Type

Update model type configuration

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
    api_instance = llmhub_generated.AdminApi(api_client)
    type_id = 'type_id_example' # str | 
    request_body = None # Dict[str, object] | 

    try:
        # Update Model Type
        api_response = api_instance.update_model_type_api_v1_admin_model_types_type_id_patch(type_id, request_body)
        print("The response of AdminApi->update_model_type_api_v1_admin_model_types_type_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->update_model_type_api_v1_admin_model_types_type_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type_id** | **str**|  | 
 **request_body** | [**Dict[str, object]**](object.md)|  | 

### Return type

**Dict[str, object]**

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

# **update_provider_api_key_api_v1_admin_providers_provider_key_api_key_put**
> Dict[str, object] update_provider_api_key_api_v1_admin_providers_provider_key_api_key_put(provider_key, request_body)

Update Provider Api Key

DEPRECATED: API keys are managed via .env file

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
    api_instance = llmhub_generated.AdminApi(api_client)
    provider_key = 'provider_key_example' # str | 
    request_body = None # Dict[str, object] | 

    try:
        # Update Provider Api Key
        api_response = api_instance.update_provider_api_key_api_v1_admin_providers_provider_key_api_key_put(provider_key, request_body)
        print("The response of AdminApi->update_provider_api_key_api_v1_admin_providers_provider_key_api_key_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->update_provider_api_key_api_v1_admin_providers_provider_key_api_key_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_key** | **str**|  | 
 **request_body** | [**Dict[str, object]**](object.md)|  | 

### Return type

**Dict[str, object]**

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

