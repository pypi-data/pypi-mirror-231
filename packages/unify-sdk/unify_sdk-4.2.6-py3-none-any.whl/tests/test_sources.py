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
from tests import *
from unify.helpers.pipeline.schema import FlowSchema


class TestSourcesWithOrgID(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.sources = Sources(
            cluster=cluster_name,
            props=props
        )
        cls.dataset_name = 'test-{}'.format(str(uuid.uuid4()))

    def test_source_list_default_org(self):
        source_list = self.sources.get_sources(
            org_id=test_org
        )

        self.assertTrue(len(source_list) > 0, source_list)

    def test_source_was_created(self):

        try:
            created_source = self.sources.download_dataset_content(
                org_id=test_org,
                dataset_id=test_dataset["id"]
            )

            self.assertTrue(True, created_source)

        except Exception as e:

            self.assertTrue(False, e)

    def test_big_dataset(self):
        big = self.sources.upload_big_dataset(
            name=str(uuid.uuid4()),
            org_id=test_org,
            content=open("tests/data_test.csv").read()
        )
        self.assertTrue("create" in big)

    def test_create_api_dataset(self):
        api = self.sources.create_api_data_set(
            org_id=test_org,
            name=str(uuid.uuid4()),
            file_path="tests/data_test.csv"
        )

        self.assertTrue("data_set_id" in api, api)

    def test_create_api_dataset_content(self):
        api = self.sources.create_api_data_set_with_content(
            name=str(uuid.uuid4()),
            org_id=test_org,
            content=open("tests/data_test.csv").read()
        )

        self.assertTrue("data_set_id" in api, api)

    def test_commit_status(self):
        api = self.sources.create_api_data_set(
            name=str(uuid.uuid4()),
            org_id=test_org,
            file_path="tests/data_test.csv"
        )

        commit, response_code = self.sources.get_commit_status(
            org_id=test_org,
            commit_id=api["commit_id"],
            data_set_id=api["data_set_id"]
        )

        self.assertTrue(response_code in [200, 202, 201], commit)

    def test_export_dataset(self):
        export = self.sources.create_export_dataset(
            org_id=test_org,
            dataset_ids=[test_dataset["id"]]
        )

        self.assertTrue(len(export) > 0, export)

    def test_append_data(self):
        export = self.sources.add_data_to_existing_source(
            org_id=test_org,
            name=str(uuid.uuid4()),
            data_set_id=test_dataset["id"],
            file_path="tests/data_test.csv"
        )

        self.assertTrue("status" in export, export)

    def test_overwrite_dataset(self):
        export = self.sources.overwrite_dataset(
            org_id=test_org,
            data_set_id=test_dataset["id"],
            file_path="tests/data_test.csv"
        )

        self.assertTrue("stage" in export, export)
        self.assertTrue("overwrite" in export, export)

    def test_truncate_data_set(self):
        export = self.sources.truncate_data_set(
            org_id=test_org,
            data_set_id=test_dataset["id"]
        )

        self.assertTrue("commit_id" in export, export)

    def test_append_data_v2(self):
        export = self.sources.append_dataset(
            data_set_id=test_dataset["id"],
            content=open("tests/data_test.csv").read(),
            org_id=test_org
        )

        self.assertTrue("id" in export, export)

    def test_static_file_upload(self):
        export = self.sources.static_file_upload(
            org_id=test_org,
            name=str(uuid.uuid4()),
            content="tests/data_test.csv"
        )

        self.assertTrue("id" in export, export)

    def test_delete_source(self):
        export = self.sources.static_file_upload(
            org_id=test_org,
            name=str(uuid.uuid4()),
            content="tests/data_test.csv"
        )

        delete = self.sources.delete_source(
            org_id=test_org,
            source_id=export["id"]
        )

        self.assertEqual(delete['message'], 'Success', delete)

    def test_rename_datset(self):
        export = self.sources.static_file_upload(
            org_id=test_org,
            name=str(uuid.uuid4()),
            content="tests/data_test.csv"
        )

        try:
            _ = self.sources.update_dataset_metadata(
                org_id=test_org,
                dataset_id=export["id"],
                name="{}__renamed".format(str(uuid.uuid4()))
            )
            self.assertTrue(True, "Pipeline was renamed")
        except Exception as e:
            self.assertTrue(False, e)

    def test_add_facets_datset(self):
        export = self.sources.static_file_upload(
            org_id=test_org,
            name=str(uuid.uuid4()),
            content="tests/data_test.csv"
        )

        try:
            _ = self.sources.update_dataset_metadata(
                org_id=test_org,
                dataset_id=export["id"],
                facets=[str(uuid.uuid4())[:10]]
            )
            self.assertTrue(True, "Facets were added to dataset")
        except Exception as e:
            self.assertTrue(False, e)

    def test_add_description_datset(self):
        export = self.sources.static_file_upload(
            org_id=test_org,
            name=str(uuid.uuid4()),
            content="tests/data_test.csv"
        )

        try:
            _ = self.sources.update_dataset_metadata(
                org_id=test_org,
                dataset_id=export["id"],
                description="{}__renamed".format(str(uuid.uuid4()))
            )
            self.assertTrue(True, "Description was added to dataset")
        except Exception as e:
            self.assertTrue(False, e)

    def test_utf_encoding_source(self):
        try:
            _ = self.sources.static_file_upload(
                org_id=test_org,
                name=str(uuid.uuid4()),
                content="tests/data_test.csv",
                encoding="UTF-8"

            )
            self.assertTrue(True, "Dataset was created")
        except Exception as e:
            self.assertTrue(False, e)

    def test_wait_for_pipeline(self):
        """
        Verify waitfor dataset endpoint
        :return:
        """
        try:
            _ = self.sources.wait_for_dataset(
                dataset_id=test_dataset["id"],
                org_id=test_org
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
                org_id=test_org,
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

    def test_create_empty_dataset_from_flow(self):

        flow_cols = [
            {
                "name": "name",
                "dataType": "STRING",
                "isOpt": True,
                "columnType": "Normal"
            },
            {
                "name": "description",
                "dataType": "STRING",
                "isOpt": True,
                "columnType": "Normal"
            }, {
                "name": "engunits",
                "dataType": "STRING",
                "isOpt": True,
                "columnType": "UnitOfMeasure"
            }, {
                "name": "EQUIPMENT_ID *",
                "dataType": "STRING",
                "isOpt": False,
                "columnType": "EquipmentId"
            }
        ]

        schema = {
            "columns": FlowSchema(columns=flow_cols).to_dataset_schema(),
            "properties": {}
        }

        try:
            response = self.sources.create_command(
                org_id=test_org,
                schema=schema,
                name=str(uuid.uuid4()),
                facets=[],
                description="This is a test",
                cause=[]
            )

            self.assertTrue(response["uuid"] is not None, "Dataset from flow created")

        except Exception as e:

            self.assertTrue(False, e)
