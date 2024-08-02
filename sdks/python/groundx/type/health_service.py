# coding: utf-8

"""
    GroundX APIs

    RAG Made Simple, Secure and Hallucination Free

    The version of the OpenAPI document: 1.3.26
    Contact: support@eyelevel.ai
    Created by: https://www.eyelevel.ai/
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING


class RequiredHealthService(TypedDict):
    # The data time when the service status was last updated, in RFC3339 format
    lastUpdate: datetime

    # The name of the service
    service: str

    # The health status of the service
    status: str

class OptionalHealthService(TypedDict, total=False):
    pass

class HealthService(RequiredHealthService, OptionalHealthService):
    pass
