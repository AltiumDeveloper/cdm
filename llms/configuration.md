# Bounded context: Configuration Management

Models environment configurations, which restrict the Altium Designer working environment of the Workspace members they target to approved configuration data, together with schematic templates and their revisions stored as Workspace Items. In Altium 365 this corresponds to environment configuration management through the Team Configuration Center.

HTML page: [subsets/configuration/](../subsets/configuration/)

## In the product

- [Environment Configuration Management](https://www.altium.com/documentation/altium-365/environment-configuration-management) (primary)

## Classes

- [Environment Configuration](classes/con_EnvironmentConfiguration.md) (`con_EnvironmentConfiguration`): A named set of configuration data items that the Workspace members it targets are allowed to use in Altium Designer. · Artifact
- [Schematic Template](classes/con_SchematicTemplate.md) (`con_SchematicTemplate`): A schematic template stored as a Workspace Item. · Artifact
- [Schematic Template Revision](classes/con_SchematicTemplateRevision.md) (`con_SchematicTemplateRevision`): One revision of a Workspace schematic template Item, holding the template as saved at that point, e.g. from Altium Designer with Save to Server or uploaded from a *.SchDot file. · Artifact
