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


class RequiredApiKeyManagementListResponseApiKeysItem(TypedDict):
    pass

class OptionalApiKeyManagementListResponseApiKeysItem(TypedDict, total=False):
    # The data time when the API key was created, in RFC3339 format
    created: datetime

    apiKey: str

    name: str

class ApiKeyManagementListResponseApiKeysItem(RequiredApiKeyManagementListResponseApiKeysItem, OptionalApiKeyManagementListResponseApiKeysItem):
    pass
