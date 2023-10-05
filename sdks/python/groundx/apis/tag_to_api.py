import typing_extensions

from groundx.apis.tags import TagValues
from groundx.apis.tags.document_api import DocumentApi
from groundx.apis.tags.project_api import ProjectApi
from groundx.apis.tags.bucket_api import BucketApi
from groundx.apis.tags.preprocessor_api import PreprocessorApi
from groundx.apis.tags.search_api import SearchApi
from groundx.apis.tags.api_key_management_api import APIKeyManagementApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.DOCUMENT: DocumentApi,
        TagValues.PROJECT: ProjectApi,
        TagValues.BUCKET: BucketApi,
        TagValues.PREPROCESSOR: PreprocessorApi,
        TagValues.SEARCH: SearchApi,
        TagValues.API_KEY_MANAGEMENT: APIKeyManagementApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.DOCUMENT: DocumentApi,
        TagValues.PROJECT: ProjectApi,
        TagValues.BUCKET: BucketApi,
        TagValues.PREPROCESSOR: PreprocessorApi,
        TagValues.SEARCH: SearchApi,
        TagValues.API_KEY_MANAGEMENT: APIKeyManagementApi,
    }
)
