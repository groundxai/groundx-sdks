<div align="center">

[![Visit Groundx](https://raw.githubusercontent.com/groundxai/groundx-sdks/HEAD/sdks/python/header.png)](https://www.groundx.ai)

# Groundx

Ground Your RAG Apps in Fact not Fiction


[![PyPI](https://img.shields.io/badge/PyPI-v1.3.2-blue)](https://pypi.org/project/groundx-python-sdk/1.3.2)
[![README.md](https://img.shields.io/badge/README-Click%20Here-green)](https://github.com/groundxai/groundx-sdks/tree/main/sdks/python#readme)
[![More Info](https://img.shields.io/badge/More%20Info-Click%20Here-orange)](https://www.groundx.ai/)

</div>

## Table of Contents

<!-- toc -->

- [Requirements](#requirements)
- [Installing](#installing)
- [Getting Started](#getting-started)
- [Async](#async)
- [Reference](#reference)
  * [`groundx.api_keys.list`](#groundxapi_keyslist)
  * [`groundx.buckets.get`](#groundxbucketsget)
  * [`groundx.buckets.list`](#groundxbucketslist)
  * [`groundx.buckets.update`](#groundxbucketsupdate)
  * [`groundx.documents.delete`](#groundxdocumentsdelete)
  * [`groundx.documents.get`](#groundxdocumentsget)
  * [`groundx.documents.get_processing_status_by_id`](#groundxdocumentsget_processing_status_by_id)
  * [`groundx.documents.list`](#groundxdocumentslist)
  * [`groundx.documents.lookup`](#groundxdocumentslookup)
  * [`groundx.documents.upload_local`](#groundxdocumentsupload_local)
  * [`groundx.documents.upload_remote`](#groundxdocumentsupload_remote)
  * [`groundx.projects.get`](#groundxprojectsget)
  * [`groundx.projects.list`](#groundxprojectslist)
  * [`groundx.projects.update`](#groundxprojectsupdate)
  * [`groundx.search.content`](#groundxsearchcontent)

<!-- tocstop -->

## Requirements

Python >=3.7

## Installing

```sh
pip install groundx-python-sdk==1.3.2
```

## Getting Started

```python
from pprint import pprint
from groundx import Groundx, ApiException

groundx = Groundx(
    api_key="YOUR_API_KEY",
)

try:
    # Get API keys
    list_response = groundx.api_keys.list()
    pprint(list_response.body)
    pprint(list_response.body["api_keys"])
    pprint(list_response.headers)
    pprint(list_response.status)
    pprint(list_response.round_trip_time)
except ApiException as e:
    print("Exception when calling APIKeysApi.list: %s\n" % e)
    pprint(e.body)
    if e.status == 405:
        pprint(e.body["message"])
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Async

`async` support is available by prepending `a` to any method.

```python
import asyncio
from pprint import pprint
from groundx import Groundx, ApiException

groundx = Groundx(
    api_key="YOUR_API_KEY",
)


async def main():
    try:
        # Get API keys
        list_response = await groundx.api_keys.alist()
        pprint(list_response.body)
        pprint(list_response.body["api_keys"])
        pprint(list_response.headers)
        pprint(list_response.status)
        pprint(list_response.round_trip_time)
    except ApiException as e:
        print("Exception when calling APIKeysApi.list: %s\n" % e)
        pprint(e.body)
        if e.status == 405:
            pprint(e.body["message"])
        pprint(e.headers)
        pprint(e.status)
        pprint(e.reason)
        pprint(e.round_trip_time)


asyncio.run(main())
```


## Reference
### `groundx.api_keys.list`

Retrieve the API keys for your account.

#### 🛠️ Usage

```python
list_response = groundx.api_keys.list()
```

#### 🔄 Return

[ApiKeyManagementListResponse](./groundx/type/api_key_management_list_response.py)

#### 🌐 Endpoint

`/v1/apikey` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `groundx.buckets.get`

Look up a bucket by its bucketId.

#### 🛠️ Usage

```python
get_response = groundx.buckets.get(
    bucket_id=1,
)
```

#### ⚙️ Parameters

##### bucket_id: `int`

The ID of the bucket to retrieve.

#### 🔄 Return

[BucketResponse](./groundx/type/bucket_response.py)

#### 🌐 Endpoint

`/v1/bucket/{bucketId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `groundx.buckets.list`

Look up existing buckets associated with your account.

#### 🛠️ Usage

```python
list_response = groundx.buckets.list()
```

#### 🔄 Return

[BucketListResponse](./groundx/type/bucket_list_response.py)

#### 🌐 Endpoint

`/v1/bucket` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `groundx.buckets.update`

Update the configurations of an existing bucket.

#### 🛠️ Usage

```python
update_response = groundx.buckets.update(
    bucket={
        "name": "your_bucket_name",
    },
    bucket_id=1,
)
```

#### ⚙️ Parameters

##### bucket: [`BucketUpdateRequestBucket`](./groundx/type/bucket_update_request_bucket.py)


##### bucket_id: `int`

The ID of the bucket to update.

#### ⚙️ Request Body

[`BucketUpdateRequest`](./groundx/type/bucket_update_request.py)
#### 🔄 Return

[BucketUpdateResponse](./groundx/type/bucket_update_response.py)

#### 🌐 Endpoint

`/v1/bucket/{bucketId}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `groundx.documents.delete`

Delete a document

#### 🛠️ Usage

```python
delete_response = groundx.documents.delete(
    document_id="documentId_example",
)
```

#### ⚙️ Parameters

##### document_id: `str`

#### 🔄 Return

[DocumentDeleteResponse](./groundx/type/document_delete_response.py)

#### 🌐 Endpoint

`/v1/ingest/document/{documentId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `groundx.documents.get`

Look up an existing document by its ID

#### 🛠️ Usage

```python
get_response = groundx.documents.get(
    document_id="documentId_example",
)
```

#### ⚙️ Parameters

##### document_id: `str`

#### 🔄 Return

[DocumentResponse](./groundx/type/document_response.py)

#### 🌐 Endpoint

`/v1/ingest/document/{documentId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `groundx.documents.get_processing_status_by_id`

Look up the processing status of documents for a given processId

#### 🛠️ Usage

```python
get_processing_status_by_id_response = groundx.documents.get_processing_status_by_id(
    process_id="processId_example",
)
```

#### ⚙️ Parameters

##### process_id: `str`

#### 🔄 Return

[ProcessStatusResponse](./groundx/type/process_status_response.py)

#### 🌐 Endpoint

`/v1/ingest/{processId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `groundx.documents.list`

Look up all existing documents

#### 🛠️ Usage

```python
list_response = groundx.documents.list(
    n=1,
    next_token="string_example",
)
```

#### ⚙️ Parameters

##### n: `int`

##### next_token: `str`

#### 🔄 Return

[DocumentListResponse](./groundx/type/document_list_response.py)

#### 🌐 Endpoint

`/v1/ingest/documents` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `groundx.documents.lookup`

Look up existing documents by processId, bucketId, or projectId

#### 🛠️ Usage

```python
lookup_response = groundx.documents.lookup(
    id=1,
    n=1,
    next_token="string_example",
)
```

#### ⚙️ Parameters

##### id: `int`

##### n: `int`

##### next_token: `str`

#### 🔄 Return

[DocumentLookupResponse](./groundx/type/document_lookup_response.py)

#### 🌐 Endpoint

`/v1/ingest/documents/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `groundx.documents.upload_local`

Upload local documents to GroundX

#### 🛠️ Usage

```python
upload_local_response = groundx.documents.upload_local(
    body=[
        {
            "blob": open("/path/to/file", "rb"),
            "metadata": {
                "bucket_id": 1234,
                "file_name": "my_file.txt",
                "file_type": "txt",
                "callback_data": "my_callback_data",
                "callback_url": "https://my.callback.url.com",
            },
        }
    ],
)
```

#### ⚙️ Request Body

[`DocumentLocalUploadRequest`](./groundx/type/document_local_upload_request.py)
#### 🔄 Return

[IngestResponse](./groundx/type/ingest_response.py)

#### 🌐 Endpoint

`/v1/ingest/documents/local` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `groundx.documents.upload_remote`

Upload hosted documents to GroundX

#### 🛠️ Usage

```python
upload_remote_response = groundx.documents.upload_remote(
    documents=[
        {
            "bucket_id": 1234,
            "source_url": "https://my.source.url.com/file.txt",
            "callback_data": "my_callback_data",
            "callback_url": "https://my.callback.url.com",
            "type": "txt",
        }
    ],
)
```

#### ⚙️ Parameters

##### documents: [`DocumentRemoteUploadRequestDocuments`](./groundx/type/document_remote_upload_request_documents.py)

#### ⚙️ Request Body

[`DocumentRemoteUploadRequest`](./groundx/type/document_remote_upload_request.py)
#### 🔄 Return

[IngestResponse](./groundx/type/ingest_response.py)

#### 🌐 Endpoint

`/v1/ingest/documents/remote` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `groundx.projects.get`

This endpoint allows you to retrieve a specific project by projectId.

#### 🛠️ Usage

```python
get_response = groundx.projects.get(
    project_id="projectId_example",
)
```

#### ⚙️ Parameters

##### project_id: `str`

The ID of the project to retrieve.

#### 🔄 Return

[ProjectResponse](./groundx/type/project_response.py)

#### 🌐 Endpoint

`/v1/project/{projectId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `groundx.projects.list`

This endpoint allows you to retrieve your existing projects.

#### 🛠️ Usage

```python
list_response = groundx.projects.list()
```

#### 🔄 Return

[ProjectListResponse](./groundx/type/project_list_response.py)

#### 🌐 Endpoint

`/v1/project` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `groundx.projects.update`

This endpoint allows you to update an existing project.

#### 🛠️ Usage

```python
update_response = groundx.projects.update(
    project={
        "name": "your_project_name",
    },
    project_id="projectId_example",
)
```

#### ⚙️ Parameters

##### project: [`ProjectUpdateRequestProject`](./groundx/type/project_update_request_project.py)


##### project_id: `str`

The ID of the project to update.

#### ⚙️ Request Body

[`ProjectUpdateRequest`](./groundx/type/project_update_request.py)
#### 🔄 Return

[ProjectResponse](./groundx/type/project_response.py)

#### 🌐 Endpoint

`/v1/project/{projectId}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `groundx.search.content`

Search and retrieve relevant content from a project, group, or bucket by id.

#### 🛠️ Usage

```python
content_response = groundx.search.content(
    search={
        "query": "my search query",
        "next_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9",
    },
    id=1,
    n=20,
)
```

#### ⚙️ Parameters

##### search: [`SearchRequestSearch`](./groundx/type/search_request_search.py)


##### id: `int`

The ID of the project, group, or bucket to search within.

##### n: `int`

Number of results

#### ⚙️ Request Body

[`SearchRequest`](./groundx/type/search_request.py)
#### 🔄 Return

[SearchResponse](./groundx/type/search_response.py)

#### 🌐 Endpoint

`/v1/search/{id}` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author
This Python package is automatically generated by [Konfig](https://konfigthis.com)
