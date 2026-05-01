# SEPAListResponse

SEPA payment method response for organization

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | [optional] [default to True]
**sepa** | [**SEPAResponse**](SEPAResponse.md) |  | [optional] 
**has_sepa** | **bool** |  | [optional] [default to False]

## Example

```python
from llmhub_generated.models.sepa_list_response import SEPAListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SEPAListResponse from a JSON string
sepa_list_response_instance = SEPAListResponse.from_json(json)
# print the JSON string representation of the object
print(SEPAListResponse.to_json())

# convert the object into a dict
sepa_list_response_dict = sepa_list_response_instance.to_dict()
# create an instance of SEPAListResponse from a dict
sepa_list_response_from_dict = SEPAListResponse.from_dict(sepa_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


