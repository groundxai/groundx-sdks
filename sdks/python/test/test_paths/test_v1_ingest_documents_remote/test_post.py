# coding: utf-8

"""
    GroundX API

    Ground Your RAG Apps in Fact not Fiction

    The version of the OpenAPI document: 1.0.0
    Contact: support@groundx.ai
    Created by: https://www.groundx.ai/
"""

import unittest
from unittest.mock import patch

import urllib3

import groundx
from groundx.paths.v1_ingest_documents_remote import post
from groundx import configuration, schemas, api_client

from .. import ApiTestMixin


class TestV1IngestDocumentsRemote(ApiTestMixin, unittest.TestCase):
    """
    V1IngestDocumentsRemote unit test stubs
        ingest_remote
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
