# Upload Documents from a Remote Location

This tutorial will show you how to use GroundX's Typescript and Python SDK libraries to upload online content to your GroundX database.

The upload process is an API request sent to the GroundX server that ingests the content from a URL to the GroundX database. Content ingestion includes uploading the content to the GroundX server, extracting the content, and indexing the content with vector embeddings and metadata. The content is then ready to be searched through.


## Prerequisites
- Node.js installed (for Javascript or Typescript projects)
- Python 3.7 or higher installed (for Python projects)

:::note
You can download the code for this tutorial from the GroundX code sample repository in [Typescript](https://github.com/groundxai/code-samples/tree/master/typescript/upload-remote) (for Javascript and Node.js projects) or [Python](https://github.com/groundxai/code-samples/tree/master/python/upload-remote).
:::

## Step 1: Set up your environment
If you haven't already done so, follow the steps below to get your GroundX API key and install the GroundX SDK for your project.

1. To get your GroundX API key, log in to your GroundX dashboard and go to the [API Keys](https://dashboard.groundx.ai/apikey) section.

:::note
If you don't have a GroundX account, you can sign up for a free account at [https://www.groundx.ai](https://www.groundx.ai).
:::

2. Install the GroundX SDK for either [Typescript](https://github.com/groundxai/groundx-sdks/blob/main/sdks/typescript/README.md) or [Python](https://github.com/groundxai/groundx-sdks/tree/main/sdks/python) with the following commands:

:::code

```python
pip install groundx-python-sdk
```

```typescript
npm install groundx-typescript-sdk --save
```

:::

## Step 2: Import required libraries
In your project, import the GroundX SDK library:

:::code

```python
from groundx import Groundx, ApiException
```

```typescript
import { Groundx } from "groundx-typescript-sdk";
```

:::

## Step 3: Set up your API key
Set up your API key by creating a new GroundX object and passing your API key as a parameter:

:::code

```python
groundxKey = 'YOUR_GROUNDX_KEY'
```

```typescript
const groundxKey = "YOUR_GROUNDX_KEY";
```

:::

:::note
It is recommended that you store your API key in an environment variable and access it from there. For example, using the [dotenv](https://www.npmjs.com/package/dotenv) library in Node.js or the [os](https://docs.python.org/3/library/os.html#os.environ) library in Python.
:::

## Step 4: Set up content ingestion parameters
Set up the parameters for the content ingestion request. For more information on the parameters for uploading hosted documents to GroundX, go to the [API reference](https://documentation.groundx.ai/reference/Documents/Document_uploadRemote).

1. Indicate the ID of the [bucket](https://documentation.groundx.ai/docs/concepts#concepts-buckets) you want to ingest the content into by setting the `bucket` parameter.

:::code

```python
bucketID = 0
```

```typescript
let bucketId = 0;
```

:::

:::note
For simplicity, in this tutorial we'll set `bucketID` to `0` to ingest the content into a default bucket (See [Step 7](#step-7-get-default-bucket-id)).
:::

1. Set a variable to indicate the type of content you want to ingest. Currently supported file types are:
- txt
- docx
- pptx
- xlsx
- pdf
- png
- jpg

For example:

:::code
    
```python
fileType = '<FILE_TYPE>'
```

```typescript
const fileType = "<FILE_TYPE>";
```

:::

3. Set a variable to indicate the URL of the content you want to ingest. For example:

:::code

```python
uploadHosted = '<URL>'
```

```typescript
const uploadHosted = "<URL>";
```

:::

4. Optional: Include an object containing metadata for your content. For example:

:::code

```python
contentMetadata = {
    "title": "Sample Title",
    "description": "Sample Description",
    "author": "Sample Author",
    "tags": ["Sample Tag 1", "Sample Tag 2"]
}
```

```typescript
const contentMetadata = {
    title: "Sample Title",
    description: "Sample Description",
    author: "Sample Author",
    tags: ["Sample Tag 1", "Sample Tag 2"]
};

```

:::

:::note Although metadata is automatically extracted from the content during the ingestion process, you can also include your own metadata. 
When GroundX carries out search querires, it searches through not only your content but also the associated metadata. This helps provide more accurate search results and returns document chunks with the corresponding metadata so that you don't lose the context the metadata provides.
:::


## Step 5: Set parameter validation
Set up parameter validation to check if all the required parameters are set. For example:

:::code

```python
if groundxKey == "":
    raise Exception("set your GroundX key")

if uploadHosted == "":
    raise Exception("set the hosted file URL")

if fileType == "":
    raise Exception("set the file type to a supported enumerated type (e.g. txt, pdf)")
```

```typescript
if (groundxKey === "YOUR_GROUNDX_KEY") {
    throw Error("set your GroundX key");
}

if (uploadHosted === "") {
    throw Error("set the hosted file URL");
}

if (fileType === "") {
    throw Error("set the file type to a supported enumerated type (e.g. txt, pdf)");
}
```

:::


## Step 6: Initialize the GroundX client
Initialize the GroundX client by creating a new GroundX object and passing your API key as a parameter. For example:

:::code

```python
groundx = Groundx(
    api_key=groundxKey,
)
```

```typescript
const groundx = new Groundx({
  apiKey: groundxKey,
});
```

:::

## Step 7: Get default bucket ID
Before uploading the content, we'll set the default bucket ID. Since we set the bucket ID to `0` in [Step 4.1](#step-4-set-up-content-ingestion-parameters), we'll now use the `groundx.buckets.list()` method to check if any buckets exist and get the ID of the first bucket in the list. For example:

:::code

```python
if bucketId == 0:
    # list buckets request
    try:
        bucket_response = groundx.buckets.list()

        if len(bucket_response.body["buckets"]) < 1:
            print(bucket_response.body["buckets"])
            raise Exception("no results from buckets")

        bucketId = bucket_response.body["buckets"][0]["bucketId"]
    except ApiException as e:
        print("Exception when calling BucketApi.list: %s\n" % e)
```

```typescript
// Note: Insert this code within a function.

if (bucketId === 0) {
      // List buckets request
      const bucketResponse = await groundx.buckets.list();
      if (!bucketResponse || !bucketResponse.status || bucketResponse.status != 200 ||
          !bucketResponse.data || !bucketResponse.data.buckets) {
        console.error(bucketResponse);
        throw Error("GroundX bucket request failed");
      }
    
      if (bucketResponse.data.buckets.length < 1) {
        console.error("no results from buckets");
        console.log(bucketResponse.data.buckets);
        throw Error("no results from GroundX bucket query");
      }
      console.log(bucketResponse.data);
      bucketId = bucketResponse.data.buckets[0].bucketId;
    }
```

:::

## Step 8: Upload the content
Upload the content by calling the `groundx.documents.uploadRemote()` method and passing the parameters you set in [Step 4](#step-4-set-up-content-ingestion-parameters) as arguments. For example:

:::code

```python
# Upload hosted documents to GroundX request
try:
    ingest = groundx.documents.upload_remote(
        documents=[
            {
                "bucketId": bucketId,
                "metadata": contentMetadata,
                "sourceUrl": uploadHosted,
                "fileType": fileType,
            }
        ],
    )
```

```typescript
// Note: Insert this code within a function.

// Upload hosted documents to GroundX
    let ingest = await groundx.documents.uploadRemote({
      documents: [
        {
          bucketId: bucketId,
          type: fileType,
          metadata: contentMetadata,
          sourceUrl: uploadHosted,
        }
      ]
    });
```

:::

The `groundx.documents.uploadRemote()` method returns a response object indicating the status of the ingestion process. 

For example:

```json
// Successful request response
{
  "ingest": {
    "processId": "string", // Object ID of the ingest process
    "status": "string" // "queued" | "processing" | "error" | "complete"
  }
}
```

:::note For details about the parameters for uploading hosted documents to GroundX, go to the [API reference](https://documentation.groundx.ai/reference/Documents/Document_uploadRemote).
:::


## Step 9: Get ingest status
To check the status of the ingestion process, we'll use the request response and the [get processing status by ID](https://documentation.groundx.ai/reference/Documents/Document_getProcessingStatusById) method. For example:

:::code

```python
# Insert this code after the Try block in Step 8.
while (
        ingest.body["ingest"]["status"] != "complete"
        and ingest.body["ingest"]["status"] != "error"
    ):
        ingest = groundx.documents.get_processing_status_by_id(
            process_id=ingest.body["ingest"]["processId"]
        )
except ApiException as e:
    print("Exception when calling DocumentApi.upload_remote: %s\n" % e)
```

```typescript
// Note: Insert this code within a function.

if (!ingest || !ingest.status || ingest.status != 200 ||
      !ingest.data || !ingest.data.ingest) {
      console.error(ingest);
      throw Error("GroundX upload request failed");
    }
    
    // poll ingest status
    while (ingest.data.ingest.status !== "complete" && ingest.data.ingest.status !== "error") {
      ingest = await groundx.documents.getProcessingStatusById({
        processId: ingest.data.ingest.processId,
      });
      if (!ingest || !ingest.status || ingest.status != 200 ||
        !ingest.data || !ingest.data.ingest) {
        console.error(ingest);
        throw Error("GroundX upload request failed");
      }
    
      await new Promise((resolve) => setTimeout(resolve, 3000));
    }
```

:::

## Step 10: Test your code
1. Run your code to upload the content to GroundX accordingly.
2. Make the following request from GroundX's interactive API Reference guide: 
    [Look up all existing documents](https://documentation.groundx.ai/reference/Documents/Document_list)
3. Check if the content you uploaded is listed in the response.

**And that's it!** 
_You've successfully ingested a hosted document to GroundX, complete with vector and semantic data, that you can now search through using GroundX's [search API](https://documentation.groundx.ai/reference/Search/Search_content)._