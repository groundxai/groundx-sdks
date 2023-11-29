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


class RequiredWebsiteCrawlRequestWebsitesItem(TypedDict):
    bucketId: int

    # Source website URL
    sourceUrl: str

class OptionalWebsiteCrawlRequestWebsitesItem(TypedDict, total=False):
    # The maximum number of pages to crawl
    cap: int

    # The maximum depth of linked pages to follow from the sourceUrl
    depth: int

    searchData: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

class WebsiteCrawlRequestWebsitesItem(RequiredWebsiteCrawlRequestWebsitesItem, OptionalWebsiteCrawlRequestWebsitesItem):
    pass
