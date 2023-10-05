# Groundx.bucket

All URIs are relative to *https://api.groundx.ai/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](BucketApi.md#create) | **POST** /v1/bucket | Create a bucket
[**delete**](BucketApi.md#delete) | **DELETE** /v1/bucket/{bucketId} | Delete an existing bucket
[**get**](BucketApi.md#get) | **GET** /v1/bucket/{bucketId} | Look up an existing bucket
[**list**](BucketApi.md#list) | **GET** /v1/bucket | Look up existing buckets
[**update**](BucketApi.md#update) | **PUT** /v1/bucket/{bucketId} | Update an existing bucket


# **create**

Create a new bucket for your content.

### Example

```typescript
import { Groundx } from "groundx-typescript-sdk";

const groundx = new Groundx({
  // Defining the base path is optional and defaults to https://api.groundx.ai/api
  // basePath: "https://api.groundx.ai/api",
  apiKey: "API_KEY",
});

const createResponse = await groundx.bucket.create({});

console.log(createResponse);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**bucketCreateRequest** | **BucketCreateRequest**|  |

### Return type

**BucketResponse**


### HTTP response details
| Status code | Description |
|-------------|-------------|
**200** | Bucket successfully created |
**400** | Invalid body parameter |
**401** | Permission denied |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **delete**

Deletes a bucket by bucketId.

### Example

```typescript
import { Groundx } from "groundx-typescript-sdk";

const groundx = new Groundx({
  // Defining the base path is optional and defaults to https://api.groundx.ai/api
  // basePath: "https://api.groundx.ai/api",
  apiKey: "API_KEY",
});

const deleteResponse = await groundx.bucket.delete({
  bucketId: 1,
});

console.log(deleteResponse);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**bucketId** | **number** | The ID of the bucket to delete. | (required)

### Return type

**BucketDeleteResponse**


### HTTP response details
| Status code | Description |
|-------------|-------------|
**200** | Bucket successfully deleted |
**400** | Invalid bucket ID |
**401** | Permission denied |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **get**

Look up a bucket by its bucketId.

### Example

```typescript
import { Groundx } from "groundx-typescript-sdk";

const groundx = new Groundx({
  // Defining the base path is optional and defaults to https://api.groundx.ai/api
  // basePath: "https://api.groundx.ai/api",
  apiKey: "API_KEY",
});

const getResponse = await groundx.bucket.get({
  bucketId: 1,
});

console.log(getResponse);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**bucketId** | **number** | The ID of the bucket to retrieve. | (required)

### Return type

**BucketResponse**


### HTTP response details
| Status code | Description |
|-------------|-------------|
**200** | Look up success |
**400** | Invalid bucket ID |
**401** | Permission denied |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **list**

Look up existing buckets associated with your account.

### Example

```typescript
import { Groundx } from "groundx-typescript-sdk";

const groundx = new Groundx({
  // Defining the base path is optional and defaults to https://api.groundx.ai/api
  // basePath: "https://api.groundx.ai/api",
  apiKey: "API_KEY",
});

const listResponse = await groundx.bucket.list();

console.log(listResponse);
```

### Parameters

This endpoint does not need any parameter.

### Return type

**BucketListResponse**


### HTTP response details
| Status code | Description |
|-------------|-------------|
**200** | Look up success |
**401** | Permission denied |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **update**

Update the configurations of an existing bucket.

### Example

```typescript
import { Groundx } from "groundx-typescript-sdk";

const groundx = new Groundx({
  // Defining the base path is optional and defaults to https://api.groundx.ai/api
  // basePath: "https://api.groundx.ai/api",
  apiKey: "API_KEY",
});

const updateResponse = await groundx.bucket.update({
  bucketId: 1,
});

console.log(updateResponse);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**bucketUpdateRequest** | **BucketUpdateRequest**|  |
**bucketId** | **number** | The ID of the bucket to update. | (required)

### Return type

**BucketResponse**


### HTTP response details
| Status code | Description |
|-------------|-------------|
**200** | Bucket successfully updated |
**400** | Invalid body parameter |
**401** | Permission denied |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


