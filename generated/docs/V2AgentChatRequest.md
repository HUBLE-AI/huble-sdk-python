# V2AgentChatRequest

Multi-turn chat with tool-use support.  Accepts BOTH OpenAI shape and Anthropic shape — auto-detected when `shape` is not set. Internally everything is canonicalised to OpenAI pivot; provider-side translators handle the SDK boundary.  Note: max_tokens floor is 1 (not 100 like V2BaseRequest) because short replies during tool loops are normal.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shape** | **str** |  | [optional] 
**response_shape** | **str** |  | [optional] 
**provider** | **str** |  | [optional] 
**model** | **str** |  | [optional] 
**messages** | **List[Optional[Dict[str, object]]]** | Multi-turn conversation. Either OpenAI or Anthropic shape. | 
**system** | **str** |  | [optional] 
**tools** | **List[Optional[Dict[str, object]]]** |  | [optional] 
**tool_choice** | [**ToolChoice**](ToolChoice.md) |  | [optional] 
**max_tokens** | **int** |  | [optional] 
**temperature** | **float** |  | [optional] 
**provider_options** | **Dict[str, Optional[Dict[str, object]]]** |  | [optional] 

## Example

```python
from llmhub_generated.models.v2_agent_chat_request import V2AgentChatRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V2AgentChatRequest from a JSON string
v2_agent_chat_request_instance = V2AgentChatRequest.from_json(json)
# print the JSON string representation of the object
print(V2AgentChatRequest.to_json())

# convert the object into a dict
v2_agent_chat_request_dict = v2_agent_chat_request_instance.to_dict()
# create an instance of V2AgentChatRequest from a dict
v2_agent_chat_request_from_dict = V2AgentChatRequest.from_dict(v2_agent_chat_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


