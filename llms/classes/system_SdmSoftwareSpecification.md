# Software Specification (system_SdmSoftwareSpecification)

- Name: `system_SdmSoftwareSpecification`
- IRI: `sys:SdmSoftwareSpecification` (https://w3id.org/altium/cdm/system/SdmSoftwareSpecification)
- Bounded context: [system-sdm](../system-sdm.md)
- Kind: Resource
- Is a: [core_Resource](core_Resource.md)
- HTML page: [classes/system_SdmSoftwareSpecification/](../../classes/system_SdmSoftwareSpecification/)

The "blueprint" for a software component. Captures the identity and classification of the software independently of any specific instance.

## In the API

- Platform API type: [`SysSdmSoftwareSpecification`](https://altiumdeveloper.github.io/platform-api-docs/types/objects/SysSdmSoftwareSpecification/) (object)

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| name | string | 0..1 | The identifier within the ecosystem (e.g., module.driver.uart). |  |  |
| category | [system_SdmSoftwareComponentCategory](../enums/system_SdmSoftwareComponentCategory.md) | 0..1 | The architectural role of this specification (e.g. DRIVER). |  |  |
| ecosystem | string | 0..1 | The platform or framework (e.g., FSP). |  |  |
| vendor | string | 0..1 | The organization providing the software (e.g. Renesas). |  |  |
| version | string | 0..1 |  |  |  |

## Referenced by

| From | Field | Cardinality | Relation |
| --- | --- | --- | --- |
| [system_SdmSoftwareStackInstance](system_SdmSoftwareStackInstance.md) | specification | 1 |  |
