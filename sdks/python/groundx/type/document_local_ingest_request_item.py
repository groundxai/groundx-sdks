# coding: utf-8

"""
    GroundX APIs

    RAG Made Simple, Secure and Hallucination Free

    The version of the OpenAPI document: 1.3.26
    Contact: support@eyelevel.ai
    Created by: https://www.eyelevel.ai/
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING

from groundx.type.document_local_ingest_request_item_metadata import DocumentLocalIngestRequestItemMetadata

class RequiredDocumentLocalIngestRequestItem(TypedDict):
    # The actual file being ingested.
    blob: typing.IO

    metadata: DocumentLocalIngestRequestItemMetadata

class OptionalDocumentLocalIngestRequestItem(TypedDict, total=False):
    pass

class DocumentLocalIngestRequestItem(RequiredDocumentLocalIngestRequestItem, OptionalDocumentLocalIngestRequestItem):
    pass
