# Hardware Project Variant (des_ProjectVariant)

- Name: `des_ProjectVariant`
- IRI: `des:ProjectVariant` (https://w3id.org/altium/cdm/design/ProjectVariant)
- Bounded context: [design](../design.md)
- Kind: Resource
- Is a: [core_Resource](core_Resource.md)
- HTML page: [classes/des_ProjectVariant/](../../classes/des_ProjectVariant/)

A design variant of a project: a named variation of the same base design that is assembled with a different set of components. Within a variant, each component can be fitted, not fitted, fitted with varied parameters, or replaced by an alternate part, and the variant can define its own variant-level parameters. Assembly variants share one bare board, whereas fabrication variants also change overlay information and so need a different board.

## In the product

- [Design Variants](https://www.altium.com/documentation/altium-designer/design-variants) (primary)
- [Working with the Variant Manager](https://www.altium.com/documentation/altium-designer/variant-manager)
- Term: **design variant** (exact; altium-designer)

## In the API

- Platform API type: [`DesWipVariant`](https://altiumdeveloper.github.io/platform-api-docs/types/objects/DesWipVariant/) (object)

## Referenced by

| From | Field | Cardinality | Relation |
| --- | --- | --- | --- |
| [des_Project](des_Project.md) | variants | * |  |
