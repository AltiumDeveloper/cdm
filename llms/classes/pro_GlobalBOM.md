# Global BOM (pro_GlobalBOM)

- Name: `pro_GlobalBOM`
- IRI: `pro:GlobalBOM` (https://w3id.org/altium/cdm/procurement/GlobalBOM)
- Bounded context: [procurement](../procurement.md)
- Kind: Activity
- Is a: [core_Activity](core_Activity.md)
- Mixins: [pro_Bom](pro_Bom.md)
- HTML page: [classes/pro_GlobalBOM/](../../classes/pro_GlobalBOM/)

Global BOM represents a bill of materials that resides outside of any workspace, on Octopart, where users can create, edit, collaborate on and share it with others.

## Comments

- Global BOM follows the same conceptual BOM model as workspace-scoped BOMs (items, alternates, substitutes and issues), but its identity and access are not bound to a workspace. This mirrors other entities that can exist both workspace-scoped and globally (e.g. workspace Hardware Projects vs. personal, shareable projects).
- Global BOM does not produce releases yet, hence it does not specialise BOM WIP and has no releases relation.
- Global BOM has no access to workspace libraries, so it references supply Parts only. Its item elements resolve to supply Parts; the workspace component reference is not used.

## In the product

- No public product documentation exists for this concept.

## GRID

`grid:global::procurement:bom/{id}`

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| usesParts | [sup_Part](sup_Part.md) | * | Supply Parts used in this Global BOM. | core_hasInput |  |
| issues | [pro_BomIssue](pro_BomIssue.md) | * |  |  | [pro_Bom](pro_Bom.md) |
| items | [pro_BomItem](pro_BomItem.md) | * |  |  | [pro_Bom](pro_Bom.md) |
| id | GRID | 1 | Globally unique identifier across the whole platform. |  | [core_Entity](core_Entity.md) |
