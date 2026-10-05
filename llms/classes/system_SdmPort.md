# Port (system_SdmPort)

- Name: `system_SdmPort`
- IRI: `sys:SdmPort` (https://w3id.org/altium/cdm/system/SdmPort)
- Bounded context: [system-sdm](../system-sdm.md)
- Kind: Resource
- Is a: [core_Resource](core_Resource.md)
- Mixins: [system_SdmMappableEntity](system_SdmMappableEntity.md), [system_HasSdmReferenceDesignator](system_HasSdmReferenceDesignator.md)
- HTML page: [classes/system_SdmPort/](../../classes/system_SdmPort/)

Represents a port within a system design. It is a logical interface of a functional block, distinct from dm_Port, which is a physical port of a device.

## In the API

- Platform API type: [`SysSdmPort`](https://altiumdeveloper.github.io/platform-api-docs/types/objects/SysSdmPort/) (object)

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| name | string | 0..1 | A short name of the entity. |  |  |
| parameters | [system_Parameter](system_Parameter.md) | * |  |  |  |
| portType | [system_PortType](../enums/system_PortType.md) | 0..1 | The type of this port (e.g., UART, GPIO, I2C). |  |  |
| hardwareComponentId | [system_SdmHardwareComponent](system_SdmHardwareComponent.md) | 0..1 | The hardware component associated with this port. |  |  |
| softwareComponentId | [system_SdmSoftwareComponent](system_SdmSoftwareComponent.md) | 0..1 | The software component associated with this port. |  |  |
| peripheralInstanceId | [dm_PeripheralInstance](dm_PeripheralInstance.md) | 0..1 | The peripheral instance associated with this port. |  |  |
| id | string | 1 | Local unique identifier within a given context. |  | [system_SdmMappableEntity](system_SdmMappableEntity.md) |
| sdmReferenceDesignator | string | 1 | Reference designator |  | [system_HasSdmReferenceDesignator](system_HasSdmReferenceDesignator.md) |

## Referenced by

- [system_SdmEndpoint](system_SdmEndpoint.md): `portId`
- [system_SdmFunctionalBlock](system_SdmFunctionalBlock.md): `ports`
