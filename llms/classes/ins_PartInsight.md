# Part Insight (ins_PartInsight)

- Name: `ins_PartInsight`
- IRI: `ins:PartInsight` (https://w3id.org/altium/cdm/insights/PartInsight)
- Bounded context: [insights](../insights.md)
- Kind: Activity
- Is a: [ins_Insight](ins_Insight.md)
- HTML page: [classes/ins_PartInsight/](../../classes/ins_PartInsight/)

## In the API

- Platform API type: [`DesWorkspaceInsInsight`](https://altiumdeveloper.github.io/platform-api-docs/types/objects/DesWorkspaceInsInsight/) (object)

## GRID

`grid:workspace:{workspace-id}:insights:insight/{id}`

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| part | [lib_Part](lib_Part.md) | 1 | Part associated with this insight | core_informs |  |
| informedBy | [pro_BomWIP](pro_BomWIP.md) or [des_Project](des_Project.md) | * | Entities associated with this insight | core_informedBy |  |
| occursIn | [pro_BomRelease](pro_BomRelease.md) or [des_ProjectRelease](des_ProjectRelease.md) or [lib_ComponentRevision](lib_ComponentRevision.md) | * | Entities associated with this insight | core_occursIn |  |
| tasks | [col_Task](col_Task.md) | * | Task associated with this insight | core_informs | [ins_Insight](ins_Insight.md) |
| id | GRID | 1 | Globally unique identifier across the whole platform. |  | [core_Entity](core_Entity.md) |
