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
* [tests/](tests/) - Python tests

## Developer Documentation

To run commands you may use good old `make`.

Use the `make` command to generate project artefacts:
* `make help`: list all pre-defined tasks
* `make all`: make everything
* `make gen-project`: generates various artifacts under `project` folder
* `make testdoc`: runs a local documentation website

## Key Documents
- **AGENTS.md** — Rules for humans and automated agents modifying the schema  
- **src/common_data_model/schema** — Organized via LinkML subsets  
- **Generated Artifacts** — JSON Schema, SHACL, Pydantic models  

## How to Contribute
1. Follow all rules in `AGENTS.md`  
2. Add or update classes using required naming conventions  
3. Include recommended example instances  
4. Run validation and regenerate artifacts  
5. Submit PR using Conventional Commits  
6. Ensure linting passes  

## Automated Agents
Agents modifying schema must:
- Preserve structure and comments  
- Follow naming rules strictly  
- Run validation and regenerate artifacts  
- Propose diffs before changes  

## Credits

This project was made with
[linkml-project-cookiecutter](https://github.com/linkml/linkml-project-cookiecutter).
