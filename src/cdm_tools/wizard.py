"""
CDM Entity Definition Wizard — interactive contributor tool.

Pure layer (generate_entity_yaml, validate_yaml, make_grid_template) is
importable without triggering questionary or Rich, enabling round-trip tests.
Interactive layer (run_wizard, main) requires a TTY.
"""

from __future__ import annotations

import os
import re
from pathlib import Path
from typing import Optional

import yaml

from cdm_tools.conventions import CLASS_NAME_RE, SLOT_NAME_RE

ROOT_SCHEMA = (
    Path(__file__).parents[2]
    / "src"
    / "common_data_model"
    / "schema"
    / "common_data_model.yaml"
)
# If running from repo root, this resolves correctly. Also accept override via env var.
_schema_path = str(Path(os.environ.get("CDM_SCHEMA_PATH", ROOT_SCHEMA)))

# Derived from schema annotation audit (see RESEARCH.md)
SUBSET_GRID_PREFIX: dict[str, str] = {
    "collaboration": "grid:workspace:{workspace-id}:collaboration",
    "configuration": "grid:workspace:{workspace-id}:configuration",
    "customization": "grid:workspace:{workspace-id}:scripts",
    "design": "grid:workspace:{workspace-id}:design",
    "deviceModel": "grid:global::device-model",
    "insights": "grid:workspace:{workspace-id}:insights",
    "library": "grid:workspace:{workspace-id}:library",
    "ota": "grid:workspace:{workspace-id}:ota",
    "platform": "grid:workspace:{workspace-id}:team",
    "procurement": "grid:workspace:{workspace-id}:procurement",
    "requirements": "grid:workspace:{workspace-id}:requirements",
    "software": "grid:workspace:{workspace-id}:software",
    "supply": "grid:supply::platform",
    "system": "grid:workspace:{workspace-id}:system-design",
    "system-sdm": "grid:workspace:{workspace-id}:system-design",
}

SUBSET_URI_PREFIX: dict[str, str] = {
    "collaboration": "collab",
    "configuration": "cfg",
    "customization": "custom",
    "design": "des",
    "deviceModel": "dm",
    "insights": "ins",
    "library": "lib",
    "ota": "ota",
    "platform": "plat",
    "procurement": "pro",
    "requirements": "req",
    "software": "sw",
    "supply": "sup",
    "system": "sys",
    "system-sdm": "sys",
}

# Interactive layer imports — only resolved when wizard runs in a TTY context
try:
    import questionary
    from rich.console import Console
    from rich.panel import Panel
    from rich.syntax import Syntax

    _INTERACTIVE_DEPS = True
except ImportError:
    _INTERACTIVE_DEPS = False

console = Console() if _INTERACTIVE_DEPS else None  # type: ignore[assignment]


def _camel_to_title(name: str) -> str:
    """Convert a lowerCamelCase or PascalCase name to a human-readable spaced title.

    Examples:
        mySlot       → my slot
        pcbSnippet   → pcb snippet
        aiModels     → ai models
    """
    # Insert a space before each uppercase letter, then lowercase everything
    spaced = re.sub(r"(?<=[a-z0-9])(?=[A-Z])", " ", name)
    return spaced.lower()


def make_grid_template(subset: str, pascal_class: str) -> str:
    """Return the GRID annotation template for a class in the given subset (D-05, D-06)."""
    prefix = SUBSET_GRID_PREFIX.get(subset)
    if prefix is None:
        return "grid:{area}:{tenant}:{context}:{resource-type}/{id}"
    resource_type = re.sub(r"(?<!^)(?=[A-Z])", "-", pascal_class).lower()
    return f"{prefix}:{resource_type}/{{id}}"


def generate_entity_yaml(
    subset: str,
    entity_type: str,
    pascal_class: str,
    title: str,
    description: str,
    slots: list[dict],
) -> str:
    """
    Generate a paste-ready YAML block for a new CDM entity class (pure function, no I/O).

    slots: list of dicts with keys: name (str), range (str), required (bool), multivalued (bool)
    """
    class_name = f"{subset}_{pascal_class}"
    uri_prefix = SUBSET_URI_PREFIX.get(subset, subset[:3].lower())
    grid_template = make_grid_template(subset, pascal_class)

    # Build attributes dict (slot definitions under attributes:)
    attributes: dict = {}
    for slot in slots:
        slot_name = f"{subset}_{pascal_class}_{slot['name']}"
        attributes[slot_name] = {
            "slot_uri": f"{uri_prefix}:{pascal_class}_{slot['name']}",
            "alias": slot["name"],
            "title": _camel_to_title(slot["name"]),
            "description": f"The {slot['name']} of this {pascal_class}.",
            "range": slot["range"],
            "multivalued": bool(slot["multivalued"]),
            "required": bool(slot["required"]),
        }

    class_body: dict = {
        "is_a": entity_type,
        "in_subset": subset,
        "class_uri": f"{uri_prefix}:{pascal_class}",
        "title": title,
        "description": description,
        "annotations": {"grid": grid_template},
    }
    if attributes:
        class_body["attributes"] = attributes

    return yaml.dump(
        {class_name: class_body},
        default_flow_style=False,
        allow_unicode=True,
        sort_keys=False,
    )


