# coding: utf-8

"""
    GroundX APIs

    RAG Made Simple, Secure and Hallucination Free

    The version of the OpenAPI document: 1.3.26
    Contact: support@eyelevel.ai
    Created by: https://www.eyelevel.ai/
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
