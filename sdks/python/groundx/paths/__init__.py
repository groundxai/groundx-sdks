# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from groundx.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    V1_INGEST_DOCUMENTS_REMOTE = "/v1/ingest/documents/remote"
    V1_INGEST_DOCUMENTS_LOCAL = "/v1/ingest/documents/local"
    V1_INGEST_DOCUMENTS_WEBSITE = "/v1/ingest/documents/website"
    V1_INGEST_PROCESS_ID = "/v1/ingest/{processId}"
    V1_INGEST_DOCUMENTS_ID = "/v1/ingest/documents/{id}"
    V1_INGEST_DOCUMENTS = "/v1/ingest/documents"
    V1_INGEST_DOCUMENT_DOCUMENT_ID = "/v1/ingest/document/{documentId}"
    V1_SEARCH_ID = "/v1/search/{id}"
    V1_SEARCH_DOCUMENTS = "/v1/search/documents"
    V1_BUCKET = "/v1/bucket"
    V1_BUCKET_BUCKET_ID = "/v1/bucket/{bucketId}"
    V1_GROUP = "/v1/group"
    V1_GROUP_GROUP_ID = "/v1/group/{groupId}"
    V1_GROUP_GROUP_ID_BUCKET_BUCKET_ID = "/v1/group/{groupId}/bucket/{bucketId}"
    V1_CUSTOMER = "/v1/customer"
    V1_HEALTH = "/v1/health"
    V1_HEALTH_SERVICE = "/v1/health/{service}"
