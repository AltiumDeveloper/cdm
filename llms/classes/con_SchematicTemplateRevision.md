# Schematic Template Revision (con_SchematicTemplateRevision)

- Name: `con_SchematicTemplateRevision`
- IRI: `con:SchematicTemplateRevision` (https://w3id.org/altium/cdm/configuration/SchematicTemplateRevision)
- Bounded context: [configuration](../configuration.md)
- Kind: Artifact
- Is a: [core_Artifact](core_Artifact.md)
- HTML page: [classes/con_SchematicTemplateRevision/](../../classes/con_SchematicTemplateRevision/)

One revision of a Workspace schematic template Item, holding the template as saved at that point, e.g. from Altium Designer with Save to Server or uploaded from a *.SchDot file. Editing the template saves the result into the next revision, and environment configurations list template revisions, rather than the Item itself, as their configuration data.

## Comments

- TBD

## In the product

- [Creating a Schematic Template](https://www.altium.com/documentation/altium-designer/schematic/creating-templates#creating_workspace_schematic_template) (primary)

## GRID

None declared.

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| id | GRID | 1 | Globally unique identifier across the whole platform. |  | [core_Entity](core_Entity.md) |

## Referenced by

| From | Field | Cardinality | Relation |
| --- | --- | --- | --- |
| [con_EnvironmentConfiguration](con_EnvironmentConfiguration.md) | schematicTemplates | * | core_hasPart |
| [con_SchematicTemplate](con_SchematicTemplate.md) | revisions | * | core_revisions |
| [lib_ManagedSheetRevision](lib_ManagedSheetRevision.md) | template | 0..1 | core_derivedFrom |
