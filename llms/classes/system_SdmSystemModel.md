# System Model (system_SdmSystemModel)

- Name: `system_SdmSystemModel`
- IRI: `sys:SystemModel` (https://w3id.org/altium/cdm/system/SystemModel)
- Bounded context: [system-sdm](../system-sdm.md)
- Kind: Activity
- Is a: [core_Activity](core_Activity.md)
- HTML page: [classes/system_SdmSystemModel/](../../classes/system_SdmSystemModel/)

A high-level system model that captures the overall system architecture, crossing boundary between functional and logical domains (e.g., hardware and software).

## In the product

- [Renesas 365](https://www.altium.com/documentation/altium-365/renesas-365#system_data_model) (primary)
- [Electronic System Design](https://www.altium.com/documentation/altium-365/esd#pushing_pulling_sdm)
- [Working with Renesas 365 Solutions](https://www.altium.com/documentation/altium-designer/working-renesas-365-solutions#pulling_sdm_into_a_hardware_project)
- Term: **System Data Model** (exact; altium-365, altium-designer)
- Term: **SDM** (exact; altium-365, altium-designer)

## In the API

- Platform API type: [`SysSdmSystemModel`](https://altiumdeveloper.github.io/platform-api-docs/types/objects/SysSdmSystemModel/) (object)

## GRID

`grid:workspace:{workspace-id}:system-design:sdm/{id}`

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| name | string | 0..1 | A short name of the entity. |  |  |
| latestVersion | [system_SdmSystemModelVersion](system_SdmSystemModelVersion.md) | 1 | Latest version of the system model. |  |  |
| versions | [system_SdmSystemModelVersion](system_SdmSystemModelVersion.md) | * | Versions of the system model, used for tracking changes over time. |  |  |
| id | GRID | 1 | Globally unique identifier across the whole platform. |  | [core_Entity](core_Entity.md) |
