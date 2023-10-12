# Integrating with ChatGPT

Welcome to this hands-on tutorial where we'll delve into Retrieval Augmented Generation (RAG) by merging the capabilities of GroundX's search results with OpenAI's ChatGPT.

In this tutorial, we will use Python to show you how to seamlessly extract relevant content from GroundX and then channel it into ChatGPT for enhanced, context-aware conversational experiences. This will not only broaden the knowledge base of the ChatGPT model but also leverage the precise search and retrieval capabilities of GroundX.

By the end of this tutorial, you'll possess the skills to create a more informed and enriched conversational agent that can draw upon your private data. Let's get started!

:::note
You can download the code for this tutorial from the GroundX code sample repository in [TypeScript](https://github.com/groundxai/code-samples/blob/master/typescript/chatGPT-completions/demo.js) (for javascript and NodeJS projects) or [Python](https://github.com/groundxai/code-samples/blob/master/python/chatGPT-completions/demo.py).
:::

## Step 1: Set Up Your Environment

You will need a **GroundX API Key**, which you can find in your [GroundX account](https://dashboard.groundx.ai/apikey).

You will also need a `projectId`, `groupId`, or `bucketId` for a project, group, or bucket that contains ingested content. This can also be found in the [GroundX dashboard](https://dashboard.groundx.ai/projects).

For this tutorial, you will also need an **OpenAI API Key**, which can be found in your [OpenAI account](https://platform.openai.com/account/api-keys).

Finally, you will need to install the OpenAI and GroundX SDKs, either in [TypeScript](https://github.com/groundxai/groundx-sdks/blob/main/sdks/typescript/README.md) or [Python](https://github.com/groundxai/groundx-sdks/blob/main/sdks/python/README.md), using the package manager of your choice. Here are examples using `pip` and `npm`.

:::code

```python
pip install groundx-python-sdk openai
```

```typescript
npm install groundx-typescript-sdk openai --save
```

:::

## Step 2: Initialize Your Clients

Initialize both OpenAI and GroundX clients with the appropriate API keys:

:::code

```python
groundx = Groundx(
    api_key=groundxKey,
)

openai.api_key = openaiKey
```

```typescript
const groundx = new Groundx({
    apiKey: groundxKey,
});

const openai = new OpenAI({
    apiKey: openaiKey,
});
```

:::

Replace `groundxKey` with your GroundX API key and `openaiKey` with your OpenAI key.

## Step 3: Search Your Content on GroundX

Next, you will submit a query to the GroundX Search API.  A request will look something like this:

:::code

```python
try:
    content_response = groundx.search.content(id=groundxId, search={"query": query})
    results = content_response.body["search"]
except ApiException as e:
    print("Exception when calling SearchApi.content: %s\n" % e)
```

```typescript
const result = await groundx.search.content({
    id: groundxId,
    search: {
      query: query
    },
});
if (!result || !result.status || result.status != 200 || !result.data || !result.data.search) {
    console.error(result);
    throw Error("GroundX request failed");
}
```

:::

Replace `groundxId` with your `projectId`, `groupId`, or `bucketId` and `query` with the query you want to use to search your content.

Your search results should look something like this:

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
                "score": <float_relevance_score_of_result>,
                "sourceUrl": "<source_document_url>",
                "text":  "<text_of_result>"
            }
        ]
    }
}
```

## Step 4: Curate the Search Results

Once you have the results from your GroundX search, you will want to curate the relevant content to send to OpenAI for completion. You will need to be cognizant of the token limits for OpenAI models and reserve space for the completion, since the token limits apply to the combined total of tokens used for the request and completion.

Here is an example of what that could look like:

:::code

```python
llmText = ""
for r in results["results"]:
    if "text" in r and len(r["text"]) > 0:
        if len(llmText) + len(r["text"]) > maxInstructCharacters:
            break
        elif len(llmText) > 0:
            llmText += "\n"
        llmText += r["text"]
```

```typescript
let llmText = "";
result.data.search.results.forEach((r) => {
    if (r["text"] && r["text"].length > 0) {
        if (llmText.length + r["text"].length > maxInstructCharacters) {
            return;
        } else if (llmText.length > 0) {
            llmText += "\n";
        }
        llmText += r["text"];
    }
});
```

:::

In this example, `maxInstructCharacters` serves to limit the size of the request to conform to the token limits of OpenAI models. Reference the OpenAI documentation for the most current model token limits. Keep in mind that a token is roughly equivalent to 3.5 characters and that token limits apply to the combined size of the request and completion response.

## Step 5: Submit a Completion Request to OpenAI

Once you have relevant text for your request, you will need to combine the text with instructions and submit them to OpenAI.

Here is an example of what a completion instruction could look like:

```txt
You are a helpful virtual assistant that answers questions
using the content below. Your task is to create detailed answers
to the questions by combining your understanding of the world
with the content provided below. Do not share links.
```

Combine your completion instructions with your curated GroundX search results:

:::code

```python
completion = openai.ChatCompletion.create(
    model=openaiModel,
    messages=[
        {
            "role": "system",
            "content": """%s
===
%s
===
"""
            % (instruction, llmText),
        },
        {"role": "user", "content": query},
    ],
)
```

```typescript
const completion = await openai.chat.completions.create({
    model: openaiModel,
    messages: [
        {
            "role": "system",
            "content": `${instruction}
===
${llmText}
===
`
        },
        {"role": "user", "content": query},
    ],
});
```

:::

Replace `openaiModel` with your preferred model, `instruction` with your completion instructions, `llmText` with your curated GroundX search results, and `query` with your query.

Print the results of your request and you're done!

:::note
You can download the code for this tutorial from the GroundX code sample repository in [TypeScript](https://github.com/groundxai/code-samples/blob/master/typescript/chatGPT-completions/demo.js) (for javascript and NodeJS projects) or [Python](https://github.com/groundxai/code-samples/blob/master/python/chatGPT-completions/demo.py).
:::
