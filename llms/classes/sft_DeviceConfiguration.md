# Device Configuration (sft_DeviceConfiguration)

- Name: `sft_DeviceConfiguration`
- IRI: `sft:DeviceConfiguration` (https://w3id.org/altium/cdm/software/DeviceConfiguration)
- Bounded context: [software](../software.md)
- Kind: Artifact
- Is a: [core_Artifact](core_Artifact.md)
- HTML page: [classes/sft_DeviceConfiguration/](../../classes/sft_DeviceConfiguration/)

The configuration of a device (e.g. an MCU placed as a hardware component in an ESD document), covering its ports, package information, peripherals and pin assignments. It is viewed and edited on the hardware component in the ESD document, and the pin functions it defines can be pulled from the solution's SDM onto the pins of the associated component in a hardware project in Altium Designer.

## In the product

- [Electronic System Design](https://www.altium.com/documentation/altium-365/esd#using_the_device_configuration) (primary)
- [Working with Renesas 365 Solutions](https://www.altium.com/documentation/altium-designer/working-renesas-365-solutions#pulling_sdm_into_a_hardware_project)

## In the API

- Platform API type: [`SftDevCfgDeviceConfiguration`](https://altiumdeveloper.github.io/platform-api-docs/types/objects/SftDevCfgDeviceConfiguration/) (object)

## GRID

`grid:workspace:{workspace-id}:software:device-configuration/{id}`

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| revisions | [sft_DeviceConfigurationRevision](sft_DeviceConfigurationRevision.md) | * | The set of versioned snapshots derived from this artifact. | core_revisions |  |
| id | GRID | 1 | Globally unique identifier across the whole platform. |  | [core_Entity](core_Entity.md) |

## Referenced by

| From | Field | Cardinality | Relation |
| --- | --- | --- | --- |
| [sft_SoftwareProject](sft_SoftwareProject.md) | deviceConfiguration | 0..1 | core_hasOutput |
