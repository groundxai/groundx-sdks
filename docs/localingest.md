# Local Content Ingest
<iframe width="560" height="315" src="https://www.youtube.com/embed/_iMVoB5paeY?si=h0pvy_F4Qoe0-7EF" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## Introduction

In this tutorial, we'll cover how to add or ingest your local files to GroundX.

GroundX’s true potential commences with the file ingestion process, one of its key advantages over other RAG solutions.

**With our proprietary ingest pipeline, your files undergo three critical processes in which GroundX:** 

- formats your content for LLM use, 
- parses content into intelligible text chunks, 
- and generates contextual metadata.

Unlike other RAG solutions that require you to previously convert your files into plain text, Ground X is compatible with a wide variety of file formats, detects document structures, such as tables or page numbers, eliminates clutter, and re-writes content so that it can be clearly understood by an LLM.

## Getting started

### Required information
Before we begin, make sure you have the following information:

- The ID of the GroundX bucket in which you wish to store your file.
- The path of the file you want to upload from your computer.
- The file name you wish to give your file once it's in the GroundX bucket.
- Indicate the file type to get the file correctly processed.

_Example:_

:::code

```python
bucketId = 6830
uploadLocal = "documents/Aristotle-rhetoric.pdf";
fileName = "aristotle-rhetoric.pdf";
fileType = "pdf"
```

```javascript
const bucketId = 6830;
const filePath = "documents/Aristotle-rhetoric.pdf";
const fileName = "aristotle-rhetoric.pdf";
const fileType = "pdf";
```

:::

### Adding extra search data
Although not required because GroundX automatically generates contextual search data for your files, you can add extra search data to take maximum advantage of GroundX's search capabilities, help maintain document context in the search query responses, and add tags or notes indicating instructions on how to handle the search results.

_Example:_

:::code

```python
searchData = {
    title: "rhetoric",
    author: "Aristotle",
    keywords: ["Ethos", "Pathos", "Logos", "Rhetorical Triangle", "Persuasion"]
}
```

```javascript
const searchData = {
    title: "rhetoric",
    author: "Aristotle",
    keywords: ["Ethos", "Pathos", "Logos", "Rhetorical Triangle", "Persuasion"]
}
```

:::

### Set up environment
Set up your environment.

_Example:_

:::code

```python
from groundx import Groundx

groundx = Groundx(
    api_key=GROUNDX_API_KEY,
)
```

```javascript
import { Groundx } from 'groundx-typescript-sdk';
import fs from "fs";

const groundx = new Groundx({
    apiKey: GROUNDX_API_KEY,
});
```

:::

:::info{title="API Key"}
- The "GROUNDX_API_KEY" placeholder represents your API key. We recommend storing your API key as an environment variable and accessing it from there. For this purpose, you can use libraries such as [dotenv](https://www.npmjs.com/package/dotenv) in Node.js or [os](https://docs.python.org/3/library/os.html#os.environ) in Python.
- Go to the [GroundX dashboard](https://dashboard.groundx.ai/auth/login) to get your API key.
- Go to the [GroundX-SDKs documentation](https://github.com/groundxai/groundx-sdks#groundx-sdks) for installation details.
:::

## API request
Make the API request to upload local documents and include the variables in the request body.

:::code

```python
response = groundx.documents.upload_local(
    body=[
        {
            "blob": open(uploadLocal, "rb"),
            "metadata": {
                "bucketId": bucketId,
                "fileName": fileName,
                "fileType": fileType,
                "searchData": searchData,
            },
        },
    ]
)
```

```javascript
const response = await groundx.documents.uploadLocal([
        {
            blob: fs.readFileSync(filePath),
            metadata: {
                bucketId: bucketId,
                fileName: fileName,
                fileType: fileType,
                searchData: searchData
            },
        },
    ]);
```

:::

## API response

After making the request, you should receive a response with "processId" and "status". This response indicates that GroundX is uploading or ingesting your file into the indicated bucket.

```json
{
    'ingest': {
        'processId': '23e782ac-3829-4833-965d-e77b4e289885', 
        'status': 'queued'
    }
}
```

## Final details

Processing time depends on the size of your files. File size can be up to ten megabytes. 

After automatically ingesting your files and eliminating the typical complexity of other RAG solutions, GroundX has prepared your content for searchability and automated response generation for your queries.
