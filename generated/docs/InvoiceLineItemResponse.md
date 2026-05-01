# InvoiceLineItemResponse

Invoice line item response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**line_id** | **str** |  | 
**description** | **str** |  | 
**endpoint_path** | **str** |  | [optional] 
**provider** | **str** |  | [optional] 
**quantity** | **int** |  | 
**total_tokens** | **int** |  | [optional] 
**unit_price_eur** | **float** |  | 
**line_total_eur** | **float** |  | 
**sort_order** | **int** |  | [optional] [default to 0]

## Example

```python
from llmhub_generated.models.invoice_line_item_response import InvoiceLineItemResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceLineItemResponse from a JSON string
invoice_line_item_response_instance = InvoiceLineItemResponse.from_json(json)
# print the JSON string representation of the object
print(InvoiceLineItemResponse.to_json())

# convert the object into a dict
invoice_line_item_response_dict = invoice_line_item_response_instance.to_dict()
# create an instance of InvoiceLineItemResponse from a dict
invoice_line_item_response_from_dict = InvoiceLineItemResponse.from_dict(invoice_line_item_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


