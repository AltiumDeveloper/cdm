# Insight (ins_Insight)

- Name: `ins_Insight`
- IRI: `ins:Insight` (https://w3id.org/altium/cdm/insights/Insight)
- Bounded context: [insights](../insights.md)
- Kind: Activity, abstract
- Is a: [core_Activity](core_Activity.md)
- Subclasses: [ins_PartInsight](ins_PartInsight.md)
- HTML page: [classes/ins_Insight/](../../classes/ins_Insight/)

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| tasks | [col_Task](col_Task.md) | * | Task associated with this insight | core_informs |  |
| id | GRID | 1 | Globally unique identifier across the whole platform. |  | [core_Entity](core_Entity.md) |
