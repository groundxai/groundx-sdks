<div align="center">

[![Visit Groundx](https://raw.githubusercontent.com/groundxai/groundx-sdks/HEAD/header.png)](https://www.groundx.ai)

# Groundx<a id="groundx"></a>

Ground Your RAG Apps in Fact not Fiction


[![PyPI](https://img.shields.io/badge/PyPI-v1.3.6-blue)](https://pypi.org/project/groundx-python-sdk/1.3.6)
[![GitHub last commit](https://img.shields.io/github/last-commit/groundxai/groundx-sdks.svg)](https://github.com/groundxai/groundx-sdks/commits)
[![README.md](https://img.shields.io/badge/README-Click%20Here-green)](https://github.com/groundxai/groundx-sdks/tree/main/sdks/python#readme)
[![More Info](https://img.shields.io/badge/More%20Info-Click%20Here-orange)](https://www.groundx.ai/)

</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

- [Requirements](#requirements)
- [Installing](#installing)
- [Getting Started](#getting-started)
- [Async](#async)
- [Reference](#reference)
  * [`groundx.buckets.create`](#groundxbucketscreate)
  * [`groundx.buckets.delete`](#groundxbucketsdelete)
  * [`groundx.buckets.get`](#groundxbucketsget)
  * [`groundx.buckets.list`](#groundxbucketslist)
  * [`groundx.buckets.update`](#groundxbucketsupdate)
  * [`groundx.documents.crawl_website`](#groundxdocumentscrawl_website)
  * [`groundx.documents.delete`](#groundxdocumentsdelete)
  * [`groundx.documents.delete_0`](#groundxdocumentsdelete_0)
  * [`groundx.documents.get`](#groundxdocumentsget)
  * [`groundx.documents.get_processing_status_by_id`](#groundxdocumentsget_processing_status_by_id)
  * [`groundx.documents.list`](#groundxdocumentslist)
  * [`groundx.documents.lookup`](#groundxdocumentslookup)
  * [`groundx.documents.upload_local`](#groundxdocumentsupload_local)
  * [`groundx.documents.upload_remote`](#groundxdocumentsupload_remote)
  * [`groundx.projects.add_bucket`](#groundxprojectsadd_bucket)
  * [`groundx.projects.create`](#groundxprojectscreate)
  * [`groundx.projects.delete`](#groundxprojectsdelete)
  * [`groundx.projects.get`](#groundxprojectsget)
  * [`groundx.projects.list`](#groundxprojectslist)
  * [`groundx.projects.remove_bucket`](#groundxprojectsremove_bucket)
  * [`groundx.projects.update`](#groundxprojectsupdate)
  * [`groundx.search.content`](#groundxsearchcontent)

<!-- tocstop -->

## Requirements<a id="requirements"></a>

Python >=3.7

## Installing<a id="installing"></a>

```sh
pip install groundx-python-sdk==1.3.6
```

## Getting Started<a id="getting-started"></a>

```python
from pprint import pprint
from groundx import Groundx, ApiException

groundx = Groundx(
    api_key="YOUR_API_KEY",
)

try:
    # Create a new bucket
    create_response = groundx.buckets.create(
        name="your_bucket_name",
    )
    pprint(create_response.body)
    pprint(create_response.body["bucket"])
    pprint(create_response.headers)
    pprint(create_response.status)
    pprint(create_response.round_trip_time)
except ApiException as e:
    print("Exception when calling BucketsApi.create: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Async<a id="async"></a>

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
        # Create a new bucket
        create_response = await groundx.buckets.acreate(
            name="your_bucket_name",
        )
        pprint(create_response.body)
        pprint(create_response.body["bucket"])
        pprint(create_response.headers)
        pprint(create_response.status)
        pprint(create_response.round_trip_time)
    except ApiException as e:
        print("Exception when calling BucketsApi.create: %s\n" % e)
        pprint(e.body)
        pprint(e.headers)
        pprint(e.status)
        pprint(e.reason)
        pprint(e.round_trip_time)


asyncio.run(main())
```


## Reference<a id="reference"></a>
### `groundx.buckets.create`<a id="groundxbucketscreate"></a>

This endpoint allows you to create a new bucket.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_response = groundx.buckets.create(
    name="your_bucket_name",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`BucketCreateRequest`](./groundx/type/bucket_create_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`BucketResponse`](./groundx/type/bucket_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/bucket` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `groundx.buckets.delete`<a id="groundxbucketsdelete"></a>

Delete a bucket

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_response = groundx.buckets.delete(
    bucket_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### bucket_id: `int`<a id="bucket_id-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`MessageResponse`](./groundx/type/message_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/bucket/{bucketId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `groundx.buckets.get`<a id="groundxbucketsget"></a>

Look up a bucket by its bucketId.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_response = groundx.buckets.get(
    bucket_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### bucket_id: `int`<a id="bucket_id-int"></a>

The ID of the bucket to retrieve.

#### 🔄 Return<a id="🔄-return"></a>

[`BucketResponse`](./groundx/type/bucket_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/bucket/{bucketId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `groundx.buckets.list`<a id="groundxbucketslist"></a>

Look up existing buckets associated with your account.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_response = groundx.buckets.list(
    n=1,
    next_token="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### n: `int`<a id="n-int"></a>

##### next_token: `str`<a id="next_token-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`BucketListResponse`](./groundx/type/bucket_list_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/bucket` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `groundx.buckets.update`<a id="groundxbucketsupdate"></a>

Update the configurations of an existing bucket.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_response = groundx.buckets.update(
    new_name="your_bucket_name",
    bucket_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### new_name: `str`<a id="new_name-str"></a>

##### bucket_id: `int`<a id="bucket_id-int"></a>

The ID of the bucket to update.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`BucketUpdateRequest`](./groundx/type/bucket_update_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`BucketUpdateResponse`](./groundx/type/bucket_update_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/bucket/{bucketId}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `groundx.documents.crawl_website`<a id="groundxdocumentscrawl_website"></a>

Crawl and ingest a website into GroundX

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
crawl_website_response = groundx.documents.crawl_website(
    websites=[
        {
            "bucket_id": 123,
            "cap": 100,
            "depth": 3,
            "source_url": "https://my.website.com",
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### websites: [`WebsiteCrawlRequestWebsites`](./groundx/type/website_crawl_request_websites.py)<a id="websites-websitecrawlrequestwebsitesgroundxtypewebsite_crawl_request_websitespy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`WebsiteCrawlRequest`](./groundx/type/website_crawl_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`IngestResponse`](./groundx/type/ingest_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/ingest/documents/website` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `groundx.documents.delete`<a id="groundxdocumentsdelete"></a>

Delete one or more documents from GroundX

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_response = groundx.documents.delete(
    document_ids=["documentIds_example"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### document_ids: List[`str`]<a id="document_ids-liststr"></a>

A comma delimited list of document IDs

#### 🔄 Return<a id="🔄-return"></a>

[`IngestResponse`](./groundx/type/ingest_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/ingest/documents` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `groundx.documents.delete_0`<a id="groundxdocumentsdelete_0"></a>

Delete a document

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_0_response = groundx.documents.delete_0(
    document_id="documentId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### document_id: `str`<a id="document_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`IngestResponse`](./groundx/type/ingest_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/ingest/document/{documentId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `groundx.documents.get`<a id="groundxdocumentsget"></a>

Look up an existing document by its ID

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_response = groundx.documents.get(
    document_id="documentId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### document_id: `str`<a id="document_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`DocumentResponse`](./groundx/type/document_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/ingest/document/{documentId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `groundx.documents.get_processing_status_by_id`<a id="groundxdocumentsget_processing_status_by_id"></a>

Look up the processing status of documents for a given processId

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_processing_status_by_id_response = groundx.documents.get_processing_status_by_id(
    process_id="processId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### process_id: `str`<a id="process_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`ProcessStatusResponse`](./groundx/type/process_status_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/ingest/{processId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `groundx.documents.list`<a id="groundxdocumentslist"></a>

Look up all existing documents

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_response = groundx.documents.list(
    n=1,
    next_token="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### n: `int`<a id="n-int"></a>

##### next_token: `str`<a id="next_token-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`DocumentListResponse`](./groundx/type/document_list_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/ingest/documents` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `groundx.documents.lookup`<a id="groundxdocumentslookup"></a>

Look up existing documents by processId, bucketId, or projectId

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
lookup_response = groundx.documents.lookup(
    id=1,
    n=1,
    next_token="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

##### n: `int`<a id="n-int"></a>

##### next_token: `str`<a id="next_token-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`DocumentLookupResponse`](./groundx/type/document_lookup_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/ingest/documents/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `groundx.documents.upload_local`<a id="groundxdocumentsupload_local"></a>

Upload local documents to GroundX

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
upload_local_response = groundx.documents.upload_local(
    body=[
        {
            "blob": open("/path/to/file", "rb"),
            "metadata": {
                "bucket_id": 1234,
                "file_name": "my_file.txt",
                "file_type": "txt",
            },
        }
    ],
)
```

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DocumentLocalUploadRequest`](./groundx/type/document_local_upload_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`IngestResponse`](./groundx/type/ingest_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/ingest/documents/local` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `groundx.documents.upload_remote`<a id="groundxdocumentsupload_remote"></a>

Upload hosted documents to GroundX

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
upload_remote_response = groundx.documents.upload_remote(
    documents=[
        {
            "bucket_id": 1234,
            "file_name": "my_file.txt",
            "file_type": "txt",
            "source_url": "https://my.source.url.com/file.txt",
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### documents: [`DocumentRemoteUploadRequestDocuments`](./groundx/type/document_remote_upload_request_documents.py)<a id="documents-documentremoteuploadrequestdocumentsgroundxtypedocument_remote_upload_request_documentspy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DocumentRemoteUploadRequest`](./groundx/type/document_remote_upload_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`IngestResponse`](./groundx/type/ingest_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/ingest/documents/remote` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `groundx.projects.add_bucket`<a id="groundxprojectsadd_bucket"></a>

This endpoint allows you to add a bucket to a project.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_bucket_response = groundx.projects.add_bucket(
    project_id=1,
    bucket_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### project_id: `int`<a id="project_id-int"></a>

The ID of the project to update.

##### bucket_id: `int`<a id="bucket_id-int"></a>

The ID of the bucket to update.

#### 🔄 Return<a id="🔄-return"></a>

[`MessageResponse`](./groundx/type/message_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/project/{projectId}/bucket/{bucketId}` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `groundx.projects.create`<a id="groundxprojectscreate"></a>

This endpoint allows you to create a new project.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_response = groundx.projects.create(
    name="your_project_name",
    bucket_name="your_new_bucket_name",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

##### bucket_name: `str`<a id="bucket_name-str"></a>

Include a bucket name to automatically create a bucket and add it to this project

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ProjectCreateRequest`](./groundx/type/project_create_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ProjectResponse`](./groundx/type/project_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/project` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `groundx.projects.delete`<a id="groundxprojectsdelete"></a>

Delete a project

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_response = groundx.projects.delete(
    project_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### project_id: `int`<a id="project_id-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`MessageResponse`](./groundx/type/message_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/project/{projectId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `groundx.projects.get`<a id="groundxprojectsget"></a>

This endpoint allows you to retrieve a specific project by projectId.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_response = groundx.projects.get(
    project_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### project_id: `int`<a id="project_id-int"></a>

The ID of the project to retrieve.

#### 🔄 Return<a id="🔄-return"></a>

[`ProjectResponse`](./groundx/type/project_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/project/{projectId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `groundx.projects.list`<a id="groundxprojectslist"></a>

This endpoint allows you to retrieve your existing projects.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_response = groundx.projects.list(
    n=1,
    next_token="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### n: `int`<a id="n-int"></a>

##### next_token: `str`<a id="next_token-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`ProjectListResponse`](./groundx/type/project_list_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/project` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `groundx.projects.remove_bucket`<a id="groundxprojectsremove_bucket"></a>

This endpoint allows you to remove a bucket from a project.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
remove_bucket_response = groundx.projects.remove_bucket(
    project_id=1,
    bucket_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### project_id: `int`<a id="project_id-int"></a>

The ID of the project to update.

##### bucket_id: `int`<a id="bucket_id-int"></a>

The ID of the bucket to update.

#### 🔄 Return<a id="🔄-return"></a>

[`MessageResponse`](./groundx/type/message_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/project/{projectId}/bucket/{bucketId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `groundx.projects.update`<a id="groundxprojectsupdate"></a>

This endpoint allows you to update an existing project.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_response = groundx.projects.update(
    new_name="your_project_name",
    project_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### new_name: `str`<a id="new_name-str"></a>

##### project_id: `int`<a id="project_id-int"></a>

The ID of the project to update.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ProjectUpdateRequest`](./groundx/type/project_update_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ProjectResponse`](./groundx/type/project_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/project/{projectId}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `groundx.search.content`<a id="groundxsearchcontent"></a>

Search and retrieve relevant content from a project or bucket by id.

#### 🛠️ Usage<a id="🛠️-usage"></a>

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

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### search: [`SearchRequestSearch`](./groundx/type/search_request_search.py)<a id="search-searchrequestsearchgroundxtypesearch_request_searchpy"></a>


##### id: `int`<a id="id-int"></a>

The ID of the project or bucket to search within.

##### n: `int`<a id="n-int"></a>

Number of results

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`SearchRequest`](./groundx/type/search_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`SearchResponse`](./groundx/type/search_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/search/{id}` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This Python package is automatically generated by [Konfig](https://konfigthis.com)
