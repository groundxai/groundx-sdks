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

from groundx.type.bucket_detail import BucketDetail

class RequiredBucketResponse(TypedDict):
    bucket: BucketDetail

class OptionalBucketResponse(TypedDict, total=False):
    pass

class BucketResponse(RequiredBucketResponse, OptionalBucketResponse):
    pass
