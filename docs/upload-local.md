# Upload Local Documents to GroundX

This tutorial will show you how to use GroundX's Typescript and Python SDK libraries to [upload local documents](https://documentation.groundx.ai/reference/Documents/Document_uploadLocal) to your GroundX [buckets](https://documentation.groundx.ai/docs/concepts#concepts-buckets).

Through a simple API request you can [effortlessly upload your content to GroundX](https://documentation.groundx.ai/docs/welcome#welcome-effortless-content-upload) and [automatically pre-process](https://documentation.groundx.ai/docs/welcome#welcome-sophisticated-automated-pre-processing) your data to get it ready to be [searched](https://documentation.groundx.ai/docs/welcome#welcome-superior-search-capabilities) through. 


## Prerequisites
- Node.js installed (for Javascript or Typescript projects)
- Python 3.7 or higher installed (for Python projects)

:::note
You can download the code for this tutorial from the GroundX code sample repository in [Typescript](https://github.com/groundxai/code-samples/blob/master/typescript/upload-local/demo.js) (for Javascript and Node.js projects) or [Python](https://github.com/groundxai/code-samples/blob/master/python/upload-local/demo.py).
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

:::warn
It is recommended that you store your API key in an environment variable and access it from there. For example, using the [dotenv](https://www.npmjs.com/package/dotenv) library in Node.js or the [os](https://docs.python.org/3/library/os.html#os.environ) library in Python.
:::

## Step 4: Set up content ingestion parameters
Set up the parameters for the content ingestion request. For more information on the parameters for uploading local documents to GroundX, go to the :api[Document_uploadLocal] reference guide.

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

1. Set a variable to indicate the type of content you want to ingest. Currently, the supported file types are:
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

3. Set a variable to indicate the relative path of the local content you want to ingest. For example:

:::code

```python
uploadHosted = '<RELATIVE_LOCAL_PATH>'
```

```typescript
const uploadHosted = "<RELATIVE_LOCAL_PATH>";
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

:::info{title="Metadata"}
Although metadata is automatically extracted from the content during the ingestion process, you can also include your own metadata. 
When GroundX carries out search querires, it searches through not only your content but also the associated metadata. This helps provide more accurate search results and returns document chunks with the corresponding metadata so that you don't lose the context the metadata provides.
:::


## Step 5: Set parameter validation
Optional: Set up parameter validation to check if all the required parameters are set. For example:

:::code

```python
if groundxKey == "YOUR_GROUNDX_KEY":
    raise Exception("set your GroundX key")

if uploadLocal == "":
    raise Exception("set the local file path")

if fileType == "":
    raise Exception("set the file type to a supported enumerated type (e.g. txt, pdf)")

if fileName == "":
    raise Exception("set a name for the file")
```

```typescript
if (groundxKey === "YOUR_GROUNDX_KEY") {
  throw Error("set your GroundX key");
}

if (uploadLocal === "") {
  throw Error("set the local file path")
}

if (fileType === "") {
  throw Error("set the file type to a supported enumerated type (e.g. txt, pdf)")
}

if (fileName === "") {
  throw Error("set a name for the file")
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
Before uploading the content, we'll set the default bucket ID. Since we set the bucket ID to `0` in [Step 4.1](#step-4-set-up-content-ingestion-parameters), we'll now call the :api[Bucket_list] endpoint to check if any buckets exist and get the ID of the first bucket in the list. For example:

:::code

```python
if bucketId == 0:
    # list buckets
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
      // list buckets
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
    
      bucketId = bucketResponse.data.buckets[0].bucketId;
    }
```

:::

## Step 8: Upload the content
Upload the content by calling the :api[Document_uploadLocal] endpoint with the parameters you set in [Step 4](#step-4-set-up-content-ingestion-parameters) as arguments. For example:

:::code

```python
# upload local documents to GroundX
try:
    ingest = groundx.documents.upload_local(
        body=[
            {
                "blob": open(uploadLocal, "rb"),
                "metadata": {
                    "bucketId": bucketId,
                    "fileName": fileName,
                    "fileType": fileType,
                    # optional metadata field
                    # content is added to document chunks
                    # fields are search during search requests
                    # and returned in search results
                    "metadata": contentMetadata,
                },
            },
        ]
    )
```

```typescript
// Note: Insert this code within a function.

// upload local documents to GroundX
    let ingest = await groundx.documents.uploadLocal([
      {
        blob: fs.readFileSync(uploadLocal),
        metadata: {
          bucketId: bucketId,
          fileName: fileName,
          fileType: fileType,
          metadata: contentMetadata,
        },
      }
    ]);
```

:::

The :api[Document_uploadLocal] endpoint returns a response object indicating the status of the ingestion process. 

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


## Step 9: Get ingest status
To check the status of the ingestion process, we'll use the request response and the :api[Document_getProcessingStatusById] endpoint. For example:

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
    print("Exception when calling DocumentApi.upload_local: %s\n" % e)
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
1. After you have adjustmented the code accordingly, run your code to upload the content to GroundX.
2. Call the :api[Document_list] endpoint to from GroundX's interactive [API Reference guide](https://documentation.groundx.ai/reference/Documents/Document_list) to get a list of all the documents in your GroundX buckets.
3. Check if the content you uploaded is listed in the response.

**And that's it!**  
_You've successfully ingested a local document to GroundX that you can now search through using GroundX's [search API](https://documentation.groundx.ai/reference/Search/Search_content)._