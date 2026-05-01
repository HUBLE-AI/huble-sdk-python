# SEPAValidateRequest

Request to validate IBAN/BIC

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**iban** | **str** | IBAN to validate | 
**bic** | **str** |  | [optional] 

## Example

```python
from llmhub_generated.models.sepa_validate_request import SEPAValidateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SEPAValidateRequest from a JSON string
sepa_validate_request_instance = SEPAValidateRequest.from_json(json)
# print the JSON string representation of the object
print(SEPAValidateRequest.to_json())

# convert the object into a dict
sepa_validate_request_dict = sepa_validate_request_instance.to_dict()
# create an instance of SEPAValidateRequest from a dict
sepa_validate_request_from_dict = SEPAValidateRequest.from_dict(sepa_validate_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


