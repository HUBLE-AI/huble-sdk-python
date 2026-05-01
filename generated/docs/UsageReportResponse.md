# UsageReportResponse

Schema for usage report response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**report_id** | **int** |  | 
**org_id** | **int** |  | 
**report_month** | **datetime** |  | 
**report_type** | **str** |  | 
**generated_at** | **datetime** |  | 
**generated_by** | **str** |  | [optional] 
**generation_method** | **str** |  | 
**file_name** | **str** |  | 
**file_size_bytes** | **int** |  | 
**file_path** | **str** |  | [optional] 
**total_calls** | **int** |  | 
**total_cost_eur** | **float** |  | 
**total_input_tokens** | **int** |  | 
**total_output_tokens** | **int** |  | 
**status** | **str** |  | 
**error_message** | **str** |  | 
**notes** | **str** |  | 
**report_metadata** | **Dict[str, object]** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**org_name** | **str** |  | [optional] 
**generated_by_name** | **str** |  | [optional] 
**download_url** | **str** |  | [optional] 

## Example

```python
from llmhub_generated.models.usage_report_response import UsageReportResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UsageReportResponse from a JSON string
usage_report_response_instance = UsageReportResponse.from_json(json)
# print the JSON string representation of the object
print(UsageReportResponse.to_json())

# convert the object into a dict
usage_report_response_dict = usage_report_response_instance.to_dict()
# create an instance of UsageReportResponse from a dict
usage_report_response_from_dict = UsageReportResponse.from_dict(usage_report_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


