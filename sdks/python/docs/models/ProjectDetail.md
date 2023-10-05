# groundx.model.project_detail.ProjectDetail

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**projectId** | decimal.Decimal, int,  | decimal.Decimal,  |  | 
**[buckets](#buckets)** | list, tuple,  | tuple,  |  | [optional] 
**created** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**fileCount** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**fileSize** | str,  | str,  |  | [optional] 
**name** | str,  | str,  |  | [optional] 
**updated** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# buckets

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**BucketDetail**](BucketDetail.md) | [**BucketDetail**](BucketDetail.md) | [**BucketDetail**](BucketDetail.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

