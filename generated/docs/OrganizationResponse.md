# OrganizationResponse

Response schema for organization

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**org_id** | **int** |  | 
**org_name** | **str** |  | 
**legal_name** | **str** |  | 
**vat_number** | **str** |  | 
**tax_id** | **str** |  | 
**billing_email** | **str** |  | 
**billing_address** | **str** |  | 
**billing_city** | **str** |  | 
**billing_postal_code** | **str** |  | 
**billing_country_code** | **str** |  | 
**currency_code** | **str** |  | 
**payment_method** | **str** |  | 
**payment_terms_days** | **int** |  | 
**monthly_budget_eur** | **float** |  | 
**current_month_spent_eur** | **float** |  | 
**is_active** | **bool** |  | 
**notes** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**total_api_clients** | **int** |  | [optional] 
**active_api_clients** | **int** |  | [optional] 
**total_users** | **int** |  | [optional] 
**active_users** | **int** |  | [optional] 
**last_30_days_spent** | **float** |  | [optional] 
**super_dev_assignment** | [**SuperDevOrgAssignmentResponse**](SuperDevOrgAssignmentResponse.md) |  | [optional] 

## Example

```python
from llmhub_generated.models.organization_response import OrganizationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationResponse from a JSON string
organization_response_instance = OrganizationResponse.from_json(json)
# print the JSON string representation of the object
print(OrganizationResponse.to_json())

# convert the object into a dict
organization_response_dict = organization_response_instance.to_dict()
# create an instance of OrganizationResponse from a dict
organization_response_from_dict = OrganizationResponse.from_dict(organization_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


