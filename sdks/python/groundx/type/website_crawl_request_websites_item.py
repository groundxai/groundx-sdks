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
    # the bucketId of the bucket which remote file will be uploaded to.
    bucketId: int

    # The URL from which the crawl is initiated.
    sourceUrl: str

class OptionalWebsiteCrawlRequestWebsitesItem(TypedDict, total=False):
    # The maximum number of pages to crawl
    cap: int

    # The maximum depth of linked pages to follow from the sourceUrl
    depth: int

    # Custom metadata which can be used to influence GroundX's search functionality. This data can be used to further hone GroundX search.
    searchData: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

class WebsiteCrawlRequestWebsitesItem(RequiredWebsiteCrawlRequestWebsitesItem, OptionalWebsiteCrawlRequestWebsitesItem):
    pass
