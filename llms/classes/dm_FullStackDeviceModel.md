# FullStackDeviceModel (dm_FullStackDeviceModel)

- Name: `dm_FullStackDeviceModel`
- IRI: `dm:FullStackDeviceModel` (https://w3id.org/altium/cdm/deviceModel/FullStackDeviceModel)
- Bounded context: [deviceModel](../deviceModel.md)
- Kind: Artifact
- Is a: [core_Artifact](core_Artifact.md)
- HTML page: [classes/dm_FullStackDeviceModel/](../../classes/dm_FullStackDeviceModel/)

A digital twin of an embedded hardware device. It exposes the full device model, including interfaces, peripherals, and ports.

## In the API

- Platform API type: [`DmFullStackDeviceModel`](https://altiumdeveloper.github.io/platform-api-docs/types/objects/DmFullStackDeviceModel/) (object)

## In standards

- close: [CMSIS-SVD device element](https://open-cmsis-pack.github.io/svd-spec/main/elem_device.html)
- close: [CMSIS-Pack PDSC device element](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_family_pg.html#element_device)

## GRID

`grid:global::device-model:fullstack-dm/{id}`

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| mpn | string | 1 | Manufacturer Part Number (MPN) for the device. |  |  |
| peripherals | [dm_Peripheral](dm_Peripheral.md) | * | List of all peripherals available on the device. |  |  |
| ports | [dm_Port](dm_Port.md) | * | List of physical ports on the device. |  |  |
| family | string | 1 | The family to which the device belongs. |  |  |
| processors | [dm_Processor](dm_Processor.md) | * | List of processors included in the device. |  |  |
| addressMap | [dm_AddressMap](dm_AddressMap.md) | 0..1 | The hardware address map configuration. |  |  |
| id | GRID | 1 | Globally unique identifier across the whole platform. |  | [core_Entity](core_Entity.md) |
