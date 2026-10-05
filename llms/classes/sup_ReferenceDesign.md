# Reference Design (sup_ReferenceDesign)

- Name: `sup_ReferenceDesign`
- IRI: `sup:ReferenceDesign` (https://w3id.org/altium/cdm/supply/ReferenceDesign)
- Bounded context: [supply](../supply.md)
- Kind: Artifact
- Is a: [core_Artifact](core_Artifact.md)
- HTML page: [classes/sup_ReferenceDesign/](../../classes/sup_ReferenceDesign/)

An example design published in the supply catalog, bringing together its design files (e.g. schematics and layouts), documentation and the parts it uses. In Renesas 365 a reference design can be imported into a solution, which adds it to the Workspace as a PCB project linked to that solution.

## In the product

- [Renesas 365](https://www.altium.com/documentation/altium-365/renesas-365#import_project) (primary)

## In the API

- Platform API type: [`SupRefDesign`](https://altiumdeveloper.github.io/platform-api-docs/types/objects/SupRefDesign/) (object)

## GRID

`grid:supply::platform:ref-design/{id}`

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| id | GRID | 1 | Globally unique identifier across the whole platform. |  | [core_Entity](core_Entity.md) |

## Referenced by

- [sup_Part](sup_Part.md): `referenceDesigns`
