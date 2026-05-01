# SEPACreateRequest

Request to create/update SEPA payment method

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_holder_name** | **str** | Account holder name | 
**iban** | **str** | IBAN | 
**bic** | **str** |  | [optional] 
**mandate_signed_at** | **date** |  | [optional] 

## Example

```python
from llmhub_generated.models.sepa_create_request import SEPACreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SEPACreateRequest from a JSON string
sepa_create_request_instance = SEPACreateRequest.from_json(json)
# print the JSON string representation of the object
print(SEPACreateRequest.to_json())

# convert the object into a dict
sepa_create_request_dict = sepa_create_request_instance.to_dict()
# create an instance of SEPACreateRequest from a dict
sepa_create_request_from_dict = SEPACreateRequest.from_dict(sepa_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


