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


class RequiredSearchRequestSearch(TypedDict):
    # The search query to be used to find relevant documentation. <WIP>
    query: str

class OptionalSearchRequestSearch(TypedDict, total=False):
    # A token for pagination. If the number of documents for a given query is larger than n, the response will include a \"nextToken\" value. That token can be included in this field to retrieve the next batch of n documents.
    nextToken: str

class SearchRequestSearch(RequiredSearchRequestSearch, OptionalSearchRequestSearch):
    pass
