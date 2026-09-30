# AGENTS.md — CDM LLM-First Reference

> **Audience:** LLM coding agents, AI assistants, and new contributors.
> Read this file top-to-bottom before making any changes to CDM schema YAML files.
> Authoritative source for entity model, naming conventions, and prohibited actions.

---

## 1. Entity Hierarchy

### Abstract Base Classes

| Class | Parent | Role | Examples |
|-------|--------|------|---------|
| `core_Entity` | — | Identifiable, versioned, platform-accessible domain object | (abstract — never instantiated directly) |
| `core_Artifact` | `core_Entity` | **Persistent data object** — created, stored, versioned, consumed | `lib_Component`, `lib_ComponentRevision`, `system_SdmSystemModelVersion` |
| `core_Activity` | `core_Entity` | **Process / work object** — something that happens, uses inputs, produces outputs | `system_ESDDocument`, `des_Project`, `req_Project` |
| `core_Resource` | — | Lightweight object with platform API access; not an Entity; no GRID | `dm_PortConfiguration`, `pro_BomItem` |
| `core_Event` | — | Abstract base for domain events; no GRID, no versioning | `cus_ScriptExecutionCompleted` |

### Distinguishing Artifact vs Activity

| Question | If YES → | Example |
|----------|----------|---------|
| Is it stored and retrieved as a versioned document? | `Artifact` | `lib_Component` |
| Does it orchestrate inputs and produce outputs? | `Activity` | `system_ESDDocument` |
| Is it a snapshot / version of something? | `Artifact` | `system_SdmSystemModelVersion` |
| Is it a project or workspace-level container? | `Activity` | `des_Project` |
| Is it a lightweight value-object with no lifecycle? | `Resource` | `dm_PortConfiguration` |

### Mixin Annotations

All mixins extend `core_Meta` (abstract). The core mixins are applied via `instantiates:`, **not** via `is_a`.

| Mixin | Applied to | Provides |
|-------|-----------|---------|
| `core_WithGRID` | `core_Entity` | `grid:` annotation slot (type `GRID`, base: `str`) |
| `core_WithMaturity` | `core_Entity` | `maturity:` slot (enum: `EXPERIMENTAL`, `PRODUCTION`, `OBSOLETE`) |
| `core_WithPlatformAPI` | `core_Entity`, `core_Resource` | `platformAPI:` and `nexarAPI:` slots (string — API type names) |
| `core_WithVault` | not applied yet | `contentType:` slot (enum `VaultContentType`) |
| `core_WithVaultLink` | slot `lib_ComponentRevision_template` | vault link parent/child/type annotations |

### Full Class Hierarchy

```
linkml:Any
├── core_Any
├── core_Meta (abstract)
│   ├── core_WithGRID          — mixin: grid annotation
│   ├── core_WithMaturity      — mixin: maturity annotation
│   ├── core_WithPlatformAPI   — mixin: platformAPI / nexarAPI type names
│   ├── core_WithVault         — mixin: vault content type
│   └── core_WithVaultLink     — mixin: vault link parent/child
├── core_Resource (abstract)   — instantiates: core_WithPlatformAPI
├── core_Event (abstract)
└── core_Entity (abstract)     — instantiates: core_WithGRID, core_WithMaturity, core_WithPlatformAPI
    ├── core_Artifact (abstract)
    │   └── <domain Artifact subclasses, e.g. plt_LifecycleDefinition>
    └── core_Activity (abstract)
        └── <domain Activity subclasses, e.g. system_ESDDocument>
```

### Concrete YAML Snippets

**Artifact subclass:**

```yaml
plt_LifecycleDefinition:
  is_a: core_Artifact
  in_subset: platform
  class_uri: plt:LifecycleDefinition
  title: Lifecycle Definition
  description: >-
    Defines the set of states that an entity can transition through in its lifecycle.
  annotations:
    grid: grid:workspace:{workspace-id}:platform:lifecycle-definition/{id}
    platformAPI: DesLifeCycleDefinition
```

**Activity subclass:**

