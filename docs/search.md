# Understanding Search in GroundX
<iframe width="560" height="315" src="https://www.youtube.com/embed/gqNO5zGXU1w?si=CXtwQ3ziOuTnBP7P" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## Introduction
In this tutorial, we’ll explore the GroundX search API.

What makes GroundX search results stand out?

**Under the hood, the GroundX Search API goes through the following process:**

- First, it analyzes your search query, and improves it if necessary, to carry out a semantic search that helps avoid the hallucination trap most RAG apps fall into with their vectorized searches.

- Next, it searches through GroundX buckets where your content and its extra search data are stored.  
GroundX’s unique extra search data approach helps maintain your content within its original context.
After finding relevant content, the Search API returns much more than just simple, unformatted chunks of raw text like most RAG systems. Instead, GroundX returns a search response bundled with intelligible text chunks along with extra search data, automatically generated documentation and section summaries, source URL, and a new, more readable, contextualized, and performant version of the text chunk ready for LLM use.

- Then, GroundX uses its proprietary re-ranker that scores every chunk for how well it answers the original question to ensure that the most trustworthy results are always on top.

- And finally, it merges all of this into a simple text block that you can send to the LLM of your choice, so you get accurate, contextualized, and hallucination-free responses from your LLMs when working with your content.

## LLM integration
_Sounds complex?_
Luckily GroundX does all the hard stuff for you in the background, you just have to follow these simple steps:

1. Make an API search request.

_Example:_

:::code

```python
queryString = "How many workers walk to work in the Bay Area?"

result = groundx.search.content(
    id=6839, 
    n=10,
    query=queryString,
)

llmText = result.body["search"]["text"]

```

```javascript
const queryString = "How many workers walk to work in the Bay Area?"

const result = await groundx.search.content({
    id: 6839,
    n: 10,
    query: queryString,
  });

const llmText = result.data.search.text;
```

:::info{title="More information"}

