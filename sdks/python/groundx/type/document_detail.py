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

from groundx.type.document_type import DocumentType
from groundx.type.processing_status import ProcessingStatus

class RequiredDocumentDetail(TypedDict):
    # Unique system generated ID for the document
    documentId: str


class OptionalDocumentDetail(TypedDict, total=False):
    bucketId: int

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

    # Document X-Ray results
    xrayUrl: str

class DocumentDetail(RequiredDocumentDetail, OptionalDocumentDetail):
    pass
