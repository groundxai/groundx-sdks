# coding: utf-8

"""
    GroundX API

    Ground Your RAG Apps in Fact not Fiction

    The version of the OpenAPI document: 1.0.0
    Contact: support@groundx.ai
    Created by: https://www.groundx.ai/
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING

from groundx.type.health_service import HealthService

class RequiredHealthResponseHealth(TypedDict):
    services: typing.List[HealthService]

class OptionalHealthResponseHealth(TypedDict, total=False):
    pass

class HealthResponseHealth(RequiredHealthResponseHealth, OptionalHealthResponseHealth):
    pass
