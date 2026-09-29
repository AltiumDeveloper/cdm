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
