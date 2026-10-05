# Comment Thread (col_CommentThread)

- Name: `col_CommentThread`
- IRI: `col:CommentThread` (https://w3id.org/altium/cdm/collaboration/CommentThread)
- Bounded context: [collaboration](../collaboration.md)
- Kind: Activity
- Is a: [core_Activity](core_Activity.md)
- HTML page: [classes/col_CommentThread/](../../classes/col_CommentThread/)

Comment Thread represents a structured discussion linked to a specific design object, document, or workspace item, capturing feedback, decisions, and context directly within the collaborative design environment.

## Comments

- Each Comment Thread has its own identity and lifecycle, grouping related comments and replies into a coherent conversation.
- It serves as a persistent communication artifact that promotes design review transparency, traceability, and cross-team collaboration within Altium 365 and connected design tools.

## In the product

- [Web Viewer](https://www.altium.com/documentation/altium-365/viewers/web-viewer#commenting) (primary)
- [Document Commenting](https://www.altium.com/documentation/altium-designer/document-commenting)

## In the API

- Platform API type: [`DesCommentThread`](https://altiumdeveloper.github.io/platform-api-docs/types/objects/DesCommentThread/) (object)

## GRID

`grid:workspace:{workspace-id}:collaboration:comment-thread/{id}`

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| comments | [col_Comment](col_Comment.md) | 1..* |  |  |  |
| id | GRID | 1 | Globally unique identifier across the whole platform. |  | [core_Entity](core_Entity.md) |
