# coding: utf-8

"""
    GroundX APIs

    RAG Made Simple, Secure and Hallucination Free

    The version of the OpenAPI document: 1.3.26
    Contact: support@eyelevel.ai
    Created by: https://www.eyelevel.ai/
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING

from groundx.type.bucket_detail import BucketDetail

class RequiredGroupDetail(TypedDict):
    groupId: int


class OptionalGroupDetail(TypedDict, total=False):
    # The content buckets associated with the group
    buckets: typing.List[BucketDetail]

    # The data time when the group was created, in RFC3339 format
    created: datetime

    # The number of files contained in the content buckets associated with the group
    fileCount: int

    # The total file size of files contained in the content buckets associated with the group
    fileSize: str

    name: str

    # The data time when the group was last updated, in RFC3339 format
    updated: datetime

class GroupDetail(RequiredGroupDetail, OptionalGroupDetail):
    pass
