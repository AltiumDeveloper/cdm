# Project Parameter (des_ProjectParameter)

- Name: `des_ProjectParameter`
- IRI: `des:ProjectParameter` (https://w3id.org/altium/cdm/design/ProjectParameter)
- Bounded context: [design](../design.md)
- Kind: Resource
- Is a: [core_Resource](core_Resource.md)
- HTML page: [classes/des_ProjectParameter/](../../classes/des_ProjectParameter/)

A name/value parameter defined at the level of a design project. It is either a Workspace-side (server-side) parameter, kept with the project in the Workspace and editable only there, or a design-side parameter, kept in the project file (e.g. *.PrjPcb) and editable in Altium Designer. Both kinds appear in the project options and can be used as special strings in design documents.

## In the product

- [Workspace Projects](https://www.altium.com/documentation/altium-365/workspace-projects#project_parameters) (primary)
- [Accessing, Defining & Managing Project Options](https://www.altium.com/documentation/altium-designer/accessing-defining-managing-project-options#parameters)

## In the API

- Platform API type: [`DesProjectParameter`](https://altiumdeveloper.github.io/platform-api-docs/types/objects/DesProjectParameter/) (object)

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| name | string | 1 |  |  |  |
| value | string | 0..1 |  |  |  |

## Referenced by

| From | Field | Cardinality | Relation |
| --- | --- | --- | --- |
| [des_Project](des_Project.md) | parameters | * |  |
