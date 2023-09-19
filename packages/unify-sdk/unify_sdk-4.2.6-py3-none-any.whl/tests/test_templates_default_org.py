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
from unify.templates import Templates
import json
import os
import uuid
from tests import test_org, cluster_name, props


class TestTemplatesWithDefaultOrg(unittest.TestCase):
    templates = Templates(cluster_name, props, org_id=test_org)
    templates.upload_string_content_file(
        test_org,
        """Template Name,Attribute,Datatype,UoM,Attribute Type
        Conveyer,Vibration,Float4,hz,""")
    test_template = templates.list_asset_templates()[0]
    template_id = test_template['id']
    template_name = test_template['name']
    version = test_template['version']

    def test_category(self):
        categories = ['python sdk test', 'antoher category']
        self.templates.category(template_id=self.template_id, template_name=self.template_name, version=self.version,
                                categories=categories)

        all_categories = self.templates.list_all_categories()
        self.assertListEqual(list(all_categories.keys()), categories)

        template_category_ids = self.templates.get_template(template_id=self.template_id)['categoryIds']
        self.assertListEqual(list(all_categories.values()), template_category_ids)

    def test_category_with_existing_category(self):
        categories = ['python sdk test']
        self.templates.category(
            template_id=self.template_id,
            template_name=self.template_name,
            version=self.version,
            categories=categories
        )

        new_categories = ['python sdk test', 'antoher category']
        self.templates.category(
            template_id=self.template_id,
            template_name=self.template_name,
            version=self.version,
            categories=new_categories
        )

        all_categories = self.templates.list_all_categories()
        self.assertListEqual(list(all_categories.keys()), new_categories)

        template_category_ids = self.templates.get_template(template_id=self.template_id)['categoryIds']
        self.assertListEqual(list(all_categories.values()), template_category_ids)

    def test_add_attributes(self):
        name = str(uuid.uuid4())
        create = self.templates.create_template_attribute_params(
            template_id=self.template_id,
            attribute_name=str(uuid.uuid4()),
            sanitized_name=name.replace("-", "_"),
            data_type="Int32",
            attribute_type="limitLow",
            description=str(uuid.uuid4()),
            uom=str(uuid.uuid4()),
            interpolation="Lookback"
        )
        self.assertTrue("id" in create, create)

    def test_unit_of_measure_list(self):
        """
        Verify org has UOM list

        :return:
        """

        uom_list = self.templates.get_uom()

        self.assertTrue(len(uom_list["items"]) > 0)
