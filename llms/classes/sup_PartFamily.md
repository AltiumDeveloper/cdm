# Part Family (sup_PartFamily)

- Name: `sup_PartFamily`
- IRI: `sup:PartFamily` (https://w3id.org/altium/cdm/supply/PartFamily)
- Bounded context: [supply](../supply.md)
- Kind: Artifact
- Is a: [core_Artifact](core_Artifact.md)
- HTML page: [classes/sup_PartFamily/](../../classes/sup_PartFamily/)

A manufacturer's grouping of parts in the supply data, where the kind of family is vendor-specific (e.g. Series or Family). Part families form a hierarchy: a family has either child families or, at the lowest level, Part Groups. Families sharing the same parent are usually close alternatives to one another.

## In the API

- Platform API type: [`SupPartFamily`](https://altiumdeveloper.github.io/platform-api-docs/types/objects/SupPartFamily/) (object)

## GRID

`grid:supply::platform:part-family/{id}`

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| partGroups | [sup_PartGroup](sup_PartGroup.md) | * | Part groups belonging to this part family. |  |  |
| alternatives | [sup_PartFamily](sup_PartFamily.md) | * | Alternative part families that can substitute this one. |  |  |
| id | GRID | 1 | Globally unique identifier across the whole platform. |  | [core_Entity](core_Entity.md) |
