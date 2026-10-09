# Parameter (system_Parameter)

- Name: `system_Parameter`
- IRI: `sys:Parameter` (https://w3id.org/altium/cdm/system/Parameter)
- Bounded context: [system](../system.md)
- Kind: Resource
- Is a: [core_Resource](core_Resource.md)
- HTML page: [classes/system_Parameter/](../../classes/system_Parameter/)

Name–value parameter associated with functional blocks, ports, or other system design resources.

## In the product

- [Electronic System Design](https://www.altium.com/documentation/altium-365/esd#accessing_object_properties) (primary)

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| id | string | 1 | Local unique identifier within a given context. |  |  |
| name | string | 0..1 | A short name of the entity. |  |  |
| value | string | 1 |  |  |  |

## Referenced by

| From | Field | Cardinality | Relation |
| --- | --- | --- | --- |
| [system_Connection](system_Connection.md) | parameters | * |  |
| [system_ESDDocument](system_ESDDocument.md) | parameters | * |  |
| [system_FunctionalBlock](system_FunctionalBlock.md) | parameters | * |  |
| [system_KeyComponent](system_KeyComponent.md) | parameters | * |  |
| [system_Port](system_Port.md) | parameters | * |  |
| [system_SdmClientMetadata](system_SdmClientMetadata.md) | parameters | * |  |
| [system_SdmConnection](system_SdmConnection.md) | parameters | * |  |
| [system_SdmFunctionalBlock](system_SdmFunctionalBlock.md) | parameters | * |  |
| [system_SdmHardwareComponent](system_SdmHardwareComponent.md) | parameters | * |  |
| [system_SdmPort](system_SdmPort.md) | parameters | * |  |
| [system_SdmSoftwareComponent](system_SdmSoftwareComponent.md) | parameters | * |  |
| [system_SdmSoftwareStackInstance](system_SdmSoftwareStackInstance.md) | parameters | * |  |
| [system_SoftwareComponent](system_SoftwareComponent.md) | parameters | * |  |
