# coding: utf-8
"""
    GroundX API

    Ground Your RAG Apps in Fact not Fiction

    The version of the OpenAPI document: 1.0.0
    Contact: support@groundx.ai
    Created by: https://www.groundx.ai/
"""

import typing

from groundx.xray import XRay

from groundx.configuration import Configuration
from groundx.api_client import ApiClient


class ClientCustom:
    def __init__(
        self, configuration: typing.Union[Configuration, None] = None, **kwargs
    ):
        if len(kwargs) > 0:
            configuration = Configuration(**kwargs)
        if configuration is None:
            raise Exception("configuration is required")

        self.x_ray = XRay(file_path="", api_client=ApiClient(configuration))
