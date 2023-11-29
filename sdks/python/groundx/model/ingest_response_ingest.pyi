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


class IngestResponseIngest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "processId",
            "status",
        }
        
        class properties:
            processId = schemas.UUIDSchema
        
            @staticmethod
            def status() -> typing.Type['ProcessingStatus']:
                return ProcessingStatus
            __annotations__ = {
                "processId": processId,
                "status": status,
            }
    
    processId: MetaOapg.properties.processId
    status: 'ProcessingStatus'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["processId"]) -> MetaOapg.properties.processId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> 'ProcessingStatus': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["processId", "status", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["processId"]) -> MetaOapg.properties.processId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> 'ProcessingStatus': ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["processId", "status", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        processId: typing.Union[MetaOapg.properties.processId, str, uuid.UUID, ],
        status: 'ProcessingStatus',
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'IngestResponseIngest':
        return super().__new__(
            cls,
            *args,
            processId=processId,
            status=status,
            _configuration=_configuration,
            **kwargs,
        )

from groundx.model.processing_status import ProcessingStatus
