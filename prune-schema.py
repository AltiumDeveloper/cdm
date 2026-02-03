import argparse
import json


def prune_schema(full_schema, target_type, target_title):
    defs = full_schema.get("$defs", {})
    if target_type not in defs:
        raise ValueError(f"Type '{target_type}' not found in $defs")

    referenced_names = {target_type}
    to_process = [defs[target_type]]

    # Step 1: Find all recursive references
    while to_process:
        current = to_process.pop()

        # We look for strings like "#/$defs/TypeName"
        if isinstance(current, dict):
            for key, value in current.items():
                if key == "$ref" and isinstance(value, str):
                    ref_name = value.split("/")[-1]
                    if ref_name in defs and ref_name not in referenced_names:
                        referenced_names.add(ref_name)
                        to_process.append(defs[ref_name])
                else:
                    to_process.append(value)
        elif isinstance(current, list):
            to_process.extend(current)

    # Step 2: Build the new pruned schema
    pruned_defs = {name: defs[name] for name in referenced_names}

    return {
        "$schema": full_schema.get(
            "$schema", "https://json-schema.org/draft/2020-12/schema"
        ),
        "title": target_title,
        "$ref": f"#/$defs/{target_type}",
        "$defs": pruned_defs,
    }

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Prune a JSON schema to a specific type and its dependencies.")
    parser.add_argument("input_file", help="Path to the input JSON schema file")
    parser.add_argument("output_file", help="Path to the output pruned JSON schema file")
    parser.add_argument("target_type", help="Type name to prune to (must exist in $defs)")
    parser.add_argument("target_title", help="Title for the pruned schema")
    args = parser.parse_args()

    with open(args.input_file) as f:
        schema = json.load(f)
    pruned = prune_schema(schema, args.target_type, args.target_title)
    with open(args.output_file, "w") as f:
        json.dump(pruned, f, indent=2)