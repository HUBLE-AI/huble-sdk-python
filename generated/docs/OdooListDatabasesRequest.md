# OdooListDatabasesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_url** | **str** | Odoo instance URL | 

## Example

```python
from llmhub_generated.models.odoo_list_databases_request import OdooListDatabasesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OdooListDatabasesRequest from a JSON string
odoo_list_databases_request_instance = OdooListDatabasesRequest.from_json(json)
# print the JSON string representation of the object
print(OdooListDatabasesRequest.to_json())

# convert the object into a dict
odoo_list_databases_request_dict = odoo_list_databases_request_instance.to_dict()
# create an instance of OdooListDatabasesRequest from a dict
odoo_list_databases_request_from_dict = OdooListDatabasesRequest.from_dict(odoo_list_databases_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


