# Design Insight (ins_DesignInsight)

- Name: `ins_DesignInsight`
- IRI: `ins:DesignInsight` (https://w3id.org/altium/cdm/insights/DesignInsight)
- Bounded context: [insights](../insights.md)
- Kind: Activity
- Is a: [ins_Insight](ins_Insight.md)
- HTML page: [classes/ins_DesignInsight/](../../classes/ins_DesignInsight/)

An insight within the design domain: a finding, detected asynchronously, about the design under review in a design review. It is always part of that review and can be followed up by tasks.

## In the product

- No public product documentation exists for this concept.

## In the API

- Platform API type: [`DesWorkspaceInsInsight`](https://altiumdeveloper.github.io/platform-api-docs/types/objects/DesWorkspaceInsInsight/) (object)
- Inherited from [ins_Insight](ins_Insight.md).

## GRID

None declared (nearest ancestor `ins_Insight`: `grid:workspace:{workspace-id}:insights:insight/{id}`).

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| designReview | [col_DesignReview](col_DesignReview.md) | 1 | The design review that the insight is part of. | core_partOf |  |
| tasks | [col_Task](col_Task.md) | * | Task associated with this insight | core_informs | [ins_Insight](ins_Insight.md) |
| id | GRID | 1 | Globally unique identifier across the whole platform. |  | [core_Entity](core_Entity.md) |
