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

from groundx.type.document_remote_ingest_request_documents import DocumentRemoteIngestRequestDocuments

class RequiredDocumentRemoteIngestRequest(TypedDict):
    documents: DocumentRemoteIngestRequestDocuments

class OptionalDocumentRemoteIngestRequest(TypedDict, total=False):
    pass

class DocumentRemoteIngestRequest(RequiredDocumentRemoteIngestRequest, OptionalDocumentRemoteIngestRequest):
    pass
