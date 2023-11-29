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

from groundx.type.website_request import WebsiteRequest

class RequiredWebsiteCrawlRequest(TypedDict):
    pass

class OptionalWebsiteCrawlRequest(TypedDict, total=False):
    project: WebsiteRequest

class WebsiteCrawlRequest(RequiredWebsiteCrawlRequest, OptionalWebsiteCrawlRequest):
    pass