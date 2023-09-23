from collections import defaultdict

from libcoveofds.schema import OFDSSchema


class AdditionalCheckForNetwork:
    """Any check that wants to be provided should extend this abstract class and overwrite methods"""

    def __init__(self, schema_object: OFDSSchema):
        self._additional_check_results: list = []
        self._schema_object: OFDSSchema = schema_object

    def check_node_first_pass(self, node: dict, path: str):
        pass

    def check_span_first_pass(self, span: dict, path: str):
        pass

    def check_phase_first_pass(self, phase: dict, path: str):
        pass

    def check_organisation_first_pass(self, organisation: dict, path: str):
        pass

    def check_contract_first_pass(self, contract: dict, path: str):
        pass

    def check_node_second_pass(self, node: dict, path: str):
        pass

    def check_span_second_pass(self, span: dict, path: str):
        pass

    def check_phase_second_pass(self, phase: dict, path: str):
        pass

    def check_organisation_second_pass(self, organisation: dict, path: str):
        pass

    def check_contract_second_pass(self, contract: dict, path: str):
        pass

    def get_additional_check_results(self) -> list:
        return self._additional_check_results

    def skip_if_any_links_have_external_node_data(self) -> bool:
        return False

    def skip_if_any_links_have_external_span_data(self) -> bool:
        return False


class SpansMustHaveValidNodesAdditionalCheckForNetwork(AdditionalCheckForNetwork):
    def __init__(self, schema_object: OFDSSchema):
        super().__init__(schema_object)
        self._node_ids_seen: list = []

    def check_node_first_pass(self, node: dict, path: str):
        id = node.get("id")
        if id:
            self._node_ids_seen.append(id)

    def check_span_second_pass(self, span: dict, path: str):
        span_id = span.get("id")
        start = span.get("start")
        if start and isinstance(start, str) and not start in self._node_ids_seen:
            self._additional_check_results.append(
                {
                    "type": "span_start_node_not_found",
                    "missing_node_id": start,
                    "span_id": span_id,
                    "path": path + "/start",
                }
            )
        end = span.get("end")
        if end and isinstance(end, str) and not end in self._node_ids_seen:
            self._additional_check_results.append(
                {
                    "type": "span_end_node_not_found",
                    "missing_node_id": end,
                    "span_id": span_id,
                    "path": path + "/end",
                }
            )

    def skip_if_any_links_have_external_node_data(self) -> bool:
        return True

    def skip_if_any_links_have_external_span_data(self) -> bool:
        return True


class NodesLocationAndSpansRouteAdditionalCheckForNetwork(AdditionalCheckForNetwork):
    def check_node_first_pass(self, node: dict, path: str):
        location = node.get("location")
        if isinstance(location, dict) and location:
            type = location.get("type")
            if type != "Point":
                self._additional_check_results.append(
                    {
                        "type": "node_location_type_incorrect",
                        "node_id": node.get("id"),
                        "incorrect_type": type,
                        "path": path + "/location/type",
                    }
                )
            if not self._is_json_coordinates(location.get("coordinates")):
                self._additional_check_results.append(
                    {
                        "type": "node_location_coordinates_incorrect",
                        "node_id": node.get("id"),
                        "incorrect_coordinates": location.get("coordinates"),
                        "path": path + "/location/coordinates",
                    }
                )

    def check_span_first_pass(self, span: dict, path: str):
        location = span.get("route")
        if isinstance(location, dict) and location:
            type = location.get("type")
            if type != "LineString":
                self._additional_check_results.append(
                    {
                        "type": "span_route_type_incorrect",
                        "span_id": span.get("id"),
                        "incorrect_type": type,
                        "path": path + "/route/type",
                    }
                )
            if not self._is_json_list_coordinates(location.get("coordinates")):
                self._additional_check_results.append(
                    {
                        "type": "span_route_coordinates_incorrect",
                        "span_id": span.get("id"),
                        "incorrect_coordinates": location.get("coordinates"),
                        "path": path + "/route/coordinates",
                    }
                )

    def _is_json_list_coordinates(self, list_coordinates):
        if not isinstance(list_coordinates, list):
            return False
        for coordinates in list_coordinates:
            if not self._is_json_coordinates(coordinates):
                return False
        return True

    def _is_json_coordinates(self, coordinates):
        return (
            isinstance(coordinates, list)
            and len(coordinates) == 2
            and (isinstance(coordinates[0], float) or isinstance(coordinates[0], int))
            and (isinstance(coordinates[1], float) or isinstance(coordinates[1], int))
        )


