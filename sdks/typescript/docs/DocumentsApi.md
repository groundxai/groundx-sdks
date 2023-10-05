# Groundx.documents

All URIs are relative to *https://api.groundx.ai/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete**](DocumentsApi.md#delete) | **DELETE** /v1/ingest/document/{documentId} | Delete a document
[**get**](DocumentsApi.md#get) | **GET** /v1/ingest/document/{documentId} | Look up an existing document by its ID
[**getProcessingStatusById**](DocumentsApi.md#getProcessingStatusById) | **GET** /v1/ingest/{processId} | Look up the processing status of documents for a given processId
[**list**](DocumentsApi.md#list) | **GET** /v1/ingest/documents | Look up all existing documents
[**lookup**](DocumentsApi.md#lookup) | **GET** /v1/ingest/documents/{id} | Look up existing documents by processId, bucketId, or projectId
[**uploadLocal**](DocumentsApi.md#uploadLocal) | **POST** /v1/ingest/documents/local | Upload local documents to GroundX
[**uploadRemote**](DocumentsApi.md#uploadRemote) | **POST** /v1/ingest/documents/remote | Upload hosted documents to GroundX


# **Groundx.documents.delete**


### Example

```typescript
import { Groundx } from "groundx-typescript-sdk";

const groundx = new Groundx({
  // Defining the base path is optional and defaults to https://api.groundx.ai/api
  // basePath: "https://api.groundx.ai/api",
  apiKey: "API_KEY",
});

const deleteResponse = await groundx.documents.delete({
  documentId: "documentId_example",
});

console.log(deleteResponse);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**documentId** | **string** |  | (required)

### Return type

**DocumentDeleteResponse**


### HTTP response details
| Status code | Description |
|-------------|-------------|
**200** | Document successfully deleted |
**400** | Invalid document ID |
**401** | Permission denied |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **Groundx.documents.get**


### Example

```typescript
import { Groundx } from "groundx-typescript-sdk";

const groundx = new Groundx({
  // Defining the base path is optional and defaults to https://api.groundx.ai/api
  // basePath: "https://api.groundx.ai/api",
  apiKey: "API_KEY",
});

const getResponse = await groundx.documents.get({
  documentId: "documentId_example",
});

console.log(getResponse);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**documentId** | **string** |  | (required)

### Return type

**DocumentResponse**


### HTTP response details
| Status code | Description |
|-------------|-------------|
**200** | Look up success |
**400** | Invalid document ID |
**401** | Permission denied |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **Groundx.documents.getProcessingStatusById**


### Example

```typescript
import { Groundx } from "groundx-typescript-sdk";

const groundx = new Groundx({
  // Defining the base path is optional and defaults to https://api.groundx.ai/api
  // basePath: "https://api.groundx.ai/api",
  apiKey: "API_KEY",
});

const getProcessingStatusByIdResponse =
  await groundx.documents.getProcessingStatusById({
    processId: "processId_example",
  });

console.log(getProcessingStatusByIdResponse);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**processId** | **string** |  | (required)

### Return type

**ProcessStatusResponse**


### HTTP response details
| Status code | Description |
|-------------|-------------|
**200** | Look up success |
**401** | Permission denied |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **Groundx.documents.list**


### Example

```typescript
import { Groundx } from "groundx-typescript-sdk";

const groundx = new Groundx({
  // Defining the base path is optional and defaults to https://api.groundx.ai/api
  // basePath: "https://api.groundx.ai/api",
  apiKey: "API_KEY",
});

const listResponse = await groundx.documents.list();

console.log(listResponse);
```

### Parameters

This endpoint does not need any parameter.

### Return type

**DocumentListResponse**


### HTTP response details
| Status code | Description |
|-------------|-------------|
**200** | Look up success |
**401** | Permission denied |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **Groundx.documents.lookup**


### Example

```typescript
import { Groundx } from "groundx-typescript-sdk";

const groundx = new Groundx({
  // Defining the base path is optional and defaults to https://api.groundx.ai/api
  // basePath: "https://api.groundx.ai/api",
  apiKey: "API_KEY",
});

const lookupResponse = await groundx.documents.lookup({
  id: 1,
});

console.log(lookupResponse);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**id** | **number** |  | (required)

### Return type

**DocumentLookupResponse**


### HTTP response details
| Status code | Description |
|-------------|-------------|
**200** | Look up success |
**401** | Permission denied |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **Groundx.documents.uploadLocal**


### Example

```typescript
import { Groundx } from "groundx-typescript-sdk";

const groundx = new Groundx({
  // Defining the base path is optional and defaults to https://api.groundx.ai/api
  // basePath: "https://api.groundx.ai/api",
  apiKey: "API_KEY",
});

const uploadLocalResponse = await groundx.documents.uploadLocal({
  blob: [open("/path/to/file", "rb")],
  metadata: {
    bucketId: 1234,
    fileName: "my_file.txt",
    fileType: "txt",
    callbackData: "my_callback_data",
    callbackUrl: "https://my.callback.url.com",
  },
});

console.log(uploadLocalResponse);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**blob** | **Array<Uint8Array | File>** |  | (required)
**metadata** | **DocumentLocalUploadRequestMetadata** |  | (required)

### Return type

**IngestResponse**


### HTTP response details
| Status code | Description |
|-------------|-------------|
**200** | Documents successfully uploaded |
**400** | Invalid document type or source URL |
**401** | Permission denied |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **Groundx.documents.uploadRemote**


### Example

```typescript
import { Groundx } from "groundx-typescript-sdk";

const groundx = new Groundx({
  // Defining the base path is optional and defaults to https://api.groundx.ai/api
  // basePath: "https://api.groundx.ai/api",
  apiKey: "API_KEY",
});

const uploadRemoteResponse = await groundx.documents.uploadRemote({
  type: "txt",
});

console.log(uploadRemoteResponse);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**documentRemoteUploadRequest** | **DocumentRemoteUploadRequest**|  |

### Return type

**IngestResponse**


### HTTP response details
| Status code | Description |
|-------------|-------------|
**200** | Documents successfully uploaded |
**400** | Invalid document type or source URL |
**401** | Permission denied |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


