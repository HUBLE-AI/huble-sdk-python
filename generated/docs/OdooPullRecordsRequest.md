# OdooPullRecordsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_url** | **str** | Odoo instance URL (e.g. https://mycompany.odoo.com) | 
**db** | **str** | Odoo database name | 
**username** | **str** | Odoo username (email) | 
**api_key** | **str** | Odoo API key or password | 
**uid** | **int** | Authenticated Odoo user ID | 
**model_name** | **str** | Odoo model technical name (e.g. sale.order) | 
**last_sync_at** | **str** |  | [optional] 
**batch_size** | **int** | Records per batch | [optional] [default to 500]

## Example

```python
from llmhub_generated.models.odoo_pull_records_request import OdooPullRecordsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OdooPullRecordsRequest from a JSON string
odoo_pull_records_request_instance = OdooPullRecordsRequest.from_json(json)
# print the JSON string representation of the object
print(OdooPullRecordsRequest.to_json())

# convert the object into a dict
odoo_pull_records_request_dict = odoo_pull_records_request_instance.to_dict()
# create an instance of OdooPullRecordsRequest from a dict
odoo_pull_records_request_from_dict = OdooPullRecordsRequest.from_dict(odoo_pull_records_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


