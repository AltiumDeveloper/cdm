## Add your own custom Makefile targets here

DOCKERIMAGE=ontology-kit:latest
DOCKER=docker run --rm -v $(PWD):/workspace -w /workspace $(DOCKERIMAGE)
ONTOLOGY=${DEST}/owl/${SCHEMA_NAME}.owl.ttl
DIST=widoco-dist
DOCS=widoco-docs

# all: clean build verify serialize docs test

# clean:
#  @rm -rf $(DIST) $(DOCS); mkdir -p $(DIST)

widoco-docker:	
	docker build -t $(DOCKERIMAGE) tools/docker

# verify:
#  $(DOCKER) -lc "tools/scripts/reason_and_report.sh"

# serialize:
#  $(DOCKER) -lc "tools/scripts/build_serializations.sh"

widoco-docs:
	rm -rf $(DOCS)
	$(DOCKER) -lc "mkdir -p $(DOCS) && java -jar /opt/widoco.jar -ontFile $(ONTOLOGY) -outFolder $(DOCS) -rewriteAll -getOntologyMetadata -oops -webVowl"

# test: shacl sparql

# shacl:
#  $(DOCKER) tools/scripts/validate_shacl.sh

# sparql:
#  $(DOCKER) tools/scripts/run_sparql_tests.sh

###
### Full JSON output for downstream processing
###

gen-schema: 
	$(RUN) gen-linkml --useuris --metadata --format json --output google-sheet-schema.json --no-materialize-attributes $(SOURCE_SCHEMA_PATH)

###
### JSON schema generation
###

JSON_SCHEMA_DIR = $(DEST)/jsonschema
JSON_SCHEMA_PATH = $(JSON_SCHEMA_DIR)/$(SCHEMA_NAME).schema.json

.PHONY: gen-sdm-schema

$(DEST)/jsonschema:
	mkdir -p $@
	mkdir -p tmp

gen-sdm-schema:
	python3 prune-schema.py \
		"$(JSON_SCHEMA_PATH)" \
		"$(JSON_SCHEMA_DIR)/system_data_model.schema.json" \
		"SystemSdmSystemModelVersion" \
		"System Data Model"

gen-esd-schema:
	python3 prune-schema.py \
		"$(JSON_SCHEMA_PATH)" \
		"$(JSON_SCHEMA_DIR)/esd_compiled_model.schema.json" \
		"SystemESDDocument" \
		"ESD Compiled Model"

###
### CI targets
###

ci-generate: clean install gen-project gen-schema gen-sdm-schema gen-esd-schema
ci-test: lint test