# OdooAuthenticateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_url** | **str** | Odoo instance URL (e.g. https://mycompany.odoo.com) | 
**db** | **str** | Odoo database name | 
**username** | **str** | Odoo username (email) | 
**api_key** | **str** | Odoo API key or password | 

## Example

```python
from llmhub_generated.models.odoo_authenticate_request import OdooAuthenticateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OdooAuthenticateRequest from a JSON string
odoo_authenticate_request_instance = OdooAuthenticateRequest.from_json(json)
# print the JSON string representation of the object
print(OdooAuthenticateRequest.to_json())

# convert the object into a dict
odoo_authenticate_request_dict = odoo_authenticate_request_instance.to_dict()
# create an instance of OdooAuthenticateRequest from a dict
odoo_authenticate_request_from_dict = OdooAuthenticateRequest.from_dict(odoo_authenticate_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


