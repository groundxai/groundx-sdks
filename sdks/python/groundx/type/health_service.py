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
