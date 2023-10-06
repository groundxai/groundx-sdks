# groundx.api_keys

All URIs are relative to *https://api.groundx.ai/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list**](#list) | **get** /v1/apikey | Get API keys

# **list**

Retrieve the API keys for your account.

### Example

```python
from pprint import pprint
from groundx import Groundx, ApiException

groundx = Groundx(
    api_key="YOUR_API_KEY",
)

try:
    # Get API keys
    list_response = groundx.api_keys.list()
    pprint(list_response.body)
    pprint(list_response.body["api_keys"])
    pprint(list_response.headers)
    pprint(list_response.status)
    pprint(list_response.round_trip_time)
except ApiException as e:
    print("Exception when calling APIKeysApi.list: %s\n" % e)
    pprint(e.body)
    if e.status == 405:
        pprint(e.body["message"])
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)
