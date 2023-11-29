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


class RequiredSearchResultItem(TypedDict):
    pass

class OptionalSearchResultItem(TypedDict, total=False):
    # Content bucket the search result belongs to
    bucketId: int

    # Unique system generated ID for the document
    documentId: str

    # Confidence score in the search result
    score: typing.Union[int, float]

    # Document, section, and chunk search data, both custom and system-generated
    searchData: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    # Source document URL
    sourceUrl: str

    # System-generated text, re-written for LLM completions
    suggestedText: str

    # Original text from the source document
    text: str

class SearchResultItem(RequiredSearchResultItem, OptionalSearchResultItem):
    pass
