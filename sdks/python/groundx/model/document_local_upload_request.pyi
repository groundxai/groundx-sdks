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


class DocumentLocalUploadRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "metadata",
            "blob",
        }
        
        class properties:
        
            @staticmethod
            def blob() -> typing.Type['DocumentLocalUploadRequestBlob']:
                return DocumentLocalUploadRequestBlob
        
            @staticmethod
            def metadata() -> typing.Type['DocumentLocalUploadRequestMetadata']:
                return DocumentLocalUploadRequestMetadata
            __annotations__ = {
                "blob": blob,
                "metadata": metadata,
            }
    
    metadata: 'DocumentLocalUploadRequestMetadata'
    blob: 'DocumentLocalUploadRequestBlob'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["blob"]) -> 'DocumentLocalUploadRequestBlob': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["metadata"]) -> 'DocumentLocalUploadRequestMetadata': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["blob", "metadata", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["blob"]) -> 'DocumentLocalUploadRequestBlob': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["metadata"]) -> 'DocumentLocalUploadRequestMetadata': ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["blob", "metadata", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        metadata: 'DocumentLocalUploadRequestMetadata',
        blob: 'DocumentLocalUploadRequestBlob',
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'DocumentLocalUploadRequest':
        return super().__new__(
            cls,
            *args,
            metadata=metadata,
            blob=blob,
            _configuration=_configuration,
            **kwargs,
        )

from groundx.model.document_local_upload_request_blob import DocumentLocalUploadRequestBlob
from groundx.model.document_local_upload_request_metadata import DocumentLocalUploadRequestMetadata
from groundx.model.document_type import DocumentType
