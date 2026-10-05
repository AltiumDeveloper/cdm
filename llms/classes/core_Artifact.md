# Artifact (core_Artifact)

- Name: `core_Artifact`
- IRI: `core:Artifact` (https://w3id.org/altium/cdm/core/Artifact)
- Bounded context: [core](../core.md)
- Kind: Artifact, abstract
- Is a: [core_Entity](core_Entity.md)
- HTML page: [classes/core_Artifact/](../../classes/core_Artifact/)

Abstract base for persistent data objects that are created, stored, versioned, and consumed. Examples: components, documents, system models.

## In standards

- close: [prov:Entity](http://www.w3.org/ns/prov#Entity)
- related: [obo:BFO_0000031](http://purl.obolibrary.org/obo/BFO_0000031)

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| id | GRID | 1 | Globally unique identifier across the whole platform. |  | [core_Entity](core_Entity.md) |
