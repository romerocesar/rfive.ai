# rfive.ai

R5’s marketing site for **custom MCP server development and management**.

The publishable site lives entirely in `site/`: plain HTML, a shared stylesheet,
and local assets. No framework, package installation, compilation, or JavaScript
is needed for the marketing pages. The retained nontech presentation keeps its
existing JavaScript and visual design.

## Local preview

From the repository root:

```bash
python3 -m http.server 8000 --directory site
```

Open:

- Homepage: http://localhost:8000/
- Contact: http://localhost:8000/contact/
- Retained deck: http://localhost:8000/decks/nontech/
- Custom 404 design: http://localhost:8000/404.html

Python’s basic server returns its own 404 response for missing URLs. GitHub Pages
uses `site/404.html` for those requests in production.

## Editing

- `site/index.html`: homepage copy, social proof, examples, offering, and FAQ.
- `site/styles.css`: shared monochrome theme and responsive layouts.
- `site/contact/index.html`: consultation and email contact.
- `site/404.html`: retired/missing pages.
- `site/assets/`: logos, favicon, and social preview artwork.
- `site/sitemap.xml` and `site/robots.txt`: search-engine discovery.
- `docs/site.md`: direction, implementation notes, and review checklist.
- `docs/products.md`: current commercial focus.

There is no template layer: shared header/footer markup is intentionally repeated
in three small HTML files. Keep it consistent when editing. Use root-relative
links; preview over HTTP rather than opening HTML files directly.

The social preview is committed as PNG for link-preview compatibility. Its
editable source is `site/assets/social-preview.svg`. To regenerate it with
ImageMagick installed:

```bash
magick -background black site/assets/social-preview.svg site/assets/social-preview.png
```

This is an optional asset-editing tool, not a deployment dependency.

## Presentation deck and experience logos

The retained deck source remains `docs/decks/nontech.html`; speaker notes remain
in `docs/decks/nontech.md`. Its older workshops/audits/solutions content is
intentionally preserved and is not promoted in the new site navigation.
The PDF in `docs/decks/` is a previous export, not automatically regenerated.

After editing the deck or its logos, refresh the published copies:

```bash
python3 scripts/sync-assets.py
```

This copies only the deck HTML and its assets into `site/decks/nontech/`, and the
company logos into `site/assets/company-logos/`. Commit the source and updated
copies together. Validation catches out-of-sync copies. Do not add private
documents or unrelated files to the deck’s assets directory.

## Validation

Requires Python 3.9 or newer, with no third-party packages:

```bash
python3 scripts/check-site.py
git diff --check
```

The checker verifies local links and anchors, image alt attributes, metadata,
structured data, sitemap routes, XML assets, the publish-file allowlist, and
deck/logo synchronization. It also checks that the marketing pages do not
introduce executable JavaScript. Use a browser to review visual changes,
keyboard navigation, responsive layouts, and native FAQ disclosures.

## Deployment

`.github/workflows/gh-pages.yml` validates the site on pushes to `main` and
publishes `site/` directly using GitHub Pages artifacts. The workflow can also
be triggered manually. There is no site build step.

`site/CNAME` retains the custom domain **rfive.ai**. Deploy **only `site/`**,
never the repository root: other directories contain internal documents and
unrelated work.

Old blog and services routes are intentionally retired, without redirects or RSS.
The contact and nontech deck routes remain available.

The consultation buttons use
https://cal.com/rfive.ai/free-consultation. Booking-page copy is managed in Cal.com
and must be updated there separately.
