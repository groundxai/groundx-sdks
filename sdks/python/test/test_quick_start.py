# coding: utf-8

import unittest

import os
from pprint import pprint
from groundx import Groundx

class TestSimple(unittest.TestCase):
    def setUp(self):
        pass

    def test_list_buckets(self):
        groundx = Groundx(
            api_key = os.environ['GROUNDX_API_KEY'],
        )
        buckets = groundx.bucket.list()
        pprint(buckets.body)

    def test_quick_start(self):
        groundx = Groundx(
            api_key = os.environ['GROUNDX_API_KEY'],
        )
        # bucket = groundx.bucket.create(bucket={"name": "test-bucket"}).body["bucket"]


    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
