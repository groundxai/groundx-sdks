import typing_extensions

from groundx.apis.tags import TagValues
from groundx.apis.tags.documents_api import DocumentsApi
from groundx.apis.tags.projects_api import ProjectsApi
from groundx.apis.tags.buckets_api import BucketsApi
from groundx.apis.tags.search_api import SearchApi
from groundx.apis.tags.api_keys_api import APIKeysApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.DOCUMENTS: DocumentsApi,
        TagValues.PROJECTS: ProjectsApi,
        TagValues.BUCKETS: BucketsApi,
        TagValues.SEARCH: SearchApi,
        TagValues.API_KEYS: APIKeysApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.DOCUMENTS: DocumentsApi,
        TagValues.PROJECTS: ProjectsApi,
        TagValues.BUCKETS: BucketsApi,
        TagValues.SEARCH: SearchApi,
        TagValues.API_KEYS: APIKeysApi,
    }
)
