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

from groundx.type.bounding_box_detail import BoundingBoxDetail
from groundx.type.search_result_item_page_images import SearchResultItemPageImages

class RequiredSearchResultItem(TypedDict):
    pass

class OptionalSearchResultItem(TypedDict, total=False):
    # Coordinates corresponding to the areas of the document where the chunk appears
    boundingBoxes: typing.List[BoundingBoxDetail]

    # Content bucket the search result belongs to
    bucketId: int

    # Unique system generated ID for the chunk
    chunkId: str

    # Unique system generated ID for the document
    documentId: str

    # Name of ingested file
    fileName: str

    # An image clipping of the table or figure object from the document
    multimodalUrl: str

    pageImages: SearchResultItemPageImages

    # Confidence score in the search result
    score: typing.Union[int, float]

    # Document, section, and chunk search data, both custom and system-generated
    searchData: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    # Source document URL
    sourceUrl: str

    # System-generated text, re-written for LLM completions
    suggestedText: str

    # Original text from the source document
    text: str

class SearchResultItem(RequiredSearchResultItem, OptionalSearchResultItem):
    pass
