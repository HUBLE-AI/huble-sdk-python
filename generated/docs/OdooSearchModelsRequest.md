# OdooSearchModelsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_url** | **str** | Odoo instance URL (e.g. https://mycompany.odoo.com) | 
**db** | **str** | Odoo database name | 
**username** | **str** | Odoo username (email) | 
**api_key** | **str** | Odoo API key or password | 
**uid** | **int** | Authenticated Odoo user ID | 
**query** | **str** | Search query for model name or display name | [optional] [default to '']

## Example

```python
from llmhub_generated.models.odoo_search_models_request import OdooSearchModelsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OdooSearchModelsRequest from a JSON string
odoo_search_models_request_instance = OdooSearchModelsRequest.from_json(json)
# print the JSON string representation of the object
print(OdooSearchModelsRequest.to_json())

# convert the object into a dict
odoo_search_models_request_dict = odoo_search_models_request_instance.to_dict()
# create an instance of OdooSearchModelsRequest from a dict
odoo_search_models_request_from_dict = OdooSearchModelsRequest.from_dict(odoo_search_models_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


