# V2AgentChatResponse

Agent chat response. Content / tool_calls / stop_reason rendered in the requested wire shape; bookkeeping fields stay canonical.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | [optional] [default to True]
**content** | **object** |  | [optional] 
**tool_calls** | **List[Dict[str, object]]** |  | [optional] 
**stop_reason** | **str** |  | 
**provider_used** | **str** |  | 
**model_used** | **str** |  | 
**input_tokens** | **int** |  | [optional] [default to 0]
**output_tokens** | **int** |  | [optional] [default to 0]
**tokens_used** | **int** |  | [optional] [default to 0]
**cost_usd** | **float** |  | [optional] [default to 0.0]
**generation_time_ms** | **int** |  | [optional] [default to 0]
**log_id** | **str** |  | [optional] 
**provider_metadata** | **Dict[str, object]** |  | [optional] 
**shape** | **str** |  | 

## Example

```python
from llmhub_generated.models.v2_agent_chat_response import V2AgentChatResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V2AgentChatResponse from a JSON string
v2_agent_chat_response_instance = V2AgentChatResponse.from_json(json)
# print the JSON string representation of the object
print(V2AgentChatResponse.to_json())

# convert the object into a dict
v2_agent_chat_response_dict = v2_agent_chat_response_instance.to_dict()
# create an instance of V2AgentChatResponse from a dict
v2_agent_chat_response_from_dict = V2AgentChatResponse.from_dict(v2_agent_chat_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


