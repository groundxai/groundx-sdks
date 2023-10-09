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

from groundx.type.document_type import DocumentType

class RequiredDocumentLocalUploadRequestItemMetadata(TypedDict):
    bucketId: int

    fileName: str

    fileType: DocumentType

class OptionalDocumentLocalUploadRequestItemMetadata(TypedDict, total=False):
    metadata: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    callbackData: str

    callbackUrl: str

class DocumentLocalUploadRequestItemMetadata(RequiredDocumentLocalUploadRequestItemMetadata, OptionalDocumentLocalUploadRequestItemMetadata):
    pass
