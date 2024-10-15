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

from groundx.type.search_documents_request_document_ids import SearchDocumentsRequestDocumentIds

class RequiredSearchDocumentsRequest(TypedDict):
    # The search query to be used to find relevant documentation.
    query: str

    documentIds: SearchDocumentsRequestDocumentIds


class OptionalSearchDocumentsRequest(TypedDict, total=False):
    # The minimum search relevance score required to include the result. By default, this is 10.0.
    relevance: typing.Union[int, float]

class SearchDocumentsRequest(RequiredSearchDocumentsRequest, OptionalSearchDocumentsRequest):
    pass
