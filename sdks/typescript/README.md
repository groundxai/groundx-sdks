# groundx-typescript-sdk

Ground Your RAG Apps in Fact not Fiction

[![npm](https://img.shields.io/badge/npm-v1.2.0-blue)](https://www.npmjs.com/package/groundx-typescript-sdk/v/1.2.0)

## Table of Contents

<!-- toc -->

- [Installing](#installing)
  * [npm](#npm)
  * [yarn](#yarn)
- [Getting Started](#getting-started)
- [Reference](#reference)
  * [`groundx.apiKeys.list`](#groundxapikeyslist)
  * [`groundx.buckets.get`](#groundxbucketsget)
  * [`groundx.buckets.list`](#groundxbucketslist)
  * [`groundx.buckets.update`](#groundxbucketsupdate)
  * [`groundx.documents.delete`](#groundxdocumentsdelete)
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

## Installing

### npm
```
npm install groundx-typescript-sdk --save
```

### yarn
```
yarn add groundx-typescript-sdk
```

## Getting Started

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

## Reference


### `groundx.apiKeys.list`

Retrieve the API keys for your account.

#### 🛠️ Usage

```typescript
const listResponse = await groundx.apiKeys.list();
```

#### 🔄 Return
[ApiKeyManagementListResponse](./models/api-key-management-list-response.ts)

#### 🌐 Endpoint

`/v1/apikey` `GET`

[🔙 Back to Table of Contents](#table-of-contents)

---


### `groundx.buckets.get`

Look up a bucket by its bucketId.

#### 🛠️ Usage

```typescript
const getResponse = await groundx.buckets.get({
  bucketId: 1,
});
```

#### ⚙️ Parameters

##### bucketId: `number`

The ID of the bucket to retrieve.

#### 🔄 Return
[BucketResponse](./models/bucket-response.ts)

#### 🌐 Endpoint

`/v1/bucket/{bucketId}` `GET`

[🔙 Back to Table of Contents](#table-of-contents)

---


### `groundx.buckets.list`

Look up existing buckets associated with your account.

#### 🛠️ Usage

```typescript
const listResponse = await groundx.buckets.list();
```

#### 🔄 Return
[BucketListResponse](./models/bucket-list-response.ts)

#### 🌐 Endpoint

`/v1/bucket` `GET`

[🔙 Back to Table of Contents](#table-of-contents)

---


### `groundx.buckets.update`

Update the configurations of an existing bucket.

#### 🛠️ Usage

```typescript
const updateResponse = await groundx.buckets.update({
  bucketId: 1,
  bucket: {
    name: "your_bucket_name",
  },
});
```

#### ⚙️ Parameters

##### bucket: [`BucketUpdateRequestBucket`](./models/bucket-update-request-bucket.ts)

##### bucketId: `number`

The ID of the bucket to update.

#### 🔄 Return
[BucketResponse](./models/bucket-response.ts)

#### 🌐 Endpoint

`/v1/bucket/{bucketId}` `PUT`

[🔙 Back to Table of Contents](#table-of-contents)

---


### `groundx.documents.delete`

Delete a document

#### 🛠️ Usage

```typescript
const deleteResponse = await groundx.documents.delete({
  documentId: "documentId_example",
});
```

#### ⚙️ Parameters

##### documentId: `string`

#### 🔄 Return
[DocumentDeleteResponse](./models/document-delete-response.ts)

#### 🌐 Endpoint

`/v1/ingest/document/{documentId}` `DELETE`

[🔙 Back to Table of Contents](#table-of-contents)

---


### `groundx.documents.get`

Look up an existing document by its ID

#### 🛠️ Usage

```typescript
const getResponse = await groundx.documents.get({
  documentId: "documentId_example",
});
```

#### ⚙️ Parameters

##### documentId: `string`

#### 🔄 Return
[DocumentResponse](./models/document-response.ts)

#### 🌐 Endpoint

`/v1/ingest/document/{documentId}` `GET`

[🔙 Back to Table of Contents](#table-of-contents)

---


### `groundx.documents.getProcessingStatusById`

Look up the processing status of documents for a given processId

#### 🛠️ Usage

```typescript
const getProcessingStatusByIdResponse =
  await groundx.documents.getProcessingStatusById({
    processId: "processId_example",
  });
```

#### ⚙️ Parameters

##### processId: `string`

#### 🔄 Return
[ProcessStatusResponse](./models/process-status-response.ts)

#### 🌐 Endpoint

`/v1/ingest/{processId}` `GET`

[🔙 Back to Table of Contents](#table-of-contents)

---


### `groundx.documents.list`

Look up all existing documents

#### 🛠️ Usage

```typescript
const listResponse = await groundx.documents.list();
```

#### 🔄 Return
[DocumentListResponse](./models/document-list-response.ts)

#### 🌐 Endpoint

`/v1/ingest/documents` `GET`

[🔙 Back to Table of Contents](#table-of-contents)

---


### `groundx.documents.lookup`

Look up existing documents by processId, bucketId, or projectId

#### 🛠️ Usage

```typescript
const lookupResponse = await groundx.documents.lookup({
  id: 1,
});
```

#### ⚙️ Parameters

##### id: `number`

#### 🔄 Return
[DocumentLookupResponse](./models/document-lookup-response.ts)

#### 🌐 Endpoint

`/v1/ingest/documents/{id}` `GET`

[🔙 Back to Table of Contents](#table-of-contents)

---


### `groundx.documents.uploadLocal`

Upload local documents to GroundX

#### 🛠️ Usage

```typescript
const uploadLocalResponse = await groundx.documents.uploadLocal([
  {
    blob: open("/path/to/file", "rb"),
    metadata: {
      bucketId: 1234,
      fileName: "my_file.txt",
      fileType: "txt",
      callbackData: "my_callback_data",
      callbackUrl: "https://my.callback.url.com",
    },
  },
]);
```

#### ⚙️ Parameter

[`DocumentLocalUploadRequestInner`](./models/document-local-upload-request-inner.ts)[]

#### 🔄 Return
[IngestResponse](./models/ingest-response.ts)

#### 🌐 Endpoint

`/v1/ingest/documents/local` `POST`

[🔙 Back to Table of Contents](#table-of-contents)

---


### `groundx.documents.uploadRemote`

Upload hosted documents to GroundX

#### 🛠️ Usage

```typescript
const uploadRemoteResponse = await groundx.documents.uploadRemote({
  documents: [
    {
      bucketId: 1234,
      sourceUrl: "https://my.source.url.com/file.txt",
      callbackData: "my_callback_data",
      callbackUrl: "https://my.callback.url.com",
      type: "txt",
    },
  ],
});
```

#### ⚙️ Parameters

##### documents: [`DocumentRemoteUploadRequestDocumentsInner`](./models/document-remote-upload-request-documents-inner.ts)[]

#### 🔄 Return
[IngestResponse](./models/ingest-response.ts)

#### 🌐 Endpoint

`/v1/ingest/documents/remote` `POST`

[🔙 Back to Table of Contents](#table-of-contents)

---


### `groundx.projects.get`

This endpoint allows you to retrieve a specific project by projectId.

#### 🛠️ Usage

```typescript
const getResponse = await groundx.projects.get({
  projectId: "projectId_example",
});
```

#### ⚙️ Parameters

##### projectId: `string`

The ID of the project to retrieve.

#### 🔄 Return
[ProjectResponse](./models/project-response.ts)

#### 🌐 Endpoint

`/v1/project/{projectId}` `GET`

[🔙 Back to Table of Contents](#table-of-contents)

---


### `groundx.projects.list`

This endpoint allows you to retrieve your existing projects.

#### 🛠️ Usage

```typescript
const listResponse = await groundx.projects.list();
```

#### 🔄 Return
[ProjectListResponse](./models/project-list-response.ts)

#### 🌐 Endpoint

`/v1/project` `GET`

[🔙 Back to Table of Contents](#table-of-contents)

---


### `groundx.projects.update`

This endpoint allows you to update an existing project.

#### 🛠️ Usage

```typescript
const updateResponse = await groundx.projects.update({
  projectId: "projectId_example",
  project: {
    name: "your_project_name",
  },
});
```

#### ⚙️ Parameters

##### project: [`ProjectUpdateRequestProject`](./models/project-update-request-project.ts)

##### projectId: `string`

The ID of the project to update.

#### 🔄 Return
[ProjectResponse](./models/project-response.ts)

#### 🌐 Endpoint

`/v1/project/{projectId}` `PUT`

[🔙 Back to Table of Contents](#table-of-contents)

---


### `groundx.search.content`

Search and retrieve relevant content from a project, group, or bucket by id.

#### 🛠️ Usage

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

#### ⚙️ Parameters

##### search: [`SearchRequestSearch`](./models/search-request-search.ts)

##### id: `number`

The ID of the project, group, or bucket to search within.

##### n: `number`

Number of results

#### 🔄 Return
[SearchResponse](./models/search-response.ts)

#### 🌐 Endpoint

`/v1/search/{id}` `POST`

[🔙 Back to Table of Contents](#table-of-contents)

---


## Author
This TypeScript package is automatically generated by [Konfig](https://konfigthis.com)
