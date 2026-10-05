# Bounded context: design

Models design projects stored in a Workspace, including multi-board and harness projects, with their parameters, variants and releases, the manufacturing packages shared from releases, project templates with their revisions, and rule checks run against projects. It corresponds to Workspace projects in Altium 365 and Altium Designer, from project creation through to design release.

HTML page: [subsets/design/](../subsets/design/)

## In the product

- [Workspace Projects](https://www.altium.com/documentation/altium-365/workspace-projects) (primary)
- [Management of a Specific Project](https://www.altium.com/documentation/altium-365/management-specific-project)
- [Design Project Release](https://www.altium.com/documentation/altium-designer/preparing-for-manufacture/design-release)

## Classes

- [Hardware Project](classes/des_Project.md) (`des_Project`): A design project stored in a Workspace, normally under its built-in version control, such as a PCB project. · Activity · API DesProject · GRID `grid:workspace:{workspace-id}:design:project/{id}`
- [Hardware Project Release](classes/des_ProjectRelease.md) (`des_ProjectRelease`): Project Release captures an immutable snapshot of a PCB design project at a specific point in its lifecycle, packaging all design data, outputs, and metadata required for manufacturing, assembly, and downstream processes. · Activity · API DesRelease · GRID `grid:workspace:{workspace-id}:design:project-release/{id}`
- [Hardware Project Variant](classes/des_ProjectVariant.md) (`des_ProjectVariant`): A design variant of a project: a named variation of the same base design that is assembled with a different set of components. · Resource · API DesWipVariant
- [Harness Project](classes/des_HarnessProject.md) (`des_HarnessProject`): Harness Project defines the design of a cable and wiring harness as a standalone yet integrable artifact, capturing connectors, wires, splices, and pin-to-pin mappings required to implement electrical interconnects between boards and system elements. · Activity · API DesProject
- [Manufacturing Package](classes/des_ManufacturingPackage.md) (`des_ManufacturingPackage`): A read-only package that contains a subset of Project Release artifacts that is typically shared with an external party for the purposes of manufacturing the board (e.g. Manufacturing Package may contain fabrication/assembly files required by the factories, but not the sources of the project) · Artifact · GRID `grid:workspace:{workspace-id}:design:manufacturing-package/{id}`
- [Multiboard Project](classes/des_MultiboardProject.md) (`des_MultiboardProject`): Multiboard Project represents the coordinated design of multiple interconnected PCB projects assembled into a single system, capturing both their logical interconnects and physical arrangements. · Activity · API DesProject
- [Project Parameter](classes/des_ProjectParameter.md) (`des_ProjectParameter`): A name/value parameter defined at the level of a design project. · Resource · API DesProjectParameter
- [Project Template](classes/des_ProjectTemplate.md) (`des_ProjectTemplate`): A reusable starting point for new design projects that bundles the documents, files and project settings a team wants to apply again and again. · Artifact · API DesProjectTemplate · GRID `grid:workspace:{workspace-id}:design:project-template/{id}`
- [Project Template Revision](classes/des_ProjectTemplateRevision.md) (`des_ProjectTemplateRevision`): An immutable revision of a project template. · Artifact · API DesProjectTemplateRevision · GRID `grid:workspace:{workspace-id}:design:project-template-revision/{id}`
- [Rule Check](classes/des_RuleCheck.md) (`des_RuleCheck`): Rule check definitions that can be executed against a project to validate design integrity and compliance with specified constraints. · Artifact · API RuleCheck · GRID `grid:workspace:{workspace-id}:design:rule-check/{id}`
- [Rule Check Execution](classes/des_RuleCheckExecution.md) (`des_RuleCheckExecution`): Execution of a rule check against a project to validate design integrity and compliance with specified constraints. · Activity · API RuleCheckExecution · GRID `grid:workspace:{workspace-id}:design:rule-check-execution/{id}`
