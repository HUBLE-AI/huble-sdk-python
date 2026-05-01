# InvoiceListResponse

List of invoices response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | [optional] [default to True]
**invoices** | [**List[InvoiceResponse]**](InvoiceResponse.md) |  | 
**total_count** | **int** |  | 
**page** | **int** |  | [optional] [default to 1]
**page_size** | **int** |  | [optional] [default to 20]

## Example

```python
from llmhub_generated.models.invoice_list_response import InvoiceListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceListResponse from a JSON string
invoice_list_response_instance = InvoiceListResponse.from_json(json)
# print the JSON string representation of the object
print(InvoiceListResponse.to_json())

# convert the object into a dict
invoice_list_response_dict = invoice_list_response_instance.to_dict()
# create an instance of InvoiceListResponse from a dict
invoice_list_response_from_dict = InvoiceListResponse.from_dict(invoice_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


