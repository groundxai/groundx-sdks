<div align="center">

[![Visit Groundx](./header.png)](https://www.groundx.ai)

# [Groundx](https://www.groundx.ai)<a id="groundx"></a>

Ground Your RAG Apps in Fact not Fiction

[![npm](https://img.shields.io/badge/npm-v1.3.16-blue)](https://www.npmjs.com/package/groundx-typescript-sdk/v/1.3.16)
[![More Info](https://img.shields.io/badge/More%20Info-Click%20Here-orange)](https://www.groundx.ai/)

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
  * [`groundx.documents.crawlWebsite`](#groundxdocumentscrawlwebsite)
  * [`groundx.documents.delete`](#groundxdocumentsdelete)
  * [`groundx.documents.delete1`](#groundxdocumentsdelete1)
  * [`groundx.documents.get`](#groundxdocumentsget)
  * [`groundx.documents.getProcessingStatusById`](#groundxdocumentsgetprocessingstatusbyid)
  * [`groundx.documents.list`](#groundxdocumentslist)
  * [`groundx.documents.lookup`](#groundxdocumentslookup)
  * [`groundx.documents.uploadLocal`](#groundxdocumentsuploadlocal)
  * [`groundx.documents.uploadRemote`](#groundxdocumentsuploadremote)
  * [`groundx.projects.addBucket`](#groundxprojectsaddbucket)
  * [`groundx.projects.create`](#groundxprojectscreate)
  * [`groundx.projects.delete`](#groundxprojectsdelete)
  * [`groundx.projects.get`](#groundxprojectsget)
  * [`groundx.projects.list`](#groundxprojectslist)
  * [`groundx.projects.removeBucket`](#groundxprojectsremovebucket)
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

const createResponse = await groundx.buckets.create({
  name: "your_bucket_name",
});

console.log(createResponse);
```

## Reference<a id="reference"></a>


### `groundx.buckets.create`<a id="groundxbucketscreate"></a>

Create a new bucket.  Interact with the \"Request Body\" below to explore the arguments of this function. Enter your GroundX API key to send a request directly from this web page. Select your language of choice to structure a code snippet based on your specified arguments. 

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

Delete a bucket.  Interact with the \"Request Body\" below to explore the arguments of this function. Enter your GroundX API key to send a request directly from this web page. Select your language of choice to structure a code snippet based on your specified arguments. 

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

Look up a specific bucket by its bucketId.  Interact with the \"Request Body\" below to explore the arguments of this function. Enter your GroundX API key to send a request directly from this web page. Select your language of choice to structure a code snippet based on your specified arguments. 

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

List all buckets within your GroundX account  Interact with the \"Request Body\" below to explore the arguments of this function. Enter your GroundX API key to send a request directly from this web page. Select your language of choice to structure a code snippet based on your specified arguments. 

#### 🛠️ Usage<a id="🛠️-usage"></a>

```typescript
const listResponse = await groundx.buckets.list({});
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### n: `number`<a id="n-number"></a>

The maximum number of returned documents. Accepts 1-100 with a default of 20.

##### nextToken: `string`<a id="nexttoken-string"></a>

A token for pagination. If the number of documents for a given query is larger than n, the response will include a \"nextToken\" value. That token can be included in this field to retrieve the next batch of n documents.

#### 🔄 Return<a id="🔄-return"></a>

[BucketListResponse](./models/bucket-list-response.ts)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/bucket` `GET`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


### `groundx.buckets.update`<a id="groundxbucketsupdate"></a>

Rename a bucket.  Interact with the \"Request Body\" below to explore the arguments of this function. Enter your GroundX API key to send a request directly from this web page. Select your language of choice to structure a code snippet based on your specified arguments. 

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


### `groundx.documents.crawlWebsite`<a id="groundxdocumentscrawlwebsite"></a>

Upload the content of a publicly accessible website to a GroundX bucket. This is done by following links within a specified URL, recursively, up to a specified depth or number of pages.  Interact with the \"Request Body\" below to explore the arguments of this function. Enter your GroundX API key to send a request directly from this web page. Select your language of choice to structure a code snippet based on your specified arguments. 

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

Delete multiple documents hosted on GroundX  Interact with the \"Request Body\" below to explore the arguments of this function. Enter your GroundX API key to send a request directly from this web page. Select your language of choice to structure a code snippet based on your specified arguments. 

#### 🛠️ Usage<a id="🛠️-usage"></a>

```typescript
const deleteResponse = await groundx.documents.delete({
  documentIds: ["documentIds_example"],
});
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### documentIds: `string`[]<a id="documentids-string"></a>

A list of documentIds which correspond to documents uploaded to GroundX

#### 🔄 Return<a id="🔄-return"></a>

[IngestResponse](./models/ingest-response.ts)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/ingest/documents` `DELETE`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


### `groundx.documents.delete1`<a id="groundxdocumentsdelete1"></a>

Delete a single document hosted on GroundX  Interact with the \"Request Body\" below to explore the arguments of this function. Enter your GroundX API key to send a request directly from this web page. Select your language of choice to structure a code snippet based on your specified arguments. 

#### 🛠️ Usage<a id="🛠️-usage"></a>

```typescript
const delete1Response = await groundx.documents.delete1({
  documentId: "documentId_example",
});
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### documentId: `string`<a id="documentid-string"></a>

A documentId which correspond to a document uploaded to GroundX

#### 🔄 Return<a id="🔄-return"></a>

[IngestResponse](./models/ingest-response.ts)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/ingest/document/{documentId}` `DELETE`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


### `groundx.documents.get`<a id="groundxdocumentsget"></a>

Look up an existing document by documentId.  Interact with the \"Request Body\" below to explore the arguments of this function. Enter your GroundX API key to send a request directly from this web page. Select your language of choice to structure a code snippet based on your specified arguments. 

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

Get the current status of an upload, initiated with documents.upload_remote, documents.upload_local, or documents.crawl_website, by specifying the processId (the processId is included in the response of the documents.upload functions).  Interact with the \"Request Body\" below to explore the arguments of this function. Enter your GroundX API key to send a request directly from this web page. Select your language of choice to structure a code snippet based on your specified arguments. 

#### 🛠️ Usage<a id="🛠️-usage"></a>

```typescript
const getProcessingStatusByIdResponse =
  await groundx.documents.getProcessingStatusById({
    processId: "processId_example",
  });
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### processId: `string`<a id="processid-string"></a>

the processId for the upload process being checked

#### 🔄 Return<a id="🔄-return"></a>

[ProcessStatusResponse](./models/process-status-response.ts)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/ingest/{processId}` `GET`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


### `groundx.documents.list`<a id="groundxdocumentslist"></a>

lookup all documents across all resources which are currently on GroundX  Interact with the \"Request Body\" below to explore the arguments of this function. Enter your GroundX API key to send a request directly from this web page. Select your language of choice to structure a code snippet based on your specified arguments. 

#### 🛠️ Usage<a id="🛠️-usage"></a>

```typescript
const listResponse = await groundx.documents.list({});
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### n: `number`<a id="n-number"></a>

The maximum number of returned documents. Accepts 1-100 with a default of 20.

##### nextToken: `string`<a id="nexttoken-string"></a>

A token for pagination. If the number of documents for a given query is larger than n, the response will include a \"nextToken\" value. That token can be included in this field to retrieve the next batch of n documents.

#### 🔄 Return<a id="🔄-return"></a>

[DocumentListResponse](./models/document-list-response.ts)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/ingest/documents` `GET`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


### `groundx.documents.lookup`<a id="groundxdocumentslookup"></a>

lookup the document(s) associated with a processId, bucketId, or projectId.  Interact with the \"Request Body\" below to explore the arguments of this function. Enter your GroundX API key to send a request directly from this web page. Select your language of choice to structure a code snippet based on your specified arguments. 

#### 🛠️ Usage<a id="🛠️-usage"></a>

```typescript
const lookupResponse = await groundx.documents.lookup({
  id: 1,
});
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `number`<a id="id-number"></a>

a processId, bucketId, or projectId

##### n: `number`<a id="n-number"></a>

The maximum number of returned documents. Accepts 1-100 with a default of 20.

##### nextToken: `string`<a id="nexttoken-string"></a>

A token for pagination. If the number of documents for a given query is larger than n, the response will include a \"nextToken\" value. That token can be included in this field to retrieve the next batch of n documents.

#### 🔄 Return<a id="🔄-return"></a>

[DocumentLookupResponse](./models/document-lookup-response.ts)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/ingest/documents/{id}` `GET`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


### `groundx.documents.uploadLocal`<a id="groundxdocumentsuploadlocal"></a>

Upload documents hosted on a local file system to a GroundX bucket.  Interact with the \"Request Body\" below to explore the arguments of this function. Enter your GroundX API key to send a request directly from this web page. Select your language of choice to structure a code snippet based on your specified arguments. 

#### 🛠️ Usage<a id="🛠️-usage"></a>

```typescript
const uploadLocalResponse = await groundx.documents.uploadLocal([
  {
    blob: fs.readFileSync("/path/to/file"),
    metadata: {
      bucketId: 1234,
      fileName: "my_file.txt",
      fileType: "string_example",
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

Upload documents hosted on public URLs to a GroundX bucket.   Interact with the \"Request Body\" below to explore the arguments of this function. Enter your GroundX API key to send a request directly from this web page. Select your language of choice to structure a code snippet based on your specified arguments. 

#### 🛠️ Usage<a id="🛠️-usage"></a>

```typescript
const uploadRemoteResponse = await groundx.documents.uploadRemote({
  documents: [
    {
      bucketId: 1234,
      fileName: "my_file.txt",
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


### `groundx.projects.addBucket`<a id="groundxprojectsaddbucket"></a>

Add an existing bucket to an existing project. Buckets and projects can be associated many to many.  Interact with the \"Request Body\" below to explore the arguments of this function. Enter your GroundX API key to send a request directly from this web page. Select your language of choice to structure a code snippet based on your specified arguments. 

#### 🛠️ Usage<a id="🛠️-usage"></a>

```typescript
const addBucketResponse = await groundx.projects.addBucket({
  projectId: 1,
  bucketId: 1,
});
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### projectId: `number`<a id="projectid-number"></a>

The projectId of the project which the bucket will be added to.

##### bucketId: `number`<a id="bucketid-number"></a>

The bucketId of the bucket being added to the project.

#### 🔄 Return<a id="🔄-return"></a>

[MessageResponse](./models/message-response.ts)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/project/{projectId}/bucket/{bucketId}` `POST`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


### `groundx.projects.create`<a id="groundxprojectscreate"></a>

create a new project, a project being a collection of buckets which can be searched.  Interact with the \"Request Body\" below to explore the arguments of this function. Enter your GroundX API key to send a request directly from this web page. Select your language of choice to structure a code snippet based on your specified arguments. 

#### 🛠️ Usage<a id="🛠️-usage"></a>

```typescript
const createResponse = await groundx.projects.create({
  name: "your_project_name",
  bucketName: "your_new_bucket_name",
});
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `string`<a id="name-string"></a>

The name of the project being created.

##### bucketName: `string`<a id="bucketname-string"></a>

Specify bucketName to automatically create a bucket, by the name specified, and add it to the created project.

#### 🔄 Return<a id="🔄-return"></a>

[ProjectResponse](./models/project-response.ts)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/project` `POST`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


### `groundx.projects.delete`<a id="groundxprojectsdelete"></a>

Delete a project.  Interact with the \"Request Body\" below to explore the arguments of this function. Enter your GroundX API key to send a request directly from this web page. Select your language of choice to structure a code snippet based on your specified arguments. 

#### 🛠️ Usage<a id="🛠️-usage"></a>

```typescript
const deleteResponse = await groundx.projects.delete({
  projectId: 1,
});
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### projectId: `number`<a id="projectid-number"></a>

The projectId of the project to be deleted.

#### 🔄 Return<a id="🔄-return"></a>

[MessageResponse](./models/message-response.ts)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/project/{projectId}` `DELETE`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


### `groundx.projects.get`<a id="groundxprojectsget"></a>

look up a specific project by its projectId.  Interact with the \"Request Body\" below to explore the arguments of this function. Enter your GroundX API key to send a request directly from this web page. Select your language of choice to structure a code snippet based on your specified arguments. 

#### 🛠️ Usage<a id="🛠️-usage"></a>

```typescript
const getResponse = await groundx.projects.get({
  projectId: 1,
});
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### projectId: `number`<a id="projectid-number"></a>

The projectId of the project to look up.

#### 🔄 Return<a id="🔄-return"></a>

[ProjectResponse](./models/project-response.ts)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/project/{projectId}` `GET`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


### `groundx.projects.list`<a id="groundxprojectslist"></a>

list all projects within your GroundX account.  Interact with the \"Request Body\" below to explore the arguments of this function. Enter your GroundX API key to send a request directly from this web page. Select your language of choice to structure a code snippet based on your specified arguments. 

#### 🛠️ Usage<a id="🛠️-usage"></a>

```typescript
const listResponse = await groundx.projects.list({});
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### n: `number`<a id="n-number"></a>

The maximum number of returned documents. Accepts 1-100 with a default of 20.

##### nextToken: `string`<a id="nexttoken-string"></a>

A token for pagination. If the number of documents for a given query is larger than n, the response will include a \"nextToken\" value. That token can be included in this field to retrieve the next batch of n documents.

#### 🔄 Return<a id="🔄-return"></a>

[ProjectListResponse](./models/project-list-response.ts)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/project` `GET`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


### `groundx.projects.removeBucket`<a id="groundxprojectsremovebucket"></a>

remove a bucket from a project. Buckets and projects can be associated many to many, this removes one bucket to project association without disturbing others.  Interact with the \"Request Body\" below to explore the arguments of this function. Enter your GroundX API key to send a request directly from this web page. Select your language of choice to structure a code snippet based on your specified arguments. 

#### 🛠️ Usage<a id="🛠️-usage"></a>

```typescript
const removeBucketResponse = await groundx.projects.removeBucket({
  projectId: 1,
  bucketId: 1,
});
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### projectId: `number`<a id="projectid-number"></a>

The projectId of the project which the bucket will be removed from.

##### bucketId: `number`<a id="bucketid-number"></a>

The bucketId of the bucket which will be removed from the project.

#### 🔄 Return<a id="🔄-return"></a>

[MessageResponse](./models/message-response.ts)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/project/{projectId}/bucket/{bucketId}` `DELETE`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


### `groundx.projects.update`<a id="groundxprojectsupdate"></a>

Rename a project  Interact with the \"Request Body\" below to explore the arguments of this function. Enter your GroundX API key to send a request directly from this web page. Select your language of choice to structure a code snippet based on your specified arguments. 

#### 🛠️ Usage<a id="🛠️-usage"></a>

```typescript
const updateResponse = await groundx.projects.update({
  projectId: 1,
  newName: "your_project_name",
});
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### newName: `string`<a id="newname-string"></a>

The new name of the project being renamed.

##### projectId: `number`<a id="projectid-number"></a>

The projectId of the project to update.

#### 🔄 Return<a id="🔄-return"></a>

[ProjectResponse](./models/project-response.ts)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/project/{projectId}` `PUT`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


### `groundx.search.content`<a id="groundxsearchcontent"></a>

Search documents on GroundX for the most relevant information to a given query.  The result of this query is typically used in one of two ways; result[\'search\'][\'text\'] can be used to provide context to a language model, facilitating RAG, or result[\'search\'][\'results\'] can be used to observe chunks of text which are relevant to the query, facilitating citation.  Interact with the \"Request Body\" below to explore the arguments of this function. Enter your GroundX API key to send a request directly from this web page. Select your language of choice to structure a code snippet based on your specified arguments. 

#### 🛠️ Usage<a id="🛠️-usage"></a>

```typescript
const contentResponse = await groundx.search.content({
  id: 1,
  n: 20,
  nextToken: "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9",
  query: "my search query",
});
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### query: `string`<a id="query-string"></a>

The search query to be used to find relevant documentation.

##### id: `number`<a id="id-number"></a>

The bucketId or projectId of the bucket or project being searched. The documents within the specified container will be compared to the query, and relevant information will be extracted.

##### n: `number`<a id="n-number"></a>

The maximum number of returned documents. Accepts 1-100 with a default of 20.

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


## Author<a id="author"></a>
This TypeScript package is automatically generated by [Konfig](https://konfigthis.com)
