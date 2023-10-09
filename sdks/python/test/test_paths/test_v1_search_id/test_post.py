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
from groundx.paths.v1_search_id import post
from groundx import configuration, schemas, api_client

from .. import ApiTestMixin


class TestV1SearchId(ApiTestMixin, unittest.TestCase):
    """
    V1SearchId unit test stubs
        Perform a search query of your content
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
