# Quick Start

This Quick Start guide is intended to show you how to upload documents and search them using the GroundX APIs. The code within this QuickStart guide can be downloaded from the [code samples GitHub repository](https://github.com/groundxai/code-samples) in [Python](https://github.com/groundxai/code-samples/tree/master/python/getting-started) and [TypeScript](https://github.com/groundxai/code-samples/tree/master/typescript/getting-started).

## Step 1: Download GroundX SDK (optional)

This step is optional. Do this step only if you want to use our [TypeScript](https://github.com/groundxai/groundx-sdks/blob/main/sdks/typescript/README.md) (for javascript and NodeJS projects) or [Python](https://github.com/groundxai/groundx-sdks/blob/main/sdks/python/README.md) SDKs.

Use the following shell commands to install:

:::code

```python
pip install groundx-python-sdk
```

```typescript
npm install groundx-typescript-sdk --save
```

:::

## Step 2: Register and Get Your API Key

Before you can use our APIs, you will need to [create an account](https://dashboard.groundx.ai/auth/register) here.

Log into the [GroundX Dashboard](https://dashboard.groundx.ai) and navigate to API Keys.

<p style="text-align: center;">![Navigate to API Keys](./imgs/gs1.webp "Navigate to API Keys")</p>
<p style="text-align: center;">Navigate to <b>API Keys</b></p>

Copy your API Key and save it somewhere for use later in this tutorial.

<p style="text-align: center;">![Copy Your API Key](./imgs/gs2.webp "Copy Your API Key")</p>
<p style="text-align: center;">Copy Your API Key</p>

## Step 3: Initialize Your SDK (optional)

If you're using one of our SDKs, you will use your API key to initialize your client:

:::code

```python
import asyncio
from groundx import Groundx, ApiException

groundx = Groundx(
  api_key="<your_api_key>",
)
```

```typescript
import { Groundx } from "groundx-typescript-sdk";

const groundx = new Groundx({
  apiKey: "<your_api_key>",
});
```

:::

Replace `<your_api_key>` with your actual API key.

## Step 4: Make Your First Request

All of our API requests require your API Key in the header. Here is an example of how to include it:

:::code

```bash
curl https://api.groundx.ai/api/v1/bucket \
    -H "X-API-KEY: <your_api_key>"
```

```python
try:
  bucket_response = groundx.bucket.list()

  print(bucket_response.body["buckets"])
except ApiException as e:
  print("Exception when calling BucketApi.list: %s\n" % e)
```

```typescript
const bucketResponse = await groundx.bucket.list();

console.log(bucketResponse);
```

:::

For bash requests, replace <your_api_key> with your actual API key.

If your request is successful, you will receive a response that looks something like this:

```json
{
  "buckets": [
    {
      "bucketId": <unique_system_generated_id>,
      "fileCount": <number_of_documents_in_bucket>,
      "fileSize": "<files_size_total>",
      "name": "<your_bucket_name>"
    }
  ],
}
```

This request will return a list of your content buckets where you can upload your documents. Make note of the `bucketId` for use later in this tutorial.

## Step 5: Upload Content

To upload document content, use the [Document Upload API](/reference/Documents/Document_uploadRemote):

:::code

```bash
curl https://api.groundx.ai/api/v1/ingest/documents \
     -X POST \
     -H "X-API-KEY: <your_api_key>" \
     -d '{
           "documents": [
             {
               "bucketId":  <your_bucket_id>,
               "metadata": {
                 "<your_key>": "<your_value>"
               },
               "sourceUrl": "<path_to_your_file>"
             }
           ]
         }'
```

```python
# Upload local documents to GroundX

try:
  upload_local_response = groundx.document.upload_local(
    blob=[open("/path/to/your/file", "rb")],
    metadata={
      "bucket_id": <your_bucket_id>,
      "file_name": "my_file.pdf",
      "file_type": "pdf"
    },
  )
  print(upload_remote_response.body["ingest"])
except ApiException as e:
  print("Exception when calling DocumentApi.upload_local: %s\n" % e)


# Upload hosted documents to GroundX

try:
  upload_remote_response = groundx.document.upload_remote(
    documents=[
      {
        "bucket_id": <your_bucket_id>,
        "source_url": "https://path.to.your/file.docx",
        "type": "docx"
      }
    ],
  )
  print(upload_remote_response.body["ingest"])
except ApiException as e:
  print("Exception when calling DocumentApi.upload_remote: %s\n" % e)
```

```typescript
// Upload local documents to GroundX

const uploadLocalResponse = await groundx.document.uploadLocal({
  blob: [open("/path/to/your/file", "rb")],
  metadata: {
    bucketId: <your_bucket_id>,
    fileName: "my_file.pdf",
    fileType: "pdf"
  },
});
console.log(uploadLocalResponse);


// Upload hosted documents to GroundX

const uploadRemoteResponse = await groundx.document.uploadRemote({
  bucketId: <your_bucket_id>,
  sourceUrl: "https://path.to.your/file.docx",
  type: "docx"
});
console.log(uploadRemoteResponse);
```

:::

Replace `<path_to_your_file>` with the path to your file and `<your_bucket_id>` with the content bucket you would like to add the document to. Also, you can add `metadata`.

If your request is successful, will receive a response that looks something like this:

```json
{
    "ingest": {
        "processId": "<unique_system_generated_id",
        "status": "<enumerated_status>"
    }
}
```

Make note of `processId`. You will need it in the next step of this Quick Start guide.

## Step 6: Check the Status of Your Upload

Make the following request to query the status of your document upload as it is processed through the GroundX ingestion pipeline:

:::code

```bash
curl https://api.groundx.ai/api/v1/ingest/<processId> \
     -H "X-API-KEY: <your_api_key>" \
     -H "Content-Type: application/json"
```

```python
try:
  get_processing_status_by_id_response = groundx.document.get_processing_status_by_id(
    process_id="<processId>",  # required
  )
  print(get_processing_status_by_id_response.body["ingest"])
except ApiException as e:
  print("Exception when calling DocumentApi.get_processing_status_by_id: %s\n" % e)
```

```typescript
const getProcessingStatusByIdResponse =
  await groundx.document.getProcessingStatusById({
    processId: "<processId>",
  });

console.log(getProcessingStatusByIdResponse);
```

:::

Replace `<processId>` the processId from the previous step.

If your request is successful, will receive a response that looks something like this:

```json
{
    "ingest": {
        "processId": "<unique_system_generated_id>",
        "progress": {
            "complete": {
                "documents": [
                    {
                        "documentId": "<unique_system_generated_id>",
                        "fileName": "<given_file_name>",
                        "fileSize": "<files_size_total>",
                        "fileType": "<file_type>",
                        "bucketId": <your_bucket_id>,
                        "processId": "<unique_system_generated_id>",
                        "sourceUrl": "<document_url>",
                        "status": "<enumerated_status>"
                    }
                ],
                "total": 1
            }
        },
        "status": "<enumerated_status>"
    }
}
```

The value of `status` will be one of `queued`, `processing`, `error`,  or `complete`.

## Step 7: Search Your Content

Make the following request to search your ingested content:

:::code

```bash
curl https://api.groundx.ai/api/v1/search/<id> \
     -X POST \
     -H "X-API-KEY: <your_api_key>" \
     -H "Content-Type: application/json" \
     -d '{"search":{"query":"<your_query>"}}'
```

```python
try:
  content_response = groundx.search.content(
    id=<id>,  # required
    search={
      "query": "<your_query>"
    }
  )
  print(content_response.body["search"])
except ApiException as e:
  print("Exception when calling SearchApi.content: %s\n" % e)
```

```typescript
const contentResponse = await groundx.search.content({
  id: <id>,
  search: {
    query: "<your_query>"
  },
});

console.log(contentResponse);
```

:::

Replace `<id>` with your `projectId`, `groupId`, or `bucketId` and `<your_query>` with the query you want to use to search your content.

If your request is successful, will receive a response that looks something like this:

```json
{
    "search": {
        "count": <int_number_of_results>,
        "query": "<your_query>"
        "score": <float_highest_relevance_score_in_results>,
        "text": "<combined_text_of_search_results>",
        "nextToken": "<token_for_next_set_of_results>",
        "results":[
            {
                "documentId": "<unique_system_generated_id>",
                "metadata": {
                    <document_metadata>
                },
                "score": <float_relevance_score_of_result>,
                "sourceUrl": "<source_document_url>",
                "text":  "<text_of_result>"
            }
        ]
    }
}
```

If you need to look up a `projectId`, `groupId`, or `bucketId`, you can find them in the [GroundX Dashboard](https://dashboard.groundx.ai) or by querying for them using the APIs.

Make the following request to query for your projects:

:::code

```bash
curl https://api.groundx.ai/api/v1/project \
     -H "X-API-KEY: <your_api_key>"
```

```python
try:
  project_response = groundx.project.list()
  print(project_response.body["projects"])
except ApiException as e:
  print("Exception when calling ProjectApi.list: %s\n" % e)
```

```typescript
const projectResponse = await groundx.project.list();

console.log(projectResponse);
```

:::

If your request is successful, will receive a response that looks something like this:

```json
{
    "projects": [
        {
            "buckets": [
                {
                    "bucketId": <unique_system_generated_id>,
                    "fileCount": <number_of_documents_in_bucket>,
                    "fileSize": "<files_size_total>",
                    "name": "<your_bucket_name>"
                }
            ],
            "created": "<project_created_date_time>",
            "fileCount": <number_of_documents_in_project>,
            "fileSize": "<files_size_total>",
            "fileCount": <number_of_documents_in_project>,
            "name": "<your_project_name>",
            "projectId": <unique_system_generated_id>,
            "updated": "<project_updated_date_time>"
        }
    ]
}
```

## Next Steps

Now that you've successfully used the GroundX APIs to upload and search content, you can dive into our [tutorials](/docs/tutorials) and [documentation](/reference)!

Remember, our APIs are still in closed beta, so we appreciate your patience and feedback as we continue to improve our service.
