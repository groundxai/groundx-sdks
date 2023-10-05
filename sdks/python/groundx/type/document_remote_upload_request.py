# coding: utf-8

"""
    GroundX API

    Ground Your RAG Apps in Fact not Fiction

    The version of the OpenAPI document: 1.0.0
    Contact: support@groundx.ai
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal

from groundx.type.document_remote_upload_request_documents import DocumentRemoteUploadRequestDocuments
from groundx.type.document_type import DocumentType

class RequiredDocumentRemoteUploadRequest(TypedDict):
    bucketId: int

    sourceUrl: str

class OptionalDocumentRemoteUploadRequest(TypedDict, total=False):
    callbackData: str

    callbackUrl: str

    metadata: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    type: DocumentType

    documents: DocumentRemoteUploadRequestDocuments

class DocumentRemoteUploadRequest(RequiredDocumentRemoteUploadRequest, OptionalDocumentRemoteUploadRequest):
    pass
