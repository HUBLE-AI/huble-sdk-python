# SuperDevDashboardStats

Dashboard statistics for Super Dev

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_organizations** | **int** |  | 
**active_organizations** | **int** |  | 
**total_commission_this_month_eur** | **float** |  | 
**total_commission_last_month_eur** | **float** |  | 
**total_commission_ytd_eur** | **float** |  | 
**total_api_calls_this_month** | **int** |  | 
**total_spent_this_month_eur** | **float** |  | 
**organizations** | **List[Dict[str, object]]** |  | 
**recent_reports** | [**List[CommissionReportResponse]**](CommissionReportResponse.md) |  | 

## Example

```python
from llmhub_generated.models.super_dev_dashboard_stats import SuperDevDashboardStats

# TODO update the JSON string below
json = "{}"
# create an instance of SuperDevDashboardStats from a JSON string
super_dev_dashboard_stats_instance = SuperDevDashboardStats.from_json(json)
# print the JSON string representation of the object
print(SuperDevDashboardStats.to_json())

# convert the object into a dict
super_dev_dashboard_stats_dict = super_dev_dashboard_stats_instance.to_dict()
# create an instance of SuperDevDashboardStats from a dict
super_dev_dashboard_stats_from_dict = SuperDevDashboardStats.from_dict(super_dev_dashboard_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


