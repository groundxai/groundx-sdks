# coding: utf-8

"""
    GroundX API

    Ground Your RAG Apps in Fact not Fiction

    The version of the OpenAPI document: 1.0.0
    Contact: support@groundx.ai
    Created by: https://www.groundx.ai/
"""

import unittest

import os
from pprint import pprint
from groundx import Groundx

class TestSimple(unittest.TestCase):
    def setUp(self):
        pass

    def test_client(self):
        groundx = Groundx(
        
            api_key = 'YOUR_API_KEY',
        )
        self.assertIsNotNone(groundx)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
