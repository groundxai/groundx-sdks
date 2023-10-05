# groundx.inventory

All URIs are relative to *https://api.groundx.ai/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add**](#add) | **post** /v1/inventory | adds an inventory item
[**search**](#search) | **get** /v1/inventory | searches inventory

# **add**

Adds an item to the system

### Example

```python
from pprint import pprint
from groundx import Groundx, ApiException

groundx = Groundx(
    api_key="YOUR_API_KEY",
)

try:
    # adds an inventory item
    groundx.inventory.add(
        id="d290f1ee-6c54-4b01-90e6-d701748f0851",  # required
        name="Widget Adapter",  # required
        release_date="2016-08-29T09:12:33.001Z",  # required
        manufacturer={
            "name": "ACME Corporation",
            "home_page": "https://www.acme-corp.com",
            "phone": "408-867-5309",
        },  # required
    )
except ApiException as e:
    print("Exception when calling InventoryApi.add: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **search**

By passing in the appropriate options, you can search for available inventory in the system 

### Example

```python
from pprint import pprint
from groundx import Groundx, ApiException

groundx = Groundx(
    api_key="YOUR_API_KEY",
)

try:
    # searches inventory
    search_response = groundx.inventory.search(
        search_string="string_example",  # optional
        skip=0,  # optional
        limit=0,  # optional
    )
    pprint(search_response.body)
    pprint(search_response.headers)
    pprint(search_response.status)
    pprint(search_response.round_trip_time)
except ApiException as e:
    print("Exception when calling InventoryApi.search: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

