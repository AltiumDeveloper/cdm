# ESD (system_ESD)

- Name: `system_ESD`
- IRI: `sys:ESD` (https://w3id.org/altium/cdm/system/ESD)
- Bounded context: [system](../system.md)
- Kind: abstract, mixin
- Is a: [core_Meta](core_Meta.md)
- HTML page: [classes/system_ESD/](../../classes/system_ESD/)

Electronic System Design: a system-level block diagram of functional blocks and the connections between them, together with the hardware and software projects that implement the system.

## In the product

- [Electronic System Design](https://www.altium.com/documentation/altium-365/esd) (primary)

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| parameters | [system_Parameter](system_Parameter.md) | * |  |  |  |
| functionalBlocks | [system_FunctionalBlock](system_FunctionalBlock.md) | * | The functional blocks of the system design. |  |  |
| connections | [system_Connection](system_Connection.md) | * | The connections between functional blocks. |  |  |
| hardwareProjects | [system_HardwareProject](system_HardwareProject.md) | * | Hardware projects associated with this system design. |  |  |
| softwareProjects | [system_SoftwareProject](system_SoftwareProject.md) | * | Software projects associated with this system design. |  |  |
