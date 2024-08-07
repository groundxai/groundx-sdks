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


class HealthService(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "service",
            "lastUpdate",
            "status",
        }
        
        class properties:
            lastUpdate = schemas.DateTimeSchema
            service = schemas.StrSchema
            
            
            class status(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def HEALTHY(cls):
                    return cls("healthy")
                
                @schemas.classproperty
                def DEGRADED(cls):
                    return cls("degraded")
                
                @schemas.classproperty
                def DOWN(cls):
                    return cls("down")
                
                @schemas.classproperty
                def UNKNOWN(cls):
                    return cls("unknown")
            __annotations__ = {
                "lastUpdate": lastUpdate,
                "service": service,
                "status": status,
            }
    
    service: MetaOapg.properties.service
    lastUpdate: MetaOapg.properties.lastUpdate
    status: MetaOapg.properties.status
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lastUpdate"]) -> MetaOapg.properties.lastUpdate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["service"]) -> MetaOapg.properties.service: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["lastUpdate", "service", "status", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lastUpdate"]) -> MetaOapg.properties.lastUpdate: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["service"]) -> MetaOapg.properties.service: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["lastUpdate", "service", "status", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        service: typing.Union[MetaOapg.properties.service, str, ],
        lastUpdate: typing.Union[MetaOapg.properties.lastUpdate, str, datetime, ],
        status: typing.Union[MetaOapg.properties.status, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'HealthService':
        return super().__new__(
            cls,
            *args,
            service=service,
            lastUpdate=lastUpdate,
            status=status,
            _configuration=_configuration,
            **kwargs,
        )
