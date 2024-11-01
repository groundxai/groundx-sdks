<div align="center">

[![Visit EyeLevel's GroundX APIs](https://raw.githubusercontent.com/groundxai/groundx-sdks/HEAD/sdks/python/header.png)](https://www.eyelevel.ai)

# EyeLevel's GroundX APIs<a id="eyelevels-groundx-apis"></a>

RAG Made Simple, Secure and Hallucination Free


[![PyPI](https://img.shields.io/badge/PyPI-v1.3.29-blue)](https://pypi.org/project/groundx-python-sdk/1.3.29)
[![README.md](https://img.shields.io/badge/README-Click%20Here-green)](https://github.com/groundxai/groundx-sdks/tree/main/sdks/python#readme)
[![More Info](https://img.shields.io/badge/More%20Info-Click%20Here-orange)](https://www.eyelevel.ai/)

</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

- [Requirements](#requirements)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Async](#async)
- [Reference](#reference)
  * [`groundx.buckets.create`](#groundxbucketscreate)
  * [`groundx.buckets.delete`](#groundxbucketsdelete)
  * [`groundx.buckets.get`](#groundxbucketsget)
  * [`groundx.buckets.list`](#groundxbucketslist)
  * [`groundx.buckets.update`](#groundxbucketsupdate)
  * [`groundx.customer.get`](#groundxcustomerget)
  * [`groundx.documents.crawl_website`](#groundxdocumentscrawl_website)
  * [`groundx.documents.delete`](#groundxdocumentsdelete)
  * [`groundx.documents.delete1`](#groundxdocumentsdelete1)
  * [`groundx.documents.get`](#groundxdocumentsget)
  * [`groundx.documents.get_processing_status_by_id`](#groundxdocumentsget_processing_status_by_id)
  * [`groundx.documents.ingest_local`](#groundxdocumentsingest_local)
  * [`groundx.documents.ingest_remote`](#groundxdocumentsingest_remote)
  * [`groundx.documents.list`](#groundxdocumentslist)
  * [`groundx.documents.lookup`](#groundxdocumentslookup)
  * [`groundx.groups.add_bucket`](#groundxgroupsadd_bucket)
  * [`groundx.groups.create`](#groundxgroupscreate)
  * [`groundx.groups.delete`](#groundxgroupsdelete)
  * [`groundx.groups.get`](#groundxgroupsget)
  * [`groundx.groups.list`](#groundxgroupslist)
  * [`groundx.groups.remove_bucket`](#groundxgroupsremove_bucket)
  * [`groundx.groups.update`](#groundxgroupsupdate)
  * [`groundx.health.get`](#groundxhealthget)
  * [`groundx.health.list`](#groundxhealthlist)
  * [`groundx.search.content`](#groundxsearchcontent)
  * [`groundx.search.documents`](#groundxsearchdocuments)

<!-- tocstop -->

## Requirements<a id="requirements"></a>

Python >=3.7

## Installation<a id="installation"></a>

```sh
pip install groundx-python-sdk==1.3.29
```

## Getting Started<a id="getting-started"></a>

```python
from pprint import pprint
from groundx import Groundx, ApiException

groundx = Groundx(
    api_key="YOUR_API_KEY",
)

try:
    # create
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
        # create
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

Create a new bucket.

Interact with the "Request Body" below to explore the arguments of this function. Enter your GroundX API key to send a request directly from this web page. Select your language of choice to structure a code snippet based on your specified arguments.


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

Delete a bucket.

Interact with the "Request Body" below to explore the arguments of this function. Enter your GroundX API key to send a request directly from this web page. Select your language of choice to structure a code snippet based on your specified arguments.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_response = groundx.buckets.delete(
    bucket_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### bucket_id: `int`<a id="bucket_id-int"></a>

The bucketId of the bucket being deleted.

#### 🔄 Return<a id="🔄-return"></a>

[`MessageResponse`](./groundx/type/message_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/bucket/{bucketId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `groundx.buckets.get`<a id="groundxbucketsget"></a>

Look up a specific bucket by its bucketId.

Interact with the "Request Body" below to explore the arguments of this function. Enter your GroundX API key to send a request directly from this web page. Select your language of choice to structure a code snippet based on your specified arguments.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_response = groundx.buckets.get(
    bucket_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### bucket_id: `int`<a id="bucket_id-int"></a>

The bucketId of the bucket to look up.

#### 🔄 Return<a id="🔄-return"></a>

[`BucketResponse`](./groundx/type/bucket_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/bucket/{bucketId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `groundx.buckets.list`<a id="groundxbucketslist"></a>

List all buckets within your GroundX account

Interact with the "Request Body" below to explore the arguments of this function. Enter your GroundX API key to send a request directly from this web page. Select your language of choice to structure a code snippet based on your specified arguments.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_response = groundx.buckets.list(
    n=1,
    next_token="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### n: `int`<a id="n-int"></a>

The maximum number of returned buckets. Accepts 1-100 with a default of 20.

##### next_token: `str`<a id="next_token-str"></a>

A token for pagination. If the number of buckets for a given query is larger than n, the response will include a \"nextToken\" value. That token can be included in this field to retrieve the next batch of n buckets.

#### 🔄 Return<a id="🔄-return"></a>

[`BucketListResponse`](./groundx/type/bucket_list_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/bucket` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `groundx.buckets.update`<a id="groundxbucketsupdate"></a>

Rename a bucket.

Interact with the "Request Body" below to explore the arguments of this function. Enter your GroundX API key to send a request directly from this web page. Select your language of choice to structure a code snippet based on your specified arguments.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_response = groundx.buckets.update(
    new_name="your_bucket_name",
    bucket_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### new_name: `str`<a id="new_name-str"></a>

The new name of the bucket being renamed.

##### bucket_id: `int`<a id="bucket_id-int"></a>

The bucketId of the bucket being updated.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`BucketUpdateRequest`](./groundx/type/bucket_update_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`BucketUpdateResponse`](./groundx/type/bucket_update_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/bucket/{bucketId}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `groundx.customer.get`<a id="groundxcustomerget"></a>

Get the account information associated with the API key.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_response = groundx.customer.get()
```

#### 🔄 Return<a id="🔄-return"></a>

[`CustomerResponse`](./groundx/type/customer_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/customer` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `groundx.documents.crawl_website`<a id="groundxdocumentscrawl_website"></a>

Upload the content of a publicly accessible website for ingestion into a GroundX bucket. This is done by following links within a specified URL, recursively, up to a specified depth or number of pages.

Interact with the "Request Body" below to explore the arguments of this function. Enter your GroundX API key to send a request directly from this web page. Select your language of choice to structure a code snippet based on your specified arguments.


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

Delete multiple documents hosted on GroundX

Interact with the "Request Body" below to explore the arguments of this function. Enter your GroundX API key to send a request directly from this web page. Select your language of choice to structure a code snippet based on your specified arguments.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_response = groundx.documents.delete(
    document_ids=["documentIds_example"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### document_ids: List[`str`]<a id="document_ids-liststr"></a>

A list of documentIds which correspond to documents ingested by GroundX

#### 🔄 Return<a id="🔄-return"></a>

[`IngestResponse`](./groundx/type/ingest_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/ingest/documents` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `groundx.documents.delete1`<a id="groundxdocumentsdelete1"></a>

Delete a single document hosted on GroundX

Interact with the "Request Body" below to explore the arguments of this function. Enter your GroundX API key to send a request directly from this web page. Select your language of choice to structure a code snippet based on your specified arguments.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete1_response = groundx.documents.delete1(
    document_id="documentId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### document_id: `str`<a id="document_id-str"></a>

A documentId which correspond to a document ingested by GroundX

#### 🔄 Return<a id="🔄-return"></a>

[`IngestResponse`](./groundx/type/ingest_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/ingest/document/{documentId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `groundx.documents.get`<a id="groundxdocumentsget"></a>

Look up an existing document by documentId.

Interact with the "Request Body" below to explore the arguments of this function. Enter your GroundX API key to send a request directly from this web page. Select your language of choice to structure a code snippet based on your specified arguments.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_response = groundx.documents.get(
    document_id="documentId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### document_id: `str`<a id="document_id-str"></a>

The documentId of the document for which GroundX information will be provided.

#### 🔄 Return<a id="🔄-return"></a>

[`DocumentResponse`](./groundx/type/document_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/ingest/document/{documentId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `groundx.documents.get_processing_status_by_id`<a id="groundxdocumentsget_processing_status_by_id"></a>

Get the current status of an ingest, initiated with documents.ingest_remote, documents.ingest_local, or documents.crawl_website, by specifying the processId (the processId is included in the response of the documents.ingest functions).

Interact with the "Request Body" below to explore the arguments of this function. Enter your GroundX API key to send a request directly from this web page. Select your language of choice to structure a code snippet based on your specified arguments.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_processing_status_by_id_response = groundx.documents.get_processing_status_by_id(
    process_id="processId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### process_id: `str`<a id="process_id-str"></a>

the processId for the ingest process being checked

#### 🔄 Return<a id="🔄-return"></a>

[`ProcessStatusResponse`](./groundx/type/process_status_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/ingest/{processId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `groundx.documents.ingest_local`<a id="groundxdocumentsingest_local"></a>

Upload documents hosted on a local file system for ingestion into a GroundX bucket.

Interact with the "Request Body" below to explore the arguments of this function. Enter your GroundX API key to send a request directly from this web page. Select your language of choice to structure a code snippet based on your specified arguments.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
ingest_local_response = groundx.documents.ingest_local(
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

[`DocumentLocalIngestRequest`](./groundx/type/document_local_ingest_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`IngestResponse`](./groundx/type/ingest_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/ingest/documents/local` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `groundx.documents.ingest_remote`<a id="groundxdocumentsingest_remote"></a>

Ingest documents hosted on public URLs to a GroundX bucket. 

Interact with the "Request Body" below to explore the arguments of this function. Enter your GroundX API key to send a request directly from this web page. Select your language of choice to structure a code snippet based on your specified arguments.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
ingest_remote_response = groundx.documents.ingest_remote(
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

##### documents: [`DocumentRemoteIngestRequestDocuments`](./groundx/type/document_remote_ingest_request_documents.py)<a id="documents-documentremoteingestrequestdocumentsgroundxtypedocument_remote_ingest_request_documentspy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DocumentRemoteIngestRequest`](./groundx/type/document_remote_ingest_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`IngestResponse`](./groundx/type/ingest_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/ingest/documents/remote` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `groundx.documents.list`<a id="groundxdocumentslist"></a>

lookup all documents across all resources which are currently on GroundX

Interact with the "Request Body" below to explore the arguments of this function. Enter your GroundX API key to send a request directly from this web page. Select your language of choice to structure a code snippet based on your specified arguments.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_response = groundx.documents.list(
    n=1,
    filter="string_example",
    sort="name",
    sort_order="asc",
    status="queued",
    next_token="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### n: `int`<a id="n-int"></a>

The maximum number of returned documents. Accepts 1-100 with a default of 20.

##### filter: `str`<a id="filter-str"></a>

Only documents with names that contain the filter string will be returned in the results.

##### sort: [`Sort`](./groundx/type/.py)<a id="sort-sortgroundxtypepy"></a>

The document attribute that will be used to sort the results.

##### sort_order: [`SortOrder`](./groundx/type/.py)<a id="sort_order-sortordergroundxtypepy"></a>

The order in which to sort the results. A value for sort must also be set.

##### status: [`ProcessingStatus`](./groundx/type/.py)<a id="status-processingstatusgroundxtypepy"></a>

A status filter on the get documents query. If this value is set, then only documents with this status will be returned in the results.

##### next_token: `str`<a id="next_token-str"></a>

A token for pagination. If the number of documents for a given query is larger than n, the response will include a \"nextToken\" value. That token can be included in this field to retrieve the next batch of n documents.

#### 🔄 Return<a id="🔄-return"></a>

[`DocumentListResponse`](./groundx/type/document_list_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/ingest/documents` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `groundx.documents.lookup`<a id="groundxdocumentslookup"></a>

lookup the document(s) associated with a processId, bucketId, groupId, or projectId.

Interact with the "Request Body" below to explore the arguments of this function. Enter your GroundX API key to send a request directly from this web page. Select your language of choice to structure a code snippet based on your specified arguments.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
lookup_response = groundx.documents.lookup(
    id=1,
    n=1,
    filter="string_example",
    sort="name",
    sort_order="asc",
    status="queued",
    next_token="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

a processId, bucketId, groupId, or projectId

##### n: `int`<a id="n-int"></a>

The maximum number of returned documents. Accepts 1-100 with a default of 20.

##### filter: `str`<a id="filter-str"></a>

Only documents with names that contain the filter string will be returned in the results.

##### sort: [`Sort`](./groundx/type/.py)<a id="sort-sortgroundxtypepy"></a>

The document attribute that will be used to sort the results.

##### sort_order: [`SortOrder`](./groundx/type/.py)<a id="sort_order-sortordergroundxtypepy"></a>

The order in which to sort the results. A value for sort must also be set.

##### status: [`ProcessingStatus`](./groundx/type/.py)<a id="status-processingstatusgroundxtypepy"></a>

A status filter on the get documents query. If this value is set, then only documents with this status will be returned in the results.

##### next_token: `str`<a id="next_token-str"></a>

A token for pagination. If the number of documents for a given query is larger than n, the response will include a \"nextToken\" value. That token can be included in this field to retrieve the next batch of n documents.

#### 🔄 Return<a id="🔄-return"></a>

[`DocumentLookupResponse`](./groundx/type/document_lookup_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/ingest/documents/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `groundx.groups.add_bucket`<a id="groundxgroupsadd_bucket"></a>

Add an existing bucket to an existing group. Buckets and groups can be associated many to many.

Interact with the "Request Body" below to explore the arguments of this function. Enter your GroundX API key to send a request directly from this web page. Select your language of choice to structure a code snippet based on your specified arguments.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_bucket_response = groundx.groups.add_bucket(
    group_id=1,
    bucket_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### group_id: `int`<a id="group_id-int"></a>

The groupId of the group which the bucket will be added to.

##### bucket_id: `int`<a id="bucket_id-int"></a>

The bucketId of the bucket being added to the group.

#### 🔄 Return<a id="🔄-return"></a>

[`MessageResponse`](./groundx/type/message_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/group/{groupId}/bucket/{bucketId}` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `groundx.groups.create`<a id="groundxgroupscreate"></a>

create a new group, a group being a collection of buckets which can be searched.

Interact with the "Request Body" below to explore the arguments of this function. Enter your GroundX API key to send a request directly from this web page. Select your language of choice to structure a code snippet based on your specified arguments.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_response = groundx.groups.create(
    name="your_group_name",
    bucket_name="your_new_bucket_name",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

The name of the group being created.

##### bucket_name: `str`<a id="bucket_name-str"></a>

Specify bucketName to automatically create a bucket, by the name specified, and add it to the created group.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`GroupCreateRequest`](./groundx/type/group_create_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`GroupResponse`](./groundx/type/group_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/group` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `groundx.groups.delete`<a id="groundxgroupsdelete"></a>

Delete a group.

Interact with the "Request Body" below to explore the arguments of this function. Enter your GroundX API key to send a request directly from this web page. Select your language of choice to structure a code snippet based on your specified arguments.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_response = groundx.groups.delete(
    group_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### group_id: `int`<a id="group_id-int"></a>

The groupId of the group to be deleted.

#### 🔄 Return<a id="🔄-return"></a>

[`MessageResponse`](./groundx/type/message_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/group/{groupId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `groundx.groups.get`<a id="groundxgroupsget"></a>

look up a specific group by its groupId.

Interact with the "Request Body" below to explore the arguments of this function. Enter your GroundX API key to send a request directly from this web page. Select your language of choice to structure a code snippet based on your specified arguments.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_response = groundx.groups.get(
    group_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### group_id: `int`<a id="group_id-int"></a>

The groupId of the group to look up.

#### 🔄 Return<a id="🔄-return"></a>

[`GroupResponse`](./groundx/type/group_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/group/{groupId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `groundx.groups.list`<a id="groundxgroupslist"></a>

list all groups within your GroundX account.

Interact with the "Request Body" below to explore the arguments of this function. Enter your GroundX API key to send a request directly from this web page. Select your language of choice to structure a code snippet based on your specified arguments.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_response = groundx.groups.list(
    n=1,
    next_token="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### n: `int`<a id="n-int"></a>

The maximum number of returned groups. Accepts 1-100 with a default of 20.

##### next_token: `str`<a id="next_token-str"></a>

A token for pagination. If the number of groups for a given query is larger than n, the response will include a \"nextToken\" value. That token can be included in this field to retrieve the next batch of n groups.

#### 🔄 Return<a id="🔄-return"></a>

[`GroupListResponse`](./groundx/type/group_list_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/group` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `groundx.groups.remove_bucket`<a id="groundxgroupsremove_bucket"></a>

remove a bucket from a group. Buckets and groups can be associated many to many, this removes one bucket to group association without disturbing others.

Interact with the "Request Body" below to explore the arguments of this function. Enter your GroundX API key to send a request directly from this web page. Select your language of choice to structure a code snippet based on your specified arguments.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
remove_bucket_response = groundx.groups.remove_bucket(
    group_id=1,
    bucket_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### group_id: `int`<a id="group_id-int"></a>

The groupId of the group which the bucket will be removed from.

##### bucket_id: `int`<a id="bucket_id-int"></a>

The bucketId of the bucket which will be removed from the group.

#### 🔄 Return<a id="🔄-return"></a>

[`MessageResponse`](./groundx/type/message_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/group/{groupId}/bucket/{bucketId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `groundx.groups.update`<a id="groundxgroupsupdate"></a>

Rename a group

Interact with the "Request Body" below to explore the arguments of this function. Enter your GroundX API key to send a request directly from this web page. Select your language of choice to structure a code snippet based on your specified arguments.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_response = groundx.groups.update(
    new_name="your_group_name",
    group_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### new_name: `str`<a id="new_name-str"></a>

The new name of the group being renamed.

##### group_id: `int`<a id="group_id-int"></a>

The groupId of the group to update.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`GroupUpdateRequest`](./groundx/type/group_update_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`GroupResponse`](./groundx/type/group_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/group/{groupId}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `groundx.health.get`<a id="groundxhealthget"></a>

Look up the current health status of a specific service. Statuses update every 5 minutes.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_response = groundx.health.get(
    service="search",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### service: `str`<a id="service-str"></a>

The name of the service to look up.

#### 🔄 Return<a id="🔄-return"></a>

[`HealthResponse`](./groundx/type/health_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/health/{service}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `groundx.health.list`<a id="groundxhealthlist"></a>

List the current health status of all services. Statuses update every 5 minutes.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_response = groundx.health.list()
```

#### 🔄 Return<a id="🔄-return"></a>

[`HealthResponse`](./groundx/type/health_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/health` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `groundx.search.content`<a id="groundxsearchcontent"></a>

Search documents on GroundX for the most relevant information to a given query.

The result of this query is typically used in one of two ways; result['search']['text'] can be used to provide context to a language model, facilitating RAG, or result['search']['results'] can be used to observe chunks of text which are relevant to the query, facilitating citation.

Interact with the "Request Body" below to explore the arguments of this function. Enter your GroundX API key to send a request directly from this web page. Select your language of choice to structure a code snippet based on your specified arguments.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
content_response = groundx.search.content(
    query="my search query",
    id=None,
    relevance=10,
    n=20,
    next_token="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9",
    verbosity=0,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### query: `str`<a id="query-str"></a>

The search query to be used to find relevant documentation.

##### id: Union[`int`, `str`]<a id="id-unionint-str"></a>


The bucketId, groupId, projectId, or documentId to be searched. The document or documents within the specified container will be compared to the query, and relevant information will be extracted.

##### relevance: `Union[int, float]`<a id="relevance-unionint-float"></a>

The minimum search relevance score required to include the result. By default, this is 10.0.

##### n: `int`<a id="n-int"></a>

The maximum number of returned search results. Accepts 1-100 with a default of 20.

##### next_token: `str`<a id="next_token-str"></a>

A token for pagination. If the number of search results for a given query is larger than n, the response will include a \"nextToken\" value. That token can be included in this field to retrieve the next batch of n search results.

##### verbosity: `int`<a id="verbosity-int"></a>

The amount of data returned with each search result. 0 == no search results, only the recommended context. 1 == search results but no searchData. 2 == search results and searchData.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`SearchRequest`](./groundx/type/search_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`SearchResponse`](./groundx/type/search_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/search/{id}` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `groundx.search.documents`<a id="groundxsearchdocuments"></a>

Search documents on GroundX for the most relevant information to a given query by documentId(s).

The result of this query is typically used in one of two ways; result['search']['text'] can be used to provide context to a language model, facilitating RAG, or result['search']['results'] can be used to observe chunks of text which are relevant to the query, facilitating citation.

Interact with the "Request Body" below to explore the arguments of this function. Enter your GroundX API key to send a request directly from this web page. Select your language of choice to structure a code snippet based on your specified arguments.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
documents_response = groundx.search.documents(
    query="my search query",
    document_ids=["docUUID1", "docUUID2"],
    relevance=10,
    n=20,
    next_token="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9",
    verbosity=0,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### query: `str`<a id="query-str"></a>

The search query to be used to find relevant documentation.

##### document_ids: [`SearchDocumentsRequestDocumentIds`](./groundx/type/search_documents_request_document_ids.py)<a id="document_ids-searchdocumentsrequestdocumentidsgroundxtypesearch_documents_request_document_idspy"></a>

##### relevance: `Union[int, float]`<a id="relevance-unionint-float"></a>

The minimum search relevance score required to include the result. By default, this is 10.0.

##### n: `int`<a id="n-int"></a>

The maximum number of returned search results. Accepts 1-100 with a default of 20.

##### next_token: `str`<a id="next_token-str"></a>

A token for pagination. If the number of search results for a given query is larger than n, the response will include a \"nextToken\" value. That token can be included in this field to retrieve the next batch of n search results.

##### verbosity: `int`<a id="verbosity-int"></a>

The amount of data returned with each search result. 0 == no search results, only the recommended context. 1 == search results but no searchData. 2 == search results and searchData.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`SearchDocumentsRequest`](./groundx/type/search_documents_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`SearchResponse`](./groundx/type/search_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/search/documents` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This Python package is automatically generated by [Konfig](https://konfigthis.com)
