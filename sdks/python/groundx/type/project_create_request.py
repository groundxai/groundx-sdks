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


class RequiredProjectCreateRequest(TypedDict):
    # The name of the project being created.
    name: str


class OptionalProjectCreateRequest(TypedDict, total=False):
    # Specify bucketName to automatically create a bucket, by the name specified, and add it to the created project.
    bucketName: str

class ProjectCreateRequest(RequiredProjectCreateRequest, OptionalProjectCreateRequest):
    pass
