import typing_extensions

from groundx.paths import PathValues
from groundx.apis.paths.v1_ingest_documents_remote import V1IngestDocumentsRemote
from groundx.apis.paths.v1_ingest_documents_local import V1IngestDocumentsLocal
from groundx.apis.paths.v1_ingest_documents_website import V1IngestDocumentsWebsite
from groundx.apis.paths.v1_ingest_process_id import V1IngestProcessId
from groundx.apis.paths.v1_ingest_documents_id import V1IngestDocumentsId
from groundx.apis.paths.v1_ingest_documents import V1IngestDocuments
from groundx.apis.paths.v1_ingest_document_document_id import V1IngestDocumentDocumentId
from groundx.apis.paths.v1_search_id import V1SearchId
from groundx.apis.paths.v1_search_documents import V1SearchDocuments
from groundx.apis.paths.v1_bucket import V1Bucket
from groundx.apis.paths.v1_bucket_bucket_id import V1BucketBucketId
from groundx.apis.paths.v1_group import V1Group
from groundx.apis.paths.v1_group_group_id import V1GroupGroupId
from groundx.apis.paths.v1_group_group_id_bucket_bucket_id import V1GroupGroupIdBucketBucketId
from groundx.apis.paths.v1_customer import V1Customer
from groundx.apis.paths.v1_health import V1Health
from groundx.apis.paths.v1_health_service import V1HealthService

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.V1_INGEST_DOCUMENTS_REMOTE: V1IngestDocumentsRemote,
        PathValues.V1_INGEST_DOCUMENTS_LOCAL: V1IngestDocumentsLocal,
        PathValues.V1_INGEST_DOCUMENTS_WEBSITE: V1IngestDocumentsWebsite,
        PathValues.V1_INGEST_PROCESS_ID: V1IngestProcessId,
        PathValues.V1_INGEST_DOCUMENTS_ID: V1IngestDocumentsId,
        PathValues.V1_INGEST_DOCUMENTS: V1IngestDocuments,
        PathValues.V1_INGEST_DOCUMENT_DOCUMENT_ID: V1IngestDocumentDocumentId,
        PathValues.V1_SEARCH_ID: V1SearchId,
        PathValues.V1_SEARCH_DOCUMENTS: V1SearchDocuments,
        PathValues.V1_BUCKET: V1Bucket,
        PathValues.V1_BUCKET_BUCKET_ID: V1BucketBucketId,
        PathValues.V1_GROUP: V1Group,
        PathValues.V1_GROUP_GROUP_ID: V1GroupGroupId,
        PathValues.V1_GROUP_GROUP_ID_BUCKET_BUCKET_ID: V1GroupGroupIdBucketBucketId,
        PathValues.V1_CUSTOMER: V1Customer,
        PathValues.V1_HEALTH: V1Health,
        PathValues.V1_HEALTH_SERVICE: V1HealthService,
    }
)

path_to_api = PathToApi(
    {
        PathValues.V1_INGEST_DOCUMENTS_REMOTE: V1IngestDocumentsRemote,
        PathValues.V1_INGEST_DOCUMENTS_LOCAL: V1IngestDocumentsLocal,
        PathValues.V1_INGEST_DOCUMENTS_WEBSITE: V1IngestDocumentsWebsite,
        PathValues.V1_INGEST_PROCESS_ID: V1IngestProcessId,
        PathValues.V1_INGEST_DOCUMENTS_ID: V1IngestDocumentsId,
        PathValues.V1_INGEST_DOCUMENTS: V1IngestDocuments,
        PathValues.V1_INGEST_DOCUMENT_DOCUMENT_ID: V1IngestDocumentDocumentId,
        PathValues.V1_SEARCH_ID: V1SearchId,
        PathValues.V1_SEARCH_DOCUMENTS: V1SearchDocuments,
        PathValues.V1_BUCKET: V1Bucket,
        PathValues.V1_BUCKET_BUCKET_ID: V1BucketBucketId,
        PathValues.V1_GROUP: V1Group,
        PathValues.V1_GROUP_GROUP_ID: V1GroupGroupId,
        PathValues.V1_GROUP_GROUP_ID_BUCKET_BUCKET_ID: V1GroupGroupIdBucketBucketId,
        PathValues.V1_CUSTOMER: V1Customer,
        PathValues.V1_HEALTH: V1Health,
        PathValues.V1_HEALTH_SERVICE: V1HealthService,
    }
)
