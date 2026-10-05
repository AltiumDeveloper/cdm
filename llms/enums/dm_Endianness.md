# dm_Endianness

- Name: `dm_Endianness`
- IRI: `dm:Endianness` (https://w3id.org/altium/cdm/deviceModel/Endianness)
- Kind: enumeration
- HTML page: [enums/dm_Endianness/](../../enums/dm_Endianness/)

Specifies the byte-ordering convention of the processor. Bi-endian indicates the hardware can be configured for either mode.

## Values

| Value | Description |
| --- | --- |
| `LittleEndian` | Least significant byte is stored at the lowest address. |
| `BigEndian` | Most significant byte is stored at the lowest address. |
| `BiEndian` | Processor supports switching between little and big endian modes. |

## Referenced by

- [dm_Processor](../classes/dm_Processor.md): `endian`
