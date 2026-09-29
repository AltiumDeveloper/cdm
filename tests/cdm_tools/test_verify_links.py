from cdm_tools.registry import LinkEntry
from cdm_tools.verify_links import Page, check_entry, load_sitemap_urls, page_title, parse_page

URL = "https://www.altium.com/documentation/altium-365/lifecycle-management"
HTML = """<html><head><title>Lifecycle Management | Altium 365 Technical Documentation</title></head>
<body><h1>Lifecycle Management</h1><a name="legacy"></a><div id="states">x</div></body></html>"""


def _entry(**kw):
    base = dict(url=URL, title="Lifecycle Management", source="altium-docs", anchors=["states"])
    base.update(kw)
    return LinkEntry(**base)


def _page(**kw):
    title, ids = parse_page(HTML)
    base = dict(status=200, final_url=URL, title=title, ids=ids)
    base.update(kw)
    return Page(**base)


def test_parse_page_collects_title_and_ids():
    title, ids = parse_page(HTML)
    assert title == "Lifecycle Management | Altium 365 Technical Documentation"
    assert {"states", "legacy"} <= ids


def test_page_title_strips_suffix():
    assert page_title("A | B Technical Documentation") == "A"
    assert page_title("PROV-O: The PROV Ontology") == "PROV-O: The PROV Ontology"
    assert page_title(None) is None


def test_check_entry_ok():
    assert check_entry(_entry(), _page(), sitemap={URL}) == []


def test_check_entry_problems():
    problems = check_entry(
        _entry(title="Old Title", anchors=["states", "gone"]),
        _page(final_url="https://www.altium.com/login"),
        sitemap=set(),
    )
    text = "\n".join(problems)
    assert "redirected to https://www.altium.com/login" in text
    assert "title changed" in text and "Old Title" in text
    assert "anchor #gone not found" in text
    assert "sitemap" in text


def test_check_entry_http_error_short_circuits():
    assert check_entry(_entry(), _page(status=404), sitemap=None) == ["HTTP 404"]


def test_load_sitemap_urls_follows_indexes():
    docs = {
        "https://s/index.xml": '<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
        "<sitemap><loc>https://s/a.xml</loc></sitemap></sitemapindex>",
        "https://s/a.xml": '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
        f"<url><loc>{URL}/</loc></url></urlset>",
    }
    assert load_sitemap_urls("https://s/index.xml", fetch_text=docs.__getitem__) == {URL}


# --- network-error robustness (no network) ---
from urllib.error import URLError  # noqa: E402

from cdm_tools import verify_links  # noqa: E402
from cdm_tools.registry import dump_registry  # noqa: E402


def _tmp_registry(tmp_path):
    path = tmp_path / "registry.yaml"
    dump_registry({URL: _entry(anchors=[])}, path)
    return str(path)


def test_fetch_page_maps_os_errors_to_status_zero(monkeypatch):
    def fake(*args, **kwargs):
        raise ConnectionResetError("reset by peer")

    monkeypatch.setattr(verify_links, "urlopen", fake)
    page = verify_links.fetch_page(URL)
    assert page.status == 0
    assert page.error and "ConnectionResetError" in page.error


def test_check_entry_network_error():
    page = Page(status=0, final_url=URL, title=None, error="TimeoutError: timed out")
    assert check_entry(_entry(), page, sitemap=None) == ["network error: TimeoutError: timed out"]


def test_main_returns_2_when_sitemap_unavailable(monkeypatch, tmp_path, capsys):
    def boom(*args, **kwargs):
        raise URLError("no route")

    monkeypatch.setattr(verify_links, "load_sitemap_urls", boom)
    assert verify_links.main(["--registry", _tmp_registry(tmp_path)]) == 2
    assert "--no-sitemap" in capsys.readouterr().err


def test_main_exit_codes_without_sitemap(monkeypatch, tmp_path):
    reg = _tmp_registry(tmp_path)
    title, ids = parse_page(HTML)
    monkeypatch.setattr(verify_links, "fetch_page", lambda url: Page(200, URL, title, ids))
    assert verify_links.main(["--registry", reg, "--no-sitemap"]) == 0
    monkeypatch.setattr(verify_links, "fetch_page", lambda url: Page(404, URL, None))
    assert verify_links.main(["--registry", reg, "--no-sitemap"]) == 1
