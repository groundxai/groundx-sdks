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

from groundx.type.document_response import DocumentResponse

class RequiredDocumentLookupResponse(TypedDict):
    pass

class OptionalDocumentLookupResponse(TypedDict, total=False):
    # The number of results returned in the current response
    count: int

    documents: typing.List[DocumentResponse]

    nextToken: str

    # The total number of results found
    total: int

class DocumentLookupResponse(RequiredDocumentLookupResponse, OptionalDocumentLookupResponse):
    pass
