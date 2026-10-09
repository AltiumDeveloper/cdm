# Processor (dm_Processor)

- Name: `dm_Processor`
- IRI: `dm:Processor` (https://w3id.org/altium/cdm/deviceModel/Processor)
- Bounded context: [deviceModel](../deviceModel.md)
- Kind: Resource
- Is a: [core_Resource](core_Resource.md)
- HTML page: [classes/dm_Processor/](../../classes/dm_Processor/)

Represents a physical processing core. Defining endianness and clock frequency allows the system to determine if the hardware can meet the computational and data-ordering requirements of a use-case.

## In standards

- close: [CMSIS-Pack PDSC processor element](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_family_pg.html#element_processor)
- close: [CMSIS-SVD cpu element](https://open-cmsis-pack.github.io/svd-spec/main/elem_cpu.html)

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| name | string | 1 | The unique identifier for this processor instance. |  |  |
| core | string | 1 | Architectural core type (e.g., Cortex-M4). |  |  |
| endian | [dm_Endianness](../enums/dm_Endianness.md) | 1 | The byte-ordering capability of the core. |  |  |
| clock | integer | 1 | The operating frequency in Hz. |  |  |

## Referenced by

| From | Field | Cardinality | Relation |
| --- | --- | --- | --- |
| [dm_FullStackDeviceModel](dm_FullStackDeviceModel.md) | processors | * |  |
