from cdm_tools.api_links import DOCS_BASE, ApiIndex, base_type

SNAP = {
    "query_type": "Query",
    "mutation_type": "Mutation",
    "types": {
        "Query": {"kind": "OBJECT", "fields": {
            "desXById": "DesX", "desXs": "DesXConnection", "desXsByIds": "[DesUnion!]!",
            "design": "DesignQueries!", "node": "Node", "bomBomById": "Bom!", "desStageCount": "Int!",
        }},
        "DesignQueries": {"kind": "OBJECT", "fields": {"ruleCheck": "RuleCheckQueries!"}},
        "RuleCheckQueries": {"kind": "OBJECT", "fields": {"byId": "RuleCheck", "byIds": "[RuleCheck]!"}},
        "RuleCheck": {"kind": "OBJECT", "fields": {"id": "ID!"}},
        "DesXConnection": {"kind": "OBJECT", "fields": {"nodes": "[DesX!]", "pageInfo": "PageInfo!"}},
        "PageInfo": {"kind": "OBJECT", "fields": {"hasNextPage": "Boolean!"}},
        "DesX": {"kind": "OBJECT", "fields": {"id": "ID!", "stages": "[DesStage!]!"}, "interfaces": ["Node"]},
        "DesStage": {"kind": "OBJECT", "fields": {"name": "String!"}},
        "DesXTemplate": {"kind": "OBJECT", "fields": {"id": "ID!"}},
        "DesErr": {"kind": "OBJECT", "fields": {"message": "String!"}},
        "DesUnion": {"kind": "UNION", "possible_types": ["DesErr", "DesX"]},
        "Node": {"kind": "INTERFACE", "fields": {"id": "ID!"}, "possible_types": ["DesX"]},
        "Bom": {"kind": "INTERFACE", "fields": {"id": "ID!"}, "possible_types": ["BomWip"]},
        "BomWip": {"kind": "OBJECT", "fields": {"id": "ID!"}, "interfaces": ["Bom"]},
        "Mutation": {"kind": "OBJECT", "fields": {
            "desCreateX": "DesCreateXPayload!", "desUpdateXParams": "DesIdPayload!",
            "desCreateXTemplate": "DesIdPayload!", "bomCreateBom": "BomCreateBomPayload!",
        }},
        "DesCreateXPayload": {"kind": "OBJECT", "fields": {"id": "ID!"}},
        "DesIdPayload": {"kind": "OBJECT", "fields": {"id": "ID!"}},
        "BomCreateBomPayload": {"kind": "OBJECT", "fields": {"bom": "BomWip", "errors": "[String!]!"}},
        "Int": {"kind": "SCALAR"}, "ID": {"kind": "SCALAR"}, "String": {"kind": "SCALAR"}, "Boolean": {"kind": "SCALAR"},
    },
}


def _paths(ops):
    return [(o.path, o.via) for o in ops]


def test_base_type():
    assert base_type("[DesX!]!") == "DesX"


def test_reads_direct_connection_union_and_refetch():
    links = ApiIndex(SNAP).links_for("DesX")
    assert links.kind == "OBJECT"
    assert _paths(links.reads) == [("desXById", None), ("desXs", "DesXConnection"), ("desXsByIds", "DesUnion")]
    assert links.refetchable is True
    assert links.reached_via == []


def test_reads_through_namespace_roots():
    links = ApiIndex(SNAP).links_for("RuleCheck")
    assert _paths(links.reads) == [("design.ruleCheck.byId", None), ("design.ruleCheck.byIds", None)]
    assert {o.root for o in links.reads} == {"design"}


def test_reads_through_interface_and_writes_by_payload():
    links = ApiIndex(SNAP).links_for("BomWip")
    assert _paths(links.reads) == [("bomBomById", "Bom")]
    assert _paths(links.writes) == [("bomCreateBom", None)]


def test_write_candidates_by_name_exclude_longer_types():
    links = ApiIndex(SNAP).links_for("DesX")
    assert [o.path for o in links.write_candidates] == ["desCreateX", "desUpdateXParams"]


def test_reached_via_for_nested_only_types():
    links = ApiIndex(SNAP).links_for("DesStage")
    assert links.reads == []
    assert links.reached_via == ["DesX.stages"]


def test_unknown_type_returns_none():
    assert ApiIndex(SNAP).links_for("Nope") is None


