"""
cdm-verify-links — check every URL in the link registry against the live page:
HTTP 200 without redirect, <title> matches, listed anchors exist, altium.com URLs are in the sitemap.
"""

from __future__ import annotations

import argparse
import datetime
import http.client
import sys
import xml.etree.ElementTree as ET
from dataclasses import dataclass, field
from html.parser import HTMLParser
from typing import Callable, Optional
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

from cdm_tools.registry import DEFAULT_REGISTRY_PATH, LinkEntry, RegistryError, dump_registry, load_registry

USER_AGENT = "cdm-verify-links (+https://github.com/AltiumDeveloper/cdm)"
ALTIUM_DOCS_PREFIX = "https://www.altium.com/documentation/"
SITEMAP_INDEX = "https://www.altium.com/documentation/sitemap.xml"
_SM_NS = "{http://www.sitemaps.org/schemas/sitemap/0.9}"


@dataclass
class Page:
    status: int
    final_url: str
    title: Optional[str]
    ids: set[str] = field(default_factory=set)
    error: Optional[str] = None


class _PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.ids: set[str] = set()
        self.title: Optional[str] = None
        self._in_title = False
        self._parts: list[str] = []

    def handle_starttag(self, tag, attrs):
        for key, value in attrs:
            if value and (key == "id" or (key == "name" and tag == "a")):
                self.ids.add(value)
        if tag == "title" and self.title is None:
            self._in_title = True

    def handle_endtag(self, tag):
        if tag == "title" and self._in_title:
            self._in_title = False
            self.title = "".join(self._parts).strip()

    def handle_data(self, data):
        if self._in_title:
            self._parts.append(data)


def parse_page(html_text: str) -> tuple[Optional[str], set[str]]:
    parser = _PageParser()
    parser.feed(html_text)
    return parser.title, parser.ids


def page_title(raw: Optional[str]) -> Optional[str]:
    return raw.split(" | ")[0].strip() if raw else None


def _fetch_text(url: str) -> str:
    with urlopen(Request(url, headers={"User-Agent": USER_AGENT}), timeout=60) as resp:
        return resp.read().decode(resp.headers.get_content_charset() or "utf-8", errors="replace")


def fetch_page(url: str, timeout: int = 30) -> Page:
    try:
        with urlopen(Request(url, headers={"User-Agent": USER_AGENT}), timeout=timeout) as resp:
            body = resp.read().decode(resp.headers.get_content_charset() or "utf-8", errors="replace")
            title, ids = parse_page(body)
            return Page(status=resp.status, final_url=resp.geturl(), title=title, ids=ids)
    except HTTPError as exc:
        return Page(status=exc.code, final_url=url, title=None)
    except (URLError, OSError, http.client.HTTPException) as exc:
        return Page(status=0, final_url=url, title=None, error=f"{type(exc).__name__}: {exc}")


def _norm(url: str) -> str:
    return url.rstrip("/")


def check_entry(entry: LinkEntry, page: Page, sitemap: Optional[set[str]]) -> list[str]:
    if page.status == 0:
        return [f"network error: {page.error}"]
    if page.status != 200:
        return [f"HTTP {page.status}"]
    problems: list[str] = []
    if _norm(page.final_url) != _norm(entry.url):
        problems.append(f"redirected to {page.final_url}")
    actual = page_title(page.title)
    if actual != entry.title:
        problems.append(f"title changed: registry '{entry.title}', page '{actual}'")
    for anchor in entry.anchors:
        if anchor not in page.ids:
            problems.append(f"anchor #{anchor} not found")
    if sitemap is not None and entry.url.startswith(ALTIUM_DOCS_PREFIX) and _norm(entry.url) not in sitemap:
        problems.append("not listed in the altium.com documentation sitemap")
    return problems


def load_sitemap_urls(index_url: str = SITEMAP_INDEX, fetch_text: Callable[[str], str] = _fetch_text) -> set[str]:
    urls: set[str] = set()
    seen: set[str] = set()
    pending = [index_url]
    while pending:
        sitemap_url = pending.pop()
        if sitemap_url in seen:
            continue
        seen.add(sitemap_url)
        root = ET.fromstring(fetch_text(sitemap_url))
        is_index = root.tag == f"{_SM_NS}sitemapindex"
        for loc in root.iter(f"{_SM_NS}loc"):
            value = (loc.text or "").strip()
            if is_index:
                pending.append(value)
            else:
                urls.add(_norm(value))
    return urls


def main(argv: Optional[list[str]] = None) -> int:
    parser = argparse.ArgumentParser(prog="cdm-verify-links", description=__doc__)
    parser.add_argument("--registry", default=DEFAULT_REGISTRY_PATH)
    parser.add_argument("--no-sitemap", action="store_true", help="skip the altium.com sitemap check")
    parser.add_argument("--update", action="store_true", help="set last_verified=today on passing entries")
    args = parser.parse_args(argv)

    try:
        registry = load_registry(args.registry)
    except RegistryError as exc:
        print(f"cdm-verify-links: invalid link registry: {exc}", file=sys.stderr)
        return 2
    sitemap = None
    if not args.no_sitemap:
        try:
            sitemap = load_sitemap_urls()
        except (URLError, OSError, http.client.HTTPException, ET.ParseError) as exc:
            print(
                f"cdm-verify-links: could not load sitemap ({exc}); rerun with --no-sitemap to skip that check",
                file=sys.stderr,
            )
            return 2
    today = datetime.date.today().isoformat()
    failed = 0
    for url, entry in sorted(registry.items()):
        problems = check_entry(entry, fetch_page(url), sitemap)
        if problems:
            failed += 1
            print(f"FAIL {url}")
            for p in problems:
                print(f"  - {p}")
        else:
            print(f"ok   {url}")
            if args.update:
                entry.last_verified = today
    if args.update:
        dump_registry(registry, args.registry)
    print(f"{len(registry) - failed}/{len(registry)} links verified")
    return 1 if failed else 0
