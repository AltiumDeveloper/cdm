# Entity (core_Entity)

- Name: `core_Entity`
- IRI: `core:Entity` (https://w3id.org/altium/cdm/core/Entity)
- Bounded context: [core](../core.md)
- Kind: Entity, abstract
- Subclasses: [core_Activity](core_Activity.md), [core_Artifact](core_Artifact.md)
- Mixins (instantiates): [core_WithGRID](core_WithGRID.md), [core_WithMaturity](core_WithMaturity.md), [core_WithPlatformAPI](core_WithPlatformAPI.md)
- HTML page: [classes/core_Entity/](../../classes/core_Entity/)

Abstract base for all identifiable, versioned, platform-accessible domain objects. Carries a GRID, maturity level, and platform API reference.

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| id | GRID | 1 | Globally unique identifier across the whole platform. |  |  |
