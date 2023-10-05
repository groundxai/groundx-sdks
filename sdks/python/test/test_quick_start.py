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

    def test_list_projects(self):
        groundx = Groundx(
            api_key = os.environ['GROUNDX_API_KEY'],
        )
        projects = groundx.project.list()
        pprint(projects.body)

    def test_quick_start(self):
        groundx = Groundx(
            api_key = os.environ['GROUNDX_API_KEY'],
        )

        project = groundx.project.create(project={"name": "test-project"}).body
        bucket = groundx.bucket.create(bucket={"name": "test-bucket"}).body["bucket"]
        ingest = groundx.document.upload_remote(documents=[{
            "bucketId": bucket["bucketId"],
            "metadata": {
                "key": "value"
            },
            "type": "txt",
            "sourceUrl": "https://raw.githubusercontent.com/konfig-dev/groundx-sdks/main/document.txt"
        }]).body

        # poll the status of upload until it is complete
        while ingest["ingest"]["status"] != "complete":
            ingest = groundx.document.get_processing_status_by_id(ingest["ingest"]["processId"]).body

            # sleep for 3 seconds
            import time
            time.sleep(3)

        # search
        search = groundx.search.content(project_id=project["project"]["projectId"], search={"query": "Documents"})
        pprint(search.body)

    def test_quick_start_local(self):
        groundx = Groundx(
            api_key = os.environ['GROUNDX_API_KEY'],
        )

        project = groundx.project.create(project={"name": "test-project"}).body
        bucket = groundx.bucket.create(bucket={"name": "test-bucket"}).body["bucket"]
        # create file instance with open() for ../../../document.txt. Use path relative to this file
        file = open(os.path.join(os.path.dirname(__file__), "../../../document.txt"), "rb")
        ingest = groundx.document.upload_local(blob=[file], metadata={"bucketId": bucket["bucketId"], "fileName": "document.txt", "fileType": "txt"}).body

        # poll the status of upload until it is complete
        while ingest["ingest"]["status"] != "complete":
            ingest = groundx.document.get_processing_status_by_id(ingest["ingest"]["processId"]).body

            # sleep for 3 seconds
            import time
            time.sleep(3)

        # search
        search = groundx.search.content(project_id=project["project"]["projectId"], search={"query": "Documents"})
        pprint(search.body)


    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
