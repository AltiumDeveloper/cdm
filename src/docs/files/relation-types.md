# Relation Types

The `core` subset defines a small set of **abstract relation slots** — derivation, composition, input, output,
information flow and scope. Domain classes never use them directly. Every relation between domain classes is a
slot that specialises one of them with `is_a`, narrowing the domain and range to concrete classes. This keeps the
meaning of relations uniform across bounded contexts and gives the OWL export consistent super-properties,
inverses and transitivity.

## Core relations

The table is generated from `core.yaml` and is the reference for names, domains, ranges, inverses,
transitivity and mappings. It lists the abstract slots and the specialisations that `core.yaml` itself provides:
`core_implements` / `core_implementedBy` (under `core_informedBy` / `core_informs`), `core_revisionOf` /
`core_revisions` (under `core_derivedFrom` / `core_derivesInto`) and `core_releaseOf` / `core_releases` (under
`core_outputOf` / `core_hasOutput`).

--8<-- "docs/_snippets/relations.md"

Notes:

- Domains and ranges are stated in terms of the [base classes](entity-classification.md): derivation links
  Artifacts, input and output link an Activity and an Artifact, information flow links Activities, and
  composition links any Entities.
- Inverse pairs are declared once, on one side; the table shows the inverse on both. `core_occursIn` has no
  inverse.
- Only `core_partOf` and `core_hasPart` are transitive (`transitive: true`; `owl:TransitiveProperty` in the OWL
  export).

## Choosing the parent relation

1. **One Artifact is produced from, or superseded by, another** → `core_derivedFrom` / `core_derivesInto`;
   for versions of the same thing, `core_revisionOf` / `core_revisions`.
2. **Whole and part** → `core_hasPart` (whole to part) or `core_partOf` (part to whole).
3. **An Activity consumes an Artifact** → `core_hasInput` (from the Activity) or `core_inputOf` (from the
   Artifact).
4. **An Activity produces an Artifact** → `core_hasOutput` or `core_outputOf`; for releases,
   `core_releases` / `core_releaseOf`.
5. **One Activity uses knowledge from another** → `core_informedBy` / `core_informs`; when one implements a
   requirement or specification, `core_implements` / `core_implementedBy`.
6. **An Activity takes place within the context of an Artifact** → `core_occursIn`.

The domain and range of the domain slot should stay within those of its parent — for example, a specialisation
of `core_hasInput` goes from an Activity to an Artifact.

## Declaring a domain relation

A relation that belongs to one class is defined under that class's `attributes:` with the three-part name
`{prefix}_{ClassName}_{fieldName}`, its own `slot_uri`, `alias`, `title`, `description`, `range`,
`multivalued` and `required` (see `AGENTS.md` §4 in the repository). An example from the requirements schema:

```yaml
# excerpt from requirement.yaml
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
```

Here a requirements project (an Activity) has its specifications (Artifacts) as parts. Another example is
`sft_SoftwareProject_aiModels`, which specialises `core_hasInput`: a software project uses AI models as inputs.

Never attach an abstract core slot to a class:

```yaml
# Invalid: abstract core slot used directly
req_Project:
  slots:
    - core_hasPart
```

A domain slot may declare its inverse with `inverse:`; no domain relation in the current schema does, so the
inverse direction of a domain relation is not modelled. Do not add `transitive: true` to specialisations of
non-transitive relations. The OWL export declares only the two core composition properties transitive; domain
specialisations become sub-properties of them, and in OWL a sub-property of a transitive property is not
transitive itself.

## Ontological basis

The relations are aligned with the W3C provenance ontology [PROV-O](https://www.w3.org/TR/prov-o/) and with the
OBO [Relation Ontology](https://obofoundry.org/ontology/ro.html) (RO), which also defines the relations
*part of*, *has part* and *occurs in* (their identifiers use the `BFO_` prefix). The **Mappings** column above lists them; they are declared in `core.yaml`
and exported to OWL as `skos:closeMatch` and `skos:relatedMatch`. None is exact, because the CDM domains and
ranges are narrower than the upper-ontology terms:

- **PROV-O** terms are close matches: `prov:wasDerivedFrom`, `prov:used`, `prov:generated`,
  `prov:wasGeneratedBy` and `prov:wasInformedBy` relate PROV entities and activities in the same directions as the
  CDM relations. The inverses of `prov:wasDerivedFrom`, `prov:used` and `prov:wasInformedBy` are not terms of
  the PROV-O Recommendation (names suggested for them, such as `wasUsedBy`, appear only in a separate inverses
  module), so `core_derivesInto`, `core_inputOf` and `core_informs` have no PROV-O mapping.
- **RO has output / output of** are close matches: they only require the output to take part in the process and
  to be present at its end in a new state, which fits an Artifact produced by an Activity.
- **RO derives from / derives into** are related matches: RO defines them for material entities, where the new
  entity takes over the matter of the old one and the old one ceases to exist; CDM sources persist.
- **RO has input / input of** are related matches: RO requires a material input whose state changes during the
  process; CDM inputs are information that usually stays unchanged.
- **BFO part of / has part** are related matches: RO parthood requires compatible categories (an occurrent cannot
  have continuants as parts), while CDM composition also links Activities and Artifacts, as in
  `req_Project_specifications` above.
- **BFO occurs in** is a related match: its range is a material or immaterial entity that spatially contains the
  process, while the range of `core_occursIn` is an Artifact that gives the Activity its context.
