# groundx.model.search_response_search.SearchResponseSearch

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**count** | decimal.Decimal, int,  | decimal.Decimal,  | Total results | [optional] 
**[results](#results)** | list, tuple,  | tuple,  |  | [optional] 
**query** | str,  | str,  | The search query | [optional] 
**score** | decimal.Decimal, int, float,  | decimal.Decimal,  | Top result relevance score | [optional] 
**text** | str,  | str,  | Combined text from results | [optional] 
**nextToken** | str,  | str,  | For paginated results | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# results

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**SearchResultItem**](SearchResultItem.md) | [**SearchResultItem**](SearchResultItem.md) | [**SearchResultItem**](SearchResultItem.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

