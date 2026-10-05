# Activity (core_Activity)

- Name: `core_Activity`
- IRI: `core:Activity` (https://w3id.org/altium/cdm/core/Activity)
- Bounded context: [core](../core.md)
- Kind: Activity, abstract
- Is a: [core_Entity](core_Entity.md)
- HTML page: [classes/core_Activity/](../../classes/core_Activity/)

Abstract base for process and work objects — things that happen, use inputs, and produce outputs. Examples: projects, releases, design workflows.

## In standards

- close: [prov:Activity](http://www.w3.org/ns/prov#Activity)
- related: [obo:BFO_0000015](http://purl.obolibrary.org/obo/BFO_0000015)

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| id | GRID | 1 | Globally unique identifier across the whole platform. |  | [core_Entity](core_Entity.md) |

## Referenced by

- [req_Requirement](req_Requirement.md): `verifiedByActivities`
