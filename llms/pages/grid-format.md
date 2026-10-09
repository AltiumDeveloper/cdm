# GRIDs

A **GRID** (Global Resource ID) is the platform-wide identifier of an entity on the Altium platform, such as a
project, a component, a BOM or a task. The format is defined by the platform and documented on the
Altium Developer Center page [GRID](https://www.altium.com/documentation/altium-developer-center/altium-365/key-concepts/grid);
that page is the authority for the format. This page explains how the CDM uses GRIDs and lists the GRID template
the schema declares for each class, grouped by bounded context.

## Format

```text
grid:area:[tenant-id]:context:resource-type/resource-id
```

In short (see the [official page](https://www.altium.com/documentation/altium-developer-center/altium-365/key-concepts/grid)
for the full definition):

- The **context path** `area:[tenant-id]:context` uses `:` as separator; the **resource path**
  `resource-type/resource-id` uses `/` and is defined by the bounded context. Sub-resources extend the resource
  path (`resource-type/id/sub-type/sub-id`).
- `area` is one of `global`, `workspace`, `supply`, `community`, `manufacture`.
- `tenant-id` identifies the owning tenant (the Workspace GUID for Workspace resources). It is left empty for
  resources that no tenant owns, which gives a double colon (`::`).
- `context` names the bounded context, `resource-type` the kind of entity, and `resource-id` is the entity's
  **local identifier** — a GUID in some contexts, a number in others; it is not always a UUID.
- GRIDs are **case-sensitive**.

### Design principles

- **Brand- and product-agnostic** — area names follow OAuth scope areas and contain no product names, so GRIDs
  stay valid when products are renamed.
- **Readable** — the resource type is a human-readable name from the domain vocabulary, so a GRID shows what kind
  of entity it identifies and which context owns it.

### Why GRIDs exist

Most platform entities have a local ID — a GUID or a number — that is unique only where it was issued: two
projects in different Workspaces may share a GUID, and the ID of a supply part is meaningful only to the supply
system. A local ID alone therefore cannot identify an entity when services, events or integrations exchange references.
Some Platform API entities still expose opaque, base64-encoded node IDs from the underlying GraphQL framework;
these are being replaced by GRIDs step by step.

A GRID therefore provides:

1. **Uniqueness** — one stable identifier that is unique across the whole platform.
2. **Context in the identifier** — the GRID carries the area, tenant, bounded context and resource type next to
   the local ID, so the platform can locate the entity from the GRID alone. The Platform API gateway uses this
   to route a `node(id: …)` query to the right subgraph.

## Catalogue

The GRID template of every class that declares one, per bounded context. Templates are informational
and are declared per class in the `grid` annotation.

### Platform

Bounded context page: [Platform](../platform.md).

| Entity | GRID template |
| --- | --- |
| [Application](../classes/plt_Application.md) | `grid:global::platform:application/{id}` |
| [Event Subscription](../classes/plt_EventSubscription.md) | `grid:global::events:subscription/{id}` |
| [Lifecycle Definition](../classes/plt_LifecycleDefinition.md) | `grid:workspace:{workspace-id}:platform:lifecycle-definition/{id}` |
| [Revision Naming Scheme](../classes/plt_NamingScheme.md) | `grid:workspace:{workspace-id}:platform:revision-naming-scheme/{id}` |
| [Organization](../classes/plt_Organization.md) | `grid:global::platform:organization/{id}` |
| [Solution](../classes/plt_Solution.md) | `grid:workspace:{workspace-id}:platform:solution/{id}` |
| [Solution Release](../classes/plt_SolutionRelease.md) | `grid:workspace:{workspace-id}:platform:solution-release/{id}` |
| [User](../classes/plt_User.md) | `grid:global::platform:user/{id}` |
| [User Group](../classes/plt_UserGroup.md) | `grid:global::platform:group/{id}` |
| [Workspace](../classes/plt_Workspace.md) | `grid:global::platform:workspace/{id}` |
| [Workspace Group](../classes/plt_WorkspaceGroup.md) | `grid:workspace:{workspace-id}:team:group/{id}` |
| [Workspace User](../classes/plt_WorkspaceUser.md) | `grid:workspace:{workspace-id}:team:user/{id}` |

### Design

Bounded context page: [Design](../design.md).

| Entity | GRID template |
| --- | --- |
| [Manufacturing Package](../classes/des_ManufacturingPackage.md) | `grid:workspace:{workspace-id}:design:manufacturing-package/{id}` |
| [Hardware Project](../classes/des_Project.md) | `grid:workspace:{workspace-id}:design:project/{id}` |
| [Hardware Project Release](../classes/des_ProjectRelease.md) | `grid:workspace:{workspace-id}:design:project-release/{id}` |
| [Project Template](../classes/des_ProjectTemplate.md) | `grid:workspace:{workspace-id}:design:project-template/{id}` |
| [Project Template Revision](../classes/des_ProjectTemplateRevision.md) | `grid:workspace:{workspace-id}:design:project-template-revision/{id}` |
| [Rule Check](../classes/des_RuleCheck.md) | `grid:workspace:{workspace-id}:design:rule-check/{id}` |
| [Rule Check Execution](../classes/des_RuleCheckExecution.md) | `grid:workspace:{workspace-id}:design:rule-check-execution/{id}` |

### Insights

Bounded context page: [Insights](../insights.md).

| Entity | GRID template |
| --- | --- |
| [Part Insight](../classes/ins_PartInsight.md) | `grid:workspace:{workspace-id}:insights:insight/{id}` |

### Library Management

Bounded context page: [Library Management](../library.md).

| Entity | GRID template |
| --- | --- |
| [Component](../classes/lib_Component.md) | `grid:workspace:{workspace-id}:library:component/{id}` |
| [Component Revision](../classes/lib_ComponentRevision.md) | `grid:workspace:{workspace-id}:library:component-revision/{id}` |
| [Component Template](../classes/lib_ComponentTemplate.md) | `grid:workspace:{workspace-id}:library:component-template/{id}` |
| [Component Template Revision](../classes/lib_ComponentTemplateRevision.md) | `grid:workspace:{workspace-id}:library:component-template-revision/{id}` |
| [Datasheet](../classes/lib_Datasheet.md) | `grid:workspace:{workspace-id}:library:datasheet/{id}` |
| [Footprint](../classes/lib_Footprint.md) | `grid:workspace:{workspace-id}:library:footprint/{id}` |
| [Footprint Revision](../classes/lib_FootprintRevision.md) | `grid:workspace:{workspace-id}:library:footprint-revision/{id}` |
| [Managed Sheet](../classes/lib_ManagedSheet.md) | `grid:workspace:{workspace-id}:library:managed-sheet/{id}` |
| [Managed Sheet Revision](../classes/lib_ManagedSheetRevision.md) | `grid:workspace:{workspace-id}:library:managed-sheet-revision/{id}` |
| [Part](../classes/lib_Part.md) | `grid:workspace:{workspace-id}:library:part/{id}` |
| [Part Request](../classes/lib_PartRequest.md) | `grid:workspace:{workspace-id}:library:part-request/{id}` |
| [Reuse Block](../classes/lib_ReuseBlock.md) | `grid:workspace:{workspace-id}:library:reuse-block/{id}` |
| [Reuse Block Revision](../classes/lib_ReuseBlockRevision.md) | `grid:workspace:{workspace-id}:library:reuse-block-revision/{id}` |
| [Symbol](../classes/lib_Symbol.md) | `grid:workspace:{workspace-id}:library:symbol/{id}` |
| [Symbol Revision](../classes/lib_SymbolRevision.md) | `grid:workspace:{workspace-id}:library:symbol-revision/{id}` |

### Collaboration

Bounded context page: [Collaboration](../collaboration.md).

| Entity | GRID template |
| --- | --- |
| [Comment Thread](../classes/col_CommentThread.md) | `grid:workspace:{workspace-id}:collaboration:comment-thread/{id}` |
| [Task](../classes/col_Task.md) | `grid:workspace:{workspace-id}:collaboration:task/{id}` |

### Procurement

Bounded context page: [Procurement](../procurement.md).

| Entity | GRID template |
| --- | --- |
| [BOM Release](../classes/pro_BomRelease.md) | `grid:workspace:{workspace-id}:procurement:bom-release/{id}` |
| [Consolidated BOM](../classes/pro_ConsolidatedBOM.md) | `grid:workspace:{workspace-id}:procurement:bom/{id}` |
| [Global BOM](../classes/pro_GlobalBOM.md) | `grid:global::procurement:bom/{id}` |
| [Managed BOM](../classes/pro_ManagedBOM.md) | `grid:workspace:{workspace-id}:procurement:bom/{id}` |

### Supply

Bounded context page: [Supply](../supply.md).

| Entity | GRID template |
| --- | --- |
| [Company](../classes/sup_Company.md) | `grid:supply::platform:company/{id}` |
| [Evaluation Kit](../classes/sup_EvalKit.md) | `grid:supply::platform:eval-kit/{id}` |
| [Offer](../classes/sup_Offer.md) | `grid:supply::platform:part/{id}/offer/{offerID}` |
| [Part](../classes/sup_Part.md) | `grid:supply::platform:part/{id}` |
| [Part Family](../classes/sup_PartFamily.md) | `grid:supply::platform:part-family/{id}` |
| [Part Group](../classes/sup_PartGroup.md) | `grid:supply::platform:part-group/{id}` |
| [Reference Design](../classes/sup_ReferenceDesign.md) | `grid:supply::platform:ref-design/{id}` |
| [Software Project](../classes/sup_SoftwareProject.md) | `grid:supply::platform:software-project/{id}` |
| [Solution Template](../classes/sup_SolutionTemplate.md) | `grid:supply::platform:solution-template/{id}` |

### Customization

Bounded context page: [Customization](../customization.md).

| Entity | GRID template |
| --- | --- |
| [Script](../classes/cus_Script.md) | `grid:workspace:{workspace-id}:scripts:script/{id}` |
| [Script Execution](../classes/cus_ScriptExecution.md) | `grid:workspace:{workspace-id}:scripts:script-execution/{id}` |
| [Script Version](../classes/cus_ScriptVersion.md) | `grid:workspace:{workspace-id}:scripts:script-version/{id}` |
| [Workflow](../classes/cus_Workflow.md) | `grid:workspace:{workspace-id}:customization:workflow/{id}` |

### System Design

Bounded context page: [System Design](../system.md).

| Entity | GRID template |
| --- | --- |
| [ESD Document](../classes/system_ESDDocument.md) | `grid:workspace:{workspace-id}:system-design:esd/{id}` |

### System Design - System Data Model

Bounded context page: [System Design - System Data Model](../system-sdm.md).

| Entity | GRID template |
| --- | --- |
| [System Model](../classes/system_SdmSystemModel.md) | `grid:workspace:{workspace-id}:system-design:sdm/{id}` |
| [System Model Version](../classes/system_SdmSystemModelVersion.md) | `grid:workspace:{workspace-id}:system-design:sdm-version/{id}` |

### Requirements

Bounded context page: [Requirements](../requirements.md).

| Entity | GRID template |
| --- | --- |
| [Requirements Project](../classes/req_Project.md) | `grid:workspace:{workspace-id}:requirements:project/{id}` |
| [Requirement](../classes/req_Requirement.md) | `grid:workspace:{workspace-id}:requirements:requirement/{id}` |
| [Requirement Baseline](../classes/req_RequirementBaseline.md) | `grid:workspace:{workspace-id}:requirements:baseline/{id}` |
| [Requirement Change Request](../classes/req_RequirementChangeRequest.md) | `grid:workspace:{workspace-id}:requirements:change-request/{id}` |
| [Requirement Revision](../classes/req_RequirementRevision.md) | `grid:workspace:{workspace-id}:requirements:requirement-revision/{id}` |
| [Requirement Specification](../classes/req_RequirementSpecification.md) | `grid:workspace:{workspace-id}:requirements:specification/{id}` |
| [Verification Case](../classes/req_VerificationCase.md) | `grid:workspace:{workspace-id}:requirements:verification-case/{id}` |

### Device Model

Bounded context page: [Device Model](../deviceModel.md).

| Entity | GRID template |
| --- | --- |
| [FullStackDeviceModel](../classes/dm_FullStackDeviceModel.md) | `grid:global::device-model:fullstack-dm/{id}` |

### Software

Bounded context page: [Software](../software.md).

| Entity | GRID template |
| --- | --- |
| [AI Model](../classes/sft_AIModel.md) | `grid:workspace:{workspace-id}:software:ai-model/{id}` |
| [Device Configuration](../classes/sft_DeviceConfiguration.md) | `grid:workspace:{workspace-id}:software:device-configuration/{id}` |
| [Device Configuration Revision](../classes/sft_DeviceConfigurationRevision.md) | `grid:workspace:{workspace-id}:software:device-configuration-revision/{id}` |
| [Software Project](../classes/sft_SoftwareProject.md) | `grid:workspace:{workspace-id}:software:software-project/{id}` |
| [Software Release](../classes/sft_SoftwareRelease.md) | `grid:workspace:{workspace-id}:software:software-release/{id}` |

### Over-the-Air Updates

Bounded context page: [Over-the-Air Updates](../ota.md).

| Entity | GRID template |
| --- | --- |
| [Device](../classes/ota_Device.md) | `grid:workspace:{workspace-id}:ota:device/{id}` |
| [Fleet](../classes/ota_Fleet.md) | `grid:workspace:{workspace-id}:ota:fleet/{id}` |
| [Package](../classes/ota_Package.md) | `grid:workspace:{workspace-id}:ota:package/{id}` |

## The GRID context is not the CDM subset

The `context` segment is the platform's bounded-context name, which often but not always equals the CDM subset.
For example, the system classes use `system-design`, the full-stack device model uses `device-model`, supply
records use context `platform` in area `supply`, scripts use `scripts`, Workspace users and groups use `team`,
and event subscriptions use `events`. The catalogue above is grouped by bounded context; the GRID context of a
class is the `context` segment of its template.

## GRIDs in the schema

- `GRID` is a scalar type in `core.yaml` with base `str`. LinkML does not validate the content of a GRID string;
  the platform defines and enforces the format.
- Every class under `core_Entity` inherits the identifier slot `core_id` (alias `id`), whose range is `GRID`.
  Resources (`core_Resource`) have no GRID; some of them (27 of 63 concrete Resources) have `core_localId`,
  an identifier that is unique only within its context. See [Entity Classification](entity-classification.md).
- A class documents the GRID of its instances with a `grid` annotation — a **template** with placeholders:
  `{workspace-id}` for the tenant, `{id}` for the local ID, and a named placeholder for a sub-resource ID
  (`{offerID}` in `sup_Offer`). The annotation is informational: it is shown in the documentation and consumed
  by tooling, and it does not affect LinkML validation. `cdm-lint` checks that it has the shape of a GRID
  (rule LINT-07).

```yaml
system_ESDDocument:
  is_a: core_Activity
  in_subset: system
  class_uri: sys:ESDDocument
  annotations:
    grid: grid:workspace:{workspace-id}:system-design:esd/{id}
    platformAPI: SysEsdDocument
```

Not every entity class has a template yet; the catalogue lists those that do.

## GRIDs and schema IRIs

A GRID identifies an **instance** on the platform. Classes, slots and enums of the schema are identified by
**IRIs**, declared with `class_uri`, `slot_uri` and `enum_uri`:

| Element | Pattern | Example |
| --- | --- | --- |
| Class | `prefix:ClassName` | `sys:ESDDocument` |
| Class-specific slot | `prefix:ClassName_fieldName` | `sys:ESDDocument_functionalBlocks` |
| Enum | `prefix:EnumName` | `sys:PortType` |

Each prefix expands to a namespace declared by the schema files:

Every prefix declared by the schema files, with the bounded context that owns the namespace where it has the form `https://w3id.org/altium/cdm/<subset>/`.

| Prefix | Namespace | Bounded context |
| --- | --- | --- |
| `cdm` | `https://w3id.org/altium/cdm/` |  |
| `col` | `https://w3id.org/altium/cdm/collaboration/` | [Collaboration](../collaboration.md) |
| `con` | `https://w3id.org/altium/cdm/configuration/` | [Configuration Management](../configuration.md) |
| `core` | `https://w3id.org/altium/cdm/core/` | [Core](../core.md) |
| `cus` | `https://w3id.org/altium/cdm/customization/` | [Customization](../customization.md) |
| `des` | `https://w3id.org/altium/cdm/design/` | [Design](../design.md) |
| `dm` | `https://w3id.org/altium/cdm/deviceModel/` | [Device Model](../deviceModel.md) |
| `ins` | `https://w3id.org/altium/cdm/insights/` | [Insights](../insights.md) |
| `lib` | `https://w3id.org/altium/cdm/library/` | [Library Management](../library.md) |
| `linkml` | `https://w3id.org/linkml/` |  |
| `obo` | `http://purl.obolibrary.org/obo/` |  |
| `ota` | `https://w3id.org/altium/cdm/ota/` | [Over-the-Air Updates](../ota.md) |
| `plt` | `https://w3id.org/altium/cdm/platform/` | [Platform](../platform.md) |
| `pro` | `https://w3id.org/altium/cdm/procurement/` | [Procurement](../procurement.md) |
| `prov` | `http://www.w3.org/ns/prov#` |  |
| `req` | `https://w3id.org/altium/cdm/requirement/` | [Requirements](../requirements.md) |
| `schema` | `http://schema.org/` |  |
| `sft` | `https://w3id.org/altium/cdm/software/` | [Software](../software.md) |
| `shex` | `http://www.w3.org/ns/shex#` |  |
| `sup` | `https://w3id.org/altium/cdm/supply/` | [Supply](../supply.md) |
| `sys` | `https://w3id.org/altium/cdm/system/` | [System Design](../system.md) |
| `xsd` | `http://www.w3.org/2001/XMLSchema#` |  |

A new subset prefix needs formal approval of the subset it belongs to (see `AGENTS.md` §6 in the repository). External vocabulary prefixes allow-listed for mappings (`prov:`, `obo:`) are exempt.

### Resolving IRIs through w3id.org

IRIs under `https://w3id.org/altium/cdm/` are redirected by the [w3id.org](https://w3id.org/) persistent
identifier service to this documentation site; the redirects are currently temporary (HTTP 302). Not every
class IRI resolves yet (MF-076): IRIs in the `system` namespace, such as
`https://w3id.org/altium/cdm/system/ESDDocument`, redirect to `classes/sys_<Class>/`, which does not exist (the
pages are `classes/system_<Class>/`), and IRIs in the `requirement` namespace (for example
`https://w3id.org/altium/cdm/requirement/Requirement`) get a 404 from w3id.org, which redirects only the
`requirements/` path. Rules for changing the redirects:

- Keep redirects temporary (`R=302`) until the target URL is confirmed correct and stable.
- Never deploy a permanent redirect (`R=301`) to an unverified target: browsers and ontology tools cache
  permanent redirects, and there is no easy way to roll them back.
- Switch to `R=301` only after the target has been confirmed, tested and merged in the w3id.org repository.