class PhaseReferenceAdditionalCheckForNetwork(AdditionalCheckForNetwork):
    def __init__(self, schema_object: OFDSSchema):
        super().__init__(schema_object)
        self._phases: dict = {}

    def check_phase_first_pass(self, phase: dict, path: str):
        id = phase.get("id")
        name = phase.get("name")
        if id:
            self._phases[id] = name

    def check_node_second_pass(self, node: dict, path: str):
        if "phase" in node and isinstance(node["phase"], dict):
            self._check_related_phase_object(
                node["phase"],
                {
                    "type": "node_phase_reference_id_not_found",
                    "node_id": node.get("id"),
                    "path": path + "/phase/id",
                },
                {
                    "type": "node_phase_reference_name_does_not_match",
                    "node_id": node.get("id"),
                    "path": path + "/phase/name",
                },
                {
                    "type": "node_phase_reference_name_set_but_not_in_original",
                    "node_id": node.get("id"),
                    "path": path + "/phase/name",
                },
            )

    def check_span_second_pass(self, span: dict, path: str):
        if "phase" in span and isinstance(span["phase"], dict):
            self._check_related_phase_object(
                span["phase"],
                {
                    "type": "span_phase_reference_id_not_found",
                    "span_id": span.get("id"),
                    "path": path + "/phase/id",
                },
                {
                    "type": "span_phase_reference_name_does_not_match",
                    "span_id": span.get("id"),
                    "path": path + "/phase/name",
                },
                {
                    "type": "span_phase_reference_name_set_but_not_in_original",
                    "span_id": span.get("id"),
                    "path": path + "/phase/name",
                },
            )

    def check_contract_second_pass(self, contract: dict, path: str):
        if "relatedPhases" in contract and isinstance(contract["relatedPhases"], list):
            for related_phase_idx, related_phase in enumerate(
                contract["relatedPhases"]
            ):
                if isinstance(related_phase, dict):
                    self._check_related_phase_object(
                        related_phase,
                        {
                            "type": "contract_related_phase_reference_id_not_found",
                            "contract_id": contract.get("id"),
                            "path": path
                            + "/relatedPhases/"
                            + str(related_phase_idx)
                            + "/id",
                        },
                        {
                            "type": "contract_related_phase_reference_name_does_not_match",
                            "contract_id": contract.get("id"),
                            "path": path
                            + "/relatedPhases/"
                            + str(related_phase_idx)
                            + "/name",
                        },
                        {
                            "type": "contract_related_phase_reference_name_set_but_not_in_original",
                            "contract_id": contract.get("id"),
                            "path": path
                            + "/relatedPhases/"
                            + str(related_phase_idx)
                            + "/name",
                        },
                    )

    def _check_related_phase_object(
        self,
        related_phase: dict,
        id_not_found_result: dict,
        name_not_match_result: dict,
        name_set_but_not_in_original_result: dict,
    ):
        id = related_phase.get("id")
        name = related_phase.get("name")
        # id is required in JSON Schema - if it is not set we can let that validation raise an error.
        # We'll only carry on with our checks (those that can't be done in JSON Schema) if id exists.
        if id:
            if id in self._phases:
                # check - if name is set on reference but not on original
                if name and not self._phases[id]:
                    name_set_but_not_in_original_result.update(
                        {"name_in_reference": name}
                    )
                    self._additional_check_results.append(
                        name_set_but_not_in_original_result
                    )
                # check - if names are both set, do they match?
                if name and self._phases[id] and name != self._phases[id]:
                    name_not_match_result.update(
                        {"name_in_reference": name, "name_should_be": self._phases[id]}
                    )
                    self._additional_check_results.append(name_not_match_result)
            else:
                # check failed - id is not known
                id_not_found_result.update({"phase_id_not_found": id})
                self._additional_check_results.append(id_not_found_result)


