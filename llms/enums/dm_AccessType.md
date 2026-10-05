# dm_AccessType

- Name: `dm_AccessType`
- IRI: `dm:AccessType` (https://w3id.org/altium/cdm/deviceModel/AccessType)
- Kind: enumeration
- HTML page: [enums/dm_AccessType/](../../enums/dm_AccessType/)

Specifies the access permissions for a register or memory region.

## Values

| Value | Description |
| --- | --- |
| `ReadOnly` | The register or memory region can only be read. |
| `WriteOnly` | The register or memory region can only be written to. |
| `ReadWrite` | The register or memory region can be both read from and written to. |

## Referenced by

- [dm_Register](../classes/dm_Register.md): `access`
- [dm_RegisterField](../classes/dm_RegisterField.md): `access`
