# OrganizationUpdate

Schema for updating an organization

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**org_name** | **str** |  | [optional] 
**legal_name** | **str** |  | [optional] 
**vat_number** | **str** |  | [optional] 
**tax_id** | **str** |  | [optional] 
**billing_email** | **str** |  | [optional] 
**billing_address** | **str** |  | [optional] 
**billing_city** | **str** |  | [optional] 
**billing_postal_code** | **str** |  | [optional] 
**billing_country_code** | **str** |  | [optional] 
**currency_code** | **str** |  | [optional] 
**payment_method** | **str** |  | [optional] 
**payment_terms_days** | **int** |  | [optional] 
**monthly_budget_eur** | **float** |  | [optional] 
**is_active** | **bool** |  | [optional] 
**notes** | **str** |  | [optional] 

## Example

```python
from llmhub_generated.models.organization_update import OrganizationUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationUpdate from a JSON string
organization_update_instance = OrganizationUpdate.from_json(json)
# print the JSON string representation of the object
print(OrganizationUpdate.to_json())

# convert the object into a dict
organization_update_dict = organization_update_instance.to_dict()
# create an instance of OrganizationUpdate from a dict
organization_update_from_dict = OrganizationUpdate.from_dict(organization_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


