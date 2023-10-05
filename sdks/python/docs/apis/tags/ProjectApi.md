# groundx.project

All URIs are relative to *https://api.groundx.ai/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bind_bucket**](#bind_bucket) | **post** /v1/project/{projectId} | Bound project and bucket
[**create**](#create) | **post** /v1/project | Create a project
[**delete**](#delete) | **delete** /v1/project/{projectId} | Delete an existing project
[**get**](#get) | **get** /v1/project/{projectId} | Look up an existing project
[**list**](#list) | **get** /v1/project | Look up existing projects
[**update**](#update) | **put** /v1/project/{projectId} | Update an existing project

# **bind_bucket**

Bind a specific bucket to a project.

### Example

```python
from pprint import pprint
from groundx import Groundx, ApiException

groundx = Groundx(
    api_key="YOUR_API_KEY",
)

try:
    # Bound project and bucket
    bind_bucket_response = groundx.project.bind_bucket(
        project={
            "bucket_id": 6122,
        },  # required
        project_id=1,  # required
    )
    pprint(bind_bucket_response.headers)
    pprint(bind_bucket_response.status)
    pprint(bind_bucket_response.round_trip_time)
except ApiException as e:
    print("Exception when calling ProjectApi.bind_bucket: %s\n" % e)
    pprint(e.body)
    if e.status == 400:
        pprint(e.body["message"])
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create**

This endpoint allows you to initialize a new project.

### Example

```python
from pprint import pprint
from groundx import Groundx, ApiException

groundx = Groundx(
    api_key="YOUR_API_KEY",
)

try:
    # Create a project
    create_response = groundx.project.create(
        project={
            "name": "your_project_name",
        },  # optional
    )
    pprint(create_response.body)
    pprint(create_response.body["project"])
    pprint(create_response.headers)
    pprint(create_response.status)
    pprint(create_response.round_trip_time)
except ApiException as e:
    print("Exception when calling ProjectApi.create: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete**

This endpoint allows you to delete your existing projects.

### Example

```python
from pprint import pprint
from groundx import Groundx, ApiException

groundx = Groundx(
    api_key="YOUR_API_KEY",
)

try:
    # Delete an existing project
    delete_response = groundx.project.delete(
        project_id="projectId_example",  # required
    )
    pprint(delete_response.body)
    pprint(delete_response.body["message"])
    pprint(delete_response.headers)
    pprint(delete_response.status)
    pprint(delete_response.round_trip_time)
except ApiException as e:
    print("Exception when calling ProjectApi.delete: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get**

This endpoint allows you to retrieve a specific project by projectId.

### Example

```python
from pprint import pprint
from groundx import Groundx, ApiException

groundx = Groundx(
    api_key="YOUR_API_KEY",
)

try:
    # Look up an existing project
    get_response = groundx.project.get(
        project_id="projectId_example",  # required
    )
    pprint(get_response.body)
    pprint(get_response.body["project"])
    pprint(get_response.headers)
    pprint(get_response.status)
    pprint(get_response.round_trip_time)
except ApiException as e:
    print("Exception when calling ProjectApi.get: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **list**

This endpoint allows you to retrieve your existing projects.

### Example

```python
from pprint import pprint
from groundx import Groundx, ApiException

groundx = Groundx(
    api_key="YOUR_API_KEY",
)

try:
    # Look up existing projects
    list_response = groundx.project.list()
    pprint(list_response.body)
    pprint(list_response.body["projects"])
    pprint(list_response.headers)
    pprint(list_response.status)
    pprint(list_response.round_trip_time)
except ApiException as e:
    print("Exception when calling ProjectApi.list: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update**

This endpoint allows you to update an existing project.

### Example

```python
from pprint import pprint
from groundx import Groundx, ApiException

groundx = Groundx(
    api_key="YOUR_API_KEY",
)

try:
    # Update an existing project
    update_response = groundx.project.update(
        project_id="projectId_example",  # required
        project={
            "name": "your_project_name",
        },  # optional
    )
    pprint(update_response.body)
    pprint(update_response.body["project"])
    pprint(update_response.headers)
    pprint(update_response.status)
    pprint(update_response.round_trip_time)
except ApiException as e:
    print("Exception when calling ProjectApi.update: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

