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

"""
Contains methods to interact with pipeline api
"""
import json
import uuid
import logging

from tempfile import mkstemp

from unify.generalutils import json_to_csv
from unify.properties import Properties
from unify.properties import ClusterSetting
from unify.apirequestsmng import ApiRequestManager
from unify.helpers.SingleOrg import single_org
from unify.helpers.graph_ql.pipeline_gql import PipelineGrapql


class Pipelines(ApiRequestManager):
    """
    Class to interact with pipeline endpoints
    """

    def __init__(self, cluster=None, props=Properties(ClusterSetting.KEY_RING), org_id=None):
        """
        Class constructor

        :param cluster: Cluster name to be used
        :type cluster: str
        :param props: Properties instantiated object
        :type props: class:`unify.properties.Properties`
        """

        self.logger = logging.getLogger(__name__)

        super().__init__(cluster=cluster, props=props, org_id=org_id)

        try:

            remote = self.props.get_remote(self.cluster)

            self.pipelines_url = self.props.get_remote(
                self.cluster) + "tags/org/" + '{}' + "/pipelines"

            self.regular_duplicate_url = self.pipelines_url + "/v2/{}/duplicate"

            self.delete_pipeline_url = self.pipelines_url + '/{}'

            self.pipeline_url = self.pipelines_url + '/{}'

            self.flow_url = self.pipeline_url + '/flows/{}'

            self.run_pipeline_url = self.pipeline_url + '/run'

            self.run_pipeline_status_url = self.pipeline_url + '/status'

            self.create_map_attributes_transf = self.pipeline_url + "/components/{}/map-attribute-rules"

            self.pipelines_url_v2 = self.pipelines_url + "/v2/{}"

            self.autosync_url = remote + "tags/org/{}/pipelines/{}/autosync"

            self.retrieve_pipelines_v2 = remote + "tags/org/" + '{}' + "/pipelines/v2"

            self.duplicate_pipeline_url = self.pipelines_url_v2 + "/duplicate"

            self.published_pipelines_url = remote + 'api/orgs/{}/graphs/current/pipelines'

            self.preview_data_pipeline = self.flow_url + '/preview?pageNum=1&sortKey={}&sortDir=ASC'

            self.download_map_attribute_rules = remote + 'tags/org/{}/pipelines/{}/components/{}/map-attribute-rules/csv'

            self.flow_preview_url = self.flow_url + '/preview?pageNum=1'

            self.download_flow_url = self.props.get_remote(
                self.cluster
            ) + "tags/org/{}/pipelines/{}/flows/{}/download"

            self.rules_by_templates_url = remote + "tags/org/{}/pipelines/{}/components/{}/map-attribute-rules/rules-by-template"

            self.distinct_values_map_attributes = self.props.get_remote(
                self.cluster) + "tags/org/{}/pipelines/{}/flows/{}/distinctValuesWithCount"

            self.apply_map_attributes_url = self.props.get_remote(
                self.cluster) + "tags/org/{}/pipelines/{}/components/{}/map-attribute-rules"

            self.count_endpoint = self.props.get_remote(self.cluster) + "tags/org/{}/pipelines/{}/flows/{}/count"

            self.distinct_count_values_url = self.props.get_remote(
                self.cluster) + 'tags/org/{}/pipelines/{}/flows/{}/distinctValuesWithCount'

            self.distinct_values_url = self.props.get_remote(
                self.cluster) + 'tags/org/{}/pipelines/{}/flows/{}/distinctValues'

            self.group_components_url = self.pipeline_url + "/groupComponents"

            self.gql_builder = PipelineGrapql()

        except Exception as error:
            raise error

    @single_org
    def apply_map_attributes(self, org_id=None, pipeline_id=None, component=None, payload=None):
        """
        Applies map attribute rules to given component

        :param org_id: Org id where the pipeline exists
        :type org_id: int or str
        :param pipeline_id: Pipeline where the map attributes component exists
        :type pipeline_id: int or str
        :param component: Map attribute component id where the rules are applied
        :type component: int or str
        :param payload: Dict representing mappings
        :type payload: dict
        :return:
        """

        final_url = self.apply_map_attributes_url.format(org_id, pipeline_id, component)

        header = self.build_header(
            org_id=org_id,
            aut_token=self.props.get_auth_token(cluster=self.cluster),
            others=self.delete_content_type_header
        )

        self.logger.debug("appling map attributes to %s (%s)", final_url, header)
        try:
            result = self.session.post(final_url, headers=header, data=json.dumps(payload))
            if result.status_code == 200:
                return json.loads(result.content)

            raise Exception(repr(result.content))
        except Exception as error:
            error_message = "map attributes couldn't be applied to {0}: {1}".format(final_url, error)
            # nb: we want to log the exception trace before raising a new error
            logging.exception(error_message)
            raise Exception(error_message)

    @single_org
    def regular_duplicate(self, org_id=None, *, pipeline_id, new_name):
        """
        Will duplicate the given pipeline on the given org
        :param org_id:
        :param pipeline_id:
        :param new_name:
        :return:
        """
        if pipeline_id is None:
            raise Exception("Pipeline id cant be null")
        if new_name is None:
            raise Exception("New pipeline name cant be none")

        headers = self.build_header(
            org_id=org_id,
            aut_token=self.props.get_auth_token(cluster=self.cluster),
            others={"Content-Type": "application/json"}
        )

        upload_url = self.regular_duplicate_url.format(org_id, pipeline_id)

        self.logger.debug("duplicating pipelines via %s (%s)", upload_url, headers)
        try:

            post_upload_file = self.session.post(
                upload_url,
                headers=headers,
                data=json.dumps({"name": new_name})
            )

            if post_upload_file.status_code == 200:
                response = json.loads(post_upload_file.content)

                if "sourceMetadata" in response:
                    del response["sourceMetadata"]

                return response

            raise Exception(repr(post_upload_file.content))
        except Exception as error:
            error_message = "pipeline couldn't be duplicated via {0}: {1}".format(upload_url, error)
            # nb: we want to log the exception trace before raising a new error
            logging.exception(error_message)
            raise Exception(error_message)

    @single_org
    def update_pipeline_from_json(self, org_id=None, update_payload=None, pipeline_id=None, pipeline_name=None,
                                  sources=None):
        """
        Updates a pipeline with a json content

        :param org_id: Org id where the pipeline is located
        :type org_id: int or str
        :param update_payload: JSON payload that contains pipeline content
        :type update_payload: dict
        :param pipeline_id: Pipeline identification
        :type pipeline_id: int or str
        :param pipeline_name: Pipeline current name
        :type pipeline_name: str
        :param sources: List of sources id to use
        :type sources: list of str
        :return:
        """

        header = self.build_header(
            org_id=org_id,
            aut_token=self.props.get_auth_token(cluster=self.cluster),
            others=self.content_type_header
        )

        update_payload["name"] = str(pipeline_name)

        index = 0

        for component in update_payload["components"]:
            if sources is not None and len(sources) > 0:
                if component["jsonClass"] == "JsonSourceRef":

                    if self.evergreen_enabled is False:
                        if "version" in component:
                            del component["version"]
                            component["sourceId"] = "100"

                    if isinstance(sources[index], int):
                        component["sourceId"] = int(sources[index])
                    else:
                        component["sourceId"] = sources[index]
                        if self.evergreen_enabled:
                            component["version"] = 1

                    index += 1
            if sources is None:
                if component["jsonClass"] == "JsonSourceRef":
                    if self.evergreen_enabled is False:
                        if "version" in component:
                            del component["version"]
                            component["sourceId"] = 1000

            if self.evergreen_enabled:
                if "version" not in component:
                    if component["jsonClass"] == "JsonSourceRef":
                        component["version"] = 1
                        component["sourceId"] = str(uuid.uuid4())

            if component["jsonClass"] == "JsonGraphSink":
                component["orgId"] = int(org_id)

        pipeline_url = self.pipeline_url.format(org_id, pipeline_id)
        self.logger.debug("updating pipeline %s (%s)", pipeline_url, header)

        try:
            update_pipeline_request = self.session.put(
                pipeline_url,
                headers=header,
                data=json.dumps(update_payload)
            )

            if update_pipeline_request.status_code == 200:
                return json.loads(update_pipeline_request.content)

            raise Exception(repr(update_pipeline_request.content))
        except Exception as error:
            error_message = "pipeline {0} couldn't be updated: {1}".format(pipeline_url, error)
            # nb: we want to log the exception trace before raising a new error
            logging.exception(error_message)
            raise Exception(error_message)

    @single_org
    def download_map_attributes(self, org_id=None, *, pipeline_id, component_id):
        """
        Downloads the map attributes data from the given pipeline

        :param org_id: Org id where the pipleine exists
        :type org_id: int or str
        :param pipeline_id: Pipeline id where the componentn exists
        :type pipeline_id: int or str
        :param component_id: Component where the map attributes are located
        :type component_id: int or str
        :return:
        """
        headers = self.build_header(
            org_id=org_id,
            aut_token=self.props.get_auth_token(cluster=self.cluster),
            others=self.content_type_header
        )

        download_rules = self.download_map_attribute_rules.format(
            org_id,
            pipeline_id,
            component_id
        )

        self.logger.debug("retrieving map attributes from %s (%s)", download_rules, headers)
        try:
            result = self.session.get(download_rules, headers=headers)

            if result.status_code == 200:
                return result.content

            raise Exception(repr(result.content))
        except Exception as error:
            error_message = "map attributes couldn't be retrieved from {0}: {1}".format(download_rules, error)
            # nb: we want to log the exception trace before raising a new error
            logging.exception(error_message)
            raise Exception(error_message)

    @single_org
    def upload_map_attributes_from_json(self, org_id=None, pipeline_id=None, component_id=None, json_data=None):
        """
        Uploads a json file to the given map attributes component

        :param org_id: Org id where the pipeline exists
        :type org_id: int or str
        :param pipeline_id: Pipeline id where to component id exists
        :type pipeline_id: int or str
        :param component_id: Map attributes component id exists
        :type component_id: int or str
        :param json_data: Contains the map attribute rules
        :type json_data: dict
        :return:
        """
        _, path = mkstemp(suffix=".csv")

        open(path, "wb").write(json_to_csv(data_array=json_data).encode())

        self.upload_map_attributes(
            org_id=org_id,
            pipeline_id=pipeline_id,
            component_id=component_id,
            csv_file=path
        )

    @single_org
    def upload_map_attributes(self, org_id=None, pipeline_id=None, component_id=None, csv_file=None):
        """
        Uploads a csv file to the given map attributes component

        :param org_id: Org id where the pipeline exists
        :type org_id: int or str
        :param pipeline_id: Pipeline id where to component id exists
        :type pipeline_id: int or str
        :param component_id: Map attributes component id exists
        :type component_id: int or str
        :param csv_file: CSV file that contains the map attribute rules
        :type csv_file: str
        :return:
        """

        headers = self.build_header(
            org_id=org_id,
            aut_token=self.props.get_auth_token(cluster=self.cluster),
            others={"'Content-Type'": "application/data"}
        )

        files = {'file': open(csv_file, "rb")}

        upload_url = self.download_map_attribute_rules.format(org_id, pipeline_id, component_id)

        self.logger.debug("uploading a csv for map attributes via %s (%s)", upload_url, headers)
        try:
            post_upload_file = self.session.post(
                upload_url,
                headers=headers,
                files=files
            )

            if post_upload_file.status_code == 200:
                response = json.loads(post_upload_file.content)

                if "sourceMetadata" in response:
                    del response["sourceMetadata"]

                return response

            raise Exception(repr(post_upload_file.content))
        except Exception as error:
            error_message = "map attributes couldn't be uploaded to {0}: {1}".format(upload_url, error)
            # nb: we want to log the exception trace before raising a new error
            logging.exception(error_message)
            raise Exception(error_message)

    @single_org
    def create_pipeline(self, name, org_id=None, function=False, is_stream=False):
        """
        Creates an empty pipeline

        :param name: New pipeline name
        :type name: str
        :param org_id: Org id where the pipeline is going to be created
        :type org_id: int or str
        :param function: Defines if the pipeline is a function or not
        :type function: boolean
        :param is_stream: Define if the pipeline is a stream pipeline
        :type is_stream: boolean
        :return:
        """

        header = self.build_header(
            org_id=org_id,
            aut_token=self.props.get_auth_token(cluster=self.cluster),
            others=self.content_type_header
        )

        payload = {"name": name, "components": [], "isStream": is_stream}

        if function:
            payload["pipelineType"] = "function"

        pipeline_url = self.pipelines_url.format(org_id)
        self.logger.debug("creating empty pipeline %s (%s) with body: %s", pipeline_url, header, payload)
        try:
            result = self.session.post(
                pipeline_url,
                headers=header,
                data=json.dumps(payload)
            )

            if result.status_code == 200:
                return json.loads(result.content)

            raise Exception(json.loads(result.content))
        except Exception as error:
            error_message = "empty pipeline couldn't be created via {0}: {1}".format(pipeline_url, error)
            # nb: we want to log the exception trace before raising a new error
            logging.exception(error_message)
            raise Exception(error_message)

    @single_org
    def download_flow(self, org_id=None, pipeline_id=None, flow_id=None, filetype='csv'):
        """
        Downloads the flow data

        :param org_id: Org where the piprline exists
        :type org_id: int or str
        :param pipeline_id: Pipeline id where the flow exists
        :type pipeline_id: int or str
        :param flow_id: Flow id to be queried
        :type flow_id: int or str
        :return:
        """

        header = self.build_header(
            org_id=org_id,
            aut_token=self.props.get_auth_token(cluster=self.cluster),
            others=self.content_type_header
        )

        cookies = {'_gid': 'GA1.1.1649742346.1580648966'}

        schema_url = self.download_flow_url.format(org_id, pipeline_id, flow_id)

        self.logger.debug("downloading pipeline flow from %s (%s)", schema_url, header)
        try:
            result = self.session.get(schema_url, headers=header, cookies=cookies, params=[('filetype',filetype)])

            if result.status_code == 200:
                return result.content

            raise Exception(repr(result.content))
        except Exception as error:
            error_message = "pipeline flow couldn't be downloaded from {0}: {1}".format(schema_url, error)
            # nb: we want to log the exception trace before raising a new error
            logging.exception(error_message)
            raise Exception(error_message)

    @single_org
    def get_pipeline(self, org_id=None, *, pipeline_id):
        """
        Retrieves pipeline json blob

        :param org_id: Org where the pipeline to be queried exists
        :type org_id: int or str
        :param pipeline_id: Pipeline id to be queried
        :type pipeline_id: int or str
        :return:
        """

        header = self.build_header(
            aut_token=self.props.get_auth_token(cluster=self.cluster),
            others=self.content_type_header
        )

        pipeline_url = self.pipeline_url.format(org_id, pipeline_id)

        self.logger.debug("retrieving pipeline info from %s (%s)", pipeline_url, header)
        try:
            result = self.session.get(pipeline_url, headers=header)
            if result.status_code == 200:
                return json.loads(result.content)

            raise Exception(repr(result.content))
        except Exception as error:
            error_message = "pipeline info couldn't be retrieved from {0}: {1}".format(pipeline_url, error)
            # nb: we want to log the exception trace before raising a new error
            logging.exception(error_message)
            raise Exception(error_message)

    @single_org
    def delete_pipeline(self, org_id=None, *, pipeline_id):
        """
        Deletes the given pipeline
        :param org_id:
        :param pipeline_id:
        :return:
        """

        header = self.build_header(
            org_id=org_id,
            aut_token=self.props.get_auth_token(cluster=self.cluster),
            others=self.content_type_header
        )

        pipeline_url = self.pipelines_url_v2.format(org_id, pipeline_id)

        self.logger.debug("deleting pipeline via %s (%s)", pipeline_url, header)
        try:
            result = self.session.delete(
                pipeline_url,
                headers=header
            )

            if result.status_code in [200, 201, 202]:
                return json.loads(result.content)

            raise Exception(repr(result.content))
        except Exception as error:
            error_message = "pipeline couldn't be deleted via {0}: {1}".format(pipeline_url, error)
            # nb: we want to log the exception trace before raising a new error
            logging.exception(error_message)
            raise Exception(error_message)

    @single_org
    def unpublish_pipeline(self, org_id=None, *, pipeline_id):
        """
        Unpublishes a pipeline from graph v1
        :param org_id:
        :param pipeline_id:
        :return:
        """
        header = self.build_header(
            org_id=org_id,
            aut_token=self.props.get_auth_token(cluster=self.cluster),
            others=self.content_type_header
        )

        update_payload = {"status": "draft"}

        pipeline_url = self.pipelines_url_v2.format(org_id, pipeline_id)

        self.logger.debug("unpublishing pipeline via PUT %s (%s) with body %s", pipeline_url, header, update_payload)
        try:
            response = self.session.put(
                pipeline_url,
                headers=header,
                data=json.dumps(update_payload)
            )

            if response.status_code in [200, 201, 202]:
                return json.loads(response.content)

            raise Exception(repr(response.content))
        except Exception as error:
            error_message = \
                "pipeline couldn't be unpublished via PUT {0} with body {1}: {2}" \
                    .format(pipeline_url, update_payload, error)
            # nb: we want to log the exception trace before raising a new error
            logging.exception(error_message)
            raise Exception(error_message)

    @single_org
    def get_map_attribute_rules(self, org_id=None, *, pipeline_id, component):
        """
        Downloads map attributes rules of the given pipeline component

        :param org_id: Org where pipeline lives
        :type org_id: int or str
        :param pipeline_id: Pipeline id to be queried
        :type pipeline_id: int or str
        :param component: Map attributes id component
        :type component: int or str
        :return:
        """

        header = self.build_header(
            org_id=org_id,
            aut_token=self.props.get_auth_token(cluster=self.cluster),
            others=self.content_type_header
        )

        final_url = self.rules_by_templates_url.format(org_id, pipeline_id, component)

        self.logger.debug("retrieving map attributes for %s (%s)", final_url, header)
        try:
            result = self.session.get(final_url, headers=header)

            if result.status_code == 200:
                return json.loads(result.content)

            raise Exception(repr(result.content))
        except Exception as error:
            error_message = "map attributes couldn't be retrieved from {0}: {1}".format(final_url, error)
            # nb: we want to log the exception trace before raising a new error
            logging.exception(error_message)
            raise Exception(error_message)

    @single_org
    def get_distinct_values_map_attributes(self, org_id=None, *, pipeline_id, flows, columns):
        """
        Retrieves distinct values from the given flow id

        :param org_id: Org id where the pipeline/flow is located
        :type org_id: int or str
        :param pipeline_id: Id of the pipeline to be queried
        :type pipeline_id: int or str
        :param flows: Flow id
        :type flows: int or str
        :param columns: Columns to used
        :type columns: list of str
        :return:
        """

        columns.append("TEMPLATE *")

        columns.append("SENSOR *")

        cols = []

        for col_name in columns:
            cols.append(('col', col_name))

        header = self.build_header(
            org_id=org_id,
            aut_token=self.props.get_auth_token(cluster=self.cluster),
            others=self.content_type_header
        )

        final_url = self.distinct_values_map_attributes.format(org_id, pipeline_id, flows)

        self.logger.debug("retrieving distinct values from flow %s (params: %s)(%s)", final_url, cols, header)
        try:

            result = self.session.get(final_url, headers=header, params=cols)

            if result.status_code == 200:
                return json.loads(result.content)

            raise Exception(repr(result.content))
        except Exception as error:
            error_message = "distinct values from flow couldn't be retrieved {0}: {1}".format(final_url, error)
            # nb: we want to log the exception trace before raising a new error
            logging.exception(error_message)
            raise Exception(error_message)

    @single_org
    def get_pipelines_v2(self, org_id=None, deleted=False, pipeline_type="standard", page_num=1, page_size=100):
        """
        Retrieves the pipeline list from the given org

        :param org_id: Org id to be queried
        :type org_id: int or str
        :param deleted: Deletion status fo pipeliens to be queried
        :type deleted: bool or None
        :param pipeline_type: Pipeline type standard or function
        :type pipeline_type: str
        :return:
        """

        if deleted is True:
            query = self.gql_builder.get_deleted_pipelines(pipeline_type=pipeline_type,
                                                           page_num=page_num,
                                                           page_size=page_size)
        elif deleted is False:
            query = self.gql_builder.get_non_deleted_pipelines(pipeline_type=pipeline_type,
                                                               page_num=page_num,
                                                               page_size=page_size)
        else:
            query = self.gql_builder.get_pipelines_query(pipeline_type=pipeline_type,
                                                         page_num=page_num,
                                                         page_size=page_size)

        self.logger.debug("retrieving pipeline list for org %s by querying: %s", org_id, query)
        try:
            get_pipelines_request = self.graph_ql_query(org_id=org_id, query=query)

            if get_pipelines_request.status_code in range(200, 202):
                data = json.loads(get_pipelines_request.content)
                if "data" in data:
                    if "artifacts" in data["data"]:
                        return data["data"]["artifacts"]

                return []
            raise Exception(repr(get_pipelines_request.content))
        except Exception as error:
            error_message = \
                "pipeline list couldn't be retrieved for org {0} by queryng: {1}. Error: {2}" \
                    .format(org_id, query, error)
            # nb: we want to log the exception trace before raising a new error
            logging.exception(error_message)
            raise Exception(error_message)

    @single_org
    def get_pipelines_functions(self, org_id=None, deleted=False, page_num=1, page_size=100):
        """
        Retrieves the pipeline list from the given org

        :param org_id: Org id to be queried
        :type org_id: int or str
        :param deleted: Deletion status fo pipeliens to be queried
        :type deleted: bool or None
        :return:
        """
        return self.get_pipelines_v2(org_id=org_id, deleted=deleted, pipeline_type="function", page_num=page_num,
                                     page_size=page_size)

    @single_org
    def verify_if_pipeline_exists_and_get_id(self, org_id=None, *, pipeline_name):
        """
        Verifies that the pipeline name exists on the given org. Returns pipeline id.

        :param org_id: Org id of pipeline
        :type org_id: int or str
        :param pipeline_name: Name of pipeline
        :type pipeline_name: str
        :return:
        """

        if pipeline_name is None:
            raise Exception("Pipeline name cant be none")

        pipeline_list = self.get_pipelines_v2(org_id=org_id)

        results = {"pipeline_id": None}

        for pipe in pipeline_list:
            if pipe["name"] == pipeline_name:
                existing_pipeline_id = pipe["id"]["id"]
                results.update({"pipeline_id": existing_pipeline_id})
                break

        return results

    @single_org
    def pipeline_exists(self, org_id=None, *, pipeline_name):
        """
        Verifies that the pipeline name exists on the given org

        :param org_id: Org to query if the pipeline exists
        :type org_id: int or str
        :param pipeline_name: Pipeline name to be queried
        :type pipeline_name: str
        :return:
        """
        if pipeline_name is None:
            raise Exception("Pipeline name cant be none")

        return self.verify_if_pipeline_exists_and_get_id(
            org_id=org_id,
            pipeline_name=pipeline_name
        )["pipeline_id"] is not None

    @single_org
    def update_pipeline_metadata(self, org_id=None, *, pipeline_id=None, name=None, description=None, facets=None):
        """
        Method to update a pipeline's metadata

        :param org_id: org id where the pipeline is stored
        :param pipeline_id: id of the pipeline to be edited
        :param name: new pipeline name
        :param description: description to be added
        :param facets:
        :return:
        """

        return self.update_artifact_metadata(
            org_id=org_id,
            artifact_id=pipeline_id,
            artifact_type="pipeline",
            name=name,
            description=description,
            facets=facets
        )

    @single_org
    def preview_flow(self, org_id=None, *, pipeline_id, flow_id):

        """
        Previews the given flow with default ordering
        :param org_id:
        :param pipeline_id:
        :param flow_id:
        :return:
        """

        header = self.build_header(
            org_id=str(org_id),
            aut_token=self.props.get_auth_token(cluster=self.cluster),
            others=self.content_type_header
        )

        cookies = {'_gid': 'GA1.1.1649742346.1580648966'}

        schema_url = self.flow_preview_url.format(org_id, pipeline_id, flow_id)

        self.logger.debug("preview flow from %s (%s)", schema_url, header)
        try:
            flow_data = self.session.get(
                schema_url,
                headers=header,
                cookies=cookies
            )

            if flow_data.status_code in [200, 201, 202]:
                return json.loads(flow_data.content)

            raise Exception(repr(flow_data.content))
        except Exception as error:
            error_message = "preview flow couldn't be retrieved from {0}: {1}".format(schema_url, error)
            # nb: we want to log the exception trace before raising a new error
            logging.exception(error_message)
            raise Exception(error_message)

    @single_org
    def preview_flow_by_column(self, org_id=None, *, pipeline_id, flow_id, sort_column):

        """
        Previews the given flow ordered by the column name give
        :param org_id:
        :param pipeline_id:
        :param flow_id:
        :param sort_column:
        :return:
        """

        header = self.build_header(
            org_id=str(org_id),
            aut_token=self.props.get_auth_token(cluster=self.cluster),
            others=self.content_type_header
        )

        schema_url = self.preview_data_pipeline.format(org_id, pipeline_id, flow_id, sort_column)

        self.logger.debug("preview flow by column name via %s (%s)", schema_url, header)
        try:
            request = self.session.get(schema_url, headers=header)

            if request.status_code in [200, 201, 202]:
                return json.loads(request.content)

            raise Exception(repr(request.content))
        except Exception as error:
            error_message = "preview flow by column name couldn't be retrieved from {0}: {1}".format(schema_url, error)
            # nb: we want to log the exception trace before raising a new error
            logging.exception(error_message)
            raise Exception(error_message)

    @single_org
    def flow_row_count(self, org_id=None, *, pipeline_id=None, flow_id=None):

        """
        Retrieves the number of rows the given flow contains
        :param org_id:
        :param pipeline_id:
        :param flow_id:
        :return:
        """

        header = self.build_header(
            org_id=str(org_id),
            aut_token=self.props.get_auth_token(cluster=self.cluster),
            others=self.content_type_header
        )

        schema_url = self.count_endpoint.format(org_id, pipeline_id, flow_id)

        self.logger.debug("retrieving the number of rows for a flow from %s (%s)", schema_url, header)
        try:
            request = self.session.get(schema_url, headers=header)

            if request.status_code in [200, 201, 202]:
                return json.loads(request.content)

            raise Exception(repr(request.content))
        except Exception as error:
            error_message = "the number of rows couldn't be retrieved from flow {0}: {1}".format(schema_url, error)
            # nb: we want to log the exception trace before raising a new error
            logging.exception(error_message)
            raise Exception(error_message)

    @single_org
    def publish_pipeline(self, org_id=None, *, pipeline_id):

        """
        Published pipeline
        :param org_id:
        :param pipeline_id:
        :return:
        """

        header = self.build_header(
            org_id=str(org_id),
            aut_token=self.props.get_auth_token(cluster=self.cluster),
            others=self.content_type_header
        )

        run_url = self.run_pipeline_url.format(org_id, pipeline_id)

        params = [("parquet", True)]

        self.logger.debug("publishing pipeline %s with params: %s (%s)", run_url, params, header)
        try:
            run_request = self.session.post(run_url, headers=header, params=params)

            if run_request.status_code in [200, 201, 202]:
                return json.loads(run_request.content)

            raise Exception(repr(run_request.content))
        except Exception as error:
            error_message = \
                "pipeline couldn't be published via {0} with params: {1}: Error: {2}" \
                    .format(run_url, params, error)
            # nb: we want to log the exception trace before raising a new error
            logging.exception(error_message)
            raise Exception(error_message)

    @single_org
    def get_flow_distinct_values(self, org_id=None, *, pipeline_id, flow_id, col, sort_key, count=False):
        """
        Returns distinct values from a given flow, if count is true, it will return the count per distinct value
        :param org_id:
        :param pipeline_id:
        :param flow_id:
        :param col:
        :param sort_key:
        :param count:
        :return:
        """
        headers = self.build_header(
            org_id=str(org_id),
            aut_token=self.props.get_auth_token(cluster=self.cluster),
            others=self.content_type_header
        )

        if count:
            get_distinct_vals = self.distinct_count_values_url.format(org_id, pipeline_id, flow_id)
        else:
            get_distinct_vals = self.distinct_values_url.format(org_id, pipeline_id, flow_id)

        data = [("col", col), ("sortKey", sort_key), ("sortDir", "ASC")]

        self.logger.debug(
            "retrieving distinct values for %s flow with params: %s (%s)",
            get_distinct_vals, data, headers)

        try:
            result = self.session.get(get_distinct_vals, headers=headers, params=data)

            if result.status_code in [200, 201, 202]:
                return json.loads(result.content)

            raise Exception(repr(result.content))
        except Exception as error:
            error_message = \
                "pdistinct values couldn't be retrieved for flow {0} with params {1}. Error: {2}" \
                    .format(get_distinct_vals, data, error)
            # nb: we want to log the exception trace before raising a new error
            logging.exception(error_message)
            raise Exception(error_message)

    @single_org
    def autosync_pipeline(self, org_id=None, *, pipeline_id, autoSyncEnabled=True):

        """
        Changes the autosync status of a pipeline
        :param org_id:
        :param pipeline_id:
        :param autoSyncEnabled:
        :return:
        """
        headers = self.build_header(
            org_id=str(org_id),
            aut_token=self.props.get_auth_token(cluster=self.cluster),
            others=self.content_type_header
        )

        payload = {"autoSyncEnabled": autoSyncEnabled}

        pipeline_url = self.autosync_url.format(org_id, pipeline_id)

        self.logger.debug("updating autosync status for pipeline %s (body: %s) (%s)", pipeline_url, payload, headers)
        try:
            post_pipeline_request = self.session.put(
                pipeline_url,
                headers=headers,
                data=json.dumps(payload)
            )

            if post_pipeline_request.status_code in [200, 201, 202]:
                return json.loads(post_pipeline_request.content)

            raise Exception(repr(post_pipeline_request.content))
        except Exception as error:
            error_message = "pipeline autosync status couldn't be updated via {0}: {1}".format(pipeline_url, error)
            # nb: we want to log the exception trace before raising a new error
            logging.exception(error_message)
            raise Exception(error_message)

    @single_org
    def get_pipeline_run_status(self, org_id=None, *, pipeline_id):
        """
        Returns distinct values from a given flow, if count is true, it will return the count per distinct value
        :param org_id:
        :param pipeline_id:
        :param flow_id:
        :param col:
        :param sort_key:
        :param count:
        :return:
        """

        header = self.build_header(
            org_id=str(org_id),
            aut_token=self.props.get_auth_token(cluster=self.cluster),
            others=self.content_type_header
        )

        status_url = self.run_pipeline_status_url.format(org_id, pipeline_id)

        self.logger.debug("retrieving pipeline run status from %s (%s)", status_url, header)
        try:
            run_request = self.session.get(status_url, headers=header)

            return run_request.status_code, json.loads(run_request.content)
        except Exception as error:
            error_message = "pipeline run status couldn't be retrieved from {0}: {1}".format(status_url, error)
            # nb: we want to log the exception trace before raising a new error
            logging.exception(error_message)
            raise Exception(error_message)

    @single_org
    def wait_for_pipeline(self, org_id=None, *, pipeline_id):
        """
        Wait for a pipeline to be ready to be used

        :param org_id: Organization id where the pipeline was created
        :param pipeline_id: pipeline id number
        :return:
        """

        return self.wait_for_artifact(
            org_id=org_id,
            artifact_id=pipeline_id,
            artifact_type="pipeline"
        )

    @single_org
    def group_components(self, org_id=None, *, pipeline_id, components: list = None):
        """
        Group pipeline components

        :param org_id: org id where the pipeline is stored
        :param pipeline_id: id of the pipeline to be edited
        :param components: list of pipeline components ids to be grouped
        :return:
        """

        if components is None or len(components) == 0:
            raise Exception("Component list must have at least one ID")

        headers = self.build_header(
            org_id=str(org_id),
            aut_token=self.props.get_auth_token(cluster=self.cluster),
            others=self.content_type_header
        )

        pipeline_url = self.group_components_url.format(org_id, pipeline_id)

        payload = {"componentIds": components}

        self.logger.debug("gouping pipeline components via %s (%s) (%s)", pipeline_url, payload, headers)
        try:

            post_pipeline_request = self.session.post(
                pipeline_url,
                headers=headers,
                data=json.dumps(payload)
            )

            if post_pipeline_request.status_code in self.OK:
                return json.loads(post_pipeline_request.content)

            raise Exception(repr(post_pipeline_request.content))
        except Exception as error:
            error_message = "pipeline components couldn't be grouped via {0}: {1}".format(pipeline_url, error)
            # nb: we want to log the exception trace before raising a new error
            logging.exception(error_message)
            raise Exception(error_message)
