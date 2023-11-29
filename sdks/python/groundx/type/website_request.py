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


class RequiredWebsiteRequest(TypedDict):
    bucketId: int

    # Source website URL
    sourceUrl: str

class OptionalWebsiteRequest(TypedDict, total=False):
    # Data that is passed through on callback
    callbackData: str

    # URL where GroundX will post status changes to the ingest request
    callbackUrl: str

    # The maximum number of pages to crawl
    cap: int

    # The maximum depth of linked pages to follow from the sourceUrl
    depth: int

    metadata: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

class WebsiteRequest(RequiredWebsiteRequest, OptionalWebsiteRequest):
    pass
