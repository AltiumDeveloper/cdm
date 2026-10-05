# Part Group (sup_PartGroup)

- Name: `sup_PartGroup`
- IRI: `sup:PartGroup` (https://w3id.org/altium/cdm/supply/PartGroup)
- Bounded context: [supply](../supply.md)
- Kind: Artifact
- Is a: [core_Artifact](core_Artifact.md)
- HTML page: [classes/sup_PartGroup/](../../classes/sup_PartGroup/)

A leaf of the part family hierarchy in the supply data, holding the parts that belong to it together with group-level information such as its manufacturer, overview, key features and documents. Groups sharing the same parent family are usually close alternatives to one another.

## In the API

- Platform API type: [`SupPartGroup`](https://altiumdeveloper.github.io/platform-api-docs/types/objects/SupPartGroup/) (object)

## GRID

`grid:supply::platform:part-group/{id}`

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| parts | [sup_Part](sup_Part.md) | * | Parts belonging to this part group. |  |  |
| alternatives | [sup_PartGroup](sup_PartGroup.md) | * | Alternative part groups that can substitute this one. |  |  |
| id | GRID | 1 | Globally unique identifier across the whole platform. |  | [core_Entity](core_Entity.md) |

## Referenced by

- [sup_PartFamily](sup_PartFamily.md): `partGroups`
