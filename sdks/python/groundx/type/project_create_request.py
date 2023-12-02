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


class RequiredProjectCreateRequest(TypedDict):
    # The name of the project being created.
    name: str

class OptionalProjectCreateRequest(TypedDict, total=False):
    # Specify bucketName to automatically create a bucket, by the name specified, and add it to the created project.
    bucketName: str

class ProjectCreateRequest(RequiredProjectCreateRequest, OptionalProjectCreateRequest):
    pass
