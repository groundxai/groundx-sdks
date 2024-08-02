# coding: utf-8

"""
    GroundX APIs

    RAG Made Simple, Secure and Hallucination Free

    The version of the OpenAPI document: 1.3.26
    Contact: support@eyelevel.ai
    Created by: https://www.eyelevel.ai/
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


class DocumentDetail(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "documentId",
        }
        
        class properties:
            documentId = schemas.UUIDSchema
            bucketId = schemas.IntSchema
            fileName = schemas.StrSchema
            fileSize = schemas.StrSchema
        
            @staticmethod
            def fileType() -> typing.Type['DocumentType']:
                return DocumentType
            processId = schemas.UUIDSchema
            searchData = schemas.DictSchema
            sourceUrl = schemas.StrSchema
        
            @staticmethod
            def status() -> typing.Type['ProcessingStatus']:
                return ProcessingStatus
            statusMessage = schemas.StrSchema
            xrayUrl = schemas.StrSchema
            __annotations__ = {
                "documentId": documentId,
                "bucketId": bucketId,
                "fileName": fileName,
                "fileSize": fileSize,
                "fileType": fileType,
                "processId": processId,
                "searchData": searchData,
                "sourceUrl": sourceUrl,
                "status": status,
                "statusMessage": statusMessage,
                "xrayUrl": xrayUrl,
            }
    
    documentId: MetaOapg.properties.documentId
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["documentId"]) -> MetaOapg.properties.documentId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["bucketId"]) -> MetaOapg.properties.bucketId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fileName"]) -> MetaOapg.properties.fileName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fileSize"]) -> MetaOapg.properties.fileSize: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fileType"]) -> 'DocumentType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["processId"]) -> MetaOapg.properties.processId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["searchData"]) -> MetaOapg.properties.searchData: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sourceUrl"]) -> MetaOapg.properties.sourceUrl: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> 'ProcessingStatus': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["statusMessage"]) -> MetaOapg.properties.statusMessage: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["xrayUrl"]) -> MetaOapg.properties.xrayUrl: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["documentId", "bucketId", "fileName", "fileSize", "fileType", "processId", "searchData", "sourceUrl", "status", "statusMessage", "xrayUrl", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["documentId"]) -> MetaOapg.properties.documentId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["bucketId"]) -> typing.Union[MetaOapg.properties.bucketId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fileName"]) -> typing.Union[MetaOapg.properties.fileName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fileSize"]) -> typing.Union[MetaOapg.properties.fileSize, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fileType"]) -> typing.Union['DocumentType', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["processId"]) -> typing.Union[MetaOapg.properties.processId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["searchData"]) -> typing.Union[MetaOapg.properties.searchData, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sourceUrl"]) -> typing.Union[MetaOapg.properties.sourceUrl, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union['ProcessingStatus', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["statusMessage"]) -> typing.Union[MetaOapg.properties.statusMessage, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["xrayUrl"]) -> typing.Union[MetaOapg.properties.xrayUrl, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["documentId", "bucketId", "fileName", "fileSize", "fileType", "processId", "searchData", "sourceUrl", "status", "statusMessage", "xrayUrl", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        documentId: typing.Union[MetaOapg.properties.documentId, str, uuid.UUID, ],
        bucketId: typing.Union[MetaOapg.properties.bucketId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        fileName: typing.Union[MetaOapg.properties.fileName, str, schemas.Unset] = schemas.unset,
        fileSize: typing.Union[MetaOapg.properties.fileSize, str, schemas.Unset] = schemas.unset,
        fileType: typing.Union['DocumentType', schemas.Unset] = schemas.unset,
        processId: typing.Union[MetaOapg.properties.processId, str, uuid.UUID, schemas.Unset] = schemas.unset,
        searchData: typing.Union[MetaOapg.properties.searchData, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        sourceUrl: typing.Union[MetaOapg.properties.sourceUrl, str, schemas.Unset] = schemas.unset,
        status: typing.Union['ProcessingStatus', schemas.Unset] = schemas.unset,
        statusMessage: typing.Union[MetaOapg.properties.statusMessage, str, schemas.Unset] = schemas.unset,
        xrayUrl: typing.Union[MetaOapg.properties.xrayUrl, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'DocumentDetail':
        return super().__new__(
            cls,
            *args,
            documentId=documentId,
            bucketId=bucketId,
            fileName=fileName,
            fileSize=fileSize,
            fileType=fileType,
            processId=processId,
            searchData=searchData,
            sourceUrl=sourceUrl,
            status=status,
            statusMessage=statusMessage,
            xrayUrl=xrayUrl,
            _configuration=_configuration,
            **kwargs,
        )

from groundx.model.document_type import DocumentType
from groundx.model.processing_status import ProcessingStatus
