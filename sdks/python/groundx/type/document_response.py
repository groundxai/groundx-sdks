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

from groundx.type.document_response_document import DocumentResponseDocument

class RequiredDocumentResponse(TypedDict):
    pass

class OptionalDocumentResponse(TypedDict, total=False):
    document: DocumentResponseDocument

class DocumentResponse(RequiredDocumentResponse, OptionalDocumentResponse):
    pass
