# Component Revision (lib_ComponentRevision)

- Name: `lib_ComponentRevision`
- IRI: `lib:ComponentRevision` (https://w3id.org/altium/cdm/library/ComponentRevision)
- Bounded context: [library](../library.md)
- Kind: Artifact
- Is a: [core_Artifact](core_Artifact.md)
- Mixins: [plt_HasLifecycle](plt_HasLifecycle.md)
- HTML page: [classes/lib_ComponentRevision/](../../classes/lib_ComponentRevision/)

Revision of a Component.

## In the product

- [Building & Maintaining Your Components and Libraries](https://www.altium.com/documentation/altium-designer/components-libraries#WSL) (primary)
- [Single Component Editing](https://www.altium.com/documentation/altium-designer/components-libraries/single-component-editing)
- [Working with Items](https://www.altium.com/documentation/altium-designer/connected-workspace/items)

## In the API

- Platform API type: [`DesComponent`](https://altiumdeveloper.github.io/platform-api-docs/types/objects/DesComponent/) (object)

## GRID

`grid:workspace:{workspace-id}:library:component-revision/{id}`

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| consistsOfParts | [lib_Part](lib_Part.md) | * | Parts used in this Artifact | core_hasPart |  |
| parameters | [lib_ComponentParameter](lib_ComponentParameter.md) | * | Component parameters |  |  |
| partChoiceList | [lib_PartChoiceList](lib_PartChoiceList.md) | 1 | List of part choices |  |  |
| template | [lib_ComponentTemplateRevision](lib_ComponentTemplateRevision.md) | 0..1 |  | core_derivedFrom |  |
| symbols | [lib_SymbolRevision](lib_SymbolRevision.md) | * |  | core_hasPart |  |
| footprints | [lib_FootprintRevision](lib_FootprintRevision.md) | * |  | core_hasPart |  |
| usedByProjectVariant | [des_Project](des_Project.md) | * | There is a relation per each project/variant where this Component Revision is used. | core_inputOf |  |
| lifecycleState | [plt_LifecycleState](plt_LifecycleState.md) | 1 | The current lifecycle state assigned to this entity. |  | [plt_HasLifecycle](plt_HasLifecycle.md) |
| id | GRID | 1 | Globally unique identifier across the whole platform. |  | [core_Entity](core_Entity.md) |

## Referenced by

| From | Field | Cardinality | Relation |
| --- | --- | --- | --- |
| [des_Project](des_Project.md) | usesComponents | * | core_hasInput |
| [des_ProjectRelease](des_ProjectRelease.md) | consistsOfComponents | * | core_hasPart |
| [ins_PartInsight](ins_PartInsight.md) | occursIn | * | core_occursIn |
| [lib_Component](lib_Component.md) | revisions | * | core_revisions |
| [lib_ManagedSheetRevision](lib_ManagedSheetRevision.md) | consistsOfComponents | * | core_hasPart |
| [lib_ReuseBlockRevision](lib_ReuseBlockRevision.md) | consistsOfComponents | * | core_hasPart |
| [pro_BomItemElement](pro_BomItemElement.md) | component | 0..1 |  |
| [pro_BomRelease](pro_BomRelease.md) | consistsOfComponents | * | core_hasPart |
| [pro_BomWIP](pro_BomWIP.md) | usesComponents | * | core_hasInput |
