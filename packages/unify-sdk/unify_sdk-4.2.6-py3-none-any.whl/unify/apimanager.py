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
Contains support methods for export and import workflows
"""
import json
import os.path
import uuid
import logging

from tempfile import mkstemp

from unify.properties import ClusterSetting
from unify.orgadmin import OrgAdmin
from unify.properties import Properties
from unify.templates import Templates
from unify.pipelines import Pipelines
from unify.sources import Sources
from unify.generalutils import json_to_csv
from unify.generalutils import csv_to_json
from unify.apiutils import remove_special
from unify.assetaccess import AssetAccess
from unify.graph import Graph
from unify.hierarchies import Hierarchy
from unify.helpers.SingleOrg import single_org
from unify.permissions import Permissions
from unify.helpers.Permissions import ArtifactType


class ApiManager:
    """
    Class to interact with import and export dataset methods
    """

    def __init__(self, cluster=None, props=Properties(ClusterSetting.KEY_RING), org_id=None):

        self.logger = logging.getLogger(__name__)

        try:

            self.properties = props

            self.evergreen_enabled = self.properties.get_asset_sync(cluster=cluster)

            self.orgs = OrgAdmin(cluster=cluster, props=self.properties)

            self.templates = Templates(cluster=cluster, props=self.properties, org_id=org_id)

            self.pipelines = Pipelines(cluster=cluster, props=self.properties)

            self.sources = Sources(cluster=cluster, props=self.properties)

            self.graphs = Graph(cluster=cluster, props=self.properties)

            self.hierarchies = Hierarchy(cluster=cluster, props=self.properties)

            self.permissions = Permissions(cluster=cluster, props=self.properties)

            self.cluster = cluster

            self.sources.evergreen_enabled = self.evergreen_enabled

            self.pipelines.evergreen_enabled = self.evergreen_enabled

            self.org_id = org_id

        except Exception as error:
            raise error

    @single_org
    def delete_source(self, org_id=None, *, source_id):

        return self.sources.delete_source(
            org_id=org_id,
            source_id=source_id
        )

    def query_graph(self, org, graph, query, json_format):
        """
        Create a cypher query request

        :param org: Org where the graph to be queried is stored
        :param graph: Graph uuid to be queried
        :param query: String that contains cypher query
        :param json_format: return the results in a universal correctly json o json lines
        :return:
        """

        return self.graphs.query_graph(
            org_id=org,
            graph=graph,
            query=query,
            json_format=json_format
        )

    @single_org
    def graphs_list(self, org_id=None):
        """
        Return the list of graphs on a given org

        :param org_id: Org ID that wants to be queried
        :return: Json list with graph on the org
        """
        return self.graphs.get_graphs_list(org_id=org_id)

    @single_org
    def regular_pipeline_duplicate(self, org_id=None, *, pipeline_id, new_name):
        """
        Duplicate a given pipeline on the same org

        :param org_id: Org id where the pipeline is stored
        :param pipeline_id: Pipeline id that will be duplicated
        :param new_name: The new pipeline's name
        :return:
        """
        return self.pipelines.regular_duplicate(
            org_id=org_id,
            pipeline_id=pipeline_id,
            new_name=new_name
        )

    def import_source(self, content, orgid, name, type, encoding="UTF-8", chunks=10000):
        """
        Creates a new dataset with content. Option to chunk the amount of lines that the file will be partitioned

        :param content: CSV or TSV file content
        :type content: str
        :param orgid: Org where the source will be imported
        :type orgid: int or str
        :param name: Name to be given to the datasource
        :type name: str
        :param type: Type of the dataset. Accepts "external" or "generic"
        :type type: str
        :param encoding: File encoding
        :type encoding: str
        :param chunks: Number of chunks to split a large dataset,
        :type chunks: int
        :return:
        """
        if type == "external":

            file_dir, path = mkstemp(suffix=".csv")

            open(path, "wb").write(content.encode())

            new_source = self.sources.static_file_upload(
                name=name,
                content=path,
                org_id=orgid
            )

            os.close(file_dir)

            if "sourceMetadata" in new_source:
                del new_source["sourceMetadata"]

            return new_source

        elif type == "generic":

            return self.sources.upload_big_dataset(
                name=name,
                org_id=orgid,
                content=content,
                encoding=encoding,
                chunks=chunks
            )

        elif type == "split":
            return self.sources.divide_dataset_in(
                name=name,
                org_id=orgid,
                content=content,
                encoding=encoding,
                chunks=chunks
            )

        raise Exception("Unsupported type of source to be imported")

    @single_org
    def export_source(self, org_id=None, *, dataset_ids):
        """
        Retrieves the content of a dataset

        :param org_id: org id where the dataset is located
        :type org_id: int or str
        :param dataset_ids: dataset id to be retrieved
        :type dataset_ids: list of str
        :return:
        """
        return self.sources.create_export_dataset(
            org_id=org_id,
            dataset_ids=dataset_ids
        )

    def append_data(self, content, orgid, dataset_id):
        """
        Appends content to a dataset

        :param content: dataset comntent to be appended
        :type content: str
        :param orgid: org id where the target dataset lives
        :type orgid: int or str
        :param dataset_id: dataset id
        :type dataset_id: str
        :return:
        """
        return self.sources.append_dataset(
            org_id=orgid,
            data_set_id=dataset_id,
            content=content
        )

    @single_org
    def dataset_list(self, org_id=None, page_num=1, page_size=1000):
        """
        Retrieves metadata for all datasets on a given org, as long as there
        are 1000 or less. For more than 1k, page through the results by
        incrementing page_num (or increasing page_size)

        :param org_id: ORG id to be queried
        :type org_id: ORG id to be queried
        :param page_num: page number of results
        :param page_size: number of results per page
        :return:
        """
        try:
            sources = self.sources.get_sources(org_id=org_id, page_num=page_num, page_size=page_size)

            for source in sources:
                if "schema" in source:
                    del source["schema"]

            return sources
        except Exception as error:
            raise error

    @single_org
    def pipeline_list(self, org_id=None, page_num=1, page_size=100):
        """
        Retrieves metadata for all pipelines on a given org

        :param org_id: ORG id to be queried
        :type org_id: ORG id to be queried
        :return:
        """
        try:
            return self.pipelines.get_pipelines_v2(org_id=org_id, page_num=page_num, page_size=page_size)

        except Exception as error:
            raise error

    def execute_query(self, query, orgid, format):
        """
        Executes the given sql query through Unify Access on a given org

        :param query: Query
        :type query: str
        :param orgid: Org id to query
        :type orgid: int or str
        :param format: Result format. Accepts "CSV".
        :type format: str
        :return:
        """

        access = AssetAccess(cluster=self.cluster, orgid=orgid, props=self.properties)

        result = access.execute_query(query=query)

        if format == "csv":
            return json_to_csv(result, io_format=False)

        return result

    def export_function(self, org_id, function):
        """
        Create a json structure with all the components needed to import a function

        :param org_id:
        :param function:
        :return:
        """
        return self.create_pipeline_export_data(
            org_id=org_id,
            pipeline_id=function,
            skip=[]
        )

    def assethub_access_tables(self, orgid):
        """
        Retrieves all Unify Access tables on the given org

        :param orgid: Org id to query the asset access tables
        :type orgid: int or str
        :return:
        """
        access = AssetAccess(cluster=self.cluster, orgid=orgid, props=self.properties)

        return access.get_all_tables()

    def import_sources(self, org_id, pipeline_id, content, handleduplicates="clone", update_pipeline=True):
        """
        Import the datasets, this method is used on the wf import pipelines

        :param org_id: Org id where the sources are going to be imported
        :type org_id: int or str
        :param pipeline_id: In case the sources that are imported and a pipeline used then
        :type pipeline_id: int or str
        :param content: Content file has all the data.
        :type content: str
        :param handleduplicates: In case there is a dataset with the same name. Accept "clone"
        :type handleduplicates: str, optional
        :param update_pipeline: Flag to update the pipeline
        :type update_pipeline: bool, optional
        :return:
        """

        try:
            data = json.loads(content)

            non_evergreen_conversion_type = {
                "JsonPiConfigFileSourceMetaData": "piconfig",
                "JsonFileSourceMetadata": "external",
                "JsonPiWebApiSourceMetadata": "web",
                "PI_Upload": "piconfig",
                "Upload": "external",
                "api_dataset": "api_dataset",
                "PiWeb": "web"
            }

            needed_keys = {"id", "component", "schema", "type", "file_content", "name"}

            already_created_by_name = {}

            msg = []

            for source_to_import in data:

                if needed_keys.issubset(source_to_import.keys()):

                    if source_to_import["type"] in non_evergreen_conversion_type:

                        which_type = non_evergreen_conversion_type[source_to_import["type"]]

                    else:
                        which_type = "api_dataset"

                    if which_type in ["api_dataset"]:
                        new_source = self.sources.create_api_data_set_with_content(
                            name=source_to_import["name"],
                            org_id=org_id,
                            content=json_to_csv(
                                source_to_import["file_content"],
                                io_format=False
                            )
                        )

                        self.sources.wait_for_dataset(org_id=org_id, dataset_id=new_source["data_set_id"])

                        source_to_import["new_source_id"] = new_source["data_set_id"]

                        msg.append("DataSource '{}' imported successfully".format(source_to_import["name"]))

                    if which_type in ["external"]:

                        file_dir, path = mkstemp(suffix=".csv")

                        open(path, "wb").write(
                            json_to_csv(
                                source_to_import["file_content"],
                                io_format=False
                            ).encode()
                        )

                        new_source = self.sources.static_file_upload(
                            name=source_to_import["name"],
                            content=path,
                            org_id=org_id
                        )

                        self.sources.wait_for_dataset(org_id=org_id, dataset_id=new_source["id"])

                        source_to_import["new_source_id"] = new_source["id"]

                        already_created_by_name[source_to_import["name"]] = new_source["id"]

                        msg.append("DataSource '{}' imported successfully".format(source_to_import["name"]))

                        os.close(file_dir)
                        try:
                            os.remove(path)
                        except OSError:
                            pass

                    if which_type in ["piconfig", "web"]:

                        file_dir, path = mkstemp(suffix=".csv")

                        server_name = remove_special(
                            out_file=path,
                            data_array=source_to_import["file_content"]
                        )

                        if server_name is None:
                            server_name = "PITAGCONFIGFILESERVER"

                        new_source = self.sources.pi_config_upload(
                            name=source_to_import["name"],
                            server_name=server_name,
                            file_path=path,
                            org_id=org_id
                        )

                        self.sources.wait_for_dataset(org_id=org_id, dataset_id=new_source["id"])

                        source_to_import["new_source_id"] = new_source["id"]

                        already_created_by_name[source_to_import["name"]] = new_source["id"]

                        msg.append("DataSource '{}' imported successfully".format(source_to_import["name"]))

                        os.close(file_dir)
                        try:
                            os.remove(path)
                        except OSError:
                            pass

                else:

                    raise Exception("Missing export data {} ".format(
                        needed_keys.difference(source_to_import.keys()))
                    )

            if update_pipeline:

                pipeline_info = self.pipelines.get_pipeline(
                    org_id=org_id,
                    pipeline_id=pipeline_id
                )

                def updateSourceRefs(components):
                    for component in components:
                        if component["jsonClass"] == "JsonSourceRef":
                            for modified_source in data:
                                if modified_source["component"] == component["id"]:
                                    component["sourceId"] = modified_source["new_source_id"]
                        elif component["jsonClass"] == "JsonGroup":
                            updateSourceRefs(component["components"])

                updateSourceRefs(pipeline_info["pipeline"]["data"]["components"])

                self.pipelines.update_pipeline_from_json(
                    org_id=org_id,
                    update_payload=pipeline_info["pipeline"]["data"],
                    pipeline_id=pipeline_id,
                    pipeline_name=pipeline_info["pipeline"]["data"]["name"]
                )

                return json.dumps(pipeline_info)

            return str(msg)

        except Exception as error:
            raise error

    def use_existing_datasets(self, org_id, pipeline_id, content):
        """
        Method to use the existing datasets in the pipeline to be imported

        :param org_id: Destination org where datasets live
        :type org_id: int or str
        :param pipeline_id: Pipeline which is being exported
        :type pipeline_id: int or str
        :param content: Contents
        :type content: str
        :return:
        """
        try:
            errors = set()
            pipeline_info = self.pipelines.get_pipeline(
                org_id=org_id,
                pipeline_id=pipeline_id
            )

            data = json.loads(content)

            sources = self.sources.get_sources(org_id=org_id)

            current_name_to_id = {}

            for source in sources:
                current_name_to_id[source["name"]] = source["id"]["id"]

            import_id_to_name = {}
            for source_to_import in data:
                import_id_to_name[source_to_import["id"]] = source_to_import["file_content"]

            for component in pipeline_info["pipeline"]["data"]["components"]:
                if component["jsonClass"] == "JsonSourceRef":

                    for modified_source in data:

                        if modified_source["component"] == component["id"]:
                            if import_id_to_name[component["sourceId"]] in current_name_to_id:

                                component["sourceId"] = current_name_to_id[
                                    import_id_to_name[component["sourceId"]]
                                ]

                            else:
                                errors.add(
                                    "No dataset with name {} was found".format(
                                        import_id_to_name[component["sourceId"]]
                                    )
                                )

                                component["sourceId"] = str(uuid.uuid4())

                self.pipelines.update_pipeline_from_json(
                    org_id=org_id,
                    update_payload=pipeline_info["pipeline"]["data"],
                    pipeline_id=pipeline_id,
                    pipeline_name=pipeline_info["pipeline"]["data"]["name"]
                )

        except Exception as err:
            raise err

        return list(errors)

    @single_org
    def create_export_source_file(self, org_id=None, *, pipeline_id, skip):
        """
        This method creates the export file content with data for all related pipeline components

        :param org_id: Org id to export the dataset
        :type org_id: str
        :param pipeline_id: Pipeline id
        :type pipeline_id: int or str
        :param skip: skip
        :type skip: list
        :return:
        """
        pipeline_info = self.pipelines.get_pipeline(org_id=org_id, pipeline_id=pipeline_id)
        self.create_export_source_file_from_pipeline_payloads(
            org_id=org_id,
            pipeline_payloads=[pipeline_info],
            skip=skip)

    @single_org
    def create_export_source_file_from_pipeline_payloads(self, org_id=None, *, pipeline_payloads, skip):
        """
        This method creates the export file content with data for all related pipeline components

        :param org_id: Org id to export the dataset
        :type org_id: str
        :param pipeline_payloads: Pipeline payload
        :type pipeline_payloads: list of pipeline dictionary
        :param skip: skip
        :type skip: list
        :return:
        """

        sources = self.sources.get_sources(org_id=org_id)

        source_id_to_data = {}

        result_data = []

        for source in sources:
            source_id_to_data[source["id"]["id"]] = source

        sourceComponents = list()

        def collectSources(components):
            for component in components:
                if component["jsonClass"] == "JsonSourceRef":
                    sourceComponents.append(component)
                elif component["jsonClass"] == "JsonGroup":
                    collectSources(component["components"])

        for pipeline_payload in pipeline_payloads:
            collectSources(pipeline_payload["pipeline"]["data"]["components"])

        for component in sourceComponents:
            source_data = {
                "id": component["sourceId"],
                "component": component["id"]
            }

            if component["sourceId"] in source_id_to_data:

                if self.evergreen_enabled:

                    source_data["schema"] = source_id_to_data[source_data["id"]]["schema"]

                    source_data["name"] = source_id_to_data[source_data["id"]]["name"]

                    if "ean_source_type" in source_id_to_data[source_data["id"]]["labels"]["raw"]:
                        source_data["type"] = source_id_to_data[source_data["id"]]["labels"]["raw"][
                            "ean_source_type"]
                    else:
                        source_data["type"] = "api_dataset"

                else:
                    source_data["name"] = source_id_to_data[source_data["id"]]["name"]
                    source_data["schema"] = source_id_to_data[source_data["id"]]["schema"]
                    source_data["type"] = source_id_to_data[source_data["id"]]["sourceMetadata"]["jsonClass"]

                if skip:
                    source_data["file_content"] = source_id_to_data[source_data["id"]]["name"]
                else:
                    source_original_data = self.sources.download_dataset_content(
                        org_id=org_id,
                        dataset_id=component["sourceId"]
                    )
                    source_data["file_content"] = csv_to_json(csv_data=source_original_data)

                result_data.append(source_data)

        return json.dumps(result_data)

    @single_org
    def create_pipeline_export_data(self, org_id=None, *, pipeline_id, skip):
        return self.create_pipelines_export_data(org_id=org_id, pipeline_ids=[pipeline_id], skip=skip)

    @single_org
    def create_pipelines_export_data(self, org_id=None, *, pipeline_ids, skip):
        """
        Create all the necessary data to export a pipeline

        :param org_id: Org id where the pipeline to be migrated is located
        :type org_id: int or str
        :param pipeline_id: Pipeline id to be exported
        :type pipeline_id: int or str
        :param skip: List of assets tp export, datasets and templates
        :type skip: list of str
        :return:
        """
        try:
            results = {}
            results["map_attributes"] = {}
            results["functions"] = {}

            templates_used = []
            mapped_templates = []
            aux_list = self.templates.list_asset_templates(org_id=org_id)

            results["pipelines"] = []

            for pipeline_id in pipeline_ids:

                pipeline_info = self.pipelines.get_pipeline(org_id=org_id, pipeline_id=pipeline_id)

                for component in pipeline_info["pipeline"]["data"]["components"]:

                    if component["jsonClass"] == "JsonMapTemplates":

                        for mapped_value in component["values"]:
                            mapped_templates.append(mapped_value[1])

                    if component["jsonClass"] == "JsonMapAttributes":
                        results["map_attributes"][component["id"]] = csv_to_json(
                            csv_data=self.pipelines.download_map_attributes(
                                org_id=org_id,
                                pipeline_id=pipeline_id,
                                component_id=component["id"]
                            )
                        )

                    if component["jsonClass"] == "JsonFunctionApply":
                        func_id = "{}.{}.{}".format(pipeline_id, component["id"], component["pipelineId"])
                        results["functions"][func_id] = json.loads(
                            self.create_pipeline_export_data(
                                org_id=org_id,
                                pipeline_id=func_id,
                                skip=skip
                            )
                        )

                results["pipelines"].append(pipeline_info)

            used_templates = []
            template_id_to_name = {}

            for temp in aux_list:

                if str(temp["id"]) in mapped_templates:
                    used_templates.append(temp["id"])
                    template_id_to_name[str(temp["id"])] = temp["name"]
                    if "updatedBy" in temp:
                        del temp["updatedBy"]
                    if "updated" in temp:
                        del temp["updated"]
                    templates_used.append(temp)

            self.logger.debug("exporting sources...")
            results["sources"] = json.loads(
                self.create_export_source_file_from_pipeline_payloads(
                    org_id=org_id,
                    pipeline_payloads=results["pipelines"],
                    skip="datasets" in skip
                )
            )

            if "templates" in skip:

                for pipeline_data in results["pipelines"]:
                    pipeline_data, _ = self.change_template_ids_to_names(
                        pipeline_data=pipeline_data,
                        templates_data=template_id_to_name
                    )

                results["templates"] = []

                results["template_values"] = []

            else:

                results["templates"] = templates_used
                results["template_values"] = []
                if len(used_templates) > 0:
                    results["template_values"] = json.loads(
                        self.templates.download_given_templates(
                            org_id=org_id,
                            template_list=used_templates,
                            format="json")
                    )

            return json.dumps(results)

        except Exception as error:
            raise error

    def change_template_ids_to_names(self, pipeline_data, templates_data):
        """
        Changes the templates ids to its name

        :param pipeline_data: Pipeline json blob where templates are used
        :type pipeline_data: json
        :param templates_data: Templates data to be used
        :type templates_data: List of str
        :return:
        """

        errors = set()

        for component in pipeline_data["pipeline"]["data"]["components"]:

            if component["jsonClass"] == "JsonMapTemplates":

                if "values" in component:
                    new_val = []
                    for value in component["values"]:
                        row_vale = value[0]
                        template_id = value[1]
                        if template_id in templates_data:
                            new_val.append(
                                [
                                    row_vale,
                                    templates_data[template_id]
                                ]
                            )
                        else:
                            errors.add("{} not found".format(row_vale))

                    component["values"] = new_val

        return pipeline_data, list(errors)

    def mapped_rules_to_csv(self, rules):
        full_json = []

        if "distinctValues" in rules:
            distinct = rules["distinctValues"]
            if "cols" in distinct:
                cols = distinct["cols"]

                if "Count *" in cols:
                    cols.remove("Count *")

                if "data" in distinct:
                    # we have data :)
                    data = distinct["data"]
                    if "rows" in data:
                        raw_data = data["rows"]

                        for row in raw_data:
                            new_row = dict()

                            for col in cols:
                                new_row[col] = row[col]

                            full_json.append(new_row)

        return full_json

    def create_map_attributes_without_download(self, component, org_id, pipeline_id):
        if "displayInformation" in component:
            try:
                if component["displayInformation"] is not None:

                    if "columns" in component["displayInformation"]:

                        mapped_rules = self.pipelines.get_distinct_values_map_attributes(
                            org_id=org_id,
                            pipeline_id=pipeline_id,
                            flows=component["mappedFlow"]["id"],
                            columns=component["displayInformation"]["columns"]
                        )

                    else:
                        mapped_rules = self.pipelines.get_distinct_values_map_attributes(
                            org_id=org_id,
                            pipeline_id=pipeline_id,
                            flows=component["mappedFlow"]["id"],
                            columns=[]
                        )
                else:
                    mapped_rules = self.pipelines.get_distinct_values_map_attributes(
                        org_id=org_id,
                        pipeline_id=pipeline_id,
                        flows=component["mappedFlow"]["id"],
                        columns=[]
                    )

                return self.mapped_rules_to_csv(rules=mapped_rules)
            except Exception as err:
                pass

    def change_tempate_names_to_ids(self, pipeline_data, templates_data):
        """
        Change the templates names to its ids

        :param pipeline_data: Pipeline json blob where templates are used
        :type pipeline_data: int or str
        :param templates_data: Templates data to be used
        :type templates_data: List of str
        :return:
        """

        errors = set()

        for component in pipeline_data["pipeline"]["pipeline"]["data"]["components"]:

            if component["jsonClass"] == "JsonMapTemplates":

                if "values" in component:
                    new_val = []
                    for value in component["values"]:
                        row_vale = value[0]
                        template_name = value[1]
                        if template_name in templates_data:
                            new_val.append(
                                [
                                    row_vale,
                                    str(templates_data[template_name])
                                ]
                            )
                        else:
                            errors.add("{} not found".format(template_name))

                    component["values"] = new_val

        return pipeline_data, list(errors)

    @single_org
    def proceses_importing_pipeline_file(self, org_id=None, *, content, skip, handleduplicates="clone", function=False,
                                         loaded=False):
        """
        Process pipeline importing.

        :param org_id: Target org id where the pipelien will be imported
        :type org_id: int or str
        :param content: Pipeline import content
        :type content: str
        :param skip: variable to skip datasets or templates
        :type skip: list
        :param handleduplicates: Boolean variable to decide what to do with duplicate pipeline
        :type handleduplicates: bool, optional
        :return:
        """
        try:
            errors = []
            pipelines = []

            if not loaded:
                data = json.loads(content)
            else:
                data = content

            if "pipelines" not in data:
                raise Exception("Pipelines data were not found")

            for pipeline_info in data["pipelines"]:

                if handleduplicates == "clone":

                    temp_name = pipeline_info["pipeline"]["data"]["name"]

                    if self.pipelines.pipeline_exists(org_id=org_id, pipeline_name=temp_name):
                        pipeline_info["pipeline"]["data"]["name"] = "{}_{}".format(
                            temp_name,
                            str(uuid.uuid4())[:5]
                        )

            migrated_funcs = {}
            if "functions" in data:
                for func_id, func_content in data["functions"].items():
                    exists = self.pipelines.verify_if_pipeline_exists_and_get_id(
                        org_id=org_id,
                        pipeline_name=func_content["pipeline"]["pipeline"]["data"]["name"]
                    )
                    keys = func_id.split(".")

                    if exists["pipeline_id"] is not None:
                        migrated_funcs[keys[-1]] = exists["pipeline_id"]

                    if func_id not in migrated_funcs and exists["pipeline_id"] is None:
                        resp = json.loads(
                            self.proceses_importing_pipeline_file(
                                org_id=org_id,
                                content=func_content,
                                skip=skip,
                                handleduplicates=handleduplicates,
                                function=True,
                                loaded=True
                            )
                        )

                        migrated_funcs[keys[-1]] = resp["pipeline_id"]

                for pipeline_info in data["pipelines"]:
                    if function:
                        pipeline_info["pipeline"]["data"]["pipelineType"] = "function"
                    else:
                        if "pipelineType" in pipeline_info["pipeline"]["data"]:
                            del pipeline_info["pipeline"]["data"]["pipelineType"]

            if "templates" not in data:
                raise Exception("Template data was not found")

            if "template_values" not in data:
                raise Exception("Template definitions was not found")

            if len(data["template_values"]) > 0:
                try:

                    self.templates.upload_string_content_file(
                        content=json_to_csv(
                            data_array=data["template_values"],
                            io_format=False
                        ),
                        org_id=org_id
                    )

                except Exception as error:
                    errors.append("Exporting many templates can cause issues!")

            template_info = data["templates"]

            templates = self.templates.list_asset_templates(org_id=org_id)

            current_id_name_map = {}
            prev_id_name_map = {}

            for template in template_info:
                prev_id_name_map[str(template["id"])] = template["name"]

            for template in templates:
                current_id_name_map[template["name"]] = template["id"]

            if "templates" in skip:
                data, err = self.change_tempate_names_to_ids(
                    pipeline_data=data,
                    templates_data=current_id_name_map
                )

                errors.extend(err)

            attributes_name_to_id = {}

            for used_template in data["templates"]:

                current_temp_id = current_id_name_map[used_template["name"]]

                attrs = self.templates.get_attributes(
                    org_id=org_id,
                    template_id=current_temp_id
                )

                attributes_name_to_id[current_temp_id] = {}

                for item in attrs["items"]:
                    attributes_name_to_id[current_temp_id][item["name"]] = item["id"]

            for pipeline_info in data["pipelines"]:

                map_recipes = {}

                for component in pipeline_info["pipeline"]["data"]["components"]:

                    if component["jsonClass"] == "JsonMapTemplates":
                        if "templates" not in skip:
                            for mapped_value in component["values"]:
                                if mapped_value[1] in prev_id_name_map:
                                    inside = prev_id_name_map[mapped_value[1]]
                                    if inside in current_id_name_map:
                                        mapped_value[1] = str(
                                            current_id_name_map[inside]
                                        )
                                    else:
                                        errors.append(
                                            ("Template {} was deleted and "
                                             "is still mapped".format(mapped_value[1]))
                                        )
                                else:
                                    errors.append(
                                        ("Template {} was deleted and "
                                         "is still mapped".format(mapped_value[1]))
                                    )

                    if component["jsonClass"] == "JsonMapAttributes":
                        if component["id"] in data["map_attributes"]:
                            map_recipes[component["id"]] = data["map_attributes"][component["id"]]

                    if component["jsonClass"] == "JsonFunctionApply":
                        component["pipelineId"] = migrated_funcs[str(component["pipelineId"])]

                    if component["jsonClass"] == "JsonGraphsV2Sink":
                        component["orgId"] = org_id
                        component["graphId"] = str(uuid.uuid4())

                    if component["jsonClass"] == "JsonDatasetsSink":
                        component["orgId_from"] = component["orgId"]
                        component["datasetId_from"] = component["datasetId"]
                        component["orgId"] = org_id
                        component["datasetId"] = str(uuid.uuid4())

                pipeline_name = pipeline_info["pipeline"]["data"]["name"]
                self.logger.info("creating pipeline " + str(pipeline_name))
                pipeline = self.pipelines.create_pipeline(
                    org_id=org_id,
                    name=pipeline_name,
                    function=function
                )

                created_pipeline_id = pipeline['pipeline']['id']

                self.pipelines.wait_for_pipeline(
                    org_id=org_id,
                    pipeline_id=created_pipeline_id
                )

                self.logger.info("updating pipeline " + str(pipeline_name) + " (" + str(created_pipeline_id) + ")")
                self.pipelines.update_pipeline_from_json(
                    org_id=org_id,
                    update_payload=pipeline_info["pipeline"]["data"],
                    pipeline_id=created_pipeline_id,
                    pipeline_name=pipeline_name
                )

                self.pipelines.wait_for_pipeline(
                    org_id=org_id,
                    pipeline_id=created_pipeline_id
                )

                pipeline_info["pipeline"]["id"] = created_pipeline_id

                for component_id, recipe in map_recipes.items():
                    try:
                        self.pipelines.upload_map_attributes_from_json(
                            org_id=org_id,
                            component_id=component_id,
                            pipeline_id=created_pipeline_id,
                            json_data=recipe
                        )
                    except Exception as err:
                        errors.append(repr(err))

                # nb: dataset sink must be commited with schema from migrated sink
                def set_sink_schemas(components):

                    for component in components:
                        if component["jsonClass"] == "JsonDatasetsSink":
                            try:
                                schemas = self.sources.get_dataset_schema(org_id=component["orgId_from"],
                                                                          dataset_id=component["datasetId_from"])

                                self.sources.create_command(org_id=component["orgId"],
                                                            schema=schemas["schemas"][0][1],
                                                            name=component["datasetName"],
                                                            facets=component["facets"],
                                                            description=component["description"],
                                                            cause=[],
                                                            dataset_uuid=component["datasetId"])

                            except Exception as err:
                                errors.append(repr(err))

                        elif component["jsonClass"] == "JsonGroup":
                            set_sink_schemas(component["components"])

                set_sink_schemas(pipeline_info["pipeline"]["data"]["components"])

                pipeline = {
                    "pipeline_id": created_pipeline_id,
                    "name": pipeline_name,
                    "url": "{}#/org/{}/pipelines/{}".format(
                        self.properties.get_remote(self.cluster),
                        org_id,
                        created_pipeline_id
                    )
                }
                pipelines.append(pipeline)

            if "sources" in data:

                def collect_source_component_ids(components, source_component_ids):
                    for component in components:
                        if component["jsonClass"] == "JsonSourceRef":
                            source_component_ids.append(component["id"])
                        elif component["jsonClass"] == "JsonGroup":
                            collect_source_component_ids(component["components"], source_component_ids)

                for pipeline_info in data["pipelines"]:

                    pipeline_id = pipeline_info["pipeline"]["id"]
                    pipeline_name = pipeline_info["pipeline"]["data"]["name"]

                    source_component_ids = list()
                    collect_source_component_ids(pipeline_info["pipeline"]["data"]["components"], source_component_ids)
                    self.logger.debug(
                        "source component ids found for pipeline {0}: {1}".format(pipeline_name, source_component_ids))

                    sources = []
                    source_names = []
                    for source in data["sources"]:
                        for source_component_id in source_component_ids:
                            if source["component"] == source_component_id:
                                sources.append(source)
                                source_names.append(source["name"])

                    if "datasets" not in skip:
                        self.logger.debug("importing {0} sources to {1} pipeline".format(source_names, pipeline_name))
                        self.import_sources(
                            org_id=org_id,
                            pipeline_id=pipeline_id,
                            content=json.dumps(sources),
                            handleduplicates=handleduplicates,
                        )

                    else:
                        self.logger.debug(
                            "using {0} existing sources in {1} pipeline".format(source_names, pipeline_name))
                        err = self.use_existing_datasets(
                            org_id=org_id,
                            pipeline_id=pipeline_id,
                            content=json.dumps(sources),
                        )
                        errors.append(err)

            results = {
                "org_id": org_id,
                "pipelines": pipelines,
                "warnings": errors
            }
            return json.dumps(results)
        except Exception as error:
            raise error

    @single_org
    def get_all_hierarchies_display(self, org_id=None):
        """
        Method to retrieve all the organization on a given org

        :param org_id: Organization id where the org is stored
        :return:
        """
        columns = [
            "id", "name"
        ]

        raw_data = self.get_all_hierarchies(org_id=org_id)

        for data in raw_data:

            for key in list(data.keys()):

                if key not in columns:
                    del data[key]

        return raw_data

    @single_org
    def get_single_hierarchy(self, org_id=None, *, hierarchy):
        """
        Method to retrieve all the data form a single hierarchy and remove unnecessary data to be displayed on the console

        :param org_id: Organization id where the org is stored
        :param hierarchy: Hierarchy id to be retrieved
        :return:
        """
        try:
            columns = [
                "id", "name", "levels"
            ]

            raw_data = self.hierarchies.get_hierarchy(
                org_id=org_id,
                hierarchy_id=hierarchy
            )["config"]

            for key in list(raw_data.keys()):

                if key not in columns:
                    del raw_data[key]

            return raw_data

        except Exception as error:
            raise error

    @single_org
    def get_all_hierarchies(self, org_id=None):
        """
        Method to retrieve all the organization on a given org

        :param org_id: Organization id where the org is stored
        :return:
        """
        try:
            return self.hierarchies.get_all_hierarchies(
                org_id=org_id
            )
        except Exception as error:
            raise error

    @single_org
    def create_hierarchy(self, org_id=None, *, name, levels=None, attribute_names=None, private=False):
        """
        Method to create a new hierarchy on the given org

        :param org_id: Organization id where the org would be saved
        :param name: String name of the new hierarchy
        :param levels: Array containing the level names
        :param attribute_names:
        :param private: Boolean value to specify if the hierarchy is private
        :return:
        """
        try:
            return self.hierarchies.create_hierarchy(
                org_id=org_id,
                name=name,
                levels=levels if levels is not None else [],
                attribute_names=attribute_names,
                private=private
            )
        except Exception as error:
            raise error

    @single_org
    def export_hierarchy(self, org_id=None, *, hierarchy):
        """
        Method to extract the necessary information to export a hierarchy

        :param org_id: organization id where the hierarchy currently is stored
        :param hierarchy: hierarchy id to be exported
        :return:
        """
        try:
            data = self.get_single_hierarchy(
                org_id=org_id,
                hierarchy=hierarchy
            )

            full_data = {
                "name": data["name"],
                "levels": dict()
            }

            for level in data["levels"]:
                full_data["levels"][level["index"]] = level['groupName']

            return json.dumps(full_data)
        except Exception as error:
            raise error

    @single_org
    def import_hierarchy(self, org_id=None, *, content):
        """
        Method to import a hierarchy, this should be used with the output of the export hierarchy

        :param org_id: organization id where the new hierarchy will be saved
        :param content: json object containing hierarchy data
        :return:
        """
        try:
            data = json.loads(content)
            if "name" in data:

                new_h = self.create_hierarchy(
                    org_id=org_id,
                    name=data["name"]
                )

                hierarchy_id = new_h["id"]

                if "levels" in data:
                    levels = data["levels"]

                    for i in range(0, len(levels.keys())):
                        self.hierarchies.add_level(
                            org_id=org_id,
                            hierarchy_id=hierarchy_id,
                            level_name=levels[str(i)]
                        )

                return new_h

        except Exception as error:
            raise error

    @single_org
    def get_rules_list(self, org_id=None):
        """

        Retrieves the org rules
        :param org_id: organization id to be queried
        :return:
        """

        resp = self.permissions.get_rules(org_id=org_id)

        return resp["data"]["permissions"]["getRules"]

    @single_org
    def get_selectors_list(self, org_id=None):
        """

        Retrieves selectors
        :param org_id: organization id to be queried
        :return:
        """

        resp = self.permissions.get_selector_definitions(org_id=org_id)

        return resp["data"]["permissions"]["getSelectorDefinitions"]

    @single_org
    def get_permissions_org_config(self, org_id=None):
        """

        Retrieves org permissions config
        :param org_id: organization id to be queried
        :return:
        """

        resp = self.permissions.get_org_config(org_id=org_id)

        return resp["data"]["permissions"]["getOrgConfig"]

    @single_org
    def get_pipeline_rules(self, org_id=None, *, pipeline_id):
        resp = self.permissions.get_artifact_rules(
            org_id=org_id, artifact_id=pipeline_id, artifact_type=ArtifactType.pipeline
        )

        return resp

    @single_org
    def get_dataset_rules(self, org_id=None, *, dataset_id):
        resp = self.permissions.get_artifact_rules(
            org_id=org_id, artifact_id=dataset_id, artifact_type=ArtifactType.dataset
        )

        return resp["data"]["permissions"]["getArtifactRules"]

    @single_org
    def check_permission(self, org_id=None, *, artifact_type, artifact_id, user_id, verb):
        resp = self.permissions.check_permission(
            org_id=org_id,
            artifact_type=artifact_type,
            artifact_id=artifact_id,
            user_id=user_id,
            verb=verb
        )

        return resp["data"]["permissions"]["check"]["allowed"]

    @single_org
    def get_selector_definition(self, org_id=None, *, selector_id):
        resp = self.permissions.get_selector_definition(
            org_id=org_id,
            selector_id=selector_id
        )
        return resp["data"]["permissions"]['getSelectorDefinition']

    @single_org
    def add_rule(self, org_id=None, *, domain, verb, effect, userSelector, resourceSelector):
        resp = self.permissions.add_rule(
            org_id=org_id,
            domain=domain,
            verb=verb,
            effect=effect,
            userSelector=userSelector,
            resourceSelector=resourceSelector
        )
        return resp["data"]["permissions"]

    @single_org
    def delete_rule(self, org_id=None, *, rule_id):

        resp = self.permissions.delete_rule(
            org_id=org_id,
            rule_id=rule_id
        )

        return resp["data"]["permissions"]
