#!/usr/bin/env python3
"""Validate the publish directory using only the Python standard library."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import json
import re
import sys
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "site"
ERRORS = []


def check(condition, message):
    if not condition:
        ERRORS.append(message)


class Page(HTMLParser):
    def __init__(self, path):
        super().__init__(convert_charrefs=True)
        self.path = path
        self.ids = set()
        self.refs = []
        self.meta = {}
        self.canonical = None
        self.h1s = 0
        self.mains = 0
        self.lang = None
        self.has_title = False
        self.scripts = []
        self.script = None
        self.feed(path.read_text())
        self.close()

    def handle_starttag(self, tag, attributes):
        attrs = dict(attributes)
        if "id" in attrs:
            check(attrs["id"] not in self.ids, f"{self.path}: duplicate ID {attrs['id']}")
            self.ids.add(attrs["id"])
        for attribute in ("href", "src", "poster"):
            if attrs.get(attribute):
                self.refs.append(attrs[attribute])
        if tag == "html":
            self.lang = attrs.get("lang")
        if tag == "h1":
            self.h1s += 1
        if tag == "main":
            self.mains += 1
        if tag == "title":
            self.has_title = True
        if tag == "img":
            check("alt" in attrs, f"{self.path}: image is missing alt text")
        if tag == "meta":
            key = attrs.get("name", attrs.get("property"))
            if key:
                self.meta[key] = attrs.get("content", "")
            if key == "og:image":
                self.refs.append(attrs.get("content", ""))
        if tag == "link" and attrs.get("rel") == "canonical":
            self.canonical = attrs.get("href")
        if tag == "script":
            self.script = {"type": attrs.get("type"), "src": attrs.get("src"), "text": ""}
            self.scripts.append(self.script)

    def handle_data(self, data):
        if self.script is not None:
            self.script["text"] += data

    def handle_endtag(self, tag):
        if tag == "script":
            self.script = None


expected_pages = {"index.html", "contact/index.html", "404.html", "decks/nontech/index.html"}
actual_pages = {str(path.relative_to(SITE)) for path in SITE.rglob("*.html")}
check(actual_pages == expected_pages, f"Unexpected page set: {actual_pages ^ expected_pages}")
pages = {path.resolve(): Page(path) for path in SITE.rglob("*.html")}


def check_ref(source, ref):
    url = urlsplit(ref)
    if url.scheme and url.scheme not in {"https", "http"}:
        check(url.scheme in {"mailto", "tel", "data"}, f"{source}: unexpected URL scheme: {ref}")
        return
    if url.netloc and url.netloc != "rfive.ai":
        return
    if not url.path:
        target = source
    elif url.path.startswith("/"):
        target = SITE / unquote(url.path).lstrip("/")
    else:
        target = source.parent / unquote(url.path)
    target = target.resolve()
    check(target.is_relative_to(SITE.resolve()), f"{source}: reference escapes site/: {ref}")
    if target.is_dir():
        target /= "index.html"
    check(target.is_file(), f"{source}: broken local reference: {ref}")
    if url.fragment and target in pages:
        check(unquote(url.fragment) in pages[target].ids, f"{source}: missing anchor: {ref}")


for path, page in pages.items():
    check(page.lang == "en", f"{path}: missing English language attribute")
    check(page.has_title, f"{path}: missing title")
    check(bool(page.meta.get("viewport")), f"{path}: missing viewport")
    for ref in page.refs:
        check_ref(path, ref)
    if path.relative_to(SITE).as_posix().startswith("decks/"):
        continue  # The retained deck intentionally keeps its original presentation behavior.
    check(page.h1s == 1, f"{path}: expected exactly one h1")
    check(page.mains == 1, f"{path}: expected exactly one main landmark")
    check(bool(page.meta.get("description")), f"{path}: missing description")
    for script in page.scripts:
        check(script["type"] == "application/ld+json" and not script["src"], f"{path}: marketing page has executable JS")
        if script["type"] == "application/ld+json":
            try:
                json.loads(script["text"])
            except ValueError as error:
                ERRORS.append(f"{path}: invalid structured data: {error}")
    if path.name == "404.html":
        check(page.meta.get("robots") == "noindex", "404 page must be noindex")
    else:
        route = "/" + path.relative_to(SITE).as_posix().removesuffix("index.html")
        check(page.canonical == f"https://rfive.ai{route}", f"{path}: incorrect canonical")
        for key in ("og:title", "og:description", "og:url", "og:image", "og:image:alt", "twitter:card"):
            check(bool(page.meta.get(key)), f"{path}: missing {key}")

for path in SITE.rglob("*"):
    check(not path.is_symlink(), f"Do not publish symlinks: {path}")
    if not path.is_file():
        continue
    check(path.suffix in {".html", ".css", ".svg", ".png", ".xml", ".txt"} or path.name in {"CNAME", ".nojekyll"}, f"Unexpected publish file: {path}")
    if path.suffix in {".xml", ".svg"}:
        try:
            ET.parse(path)
        except ET.ParseError as error:
            ERRORS.append(f"{path}: invalid XML: {error}")
    if path.suffix == ".css":
        for ref in re.findall(r"url\(['\"]?([^)'\"]+)", path.read_text()):
            check_ref(path, ref)

check((SITE / "CNAME").read_text().strip() == "rfive.ai", "Incorrect custom domain")
check((SITE / ".nojekyll").is_file(), "Missing .nojekyll")
check("Sitemap: https://rfive.ai/sitemap.xml" in (SITE / "robots.txt").read_text(), "Missing sitemap reference")
locations = {el.text for el in ET.parse(SITE / "sitemap.xml").iter("{http://www.sitemaps.org/schemas/sitemap/0.9}loc")}
check(locations == {"https://rfive.ai/", "https://rfive.ai/contact/", "https://rfive.ai/decks/nontech/"}, "Sitemap routes do not match retained pages")
for location in locations:
    check_ref(SITE / "index.html", location)

# Prevent source/published deck and logo copies drifting apart.
source = ROOT / "docs/decks"
copies = [(source / "nontech.html", SITE / "decks/nontech/index.html")]
for asset in (source / "assets").rglob("*"):
    if asset.is_file():
        copies.append((asset, SITE / "decks/nontech/assets" / asset.relative_to(source / "assets")))
for logo in (source / "assets/company-logos").glob("*.svg"):
    copies.append((logo, SITE / "assets/company-logos" / logo.name))
for original, copy in copies:
    check(copy.is_file() and copy.read_bytes() == original.read_bytes(), f"Out-of-sync asset: {copy}. Run python3 scripts/sync-assets.py")

if ERRORS:
    print("Site validation failed:", file=sys.stderr)
    for error in ERRORS:
        print(f"- {error}", file=sys.stderr)
    sys.exit(1)
print(f"Site validation passed: {len(pages)} HTML pages; local links, anchors, metadata, XML, publish files, and retained assets checked.")
