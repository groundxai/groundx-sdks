# coding: utf-8

"""
    GroundX API

    Ground Your RAG Apps in Fact not Fiction

    The version of the OpenAPI document: 1.0.0
    Contact: support@groundx.ai
    Created by: https://www.groundx.ai/
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


class DocumentRemoteIngestRequestDocuments(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['DocumentRemoteIngestRequestDocumentsItem']:
            return DocumentRemoteIngestRequestDocumentsItem

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple['DocumentRemoteIngestRequestDocumentsItem'], typing.List['DocumentRemoteIngestRequestDocumentsItem']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'DocumentRemoteIngestRequestDocuments':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'DocumentRemoteIngestRequestDocumentsItem':
        return super().__getitem__(i)

from groundx.model.document_remote_ingest_request_documents_item import DocumentRemoteIngestRequestDocumentsItem