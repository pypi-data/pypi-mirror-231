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

import os
import uuid

from unify.orgadmin import OrgAdmin
from unify.properties import Properties
from unify.properties import ClusterSetting
from unify.sources import Sources
from unify.pipelines import Pipelines
from unify.apimanager import ApiManager
from unify.connectors import Connectors
from unify.WaitingLibrary import Wait

cluster_name = "data"


def user_is_loged_in_to_org(prp, org_id):
    with Sources(cluster=cluster_name, props=prp) as s_admin:
        try:
            s_admin.get_sources(org_id=org_id)
            return True
        except:
            return False


props = Properties(clusterSetting=ClusterSetting.MEMORY)

props.store_cluster(
    username=os.environ.get("username"),
    password=os.environ.get("password"),
    name=cluster_name,
    cluster=os.environ.get("cluster")
)

org_admin = OrgAdmin(props=props, cluster=cluster_name)

test_org = org_admin.create_organization(
    org_name="zQA-{}".format(str(uuid.uuid4()))
)

Wait(timeout=200).until(user_is_loged_in_to_org, "User never available in org", props, test_org)

sources = Sources(cluster=cluster_name, props=props)

test_dataset = sources.static_file_upload(
    name="table_{}".format(str(uuid.uuid4())[:12]),
    org_id=test_org,
    content="tests/data_test.csv"
)


pipelines = Pipelines(cluster=cluster_name, props=props)

test_pipeline = pipelines.create_pipeline(name=str(uuid.uuid4()), org_id=test_org)

pipelines.wait_for_pipeline(
    org_id=test_org,
    pipeline_id=test_pipeline["pipeline"]["id"]
)

api_manager = ApiManager(cluster=cluster_name, props=props)

test_hierarchy = api_manager.create_hierarchy(name=str(uuid.uuid4()), org_id=test_org)

connectors = Connectors(cluster=cluster_name, props=props)

test_connector = None
# test_connector = connectors.create_connector(
#    org_id=test_org,
#    name=str(uuid.uuid4()),
#    connector_type='connector_test_type',
#    config={'a':'b'},
# )


print("--------Created organization {} for testing------", format(test_org))
