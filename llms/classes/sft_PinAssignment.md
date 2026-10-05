# Pin Assignment (sft_PinAssignment)

- Name: `sft_PinAssignment`
- IRI: `sft:PinAssignment` (https://w3id.org/altium/cdm/software/PinAssignment)
- Bounded context: [software](../software.md)
- Kind: Resource
- Is a: [core_Resource](core_Resource.md)
- HTML page: [classes/sft_PinAssignment/](../../classes/sft_PinAssignment/)

The assignment of a function to one pin of a device, identified by pin number and name. When a hardware project pulls changes from the solution's SDM, pin functions from the device configuration are added to or removed from the pins of the associated component.

## In the product

- [Working with Renesas 365 Solutions](https://www.altium.com/documentation/altium-designer/working-renesas-365-solutions#pulling_sdm_into_a_hardware_project) (primary)

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| pinNumber | integer | 1 |  |  |  |
| pinName | string | 1 |  |  |  |
| pinFunction | string | 1 |  |  |  |
| symbolicName | string | 1 |  |  |  |

## Referenced by

- [sft_PinAssignmentModel](sft_PinAssignmentModel.md): `pins`
