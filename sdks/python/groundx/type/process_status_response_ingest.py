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

from groundx.type.process_status_response_ingest_progress import ProcessStatusResponseIngestProgress
from groundx.type.processing_status import ProcessingStatus

class RequiredProcessStatusResponseIngest(TypedDict):
    processId: str

    status: ProcessingStatus


class OptionalProcessStatusResponseIngest(TypedDict, total=False):
    progress: ProcessStatusResponseIngestProgress

    statusMessage: str

class ProcessStatusResponseIngest(RequiredProcessStatusResponseIngest, OptionalProcessStatusResponseIngest):
    pass
