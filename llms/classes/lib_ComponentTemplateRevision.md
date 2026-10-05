# Component Template Revision (lib_ComponentTemplateRevision)

- Name: `lib_ComponentTemplateRevision`
- IRI: `lib:ComponentTemplateRevision` (https://w3id.org/altium/cdm/library/ComponentTemplateRevision)
- Bounded context: [library](../library.md)
- Kind: Artifact
- Is a: [core_Artifact](core_Artifact.md)
- Mixins: [plt_HasLifecycle](plt_HasLifecycle.md)
- HTML page: [classes/lib_ComponentTemplateRevision/](../../classes/lib_ComponentTemplateRevision/)

A revision of a Component Template: the template definition, stored as a *.CMPT document, saved into the Workspace at one point in time. A component revision can be linked to a specific template revision, from which it takes its predefined parameters, models and settings.

## In the product

- [Component Templates](https://www.altium.com/documentation/altium-designer/components-libraries/workspace-component-templates) (primary)
- [Working with Items](https://www.altium.com/documentation/altium-designer/connected-workspace/items)

## In the API

- Platform API type: [`DesComponentTemplateRevision`](https://altiumdeveloper.github.io/platform-api-docs/types/objects/DesComponentTemplateRevision/) (object)

## GRID

`grid:workspace:{workspace-id}:library:component-template-revision/{id}`

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| lifecycleState | [plt_LifecycleState](plt_LifecycleState.md) | 1 | The current lifecycle state assigned to this entity. |  | [plt_HasLifecycle](plt_HasLifecycle.md) |
| id | GRID | 1 | Globally unique identifier across the whole platform. |  | [core_Entity](core_Entity.md) |

## Referenced by

- [lib_ComponentRevision](lib_ComponentRevision.md): `template`
- [lib_ComponentTemplate](lib_ComponentTemplate.md): `revisions`
