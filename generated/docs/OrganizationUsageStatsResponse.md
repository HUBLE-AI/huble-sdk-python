# OrganizationUsageStatsResponse

Quick usage statistics for organization detail view

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_users** | **int** |  | 
**active_users** | **int** |  | 
**total_api_clients** | **int** |  | 
**active_api_clients** | **int** |  | 
**current_month_calls** | **int** |  | 
**current_month_cost_eur** | **float** |  | 
**last_30_days_calls** | **int** |  | 
**last_30_days_cost_eur** | **float** |  | 
**top_models** | **List[Optional[Dict[str, object]]]** |  | 
**budget_utilization_percentage** | **float** |  | 

## Example

```python
from llmhub_generated.models.organization_usage_stats_response import OrganizationUsageStatsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationUsageStatsResponse from a JSON string
organization_usage_stats_response_instance = OrganizationUsageStatsResponse.from_json(json)
# print the JSON string representation of the object
print(OrganizationUsageStatsResponse.to_json())

# convert the object into a dict
organization_usage_stats_response_dict = organization_usage_stats_response_instance.to_dict()
# create an instance of OrganizationUsageStatsResponse from a dict
organization_usage_stats_response_from_dict = OrganizationUsageStatsResponse.from_dict(organization_usage_stats_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


