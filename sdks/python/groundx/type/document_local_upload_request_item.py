# coding: utf-8

"""
    GroundX API

    Ground Your RAG Apps in Fact not Fiction

    The version of the OpenAPI document: 1.0.0
    Contact: support@groundx.ai
    Created by: https://www.groundx.ai/
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal

from groundx.type.document_local_upload_request_item_metadata import DocumentLocalUploadRequestItemMetadata
from groundx.type.document_type import DocumentType

class RequiredDocumentLocalUploadRequestItem(TypedDict):
    # The actual file being uploaded.
    blob: typing.IO

    metadata: DocumentLocalUploadRequestItemMetadata

class OptionalDocumentLocalUploadRequestItem(TypedDict, total=False):
    pass

class DocumentLocalUploadRequestItem(RequiredDocumentLocalUploadRequestItem, OptionalDocumentLocalUploadRequestItem):
    pass
