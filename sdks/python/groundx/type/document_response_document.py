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


class RequiredDocumentResponseDocument(TypedDict):
    pass

class OptionalDocumentResponseDocument(TypedDict, total=False):
    bucketId: int

    documentId: str

    fileName: str

    fileSize: str

    fileType: str

    metadata: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    processId: str

    processedUrl: str

    sourceUrl: str

    status: str

    statusMessage: str

class DocumentResponseDocument(RequiredDocumentResponseDocument, OptionalDocumentResponseDocument):
    pass