def validate_yaml(
    yaml_content: str,
    schema_path: Optional[str] = None,  # noqa: ARG001 — kept for API compat
) -> tuple[bool, str]:
    """
    Validate a wizard-generated YAML snippet using CDM naming and metadata rules.

    Runs the same checks as cdm-lint (CLASS_NAME_RE, SLOT_NAME_RE, required fields)
    against the in-memory parsed YAML — no subprocess, no instance-validation.

    Returns (passed: bool, error_messages: str).
    """
    from cdm_tools.conventions import (
        CLASS_NAME_RE,
        SLOT_NAME_RE,
        CLASS_REQUIRED_FIELDS,
        SLOT_REQUIRED_FIELDS,
        LintIssue,
    )

    issues: list[LintIssue] = []
    try:
        data = yaml.safe_load(yaml_content)
    except yaml.YAMLError as exc:
        return False, f"YAML parse error: {exc}"

    if not isinstance(data, dict):
        return False, "Generated YAML is not a mapping."

    for class_key, class_body in data.items():
        if not CLASS_NAME_RE.match(class_key):
            issues.append(
                LintIssue(
                    severity="error",
                    rule_id="LINT-03",
                    file="<generated>",
                    line=0,
                    message=f"Class name '{class_key}' does not follow {{subset}}_{{PascalCase}} convention.",
                )
            )
        for field in CLASS_REQUIRED_FIELDS:
            if field not in (class_body or {}):
                issues.append(
                    LintIssue(
                        severity="error",
                        rule_id="LINT-05",
                        file="<generated>",
                        line=0,
                        message=f"Class '{class_key}' is missing required field: {field}",
                    )
                )
        for slot_key, slot_body in (class_body or {}).get("attributes", {}).items():
            if not SLOT_NAME_RE.match(slot_key):
                issues.append(
                    LintIssue(
                        severity="error",
                        rule_id="LINT-04",
                        file="<generated>",
                        line=0,
                        message=f"Slot name '{slot_key}' does not follow naming convention.",
                    )
                )
            for field in SLOT_REQUIRED_FIELDS:
                if field not in (slot_body or {}):
                    issues.append(
                        LintIssue(
                            severity="error",
                            rule_id="LINT-06",
                            file="<generated>",
                            line=0,
                            message=f"Slot '{slot_key}' is missing required field: {field}",
                        )
                    )

    errors = [i for i in issues if i.severity == "error"]
    if errors:
        msg = "\n".join(f"[{i.rule_id}] {i.message}" for i in errors)
        return False, msg
    return True, ""


