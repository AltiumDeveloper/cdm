# Entity Classification

Every domain class of the CDM specialises one of a few abstract base classes defined in the `core` subset. The
choice decides whether instances have a platform-wide identity (a [GRID](grid-format.md)), which core
[relations](relation-types.md) the class can take part in — their domains and ranges are stated in terms of
these base classes — and how the class relates to external ontologies. The base set is deliberately minimal;
bounded contexts refine it with their own classes and mixins.

## Base classes

--8<-- "docs/_snippets/class-hierarchy.md"

### Entity

[`core_Entity`](classes/core_Entity.md) is the abstract root of identifiable, versioned, platform-accessible
domain objects. It is never used directly: every entity is either an Artifact or an Activity. It has the
identifier slot `core_id`, whose range is `GRID`, and it instantiates three core mixins, which allow these
class-level annotations:

- `grid` — the GRID template of the class (`core_WithGRID`);
- `maturity` — `EXPERIMENTAL`, `PRODUCTION` or `OBSOLETE` (`core_WithMaturity`); `cdm-lint` treats a class
  without the annotation as `PRODUCTION`;
- `platformAPI` / `nexarAPI` — the Altium 365 Platform API or Nexar GraphQL type of the class
  (`core_WithPlatformAPI`).

### Artifact

[`core_Artifact`](classes/core_Artifact.md): a persistent data object that is created, stored, versioned and
consumed. Artifacts are the things other work refers to or uses. Typical Artifacts in the schema:

- library items and their revisions — [lib_Component](classes/lib_Component.md),
  [lib_ComponentRevision](classes/lib_ComponentRevision.md), [lib_Footprint](classes/lib_Footprint.md);
- templates — [des_ProjectTemplate](classes/des_ProjectTemplate.md),
  [con_SchematicTemplate](classes/con_SchematicTemplate.md);
- snapshots and releases — [system_SdmSystemModelVersion](classes/system_SdmSystemModelVersion.md),
  [pro_BomRelease](classes/pro_BomRelease.md), [sft_SoftwareRelease](classes/sft_SoftwareRelease.md),
  [req_RequirementBaseline](classes/req_RequirementBaseline.md);
- produced outputs — [des_ManufacturingPackage](classes/des_ManufacturingPackage.md),
  [sft_BuildArtifact](classes/sft_BuildArtifact.md);
- platform and catalogue records — [plt_Workspace](classes/plt_Workspace.md), [plt_User](classes/plt_User.md),
  [sup_Part](classes/sup_Part.md), [sup_Offer](classes/sup_Offer.md).

### Activity

[`core_Activity`](classes/core_Activity.md): a process or work object — something that happens, uses inputs and
produces outputs. Typical Activities in the schema:

- projects and documents that organise ongoing work — [des_Project](classes/des_Project.md),
  [req_Project](classes/req_Project.md), [sft_SoftwareProject](classes/sft_SoftwareProject.md),
  [system_ESDDocument](classes/system_ESDDocument.md), [plt_Solution](classes/plt_Solution.md),
  [system_SdmSystemModel](classes/system_SdmSystemModel.md);
- the editable working state of a BOM — [pro_ManagedBOM](classes/pro_ManagedBOM.md) and
  [pro_ConsolidatedBOM](classes/pro_ConsolidatedBOM.md) (both through `pro_BomWIP`);
- work items and requests — [col_Task](classes/col_Task.md), [col_CommentThread](classes/col_CommentThread.md),
  [lib_PartRequest](classes/lib_PartRequest.md),
  [req_RequirementChangeRequest](classes/req_RequirementChangeRequest.md);
- process runs — [cus_Workflow](classes/cus_Workflow.md), [des_RuleCheckExecution](classes/des_RuleCheckExecution.md);
- insights — [ins_PartInsight](classes/ins_PartInsight.md).

### Resource

[`core_Resource`](classes/core_Resource.md) is **not** an Entity. A Resource is a lightweight object that
typically exists as part of an Entity: it has no GRID and no versioning lifecycle of its own, but it can have a
Platform API type (`core_Resource` instantiates `core_WithPlatformAPI`). Where a Resource needs an identifier it
usually has `core_localId`, which is unique only within its context (a few use a natural key, such as the name
of a pin). Examples: BOM lines
([pro_BomItem](classes/pro_BomItem.md)), parameters and variants
([des_ProjectParameter](classes/des_ProjectParameter.md), [des_ProjectVariant](classes/des_ProjectVariant.md)),
lifecycle stages and states ([plt_LifecycleState](classes/plt_LifecycleState.md)), comments
([col_Comment](classes/col_Comment.md)), the contents of a device model
([dm_Peripheral](classes/dm_Peripheral.md), [dm_PortConfiguration](classes/dm_PortConfiguration.md)), and the
models inside a system model version ([system_SdmFunctionalModel](classes/system_SdmFunctionalModel.md)).

