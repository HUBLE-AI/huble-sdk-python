# CommissionReportResponse

Response schema for commission report

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**report_id** | **int** |  | 
**super_dev_user_id** | **str** |  | 
**super_dev_name** | **str** |  | [optional] 
**super_dev_email** | **str** |  | [optional] 
**org_id** | **int** |  | 
**org_name** | **str** |  | [optional] 
**report_period_start** | **datetime** |  | 
**report_period_end** | **datetime** |  | 
**total_spent_eur** | **float** |  | 
**commission_percentage** | **float** |  | 
**commission_eur** | **float** |  | 
**total_api_calls** | **int** |  | 
**total_input_tokens** | **int** |  | 
**total_output_tokens** | **int** |  | 
**status** | **str** |  | 
**generated_at** | **datetime** |  | 
**finalized_at** | **datetime** |  | [optional] 
**paid_at** | **datetime** |  | [optional] 
**payment_reference** | **str** |  | [optional] 
**payment_notes** | **str** |  | [optional] 

## Example

```python
from llmhub_generated.models.commission_report_response import CommissionReportResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CommissionReportResponse from a JSON string
commission_report_response_instance = CommissionReportResponse.from_json(json)
# print the JSON string representation of the object
print(CommissionReportResponse.to_json())

# convert the object into a dict
commission_report_response_dict = commission_report_response_instance.to_dict()
# create an instance of CommissionReportResponse from a dict
commission_report_response_from_dict = CommissionReportResponse.from_dict(commission_report_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