The [search API request](#getting-started) is explained further below.

:::

2. Retrieve the `search.text` property and pass it on to the LLM of your choice.

_Example:_

:::code

```python
from openai import OpenAI
client = OpenAI(
    api_key = OPENAI_API_KEY,
)

completion = openai.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {
        "role": "system", 
        "content": """Get response from this data:
===
%s
===
"""
      % (llmText),
    },
    {
        "role": "user", 
        "content": queryString,
    }
  ]
)
```

```javascript
import OpenAI from "openai";

const openai = new OpenAI(
    api_key: OPENAI_API_KEY,
);

const chatCompletion = await openai.chat.completions.create({
  model: "gpt-3.5-turbo",
  messages: [
    {
      "role": "system",
      "content": 'Respond only with:
          ===
          ${llmText}
          ===
          '
    },
    {
       "role": "user",   
       "content": queryString
    },
  ],
});
```

:::

:::info{title="LLM API"}

Make sure to get the API key, endpoints, and SDK from your LLM provider. For example, if using ChatGPT, go to the [OpenAI documentation](https://platform.openai.com/docs/overview)

:::

3. Get a response from the LLM using your retrieved data.

_Example:_

:::code

```python
print(completion.choices[0].message.content)
```

```javascript
console.log(chatCompletion.choices[0].message.content);
```

:::

**The end result**: _retrievals that outperform traditional vector systems and boost the accuracy of LLM completions._

## Getting started
Let’s go into the details.

To make an API request you’ll need to do the following:

### Ingest content
First, make sure you’ve already uploaded to a GroundX bucket the content you want to search through.

:::note

Go to either [Local Content Ingest](https://documentation.groundx.ai/docs/ingest-local-content) or [Remote Content Ingest](https://documentation.groundx.ai/docs/ingest-remote-content) for details on how to add your content to a GroundX bucket.

:::

### Set up environment
Next, set up your environment with the GroundX SDK.

:::code

```python
from groundx import Groundx

groundx = Groundx(
    api_key = GROUNDX_API_KEY,
)
```

```javascript
import { Groundx } from "groundx-typescript-sdk";

const groundx = new Groundx({
    apiKey: GROUNDX_API_KEY,
});
```

:::

### Bucket or project ID
Get the ID of the project or bucket you want to search through.

_Example:_

:::code

```python
groundxId = 3839
```

```javascript
const id = 3839
```

:::

:::note

Go to the documentation for information on how to obtain a project or bucket ID with the corresponding endpoint:
- :api[Bucket_list]
- :api[Project_list]

:::

## Search query string
Create a search query string. 

The string can be a question or the keywords you want to search for.

If query strings are more than 30 words long, GroundX automatically rewrites the string with keywords using its internal LLM.

GroundX processes the string to search through your content and its extra search data to retrieve the most relevant results.

_Example:_

:::code

```python
queryString = "How many workers walk to work in the Bay Area?"
```

```javascript
const queryString = "How many workers walk to work in the Bay Area?"
```

:::

## Number of results
Optionally, you can also set the number of results that are returned by the search request. By default, search queries return up to 20 results.

_Example:_

:::code

```python
n = 10
```

```javascript
const n = 10
```

:::


## API request
You’re now ready to make the API search request.
Include the ID and search query string in the request body.

_Example:_

:::code

```python
response = groundx.search.content(
    id=groundxId, 
    query=queryString,
    n=n,
)

print(response.body["search"]["text"])
```

```javascript
const response = await groundx.search.content({
    id: id,
    query: queryString
    n: n,
})

console.log(response.data.search.text)
```

:::

## API response
After making the request, you will receive a Search object as the response.

**Let’s go over some of the details of the Search schema.**

_Response sample:_

```json
{
    "count": 10,
    "query": "How many workers walk to work in the Bay Area?",
    "results":  [
         {
            "bucketId": 6839,
            "documentId": "81111b9e-ff13-41ef-a89a-af667a4b1cac",
            "score": 357.09656,
            "searchData": {
                "documentSummary": "This document is a detailed report from the Healthy Communities Data and Indicators Project by UCSF and CDPH...",
                "sectionSummary": "\"Given a row from the provided TSV table, this row represents data about the commuting habits of workers in a specific region in California over two time periods: 2005-2007 and 2008...",
                "fullTitle": "Percent of population aged 16 years or older whose commute to work is 10 or more minutes/day by walking or biking",
                "publisher": "California Department of Public Health",
            },
            "sourceUrl": "https://upload.groundx.ai/file/hciwalkbicycle778narrativeandexamples3-26-14.pdf",
            "suggestedText": "In the Bay Area between 2005-2007, 70,287 out of 3,122,743 workers, or 2.25%, walked for 10 or more minutes per day. This number increased to 81,737 out of 3,202,761 workers, or 2.55%, in the 2008-2010 period. In Butte, 1,266 out of 85,042 workers, or 1.49%, walked for 10 or more minutes per day between 2005-2007. This increased to 1,678...",
            "text": "\t|\t\t|\t2005-2007\t|\t\t|\t\t|\t2008-2010\n\t|\tWorkers who\t|\t\t|\t\t|\tWorkers who\n\t|\twalk ≥10\t|\t\t|\t\t|\twalk ≥10\nRegion name\t|\tmin / day\t|\tTotal..."
            },
    ]
    "score": 369.19244,
            "text": "fullTitle: Percent of population aged 16 years or older whose commute to work is 10 or more minutes/day by walking or biking\npublisher: California Department of Public Health\nIn the Bay Area between 2005-2007, 70,287 out of 3,122,743 workers, or 2.25%, walked for 10 or more minutes per day. This number increased to 81,737 out of 3,202,761 workers, or 2.55%, in the 2008-2010 period. In Butte, 1,266 out of 85,042 workers, or 1.49%, walked for 10 or more minutes per day between 2005-2007. This increased to 1,678 out of 81,321 workers, or 2.06%, in 2008-2010..."
}
```

### Recommended data
The most significant property returned by the search response is the `text` property, which contains a compilation of suggested texts with their corresponding extra search data.
In other words, it’s a string that includes all the automatically rewritten text chunks and the extra search data that was manually added to the original content.

As already mentioned, this content that is automatically generated by GroundX’s internal LLM provides you with intelligible, contextualized, and machine-understandable content that you can straightforwardly pass on to your LLM to work with.

### Advanced data handling
Although we recommend passing the `search.text` property directly to the LLM you’re working with for response generation, you can also add your own logic to handle the `search.results` property.


**Let’s take a closer look:**

The `results` property contains a list of all the original text chunks that matched the search query. Chunks are ordered by a score based on semantic search and re-ranking methodologies. 
Here, you can also find the suggested text we’ve been mentioning, which is the more intelligible and performant version of the text chunk.

Furthermore, you can find automatically generated extra search data, like summaries of the document and section the text chunks are found in.

The extra search data added to your content is available as well.
And to help keep source information available, the GroundX URL, document ID, and bucket ID of the content where the text chunks were extracted from are also provided.

## Final details
You’re now ready to integrate GroundX with your LLM to generate accurate, hallucination-free responses using data from your own content.
