# Project Template Revision (des_ProjectTemplateRevision)

- Name: `des_ProjectTemplateRevision`
- IRI: `des:ProjectTemplateRevision` (https://w3id.org/altium/cdm/design/ProjectTemplateRevision)
- Bounded context: [design](../design.md)
- Kind: Artifact
- Is a: [core_Artifact](core_Artifact.md)
- Mixins: [plt_HasLifecycle](plt_HasLifecycle.md)
- HTML page: [classes/des_ProjectTemplateRevision/](../../classes/des_ProjectTemplateRevision/)

An immutable revision of a project template.

## In the API

- Platform API type: [`DesProjectTemplateRevision`](https://altiumdeveloper.github.io/platform-api-docs/types/objects/DesProjectTemplateRevision/) (object)

## GRID

`grid:workspace:{workspace-id}:design:project-template-revision/{id}`

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| lifecycleState | [plt_LifecycleState](plt_LifecycleState.md) | 1 | The current lifecycle state assigned to this entity. |  | [plt_HasLifecycle](plt_HasLifecycle.md) |
| id | GRID | 1 | Globally unique identifier across the whole platform. |  | [core_Entity](core_Entity.md) |

## Referenced by

- [des_ProjectTemplate](des_ProjectTemplate.md): `revisions`
