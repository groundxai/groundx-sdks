# Integrating with ChatGPT

Welcome to this hands-on tutorial where we'll delve into Retrieval Augmented Generation (RAG) by merging the capabilities of GroundX's search results with OpenAI's ChatGPT.

In this tutorial, we will use Python to show you how to seamlessly extract relevant content from GroundX and then channel it into ChatGPT for enhanced, context-aware conversational experiences. This will not only broaden the knowledge base of the ChatGPT model but also leverage the precise search and retrieval capabilities of GroundX.

By the end of this tutorial, you'll possess the skills to create a more informed and enriched conversational agent that can draw upon your private data. Let's get started!

:::note
You can download the code from this tutorial from the [GroundX code sample repository](https://github.com/groundxai/code-samples/blob/master/python/chatGPT-completions/demo.py).
:::

## Step 1: Set Up Your Environment

You will need a **GroundX API Key**, which you can find in your [GroundX account](https://dashboard.groundx.ai/apikey).

You will also need a `projectId` for a project that contains ingested content. This can also be found in the [GroundX dashboard](https://dashboard.groundx.ai/projects).

For this tutorial, you will also need an **OpenAI API Key**, which can be found in your [OpenAI account](https://platform.openai.com/account/api-keys).

## Step 2: Search Your Content on GroundX

Next, you will submit a query to the GroundX Search API.  A request in python will look something like this:

:::code

```python
searchResult = requests.post(
    "https://api.groundx.ai/api/v1/search/%d" % groundxProjectId,
    headers={
        "Content-Type": "application/json",
        "X-API-Key": groundxKey,
    },
    data=json.dumps(
        {
            "search": {
                "query": query,
            }
        }
    ),
)
```

:::

Replace `groundxProjectId` with your `projectId`, `groundxKey` with your GroundX API Key and `query` with the query you want to use to search your content.

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

## Step 3: Curate the Search Results

Once you have the results from your GroundX search, you will want to curate the relevant content to send to OpenAI for completion. You will need to be cognizant of the token limits for OpenAI models and reserve space for the completion, since the token limits apply to the combined total of tokens used for the request and completion.

Here is an example of what that could look like in Python:

:::code

```python
llmText = ""
for resl in searchData["search"]["results"]:
    if "text" in resl and len(resl["text"]) > 0:
        if len(llmText) + len(resl["text"]) > maxInstructCharacters:
            break
        elif len(llmText) > 0:
            llmText += "\n"
        llmText += resl["text"]
```

:::

In this example, `maxInstructCharacters` serves to limit the size of the request to conform to the token limits of OpenAI models. Reference the OpenAI documentation for the most current model token limits. Keep in mind that a token is roughly equivalent to 3.5 characters and that token limits apply to the combined size of the request and completion response.

## Step 4: Submit a Completion Request to OpenAI

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

:::

Replace `openaiModel` with your preferred model, `instruction` with your completion instructions, `llmText` with your curated GroundX search results, and `query` with your query.

Print the results of your request and you're done!

:::note
You can download the sample code from this tutorial from the [GroundX code sample repository](https://github.com/groundxai/code-samples/blob/master/python/chatGPT-completions/demo.py).
:::
