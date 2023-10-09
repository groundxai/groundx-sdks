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

from groundx.type.search_result_item import SearchResultItem

class RequiredSearchResponseSearch(TypedDict):
    pass

class OptionalSearchResponseSearch(TypedDict, total=False):
    # Total results
    count: int

    results: typing.List[SearchResultItem]

    # The search query
    query: str

    # Top result relevance score
    score: typing.Union[int, float]

    # Combined text from results
    text: str

    # For paginated results
    nextToken: str

class SearchResponseSearch(RequiredSearchResponseSearch, OptionalSearchResponseSearch):
    pass
