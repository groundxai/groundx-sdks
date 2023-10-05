# Groundx.document

All URIs are relative to *https://api.groundx.ai/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete**](DocumentApi.md#delete) | **DELETE** /v1/ingest/document/{documentId} | Delete documents
[**get**](DocumentApi.md#get) | **GET** /v1/ingest/document/{documentId} | Look up an existing document
[**getProcessingStatusByProcessId**](DocumentApi.md#getProcessingStatusByProcessId) | **GET** /v1/ingest/{processId} | Look up document processing status by processId
[**list**](DocumentApi.md#list) | **GET** /v1/ingest/documents | Look up all existing documents
[**lookup**](DocumentApi.md#lookup) | **GET** /v1/ingest/documents/{id} | Look up existing documents by processId, bucketId, or projectId
[**uploadLocal**](DocumentApi.md#uploadLocal) | **POST** /v1/ingest/documents/local | Upload local documents to GroundX
[**uploadRemote**](DocumentApi.md#uploadRemote) | **POST** /v1/ingest/documents/remote | Upload hosted documents to GroundX


# **Groundx.document.delete**


### Example

```typescript
import { Groundx } from "groundx-typescript-sdk";

const groundx = new Groundx({
  // Defining the base path is optional and defaults to https://api.groundx.ai/api
  // basePath: "https://api.groundx.ai/api",
  apiKey: "API_KEY",
});

const deleteResponse = await groundx.document.delete({
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
**200** | Documents successfully deleted |
**400** | Invalid document ID |
**401** | Permission denied |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **Groundx.document.get**


### Example

```typescript
import { Groundx } from "groundx-typescript-sdk";

const groundx = new Groundx({
  // Defining the base path is optional and defaults to https://api.groundx.ai/api
  // basePath: "https://api.groundx.ai/api",
  apiKey: "API_KEY",
});

const getResponse = await groundx.document.get({
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

# **Groundx.document.getProcessingStatusByProcessId**


### Example

```typescript
import { Groundx } from "groundx-typescript-sdk";

const groundx = new Groundx({
  // Defining the base path is optional and defaults to https://api.groundx.ai/api
  // basePath: "https://api.groundx.ai/api",
  apiKey: "API_KEY",
});

const getProcessingStatusByProcessIdResponse =
  await groundx.document.getProcessingStatusByProcessId({
    processId: "processId_example",
  });

console.log(getProcessingStatusByProcessIdResponse);
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

# **Groundx.document.list**


### Example

```typescript
import { Groundx } from "groundx-typescript-sdk";

const groundx = new Groundx({
  // Defining the base path is optional and defaults to https://api.groundx.ai/api
  // basePath: "https://api.groundx.ai/api",
  apiKey: "API_KEY",
});

const listResponse = await groundx.document.list();

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

# **Groundx.document.lookup**


### Example

```typescript
import { Groundx } from "groundx-typescript-sdk";

const groundx = new Groundx({
  // Defining the base path is optional and defaults to https://api.groundx.ai/api
  // basePath: "https://api.groundx.ai/api",
  apiKey: "API_KEY",
});

const lookupResponse = await groundx.document.lookup({
  id: "id_example",
});

console.log(lookupResponse);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**id** | **string** |  | (required)

### Return type

**DocumentLookupResponse**


### HTTP response details
| Status code | Description |
|-------------|-------------|
**200** | Look up success |
**401** | Permission denied |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **Groundx.document.uploadLocal**


### Example

```typescript
import { Groundx } from "groundx-typescript-sdk";

const groundx = new Groundx({
  // Defining the base path is optional and defaults to https://api.groundx.ai/api
  // basePath: "https://api.groundx.ai/api",
  apiKey: "API_KEY",
});

const uploadLocalResponse = await groundx.document.uploadLocal({
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

# **Groundx.document.uploadRemote**


### Example

```typescript
import { Groundx } from "groundx-typescript-sdk";

const groundx = new Groundx({
  // Defining the base path is optional and defaults to https://api.groundx.ai/api
  // basePath: "https://api.groundx.ai/api",
  apiKey: "API_KEY",
});

const uploadRemoteResponse = await groundx.document.uploadRemote({
  bucketId: 1234,
  sourceUrl: "https://my.source.url.com/file.txt",
  callbackData: "my_callback_data",
  callbackUrl: "https://my.callback.url.com",
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


