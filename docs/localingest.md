# Local Content Ingest
<iframe width="560" height="315" src="https://www.youtube.com/embed/_iMVoB5paeY?si=h0pvy_F4Qoe0-7EF" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

In this tutorial, we'll cover how to add or ingest your local files to GroundX.

GroundX’s true potential commences with the file ingestion process, one of its key advantages over other RAG solutions.

**With our proprietary ingest pipeline, your files undergo three critical processes in which GroundX:** 

- formats your content for LLM use, 
- parses content into intelligible text chunks, 
- and generates contextual metadata.

GroundX’s compatibility with a wide variety of file formats and its detection of document structures such as tables, forms, headers, footers and page numbers to help clear clutter and rewrite content to make it LLM-readable, is another one of its advantages over other RAG solutions that require you to previously turn your files into plain text.

**But before we begin, make sure you have the following information:**

- The ID of the GroundX bucket in which you wish to store your file.
- The path of the file you want to upload from your computer.
- The file name you wish to give your file once it's in the GroundX bucket.
- Indicate the file type to get the file correctly processed.

**Adding custom metadata**
Although not required because GroundX automatically generates metadata for your files, you can add custom metadata to take maximum advantage of GroundX's search capabilities, help maintain document context in the search query responses, and add tags or notes indicating instructions on how to handle the search results.

**What's Next**
- Set up your environment and declare your variables.
 - Make the API request to upload local documents and include the variables in the request body.

After making the request, you should receive a response with process ID and status. This response indicates that GroundX is uploading or ingesting your file into the indicated bucket.

Processing time depends on the size of your files. File size can be up to ten megabytes. After automatically ingesting your files, simplifying all of its complexity for you, GroundX has prepared your content for searchability and automated response generation for your queries.
