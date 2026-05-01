# UsageReportCreate

Schema for creating a new usage report record

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**org_id** | **int** |  | 
**report_month** | **datetime** |  | 
**report_type** | **str** |  | [optional] [default to 'monthly_usage']
**generation_method** | **str** |  | [optional] [default to 'manual']
**file_name** | **str** |  | [optional] 
**file_size_bytes** | **int** |  | [optional] 
**total_calls** | **int** |  | [optional] [default to 0]
**total_cost_eur** | **float** |  | [optional] [default to 0.0]
**total_input_tokens** | **int** |  | [optional] [default to 0]
**total_output_tokens** | **int** |  | [optional] [default to 0]
**status** | **str** |  | [optional] [default to 'completed']
**notes** | **str** |  | [optional] 
**report_metadata** | **Dict[str, object]** |  | [optional] 

## Example

```python
from llmhub_generated.models.usage_report_create import UsageReportCreate

# TODO update the JSON string below
json = "{}"
# create an instance of UsageReportCreate from a JSON string
usage_report_create_instance = UsageReportCreate.from_json(json)
# print the JSON string representation of the object
print(UsageReportCreate.to_json())

# convert the object into a dict
usage_report_create_dict = usage_report_create_instance.to_dict()
# create an instance of UsageReportCreate from a dict
usage_report_create_from_dict = UsageReportCreate.from_dict(usage_report_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


