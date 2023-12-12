# Remote Content Ingest
<iframe width="560" height="315" src="https://www.youtube.com/embed/KUeOKCiK2gw?si=vTpI-YLgE_iZPH7a" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

In this tutorial, we’ll go over how to add or ingest remote content into GroundX. This is the step where the magic begins. GroundX’s ingestion pipeline is much more than just simply extracting content from your files. 

**Through its unique ingestion pipeline, GroundX:**
- Formats your content for LLM use
- Parses content into intelligible text chunks
- And generates contextual metadata

Unlike other platforms, which require content to be processed to plain text before being uploaded, GroundX can automatically ingest a wide range of content types and properly handle complex objects such as tables, forms, headers, footers and columns which LLMs do not understand. 

**GroundX's fine-tuned computer vision model identifies the coordinates of these objects, extracts their content then converts them into LLM-readable formats.**

To add online files to GroundX, you simply need the following information: 
 
- BucketID: The ID of the GroundX bucket in which you will store your document. 
- SourceURL: The URL of the file you want to add to your GroundX bucket. 
  
**Metadata: Provide document context with custom metadata.** 
Although not required because GroundX automatically generates metadata for your files, you can add custom metadata to take maximum advantage of GroundX's search capabilities, help maintain document context in the search query responses, and add tags or notes indicating instructions on how to handle the search results.

Set up your environment and declare the variables for bucketId, sourceUrl, and metadata.

Now, simply make an API request to upload remote documents and include bucketId, sourceUrl, and metadata in the request body. After making the request, you should receive a response indicating processId and status. 

Processing time depends on the size of your files. File size can be up to 10 megabytes. After passing through the ingestion process, your content is consolidated for maximum searchability and query response.