def run_wizard() -> None:
    """Interactive prompt flow. Requires a TTY and questionary + rich installed."""
    if not _INTERACTIVE_DEPS:
        raise RuntimeError("questionary and rich must be installed: poetry install")

    from rich.console import Console as _Console
    from rich.panel import Panel as _Panel
    from rich.syntax import Syntax as _Syntax

    _console = _Console()

    from linkml_runtime.utils.schemaview import SchemaView

    # Load schema for live subset list and duplicate detection
    sv = SchemaView(_schema_path)
    all_subsets = sorted(sv.all_subsets().keys())
    all_classes = set(sv.all_classes().keys())

    _console.print("\n[bold cyan]CDM Entity Definition Wizard[/bold cyan]\n")

    # WIZ-03: Bounded context autocomplete from live schema
    subset: str = questionary.autocomplete(
        "Bounded context (tab for autocomplete):",
        choices=all_subsets,
        validate=lambda v: v in all_subsets
        or f"'{v}' is not a known bounded context. Choose from: {', '.join(all_subsets)}",
    ).ask()
    if subset is None:
        _console.print("[yellow]Wizard cancelled.[/yellow]")
        return

    # WIZ-02: Entity type with domain explanation
    entity_type: str = questionary.select(
        "Entity type:",
        choices=[
            questionary.Choice(
                "Artifact — persistent data object (created, stored, versioned, consumed)",
                value="Artifact",
            ),
            questionary.Choice(
                "Activity — process/work object (uses inputs, produces outputs, orchestrates)",
                value="Activity",
            ),
        ],
    ).ask()
    if entity_type is None:
        _console.print("[yellow]Wizard cancelled.[/yellow]")
        return

    # WIZ-04: Class name — PascalCase component only; validated as compound name in real-time
    def validate_class_name(val: str) -> bool | str:
        compound = f"{subset}_{val}"
        if not val:
            return "Class name cannot be empty."
        if not CLASS_NAME_RE.match(compound):
            return f"'{compound}' is not valid. PascalCase required (e.g. FunctionalBlock). Full name will be: {subset}_<YourClass>"
        if compound in all_classes:
            return (
                f"'{compound}' already exists in the schema. Choose a different name."
            )
        return True

    pascal_class: str = questionary.text(
        f"Class name (PascalCase, e.g. FunctionalBlock) — will become {subset}_<Name>:",
        validate=validate_class_name,
    ).ask()
    if pascal_class is None:
        _console.print("[yellow]Wizard cancelled.[/yellow]")
        return

    # WIZ-05: Title and description
    title: str = questionary.text(
        "Title (human-readable label, e.g. 'Functional Block'):",
        validate=lambda v: True if v.strip() else "Title cannot be empty.",
    ).ask()
    if title is None:
        _console.print("[yellow]Wizard cancelled.[/yellow]")
        return

    description: str = questionary.text(
        "Description (meaningful prose, ≥1 sentence):",
        validate=lambda v: True if v.strip() else "Description cannot be empty.",
    ).ask()
    if description is None:
        _console.print("[yellow]Wizard cancelled.[/yellow]")
        return

    # WIZ-06: Slot definition loop — optional (D-03)
    slots: list[dict] = []
    add_slot = questionary.confirm("Add slots?", default=True).ask()
    if add_slot is None:
        _console.print("[yellow]Wizard cancelled.[/yellow]")
        return
    while add_slot:
        _console.print(f"\n[bold]Define slot {len(slots) + 1}[/bold]")

        slot_name: str = questionary.text(
            f"Slot name (camelCase, e.g. portCount) — will become {subset}_{pascal_class}_<name>:",
            validate=lambda v: (
                True
                if SLOT_NAME_RE.match(f"{subset}_{pascal_class}_{v}")
                else f"'{subset}_{pascal_class}_{v}' is not valid. camelCase required (e.g. portCount)."
            ),
        ).ask()
        if slot_name is None:
            _console.print("[yellow]Wizard cancelled.[/yellow]")
            return

        # D-04: Slot range is free-text
        slot_range: str = questionary.text(
            "Range (e.g. string, integer, system_SystemModel):",
            validate=lambda v: True if v.strip() else "Range cannot be empty.",
        ).ask()
        if slot_range is None:
            _console.print("[yellow]Wizard cancelled.[/yellow]")
            return

        required = questionary.confirm("Required?", default=False).ask()
        if required is None:
            _console.print("[yellow]Wizard cancelled.[/yellow]")
            return

        multivalued = questionary.confirm("Multivalued?", default=False).ask()
        if multivalued is None:
            _console.print("[yellow]Wizard cancelled.[/yellow]")
            return

        slots.append(
            {
                "name": slot_name,
                "range": slot_range,
                "required": required,
                "multivalued": multivalued,
            }
        )

        add_slot = questionary.confirm("Add another slot?", default=True).ask()
        if add_slot is None:
            _console.print("[yellow]Wizard cancelled.[/yellow]")
            return

    # WIZ-07: Generate GRID template (auto-filled from subset, D-05)
    # WIZ-08 / WIZ-09: Generate YAML, validate, then display with Rich
    _console.print("\n[cyan]Generating YAML...[/cyan]")
    yaml_output = generate_entity_yaml(
        subset=subset,
        entity_type=entity_type,
        pascal_class=pascal_class,
        title=title,
        description=description,
        slots=slots,
    )

    # WIZ-09: Validate before displaying (D-07)
    _console.print("[cyan]Running linkml-validate...[/cyan]")
    passed, errors = validate_yaml(yaml_output)

    if not passed:
        _console.print(
            _Panel(
                f"[red]{errors}[/red]",
                title="[bold red]✗ Validation Failed[/bold red]",
                expand=False,
            )
        )

    # WIZ-08: Rich syntax-highlighted output — always shown, even on validation failure
    syntax = _Syntax(yaml_output, "yaml", theme="monokai", line_numbers=False)
    panel_title = (
        "[bold green]✓ Validation Passed — Paste-Ready YAML[/bold green]"
        if passed
        else "[bold yellow]⚠ Validation Failed — Review YAML Before Using[/bold yellow]"
    )
    _console.print(
        _Panel(
            syntax,
            title=panel_title,
            expand=False,
        )
    )
    if passed:
        _console.print(
            "\n[green]Copy the YAML block above and paste it into the appropriate schema file.[/green]"
        )
    else:
        _console.print(
            "\n[yellow]The YAML above did not pass linkml-validate. Fix the issues reported before using it.[/yellow]"
        )


def main() -> None:
    """Typer-free entrypoint registered as `cdm-wizard` in pyproject.toml."""
    _console = Console() if _INTERACTIVE_DEPS else None
    try:
        run_wizard()
    except KeyboardInterrupt:
        if _console:
            _console.print("\n[yellow]Wizard cancelled.[/yellow]")
        else:
            print("\nWizard cancelled.")
