# PreprocessorApi

All URIs are relative to *https://api.groundx.ai/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete**](PreprocessorApi.md#delete) | **DELETE** /v1/preprocess | Delete Custom Pre-Processor
[**list**](PreprocessorApi.md#list) | **GET** /v1/preprocess | Query pre-processors
[**setup**](PreprocessorApi.md#setup) | **POST** /v1/preprocess | Setup Custom Pre-Processor


# **delete**

#### **DELETE** /v1/preprocess

### Description
Deletes existing custom pre-processors that you own or manage.

### Example


```typescript
import { Groundx } from "groundx-typescript-sdk";

const groundx = new Groundx({
  // Defining the base path is optional and defaults to https://api.groundx.ai/api
  // basePath: "https://api.groundx.ai/api",
  apiKey: "API_KEY",
});

const deleteResponse = await groundx.preprocessor.delete({});

console.log(deleteResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**preprocessorDeleteRequest** | **PreprocessorDeleteRequest**|  |

### Return type

void (empty response body)


### HTTP response details
| Status code | Description |
|-------------|-------------|
**200** | Pre-processor successfully deleted |
**400** | Invalid script |
**401** | Permission denied |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **list**

#### **GET** /v1/preprocess

### Description
Look up existing pre-processors your account has access to, including those you have created yourself.

### Example


```typescript
import { Groundx } from "groundx-typescript-sdk";

const groundx = new Groundx({
  // Defining the base path is optional and defaults to https://api.groundx.ai/api
  // basePath: "https://api.groundx.ai/api",
  apiKey: "API_KEY",
});

const listResponse = await groundx.preprocessor.list({
  preprocess: ["preprocess_example"],
});

console.log(listResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**preprocess** | **Array<string>** | An array of preprocessor IDs | (required)

### Return type

**PreprocessorResponse**


### HTTP response details
| Status code | Description |
|-------------|-------------|
**200** | Look up success |
**400** | Invalid preprocessor_ids |
**401** | Permission denied |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **setup**

#### **POST** /v1/preprocess

### Description
Initializes a custom pre-processor that can be applied to your content and search queries.

### Example


```typescript
import { Groundx } from "groundx-typescript-sdk";

const groundx = new Groundx({
  // Defining the base path is optional and defaults to https://api.groundx.ai/api
  // basePath: "https://api.groundx.ai/api",
  apiKey: "API_KEY",
});

const setupResponse = await groundx.preprocessor.setup({});

console.log(setupResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**preprocessorSetupRequest** | **PreprocessorSetupRequest**|  |

### Return type

**PreprocessorSetupResponse**


### HTTP response details
| Status code | Description |
|-------------|-------------|
**200** | Pre-processor successfully setup |
**400** | Invalid script |
**401** | Permission denied |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


