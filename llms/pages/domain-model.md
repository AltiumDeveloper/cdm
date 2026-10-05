# Domain Model

The Altium Common Data Model (CDM) describes the data of the Altium platform as a
[LinkML](https://linkml.io/) schema. Its classes are grouped into **bounded contexts** (LinkML subsets), and each
schema file holds one context (`system.yaml` holds two); the root schema `common_data_model.yaml` imports them all. This
documentation and the generated artifacts (JSON Schema, OWL, SHACL, GraphQL, Python and others) are produced
from the root schema, and `cdm-lint` checks it against the naming and documentation conventions.

## Building blocks

- **Base classes.** Every domain class other than a mixin specialises an abstract base class from the `core` subset:
  `core_Artifact` or `core_Activity` (both entities with a GRID), `core_Resource` (a lightweight part of an
  entity) or `core_Event`. Mixins add annotations and slots. See [Entity Classification](entity-classification.md).
- **Relations.** Relations between domain classes should specialise abstract relations defined in `core`, such
  as *has part*, *has input* or *derived from*; 28 entity-valued slots do not yet. See
  [Relation Types](relation-types.md).
- **Identity.** Entities are identified on the platform by a GRID (Global Resource ID); each class can declare
  the GRID template of its instances. See [GRIDs](grid-format.md).
- **Names.** Class names carry a short context prefix and a PascalCase name (`lib_Component`, `des_Project`,
  `system_ESDDocument`); each class also has an IRI in its context's namespace (`lib:Component`). Class-specific
  slots add a camelCase field name (`req_Project_specifications`). The prefixes are listed on the
  [GRIDs](grid-format.md#grids-and-schema-iris) page.

## Bounded contexts

Each page below describes the context, links its product documentation where it has any, and lists its classes.

- [core](../core.md) — `core.yaml`
- [platform](../platform.md) — `platform.yaml`
- [configuration](../configuration.md) — `configuration.yaml`
- [collaboration](../collaboration.md) — `collaboration.yaml`
- [customization](../customization.md) — `customization.yaml`
- [design](../design.md) — `design.yaml`
- [deviceModel](../deviceModel.md) — `device_model.yaml`
- [insights](../insights.md) — `insights.yaml`
- [library](../library.md) — `library.yaml`
- [ota](../ota.md) — `ota.yaml`
- [procurement](../procurement.md) — `procurement.yaml`
- [supply](../supply.md) — `supply.yaml`
- [software](../software.md) — `software.yaml`
- [system](../system.md) and [system-sdm](../system-sdm.md) — both in `system.yaml`
- [requirements](../requirements.md) — `requirement.yaml`

## Finding your way

- [Glossary](glossary.md) — product terms and class names, including terms that mean different things in
  different contexts.
- [MODEL-FINDINGS.md](https://github.com/AltiumDeveloper/cdm/blob/main/MODEL-FINDINGS.md) — open questions where
  the model and the product documentation or standards disagree.
