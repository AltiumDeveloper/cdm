# system_SdmSoftwareComponentCategory

- Name: `system_SdmSoftwareComponentCategory`
- Kind: enumeration
- HTML page: [enums/system_SdmSoftwareComponentCategory/](../../enums/system_SdmSoftwareComponentCategory/)

High-level classification of software components.

## Values

| Value | Description |
| --- | --- |
| `DRIVER` | Low-level HAL/drivers interacting with hardware. |
| `MIDDLEWARE` | Functional stacks (e.g., Motor Control, USB, TCP/IP). |
| `OPERATING_SYSTEM` | Kernel or RTOS components. |
| `APPLICATION` | High-level logic, AI models, or user-defined code. |
| `LIBRARY` | Static utility code or mathematical libraries. |

## Referenced by

| From | Field | Cardinality | Relation |
| --- | --- | --- | --- |
| [system_SdmSoftwareSpecification](../classes/system_SdmSoftwareSpecification.md) | category | 0..1 |  |
