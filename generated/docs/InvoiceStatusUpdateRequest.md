# InvoiceStatusUpdateRequest

Request to update invoice status

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**InvoiceStatus**](InvoiceStatus.md) | New invoice status | 
**payment_reference** | **str** |  | [optional] 
**notes** | **str** |  | [optional] 

## Example

```python
from llmhub_generated.models.invoice_status_update_request import InvoiceStatusUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceStatusUpdateRequest from a JSON string
invoice_status_update_request_instance = InvoiceStatusUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(InvoiceStatusUpdateRequest.to_json())

# convert the object into a dict
invoice_status_update_request_dict = invoice_status_update_request_instance.to_dict()
# create an instance of InvoiceStatusUpdateRequest from a dict
invoice_status_update_request_from_dict = InvoiceStatusUpdateRequest.from_dict(invoice_status_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


