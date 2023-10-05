# Groundx.apiKeys

All URIs are relative to *https://api.groundx.ai/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list**](ApiKeysApi.md#list) | **GET** /v1/apikey | Get API keys


# **Groundx.apiKeys.list**

Retrieve the API keys for your account.

### Example

```typescript
import { Groundx } from "groundx-typescript-sdk";

const groundx = new Groundx({
  // Defining the base path is optional and defaults to https://api.groundx.ai/api
  // basePath: "https://api.groundx.ai/api",
  apiKey: "API_KEY",
});

const listResponse = await groundx.apiKeys.list();

console.log(listResponse);
```

### Parameters

This endpoint does not need any parameter.

### Return type

**ApiKeyManagementListResponse**


### HTTP response details
| Status code | Description |
|-------------|-------------|
**200** | Successful retrieval of API keys |
**401** | Unauthorized |
**403** | Forbidden |
**405** | Method Not Allowed |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


