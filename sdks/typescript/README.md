<div align="center">

[![Visit EyeLevel's GroundX APIs](./header.png)](https://www.eyelevel.ai)

# [EyeLevel's GroundX APIs](https://www.eyelevel.ai)<a id="eyelevels-groundx-apis"></a>

RAG Made Simple, Secure and Hallucination Free

[![npm](https://img.shields.io/badge/npm-v1.3.32-blue)](https://www.npmjs.com/package/groundx-typescript-sdk/v/1.3.32)
[![More Info](https://img.shields.io/badge/More%20Info-Click%20Here-orange)](https://www.eyelevel.ai/)

</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

- [Installation](#installation)
- [Getting Started](#getting-started)
- [Reference](#reference)
  * [`groundx.buckets.create`](#groundxbucketscreate)
  * [`groundx.buckets.delete`](#groundxbucketsdelete)
  * [`groundx.buckets.get`](#groundxbucketsget)
  * [`groundx.buckets.list`](#groundxbucketslist)
  * [`groundx.buckets.update`](#groundxbucketsupdate)
  * [`groundx.customer.get`](#groundxcustomerget)
  * [`groundx.documents.crawlWebsite`](#groundxdocumentscrawlwebsite)
  * [`groundx.documents.delete`](#groundxdocumentsdelete)
  * [`groundx.documents.delete1`](#groundxdocumentsdelete1)
  * [`groundx.documents.get`](#groundxdocumentsget)
  * [`groundx.documents.getProcessingStatusById`](#groundxdocumentsgetprocessingstatusbyid)
  * [`groundx.documents.ingestLocal`](#groundxdocumentsingestlocal)
  * [`groundx.documents.ingestRemote`](#groundxdocumentsingestremote)
  * [`groundx.documents.list`](#groundxdocumentslist)
  * [`groundx.documents.lookup`](#groundxdocumentslookup)
  * [`groundx.groups.addBucket`](#groundxgroupsaddbucket)
  * [`groundx.groups.create`](#groundxgroupscreate)
  * [`groundx.groups.delete`](#groundxgroupsdelete)
  * [`groundx.groups.get`](#groundxgroupsget)
  * [`groundx.groups.list`](#groundxgroupslist)
  * [`groundx.groups.removeBucket`](#groundxgroupsremovebucket)
  * [`groundx.groups.update`](#groundxgroupsupdate)
  * [`groundx.health.get`](#groundxhealthget)
  * [`groundx.health.list`](#groundxhealthlist)
  * [`groundx.search.content`](#groundxsearchcontent)
  * [`groundx.search.documents`](#groundxsearchdocuments)

<!-- tocstop -->

## Installation<a id="installation"></a>

<table>
<tr>
<th width="292px"><code>npm</code></th>
<th width="293px"><code>pnpm</code></th>
<th width="292px"><code>yarn</code></th>
</tr>
<tr>
<td>

```bash
npm i groundx-typescript-sdk
```

</td>
<td>

```bash
pnpm i groundx-typescript-sdk
```

</td>
<td>

```bash
yarn add groundx-typescript-sdk
```

</td>
</tr>
</table>

## Getting Started<a id="getting-started"></a>

```typescript
import { Groundx } from "groundx-typescript-sdk";

const groundx = new Groundx({
  // Defining the base path is optional and defaults to https://api.groundx.ai/api
  // basePath: "https://api.groundx.ai/api",
  apiKey: "API_KEY",
});

const createResponse = await groundx.buckets.create({
  name: "your_bucket_name",
});

console.log(createResponse);
```

## Reference<a id="reference"></a>


### `groundx.buckets.create`<a id="groundxbucketscreate"></a>

Create a new bucket.

Interact with the "Request Body" below to explore the arguments of this function. Enter your GroundX API key to send a request directly from this web page. Select your language of choice to structure a code snippet based on your specified arguments.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```typescript
const createResponse = await groundx.buckets.create({
  name: "your_bucket_name",
});
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `string`<a id="name-string"></a>

#### 🔄 Return<a id="🔄-return"></a>

[BucketResponse](./models/bucket-response.ts)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/bucket` `POST`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


### `groundx.buckets.delete`<a id="groundxbucketsdelete"></a>

Delete a bucket.

Interact with the "Request Body" below to explore the arguments of this function. Enter your GroundX API key to send a request directly from this web page. Select your language of choice to structure a code snippet based on your specified arguments.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```typescript
const deleteResponse = await groundx.buckets.delete({
  bucketId: 1,
});
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### bucketId: `number`<a id="bucketid-number"></a>

The bucketId of the bucket being deleted.

#### 🔄 Return<a id="🔄-return"></a>

[MessageResponse](./models/message-response.ts)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/bucket/{bucketId}` `DELETE`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


### `groundx.buckets.get`<a id="groundxbucketsget"></a>

Look up a specific bucket by its bucketId.

Interact with the "Request Body" below to explore the arguments of this function. Enter your GroundX API key to send a request directly from this web page. Select your language of choice to structure a code snippet based on your specified arguments.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```typescript
const getResponse = await groundx.buckets.get({
  bucketId: 1,
});
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### bucketId: `number`<a id="bucketid-number"></a>

The bucketId of the bucket to look up.

#### 🔄 Return<a id="🔄-return"></a>

[BucketResponse](./models/bucket-response.ts)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/bucket/{bucketId}` `GET`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


### `groundx.buckets.list`<a id="groundxbucketslist"></a>

List all buckets within your GroundX account

Interact with the "Request Body" below to explore the arguments of this function. Enter your GroundX API key to send a request directly from this web page. Select your language of choice to structure a code snippet based on your specified arguments.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```typescript
const listResponse = await groundx.buckets.list({});
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### n: `number`<a id="n-number"></a>

The maximum number of returned buckets. Accepts 1-100 with a default of 20.

##### nextToken: `string`<a id="nexttoken-string"></a>

A token for pagination. If the number of buckets for a given query is larger than n, the response will include a \"nextToken\" value. That token can be included in this field to retrieve the next batch of n buckets.

#### 🔄 Return<a id="🔄-return"></a>

[BucketListResponse](./models/bucket-list-response.ts)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/bucket` `GET`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


### `groundx.buckets.update`<a id="groundxbucketsupdate"></a>

Rename a bucket.

Interact with the "Request Body" below to explore the arguments of this function. Enter your GroundX API key to send a request directly from this web page. Select your language of choice to structure a code snippet based on your specified arguments.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```typescript
const updateResponse = await groundx.buckets.update({
  bucketId: 1,
  newName: "your_bucket_name",
});
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### newName: `string`<a id="newname-string"></a>

The new name of the bucket being renamed.

##### bucketId: `number`<a id="bucketid-number"></a>

The bucketId of the bucket being updated.

#### 🔄 Return<a id="🔄-return"></a>

[BucketUpdateResponse](./models/bucket-update-response.ts)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/bucket/{bucketId}` `PUT`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


### `groundx.customer.get`<a id="groundxcustomerget"></a>

Get the account information associated with the API key.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```typescript
const getResponse = await groundx.customer.get();
```

#### 🔄 Return<a id="🔄-return"></a>

[CustomerResponse](./models/customer-response.ts)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/customer` `GET`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


### `groundx.documents.crawlWebsite`<a id="groundxdocumentscrawlwebsite"></a>

Upload the content of a publicly accessible website for ingestion into a GroundX bucket. This is done by following links within a specified URL, recursively, up to a specified depth or number of pages.

Interact with the "Request Body" below to explore the arguments of this function. Enter your GroundX API key to send a request directly from this web page. Select your language of choice to structure a code snippet based on your specified arguments.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```typescript
const crawlWebsiteResponse = await groundx.documents.crawlWebsite({
  websites: [
    {
      bucketId: 123,
      cap: 100,
      depth: 3,
      sourceUrl: "https://my.website.com",
    },
  ],
});
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### websites: [`WebsiteCrawlRequestWebsitesInner`](./models/website-crawl-request-websites-inner.ts)[]<a id="websites-websitecrawlrequestwebsitesinnermodelswebsite-crawl-request-websites-innerts"></a>

#### 🔄 Return<a id="🔄-return"></a>

[IngestResponse](./models/ingest-response.ts)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/ingest/documents/website` `POST`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


### `groundx.documents.delete`<a id="groundxdocumentsdelete"></a>

Delete multiple documents hosted on GroundX

Interact with the "Request Body" below to explore the arguments of this function. Enter your GroundX API key to send a request directly from this web page. Select your language of choice to structure a code snippet based on your specified arguments.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```typescript
const deleteResponse = await groundx.documents.delete({
  documentIds: ["documentIds_example"],
});
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### documentIds: `string`[]<a id="documentids-string"></a>

A list of documentIds which correspond to documents ingested by GroundX

#### 🔄 Return<a id="🔄-return"></a>

[IngestResponse](./models/ingest-response.ts)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/ingest/documents` `DELETE`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


### `groundx.documents.delete1`<a id="groundxdocumentsdelete1"></a>

Delete a single document hosted on GroundX

Interact with the "Request Body" below to explore the arguments of this function. Enter your GroundX API key to send a request directly from this web page. Select your language of choice to structure a code snippet based on your specified arguments.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```typescript
const delete1Response = await groundx.documents.delete1({
  documentId: "documentId_example",
});
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### documentId: `string`<a id="documentid-string"></a>

A documentId which correspond to a document ingested by GroundX

#### 🔄 Return<a id="🔄-return"></a>

[IngestResponse](./models/ingest-response.ts)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/ingest/document/{documentId}` `DELETE`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


### `groundx.documents.get`<a id="groundxdocumentsget"></a>

Look up an existing document by documentId.

Interact with the "Request Body" below to explore the arguments of this function. Enter your GroundX API key to send a request directly from this web page. Select your language of choice to structure a code snippet based on your specified arguments.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```typescript
const getResponse = await groundx.documents.get({
  documentId: "documentId_example",
});
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### documentId: `string`<a id="documentid-string"></a>

The documentId of the document for which GroundX information will be provided.

#### 🔄 Return<a id="🔄-return"></a>

[DocumentResponse](./models/document-response.ts)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/ingest/document/{documentId}` `GET`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


### `groundx.documents.getProcessingStatusById`<a id="groundxdocumentsgetprocessingstatusbyid"></a>

Get the current status of an ingest, initiated with documents.ingest_remote, documents.ingest_local, or documents.crawl_website, by specifying the processId (the processId is included in the response of the documents.ingest functions).

Interact with the "Request Body" below to explore the arguments of this function. Enter your GroundX API key to send a request directly from this web page. Select your language of choice to structure a code snippet based on your specified arguments.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```typescript
const getProcessingStatusByIdResponse =
  await groundx.documents.getProcessingStatusById({
    processId: "processId_example",
  });
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### processId: `string`<a id="processid-string"></a>

the processId for the ingest process being checked

#### 🔄 Return<a id="🔄-return"></a>

[ProcessStatusResponse](./models/process-status-response.ts)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/ingest/{processId}` `GET`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


### `groundx.documents.ingestLocal`<a id="groundxdocumentsingestlocal"></a>

Upload documents hosted on a local file system for ingestion into a GroundX bucket.

Interact with the "Request Body" below to explore the arguments of this function. Enter your GroundX API key to send a request directly from this web page. Select your language of choice to structure a code snippet based on your specified arguments.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```typescript
const ingestLocalResponse = await groundx.documents.ingestLocal([
  {
    blob: fs.readFileSync("/path/to/file"),
    metadata: {
      bucketId: 1234,
      fileName: "my_file.txt",
      fileType: "txt",
    },
  },
]);
```

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DocumentLocalIngestRequestInner`](./models/document-local-ingest-request-inner.ts)[]

#### 🔄 Return<a id="🔄-return"></a>

[IngestResponse](./models/ingest-response.ts)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/ingest/documents/local` `POST`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


### `groundx.documents.ingestRemote`<a id="groundxdocumentsingestremote"></a>

Ingest documents hosted on public URLs to a GroundX bucket. 

Interact with the "Request Body" below to explore the arguments of this function. Enter your GroundX API key to send a request directly from this web page. Select your language of choice to structure a code snippet based on your specified arguments.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```typescript
const ingestRemoteResponse = await groundx.documents.ingestRemote({
  documents: [
    {
      bucketId: 1234,
      fileName: "my_file.txt",
      fileType: "txt",
      sourceUrl: "https://my.source.url.com/file.txt",
    },
  ],
});
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### documents: [`DocumentRemoteIngestRequestDocumentsInner`](./models/document-remote-ingest-request-documents-inner.ts)[]<a id="documents-documentremoteingestrequestdocumentsinnermodelsdocument-remote-ingest-request-documents-innerts"></a>

#### 🔄 Return<a id="🔄-return"></a>

[IngestResponse](./models/ingest-response.ts)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/ingest/documents/remote` `POST`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


### `groundx.documents.list`<a id="groundxdocumentslist"></a>

lookup all documents across all resources which are currently on GroundX

Interact with the "Request Body" below to explore the arguments of this function. Enter your GroundX API key to send a request directly from this web page. Select your language of choice to structure a code snippet based on your specified arguments.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```typescript
const listResponse = await groundx.documents.list({
  sort: "name",
  sortOrder: "asc",
  status: "queued",
});
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### n: `number`<a id="n-number"></a>

The maximum number of returned documents. Accepts 1-100 with a default of 20.

##### filter: `string`<a id="filter-string"></a>

Only documents with names that contain the filter string will be returned in the results.

##### sort: [`Sort`](./models/sort.ts)<a id="sort-sortmodelssortts"></a>

The document attribute that will be used to sort the results.

##### sortOrder: [`SortOrder`](./models/sort-order.ts)<a id="sortorder-sortordermodelssort-orderts"></a>

The order in which to sort the results. A value for sort must also be set.

##### status: [`ProcessingStatus`](./models/processing-status.ts)<a id="status-processingstatusmodelsprocessing-statusts"></a>

A status filter on the get documents query. If this value is set, then only documents with this status will be returned in the results.

##### nextToken: `string`<a id="nexttoken-string"></a>

A token for pagination. If the number of documents for a given query is larger than n, the response will include a \"nextToken\" value. That token can be included in this field to retrieve the next batch of n documents.

#### 🔄 Return<a id="🔄-return"></a>

[DocumentListResponse](./models/document-list-response.ts)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/ingest/documents` `GET`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


### `groundx.documents.lookup`<a id="groundxdocumentslookup"></a>

lookup the document(s) associated with a processId, bucketId, groupId, or projectId.

Interact with the "Request Body" below to explore the arguments of this function. Enter your GroundX API key to send a request directly from this web page. Select your language of choice to structure a code snippet based on your specified arguments.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```typescript
const lookupResponse = await groundx.documents.lookup({
  id: 1,
  sort: "name",
  sortOrder: "asc",
  status: "queued",
});
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `number`<a id="id-number"></a>

a processId, bucketId, groupId, or projectId

##### n: `number`<a id="n-number"></a>

The maximum number of returned documents. Accepts 1-100 with a default of 20.

##### filter: `string`<a id="filter-string"></a>

Only documents with names that contain the filter string will be returned in the results.

##### sort: [`Sort`](./models/sort.ts)<a id="sort-sortmodelssortts"></a>

The document attribute that will be used to sort the results.

##### sortOrder: [`SortOrder`](./models/sort-order.ts)<a id="sortorder-sortordermodelssort-orderts"></a>

The order in which to sort the results. A value for sort must also be set.

##### status: [`ProcessingStatus`](./models/processing-status.ts)<a id="status-processingstatusmodelsprocessing-statusts"></a>

A status filter on the get documents query. If this value is set, then only documents with this status will be returned in the results.

##### nextToken: `string`<a id="nexttoken-string"></a>

A token for pagination. If the number of documents for a given query is larger than n, the response will include a \"nextToken\" value. That token can be included in this field to retrieve the next batch of n documents.

#### 🔄 Return<a id="🔄-return"></a>

[DocumentLookupResponse](./models/document-lookup-response.ts)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/ingest/documents/{id}` `GET`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


### `groundx.groups.addBucket`<a id="groundxgroupsaddbucket"></a>

Add an existing bucket to an existing group. Buckets and groups can be associated many to many.

Interact with the "Request Body" below to explore the arguments of this function. Enter your GroundX API key to send a request directly from this web page. Select your language of choice to structure a code snippet based on your specified arguments.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```typescript
const addBucketResponse = await groundx.groups.addBucket({
  groupId: 1,
  bucketId: 1,
});
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### groupId: `number`<a id="groupid-number"></a>

The groupId of the group which the bucket will be added to.

##### bucketId: `number`<a id="bucketid-number"></a>

The bucketId of the bucket being added to the group.

#### 🔄 Return<a id="🔄-return"></a>

[MessageResponse](./models/message-response.ts)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/group/{groupId}/bucket/{bucketId}` `POST`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


### `groundx.groups.create`<a id="groundxgroupscreate"></a>

create a new group, a group being a collection of buckets which can be searched.

Interact with the "Request Body" below to explore the arguments of this function. Enter your GroundX API key to send a request directly from this web page. Select your language of choice to structure a code snippet based on your specified arguments.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```typescript
const createResponse = await groundx.groups.create({
  name: "your_group_name",
  bucketName: "your_new_bucket_name",
});
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `string`<a id="name-string"></a>

The name of the group being created.

##### bucketName: `string`<a id="bucketname-string"></a>

Specify bucketName to automatically create a bucket, by the name specified, and add it to the created group.

#### 🔄 Return<a id="🔄-return"></a>

[GroupResponse](./models/group-response.ts)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/group` `POST`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


### `groundx.groups.delete`<a id="groundxgroupsdelete"></a>

Delete a group.

Interact with the "Request Body" below to explore the arguments of this function. Enter your GroundX API key to send a request directly from this web page. Select your language of choice to structure a code snippet based on your specified arguments.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```typescript
const deleteResponse = await groundx.groups.delete({
  groupId: 1,
});
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### groupId: `number`<a id="groupid-number"></a>

The groupId of the group to be deleted.

#### 🔄 Return<a id="🔄-return"></a>

[MessageResponse](./models/message-response.ts)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/group/{groupId}` `DELETE`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


### `groundx.groups.get`<a id="groundxgroupsget"></a>

look up a specific group by its groupId.

Interact with the "Request Body" below to explore the arguments of this function. Enter your GroundX API key to send a request directly from this web page. Select your language of choice to structure a code snippet based on your specified arguments.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```typescript
const getResponse = await groundx.groups.get({
  groupId: 1,
});
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### groupId: `number`<a id="groupid-number"></a>

The groupId of the group to look up.

#### 🔄 Return<a id="🔄-return"></a>

[GroupResponse](./models/group-response.ts)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/group/{groupId}` `GET`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


### `groundx.groups.list`<a id="groundxgroupslist"></a>

list all groups within your GroundX account.

Interact with the "Request Body" below to explore the arguments of this function. Enter your GroundX API key to send a request directly from this web page. Select your language of choice to structure a code snippet based on your specified arguments.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```typescript
const listResponse = await groundx.groups.list({});
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### n: `number`<a id="n-number"></a>

The maximum number of returned groups. Accepts 1-100 with a default of 20.

##### nextToken: `string`<a id="nexttoken-string"></a>

A token for pagination. If the number of groups for a given query is larger than n, the response will include a \"nextToken\" value. That token can be included in this field to retrieve the next batch of n groups.

#### 🔄 Return<a id="🔄-return"></a>

[GroupListResponse](./models/group-list-response.ts)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/group` `GET`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


### `groundx.groups.removeBucket`<a id="groundxgroupsremovebucket"></a>

remove a bucket from a group. Buckets and groups can be associated many to many, this removes one bucket to group association without disturbing others.

Interact with the "Request Body" below to explore the arguments of this function. Enter your GroundX API key to send a request directly from this web page. Select your language of choice to structure a code snippet based on your specified arguments.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```typescript
const removeBucketResponse = await groundx.groups.removeBucket({
  groupId: 1,
  bucketId: 1,
});
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### groupId: `number`<a id="groupid-number"></a>

The groupId of the group which the bucket will be removed from.

##### bucketId: `number`<a id="bucketid-number"></a>

The bucketId of the bucket which will be removed from the group.

#### 🔄 Return<a id="🔄-return"></a>

[MessageResponse](./models/message-response.ts)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/group/{groupId}/bucket/{bucketId}` `DELETE`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


### `groundx.groups.update`<a id="groundxgroupsupdate"></a>

Rename a group

Interact with the "Request Body" below to explore the arguments of this function. Enter your GroundX API key to send a request directly from this web page. Select your language of choice to structure a code snippet based on your specified arguments.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```typescript
const updateResponse = await groundx.groups.update({
  groupId: 1,
  newName: "your_group_name",
});
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### newName: `string`<a id="newname-string"></a>

The new name of the group being renamed.

##### groupId: `number`<a id="groupid-number"></a>

The groupId of the group to update.

#### 🔄 Return<a id="🔄-return"></a>

[GroupResponse](./models/group-response.ts)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/group/{groupId}` `PUT`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


### `groundx.health.get`<a id="groundxhealthget"></a>

Look up the current health status of a specific service. Statuses update every 5 minutes.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```typescript
const getResponse = await groundx.health.get({
  service: "service_example",
});
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### service: `string`<a id="service-string"></a>

The name of the service to look up.

#### 🔄 Return<a id="🔄-return"></a>

[HealthResponse](./models/health-response.ts)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/health/{service}` `GET`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


### `groundx.health.list`<a id="groundxhealthlist"></a>

List the current health status of all services. Statuses update every 5 minutes.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```typescript
const listResponse = await groundx.health.list();
```

#### 🔄 Return<a id="🔄-return"></a>

[HealthResponse](./models/health-response.ts)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/health` `GET`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


### `groundx.search.content`<a id="groundxsearchcontent"></a>

Search documents on GroundX for the most relevant information to a given query.

The result of this query is typically used in one of two ways; result['search']['text'] can be used to provide context to a language model, facilitating RAG, or result['search']['results'] can be used to observe chunks of text which are relevant to the query, facilitating citation.

Interact with the "Request Body" below to explore the arguments of this function. Enter your GroundX API key to send a request directly from this web page. Select your language of choice to structure a code snippet based on your specified arguments.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```typescript
const contentResponse = await groundx.search.content({
  id: null,
  n: 20,
  nextToken: "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9",
  query: "my search query",
  relevance: 10,
});
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### query: `string`<a id="query-string"></a>

The search query to be used to find relevant documentation.

##### id: [`SearchContentIdParameter`](./models/search-content-id-parameter.ts)<a id="id-searchcontentidparametermodelssearch-content-id-parameterts"></a>

The bucketId, groupId, projectId, or documentId to be searched. The document or documents within the specified container will be compared to the query, and relevant information will be extracted.

##### relevance: `number`<a id="relevance-number"></a>

The minimum search relevance score required to include the result. By default, this is 10.0.

##### n: `number`<a id="n-number"></a>

The maximum number of returned search results. Accepts 1-100 with a default of 20.

##### nextToken: `string`<a id="nexttoken-string"></a>

A token for pagination. If the number of search results for a given query is larger than n, the response will include a \"nextToken\" value. That token can be included in this field to retrieve the next batch of n search results.

##### verbosity: `number`<a id="verbosity-number"></a>

The amount of data returned with each search result. 0 == no search results, only the recommended context. 1 == search results but no searchData. 2 == search results and searchData.

#### 🔄 Return<a id="🔄-return"></a>

[SearchResponse](./models/search-response.ts)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/search/{id}` `POST`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


### `groundx.search.documents`<a id="groundxsearchdocuments"></a>

Search documents on GroundX for the most relevant information to a given query by documentId(s).

The result of this query is typically used in one of two ways; result['search']['text'] can be used to provide context to a language model, facilitating RAG, or result['search']['results'] can be used to observe chunks of text which are relevant to the query, facilitating citation.

Interact with the "Request Body" below to explore the arguments of this function. Enter your GroundX API key to send a request directly from this web page. Select your language of choice to structure a code snippet based on your specified arguments.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```typescript
const documentsResponse = await groundx.search.documents({
  n: 20,
  nextToken: "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9",
  query: "my search query",
  documentIds: ["docUUID1", "docUUID2"],
  relevance: 10,
});
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### query: `string`<a id="query-string"></a>

The search query to be used to find relevant documentation.

##### documentIds: `string`[]<a id="documentids-string"></a>

An array of unique documentIds to be searched.

##### relevance: `number`<a id="relevance-number"></a>

The minimum search relevance score required to include the result. By default, this is 10.0.

##### n: `number`<a id="n-number"></a>

The maximum number of returned search results. Accepts 1-100 with a default of 20.

##### nextToken: `string`<a id="nexttoken-string"></a>

A token for pagination. If the number of search results for a given query is larger than n, the response will include a \"nextToken\" value. That token can be included in this field to retrieve the next batch of n search results.

##### verbosity: `number`<a id="verbosity-number"></a>

The amount of data returned with each search result. 0 == no search results, only the recommended context. 1 == search results but no searchData. 2 == search results and searchData.

#### 🔄 Return<a id="🔄-return"></a>

[SearchResponse](./models/search-response.ts)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/search/documents` `POST`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This TypeScript package is automatically generated by [Konfig](https://konfigthis.com)