class OrganisationReferenceAdditionalCheckForNetwork(AdditionalCheckForNetwork):
    def __init__(self, schema_object: OFDSSchema):
        super().__init__(schema_object)
        self._organisations: dict = {}

    def check_organisation_first_pass(self, organisation: dict, path: str):
        id = organisation.get("id")
        name = organisation.get("name")
        if id:
            self._organisations[id] = name

    def check_node_second_pass(self, node: dict, path: str):
        if "physicalInfrastructureProvider" in node and isinstance(
            node["physicalInfrastructureProvider"], dict
        ):
            self._check_related_organisation_object(
                node["physicalInfrastructureProvider"],
                {
                    "type": "node_organisation_reference_id_not_found",
                    "node_id": node.get("id"),
                    "field": "physicalInfrastructureProvider",
                    "path": path + "/physicalInfrastructureProvider/id",
                },
                {
                    "type": "node_organisation_reference_name_does_not_match",
                    "node_id": node.get("id"),
                    "field": "physicalInfrastructureProvider",
                    "path": path + "/physicalInfrastructureProvider/name",
                },
                {
                    "type": "node_organisation_reference_name_set_but_not_in_original",
                    "node_id": node.get("id"),
                    "field": "physicalInfrastructureProvider",
                    "path": path + "/physicalInfrastructureProvider/name",
                },
            )
        if "networkProviders" in node and isinstance(node["networkProviders"], list):
            for network_provider_idx, network_provider in enumerate(
                node["networkProviders"]
            ):
                if isinstance(network_provider, dict):
                    self._check_related_organisation_object(
                        network_provider,
                        {
                            "type": "node_organisation_reference_id_not_found",
                            "node_id": node.get("id"),
                            "field": "networkProviders",
                            "path": path
                            + "/networkProviders/"
                            + str(network_provider_idx)
                            + "/id",
                        },
                        {
                            "type": "node_organisation_reference_name_does_not_match",
                            "node_id": node.get("id"),
                            "field": "networkProviders",
                            "path": path
                            + "/networkProviders/"
                            + str(network_provider_idx)
                            + "/name",
                        },
                        {
                            "type": "node_organisation_reference_name_set_but_not_in_original",
                            "node_id": node.get("id"),
                            "field": "networkProviders",
                            "path": path
                            + "/networkProviders/"
                            + str(network_provider_idx)
                            + "/name",
                        },
                    )

    def check_span_second_pass(self, span: dict, path: str):
        if "physicalInfrastructureProvider" in span and isinstance(
            span["physicalInfrastructureProvider"], dict
        ):
            self._check_related_organisation_object(
                span["physicalInfrastructureProvider"],
                {
                    "type": "span_organisation_reference_id_not_found",
                    "span_id": span.get("id"),
                    "field": "physicalInfrastructureProvider",
                    "path": path + "/physicalInfrastructureProvider/id",
                },
                {
                    "type": "span_organisation_reference_name_does_not_match",
                    "span_id": span.get("id"),
                    "field": "physicalInfrastructureProvider",
                    "path": path + "/physicalInfrastructureProvider/name",
                },
                {
                    "type": "span_organisation_reference_name_set_but_not_in_original",
                    "span_id": span.get("id"),
                    "field": "physicalInfrastructureProvider",
                    "path": path + "/physicalInfrastructureProvider/name",
                },
            )
        if "networkProviders" in span and isinstance(span["networkProviders"], list):
            for network_provider_idx, network_provider in enumerate(
                span["networkProviders"]
            ):
                if isinstance(network_provider, dict):
                    self._check_related_organisation_object(
                        network_provider,
                        {
                            "type": "span_organisation_reference_id_not_found",
                            "span_id": span.get("id"),
                            "field": "networkProviders",
                            "path": path
                            + "/networkProviders/"
                            + str(network_provider_idx)
                            + "/id",
                        },
                        {
                            "type": "span_organisation_reference_name_does_not_match",
                            "span_id": span.get("id"),
                            "field": "networkProviders",
                            "path": path
                            + "/networkProviders/"
                            + str(network_provider_idx)
                            + "/name",
                        },
                        {
                            "type": "span_organisation_reference_name_set_but_not_in_original",
                            "span_id": span.get("id"),
                            "field": "networkProviders",
                            "path": path
                            + "/networkProviders/"
                            + str(network_provider_idx)
                            + "/name",
                        },
                    )
        if "supplier" in span and isinstance(span["supplier"], dict):
            self._check_related_organisation_object(
                span["supplier"],
                {
                    "type": "span_organisation_reference_id_not_found",
                    "span_id": span.get("id"),
                    "field": "supplier",
                    "path": path + "/supplier/id",
                },
                {
                    "type": "span_organisation_reference_name_does_not_match",
                    "span_id": span.get("id"),
                    "field": "supplier",
                    "path": path + "/supplier/name",
                },
                {
                    "type": "span_organisation_reference_name_set_but_not_in_original",
                    "span_id": span.get("id"),
                    "field": "supplier",
                    "path": path + "/supplier/name",
                },
            )

    def check_phase_second_pass(self, phase: dict, path: str):
        if "funders" in phase and isinstance(phase["funders"], list):
            for funder_idx, funder in enumerate(phase["funders"]):
                if isinstance(funder, dict):
                    self._check_related_organisation_object(
                        funder,
                        {
                            "type": "phase_organisation_reference_id_not_found",
                            "phase_id": phase.get("id"),
                            "path": path + "/funders/" + str(funder_idx) + "/id",
                        },
                        {
                            "type": "phase_organisation_reference_name_does_not_match",
                            "phase_id": phase.get("id"),
                            "path": path + "/funders/" + str(funder_idx) + "/name",
                        },
                        {
                            "type": "phase_organisation_reference_name_set_but_not_in_original",
                            "phase_id": phase.get("id"),
                            "path": path + "/funders/" + str(funder_idx) + "/name",
                        },
                    )

    def _check_related_organisation_object(
        self,
        related_organisation: dict,
        id_not_found_result: dict,
        name_not_match_result: dict,
        name_set_but_not_in_original_result: dict,
    ):
        id = related_organisation.get("id")
        name = related_organisation.get("name")
        # id is required in JSON Schema - if it is not set we can let that validation raise an error.
        # We'll only carry on with our checks (those that can't be done in JSON Schema) if id exists.
        if id:
            if id in self._organisations:
                # check - if name is set on reference but not on original
                if name and not self._organisations[id]:
                    name_set_but_not_in_original_result.update(
                        {"name_in_reference": name}
                    )
                    self._additional_check_results.append(
                        name_set_but_not_in_original_result
                    )
                # check - if names are both set, do they match?
                if name and self._organisations[id] and name != self._organisations[id]:
                    name_not_match_result.update(
                        {
                            "name_in_reference": name,
                            "name_should_be": self._organisations[id],
                        }
                    )
                    self._additional_check_results.append(name_not_match_result)
            else:
                # check failed - id is not known
                id_not_found_result.update({"organisation_id_not_found": id})
                self._additional_check_results.append(id_not_found_result)


