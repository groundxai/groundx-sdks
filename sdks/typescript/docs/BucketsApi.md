# Groundx.buckets

All URIs are relative to *https://api.groundx.ai/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get**](BucketsApi.md#get) | **GET** /v1/bucket/{bucketId} | Look up an existing bucket by its ID
[**list**](BucketsApi.md#list) | **GET** /v1/bucket | Look up existing buckets
[**update**](BucketsApi.md#update) | **PUT** /v1/bucket/{bucketId} | Update an existing bucket


# **Groundx.buckets.get**

Look up a bucket by its bucketId.

### Example

```typescript
import { Groundx } from "groundx-typescript-sdk";

const groundx = new Groundx({
  // Defining the base path is optional and defaults to https://api.groundx.ai/api
  // basePath: "https://api.groundx.ai/api",
  apiKey: "API_KEY",
});

const getResponse = await groundx.buckets.get({
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

# **Groundx.buckets.list**

Look up existing buckets associated with your account.

### Example

```typescript
import { Groundx } from "groundx-typescript-sdk";

const groundx = new Groundx({
  // Defining the base path is optional and defaults to https://api.groundx.ai/api
  // basePath: "https://api.groundx.ai/api",
  apiKey: "API_KEY",
});

const listResponse = await groundx.buckets.list();

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

# **Groundx.buckets.update**

Update the configurations of an existing bucket.

### Example

```typescript
import { Groundx } from "groundx-typescript-sdk";

const groundx = new Groundx({
  // Defining the base path is optional and defaults to https://api.groundx.ai/api
  // basePath: "https://api.groundx.ai/api",
  apiKey: "API_KEY",
});

const updateResponse = await groundx.buckets.update({
  bucketId: 1,
  bucket: {
    name: "your_bucket_name",
  },
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


