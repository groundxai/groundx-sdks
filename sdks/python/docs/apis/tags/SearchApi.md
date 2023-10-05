# groundx.search

All URIs are relative to *https://api.groundx.ai/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**content**](#content) | **post** /v1/search/{projectId} | Perform a search query of your content

# **content**

Search and retrieve relevant content from a project with projectId.

### Example

```python
from pprint import pprint
from groundx import Groundx, ApiException

groundx = Groundx(
    api_key="YOUR_API_KEY",
)

try:
    # Perform a search query of your content
    content_response = groundx.search.content(
        project_id="projectId_example",  # required
        search={},  # optional
        n=20,  # optional
    )
    pprint(content_response.body)
    pprint(content_response.body["search"])
    pprint(content_response.headers)
    pprint(content_response.status)
    pprint(content_response.round_trip_time)
except ApiException as e:
    print("Exception when calling SearchApi.content: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

