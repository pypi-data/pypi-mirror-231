# Copyright 2021 Element Analytics, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import unittest
from unify.sources import Sources
from unify.sources import Sources
import json
import os
import uuid
from tests import *
import os
from tempfile import mkstemp
from unify.generalutils import csv_to_json
from unify.WaitingLibrary import Wait


class TestSourcesDefaultOrg(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.sources = Sources(
            org_id=test_org,
            cluster=cluster_name,
            props=props
        )
        cls.dataset_name = 'test-{}'.format(str(uuid.uuid4()))

    def test_source_list_default_org(self):
        source_list = self.sources.get_sources()

        self.assertTrue(len(source_list) > 0, source_list)

    def test_source_was_created(self):

        try:
            created_source = self.sources.download_dataset_content(dataset_id=test_dataset["id"])

            self.assertTrue(True, created_source)

        except Exception as e:

            self.assertTrue(False, e)

    def test_big_dataset(self):
        big = self.sources.upload_big_dataset(
            name=str(uuid.uuid4()),
            content=open("tests/data_test.csv").read()
        )
        self.assertTrue("create" in big)

    def test_create_api_dataset(self):
        api = self.sources.create_api_data_set(
            name=str(uuid.uuid4()),
            file_path="tests/data_test.csv"
        )

        self.assertTrue("data_set_id" in api, api)

    def test_create_api_dataset_content(self):
        api = self.sources.create_api_data_set_with_content(
            name=str(uuid.uuid4()),
            content=open("tests/data_test.csv").read()
        )

        self.assertTrue("data_set_id" in api, api)

    def test_commit_status(self):
        api = self.sources.create_api_data_set(
            name=str(uuid.uuid4()),
            file_path="tests/data_test.csv"
        )

        commit, response_code = self.sources.get_commit_status(
            commit_id=api["commit_id"],
            data_set_id=api["data_set_id"]
        )

        self.assertTrue(response_code in [200, 202, 201], commit)

    def test_export_dataset(self):
        export = self.sources.create_export_dataset(
            dataset_ids=[test_dataset["id"]]
        )

        self.assertTrue(len(export) > 0, export)

    def test_append_data(self):
        export = self.sources.add_data_to_existing_source(
            name=str(uuid.uuid4()),
            data_set_id=test_dataset["id"],
            file_path="tests/data_test.csv"
        )

        self.assertTrue("status" in export, export)

    def test_overwrite_dataset(self):
        export = self.sources.overwrite_dataset(
            data_set_id=test_dataset["id"],
            file_path="tests/data_test.csv"
        )

        self.assertTrue("stage" in export, export)
        self.assertTrue("overwrite" in export, export)

    def test_truncate_data_set(self):
        export = self.sources.truncate_data_set(
            data_set_id=test_dataset["id"]
        )

        self.assertTrue("commit_id" in export, export)

    def test_append_data_v2(self):
        export = self.sources.append_dataset(
            data_set_id=test_dataset["id"],
            content=open("tests/data_test.csv").read()
        )

        self.assertTrue("id" in export, export)

    def test_static_file_upload(self):
        export = self.sources.static_file_upload(
            name=str(uuid.uuid4()),
            content="tests/data_test.csv"
        )

        self.assertTrue("id" in export, export)

    def test_delete_source(self):
        export = self.sources.static_file_upload(
            name=str(uuid.uuid4()),
            content="tests/data_test.csv"
        )

        delete = self.sources.delete_source(
            source_id=export["id"]
        )

        self.assertEqual(delete['message'], 'Success', delete)


    def test_utf_encoding_source(self):
        try:
            _ = self.sources.static_file_upload(
                name=str(uuid.uuid4()),
                content="tests/data_test.csv",
                encoding="UTF-8"
            )
            self.assertTrue(True, "Dataset was created")
        except Exception as e:
            self.assertTrue(False, e)

    def test_wait_for_pipeline(self):
        """
        Verify waitfor dataset endpoint with default org
        :return:
        """
        try:
            _ = self.sources.wait_for_dataset(
                dataset_id=test_dataset["id"]
            )

            self.assertTrue(True, "Dataset became ready")
        except Exception as e:
            self.assertTrue(False, e)

    def test_create_empty_dataset(self):
        """
        Verify empty dataset can be created
        :return:
        """

        try:
            response = self.sources.create_command(
                schema={
                    "columns": [
                        {
                            "header": "name",
                            "column": {
                                "type": "text",
                                "properties": {
                                    "optional": False,
                                    "datasets.v1.columnType": "Normal"
                                }
                            }
                        },
                        {
                            "header": "description",
                            "column": {
                                "type": "text",
                                "properties": {
                                    "optional": False,
                                    "datasets.v1.columnType": "Normal"
                                }
                            }
                        }
                    ],
                    "properties": {}
                },
                name=str(uuid.uuid4()),
                facets=[],
                description="This is a test",
                cause=[]
            )

            self.assertTrue(response["uuid"] is not None, "Dataset was created")

        except Exception as e:

            self.assertTrue(False, e)
