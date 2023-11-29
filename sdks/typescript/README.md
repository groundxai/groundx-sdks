<div align="center">

[![Visit Groundx](./header.png)](https://www.groundx.ai)

# [Groundx](https://www.groundx.ai)<a id="groundx"></a>

Ground Your RAG Apps in Fact not Fiction

[![npm](https://img.shields.io/badge/npm-v1.3.6-blue)](https://www.npmjs.com/package/groundx-typescript-sdk/v/1.3.6)
[![GitHub last commit](https://img.shields.io/github/last-commit/groundxai/groundx-sdks/tree/main/sdks/typescript.svg)](https://github.com/groundxai/groundx-sdks/tree/main/sdks/typescript/commits)
[![More Info](https://img.shields.io/badge/More%20Info-Click%20Here-orange)](https://www.groundx.ai/)

</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

- [Installation](#installation)
- [Getting Started](#getting-started)
- [Reference](#reference)
  * [`groundx.apiKeys.list`](#groundxapikeyslist)
  * [`groundx.buckets.get`](#groundxbucketsget)
  * [`groundx.buckets.list`](#groundxbucketslist)
  * [`groundx.buckets.update`](#groundxbucketsupdate)
  * [`groundx.documents.crawlWebsite`](#groundxdocumentscrawlwebsite)
  * [`groundx.documents.delete`](#groundxdocumentsdelete)
  * [`groundx.documents.delete_0`](#groundxdocumentsdelete_0)
  * [`groundx.documents.get`](#groundxdocumentsget)
  * [`groundx.documents.getProcessingStatusById`](#groundxdocumentsgetprocessingstatusbyid)
  * [`groundx.documents.list`](#groundxdocumentslist)
  * [`groundx.documents.lookup`](#groundxdocumentslookup)
  * [`groundx.documents.uploadLocal`](#groundxdocumentsuploadlocal)
  * [`groundx.documents.uploadRemote`](#groundxdocumentsuploadremote)
  * [`groundx.projects.get`](#groundxprojectsget)
  * [`groundx.projects.list`](#groundxprojectslist)
  * [`groundx.projects.update`](#groundxprojectsupdate)
  * [`groundx.search.content`](#groundxsearchcontent)

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

const listResponse = await groundx.apiKeys.list();

console.log(listResponse);
```

## Reference<a id="reference"></a>


### `groundx.apiKeys.list`<a id="groundxapikeyslist"></a>

Retrieve the API keys for your account.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```typescript
const listResponse = await groundx.apiKeys.list();
```

#### 🔄 Return<a id="🔄-return"></a>

[ApiKeyManagementListResponse](./models/api-key-management-list-response.ts)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/apikey` `GET`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


### `groundx.buckets.get`<a id="groundxbucketsget"></a>

Look up a bucket by its bucketId.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```typescript
const getResponse = await groundx.buckets.get({
  bucketId: 1,
});
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### bucketId: `number`<a id="bucketid-number"></a>

The ID of the bucket to retrieve.

#### 🔄 Return<a id="🔄-return"></a>

[BucketResponse](./models/bucket-response.ts)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/bucket/{bucketId}` `GET`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


### `groundx.buckets.list`<a id="groundxbucketslist"></a>

Look up existing buckets associated with your account.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```typescript
const listResponse = await groundx.buckets.list();
```

#### 🔄 Return<a id="🔄-return"></a>

[BucketListResponse](./models/bucket-list-response.ts)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/bucket` `GET`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


### `groundx.buckets.update`<a id="groundxbucketsupdate"></a>

Update the configurations of an existing bucket.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```typescript
const updateResponse = await groundx.buckets.update({
  bucketId: 1,
  bucket: {
    name: "your_bucket_name",
  },
});
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### bucket: [`BucketUpdateRequestBucket`](./models/bucket-update-request-bucket.ts)<a id="bucket-bucketupdaterequestbucketmodelsbucket-update-request-bucketts"></a>

##### bucketId: `number`<a id="bucketid-number"></a>

The ID of the bucket to update.

#### 🔄 Return<a id="🔄-return"></a>

[BucketUpdateResponse](./models/bucket-update-response.ts)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/bucket/{bucketId}` `PUT`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


### `groundx.documents.crawlWebsite`<a id="groundxdocumentscrawlwebsite"></a>

Crawl and ingest a website into GroundX

#### 🛠️ Usage<a id="🛠️-usage"></a>

```typescript
const crawlWebsiteResponse = await groundx.documents.crawlWebsite({});
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### project: [`WebsiteRequest`](./models/website-request.ts)<a id="project-websiterequestmodelswebsite-requestts"></a>

#### 🔄 Return<a id="🔄-return"></a>

[IngestResponse](./models/ingest-response.ts)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/ingest/documents/website` `POST`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


### `groundx.documents.delete`<a id="groundxdocumentsdelete"></a>

Delete one or more documents from GroundX

#### 🛠️ Usage<a id="🛠️-usage"></a>

```typescript
const deleteResponse = await groundx.documents.delete({
  documents: [
    {
      documentId: "documentId_example",
    },
  ],
});
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### documents: [`DocumentsDeleteRequestDocumentsInner`](./models/documents-delete-request-documents-inner.ts)[]<a id="documents-documentsdeleterequestdocumentsinnermodelsdocuments-delete-request-documents-innerts"></a>

#### 🔄 Return<a id="🔄-return"></a>

[IngestResponse](./models/ingest-response.ts)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/ingest/documents` `DELETE`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


### `groundx.documents.delete_0`<a id="groundxdocumentsdelete_0"></a>

Delete a document

#### 🛠️ Usage<a id="🛠️-usage"></a>

```typescript
const delete_0Response = await groundx.documents.delete_0({
  documentId: "documentId_example",
});
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### documentId: `string`<a id="documentid-string"></a>

#### 🔄 Return<a id="🔄-return"></a>

[IngestResponse](./models/ingest-response.ts)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/ingest/document/{documentId}` `DELETE`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


### `groundx.documents.get`<a id="groundxdocumentsget"></a>

Look up an existing document by its ID

#### 🛠️ Usage<a id="🛠️-usage"></a>

```typescript
const getResponse = await groundx.documents.get({
  documentId: "documentId_example",
});
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### documentId: `string`<a id="documentid-string"></a>

#### 🔄 Return<a id="🔄-return"></a>

[DocumentResponse](./models/document-response.ts)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/ingest/document/{documentId}` `GET`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


### `groundx.documents.getProcessingStatusById`<a id="groundxdocumentsgetprocessingstatusbyid"></a>

Look up the processing status of documents for a given processId

#### 🛠️ Usage<a id="🛠️-usage"></a>

```typescript
const getProcessingStatusByIdResponse =
  await groundx.documents.getProcessingStatusById({
    processId: "processId_example",
  });
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### processId: `string`<a id="processid-string"></a>

#### 🔄 Return<a id="🔄-return"></a>

[ProcessStatusResponse](./models/process-status-response.ts)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/ingest/{processId}` `GET`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


### `groundx.documents.list`<a id="groundxdocumentslist"></a>

Look up all existing documents

#### 🛠️ Usage<a id="🛠️-usage"></a>

```typescript
const listResponse = await groundx.documents.list({});
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### n: `number`<a id="n-number"></a>

##### nextToken: `string`<a id="nexttoken-string"></a>

#### 🔄 Return<a id="🔄-return"></a>

[DocumentListResponse](./models/document-list-response.ts)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/ingest/documents` `GET`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


### `groundx.documents.lookup`<a id="groundxdocumentslookup"></a>

Look up existing documents by processId, bucketId, or projectId

#### 🛠️ Usage<a id="🛠️-usage"></a>

```typescript
const lookupResponse = await groundx.documents.lookup({
  id: 1,
});
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `number`<a id="id-number"></a>

##### n: `number`<a id="n-number"></a>

##### nextToken: `string`<a id="nexttoken-string"></a>

#### 🔄 Return<a id="🔄-return"></a>

[DocumentLookupResponse](./models/document-lookup-response.ts)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/ingest/documents/{id}` `GET`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


### `groundx.documents.uploadLocal`<a id="groundxdocumentsuploadlocal"></a>

Upload local documents to GroundX

#### 🛠️ Usage<a id="🛠️-usage"></a>

```typescript
const uploadLocalResponse = await groundx.documents.uploadLocal([
  {
    blob: fs.readFileSync("/path/to/file"),
    metadata: {
      bucketId: 1234,
      callbackData: "my_callback_data",
      callbackUrl: "https://my.callback.url.com",
      fileName: "my_file.txt",
      fileType: "txt",
    },
  },
]);
```

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DocumentLocalUploadRequestInner`](./models/document-local-upload-request-inner.ts)[]

#### 🔄 Return<a id="🔄-return"></a>

[IngestResponse](./models/ingest-response.ts)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/ingest/documents/local` `POST`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


### `groundx.documents.uploadRemote`<a id="groundxdocumentsuploadremote"></a>

Upload hosted documents to GroundX

#### 🛠️ Usage<a id="🛠️-usage"></a>

```typescript
const uploadRemoteResponse = await groundx.documents.uploadRemote({
  documents: [
    {
      bucketId: 1234,
      callbackData: "my_callback_data",
      callbackUrl: "https://my.callback.url.com",
      fileName: "my_file.txt",
      fileType: "txt",
      sourceUrl: "https://my.source.url.com/file.txt",
    },
  ],
});
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### documents: [`DocumentRemoteUploadRequestDocumentsInner`](./models/document-remote-upload-request-documents-inner.ts)[]<a id="documents-documentremoteuploadrequestdocumentsinnermodelsdocument-remote-upload-request-documents-innerts"></a>

#### 🔄 Return<a id="🔄-return"></a>

[IngestResponse](./models/ingest-response.ts)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/ingest/documents/remote` `POST`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


### `groundx.projects.get`<a id="groundxprojectsget"></a>

This endpoint allows you to retrieve a specific project by projectId.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```typescript
const getResponse = await groundx.projects.get({
  projectId: "projectId_example",
});
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### projectId: `string`<a id="projectid-string"></a>

The ID of the project to retrieve.

#### 🔄 Return<a id="🔄-return"></a>

[ProjectResponse](./models/project-response.ts)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/project/{projectId}` `GET`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


### `groundx.projects.list`<a id="groundxprojectslist"></a>

This endpoint allows you to retrieve your existing projects.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```typescript
const listResponse = await groundx.projects.list();
```

#### 🔄 Return<a id="🔄-return"></a>

[ProjectListResponse](./models/project-list-response.ts)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/project` `GET`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


### `groundx.projects.update`<a id="groundxprojectsupdate"></a>

This endpoint allows you to update an existing project.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```typescript
const updateResponse = await groundx.projects.update({
  projectId: "projectId_example",
  project: {
    name: "your_project_name",
  },
});
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### project: [`ProjectUpdateRequestProject`](./models/project-update-request-project.ts)<a id="project-projectupdaterequestprojectmodelsproject-update-request-projectts"></a>

##### projectId: `string`<a id="projectid-string"></a>

The ID of the project to update.

#### 🔄 Return<a id="🔄-return"></a>

[ProjectResponse](./models/project-response.ts)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/project/{projectId}` `PUT`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


### `groundx.search.content`<a id="groundxsearchcontent"></a>

Search and retrieve relevant content from a project or bucket by id.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```typescript
const contentResponse = await groundx.search.content({
  id: 1,
  n: 20,
  search: {
    query: "my search query",
    nextToken: "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9",
  },
});
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### search: [`SearchRequestSearch`](./models/search-request-search.ts)<a id="search-searchrequestsearchmodelssearch-request-searchts"></a>

##### id: `number`<a id="id-number"></a>

The ID of the project or bucket to search within.

##### n: `number`<a id="n-number"></a>

Number of results

#### 🔄 Return<a id="🔄-return"></a>

[SearchResponse](./models/search-response.ts)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/search/{id}` `POST`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This TypeScript package is automatically generated by [Konfig](https://konfigthis.com)
