# coding: utf-8

"""
    GroundX API

    Ground Your RAG Apps in Fact not Fiction

    The version of the OpenAPI document: 1.0.0
    Contact: support@groundx.ai
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal

from groundx.type.preprocessor_response_preprocess_preprocessors_item_script import PreprocessorResponsePreprocessPreprocessorsItemScript

class RequiredPreprocessorResponsePreprocessPreprocessorsItem(TypedDict):
    pass

class OptionalPreprocessorResponsePreprocessPreprocessorsItem(TypedDict, total=False):
    # preprocessor ID
    id: str

    status: str

    # human readable status description
    status_message: str

    type: str

    script: PreprocessorResponsePreprocessPreprocessorsItemScript

class PreprocessorResponsePreprocessPreprocessorsItem(RequiredPreprocessorResponsePreprocessPreprocessorsItem, OptionalPreprocessorResponsePreprocessPreprocessorsItem):
    pass