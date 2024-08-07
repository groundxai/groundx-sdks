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


class ProcessingStatus(
    schemas.EnumBase,
    schemas.StrSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    
    @schemas.classproperty
    def QUEUED(cls):
        return cls("queued")
    
    @schemas.classproperty
    def PROCESSING(cls):
        return cls("processing")
    
    @schemas.classproperty
    def ERROR(cls):
        return cls("error")
    
    @schemas.classproperty
    def COMPLETE(cls):
        return cls("complete")
    
    @schemas.classproperty
    def CANCELLED(cls):
        return cls("cancelled")
