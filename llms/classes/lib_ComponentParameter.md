# Component Parameter (lib_ComponentParameter)

- Name: `lib_ComponentParameter`
- IRI: `lib:ComponentParameter` (https://w3id.org/altium/cdm/library/ComponentParameter)
- Bounded context: [library](../library.md)
- Kind: Resource
- Is a: [core_Resource](core_Resource.md)
- HTML page: [classes/lib_ComponentParameter/](../../classes/lib_ComponentParameter/)

A named parameter of a Workspace component, holding a value and, optionally, a data type. Parameters can be inherited from a component template or added directly to the component; a template can give them unit-aware (e.g. Farad, Ohm) or dictionary-defined types.

## In the product

- [Component Templates](https://www.altium.com/documentation/altium-designer/components-libraries/workspace-component-templates#UACPDT) (primary)

## In the API

- Platform API type: [`DesComponentParameter`](https://altiumdeveloper.github.io/platform-api-docs/types/objects/DesComponentParameter/) (object)

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| name | string | 1 |  |  |  |
| value | string | 0..1 |  |  |  |
| type | string | 0..1 |  |  |  |

## Referenced by

- [lib_Component](lib_Component.md): `parameters`
- [lib_ComponentRevision](lib_ComponentRevision.md): `parameters`
