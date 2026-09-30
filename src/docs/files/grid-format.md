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

--8<-- "docs/_snippets/grid-catalogue.md"

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

--8<-- "docs/_snippets/prefixes.md"

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
