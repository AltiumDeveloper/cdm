# Global ESD (system_GlobalESD)

- Name: `system_GlobalESD`
- IRI: `sys:GlobalESD` (https://w3id.org/altium/cdm/system/GlobalESD)
- Bounded context: [system](../system.md)
- Kind: Activity
- Is a: [core_Activity](core_Activity.md)
- Mixins: [system_ESD](system_ESD.md)
- HTML page: [classes/system_GlobalESD/](../../classes/system_GlobalESD/)

An Electronic System Design that resides outside of any Workspace. It has the same content as an ESD document but is not part of a solution.

## In the product

- No public product documentation exists for this concept.

## GRID

`grid:global::system-design:esd/{id}`

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| parameters | [system_Parameter](system_Parameter.md) | * |  |  | [system_ESD](system_ESD.md) |
| functionalBlocks | [system_FunctionalBlock](system_FunctionalBlock.md) | * | The functional blocks of the system design. |  | [system_ESD](system_ESD.md) |
| connections | [system_Connection](system_Connection.md) | * | The connections between functional blocks. |  | [system_ESD](system_ESD.md) |
| hardwareProjects | [system_HardwareProject](system_HardwareProject.md) | * | Hardware projects associated with this system design. |  | [system_ESD](system_ESD.md) |
| softwareProjects | [system_SoftwareProject](system_SoftwareProject.md) | * | Software projects associated with this system design. |  | [system_ESD](system_ESD.md) |
| id | GRID | 1 | Globally unique identifier across the whole platform. |  | [core_Entity](core_Entity.md) |
