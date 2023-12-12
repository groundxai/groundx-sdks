# Welcome

<iframe width="560" height="315" src="https://www.youtube.com/embed/SBZWj7qKtFA?si=neogiHQmE7i-8Uvz" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

GroundX APIs help you rapidly build RAG (retreieval augmented generation) applications that you can trust.

We’ve been building the GroundX platform alongside LLM providers like OpenAI, Google and Meta for more than two years and have worked hard to build a framework that will save you many hours of pain while providing the accurate, hallucination resistant answers you need. 

## Build Your First RAG App in 10 Minutes or Less

Whether you're new to RAG development or already deep in the practice, GroundX APIs are designed to save you time. We've bundled all the pieces you need into one seemless platform that just works:
- Proprietary ETL Engine (extract, transform, load) to process your documents
- Semantic Database
- Dynamic Chunker
- Powerful Content Search with Proprietary Re-Ranker
- Light Orchestrator
- Enterprise security with bank level encryption

If you're not familar with all of those terms, don't worry. We've removed the time, pain and expense of writing thousands of lines of code and integrating multiple platforms into just a few API calls. Your complex documents go in one side, LLM ready search retrievals come out the other with industry leading accuracy. Then call the LLM of your choice for completions. 

Some engineers have told us they are building RAG apps up to 10 times faster than with any other tools on the market.  

## Cutting Edge Accuracy

GroundX is also designed to tackle one of the most difficult challenges of working with LLMs — their tendency to make things up or hallucinate when they don’t know the right answer. 

To tackle hallucinations, we first have to understand what they are. Essentially, when LLMs run out of facts, they just make them up. They’re like the know-it-all at the party that should have shut up 30 minutes ago. The problem is much worse with RAG apps where the LLMs have never seen your data before.

The key here is to make sure the LLM understands your data when you send it for completion. We’ve found that 90% of hallucinations are data problems NOT prompt problems. And you can't prompt your way out of a data problem.

**GroundX solves these issues with a proprietary ingest pipeline for your data that:**
- Converts your documents, cleans the text and reformats it into LLM friendly data
- Dynamically chunks your content at natural break points that express full ideas
- Automatically creates contextual metadata for your chunks
- Automatically builds a knowledge graph to maintain entity relationships across documents (Coming Soon)

Under the hood, we’ve built a fine-tuned computer vision model for your docs and a pipeline of several LLMs to understand the layout of your documents, dynamically chunk and summarize your content and search your data. Give us your complex documents littered with tables, forms, headers, footers, index pages and other visual formatting that chokes LLMs and our pipeline returns clean, simple LLM-ready data. 

We also built a proprietary search engine that outperforms vector similarity, provides fuller retrievals and re-ranks each retrieved chunk for its adherence to the question.

**This all happens without writing a single line of code. Just ingest your content, search and complete. With GroundX you finally have RAG you can trust, made simple.** 


## Key Features

In addition to speed and accuracy, our core features are:

- **Effortless Content Upload**: Upload content from various sources like websites, documents, presentations, and raw text files in one centralized location with our Content Upload API.
- **Sophisticated Automated Pre-Processing**: Our ingestion pipeline will automatically clean and format your content for use with LLMs, generate valuable metadata, and improve search and retrieval performance.
- **Superior Search Capabilities**: Make the most of our Search API, employing a proprietary combined vector and semantic approach for accurate and relevant search results.
- **Secure Storage and Transmission**: Data is encrypted at rest and during transmission to an LLM. Each corpus is stored in virtual isolation.

## Effortless Content Upload

At GroundX, we understand the complexity of managing diverse content sources. That's why we've designed the Content Upload API, a comprehensive solution for uploading your data across multiple formats, including documents, presentations, raw text files, and even entire websites via a URL. The API ensures a secure transmission and storage of your content, simplifying your content management process with a centralized storage system

## Sophisticated Automated Pre-Processing

GroundX's pre-processing capabilities enable you to enhance your content's utility and value. Our ingestion pipeline will **automatically** clean your data, re-format your content for LLMs, and generate valuable metadata such as document, page, and section summaries. This preparation for interacting with an LLM significantly enhances the performance of search and retrieval tasks.

- **Clean your Data**: extraneous text, such as page and line numbers, page footers, and other non-essential text that hinders an LLMs ability to understand your content, is automatically removed
- **Re-Format for LLMs**: common document elements such as columns, tables, and forms are re-formatted for better search and retrieval performance and translated to a more appropriate style for LLM completions
- **Generate Metadata**: document, page, and section summaries are automatically generated to better preserve the context of your content

## Superior Search Capabilities

At GroundX, we've taken a fresh approach to search that's optimized for RAG applications. The results consistently outperform vector similarity (the industry standard). How does it work?

First, we're storing LLM friendly versions of your data in our database (explained above). That's vital for LLMs to be able to understand your content. Every retrieval contains the original text, automatically created metadata that summarizes the key elements of your chunks and an LLM-friendly rewrite of your chunks.

Then we pair a semantic search with a proprietary re-ranker that scores every retrieval for adherence to the question. And finally, we merge all of those components to creat a suggested retrieval that is tuned to send to LLMs for completion. 

It's the first search and retrieval engine built specifically for RAG and LLM apps.

## Secure Storage and Transmission

The GroundX team spent more than a decade at IBM building highly-trusted enterprise applications for millions of global users. We know how important security and privacy are to every enterprise and how much work goes into getting there. So we built enterprise security right into the platform.

First, we believe your data is your data. You or your customers own it, not us. Your uploaded data is always encrypted at rest and in transit. We don’t train LLMs on your data and the whole environment runs in a  virtual private cloud with one set of keys that you control. 

Today, this runs as a service we manage for you on AWS. Soon we'll have versions of our platform you can run on your own managed cloud. 

## What You Can Build

Our customers are building all kinds of amazing LLM-powered applications with GroundX APIs including customer service bots, personalized sales assistants, legal tools, advanced knowledge base search tools, health applications and more. Let your imagination run wild and be sure to tell us what you’re cooking. We love to support the amazing applications built on GroundX.

## Getting Started

Before you dive in, you'll need an API key to authenticate your requests. To obtain your key, please [create an account](https://dashboard.groundx.ai/auth/register). Once you've done that, you're ready to start using our APIs.

In the following sections, you'll find detailed guides for each API, including how to authenticate, make requests, and what response formats to expect. Each guide is accompanied by examples to help you understand how to use the APIs effectively.

## Explore the APIs

In our documentation, you'll find detailed information about each API, including endpoints, request and response formats, and any required parameters. We provide code examples to assist you in integrating our APIs seamlessly into your projects.

We're continuously working to improve our service based on user feedback, so we appreciate any suggestions or insights you have regarding our APIs. If you have any questions or need assistance, don't hesitate to reach out to our support team.

Join us in our mission to unlock the power of knowledge. Let's make data more accessible, manageable, and valuable together. Get started with GroundX today!