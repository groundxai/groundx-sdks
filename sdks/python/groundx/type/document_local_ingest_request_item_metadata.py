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

from groundx.type.document_type import DocumentType

class RequiredDocumentLocalIngestRequestItemMetadata(TypedDict):
    # the bucketId of the bucket which this local file will be ingested to.
    bucketId: int

    # The name of the file being ingested
    fileName: str

    fileType: DocumentType


class OptionalDocumentLocalIngestRequestItemMetadata(TypedDict, total=False):
    # Custom metadata which can be used to influence GroundX's search functionality. This data can be used to further hone GroundX search.
    searchData: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

class DocumentLocalIngestRequestItemMetadata(RequiredDocumentLocalIngestRequestItemMetadata, OptionalDocumentLocalIngestRequestItemMetadata):
    pass