class NodeInternationalConnectionCountryAdditionalCheckForNetwork(
    AdditionalCheckForNetwork
):
    def check_node_first_pass(self, node: dict, path: str):
        if "internationalConnections" in node and isinstance(
            node["internationalConnections"], list
        ):
            for international_connection_idx, international_connection in enumerate(
                node["internationalConnections"]
            ):
                if isinstance(
                    international_connection, dict
                ) and not international_connection.get("country"):
                    self._additional_check_results.append(
                        {
                            "type": "node_international_connections_country_not_set",
                            "node_id": node.get("id"),
                            "path": path
                            + "/internationalConnections/"
                            + str(international_connection_idx),
                        }
                    )


class IsNodeUsedInSpanAdditionalCheckForNetwork(AdditionalCheckForNetwork):
    def __init__(self, schema_object: OFDSSchema):
        super().__init__(schema_object)
        self._node_ids_used_in_spans: list = []

    def check_span_first_pass(self, span: dict, path: str):
        start = span.get("start")
        if start and start not in self._node_ids_used_in_spans:
            self._node_ids_used_in_spans.append(start)
        end = span.get("end")
        if end and end not in self._node_ids_used_in_spans:
            self._node_ids_used_in_spans.append(end)

    def check_node_second_pass(self, node: dict, path: str):
        id = node.get("id")
        if id and id not in self._node_ids_used_in_spans:
            self._additional_check_results.append(
                {
                    "type": "node_not_used_in_any_spans",
                    "node_id": node.get("id"),
                    "path": path,
                }
            )

    def skip_if_any_links_have_external_node_data(self) -> bool:
        return True

    def skip_if_any_links_have_external_span_data(self) -> bool:
        return True


