# AddressMap (dm_AddressMap)

- Name: `dm_AddressMap`
- IRI: `dm:AddressMap` (https://w3id.org/altium/cdm/deviceModel/AddressMap)
- Bounded context: [deviceModel](../deviceModel.md)
- Kind: Resource
- Is a: [core_Resource](core_Resource.md)
- HTML page: [classes/dm_AddressMap/](../../classes/dm_AddressMap/)

Address map for the device including memory and peripheral regions.

## In the API

- Platform API type: [`DmAddressMapModel`](https://altiumdeveloper.github.io/platform-api-docs/types/objects/DmAddressMapModel/) (object)

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| segments | [dm_AddressSegment](dm_AddressSegment.md) | * | A collection of memory segments defined within the device's address space. |  |  |

## Referenced by

| From | Field | Cardinality | Relation |
| --- | --- | --- | --- |
| [dm_FullStackDeviceModel](dm_FullStackDeviceModel.md) | addressMap | 0..1 |  |
