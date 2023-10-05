# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from groundx.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    V1_APIKEY = "/v1/apikey"
    V1_PROJECT_PROJECT_ID = "/v1/project/{projectId}"
    V1_PROJECT = "/v1/project"
    V1_BUCKET_BUCKET_ID = "/v1/bucket/{bucketId}"
    V1_BUCKET = "/v1/bucket"
    V1_INGEST_DOCUMENT_DOCUMENT_ID = "/v1/ingest/document/{documentId}"
    V1_INGEST_DOCUMENTS_REMOTE = "/v1/ingest/documents/remote"
    V1_INGEST_DOCUMENTS_LOCAL = "/v1/ingest/documents/local"
    V1_INGEST_DOCUMENTS = "/v1/ingest/documents"
    V1_INGEST_DOCUMENTS_ID = "/v1/ingest/documents/{id}"
    V1_INGEST_PROCESS_ID = "/v1/ingest/{processId}"
    V1_SEARCH_ID = "/v1/search/{id}"
