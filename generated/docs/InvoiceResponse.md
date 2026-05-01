# InvoiceResponse

Invoice response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invoice_id** | **str** |  | 
**org_id** | **int** |  | 
**invoice_number** | **str** |  | 
**invoice_month** | **datetime** |  | 
**status** | **str** |  | 
**subtotal_eur** | **float** |  | 
**vat_rate** | **float** |  | 
**vat_amount_eur** | **float** |  | 
**total_eur** | **float** |  | 
**pdf_path** | **str** |  | [optional] 
**pdf_generated_at** | **datetime** |  | [optional] 
**issued_at** | **datetime** |  | [optional] 
**due_date** | **datetime** |  | [optional] 
**paid_at** | **datetime** |  | [optional] 
**payment_reference** | **str** |  | [optional] 
**notes** | **str** |  | [optional] 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**line_items** | [**List[InvoiceLineItemResponse]**](InvoiceLineItemResponse.md) |  | [optional] 
**org_name** | **str** |  | [optional] 

## Example

```python
from llmhub_generated.models.invoice_response import InvoiceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceResponse from a JSON string
invoice_response_instance = InvoiceResponse.from_json(json)
# print the JSON string representation of the object
print(InvoiceResponse.to_json())

# convert the object into a dict
invoice_response_dict = invoice_response_instance.to_dict()
# create an instance of InvoiceResponse from a dict
invoice_response_from_dict = InvoiceResponse.from_dict(invoice_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


