# Key Component (system_KeyComponent)

- Name: `system_KeyComponent`
- IRI: `sys:KeyComponent` (https://w3id.org/altium/cdm/system/KeyComponent)
- Bounded context: [system](../system.md)
- Kind: Resource
- Is a: [core_Resource](core_Resource.md)
- HTML page: [classes/system_KeyComponent/](../../classes/system_KeyComponent/)

A key component of a functional block in an ESD document, shown in the editor as a hardware component (e.g. a Renesas RA MCU chosen with the RA Explorer). Its device configuration (ports, package information, peripherals and pin assignments) can be viewed and edited on the hardware component. Software components of the block reference their parent key component. Its SDM counterpart is system_SdmHardwareComponent.

## In the product

- [Electronic System Design](https://www.altium.com/documentation/altium-365/esd#hardware_component) (primary)
- [Electronic System Design](https://www.altium.com/documentation/altium-365/esd#using_the_device_configuration)
- Term: **Hardware Component** (exact; altium-365)

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| id | string | 1 | Local unique identifier within a given context. |  |  |
| name | string | 0..1 | A short name of the entity. |  |  |
| parameters | [system_Parameter](system_Parameter.md) | * |  |  |  |
| childSoftwareComponentsIds | [system_SoftwareComponent](system_SoftwareComponent.md) | * |  |  |  |

## Referenced by

- [system_FunctionalBlock](system_FunctionalBlock.md): `keyComponents`
- [system_SoftwareComponent](system_SoftwareComponent.md): `parentKeyComponentId`
