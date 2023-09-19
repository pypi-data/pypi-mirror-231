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
import json
from tests import *


class TestPipelinesDefaultOrg(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.pipeline = Pipelines(
            cluster=cluster_name,
            props=props,
            org_id=test_org
        )

    def test_create_pipeline(self):
        new_pipe = self.pipeline.create_pipeline(
            name=str(uuid.uuid4()),
            function=False
        )

        self.assertTrue('pipeline' in new_pipe, new_pipe)
        self.assertTrue('id' in new_pipe["pipeline"], new_pipe)
        self.assertTrue('data' in new_pipe["pipeline"], new_pipe)
        self.assertTrue('pipelineType' in new_pipe["pipeline"]["data"], new_pipe)
        self.assertEqual("standard", new_pipe["pipeline"]["data"]["pipelineType"], new_pipe)

    def test_create_function(self):
        new_pipe = self.pipeline.create_pipeline(
            name=str(uuid.uuid4()),
            function=True
        )

        self.assertTrue('pipeline' in new_pipe, new_pipe)
        self.assertTrue('id' in new_pipe["pipeline"], new_pipe)
        self.assertTrue('data' in new_pipe["pipeline"], new_pipe)
        self.assertTrue('pipelineType' in new_pipe["pipeline"]["data"], new_pipe)
        self.assertEqual("function", new_pipe["pipeline"]["data"]["pipelineType"], new_pipe)

    def test_get_pipelines_v2(self):
        pipe_list = self.pipeline.get_pipelines_v2()

        self.assertTrue(len(pipe_list) > 0, pipe_list)

    def test_get_pipeline(self):

        try:
            pipe_list = self.pipeline.get_pipeline(
                pipeline_id=test_pipeline["pipeline"]["id"]
            )
            self.assertTrue(True, pipe_list)
        except Exception as e:
            self.assertTrue(False, e)

    def test_regular_duplicate(self):
        duplicate = self.pipeline.regular_duplicate(
            pipeline_id=test_pipeline["pipeline"]["id"],
            new_name=str(uuid.uuid4())
        )
        self.assertTrue("id" in duplicate, duplicate)

    def test_regular_duplicate_id_required(self):

        try:
            _ = self.pipeline.regular_duplicate(
                pipeline_id=test_pipeline["pipeline"]["id"]
            )
            self.assertTrue(False, "Duplicate must require pipeline id")
        except Exception as e:

            self.assertTrue(True, e)

    def test_regular_duplicate_name_required(self):

        try:
            _ = self.pipeline.regular_duplicate(
                pipeline_id=test_pipeline["pipeline"]["id"]
            )
            self.assertTrue(False, "Duplicate must require new name")
        except Exception as e:

            self.assertTrue(True, e)

    def test_verify_if_pipeline_exists_and_get_id(self):
        pipeline_id = self.pipeline.verify_if_pipeline_exists_and_get_id(
            pipeline_name=test_pipeline["pipeline"]["data"]["name"]
        )

        self.assertTrue("pipeline_id" in pipeline_id)
        self.assertTrue(pipeline_id["pipeline_id"] is not None)

    def test_verify_if_pipeline_exists_and_get_id_negative(self):
        pipeline_id = self.pipeline.verify_if_pipeline_exists_and_get_id(
            pipeline_name="{}{}".format(str(uuid.uuid4()), str(uuid.uuid4()))
        )

        self.assertTrue("pipeline_id" in pipeline_id)
        self.assertTrue(pipeline_id["pipeline_id"] is None)

    def test_verify_if_pipeline_exists_and_get_id_name_required(self):
        try:
            _ = self.pipeline.verify_if_pipeline_exists_and_get_id()
            self.assertTrue(True, "verify_if_pipeline_exists_and_get_id method requires pipeline name")
        except Exception as e:
            self.assertTrue(True, e)

    def test_pipeline_exists(self):

        self.assertTrue(
            self.pipeline.pipeline_exists(
                pipeline_name=test_pipeline["pipeline"]["data"]["name"]
            ),
            "Pipeline does not exists"
        )

    def test_pipeline_exists_negative(self):

        self.assertFalse(
            self.pipeline.pipeline_exists(
                pipeline_name="{}{}".format(str(uuid.uuid4()), str(uuid.uuid4()))
            ),
            "Non existing pipeline exists"
        )

    def test_pipeline_exists_name_required(self):
        try:
            _ = self.pipeline.pipeline_exists()
            self.assertTrue(True, "pipeline_exists method requires pipeline name")
        except Exception as e:
            self.assertTrue(True, e)

    def test_rename_pipeline(self):
        new_pipe = self.pipeline.create_pipeline(
            name=str(uuid.uuid4()),
            function=False
        )
        self.assertTrue('id' in new_pipe["pipeline"], new_pipe)

        try:
            _ = self.pipeline.update_pipeline_metadata(
                pipeline_id=new_pipe["pipeline"]["id"],
                name="{}__renamed".format(str(uuid.uuid4()))
            )
            self.assertTrue(True, "Pipeline was renamed")
        except Exception as e:
            self.assertTrue(False, e)

    def test_add_facets_pipeline(self):
        original_name = "Add facets {}".format(str(uuid.uuid4())[:10])
        new_pipe = self.pipeline.create_pipeline(
            name=original_name,
            function=False,
        )

        try:
            _ = self.pipeline.update_pipeline_metadata(

                pipeline_id=new_pipe["pipeline"]["id"],
                facets=[str(uuid.uuid4())[:10]]
            )
            self.assertTrue(True, "Facets were added to Pipeline")
        except Exception as e:
            self.assertTrue(False, e)

    def test_add_description_pipeline(self):
        original_name = "Add description {}".format(str(uuid.uuid4())[:10])
        new_pipe = self.pipeline.create_pipeline(
            name=original_name,
            function=False
        )

        try:
            _ = self.pipeline.update_pipeline_metadata(
                pipeline_id=new_pipe["pipeline"]["id"],
                description=str(uuid.uuid4())
            )

            self.assertTrue(True, "Description added to Pipeline")
        except Exception as e:
            self.assertTrue(False, e)

    def test_wait_for_pipeline(self):
        """
        Verify waitfor pipeline endpoint with default org
        :return:
        """
        try:
            _ = self.pipeline.wait_for_pipeline(
                pipeline_id=test_pipeline["pipeline"]["id"]
            )

            self.assertTrue(True, "Pipeline became ready")
        except Exception as e:
            self.assertTrue(False, e)

    def test_group_components(self):
        original_name = "Group components {}".format(str(uuid.uuid4())[:10])
        new_pipe = self.pipeline.create_pipeline(
            name=original_name,
            function=False,
            org_id=test_org
        )

        self.pipeline.wait_for_pipeline(
            org_id=test_org,
            pipeline_id=new_pipe["pipeline"]["id"]
        )

        self.pipeline.update_pipeline_from_json(
            update_payload=json.loads(open("tests/data/pipeline.json", "r+").read()),
            pipeline_name=original_name,
            pipeline_id=new_pipe["pipeline"]["id"],
            org_id=test_org,
        )

        try:
            response = self.pipeline.group_components(
                pipeline_id=new_pipe["pipeline"]["id"],
                components=["44564", "674714"]
            )
            self.assertTrue(True, response)
        except Exception as e:
            self.assertTrue(False, e)
