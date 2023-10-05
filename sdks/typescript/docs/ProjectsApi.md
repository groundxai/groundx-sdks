# Groundx.projects

All URIs are relative to *https://api.groundx.ai/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get**](ProjectsApi.md#get) | **GET** /v1/project/{projectId} | Look up an existing project by its ID
[**list**](ProjectsApi.md#list) | **GET** /v1/project | Look up existing projects
[**update**](ProjectsApi.md#update) | **PUT** /v1/project/{projectId} | Update an existing project


# **Groundx.projects.get**

This endpoint allows you to retrieve a specific project by projectId.

### Example

```typescript
import { Groundx } from "groundx-typescript-sdk";

const groundx = new Groundx({
  // Defining the base path is optional and defaults to https://api.groundx.ai/api
  // basePath: "https://api.groundx.ai/api",
  apiKey: "API_KEY",
});

const getResponse = await groundx.projects.get({
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

# **Groundx.projects.list**

This endpoint allows you to retrieve your existing projects.

### Example

```typescript
import { Groundx } from "groundx-typescript-sdk";

const groundx = new Groundx({
  // Defining the base path is optional and defaults to https://api.groundx.ai/api
  // basePath: "https://api.groundx.ai/api",
  apiKey: "API_KEY",
});

const listResponse = await groundx.projects.list();

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

# **Groundx.projects.update**

This endpoint allows you to update an existing project.

### Example

```typescript
import { Groundx } from "groundx-typescript-sdk";

const groundx = new Groundx({
  // Defining the base path is optional and defaults to https://api.groundx.ai/api
  // basePath: "https://api.groundx.ai/api",
  apiKey: "API_KEY",
});

const updateResponse = await groundx.projects.update({
  projectId: "projectId_example",
  project: {
    name: "your_project_name",
  },
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


