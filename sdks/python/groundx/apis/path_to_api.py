import typing_extensions

from groundx.paths import PathValues
from groundx.apis.paths.v1_apikey import V1Apikey
from groundx.apis.paths.v1_project_project_id import V1ProjectProjectId
from groundx.apis.paths.v1_project import V1Project
from groundx.apis.paths.v1_bucket_bucket_id import V1BucketBucketId
from groundx.apis.paths.v1_bucket import V1Bucket
from groundx.apis.paths.v1_ingest_document_document_id import V1IngestDocumentDocumentId
from groundx.apis.paths.v1_ingest_documents_remote import V1IngestDocumentsRemote
from groundx.apis.paths.v1_ingest_documents_local import V1IngestDocumentsLocal
from groundx.apis.paths.v1_ingest_documents import V1IngestDocuments
from groundx.apis.paths.v1_ingest_documents_id import V1IngestDocumentsId
from groundx.apis.paths.v1_ingest_process_id import V1IngestProcessId
from groundx.apis.paths.v1_search_id import V1SearchId

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.V1_APIKEY: V1Apikey,
        PathValues.V1_PROJECT_PROJECT_ID: V1ProjectProjectId,
        PathValues.V1_PROJECT: V1Project,
        PathValues.V1_BUCKET_BUCKET_ID: V1BucketBucketId,
        PathValues.V1_BUCKET: V1Bucket,
        PathValues.V1_INGEST_DOCUMENT_DOCUMENT_ID: V1IngestDocumentDocumentId,
        PathValues.V1_INGEST_DOCUMENTS_REMOTE: V1IngestDocumentsRemote,
        PathValues.V1_INGEST_DOCUMENTS_LOCAL: V1IngestDocumentsLocal,
        PathValues.V1_INGEST_DOCUMENTS: V1IngestDocuments,
        PathValues.V1_INGEST_DOCUMENTS_ID: V1IngestDocumentsId,
        PathValues.V1_INGEST_PROCESS_ID: V1IngestProcessId,
        PathValues.V1_SEARCH_ID: V1SearchId,
    }
)

path_to_api = PathToApi(
    {
        PathValues.V1_APIKEY: V1Apikey,
        PathValues.V1_PROJECT_PROJECT_ID: V1ProjectProjectId,
        PathValues.V1_PROJECT: V1Project,
        PathValues.V1_BUCKET_BUCKET_ID: V1BucketBucketId,
        PathValues.V1_BUCKET: V1Bucket,
        PathValues.V1_INGEST_DOCUMENT_DOCUMENT_ID: V1IngestDocumentDocumentId,
        PathValues.V1_INGEST_DOCUMENTS_REMOTE: V1IngestDocumentsRemote,
        PathValues.V1_INGEST_DOCUMENTS_LOCAL: V1IngestDocumentsLocal,
        PathValues.V1_INGEST_DOCUMENTS: V1IngestDocuments,
        PathValues.V1_INGEST_DOCUMENTS_ID: V1IngestDocumentsId,
        PathValues.V1_INGEST_PROCESS_ID: V1IngestProcessId,
        PathValues.V1_SEARCH_ID: V1SearchId,
    }
)
