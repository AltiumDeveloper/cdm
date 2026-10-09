# Environment Configuration (con_EnvironmentConfiguration)

- Name: `con_EnvironmentConfiguration`
- IRI: `con:EnvironmentConfiguration` (https://w3id.org/altium/cdm/configuration/EnvironmentConfiguration)
- Bounded context: [configuration](../configuration.md)
- Kind: Artifact
- Is a: [core_Artifact](core_Artifact.md)
- HTML page: [classes/con_EnvironmentConfiguration/](../../classes/con_EnvironmentConfiguration/)

A named set of configuration data items that the Workspace members it targets are allowed to use in Altium Designer. The items are revisions of Workspace Items of supported content types (e.g. schematic, BOM, project and Draftsman templates, output job files and layer stacks, plus at most one Altium Designer Preferences revision), and the same item can be used by several configurations. Administrators define configurations in the Workspace's Team Configuration Center (TC2) and assign them to Workspace groups, called roles there; when a group member signs in to the Workspace from Altium Designer, each controlled area of the design environment is restricted to the chosen configuration's items.

## Comments

- TBD

## In the product

- [Environment Configuration Management](https://www.altium.com/documentation/altium-365/environment-configuration-management) (primary)
- [Managing Environment Configurations](https://www.altium.com/documentation/altium-365/managing-environment-configurations)

## GRID

None declared.

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| schematicTemplates | [con_SchematicTemplateRevision](con_SchematicTemplateRevision.md) | * |  | core_hasPart |  |
| id | GRID | 1 | Globally unique identifier across the whole platform. |  | [core_Entity](core_Entity.md) |

## Referenced by

| From | Field | Cardinality | Relation |
| --- | --- | --- | --- |
| [plt_Workspace](plt_Workspace.md) | environmentConfigurations | * | core_hasPart |
