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


class RequiredSearchResultItem(TypedDict):
    pass

class OptionalSearchResultItem(TypedDict, total=False):
    # Unique system generated ID for the chunk
    chunkId: str

    # Unique system generated ID for the document
    documentId: str

    # Document and chunk level metadata
    metadata: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    # Result relevance score
    score: typing.Union[int, float]

    # Document source URL
    sourceUrl: str

    # Text from result
    text: str

class SearchResultItem(RequiredSearchResultItem, OptionalSearchResultItem):
    pass
