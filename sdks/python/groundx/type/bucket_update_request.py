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

from groundx.type.bucket_update_request_bucket import BucketUpdateRequestBucket

class RequiredBucketUpdateRequest(TypedDict):
    bucket: BucketUpdateRequestBucket

class OptionalBucketUpdateRequest(TypedDict, total=False):
    pass

class BucketUpdateRequest(RequiredBucketUpdateRequest, OptionalBucketUpdateRequest):
    pass
