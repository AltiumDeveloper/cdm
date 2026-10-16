import importlib.util
import os
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]

ROOT = """\
id: https://example.org/root/
name: root
prefixes: {linkml: https://w3id.org/linkml/, ex: https://example.org/root/}
default_prefix: ex
imports: [linkml:types, module]
subsets: {ex: {title: Example}}
classes:
  core_Entity: {abstract: true}
"""

MODULE = """\
id: https://example.org/module/
name: module
prefixes: {linkml: https://w3id.org/linkml/, ex: https://example.org/module/}
default_prefix: ex
classes:
  ex_First: {is_a: core_Entity, in_subset: [ex], title: First}
"""


def _hook():
    spec = importlib.util.spec_from_file_location("cdm_nav_hook", REPO / "src/docs/hooks/nav.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_sidebar_follows_changes_to_any_schema_module(tmp_path):
    hook = _hook()
    root, module = tmp_path / "root.yaml", tmp_path / "module.yaml"
    root.write_text(ROOT, encoding="utf-8")
    module.write_text(MODULE, encoding="utf-8")
    _, classes = hook._bounded_contexts(root)
    assert [name for name, _ in classes["ex"]] == ["ex_First"]

    # A class added to an imported module only (the root file is untouched), as with mkdocs serve
    module.write_text(MODULE + "  ex_Second: {is_a: core_Entity, in_subset: [ex], title: Second}\n", encoding="utf-8")
    stat = module.stat()
    os.utime(module, (stat.st_atime, stat.st_mtime + 10))
    _, classes = hook._bounded_contexts(root)
    assert [name for name, _ in classes["ex"]] == ["ex_First", "ex_Second"]
