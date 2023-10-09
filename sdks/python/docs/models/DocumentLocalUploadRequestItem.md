# groundx.model.document_local_upload_request_item.DocumentLocalUploadRequestItem

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**metadata** | [**DocumentLocalUploadRequestItemMetadata**](DocumentLocalUploadRequestItemMetadata.md) | [**DocumentLocalUploadRequestItemMetadata**](DocumentLocalUploadRequestItemMetadata.md) |  | 
**blob** | bytes, io.FileIO, io.BufferedReader,  | bytes, FileIO,  | The actual file being uploaded. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

