# OrganizationCreate

Schema for creating a new organization

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**org_name** | **str** | Organization name (unique) | 
**legal_name** | **str** |  | [optional] 
**vat_number** | **str** |  | [optional] 
**tax_id** | **str** |  | [optional] 
**billing_email** | **str** | Billing contact email | 
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
from llmhub_generated.models.organization_create import OrganizationCreate

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationCreate from a JSON string
organization_create_instance = OrganizationCreate.from_json(json)
# print the JSON string representation of the object
print(OrganizationCreate.to_json())

# convert the object into a dict
organization_create_dict = organization_create_instance.to_dict()
# create an instance of OrganizationCreate from a dict
organization_create_from_dict = OrganizationCreate.from_dict(organization_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


