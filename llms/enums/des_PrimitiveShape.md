# Primitive Shape (des_PrimitiveShape)

- Name: `des_PrimitiveShape`
- IRI: `des:PrimitiveShape` (https://w3id.org/altium/cdm/design/PrimitiveShape)
- Kind: enumeration
- HTML page: [enums/des_PrimitiveShape/](../../enums/des_PrimitiveShape/)

The shape of a pad or via (Platform API DesPrimitiveShape).

## Values

| Value | Description |
| --- | --- |
| `None` | Platform API NONE. AD SDK TShape.eNoShape (matched by name, [interpretation]). |
| `Round` | Platform API ROUND. AD SDK TShape.eRounded (matched by name, [interpretation]). |
| `Rectangle` | Platform API RECTANGLE. AD SDK TShape.eRectangular (matched by name, [interpretation]). |
| `Octagon` | Platform API OCTAGON. AD SDK TShape.eOctagonal (matched by name, [interpretation]). |
| `Circle` | Platform API CIRCLE. AD SDK TShape.eCircleShape (matched by name, [interpretation]). |
| `Arc` | Platform API ARC. AD SDK TShape.eArcShape (matched by name, [interpretation]). |
| `Terminator` | Platform API TERMINATOR. AD SDK TShape.eTerminator (matched by name, [interpretation]). |
| `RoundRectangle` | Platform API ROUND_RECTANGLE. AD SDK TShape.eRoundRectShape (matched by name, [interpretation]). |
| `RotatedRectangle` | Platform API ROTATED_RECTANGLE. AD SDK TShape.eRotatedRectShape (matched by name, [interpretation]). |
| `RoundedRectangle` | Platform API ROUNDED_RECTANGLE. AD SDK TShape.eRoundedRectangular (matched by name, [interpretation]). |
| `Custom` | Platform API CUSTOM. AD SDK TShape.eCustomShape (matched by name, [interpretation]). |

## Referenced by

| From | Field | Cardinality | Relation |
| --- | --- | --- | --- |
| [des_Pad](../classes/des_Pad.md) | shape | 0..1 |  |
| [des_Via](../classes/des_Via.md) | shape | 0..1 |  |
