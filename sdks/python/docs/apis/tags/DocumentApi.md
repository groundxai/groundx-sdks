# groundx.document

All URIs are relative to *https://api.groundx.ai/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete**](#delete) | **delete** /v1/ingest/document/{documentId} | Delete documents
[**get**](#get) | **get** /v1/ingest/document/{documentId} | Look up an existing document
[**get_processing_status_by_id**](#get_processing_status_by_id) | **get** /v1/ingest/{processId} | Look up document processing status by processId
[**list**](#list) | **get** /v1/ingest/documents | Look up all existing documents
[**lookup**](#lookup) | **get** /v1/ingest/documents/{id} | Look up existing documents by processId, bucketId, or projectId
[**upload_local**](#upload_local) | **post** /v1/ingest/documents/local | Upload local documents to GroundX
[**upload_remote**](#upload_remote) | **post** /v1/ingest/documents/remote | Upload hosted documents to GroundX

# **delete**

Delete documents

### Example

```python
from pprint import pprint
from groundx import Groundx, ApiException

groundx = Groundx(
    api_key="YOUR_API_KEY",
)

try:
    # Delete documents
    delete_response = groundx.document.delete(
        document_id="documentId_example",  # required
    )
    pprint(delete_response.body)
    pprint(delete_response.body["message"])
    pprint(delete_response.headers)
    pprint(delete_response.status)
    pprint(delete_response.round_trip_time)
except ApiException as e:
    print("Exception when calling DocumentApi.delete: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get**

Look up an existing document

### Example

```python
from pprint import pprint
from groundx import Groundx, ApiException

groundx = Groundx(
    api_key="YOUR_API_KEY",
)

try:
    # Look up an existing document
    get_response = groundx.document.get(
        document_id="documentId_example",  # required
    )
    pprint(get_response.body)
    pprint(get_response.body["document"])
    pprint(get_response.headers)
    pprint(get_response.status)
    pprint(get_response.round_trip_time)
except ApiException as e:
    print("Exception when calling DocumentApi.get: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_processing_status_by_id**

Look up document processing status by processId

### Example

```python
from pprint import pprint
from groundx import Groundx, ApiException

groundx = Groundx(
    api_key="YOUR_API_KEY",
)

try:
    # Look up document processing status by processId
    get_processing_status_by_id_response = groundx.document.get_processing_status_by_id(
        process_id="processId_example",  # required
    )
    pprint(get_processing_status_by_id_response.body)
    pprint(get_processing_status_by_id_response.body["ingest"])
    pprint(get_processing_status_by_id_response.headers)
    pprint(get_processing_status_by_id_response.status)
    pprint(get_processing_status_by_id_response.round_trip_time)
except ApiException as e:
    print("Exception when calling DocumentApi.get_processing_status_by_id: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **list**

Look up all existing documents

### Example

```python
from pprint import pprint
from groundx import Groundx, ApiException

groundx = Groundx(
    api_key="YOUR_API_KEY",
)

try:
    # Look up all existing documents
    list_response = groundx.document.list()
    pprint(list_response.body)
    pprint(list_response.body["documents"])
    pprint(list_response.headers)
    pprint(list_response.status)
    pprint(list_response.round_trip_time)
except ApiException as e:
    print("Exception when calling DocumentApi.list: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **lookup**

Look up existing documents by processId, bucketId, or projectId

### Example

```python
from pprint import pprint
from groundx import Groundx, ApiException

groundx = Groundx(
    api_key="YOUR_API_KEY",
)

try:
    # Look up existing documents by processId, bucketId, or projectId
    lookup_response = groundx.document.lookup(
        id="id_example",  # required
    )
    pprint(lookup_response.body)
    pprint(lookup_response.body["documents"])
    pprint(lookup_response.headers)
    pprint(lookup_response.status)
    pprint(lookup_response.round_trip_time)
except ApiException as e:
    print("Exception when calling DocumentApi.lookup: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **upload_local**

Upload local documents to GroundX

### Example

```python
from pprint import pprint
from groundx import Groundx, ApiException

groundx = Groundx(
    api_key="YOUR_API_KEY",
)

try:
    # Upload local documents to GroundX
    upload_local_response = groundx.document.upload_local(
        blob=[open("/path/to/file", "rb")],  # required
        metadata={
            "bucket_id": 1234,
            "file_name": "my_file.txt",
            "file_type": "txt",
            "callback_data": "my_callback_data",
            "callback_url": "https://my.callback.url.com",
        },  # required
    )
    pprint(upload_local_response.body)
    pprint(upload_local_response.body["ingest"])
    pprint(upload_local_response.headers)
    pprint(upload_local_response.status)
    pprint(upload_local_response.round_trip_time)
except ApiException as e:
    print("Exception when calling DocumentApi.upload_local: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **upload_remote**

Upload hosted documents to GroundX

### Example

```python
from pprint import pprint
from groundx import Groundx, ApiException

groundx = Groundx(
    api_key="YOUR_API_KEY",
)

try:
    # Upload hosted documents to GroundX
    upload_remote_response = groundx.document.upload_remote(
        bucket_id=1234,  # required
        source_url="https://my.source.url.com/file.txt",  # optional
        callback_data="my_callback_data",  # optional
        callback_url="https://my.callback.url.com",  # optional
        metadata={
            "key": "value",
        },  # optional
        type="txt",  # optional
        documents=[
            {
                "bucket_id": 1234,
                "source_url": "https://my.source.url.com/file.txt",
                "callback_data": "my_callback_data",
                "callback_url": "https://my.callback.url.com",
                "type": "txt",
            }
        ],  # optional
    )
    pprint(upload_remote_response.body)
    pprint(upload_remote_response.body["ingest"])
    pprint(upload_remote_response.headers)
    pprint(upload_remote_response.status)
    pprint(upload_remote_response.round_trip_time)
except ApiException as e:
    print("Exception when calling DocumentApi.upload_remote: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

