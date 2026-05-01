# SEPAValidateResponse

IBAN/BIC validation response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**iban_valid** | **bool** |  | 
**bic_valid** | **bool** |  | [optional] 
**iban_formatted** | **str** |  | [optional] 
**bank_name** | **str** |  | [optional] 
**bank_country** | **str** |  | [optional] 
**error_message** | **str** |  | [optional] 

## Example

```python
from llmhub_generated.models.sepa_validate_response import SEPAValidateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SEPAValidateResponse from a JSON string
sepa_validate_response_instance = SEPAValidateResponse.from_json(json)
# print the JSON string representation of the object
print(SEPAValidateResponse.to_json())

# convert the object into a dict
sepa_validate_response_dict = sepa_validate_response_instance.to_dict()
# create an instance of SEPAValidateResponse from a dict
sepa_validate_response_from_dict = SEPAValidateResponse.from_dict(sepa_validate_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