class UniqueIDsAdditionalCheckForNetwork(AdditionalCheckForNetwork):
    def __init__(self, schema_object: OFDSSchema):
        super().__init__(schema_object)
        self._node_ids_seen: defaultdict = defaultdict(list)
        self._span_ids_seen: defaultdict = defaultdict(list)
        self._phase_ids_seen: defaultdict = defaultdict(list)
        self._organisation_ids_seen: defaultdict = defaultdict(list)
        self._contract_ids_seen: defaultdict = defaultdict(list)

    def check_node_first_pass(self, node: dict, path: str):
        id = node.get("id")
        if id and isinstance(id, str):
            self._node_ids_seen[id].append(path)

    def check_span_first_pass(self, span: dict, path: str):
        id = span.get("id")
        if id and isinstance(id, str):
            self._span_ids_seen[id].append(path)

    def check_phase_first_pass(self, phase: dict, path: str):
        id = phase.get("id")
        if id and isinstance(id, str):
            self._phase_ids_seen[id].append(path)

    def check_organisation_first_pass(self, organisation: dict, path: str):
        id = organisation.get("id")
        if id and isinstance(id, str):
            self._organisation_ids_seen[id].append(path)

    def check_contract_first_pass(self, contract: dict, path: str):
        id = contract.get("id")
        if id and isinstance(id, str):
            self._contract_ids_seen[id].append(path)

    def get_additional_check_results(self) -> list:
        out: list = []
        for id, paths in self._node_ids_seen.items():
            if len(paths) > 1:
                for path in paths:
                    out.append(
                        {
                            "type": "duplicate_node_id",
                            "node_id": id,
                            "path": path + "/id",
                        }
                    )
        for id, paths in self._span_ids_seen.items():
            if len(paths) > 1:
                for path in paths:
                    out.append(
                        {
                            "type": "duplicate_span_id",
                            "span_id": id,
                            "path": path + "/id",
                        }
                    )
        for id, paths in self._phase_ids_seen.items():
            if len(paths) > 1:
                for path in paths:
                    out.append(
                        {
                            "type": "duplicate_phase_id",
                            "phase_id": id,
                            "path": path + "/id",
                        }
                    )
        for id, paths in self._organisation_ids_seen.items():
            if len(paths) > 1:
                for path in paths:
                    out.append(
                        {
                            "type": "duplicate_organisation_id",
                            "organisation_id": id,
                            "path": path + "/id",
                        }
                    )
        for id, paths in self._contract_ids_seen.items():
            if len(paths) > 1:
                for path in paths:
                    out.append(
                        {
                            "type": "duplicate_contract_id",
                            "contract_id": id,
                            "path": path + "/id",
                        }
                    )
        return out

    def skip_if_any_links_have_external_node_data(self) -> bool:
        return False

    def skip_if_any_links_have_external_span_data(self) -> bool:
        return False


ADDITIONAL_CHECK_CLASSES_FOR_NETWORK = [
    SpansMustHaveValidNodesAdditionalCheckForNetwork,
    NodesLocationAndSpansRouteAdditionalCheckForNetwork,
    PhaseReferenceAdditionalCheckForNetwork,
    OrganisationReferenceAdditionalCheckForNetwork,
    NodeInternationalConnectionCountryAdditionalCheckForNetwork,
    IsNodeUsedInSpanAdditionalCheckForNetwork,
    UniqueIDsAdditionalCheckForNetwork,
]


