# Welcome

GroundX is an API framework that helps you rapidly build LLM-powered applications with private data where your answers are grounded in fact not fiction.

We’ve been building the GroundX platform alongside LLM providers like OpenAI, Google and Meta for more than three years and have worked hard to build a framework that will save you many hours of pain.

## Grounded Generation

Importantly, our APIs are designed to tackle one of the most difficult challenges of working with LLMs — their tendency to hallucinate when they don’t know the right answer.  

At its core, LLM hallucination is the result of poor search and retrieval or lack of appropriate content.

We call our approach to solving these problems grounded generation and it involves the following components:

- **Smart pre-processing** that accurately breaks down many documents and data types.
- **An automated ingest pipeline** that chunks, labels, classifies and clusters your data so an LLM has proper context when processing it.
- **A hallucination checking algorithm** that scores every LLM response for its fidelity to your corpus of data.

## Key Features

In addition to grounded generation, our core features are:

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

Discover the power of intelligent search with GroundX's Search API. Our proprietary combined vector and semantic approach ensures your search queries yield the most relevant results. With the added advantage of real-time pre-processing, the Search API provides an unrivaled level of understanding and matching queries to the right content.

## Secure Storage and Transmission

Security and privacy are paramount when building enterprise applications. First, we believe your data is your data. You or your customers own it, not us. Second, your uploaded data is encrypted at REST and encrypted in transmission to an LLM. We don’t train on your data, each corpus is stored in virtual isolation and we make it easy to control when your data is purged.

## What You Can Build

Our customers are building all kinds of amazing LLM-powered applications with GroundX APIs including customer service bots, personalized sales assistants, legal tools, advanced knowledge base search tools, live health applications and more. Let your imagination run wild and be sure to tell us what you’re cooking. We love to support the amazing applications built on GroundX.

## Getting Started

Before you dive in, you'll need an API key to authenticate your requests. To obtain your key, please [create an account](https://dashboard.groundx.ai/auth/register). Once you've done that, you're ready to start using our APIs.

In the following sections, you'll find detailed guides for each API, including how to authenticate, make requests, and what response formats to expect. Each guide is accompanied by examples to help you understand how to use the APIs effectively.

## Explore the APIs

In our documentation, you'll find detailed information about each API, including endpoints, request and response formats, and any required parameters. We provide code examples to assist you in integrating our APIs seamlessly into your projects.

We're continuously working to improve our service based on user feedback, so we appreciate any suggestions or insights you have regarding our APIs. If you have any questions or need assistance, don't hesitate to reach out to our support team.

Join us in our mission to unlock the power of knowledge. Let's make data more accessible, manageable, and valuable together. Get started with GroundX today!
