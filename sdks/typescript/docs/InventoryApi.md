# Groundx.inventory

All URIs are relative to *https://api.groundx.ai/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add**](InventoryApi.md#add) | **POST** /v1/inventory | adds an inventory item
[**search**](InventoryApi.md#search) | **GET** /v1/inventory | searches inventory


# **add**

Adds an item to the system

### Example

```typescript
import { Groundx } from "groundx-typescript-sdk";

const groundx = new Groundx({
  // Defining the base path is optional and defaults to https://api.groundx.ai/api
  // basePath: "https://api.groundx.ai/api",
  apiKey: "API_KEY",
});

const addResponse = await groundx.inventory.add({
  id: "d290f1ee-6c54-4b01-90e6-d701748f0851",
  name: "Widget Adapter",
  releaseDate: "2016-08-29T09:12:33.001Z",
  manufacturer: {
    name: "ACME Corporation",
    homePage: "https://www.acme-corp.com",
    phone: "408-867-5309",
  },
});

console.log(addResponse);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**inventoryItem** | **InventoryItem**| Inventory item to add |

### Return type

void (empty response body)


### HTTP response details
| Status code | Description |
|-------------|-------------|
**201** | item created |
**400** | invalid input, object invalid |
**409** | an existing item already exists |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **search**

By passing in the appropriate options, you can search for
available inventory in the system


### Example

```typescript
import { Groundx } from "groundx-typescript-sdk";

const groundx = new Groundx({
  // Defining the base path is optional and defaults to https://api.groundx.ai/api
  // basePath: "https://api.groundx.ai/api",
  apiKey: "API_KEY",
});

const searchResponse = await groundx.inventory.search({});

console.log(searchResponse);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**searchString** | **string** | pass an optional search string for looking up inventory | (optional)
**skip** | **number** | number of records to skip for pagination | (optional)
**limit** | **number** | maximum number of records to return | (optional)

### Return type

**Array<InventoryItem>**


### HTTP response details
| Status code | Description |
|-------------|-------------|
**200** | search results matching criteria |
**400** | bad input parameter |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


