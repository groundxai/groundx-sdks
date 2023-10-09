# coding: utf-8
"""
    GroundX API

    Ground Your RAG Apps in Fact not Fiction

    The version of the OpenAPI document: 1.0.0
    Contact: support@groundx.ai
    Created by: https://www.groundx.ai/
"""

import typing
import inspect
from datetime import date, datetime
from groundx.client_custom import ClientCustom
from groundx.configuration import Configuration
from groundx.api_client import ApiClient
from groundx.type_util import copy_signature
from groundx.apis.tags.api_keys_api import APIKeysApi
from groundx.apis.tags.buckets_api import BucketsApi
from groundx.apis.tags.documents_api import DocumentsApi
from groundx.apis.tags.projects_api import ProjectsApi
from groundx.apis.tags.search_api import SearchApi



class Groundx(ClientCustom):

    def __init__(self, configuration: typing.Union[Configuration, None] = None, **kwargs):
        super().__init__(configuration, **kwargs)
        if (len(kwargs) > 0):
            configuration = Configuration(**kwargs)
        if (configuration is None):
            raise Exception("configuration is required")
        api_client = ApiClient(configuration)
        self.api_keys: APIKeysApi = APIKeysApi(api_client)
        self.buckets: BucketsApi = BucketsApi(api_client)
        self.documents: DocumentsApi = DocumentsApi(api_client)
        self.projects: ProjectsApi = ProjectsApi(api_client)
        self.search: SearchApi = SearchApi(api_client)
