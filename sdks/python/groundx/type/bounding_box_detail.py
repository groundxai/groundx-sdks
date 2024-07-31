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


class RequiredBoundingBoxDetail(TypedDict):
    pass

class OptionalBoundingBoxDetail(TypedDict, total=False):
    # The x coordinate of the lower right corner of the bounding box
    bottomRightX: typing.Union[int, float]

    # The y coordinate of the lower right corner of the bounding box
    bottomRightY: typing.Union[int, float]

    # The page number the bounding box appears on, using a 1-based array indexing (starts with page 1, not page 0)
    pageNumber: int

    # The x coordinate of the upper left corner of the bounding box
    topLeftX: typing.Union[int, float]

    # The y coordinate of the upper left corner of the bounding box
    topLeftY: typing.Union[int, float]

class BoundingBoxDetail(RequiredBoundingBoxDetail, OptionalBoundingBoxDetail):
    pass
