# coding: utf-8

"""
    EyeLevel's GroundX APIs

    RAG Made Simple, Secure and Hallucination Free

    The version of the OpenAPI document: 1.3.26
    Contact: support@eyelevel.ai
    Created by: https://www.eyelevel.ai/
"""

import unittest
from unittest.mock import patch

import urllib3

import groundx
from groundx.paths.v1_ingest_document_document_id import delete
from groundx import configuration, schemas, api_client

from .. import ApiTestMixin


class TestV1IngestDocumentDocumentId(ApiTestMixin, unittest.TestCase):
    """
    V1IngestDocumentDocumentId unit test stubs
        delete (singular)
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
