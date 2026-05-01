# CommissionSummaryResponse

Summary of commissions across all organizations for a Super Dev

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**super_dev_user_id** | **str** |  | 
**super_dev_name** | **str** |  | 
**super_dev_email** | **str** |  | 
**total_organizations** | **int** |  | 
**total_commission_eur** | **float** |  | 
**total_spent_eur** | **float** |  | 
**total_api_calls** | **int** |  | 
**period_start** | **datetime** |  | 
**period_end** | **datetime** |  | 
**organizations** | **List[Dict[str, object]]** |  | 

## Example

```python
from llmhub_generated.models.commission_summary_response import CommissionSummaryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CommissionSummaryResponse from a JSON string
commission_summary_response_instance = CommissionSummaryResponse.from_json(json)
# print the JSON string representation of the object
print(CommissionSummaryResponse.to_json())

# convert the object into a dict
commission_summary_response_dict = commission_summary_response_instance.to_dict()
# create an instance of CommissionSummaryResponse from a dict
commission_summary_response_from_dict = CommissionSummaryResponse.from_dict(commission_summary_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


