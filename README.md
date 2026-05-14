# common-data-model

Common Data Model

## Website

[https://altium.github.io/common-data-model](https://altium.github.io/common-data-model)

## Repository Structure

* [examples/](examples/) - example data
* [project/](project/) - project files (do not edit these)
* [src/](src/) - source files (edit these)
  * [common_data_model](src/common_data_model)
    * [schema](src/common_data_model/schema) -- LinkML schema
      (edit this)
    * [datamodel](src/common_data_model/datamodel) -- generated
      Python datamodel
  * [cdm_tools/](src/cdm_tools) -- contributor tooling (wizard, lint helpers)
* [tests/](tests/) - Python tests

## Developer Documentation

To run commands you may use good old `make`.

Use the `make` command to generate project artefacts:
* `make help`: list all pre-defined tasks
* `make all`: make everything
* `make gen-project`: generates various artifacts under `project` folder
* `make testdoc`: runs a local documentation website
* `make wizard`: launch the interactive Entity Definition Wizard (see below)

## Entity Definition Wizard

Adding a new class to CDM requires following strict naming conventions, supplying all
required metadata fields, and generating a correct GRID annotation — none of which is
obvious to a first-time contributor. The wizard removes this barrier by asking plain-
English questions and producing a paste-ready, lint-validated YAML block.

### Usage

```bash
make wizard
# or directly:
poetry run cdm-wizard
```

### What it does

1. **Asks which subset** the new entity belongs to (tab-autocomplete from the live schema).
2. **Asks the entity type** — `Artifact` (persistent data object) or `Activity` (process/work object) — with a plain-English explanation of each.
3. **Asks for a PascalCase class name** and validates it in real-time against the naming rules (`{subset}_{PascalCase}`). Duplicate detection runs against the live schema so you can't accidentally shadow an existing class.
4. **Asks for title and description** (both required by the schema conventions).
5. **Collects slot definitions** — name (camelCase), range, required flag, multivalued flag. You can add as many slots as needed.
6. **Auto-generates the GRID annotation template** for the subset.
7. **Runs built-in convention checks** on the generated YAML structure and naming to catch common schema issues before you paste it into the schema files.
8. **Displays the generated YAML** in a Rich-highlighted panel, along with the wizard's validation/check status.

### What you get

A complete, paste-ready YAML block:

```yaml
system_MyNewEntity:
  is_a: Artifact
  in_subset: system
  class_uri: sys:MyNewEntity
  title: My New Entity
  description: >-
    Meaningful description goes here.
  annotations:
    grid: grid:workspace:{workspace-id}:system-design:my-new-entity/{id}
  attributes:
    system_MyNewEntity_mySlot:
      slot_uri: sys:MyNewEntity_mySlot
      alias: mySlot
      title: my slot
      description: The mySlot of this MyNewEntity.
      range: string
      multivalued: false
      required: true
```

Paste this directly into the appropriate `src/common_data_model/schema/*.yaml` file,
then run `make lint` and `make gen-project` to regenerate artifacts.

### Requirements

`questionary` and `rich` are dev dependencies — install them with:

```bash
poetry install
```

## Key Documents
- **AGENTS.md** — Rules for humans and automated agents modifying the schema  
- **src/common_data_model/schema** — Organized via LinkML subsets  
- **Generated Artifacts** — JSON Schema, SHACL, Pydantic models  

## How to Contribute
1. Follow all rules in `AGENTS.md`  
2. **Use `make wizard`** to generate a correctly structured YAML block for any new entity  
3. Paste the generated YAML into the appropriate schema file  
4. Include recommended example instances  
5. Run `make lint` and `make gen-project` to validate and regenerate artifacts  
6. Submit PR using Conventional Commits  

## Automated Agents
Agents modifying schema must:
- Preserve structure and comments  
- Follow naming rules strictly  
- Run validation and regenerate artifacts  
- Propose diffs before changes  

## Credits

This project was made with
[linkml-project-cookiecutter](https://github.com/linkml/linkml-project-cookiecutter).
