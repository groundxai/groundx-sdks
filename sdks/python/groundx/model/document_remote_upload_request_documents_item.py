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


class DocumentRemoteUploadRequestDocumentsItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "sourceUrl",
            "bucketId",
        }
        
        class properties:
            bucketId = schemas.IntSchema
            sourceUrl = schemas.StrSchema
            fileName = schemas.StrSchema
        
            @staticmethod
            def fileType() -> typing.Type['DocumentType']:
                return DocumentType
            searchData = schemas.DictSchema
            __annotations__ = {
                "bucketId": bucketId,
                "sourceUrl": sourceUrl,
                "fileName": fileName,
                "fileType": fileType,
                "searchData": searchData,
            }
    
    sourceUrl: MetaOapg.properties.sourceUrl
    bucketId: MetaOapg.properties.bucketId
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["bucketId"]) -> MetaOapg.properties.bucketId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sourceUrl"]) -> MetaOapg.properties.sourceUrl: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fileName"]) -> MetaOapg.properties.fileName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fileType"]) -> 'DocumentType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["searchData"]) -> MetaOapg.properties.searchData: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["bucketId", "sourceUrl", "fileName", "fileType", "searchData", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["bucketId"]) -> MetaOapg.properties.bucketId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sourceUrl"]) -> MetaOapg.properties.sourceUrl: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fileName"]) -> typing.Union[MetaOapg.properties.fileName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fileType"]) -> typing.Union['DocumentType', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["searchData"]) -> typing.Union[MetaOapg.properties.searchData, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["bucketId", "sourceUrl", "fileName", "fileType", "searchData", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        sourceUrl: typing.Union[MetaOapg.properties.sourceUrl, str, ],
        bucketId: typing.Union[MetaOapg.properties.bucketId, decimal.Decimal, int, ],
        fileName: typing.Union[MetaOapg.properties.fileName, str, schemas.Unset] = schemas.unset,
        fileType: typing.Union['DocumentType', schemas.Unset] = schemas.unset,
        searchData: typing.Union[MetaOapg.properties.searchData, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'DocumentRemoteUploadRequestDocumentsItem':
        return super().__new__(
            cls,
            *args,
            sourceUrl=sourceUrl,
            bucketId=bucketId,
            fileName=fileName,
            fileType=fileType,
            searchData=searchData,
            _configuration=_configuration,
            **kwargs,
        )

from groundx.model.document_type import DocumentType