### Event

[`core_Event`](classes/core_Event.md) is the abstract base for domain events: things that happened, with no GRID
and no versioning lifecycle. The schema currently has one event class,
[cus_ScriptExecutionCompleted](classes/cus_ScriptExecutionCompleted.md).

### Mixins

Mixins extend `core_Meta` and are never used as a parent with `is_a`.

- The **core mixins** are attached with `instantiates`: `core_WithGRID`, `core_WithMaturity` and
  `core_WithPlatformAPI` on `core_Entity`, `core_WithPlatformAPI` on `core_Resource`. `core_WithVaultLink` is
  attached to one slot (`lib_ComponentRevision_template`); `core_WithVault` is defined but not attached anywhere
  yet.
- **Domain mixins** add slots and are attached with `mixins`, for example `plt_HasLifecycle` (a lifecycle state,
  on revision and release classes), `plt_SolutionItem` (membership in a solution, on `des_Project`,
  `sft_SoftwareProject`, `system_ESDDocument` and `sft_AIModel`) and `pro_Bom` (on the BOM classes).

## How to classify a class

The schema applies these criteria, in this order:

| Question | If yes | Examples |
| --- | --- | --- |
| Is it a lightweight object held within another object, with no GRID of its own? | `core_Resource` | `pro_BomItem`, `dm_PortConfiguration` |
| Is it a record that something happened rather than a persistent object? | `core_Event` | `cus_ScriptExecutionCompleted` |
| Is it a project or document that organises ongoing work, or the editable working state of something? | `core_Activity` | `des_Project`, `system_ESDDocument`, `pro_ManagedBOM` |
| Is it a unit of work, a request or the run of a process? | `core_Activity` | `col_Task`, `lib_PartRequest`, `des_RuleCheckExecution` |
| Is it a stored item, revision, snapshot, release or produced output that other work uses? | `core_Artifact` | `lib_ComponentRevision`, `system_SdmSystemModelVersion`, `pro_BomRelease` |
| Is it a platform or catalogue record (user, Workspace, supply part)? | `core_Artifact` | `plt_User`, `plt_Workspace`, `sup_Part` |

A recurring pattern is a working Activity paired with Artifact snapshots of it:
`system_SdmSystemModel` → `system_SdmSystemModelVersion`, `pro_ManagedBOM` → `pro_BomRelease`,
`sft_SoftwareProject` → `sft_SoftwareRelease`, `plt_Solution` → `plt_SolutionRelease`. It is a pattern, not a
rule that splits design work from released data: [des_ProjectRelease](classes/des_ProjectRelease.md) is
described as an immutable snapshot yet is an Activity, and the run of a script
([cus_ScriptExecution](classes/cus_ScriptExecution.md)) is an Artifact while the run of a rule check is an
Activity. These cases are open questions in
[MODEL-FINDINGS.md](https://github.com/AltiumDeveloper/cdm/blob/main/MODEL-FINDINGS.md) (MF-007, MF-070,
MF-073).

## Ontological basis

The Artifact/Activity split is aligned with the entity/activity distinction of the W3C provenance ontology
[PROV-O](https://www.w3.org/TR/prov-o/) and the continuant/occurrent distinction of the Basic Formal Ontology
([BFO](https://bfo-ontology.github.io/)). The mappings are declared in `core.yaml` and exported to OWL as
`skos:closeMatch` and `skos:relatedMatch`:

- `core_Artifact` — close match [prov:Entity](https://www.w3.org/TR/prov-o/#Entity); related match
  [BFO_0000031](http://purl.obolibrary.org/obo/BFO_0000031) (generically dependent continuant).
- `core_Activity` — close match [prov:Activity](https://www.w3.org/TR/prov-o/#Activity); related match
  [BFO_0000015](http://purl.obolibrary.org/obo/BFO_0000015) (process).

None of them is an exact match:

- The CDM classes are narrower than the PROV-O classes: they are records on the platform. `prov:Entity` is also
  broader in another way — in PROV terms a persisted project, which the CDM models as an Activity, is an entity
  too.
- Artifacts are documents, models and data — information that can be copied from one carrier to another. That is
  closer to BFO's *generically dependent continuant* than to BFO *object* (a material entity), but the CDM does
  not commit to BFO categories, so the mapping is only a related match.
- BFO *process* is an occurrent that unfolds in time, and the BFO/RO parthood relations do not let an
  occurrent have continuants as parts.
  CDM Activities are persistent, versioned records with Artifact parts (for example `req_Project_specifications`
  links a requirements project to its specifications), so this is a related match as well.

`core_Entity`, `core_Resource` and `core_Event` have no mappings. The mappings of the core relations are listed
on [Relation Types](relation-types.md).
