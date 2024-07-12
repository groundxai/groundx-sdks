# X-Ray: Document Understanding

## Introduction
In this tutorial, we’ll explore the GroundX document ingestion pipeline.

What makes GroundX document ingestion unique?

**Under the hood, the GroundX document ingestion pipeline goes through the following process:**

- After you upload a document, the GroundX document ingestion pipeline uses an object detection model, fine tuned with millions of pages of documents, to identify the text, table, and figure elements within your document.

- Next, the text elements go through an advanced OCR extraction to extract the text from the page. Table and figure elements are clipped and stored for multimodal processing.

- Table, figure, and text elements go through dedicated pipelines for repair and reformatting. Text elements are cleaned, reformatted, and enhanced with additional information when necessary using an LLM, fine tuned for text repair. Table and figure elements are converted into formats that are more compatible with search and LLM completion, using a fine tuned multimodal LLM.

- Then, document and section metadata are generated, using an LLM fine tuned for text summarization, to preserve contextual information surrounding the table, figure, and text elements.

- The elements within your document are then grouped into "semantic objects", which contain the original extracted text or clipped visual elements, reformatted text for search and LLM completion, and document and section metadata.

- Semantic objects are stored in our search database for search retrievals.

## See it for yourself
It's very simple to see for yourself. You can [try out our X-Ray demo tool](https://dashboard.eyelevel.ai/xray), which will visualize what our document ingestion pipeline can do with your documents.

Or you can get started with our APIs by following these simple steps:

## Step 1: Upload a document

- [Upload a hosted file](https://documentation.groundx.ai/docs/ingest-remote-content)
- [Upload a local file](https://documentation.groundx.ai/docs/ingest-local-content)

The :api[Document_uploadRemote] and :api[Document_uploadLocal] endpoints return a response object indicating the status of the ingestion process. 

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

## Step 2: Get ingest status
To check the status of the ingestion process, use the request response and the :api[Document_getProcessingStatusById] endpoint. For example:

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

## Step 3: Get the processed document data
Once the document ingestion process has completed, you can use the `processId` to query for the document information with the :api[Document_lookup] endpoint.

You will receive a response similar to this one:

```json
// Successful lookup response
{
  "count": number, // Number of documents returned in response
  "documents": [
    {
      "documentId": "string", // Object ID of the document
      "fileName": "string", // Name you gave the document when it was uploaded
      "fileSize": "string", // Calculated size of your document
      "fileTokens": number, // Tokens generated and billed to your account for ingestion
      "bucketId": number, // ID of the bucket the document was uploaded to
      "processId": "string", // Object ID of the processing request
      "sourceUrl": "string", // Hosted URL for your document
      "status": "string", // "queued" | "processing" | "error" | "complete"
      "xrayUrl": "string" // Hosted URL for the document information generated during processing
    },
  ],
  "nextToken": "string", // A token that can be used to request the next set of results
  "total": number // Total number of documents found
}
```

The `xrayUrl` points to a JSON file containing the information generated about your document by the GroundX document ingestion pipeline. The structure of this information is [explained further below](#x-ray-document-data).

## X-Ray Document Data

The structure of the X-Ray document data looks something like this:

```json
// Successful lookup response
{
  "fileType": "string", // One of the supported file types, [as described here](https://documentation.groundx.ai/docs/file-types)
  "language": "string", // Language detected on the first page of your document during processing
  "fileKeywords": "string", // Auto-generated comma-delimited list of keywords describing your document
  "fileName": "string", // Name you gave the document when it was uploaded
  "fileSummary": "string", // Auto-generated document summary
  "documentPages": [ // Pages and metadata within the document
    {
      "chunks": [ // Semantic objects found on page, some semantic objects are spread across multiple pages
        {
          "boundingBoxes": [ // Boxes containing semantic object elements
            {
              "bottomRightX": number, // X coordinate for lower right corner of semantic object element
              "bottomRightY": number, // Y coordinate for lower right corner of semantic object element
              "pageNumber": number, // Number of page for semantic object element, starting at 1
              "topLeftX": number, // X coordinate for upper left corner of semantic object element
              "topLeftY": number, // Y coordinate for upper left corner of semantic object element
            }
          ],
          "chunk": number, // Unique integer ID for the semantic object
          "contentType": [ // Types of elements represented within the semantic object
            "string" // "table" | "figure" | "paragraph"
          ],
          "json": [ // Element text, reformatted into JSON format, for "table" and "figure" elements only
            "object" // Auto-generated JSON object describing a section of the information within the "table" or "figure"
          ],
          "multimodalUrl": "string", // Element image, for multimodal processing "table" and "figure" elements only
          "narrative": [ // Element text, reformatted into narrative format, for "table" and "figure" elements only
            "string" // Auto-generated narrative description of a section of the information within the "table" or "figure"
          ],
          "pageNumbers": [ // Pages where semantic object exists
            number // Number of page where semantic object exists
          ],
          "sectionSummary": "string", // Auto-generated section summary for the document section containing the semantic object
          "suggestedText": "string", // Element text, reformatted for LLM completion
          "text": "string" // Element text, extracted and unprocessed
        }
      ],
      "height": number, // Pixel height of page image
      "pageNumber": number, // Number of page, starting at 1
      "pageUrl": "string", // Hosted URL for the page image
      "width": number // Pixel width of page image
    }
  ],
  "sourceUrl": "string", // Hosted URL for your document
}
```