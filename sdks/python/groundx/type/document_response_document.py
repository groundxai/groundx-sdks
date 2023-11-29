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
from typing_extensions import TypedDict, Literal, TYPE_CHECKING

from groundx.type.document_type import DocumentType
from groundx.type.processing_status import ProcessingStatus

class RequiredDocumentResponseDocument(TypedDict):
    pass

class OptionalDocumentResponseDocument(TypedDict, total=False):
    bucketId: int

    # Unique system generated ID for the document
    documentId: str

    fileName: str

    # The file size of the file stored in GroundX
    fileSize: str

    fileType: DocumentType

    # Unique system generated ID for the ingest request
    processId: str

    searchData: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    # Source document URL
    sourceUrl: str

    status: ProcessingStatus

    statusMessage: str

class DocumentResponseDocument(RequiredDocumentResponseDocument, OptionalDocumentResponseDocument):
    pass
