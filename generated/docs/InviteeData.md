# InviteeData

Single invitee data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Invitee name | 
**email** | **str** | Invitee email address | 

## Example

```python
from llmhub_generated.models.invitee_data import InviteeData

# TODO update the JSON string below
json = "{}"
# create an instance of InviteeData from a JSON string
invitee_data_instance = InviteeData.from_json(json)
# print the JSON string representation of the object
print(InviteeData.to_json())

# convert the object into a dict
invitee_data_dict = invitee_data_instance.to_dict()
# create an instance of InviteeData from a dict
invitee_data_from_dict = InviteeData.from_dict(invitee_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


