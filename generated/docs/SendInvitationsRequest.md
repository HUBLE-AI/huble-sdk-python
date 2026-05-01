# SendInvitationsRequest

Request schema for sending invitations

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invitees** | [**List[InviteeData]**](InviteeData.md) | List of invitees (1-10) | 

## Example

```python
from llmhub_generated.models.send_invitations_request import SendInvitationsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SendInvitationsRequest from a JSON string
send_invitations_request_instance = SendInvitationsRequest.from_json(json)
# print the JSON string representation of the object
print(SendInvitationsRequest.to_json())

# convert the object into a dict
send_invitations_request_dict = send_invitations_request_instance.to_dict()
# create an instance of SendInvitationsRequest from a dict
send_invitations_request_from_dict = SendInvitationsRequest.from_dict(send_invitations_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


