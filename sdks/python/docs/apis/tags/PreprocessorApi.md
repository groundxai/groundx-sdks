# groundx.preprocessor

All URIs are relative to *https://api.groundx.ai/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete**](#delete) | **delete** /v1/preprocess | Delete Custom Pre-Processor
[**list**](#list) | **get** /v1/preprocess | Query pre-processors
[**setup**](#setup) | **post** /v1/preprocess | Setup Custom Pre-Processor

# **delete**

Deletes existing custom pre-processors that you own or manage.

### Example

```python
from pprint import pprint
from groundx import Groundx, ApiException

groundx = Groundx(
    # Defining the host is optional and defaults to https://api.groundx.ai/api
    # See configuration.py for a list of all supported configuration parameters.
    host="https://api.groundx.ai/api",
    # Configure API key authorization: ApiKeyAuth
    api_key="YOUR_API_KEY",
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    # api_key_prefix = {'ApiKeyAuth': 'Bearer'},
)

try:
    # Delete Custom Pre-Processor
    groundx.preprocessor.delete(
        preprocessors=["string_example"],  # optional
    )
except ApiException as e:
    print("Exception when calling PreprocessorApi.delete: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **list**

Look up existing pre-processors your account has access to, including those you have created yourself.

### Example

```python
from pprint import pprint
from groundx import Groundx, ApiException

groundx = Groundx(
    # Defining the host is optional and defaults to https://api.groundx.ai/api
    # See configuration.py for a list of all supported configuration parameters.
    host="https://api.groundx.ai/api",
    # Configure API key authorization: ApiKeyAuth
    api_key="YOUR_API_KEY",
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    # api_key_prefix = {'ApiKeyAuth': 'Bearer'},
)

try:
    # Query pre-processors
    list_response = groundx.preprocessor.list(
        preprocess=["preprocess_example"],  # required
    )
    pprint(list_response.body)
    pprint(list_response.body["preprocess"])
    pprint(list_response.headers)
    pprint(list_response.status)
    pprint(list_response.round_trip_time)
except ApiException as e:
    print("Exception when calling PreprocessorApi.list: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **setup**

Initializes a custom pre-processor that can be applied to your content and search queries.

### Example

```python
from pprint import pprint
from groundx import Groundx, ApiException

groundx = Groundx(
    # Defining the host is optional and defaults to https://api.groundx.ai/api
    # See configuration.py for a list of all supported configuration parameters.
    host="https://api.groundx.ai/api",
    # Configure API key authorization: ApiKeyAuth
    api_key="YOUR_API_KEY",
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    # api_key_prefix = {'ApiKeyAuth': 'Bearer'},
)

try:
    # Setup Custom Pre-Processor
    setup_response = groundx.preprocessor.setup(
        description="string_example",  # optional
        name="string_example",  # optional
        script=["string_example"],  # optional
    )
    pprint(setup_response.body)
    pprint(setup_response.body["preprocess"])
    pprint(setup_response.headers)
    pprint(setup_response.status)
    pprint(setup_response.round_trip_time)
except ApiException as e:
    print("Exception when calling PreprocessorApi.setup: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

