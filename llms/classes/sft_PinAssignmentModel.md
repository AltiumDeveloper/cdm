# Pin Assignment Model (sft_PinAssignmentModel)

- Name: `sft_PinAssignmentModel`
- IRI: `sft:PinAssignmentModel` (https://w3id.org/altium/cdm/software/PinAssignmentModel)
- Bounded context: [software](../software.md)
- Kind: Resource
- Is a: [core_Resource](core_Resource.md)
- HTML page: [classes/sft_PinAssignmentModel/](../../classes/sft_PinAssignmentModel/)

The set of pin assignments of a device, one part of its device configuration alongside ports, package information and peripherals.

## In the product

- [Electronic System Design](https://www.altium.com/documentation/altium-365/esd#using_the_device_configuration) (primary)

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| pins | [sft_PinAssignment](sft_PinAssignment.md) | 1..* |  |  |  |

## Referenced by

| From | Field | Cardinality | Relation |
| --- | --- | --- | --- |
| [sft_DeviceConfigurationRevision](sft_DeviceConfigurationRevision.md) | pinModel | 1 |  |