def test_urls_with_and_without_docs_page_index():
    idx = ApiIndex(SNAP)
    links = idx.links_for("RuleCheck")
    assert idx.type_url("RuleCheck") == f"{DOCS_BASE}/types/objects/RuleCheck/"
    assert idx.type_url("Bom") == f"{DOCS_BASE}/types/interfaces/Bom/"
    assert idx.type_url("DesUnion") == f"{DOCS_BASE}/types/unions/DesUnion/"
    assert idx.operation_url(links.reads[0]) == f"{DOCS_BASE}/operations/queries/design/"
    only_type = ApiIndex(SNAP, doc_pages={"types/objects/RuleCheck"})
    assert only_type.type_url("RuleCheck") == f"{DOCS_BASE}/types/objects/RuleCheck/"
    assert only_type.operation_url(links.reads[0]) is None


SNAP2 = {
    "query_type": "Query",
    "mutation_type": "Mutation",
    "types": {
        "Query": {"kind": "OBJECT", "fields": {
            "bomById": "Bom", "previewThing": "Item", "itemById": "Item", "design": "DesignQueries!",
        }},
        "DesignQueries": {"kind": "OBJECT", "fields": {"preview": "PreviewQueries!", "thing": "ThingQueries!"}},
        "PreviewQueries": {"kind": "OBJECT", "fields": {"itemById": "Item"}},
        "ThingQueries": {"kind": "OBJECT", "fields": {"itemById": "Item"}},
        "Bom": {"kind": "OBJECT", "fields": {"items": "BomItemsConnection", "id": "ID!"}, "interfaces": ["Node"]},
        "BomItemsConnection": {"kind": "OBJECT", "fields": {"nodes": "[BomItem!]"}},
        "BomItem": {"kind": "OBJECT", "fields": {"elements": "[BomElement]"}},
        "BomElement": {"kind": "INTERFACE", "fields": {"id": "ID!"}, "possible_types": ["BomAlt"]},
        "BomAlt": {"kind": "OBJECT", "fields": {"id": "ID!"}, "interfaces": ["BomElement"]},
        "SysConnection": {"kind": "OBJECT", "fields": {"id": "ID!"}},
        "SysHolder": {"kind": "OBJECT", "fields": {"conn": "SysConnection"}},
        "Fam": {"kind": "OBJECT", "fields": {"parent": "Fam", "child": "Fam"}},
        "Zed": {"kind": "OBJECT", "fields": {"tgt": "Tgt"}},
        "Alpha": {"kind": "OBJECT", "fields": {"tgt": "Tgt"}, "interfaces": ["Node"]},
        "Item": {"kind": "OBJECT", "fields": {"id": "ID!"}},
        "Node": {"kind": "INTERFACE", "fields": {"id": "ID!"}, "possible_types": ["Alpha", "Bom"]},
        "Tgt": {"kind": "OBJECT", "fields": {"id": "ID!"}},
        "DesProj": {"kind": "OBJECT", "fields": {"id": "ID!"}, "interfaces": ["Node"]},
        "DesTask": {"kind": "OBJECT", "fields": {"id": "ID!"}, "interfaces": ["Node"]},
        "Mutation": {"kind": "OBJECT", "fields": {
            "desUpdateProjParams": "IdPayload!", "desCreateProjTask": "TaskPayload!",
        }},
        "IdPayload": {"kind": "OBJECT", "fields": {"id": "ID!"}},
        "TaskPayload": {"kind": "OBJECT", "fields": {"task": "DesTask", "id": "ID!"}},
        "ID": {"kind": "SCALAR"},
    },
}


def test_entity_named_connection_is_a_parent_not_a_wrapper():
    assert ApiIndex(SNAP2).links_for("SysConnection").reached_via == ["SysHolder.conn"]


def test_reached_via_follows_connections_and_interfaces():
    idx = ApiIndex(SNAP2)
    assert idx.links_for("BomItem").reached_via == ["Bom.items"]
    assert idx.links_for("BomAlt").reached_via == ["BomItem.elements"]


def test_reached_via_excludes_self_references():
    assert ApiIndex(SNAP2).links_for("Fam").reached_via == []


def test_reached_via_lists_refetchable_parents_first():
    assert ApiIndex(SNAP2).links_for("Tgt").reached_via == ["Alpha.tgt", "Zed.tgt"]


def test_write_candidates_skip_payloads_returning_other_entities():
    links = ApiIndex(SNAP2).links_for("DesProj")
    assert [o.path for o in links.write_candidates] == ["desUpdateProjParams"]


def test_preview_reads_sorted_last():
    paths = [o.path for o in ApiIndex(SNAP2).links_for("Item").reads]
    assert paths == ["design.thing.itemById", "itemById", "previewThing", "design.preview.itemById"]
