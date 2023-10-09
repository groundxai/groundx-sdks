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
from typing_extensions import TypedDict, Literal


class RequiredApiKeyManagementList405Response(TypedDict):
    pass

class OptionalApiKeyManagementList405Response(TypedDict, total=False):
    message: str

class ApiKeyManagementList405Response(RequiredApiKeyManagementList405Response, OptionalApiKeyManagementList405Response):
    pass
