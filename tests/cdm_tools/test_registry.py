import pytest

from cdm_tools.registry import (
    LinkEntry,
    RegistryError,
    dump_registry,
    load_registry,
    lookup,
    split_url,
)

SAMPLE = """\
https://www.altium.com/documentation/altium-365/lifecycle-management:
  title: Lifecycle Management
  source: altium-docs
  product: altium-365
  anchors: [states]
  last_verified: 2026-09-29
https://open-cmsis-pack.github.io/svd-spec/main/elem_registers.html:
  title: "Open-CMSIS-SVD: /device/peripherals/peripheral/registers element"
  label: CMSIS-SVD registers element
  source: standard
"""


def _write(tmp_path, text):
    p = tmp_path / "registry.yaml"
    p.write_text(text, encoding="utf-8")
    return p


def test_load_registry_parses_entries(tmp_path):
    reg = load_registry(_write(tmp_path, SAMPLE))
    e = reg["https://www.altium.com/documentation/altium-365/lifecycle-management"]
    assert e.title == "Lifecycle Management"
    assert e.source == "altium-docs"
    assert e.product == "altium-365"
    assert e.anchors == ["states"]
    assert e.last_verified == "2026-09-29"
    svd = reg["https://open-cmsis-pack.github.io/svd-spec/main/elem_registers.html"]
    assert svd.label == "CMSIS-SVD registers element"
    assert svd.anchors == []


def test_missing_title_is_rejected(tmp_path):
    with pytest.raises(RegistryError, match="title"):
        load_registry(_write(tmp_path, "https://x.example/:\n  source: standard\n"))


def test_unknown_source_is_rejected(tmp_path):
    with pytest.raises(RegistryError, match="source"):
        load_registry(_write(tmp_path, "https://x.example/:\n  title: X\n  source: blog\n"))


def test_fragment_key_is_rejected(tmp_path):
    with pytest.raises(RegistryError, match="fragment"):
        load_registry(_write(tmp_path, "https://x.example/#a:\n  title: X\n  source: standard\n"))


def test_split_url():
    assert split_url("https://a.example/p#frag") == ("https://a.example/p", "frag")
    assert split_url("https://a.example/p") == ("https://a.example/p", None)


def test_lookup_requires_listed_anchor(tmp_path):
    reg = load_registry(_write(tmp_path, SAMPLE))
    base = "https://www.altium.com/documentation/altium-365/lifecycle-management"
    assert lookup(reg, base).title == "Lifecycle Management"
    assert lookup(reg, base + "#states").title == "Lifecycle Management"
    assert lookup(reg, base + "#nope") is None
    assert lookup(reg, "https://unknown.example/") is None


def test_dump_round_trips(tmp_path):
    reg = load_registry(_write(tmp_path, SAMPLE))
    out = tmp_path / "out.yaml"
    dump_registry(reg, out)
    assert load_registry(out) == reg
    assert out.read_text(encoding="utf-8").startswith("# CDM documentation link registry")


def test_lookup_empty_fragment_does_not_match(tmp_path):
    reg = load_registry(_write(tmp_path, SAMPLE))
    base = "https://www.altium.com/documentation/altium-365/lifecycle-management"
    assert lookup(reg, base + "#") is None


def test_scalar_anchors_are_rejected(tmp_path):
    with pytest.raises(RegistryError, match="anchors"):
        load_registry(_write(tmp_path, "https://x.example/:\n  title: X\n  source: standard\n  anchors: states\n"))


def test_non_string_source_is_rejected(tmp_path):
    with pytest.raises(RegistryError, match="source"):
        load_registry(_write(tmp_path, "https://x.example/:\n  title: X\n  source: [a]\n"))


def test_non_mapping_entry_message(tmp_path):
    with pytest.raises(RegistryError, match="entry must be a mapping with a 'title'"):
        load_registry(_write(tmp_path, "https://x.example/:\n"))


LABELED = """\
https://x.example/spec.html:
  title: Spec
  label: Spec page
  source: standard
  anchors: [b, a]
  anchor_labels:
    b: Section B
    a: Section A
"""


def test_anchor_labels_load_and_text_for(tmp_path):
    e = load_registry(_write(tmp_path, LABELED))["https://x.example/spec.html"]
    assert e.anchor_labels == {"b": "Section B", "a": "Section A"}
    assert e.text_for("https://x.example/spec.html#a") == "Section A"
    assert e.text_for("https://x.example/spec.html#b") == "Section B"


def test_text_for_falls_back_to_display_text(tmp_path):
    e = load_registry(_write(tmp_path, LABELED))["https://x.example/spec.html"]
    assert e.text_for("https://x.example/spec.html") == "Spec page"
    assert e.text_for("https://x.example/spec.html#other") == "Spec page"
    plain = LinkEntry(url="u", title="T", source="standard")
    assert plain.text_for("u#a") == "T"


def test_anchor_label_key_must_be_listed_anchor(tmp_path):
    text = "https://x.example/:\n  title: X\n  source: standard\n  anchors: [a]\n  anchor_labels: {z: Zed}\n"
    with pytest.raises(RegistryError, match="anchor_labels"):
        load_registry(_write(tmp_path, text))


def test_anchor_labels_must_be_str_mapping(tmp_path):
    for bad in ("[a]", "{a: [x]}"):
        text = f"https://x.example/:\n  title: X\n  source: standard\n  anchors: [a]\n  anchor_labels: {bad}\n"
        with pytest.raises(RegistryError, match="anchor_labels"):
            load_registry(_write(tmp_path, text))


def test_dump_writes_sorted_anchor_labels_after_anchors(tmp_path):
    reg = load_registry(_write(tmp_path, LABELED))
    out = tmp_path / "out.yaml"
    dump_registry(reg, out)
    assert load_registry(out) == reg
    body = out.read_text(encoding="utf-8")
    assert body.index("anchors:") < body.index("anchor_labels:")
    assert body.index("    a: Section A") < body.index("    b: Section B")


def test_dump_omits_empty_anchor_labels(tmp_path):
    reg = load_registry(_write(tmp_path, SAMPLE))
    out = tmp_path / "out.yaml"
    dump_registry(reg, out)
    assert "anchor_labels" not in out.read_text(encoding="utf-8")
