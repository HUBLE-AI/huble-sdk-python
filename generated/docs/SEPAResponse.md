# SEPAResponse

SEPA payment method response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sepa_id** | **str** |  | 
**org_id** | **int** |  | 
**account_holder_name** | **str** |  | 
**iban_masked** | **str** |  | 
**iban_last4** | **str** |  | 
**iban_country** | **str** |  | 
**bic** | **str** |  | [optional] 
**bank_name** | **str** |  | [optional] 
**mandate_reference** | **str** |  | 
**mandate_signed_at** | **datetime** |  | [optional] 
**mandate_status** | **str** |  | 
**is_active** | **bool** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from llmhub_generated.models.sepa_response import SEPAResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SEPAResponse from a JSON string
sepa_response_instance = SEPAResponse.from_json(json)
# print the JSON string representation of the object
print(SEPAResponse.to_json())

# convert the object into a dict
sepa_response_dict = sepa_response_instance.to_dict()
# create an instance of SEPAResponse from a dict
sepa_response_from_dict = SEPAResponse.from_dict(sepa_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


