# SearchApi

All URIs are relative to *https://api.groundx.ai/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**content**](SearchApi.md#content) | **POST** /v1/search/{projectId} | Perform a search query of your content


# **content**

#### **POST** /v1/search/{projectId}

### Description
Search and retrieve relevant content from a project with projectId.

### Example


```typescript
import { Groundx } from "groundx-typescript-sdk";

const groundx = new Groundx({
  // Defining the base path is optional and defaults to https://api.groundx.ai/api
  // basePath: "https://api.groundx.ai/api",
  apiKey: "API_KEY",
});

const contentResponse = await groundx.search.content({
  projectId: "projectId_example",
  n: 20,
});

console.log(contentResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**searchRequest** | **SearchRequest**|  |
**projectId** | **string** | The ID of the project to search within. | (required)
**n** | **number** | Number of results | (optional)

### Return type

**SearchResponse**


### HTTP response details
| Status code | Description |
|-------------|-------------|
**200** | Search query success |
**400** | Invalid request data |
**401** | Permission denied |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


