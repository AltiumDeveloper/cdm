# Common Data Model

The Altium Common Data Model (CDM) describes the entities of the Altium platform — projects, components, BOMs,
tasks, users and many more — as a [LinkML](https://linkml.io/) schema. For each class it records what the entity
is, how it relates to other entities, how it is identified by a GRID (Global Resource ID) and, where one
exists, its type in the API. The Altium Developer Center page
[GRID](https://www.altium.com/documentation/altium-developer-center/altium-365/key-concepts/grid) names the CDM
as the authoritative reference for the GRIDs of platform entities.

## Bounded contexts

The classes are grouped into bounded contexts (LinkML subsets), such as design, library, procurement and
collaboration. Each context has its own page with its product documentation, where it has any, and its classes. The
[home page](index.md) lists every context with its classes and their API types.

## Entities

- **Entity** — an identifiable, versioned object with a GRID. Every entity is one of two kinds:
    - **Artifact** — a persistent data object that is created, stored, versioned and consumed, such as a
      component revision or a BOM release;
    - **Activity** — a process or work object that uses inputs and produces outputs, such as a project or a task.
- **Resource** — a lightweight object that is not an entity and has no GRID, usually part of an entity, such
  as a BOM line.
- **Event** — a record of something that happened, with no GRID.

See [Entity Classification](entity-classification.md).

## The API behind the model

- [Platform API GraphQL documentation](https://altiumdeveloper.github.io/platform-api-docs/) — the reference
  of the Platform API's types, queries and mutations. Class pages link their Platform API type here.
- [Altium 365 API](https://www.altium.com/documentation/altium-developer-center/altium-365/api) on the Altium
  Developer Center — the GraphQL API to Altium 365 Workspace data: how it is organised, its endpoints,
  authentication and tools for exploring the schema.
- [Octopart API](https://www.altium.com/documentation/altium-developer-center/octopart/api) on the Altium
  Developer Center — the GraphQL API for supply chain data, with its endpoint on `api.nexar.com`. Supply
  classes such as [Part](classes/sup_Part.md) name their Nexar type.

## How class pages link out

Each class page has a hub panel: **In the product** (links to the product documentation and the product terms
for the concept), **In the API** (the Platform API or Nexar type) and, where the class has mappings,
**In standards** (mappings to external standards and ontologies). The hub data of the domain classes is also
published for tools as [`hub.json`](hub.json), described by the JSON Schema [`hub.schema.json`](hub.schema.json).

The artifacts generated from the schema (JSON Schema, OWL, SHACL, GraphQL, Python and others) are not published
on this site; they are built from the [repository](https://github.com/AltiumDeveloper/cdm) with
`make gen-project`.

## For tools

AI assistants and other tools can start from [`llms.txt`](llms.txt) ([llmstxt.org](https://llmstxt.org/)): it
links a plain-markdown version of the concept pages and the glossary, a catalogue of each bounded context and a
card for every class and enumeration. [`llms-ctx.txt`](llms-ctx.txt) holds llms.txt, the pages and the
catalogues in one file, [`llms-full.txt`](llms-full.txt) also every card, and [`hub.json`](hub.json) the hub data
of the domain classes.

## Where to go next

- [Home page](index.md) — every bounded context and its classes.
- Concepts — [Domain Model](domain-model.md), [Entity Classification](entity-classification.md) and
  [Relation Types](relation-types.md).
- [GRIDs](grid-format.md) — the GRID format and the GRID templates declared by the classes.
- [Glossary](glossary.md) — product terms and class names.
