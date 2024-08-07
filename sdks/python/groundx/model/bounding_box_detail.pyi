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


class BoundingBoxDetail(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            bottomRightX = schemas.NumberSchema
            bottomRightY = schemas.NumberSchema
            pageNumber = schemas.IntSchema
            topLeftX = schemas.NumberSchema
            topLeftY = schemas.NumberSchema
            __annotations__ = {
                "bottomRightX": bottomRightX,
                "bottomRightY": bottomRightY,
                "pageNumber": pageNumber,
                "topLeftX": topLeftX,
                "topLeftY": topLeftY,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["bottomRightX"]) -> MetaOapg.properties.bottomRightX: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["bottomRightY"]) -> MetaOapg.properties.bottomRightY: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pageNumber"]) -> MetaOapg.properties.pageNumber: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["topLeftX"]) -> MetaOapg.properties.topLeftX: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["topLeftY"]) -> MetaOapg.properties.topLeftY: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["bottomRightX", "bottomRightY", "pageNumber", "topLeftX", "topLeftY", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["bottomRightX"]) -> typing.Union[MetaOapg.properties.bottomRightX, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["bottomRightY"]) -> typing.Union[MetaOapg.properties.bottomRightY, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pageNumber"]) -> typing.Union[MetaOapg.properties.pageNumber, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["topLeftX"]) -> typing.Union[MetaOapg.properties.topLeftX, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["topLeftY"]) -> typing.Union[MetaOapg.properties.topLeftY, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["bottomRightX", "bottomRightY", "pageNumber", "topLeftX", "topLeftY", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        bottomRightX: typing.Union[MetaOapg.properties.bottomRightX, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        bottomRightY: typing.Union[MetaOapg.properties.bottomRightY, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        pageNumber: typing.Union[MetaOapg.properties.pageNumber, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        topLeftX: typing.Union[MetaOapg.properties.topLeftX, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        topLeftY: typing.Union[MetaOapg.properties.topLeftY, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'BoundingBoxDetail':
        return super().__new__(
            cls,
            *args,
            bottomRightX=bottomRightX,
            bottomRightY=bottomRightY,
            pageNumber=pageNumber,
            topLeftX=topLeftX,
            topLeftY=topLeftY,
            _configuration=_configuration,
            **kwargs,
        )
