# V2DataRerankResponse

Response for document reranking

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
**results** | **List[Optional[Dict[str, object]]]** | Ranked documents: [{index, text, score}, ...]. Score 0-1, higher&#x3D;more relevant | 
**num_results** | **int** | Number of results returned | 

## Example

```python
from llmhub_generated.models.v2_data_rerank_response import V2DataRerankResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V2DataRerankResponse from a JSON string
v2_data_rerank_response_instance = V2DataRerankResponse.from_json(json)
# print the JSON string representation of the object
print(V2DataRerankResponse.to_json())

# convert the object into a dict
v2_data_rerank_response_dict = v2_data_rerank_response_instance.to_dict()
# create an instance of V2DataRerankResponse from a dict
v2_data_rerank_response_from_dict = V2DataRerankResponse.from_dict(v2_data_rerank_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