```yaml
system_ESDDocument:
  is_a: core_Activity
  in_subset: system
  class_uri: sys:ESDDocument
  title: ESD Document
  description: >-
    An Electronic System Design document that orchestrates functional blocks,
    requirements, and system model versions.
  annotations:
    platformAPI: SysEsdDocument
    grid: grid:workspace:{workspace-id}:system-design:esd/{id}
```

---

## 2. GRID Format

### Definition

`GRID` (Global Resource ID) is a CDM scalar type defined in `core.yaml`:

```yaml
types:
  GRID:
    uri: core:grid
    base: str
    description: >-
      Global Resource ID. Format grid:area:[tenant-id]:context:resource-type/resource-id, see
      https://www.altium.com/documentation/altium-developer-center/altium-365/key-concepts/grid
```

Every `Entity` carries a `core_id` slot of type `GRID`. The type is a plain string — no URN prefix at the LinkML level; the platform enforces the format.

### Annotation Template

Class-level `grid:` annotations document the **GRID template** for instances of that class:

```
grid: grid:workspace:{workspace-id}:system-design:esd/{id}
```

Format (official): `grid:area:[tenant-id]:context:resource-type/resource-id` — `area` is one of
`global`, `workspace`, `supply`, `community`, `manufacture`; resources without a tenant use `::`
(e.g. `grid:global::platform:user/{id}`). See the
[GRID key concept](https://www.altium.com/documentation/altium-developer-center/altium-365/key-concepts/grid).

The annotation is informational only (consumed by platform tooling). It does **not** affect LinkML validation.

Concept page: `docs/grid-format.md` (generated table of all class GRID templates: `docs/reference/grid-templates.md`).

### Instance URIs

No instance URI scheme is defined: nothing in the repository generates or uses URIs of the form
`https://w3id.org/altium/cdm/{namespace}/{uuid}`, and such URIs would share the class namespaces.
Whether one is intended is an open question (MODEL-FINDINGS.md MF-072). Entities are identified by their GRID.

### URI Patterns for Schema Elements

| Element | Pattern | Example |
|---------|---------|---------|
| Class | `prefix:ClassName` | `sys:ESDDocument` |
| Slot | `prefix:ClassName_fieldName` | `sys:ESDDocument_functionalBlocks` |
| Enum | `prefix:EnumName` | `sys:PortType` |

---

## 3. Relation Types

### Overview

`core.yaml` defines abstract relation slots that form the CDM relation-type framework.
These abstract slots are **never used directly** in domain classes. Domain-level relations
should be specialisations (`is_a:`) of one of these abstract slots (not all are yet). `core.yaml`
also provides a few ready-made specialisations (below), which domain classes may attach directly,
narrowing the range with `slot_usage`.

Concept page: `docs/relation-types.md` (generated relation table: `docs/reference/relations.md`).

### Base Relation Table

| Slot name | Alias | Domain → Range | Inverse | Transitive | Semantic |
|-----------|-------|----------------|---------|-----------|---------|
| `core_derivesInto` | `derivesInto` | Artifact → Artifact | `core_derivedFrom` | No | One artifact is produced from / superseded by another |
| `core_derivedFrom` | `derivedFrom` | Artifact → Artifact | `core_derivesInto` | No | Reverse of derivesInto |
| `core_partOf` | `partOf` | Entity → Entity | `core_hasPart` | **Yes** | Compositional containment (child→parent) |
| `core_hasPart` | `hasPart` | Entity → Entity | `core_partOf` | **Yes** | Compositional containment (parent→child) |
| `core_inputOf` | `inputOf` | Artifact → Activity | `core_hasInput` | No | Artifact is consumed by an Activity |
| `core_hasInput` | `hasInput` | Activity → Artifact | `core_inputOf` | No | Activity references its consumed Artifacts |
| `core_outputOf` | `outputOf` | Artifact → Activity | `core_hasOutput` | No | Artifact was produced by an Activity |
| `core_hasOutput` | `hasOutput` | Activity → Artifact | `core_outputOf` | No | Activity references its produced Artifacts |
| `core_informedBy` | `informedBy` | Activity → Activity | `core_informs` | No | Activity uses knowledge from another Activity |
| `core_informs` | `informs` | Activity → Activity | `core_informedBy` | No | Reverse of informedBy |
| `core_occursIn` | `occursIn` | Activity → Artifact | — | No | Activity is scoped within an Artifact context |

### Pre-built Specialisations in core.yaml

| Slot | is_a | Semantic |
|------|------|---------|
| `core_revisionOf` | `core_derivedFrom` | A versioned snapshot derived from a prior one |
| `core_revisions` | `core_derivesInto` | Inverse of revisionOf |
| `core_releaseOf` | `core_outputOf` | A release artifact produced by an Activity |
| `core_releases` | `core_hasOutput` | Inverse of releaseOf |
| `core_implements` | `core_informedBy` | Activity implements a requirement/spec Activity |
| `core_implementedBy` | `core_informs` | Inverse of implements |

### Rule: Always Specialise

```yaml
# ✅ VALID — class-specific slot under attributes:, is_a pointing to an abstract core slot
classes:
  req_Project:
    is_a: core_Activity
    attributes:
      req_Project_specifications:
        is_a: core_hasPart
        slot_uri: req:Project_specifications
        alias: specifications
        title: specifications
        description: Specifications authored or curated within this requirements project.
        range: req_RequirementSpecification
        multivalued: true
        required: true

# ❌ INVALID — using abstract core slot directly on a domain class
classes:
  req_Project:
    slots:
      - core_hasPart   # Never do this
```

---

## 4. Naming Conventions

### 4.1 Class Names

Pattern: `{subsetName}_{ClassName}`

- `subsetName`: camelCase (e.g., `system`, `deviceModel`, `design`)
- `ClassName`: PascalCase (e.g., `FunctionalBlock`, `ESDDocument`)

```yaml
# ✅ VALID
system_FunctionalBlock:
  class_uri: sys:FunctionalBlock
  in_subset: system

dm_Peripheral:
  class_uri: dm:Peripheral
  in_subset: deviceModel

# ❌ INVALID — wrong cases
System_functionalBlock:    # subset not camelCase, class not PascalCase
system_functional_block:   # class name is snake_case, not PascalCase
FunctionalBlock:           # missing subset prefix entirely
```

### 4.2 Slot Names

CDM uses two valid slot naming patterns, depending on where the slot is defined in the YAML.

#### Class-specific slots (defined under `attributes:` in a class)

Pattern: `{subsetName}_{ClassName}_{fieldName}`

- `subsetName`: camelCase (matches the owning subset)
- `ClassName`: PascalCase (matches the class that owns the slot)
- `fieldName`: camelCase

Use this pattern for slots that belong to exactly one class. Define them inline under `attributes:` in the class definition.

```yaml
# ✅ VALID — defined under attributes: in system_ESDDocument
system_ESDDocument_functionalBlocks:
  slot_uri: sys:ESDDocument_functionalBlocks
  alias: functionalBlocks

dm_Peripheral_ports:
  slot_uri: dm:Peripheral_ports
  alias: ports

# ❌ INVALID
system_esddocument_functional_blocks:  # class part not PascalCase, field snake_case
ESDDocument_functionalBlocks:          # missing subset prefix
system_functionalBlocks:               # missing class name component
```

#### Shared slots (defined in top-level `slots:` section)

Pattern: `{subsetName}_{slotName}`

- `subsetName`: camelCase (matches the bounded context that owns the slot)
- `slotName`: camelCase or underscore-separated words

Use this pattern for slots that are **reused by multiple classes** across the schema. Common cross-context slots like `core_id`, `core_name`, and `core_localId` belong here. Domain-shared slots like `pro_bom_issues` (used by `pro_Bom`, `pro_BomItem`, `pro_BomItemElement`) also use this pattern.

```yaml
# ✅ VALID — shared slots in top-level slots: section
core_id:
  slot_uri: core:id
  alias: id
  range: GRID

pro_bom_issues:
  slot_uri: pro:bom_issues
  alias: bomIssues
  range: pro_BomIssue
  multivalued: true
```

#### Migration rule

Slots defined in the top-level `slots:` section but used by only **one class** (or zero classes) are considered migration candidates. The linter (LINT-08) emits a warning for these. They should be moved to `attributes:` under their owning class and renamed to the three-part pattern.

> **Historical note:** Early CDM development placed many class-specific slots in the top-level `slots:` section. These are being migrated incrementally.

#### slot_uri format (CONV-01)

Every class-specific slot (defined under `attributes:` in a class) must have a `slot_uri`
following the pattern:

```
{prefix}:{ClassName}_{field}
```

- **Colon** separates the prefix from the class name (NOT an underscore)
- `prefix` is the schema's `default_prefix` (e.g. `lib`, `pro`, `sft`)
- `ClassName` is the PascalCase class name WITHOUT the subset prefix
- `field` is the lowerCamelCase field name (matches the `alias`)

| Correct | Wrong | Reason |
|---------|-------|--------|
| `pro:Bom_items` | `pro:bom_items` | ClassName must be PascalCase |
| `lib:ComponentRevision_symbols` | `lib_ComponentRevision_symbols` | Must use colon, not underscore |
| `sft:SoftwareProject_aiModels` | `sft:SoftwareProject_ai_models` | field must be lowerCamelCase |

`cdm-lint` enforces this as rule **CONV-01** — violations fail CI.

### 4.3 Required Class Metadata

Every concrete and abstract class in a domain YAML **must** have all four:

```yaml
# ✅ VALID
system_FunctionalBlock:
  class_uri: sys:FunctionalBlock          # required — URI for OWL/RDF
  title: Functional Block                  # required — human-readable label
  description: >-                          # required — meaningful prose
    A named functional unit within an ESD document, grouping ports
    and implementing a portion of the system design.
  in_subset: system                        # required — exactly one subset

# ❌ INVALID — missing metadata
system_FunctionalBlock:
  is_a: core_Artifact
  slots:
    - system_FunctionalBlock_name
  # class_uri missing → OWL generation will use fallback IRI
  # title missing    → doc pages have no human label
  # description missing → TBD entries block contributor usability
  # in_subset missing → linkml-lint FAIL
```

#### platformAPI annotation

`platformAPI` must name an **existing** Altium 365 Platform API type (e.g. `BomWip`, `DesProject`,
`GloOrganization`). Supply-chain types served by the Nexar (Octopart) API use `nexarAPI` instead
(e.g. `sup_Part` → `nexarAPI: SupPart`). Never invent a type name from naming patterns — check it against
production introspection. If the entity has no API type yet, **omit the annotation** (e.g. `dm_Processor`)
and add it once the API type exists. Several classes may share one API type (e.g. `pro_ManagedBOM` and
`pro_ConsolidatedBOM` → `BomWip`).

### 4.4 Required Slot Metadata

Every named slot **must** have all seven:

```yaml
# ✅ VALID
system_FunctionalBlock_ports:
  slot_uri: sys:FunctionalBlock_ports     # required
  alias: ports                             # required — camelCase Python attribute name
  title: ports                             # required — human label
  description: >-                          # required
    The list of ports exposed by this functional block.
  range: system_Port                       # required — target class or scalar type
  multivalued: true                        # required — boolean
  required: false                          # required — boolean

# ❌ INVALID — incomplete slot
system_FunctionalBlock_ports:
  range: system_Port
  multivalued: true
  # slot_uri missing → RDF export broken
  # alias missing    → Python datamodel has no usable attribute name
  # title/description missing → TBD entries in docs
  # required missing → LinkML defaults to false but intent is unclear
```

#### alias format (CONV-02)

`alias` must be **lowerCamelCase** — matching the `field` segment of the 3-part slot name.
It is the generated Python attribute name and JSON key.

- `lib_ComponentRevision_symbols` → `alias: symbols`
- `lib_ReuseBlockRevision_pcbSnippet` → `alias: pcbSnippet`
- `sft_SoftwareProject_aiModels` → `alias: aiModels`

`cdm-lint` enforces this as rule **CONV-02** — aliases containing underscores fail CI.

#### title format (CONV-02)

`title` must be a **human-readable string with spaces** — no underscores.
Use lowercase words separated by spaces.

- `pcbSnippet` → `title: pcb snippet`
- `aiModels` → `title: ai models`
- `usedByProjectVariant` → `title: used by project variant`

`cdm-lint` enforces this as rule **CONV-02** — titles containing underscores fail CI.

### 4.5 Subset Rules

| Rule | Detail |
|------|--------|
| Every class must have `in_subset` | Exactly **one** subset name |
| Slots do **not** use `in_subset` | Never add `in_subset` to a slot definition |
| Subset names are camelCase | `system`, `deviceModel`, `library`, `procurement` |
| Nested subsets use hyphens | `system-sdm` is a sub-subset of `system` |
| One YAML file per subset/module | `device_model.yaml`, `system.yaml`, `core.yaml` |
| Root schema imports everything | Always load via `common_data_model.yaml`, never per-file |

```yaml
# ✅ VALID subset assignment
system_SdmFunctionalBlock:
  in_subset: system-sdm   # nested subset — valid

# ❌ INVALID subset usage
system_FunctionalBlock_ports:
  in_subset: system       # NEVER add in_subset to a slot
```

---

## 5. Known Violations

### Violation Tracking: Two-Layer Design

CDM uses two complementary layers to track schema violations:

| Layer | File | Role | Updated by |
|-------|------|------|------------|
| Machine record | `cdm-lint.yaml` | Authoritative baseline — lists elements whose errors are downgraded to warnings (advisory warnings such as LINT-08, DOC-02 and DOC-05 are not baselined). The linter promotes violations from errors to warnings for anything in this file, preventing CI breakage on pre-existing issues. | `poetry run cdm-lint --baseline-out cdm-lint.yaml` (automated) |
| Editorial record | `VIOLATIONS.md` | Human-curated tracking for violations worth naming, describing, and prioritising. Not exhaustive — focuses on violations that require coordination (breaking renames, version bumps, consumer impact). | Maintainers manually, via PR |

Both layers must be kept in sync. When a violation is fixed, both files must be updated.

> **Definition of Fixed**
>
> A violation is only truly fixed when ALL of the following conditions are met:
>
> 1. **Source YAML no longer contains it** — the element in `src/common_data_model/schema/`
>    conforms to the naming/metadata convention.
> 2. **`cdm-lint.yaml` no longer lists it after baseline regeneration** — run
>    `poetry run cdm-lint --baseline-out cdm-lint.yaml` and verify the entry is absent. If it still appears, the
>    YAML fix is incomplete or incorrect.
> 3. **`VIOLATIONS.md` row is updated to `Fixed`** — update the Fix Status column and
>    note the PR/commit that resolved it.
>
> Updating only VIOLATIONS.md without satisfying conditions 1 and 2 is **not** a fix.

The following active naming/convention violations exist in the schema as of the last audit.
Full tracking details, fix status, and blockers are in **[VIOLATIONS.md](VIOLATIONS.md)**.

- **`system.yaml`** — class `system_SdmSystemModelVersion` has `class_uri: sys:SystemModelVersion`
  which is missing the `Sdm` segment; the correct URI would be `sys:SdmSystemModelVersion`.
- **`system.yaml`** — class `system_SdmSystemModel` has `class_uri: sys:SystemModel`, likewise missing
  the `Sdm` segment (`sys:SdmSystemModel`).

Do **not** silently fix violations. Open a PR, reference the VIOLATIONS.md row, and update fix status.

---

## 6. Prohibited AI-Agent Actions

1. **NEVER rename a class or slot without a version bump.**
   Class and slot names are part of the public API. Renaming breaks JSON Schema `$ref`s,
   Python datamodel attribute names, SHACL property paths, and downstream consumers.
   If a rename is required, cut a new release (versions are the `vX.Y.Z` git tags), add a changelog entry, and
   coordinate with schema consumers before merging.

2. **NEVER add a new prefix without formal subset approval.**
   Each prefix maps to an IRI namespace and a registered subset. Introducing an ad-hoc prefix
   (`foo:`, `tmp:`, etc.) pollutes the OWL ontology and breaks the IRI resolution table.
   New subsets require a schema RFC and update to `common_data_model.yaml` prefixes block.

3. **NEVER edit generated files — always edit source YAML and regenerate.**
   The following paths are **generated artifacts** and must never be hand-edited:
   `src/common_data_model/datamodel/`, `src/common_data_model/pydantic.py`,
   `project/jsonschema/`, `project/owl/`, `project/shacl/`, `project/graphql/`,
   `project/typescript/`, `project/java/`, `project/protobuf/`, `project/sqlschema/`.
   Always edit `src/common_data_model/schema/*.yaml` and run `make gen-project`.

4. **NEVER load schema per-file — always load via root `common_data_model.yaml`.**
   LinkML resolves imports transitively. Loading `system.yaml` or `device_model.yaml` directly
   skips shared imports (core.yaml, linkml:types) and produces incomplete schemas that fail
   validation or generate broken artifacts.

5. **NEVER deploy `R=301` htaccess redirects to unverified target URLs.**
   The CDM IRI resolution table (`.htaccess` redirects under `w3id.org/altium/cdm/`) must only
   point to verified, stable targets. A broken 301 redirect causes permanent IRI resolution
   failures for external ontology consumers with no easy rollback path.

6. **NEVER pin `linkml` above `~1.9.4` without verifying gen-doc slug algorithm compatibility.**
   The MkDocs documentation generation (`make gendoc`) relies on the slug algorithm used by
   `gen-doc`. Upstream `linkml` has changed slug generation in minor releases, causing broken
   anchor links throughout the published docs site. Verify slug output manually before upgrading.

---

## 7. Contributor Workflow

Follow these steps for any schema addition or modification:

1. **Edit source YAML** in `src/common_data_model/schema/`
   - Apply naming conventions from Section 4
   - Add all required class/slot metadata (Sections 4.3 and 4.4)
   - Set `in_subset` on every new class

2. **Run `make lint`**
   ```bash
   make lint
   ```
   Runs `linkml-lint` and `cdm-lint` against all schema files. Fix all errors and warnings before continuing.

3. **Run `make test-schema`**
   ```bash
   make test-schema
   ```
   Generates the project from the schema into `tmp/`, which fails if the schema is structurally invalid.

4. **Run `make gen-project`**
   ```bash
   make gen-project
   ```
   Regenerates all downstream artifacts: Python dataclasses, Pydantic models, JSON Schema,
   OWL/Turtle, SHACL, GraphQL, TypeScript, Java, Protobuf, SQL DDL, JSON-LD context, prefix map.
   Commit generated artifacts alongside schema changes.

5. **Add example YAML** to `src/data/examples/valid/`
   Provide at least one valid instance YAML for each new class. Optionally add an invalid
   instance to `src/data/examples/invalid/` to document constraint enforcement.

6. **Run `make test`**
   ```bash
   make test
   ```
   Runs pytest including `tests/test_flows.py` integration tests. Update golden JSON fixtures
   if CDM compilation output has legitimately changed.

7. **Open PR with CHANGELOG entry**
   - Use conventional commit format: `feat(subset):`, `fix(subset):`, `refactor(subset):`
   - Add an entry to `CHANGELOG.md` under the `[Unreleased]` section
   - Tag breaking changes (renames, removals) with `BREAKING:` in the commit message
   - Request review from at least one CDM schema maintainer

---

## 8. Documentation Hub Links

Every class can link three layers: product docs, API, and standards. Rules are enforced by `cdm-lint` (DOC-01…05).

| Field | Purpose | Rule |
|---|---|---|
| `see_also:` | Official product/documentation pages, most relevant first (first = primary). Read from the class itself, not inherited | Each URL (and `#fragment`) must be in `src/docs/links/registry.yaml` (DOC-01). An empty `#` fragment counts as an anchor and must be listed too |
| `structured_aliases:` | Product terms for the concept, with `predicate`, `contexts`, `source` URL | `source` must be in the registry (DOC-01) |
| `annotations.platformAPI` | Altium 365 Platform API GraphQL type. Read from the class itself, not inherited | Must exist in `src/docs/api/platform-schema.json` as OBJECT/INTERFACE/UNION (DOC-03) |
| `annotations.nexarAPI` | Nexar (Octopart) GraphQL type for supply entities. Read from the class itself, not inherited | Must exist in `src/docs/api/nexar-schema.json` as OBJECT/INTERFACE/UNION (DOC-03) |
| `exact_mappings` / `close_mappings` / `related_mappings` | External standards (SVD, PDSC, SysML v2, PROV-O, RO/BFO) | Full http(s) URL, or CURIE with prefix `prov:` / `obo:` (DOC-04); full URLs must also be in the registry (DOC-01), with `source: standard` |
| `annotations.productDocs: none` | Declares that no public product documentation exists (after checking) | Silences DOC-05 |

Severities: DOC-01 error, DOC-02 warning (registry entry not used by any class), DOC-03 error,
DOC-04 error, DOC-05 warning. Errors listed in `cdm-lint.yaml` (buckets `doc_link`, `api_type`,
`mapping_format`) are downgraded to warnings.

DOC-05 (missing product documentation and API type) applies only to concrete PRODUCTION classes
descending from `core_Entity`; an absent `maturity` annotation means PRODUCTION.

`cdm-lint` must be run from the repository root (so it finds `src/docs/links/registry.yaml` and
`src/docs/api/`), or with `--registry` / `--api-dir` pointing at them. It exits with code 2 if the
registry or API snapshot directory is missing.

Example (illustrative; the real `plt_LifecycleDefinition` does not define `structured_aliases`):

```yaml
plt_LifecycleDefinition:
  annotations:
    platformAPI: DesLifeCycleDefinition
  see_also:
    - https://www.altium.com/documentation/altium-designer/connected-workspace/defining-lifecycle-definitions
  structured_aliases:
    - literal_form: Lifecycle Definition
      predicate: EXACT_SYNONYM
      contexts: [altium-designer, altium-365]
      source: https://www.altium.com/documentation/altium-designer/connected-workspace/defining-lifecycle-definitions
```

Registry entries may give `anchor_labels` (fragment → label) so links to different sections of one page render with their own text.

**Adding a link:** (1) open the page and read it — only link pages that genuinely describe the concept;
(2) add a registry entry with the exact `<title>` text before `" | "` and any anchors you use;
(3) add the URL to `see_also`; (4) run `make verify-links` and `make lint`.
Never guess an API type name — look it up in the snapshot (`make refresh-api-snapshot` to update).
Semantic disagreements between the CDM and the docs go to `MODEL-FINDINGS.md`, not silently into the schema.

**Rendering.** Class pages show a *Hub panel* with three boxes.

- **In the product** — known-as terms (`structured_aliases`) and `see_also` links titled from the registry, the first
  marked primary. Empty states: "No product documentation linked yet." or, with `productDocs: none`,
  "No public product documentation exists for this concept."
- **In the API** — the Platform API type (linked to its API reference page), or the Nexar type for supply entities,
  linked to the Octopart API docs. Empty states: "No Platform API type.", "`X` is not in the Platform API snapshot.",
  "`X` is not in the Nexar API snapshot."
- **In standards** — `*_mappings`.

API links are emitted only for pages listed in `src/docs/api/platform-docs-pages.json`; if that file is absent, API
links are emitted unfiltered, and if the Platform snapshot is absent, the type name is shown without links.
`make refresh-api-snapshot` refreshes the snapshots and that list. The class index tables link API types from the same
data.

`make gendoc` also writes `hub.json` (via `cdm-hub-export`) into the site and copies `hub.schema.json` next to it, for
tools and AI agents. `hub.json` is checked against the schema in the test suite, not at export time. Each class entry has its title,
`class_uri`, subset, GRID template and the hub (product links and terms, Platform or Nexar API type, mappings). Abstract and mixin classes, `core_*` classes and `linkml:Any` are omitted.

**Hub pages.** `make gendoc` also runs `cdm-gen-reference`, which writes the relation, prefix, GRID-template and
class-hierarchy reference tables (`docs/reference/`, plus root-relative snippets in `docs/_snippets/` that the concept
pages include via `pymdownx.snippets` with `check_paths`), the **Glossary** (class titles and `structured_aliases`;
a term shared by several classes becomes a homonym note) and the **Coverage** dashboard (per bounded context, computed
from the schema, the API snapshots and `MODEL-FINDINGS.md`). Bounded-context pages show the subset's `see_also` links,
a coverage line and its GRID templates. Subset `see_also` and slot/subset mappings are checked by DOC-01/DOC-04.
Do not edit these generated pages by hand.
