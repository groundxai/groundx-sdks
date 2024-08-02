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

from groundx.type.document_detail import DocumentDetail

class RequiredDocumentLookupResponse(TypedDict):
    pass

class OptionalDocumentLookupResponse(TypedDict, total=False):
    # The number of results returned in the current response
    count: int

    documents: typing.List[DocumentDetail]

    nextToken: str

    # The total number of results found
    total: int

class DocumentLookupResponse(RequiredDocumentLookupResponse, OptionalDocumentLookupResponse):
    pass
