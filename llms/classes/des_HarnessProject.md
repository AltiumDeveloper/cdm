# Harness Project (des_HarnessProject)

- Name: `des_HarnessProject`
- IRI: `des:HarnessProject` (https://w3id.org/altium/cdm/design/HarnessProject)
- Bounded context: [design](../design.md)
- Kind: Activity
- Is a: [des_Project](des_Project.md)
- HTML page: [classes/des_HarnessProject/](../../classes/des_HarnessProject/)

Harness Project defines the design of a cable and wiring harness as a standalone yet integrable artifact, capturing connectors, wires, splices, and pin-to-pin mappings required to implement electrical interconnects between boards and system elements.

## Comments

- Harness Project provides a structured representation of connectivity at the physical wiring level, complementing schematic and PCB projects while maintaining its own lifecycle and identity. It enables engineers to design, document, and validate interconnects in a way that is traceable, manufacturable, and tightly integrated with Multiboard and MCAD workflows within the Altium ecosystem.

## In the product

- [Harness Design](https://www.altium.com/documentation/altium-designer/harness-design) (primary)

## In the API

- Platform API type: [`DesProject`](https://altiumdeveloper.github.io/platform-api-docs/types/objects/DesProject/) (object)

## GRID

None declared (nearest ancestor `des_Project`: `grid:workspace:{workspace-id}:design:project/{id}`).

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| releases | [des_ProjectRelease](des_ProjectRelease.md) | * | The release artifacts produced by this activity. | core_releases | [des_Project](des_Project.md) |
| usesParts | [lib_Part](lib_Part.md) | * | Parts used in this Activity | core_hasInput | [des_Project](des_Project.md) |
| usesComponents | [lib_ComponentRevision](lib_ComponentRevision.md) | * | Components used in this Activity | core_hasInput | [des_Project](des_Project.md) |
| parameters | [des_ProjectParameter](des_ProjectParameter.md) | * |  |  | [des_Project](des_Project.md) |
| variants | [des_ProjectVariant](des_ProjectVariant.md) | * |  |  | [des_Project](des_Project.md) |
| partOfSolution | [plt_Solution](plt_Solution.md) | * |  | core_partOf | [plt_SolutionItem](plt_SolutionItem.md) |
| id | GRID | 1 | Globally unique identifier across the whole platform. |  | [core_Entity](core_Entity.md) |
