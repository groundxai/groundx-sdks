# coding: utf-8

import unittest

import os
from pprint import pprint
from groundx import Groundx


class TestSimple(unittest.TestCase):
    def setUp(self):
        pass

    def test_list_buckets(self):
        pass
        # groundx = Groundx(
        #     api_key = os.environ['GROUNDX_API_KEY'],
        # )
        # buckets = groundx.bucket.list()
        # pprint(buckets.body)

    def test_list_projects(self):
        pass
        # groundx = Groundx(
        #     api_key = os.environ['GROUNDX_API_KEY'],
        # )
        # projects = groundx.project.list()
        # pprint(projects.body)

    def test_quick_start(self):
        pass
        # groundx = Groundx(
        #     api_key = os.environ['GROUNDX_API_KEY'],
        # )

        # project = groundx.project.create(project={"name": "test-project"}).body
        # bucket = groundx.bucket.create(bucket={"name": "test-bucket"}).body["bucket"]
        # ingest = groundx.document.upload_remote(documents=[{
        #     "bucketId": bucket["bucketId"],
        #     "metadata": {
        #         "key": "value"
        #     },
        #     "type": "txt",
        #     "sourceUrl": "https://raw.githubusercontent.com/konfig-dev/groundx-sdks/main/document.txt"
        # }]).body

        # # poll the status of upload until it is complete
        # while ingest["ingest"]["status"] != "complete":
        #     ingest = groundx.document.get_processing_status_by_id(ingest["ingest"]["processId"]).body

        #     # sleep for 3 seconds
        #     import time
        #     time.sleep(3)

        # # search
        # search = groundx.search.content(id=project["project"]["projectId"], search={"query": "Documents"})
        # pprint(search.body)

    def test_quick_start_local(self):
        pass
        # groundx = Groundx(
        #     api_key=os.environ["GROUNDX_API_KEY"],
        # )

        # projects = groundx.projects.list().body
        # project = projects["projects"][0] if "projects" in projects else None
        # buckets = groundx.buckets.list().body
        # bucket = buckets["buckets"][0] if "buckets" in buckets else None
        # if project is None or bucket is None:
        #     raise Exception("No project or bucket found")
        # # create file instance with open() for ../../../document.txt. Use path relative to this file
        # file_1 = open(
        #     os.path.join(os.path.dirname(__file__), "../../../document.txt"), "rb"
        # )
        # file_2 = open(
        #     os.path.join(os.path.dirname(__file__), "../../../document.txt"), "rb"
        # )

        # ingest = groundx.documents.upload_local(
        #     [
        #         {
        #             "blob": file_1,
        #             "metadata": {
        #                 "bucketId": bucket["bucketId"],
        #                 "fileName": "document-1.txt",
        #                 "fileType": "txt",
        #             },
        #         },
        #         {
        #             "blob": file_2,
        #             "metadata": {
        #                 "bucketId": bucket["bucketId"],
        #                 "fileName": "document-2.txt",
        #                 "fileType": "txt",
        #             },
        #         }
        #     ]
        # ).body

        # # poll the status of upload until it is complete
        # while ingest["ingest"]["status"] != "complete":
        #     ingest = groundx.documents.get_processing_status_by_id(
        #         ingest["ingest"]["processId"]
        #     ).body

        #     # sleep for 3 seconds
        #     import time

        #     time.sleep(3)

        # # search
        # search = groundx.search.content(
        #     id=project["projectId"], search={"query": "Documents"}
        # )
        # pprint(search.body)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
