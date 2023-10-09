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

from groundx.type.document_response import DocumentResponse
from groundx.type.document_response_document import DocumentResponseDocument
from groundx.type.process_status_response_ingest_progress_complete import ProcessStatusResponseIngestProgressComplete
from groundx.type.process_status_response_ingest_progress_errors import ProcessStatusResponseIngestProgressErrors
from groundx.type.process_status_response_ingest_progress_processing import ProcessStatusResponseIngestProgressProcessing

class RequiredProcessStatusResponseIngestProgress(TypedDict):
    pass

class OptionalProcessStatusResponseIngestProgress(TypedDict, total=False):
    complete: ProcessStatusResponseIngestProgressComplete

    errors: ProcessStatusResponseIngestProgressErrors

    processing: ProcessStatusResponseIngestProgressProcessing

class ProcessStatusResponseIngestProgress(RequiredProcessStatusResponseIngestProgress, OptionalProcessStatusResponseIngestProgress):
    pass