class PythonValidate:
    """Validates data using additional checks custom written in Python"""

    def __init__(self, schema: OFDSSchema):
        self._schema = schema

    def validate(self, json_data: dict) -> list:
        """Call with data. Results are returned."""

        additional_checks: list = []

        # For each Network
        networks = json_data.get("networks")
        if isinstance(networks, list):
            for network_idx, network in enumerate(networks):
                if isinstance(network, dict):
                    additional_check_instances = [
                        x(self._schema) for x in ADDITIONAL_CHECK_CLASSES_FOR_NETWORK
                    ]
                    links = network.get("links", [])
                    links_with_external_nodes = [
                        l
                        for l in links
                        if isinstance(l, dict)
                        and l.get("rel", "")
                        in self._schema.get_link_rels_for_external_nodes()
                    ]
                    if links_with_external_nodes:
                        additional_check_instances = [
                            x
                            for x in additional_check_instances
                            if not x.skip_if_any_links_have_external_node_data()
                        ]
                        additional_checks.append(
                            {
                                "network_id": network.get("id"),
                                "type": "has_links_with_external_node_data",
                                "path": "/networks/" + str(network_idx),
                            }
                        )
                    links_with_external_spans = [
                        l
                        for l in links
                        if isinstance(l, dict)
                        and l.get("rel", "")
                        in self._schema.get_link_rels_for_external_spans()
                    ]
                    if links_with_external_spans:
                        additional_check_instances = [
                            x
                            for x in additional_check_instances
                            if not x.skip_if_any_links_have_external_span_data()
                        ]
                        additional_checks.append(
                            {
                                "network_id": network.get("id"),
                                "type": "has_links_with_external_span_data",
                                "path": "/networks/" + str(network_idx),
                            }
                        )
                    nodes = network.get("nodes", [])
                    nodes = nodes if isinstance(nodes, list) else []
                    spans = network.get("spans", [])
                    spans = spans if isinstance(spans, list) else []
                    phases = network.get("phases", [])
                    phases = phases if isinstance(phases, list) else []
                    organisations = network.get("organisations", [])
                    organisations = (
                        organisations if isinstance(organisations, list) else []
                    )
                    contracts = network.get("contracts", [])
                    contracts = contracts if isinstance(contracts, list) else []
                    # First pass
                    for additional_check_instance in additional_check_instances:
                        for node_idx, node in enumerate(nodes):
                            additional_check_instance.check_node_first_pass(
                                node,
                                "/networks/"
                                + str(network_idx)
                                + "/nodes/"
                                + str(node_idx),
                            )
                        for span_idx, span in enumerate(spans):
                            additional_check_instance.check_span_first_pass(
                                span,
                                "/networks/"
                                + str(network_idx)
                                + "/spans/"
                                + str(span_idx),
                            )
                        for phase_idx, phase in enumerate(phases):
                            additional_check_instance.check_phase_first_pass(
                                phase,
                                "/networks/"
                                + str(network_idx)
                                + "/phases/"
                                + str(phase_idx),
                            )
                        for organisation_idx, organisation in enumerate(organisations):
                            additional_check_instance.check_organisation_first_pass(
                                organisation,
                                "/networks/"
                                + str(network_idx)
                                + "/organisations/"
                                + str(organisation_idx),
                            )
                        for contract_idx, contract in enumerate(contracts):
                            additional_check_instance.check_contract_first_pass(
                                contract,
                                "/networks/"
                                + str(network_idx)
                                + "/contracts/"
                                + str(contract_idx),
                            )
                    # Second pass
                    for additional_check_instance in additional_check_instances:
                        for node_idx, node in enumerate(nodes):
                            additional_check_instance.check_node_second_pass(
                                node,
                                "/networks/"
                                + str(network_idx)
                                + "/nodes/"
                                + str(node_idx),
                            )
                        for span_idx, span in enumerate(spans):
                            additional_check_instance.check_span_second_pass(
                                span,
                                "/networks/"
                                + str(network_idx)
                                + "/spans/"
                                + str(span_idx),
                            )
                        for phase_idx, phase in enumerate(phases):
                            additional_check_instance.check_phase_second_pass(
                                phase,
                                "/networks/"
                                + str(network_idx)
                                + "/phases/"
                                + str(phase_idx),
                            )
                        for organisation_idx, organisation in enumerate(organisations):
                            additional_check_instance.check_organisation_second_pass(
                                organisation,
                                "/networks/"
                                + str(network_idx)
                                + "/organisations/"
                                + str(organisation_idx),
                            )
                        for contract_idx, contract in enumerate(contracts):
                            additional_check_instance.check_contract_second_pass(
                                contract,
                                "/networks/"
                                + str(network_idx)
                                + "/contracts/"
                                + str(contract_idx),
                            )
                    # Results
                    for additional_check_instance in additional_check_instances:
                        for (
                            additional_check
                        ) in additional_check_instance.get_additional_check_results():
                            additional_check["network_id"] = network.get("id")
                            additional_checks.append(additional_check)

        # Return
        return additional_checks
