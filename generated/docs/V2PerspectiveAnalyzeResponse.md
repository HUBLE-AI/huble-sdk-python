# V2PerspectiveAnalyzeResponse

Response for Perspective API toxicity analysis

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**content** | **object** |  | 
**provider_used** | **str** |  | 
**model_used** | **str** |  | 
**tokens_used** | **int** |  | 
**cost_usd** | **float** |  | 
**generation_time_ms** | **int** |  | 
**log_id** | **str** |  | 
**attribute_scores** | **Dict[str, Optional[Dict[str, object]]]** | Scores per attribute: {TOXICITY: {summary_score: 0.85, span_scores: [...]}, ...} | 
**detected_languages** | **List[str]** |  | [optional] 
**is_toxic** | **bool** |  | [optional] 
**toxicity_level** | **str** |  | [optional] 
**toxicity_score** | **float** |  | [optional] 

## Example

```python
from llmhub_generated.models.v2_perspective_analyze_response import V2PerspectiveAnalyzeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V2PerspectiveAnalyzeResponse from a JSON string
v2_perspective_analyze_response_instance = V2PerspectiveAnalyzeResponse.from_json(json)
# print the JSON string representation of the object
print(V2PerspectiveAnalyzeResponse.to_json())

# convert the object into a dict
v2_perspective_analyze_response_dict = v2_perspective_analyze_response_instance.to_dict()
# create an instance of V2PerspectiveAnalyzeResponse from a dict
v2_perspective_analyze_response_from_dict = V2PerspectiveAnalyzeResponse.from_dict(v2_perspective_analyze_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


