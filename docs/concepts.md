# Concepts

This page introduces some of the key concepts that form the foundation of GroundX's suite of APIs and services. Understanding these concepts will help you make the most of our APIs.

## Ingest

GroundX's Ingest API provides a powerful tool for uploading your content, supporting a variety of data types and formats. You can upload entire websites via a URL, documents, presentations, and raw text files. The API is designed to ensure secure transmission and centralized storage of your content, simplifying content management.

## Buckets

Buckets are a core feature of the GroundX APIs, aimed at the effective organization and storage of content. When documents or other forms of content are uploaded to the GroundX pipeline, they are processed and then stored in buckets. These buckets act as an organizational unit for content, making it easy to reuse and share buckets of content across different projects. The search APIs will search through the content in any buckets associated with a particular project.

## Projects

Projects in GroundX serve as the primary organizational unit, encompassing multiple buckets and the content they contain. When using the search APIs, you will search your buckets at the project level using the projectId. The Search APIs will scan all buckets and content associated with that specific project. In essence, while buckets organize content, projects consolidate these buckets for broader, unified access and searchability.

## Search

GroundX's Search API implements a proprietary combined vector and semantic approach, offering a level of search precision and relevance that is superior to traditional methods. The API allows for real-time application of pre-processors to better understand and match queries to relevant content.

## Authentication

To ensure secure access to its services, GroundX uses API Key based authentication. The API Key is provided to the users upon completion of a request form and is used in the request header (X-API-Key) for authentication.
