# Part (lib_Part)

- Name: `lib_Part`
- IRI: `lib:Part` (https://w3id.org/altium/cdm/library/Part)
- Bounded context: [library](../library.md)
- Kind: Artifact
- Is a: [core_Artifact](core_Artifact.md)
- HTML page: [classes/lib_Part/](../../classes/lib_Part/)

A manufacturer part, identified by manufacturer and part number, as held in the Workspace's Part Catalog together with the supplier parts through which it is sold. Workspace components reference manufacturer parts through their Part Choices.

## In the product

- [Adding Supply Chain Information to a Component](https://www.altium.com/documentation/altium-designer/components-libraries/adding-supply-chain-information-component#the_part_catalog) (primary)
- [Part Source Configuration](https://www.altium.com/documentation/altium-365/part-source-configuration)
- Term: **Manufacturer Part** (exact; altium-designer, altium-365)

## In the API

- Platform API type: [`DesPart`](https://altiumdeveloper.github.io/platform-api-docs/types/objects/DesPart/) (object)

## GRID

`grid:workspace:{workspace-id}:library:part/{id}`

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| id | GRID | 1 | Globally unique identifier across the whole platform. |  | [core_Entity](core_Entity.md) |

## Referenced by

- [des_Project](des_Project.md): `usesParts`
- [ins_PartInsight](ins_PartInsight.md): `part`
- [lib_ComponentRevision](lib_ComponentRevision.md): `consistsOfParts`
- [lib_PartChoice](lib_PartChoice.md): `part`
- [pro_BomItemElement](pro_BomItemElement.md): `part`
- [pro_BomRelease](pro_BomRelease.md): `consistsOfParts`
- [pro_BomWIP](pro_BomWIP.md): `usesParts`
