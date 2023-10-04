# ProjectApi

All URIs are relative to *https://api.groundx.ai/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bindBucket**](ProjectApi.md#bindBucket) | **POST** /v1/project/{projectId} | Bound project and bucket
[**create**](ProjectApi.md#create) | **POST** /v1/project | Create a project
[**delete**](ProjectApi.md#delete) | **DELETE** /v1/project/{projectId} | Delete an existing project
[**get**](ProjectApi.md#get) | **GET** /v1/project/{projectId} | Look up an existing project
[**list**](ProjectApi.md#list) | **GET** /v1/project | Look up existing projects
[**update**](ProjectApi.md#update) | **PUT** /v1/project/{projectId} | Update an existing project


# **bindBucket**

#### **POST** /v1/project/{projectId}

### Description
Bind a specific bucket to a project.

### Example


```typescript
import { Groundx } from "groundx-typescript-sdk";

const groundx = new Groundx({
  // Defining the base path is optional and defaults to https://api.groundx.ai/api
  // basePath: "https://api.groundx.ai/api",
  apiKey: "API_KEY",
});

const bindBucketResponse = await groundx.project.bindBucket({
  projectId: 1,
  project: {
    bucketId: 6122,
  },
});

console.log(bindBucketResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**projectBucketBinding** | **ProjectBucketBinding**| The bucket ID to bind to the project. |
**projectId** | **number** | The ID of the project to bind the bucket to. | (required)

### Return type

**object**


### HTTP response details
| Status code | Description |
|-------------|-------------|
**200** | Successful binding of project and bucket. |
**400** | Invalid request data. |
**401** | Unauthorized. |
**403** | Forbidden. |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **create**

#### **POST** /v1/project

### Description
This endpoint allows you to initialize a new project.

### Example


```typescript
import { Groundx } from "groundx-typescript-sdk";

const groundx = new Groundx({
  // Defining the base path is optional and defaults to https://api.groundx.ai/api
  // basePath: "https://api.groundx.ai/api",
  apiKey: "API_KEY",
});

const createResponse = await groundx.project.create({});

console.log(createResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**projectCreateRequest** | **ProjectCreateRequest**|  |

### Return type

**ProjectResponse**


### HTTP response details
| Status code | Description |
|-------------|-------------|
**200** | Successful creation of project |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **delete**

#### **DELETE** /v1/project/{projectId}

### Description
This endpoint allows you to delete your existing projects.

### Example


```typescript
import { Groundx } from "groundx-typescript-sdk";

const groundx = new Groundx({
  // Defining the base path is optional and defaults to https://api.groundx.ai/api
  // basePath: "https://api.groundx.ai/api",
  apiKey: "API_KEY",
});

const deleteResponse = await groundx.project.delete({
  projectId: "projectId_example",
});

console.log(deleteResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**projectId** | **string** | The ID of the project to delete. | (required)

### Return type

**ProjectDeleteResponse**


### HTTP response details
| Status code | Description |
|-------------|-------------|
**200** | Successful deletion of project |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **get**

#### **GET** /v1/project/{projectId}

### Description
This endpoint allows you to retrieve a specific project by projectId.

### Example


```typescript
import { Groundx } from "groundx-typescript-sdk";

const groundx = new Groundx({
  // Defining the base path is optional and defaults to https://api.groundx.ai/api
  // basePath: "https://api.groundx.ai/api",
  apiKey: "API_KEY",
});

const getResponse = await groundx.project.get({
  projectId: "projectId_example",
});

console.log(getResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**projectId** | **string** | The ID of the project to retrieve. | (required)

### Return type

**ProjectResponse**


### HTTP response details
| Status code | Description |
|-------------|-------------|
**200** | Successful retrieval of project |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **list**

#### **GET** /v1/project

### Description
This endpoint allows you to retrieve your existing projects.

### Example


```typescript
import { Groundx } from "groundx-typescript-sdk";

const groundx = new Groundx({
  // Defining the base path is optional and defaults to https://api.groundx.ai/api
  // basePath: "https://api.groundx.ai/api",
  apiKey: "API_KEY",
});

const listResponse = await groundx.project.list();

console.log(listResponse);
```


### Parameters

This endpoint does not need any parameter.

### Return type

**ProjectListResponse**


### HTTP response details
| Status code | Description |
|-------------|-------------|
**200** | Successful retrieval of projects |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **update**

#### **PUT** /v1/project/{projectId}

### Description
This endpoint allows you to update an existing project.

### Example


```typescript
import { Groundx } from "groundx-typescript-sdk";

const groundx = new Groundx({
  // Defining the base path is optional and defaults to https://api.groundx.ai/api
  // basePath: "https://api.groundx.ai/api",
  apiKey: "API_KEY",
});

const updateResponse = await groundx.project.update({
  projectId: "projectId_example",
});

console.log(updateResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**projectUpdateRequest** | **ProjectUpdateRequest**|  |
**projectId** | **string** | The ID of the project to update. | (required)

### Return type

**ProjectResponse**


### HTTP response details
| Status code | Description |
|-------------|-------------|
**200** | Successful update of project |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


