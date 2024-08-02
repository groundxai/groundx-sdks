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


class WebsiteCrawlRequestWebsitesItem(
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
            cap = schemas.IntSchema
            depth = schemas.IntSchema
            searchData = schemas.DictSchema
            __annotations__ = {
                "bucketId": bucketId,
                "sourceUrl": sourceUrl,
                "cap": cap,
                "depth": depth,
                "searchData": searchData,
            }
    
    sourceUrl: MetaOapg.properties.sourceUrl
    bucketId: MetaOapg.properties.bucketId
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["bucketId"]) -> MetaOapg.properties.bucketId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sourceUrl"]) -> MetaOapg.properties.sourceUrl: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cap"]) -> MetaOapg.properties.cap: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["depth"]) -> MetaOapg.properties.depth: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["searchData"]) -> MetaOapg.properties.searchData: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["bucketId", "sourceUrl", "cap", "depth", "searchData", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["bucketId"]) -> MetaOapg.properties.bucketId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sourceUrl"]) -> MetaOapg.properties.sourceUrl: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cap"]) -> typing.Union[MetaOapg.properties.cap, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["depth"]) -> typing.Union[MetaOapg.properties.depth, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["searchData"]) -> typing.Union[MetaOapg.properties.searchData, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["bucketId", "sourceUrl", "cap", "depth", "searchData", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        sourceUrl: typing.Union[MetaOapg.properties.sourceUrl, str, ],
        bucketId: typing.Union[MetaOapg.properties.bucketId, decimal.Decimal, int, ],
        cap: typing.Union[MetaOapg.properties.cap, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        depth: typing.Union[MetaOapg.properties.depth, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        searchData: typing.Union[MetaOapg.properties.searchData, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'WebsiteCrawlRequestWebsitesItem':
        return super().__new__(
            cls,
            *args,
            sourceUrl=sourceUrl,
            bucketId=bucketId,
            cap=cap,
            depth=depth,
            searchData=searchData,
            _configuration=_configuration,
            **kwargs,
        )
