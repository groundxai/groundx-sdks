# groundx-python-sdk

[![PyPI](https://img.shields.io/badge/PyPI-v1.1.0-blue)](https://pypi.org/project/groundx-python-sdk/1.1.0)

Ground Your RAG Apps in Fact not Fiction


## Requirements

Python >=3.7

## Installing

```sh
pip install groundx-python-sdk==1.1.0
```

## Getting Started

```python
from pprint import pprint
from groundx import Groundx, ApiException

groundx = Groundx(
    api_key="YOUR_API_KEY",
)

try:
    # Get API keys
    list_response = groundx.api_key_management.list()
    pprint(list_response.body)
    pprint(list_response.body["api_keys"])
    pprint(list_response.headers)
    pprint(list_response.status)
    pprint(list_response.round_trip_time)
except ApiException as e:
    print("Exception when calling APIKeyManagementApi.list: %s\n" % e)
    pprint(e.body)
    if e.status == 405:
        pprint(e.body["message"])
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Async

`async` support is available by prepending `a` to any method.

```python
import asyncio
from pprint import pprint
from groundx import Groundx, ApiException

groundx = Groundx(
    api_key="YOUR_API_KEY",
)


async def main():
    try:
        # Get API keys
        list_response = await groundx.api_key_management.alist()
        pprint(list_response.body)
        pprint(list_response.body["api_keys"])
        pprint(list_response.headers)
        pprint(list_response.status)
        pprint(list_response.round_trip_time)
    except ApiException as e:
        print("Exception when calling APIKeyManagementApi.list: %s\n" % e)
        pprint(e.body)
        if e.status == 405:
            pprint(e.body["message"])
        pprint(e.headers)
        pprint(e.status)
        pprint(e.reason)
        pprint(e.round_trip_time)


asyncio.run(main())
```


## Documentation for API Endpoints

All URIs are relative to *https://api.groundx.ai/api*

Tag | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*API Key Management* | [**list**](docs/apis/tags/APIKeyManagementApi.md#list) | **GET** /v1/apikey | Get API keys
*Bucket* | [**create**](docs/apis/tags/BucketApi.md#create) | **POST** /v1/bucket | Create a bucket
*Bucket* | [**delete**](docs/apis/tags/BucketApi.md#delete) | **DELETE** /v1/bucket/{bucketId} | Delete an existing bucket
*Bucket* | [**get**](docs/apis/tags/BucketApi.md#get) | **GET** /v1/bucket/{bucketId} | Look up an existing bucket
*Bucket* | [**list**](docs/apis/tags/BucketApi.md#list) | **GET** /v1/bucket | Look up existing buckets
*Bucket* | [**update**](docs/apis/tags/BucketApi.md#update) | **PUT** /v1/bucket/{bucketId} | Update an existing bucket
*Document* | [**delete**](docs/apis/tags/DocumentApi.md#delete) | **DELETE** /v1/ingest/document/{documentId} | Delete documents
*Document* | [**get**](docs/apis/tags/DocumentApi.md#get) | **GET** /v1/ingest/document/{documentId} | Look up an existing document
*Document* | [**get_processing_status_by_id**](docs/apis/tags/DocumentApi.md#get_processing_status_by_id) | **GET** /v1/ingest/{processId} | Look up document processing status by processId
*Document* | [**list**](docs/apis/tags/DocumentApi.md#list) | **GET** /v1/ingest/documents | Look up all existing documents
*Document* | [**lookup**](docs/apis/tags/DocumentApi.md#lookup) | **GET** /v1/ingest/documents/{id} | Look up existing documents by processId, bucketId, or projectId
*Document* | [**upload_local**](docs/apis/tags/DocumentApi.md#upload_local) | **POST** /v1/ingest/documents/local | Upload local documents to GroundX
*Document* | [**upload_remote**](docs/apis/tags/DocumentApi.md#upload_remote) | **POST** /v1/ingest/documents/remote | Upload hosted documents to GroundX
*Preprocessor* | [**delete**](docs/apis/tags/PreprocessorApi.md#delete) | **DELETE** /v1/preprocess | Delete Custom Pre-Processor
*Preprocessor* | [**list**](docs/apis/tags/PreprocessorApi.md#list) | **GET** /v1/preprocess | Query pre-processors
*Preprocessor* | [**setup**](docs/apis/tags/PreprocessorApi.md#setup) | **POST** /v1/preprocess | Setup Custom Pre-Processor
*Project* | [**bind_bucket**](docs/apis/tags/ProjectApi.md#bind_bucket) | **POST** /v1/project/{projectId} | Add an existing bucket to a project
*Project* | [**create**](docs/apis/tags/ProjectApi.md#create) | **POST** /v1/project | Create a project
*Project* | [**delete**](docs/apis/tags/ProjectApi.md#delete) | **DELETE** /v1/project/{projectId} | Delete an existing project
*Project* | [**get**](docs/apis/tags/ProjectApi.md#get) | **GET** /v1/project/{projectId} | Look up an existing project
*Project* | [**list**](docs/apis/tags/ProjectApi.md#list) | **GET** /v1/project | Look up existing projects
*Project* | [**update**](docs/apis/tags/ProjectApi.md#update) | **PUT** /v1/project/{projectId} | Update an existing project
*Search* | [**content**](docs/apis/tags/SearchApi.md#content) | **POST** /v1/search/{id} | Perform a search query of your content


## Author
This Python package is automatically generated by [Konfig](https://konfigthis.com)
