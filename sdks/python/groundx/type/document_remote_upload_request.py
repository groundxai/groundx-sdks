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

from groundx.type.document_remote_upload_request_documents import DocumentRemoteUploadRequestDocuments

class RequiredDocumentRemoteUploadRequest(TypedDict):
    documents: DocumentRemoteUploadRequestDocuments

class OptionalDocumentRemoteUploadRequest(TypedDict, total=False):
    pass

class DocumentRemoteUploadRequest(RequiredDocumentRemoteUploadRequest, OptionalDocumentRemoteUploadRequest):
    pass
