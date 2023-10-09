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

from groundx.type.document_response import DocumentResponse
from groundx.type.document_response_document import DocumentResponseDocument

class RequiredProcessStatusResponseIngestProgressComplete(TypedDict):
    pass

class OptionalProcessStatusResponseIngestProgressComplete(TypedDict, total=False):
    documents: typing.List[DocumentResponse]

    total: int

class ProcessStatusResponseIngestProgressComplete(RequiredProcessStatusResponseIngestProgressComplete, OptionalProcessStatusResponseIngestProgressComplete):
    pass
