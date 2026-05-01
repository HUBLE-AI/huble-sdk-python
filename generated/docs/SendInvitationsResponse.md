# SendInvitationsResponse

Response schema for send invitations endpoint

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**sent_count** | **int** |  | 
**failed_emails** | **List[str]** | Emails that failed to send | [optional] 
**invitations** | [**List[InvitationResponse]**](InvitationResponse.md) | Created invitations | [optional] 

## Example

```python
from llmhub_generated.models.send_invitations_response import SendInvitationsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SendInvitationsResponse from a JSON string
send_invitations_response_instance = SendInvitationsResponse.from_json(json)
# print the JSON string representation of the object
print(SendInvitationsResponse.to_json())

# convert the object into a dict
send_invitations_response_dict = send_invitations_response_instance.to_dict()
# create an instance of SendInvitationsResponse from a dict
send_invitations_response_from_dict = SendInvitationsResponse.from_dict(send_invitations_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


