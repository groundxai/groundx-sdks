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


class RequiredGroupUpdateRequest(TypedDict):
    # The new name of the group being renamed.
    newName: str

class OptionalGroupUpdateRequest(TypedDict, total=False):
    pass

class GroupUpdateRequest(RequiredGroupUpdateRequest, OptionalGroupUpdateRequest):
    pass
