# Remote Content Ingest
<iframe width="560" height="315" src="https://www.youtube.com/embed/KUeOKCiK2gw?si=vTpI-YLgE_iZPH7a" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## Introduction

In this tutorial, we'll go over how to add or ingest remote content into Ground X. This is the step where the magic begins. Ground X's ingestion pipeline is much more than just simply extracting content from your files. 

**Through its unique ingestion pipeline, comprised of three critical stages, Ground X:**
- Formats your content for LLM use
- Parses content into intelligible text chunks
- And generates contextual search data

Unlike other platforms that require content to be processed in plain text before being ingested, Ground X can automatically ingest a wide range of content types for you and also recognizes document structures, such as tables or page numbers, eliminates clutter, and rewrites content that can be clearly understood by an LLM.

**GroundX's fine-tuned computer vision model identifies the coordinates of these objects, extracts their content, and then converts them into LLM-readable formats.**

## Getting started
### Required information
To add online files to GroundX, you simply need the following information: 
 
- BucketID: The ID of the GroundX bucket in which you will store your document. 
- SourceURL: The URL of the file you want to add to your GroundX bucket. 

_Example:_

:::code

```python
bucketId = 6839;
sourceUrl = "https://data.chhs.ca.gov/dataset/hci_walk_bicycle.xls";
```

```javascript
const bucketId = 6839;
const sourceUrl = "https://data.chhs.ca.gov/dataset/hci_walk_bicycle.xls";
const searchData = {
    title: "Time Walk Bike to Work, 2001-2011",
    publisher: "California Department of Public Health",
    homepage: "https://catalog.data.gov/dataset/,
    abstract: "This table contains data on the percent of population aged 16 years or older whose commute to work is 10 or more minutes/day by walking or biking for California, its regions, counties, and cities/towns."
};
```

:::

### Adding extra search data
Provide document context with extra search data. Although not required because Ground X automatically generates contextual data for your files, you can add extra search data to take maximum advantage of Ground X's search capabilities, help maintain document context in the search query responses, and add tags or notes indicating instructions on how to handle the search results.

_Example:_

:::code

```python
searchData = {
    title: "Time Walk Bike to Work, 2001-2011",
    publisher: "California Department of Public Health",
    homepage: "https://catalog.data.gov/dataset/,
    abstract: "This table contains data on the percent of population aged 16 years or older whose commute to work is 10 or more minutes/day by walking or biking for California, its regions, counties, and cities/towns."
}
```

```javascript
const searchData = {
    title: "Time Walk Bike to Work, 2001-2011",
    publisher: "California Department of Public Health",
    homepage: "https://catalog.data.gov/dataset/,
    abstract: "This table contains data on the percent of population aged 16 years or older whose commute to work is 10 or more minutes/day by walking or biking for California, its regions, counties, and cities/towns."
};
```

:::

## Set up environment
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
Now simply make an API request to upload remote documents and include bucket ID, source URL, and extra search data in the request body.

_Example:_

:::code

```python
ingest = groundx.documents.upload_remote(
    documents=[
        {
            "bucketId": bucketId,
            "searchData": searchData,
            "sourceUrl": uploadHosted,
            "fileType": fileType,
        }
    ],
)

print(ingest.body)
```

```javascript
const ingest = await groundx.documents.uploadRemote({
    documents: [
        {
            bucketId: bucketId,
            sourceUrl: sourceUrl,
            searchData: searchData
        }
    ]
});

console.log(ingest.data)
```


:::

:::note
Go to :api[Document_uploadRemote] for endpoint details.
:::

## API response
After making the request, you should receive a response with `processId` and `status`. This response indicates that GroundX is uploading or ingesting your file into the indicated bucket. 

_Example:_

```json
{
  "ingest": {
    "processId": "744aaf18-ff7f-459e-831c-071866dcfa2d",
    "status": "queued"
  }
}
```


## Final details
Processing time depends on the size of your files. File size can be up to ten megabytes. 

After automatically ingesting your files and simplifying all of its complexity for you, Ground X has prepared your content for searchability and automated response generation for your queries.
