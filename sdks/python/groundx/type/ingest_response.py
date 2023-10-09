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

from groundx.type.ingest_response_ingest import IngestResponseIngest
from groundx.type.processing_status import ProcessingStatus

class RequiredIngestResponse(TypedDict):
    ingest: IngestResponseIngest

class OptionalIngestResponse(TypedDict, total=False):
    pass

class IngestResponse(RequiredIngestResponse, OptionalIngestResponse):
    pass
