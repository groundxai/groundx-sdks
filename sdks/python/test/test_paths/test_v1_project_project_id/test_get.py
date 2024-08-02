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
from groundx.paths.v1_project_project_id import get
from groundx import configuration, schemas, api_client

from .. import ApiTestMixin


class TestV1ProjectProjectId(ApiTestMixin, unittest.TestCase):
    """
    V1ProjectProjectId unit test stubs
        get
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
