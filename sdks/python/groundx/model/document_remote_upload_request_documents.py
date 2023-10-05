# coding: utf-8

"""
    GroundX API

    Ground Your RAG Apps in Fact not Fiction

    The version of the OpenAPI document: 1.0.0
    Contact: support@groundx.ai
    Generated by: https://konfigthis.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from groundx import schemas  # noqa: F401


class DocumentRemoteUploadRequestDocuments(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['DocumentRemoteUploadRequestDocumentsItem']:
            return DocumentRemoteUploadRequestDocumentsItem

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple['DocumentRemoteUploadRequestDocumentsItem'], typing.List['DocumentRemoteUploadRequestDocumentsItem']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'DocumentRemoteUploadRequestDocuments':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'DocumentRemoteUploadRequestDocumentsItem':
        return super().__getitem__(i)

from groundx.model.document_remote_upload_request_documents_item import DocumentRemoteUploadRequestDocumentsItem
from groundx.model.document_type import DocumentType