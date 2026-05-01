# ModelUsageByCustomer

Usage statistics for a model by customer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**org_id** | **int** |  | 
**org_name** | **str** |  | 
**model_id** | **str** |  | 
**model_name** | **str** |  | 
**provider_name** | **str** |  | 
**model_type_name** | **str** |  | 
**usage_date** | **datetime** |  | 
**total_calls** | **int** |  | 
**successful_calls** | **int** |  | 
**failed_calls** | **int** |  | 
**total_input_tokens** | **int** |  | 
**total_output_tokens** | **int** |  | 
**total_tokens** | **int** |  | 
**total_cost_eur** | **float** |  | 
**avg_cost_per_call** | **float** |  | 
**avg_generation_time_ms** | **float** |  | 
**min_generation_time_ms** | **int** |  | 
**max_generation_time_ms** | **int** |  | 

## Example

```python
from llmhub_generated.models.model_usage_by_customer import ModelUsageByCustomer

# TODO update the JSON string below
json = "{}"
# create an instance of ModelUsageByCustomer from a JSON string
model_usage_by_customer_instance = ModelUsageByCustomer.from_json(json)
# print the JSON string representation of the object
print(ModelUsageByCustomer.to_json())

# convert the object into a dict
model_usage_by_customer_dict = model_usage_by_customer_instance.to_dict()
# create an instance of ModelUsageByCustomer from a dict
model_usage_by_customer_from_dict = ModelUsageByCustomer.from_dict(model_usage_by_customer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


