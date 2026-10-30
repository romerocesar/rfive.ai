# Site redesign: plain HTML and an MCP-first offering

Status: proposed direction. Implementation has not started.

## Goals

- Remove Hugo, the LoveIt theme, and their build dependencies.
- Use a simple plain-HTML site with CSS and no required JavaScript.
- Replace Prussian blue with a black background, white foreground, and gray accents.
- Make selling MCP servers the core offering rather than broad AI consulting.

## Positioning

Treat this as a repositioning of R5, not just a theme change:

**R5 builds MCP servers that let AI work with your business systems.**

Suggested hero:

> Custom MCP server development
>
> **Your systems. Connected to AI.**
>
> R5 builds custom MCP servers that let AI assistants and agents work with your APIs, internal tools, and business data—with explicit permissions and controls.
>
> **Discuss your MCP project** · See how it works

Briefly explain the protocol:

> Model Context Protocol (MCP) gives AI applications a standard way to access tools and data. We build the server that connects those applications to your business.

### Main decision to settle

Are we selling **custom MCP server development**, **ready-made servers**, or both?

Recommendation: lead with custom development based on the existing consultancy business. Introduce packaged servers when there are concrete products to demonstrate, license, document, and support. Do not imply that a product catalog already exists.

## Homepage structure

Build one focused sales page:

| Section | Purpose |
| --- | --- |
| Hero | Say what we build, who it helps, and how to start. |
| What could AI do with your systems? | Show concrete workflows instead of generic AI benefits. |
| What we build | Describe internal MCP servers and customer-facing MCP integrations. |
| What you get | Clarify deliverables and ownership. |
| How an engagement works | Scope → build → validate → deploy and hand off. |
| Why R5 | Relevant engineering experience and genuine evidence. |
| FAQ and contact | Address deployment, access, compatibility, and next steps. |

### Illustrative use cases

- **Internal operations:** retrieve account history, check order status, or prepare updates through permissioned tools.
- **SaaS products:** give customers an MCP interface to the product.
- **Private systems:** expose selected capabilities from internal APIs and databases without giving an agent unrestricted access.

Label these as illustrative unless they are actual delivered projects. Do not invent customer evidence or results.

## Core offer

### Custom MCP server development

Proposed deliverables:

- Workflow and API discovery
- Tool and resource design
- Authentication and authorization appropriate to the deployment
- Input validation, error handling, and tests
- Deployment instructions and client configuration
- Documentation and handoff

Offer **ongoing maintenance and expansion** as an optional follow-on.

Workshops and audits can support discovery rather than appearing as equal-weight homepage offerings. Remove fractional CTO and recruiting calls from the primary sales path.

## Visual direction

Use a strictly monochrome palette:

```css
:root {
  color-scheme: dark;

  --bg: #000000;
  --surface: #111111;
  --fg: #ffffff;
  --muted: #b3b3b3;
  --border: #333333;
  --accent: #d4d4d4;
}
```

Design guidelines:

- Black background, white headings, gray supporting text.
- White primary buttons with black text.
- Neutral-gray secondary links and outlined buttons.
- Thin rules, generous spacing, and restrained typography.
- System sans-serif typography; monospace only for technical labels and examples.
- A simple diagram: **AI application → Your MCP server → Your systems**.
- No gradients, blue glows, carousel, or stock AI imagery.
- Visible keyboard focus, sufficient contrast, and responsive layouts.
- Review logos and image assets for embedded blue, not just CSS colors.

The result should feel like a focused engineering company rather than a generic AI agency.

## Technical approach

Replace Hugo with actual static files in a dedicated publish directory:

```text
site/
  index.html
  styles.css
  404.html
  CNAME
  robots.txt
  sitemap.xml
  assets/
  blog/
    index.html
    index.xml
    incremental/
      index.html
  contact/
    index.html
  decks/
    nontech/
      index.html
      assets/
```

No framework, bundler, Go dependency, or required JavaScript. Add JavaScript only for a specific interaction that needs it.

Publish only `site/`, never the repository root. The repository contains unrelated and potentially private files that must not become public site assets.

### Local development

```bash
python3 -m http.server 8000 --directory site
```

### Deployment

Update `.github/workflows/gh-pages.yml`:

1. Remove the Hugo setup step.
2. Remove the Hugo build step.
3. Upload `site/` instead of `public/` as the Pages artifact.
4. Keep the existing GitHub Pages deployment job.

The current workflow already uses Pages artifacts and `actions/deploy-pages`; no move to branch-based publishing is needed.

### Cleanup after verification

Once the replacement is verified:

- Remove Hugo configuration, templates, archetypes, module files, and build artifacts.
- Migrate required content and assets before removing their old directories.
- Review `config/`, `layouts/`, `archetypes/`, `content/`, `static/`, `assets/`, `resources/`, `public/`, `go.mod`, `go.sum`, and `.hugo_build.lock` for cleanup.
- Update `README.md` with plain-HTML development, publishing, and content-editing instructions.
- Preserve unrelated repository files and work.

## URL and content migration

- Preserve existing blog URLs and the RSS feed if they have readers or inbound links.
- Preserve `/decks/nontech/`, currently published through Hugo file mounts from `docs/decks/nontech.html` and `docs/decks/assets/`.
- Keep the older deck accessible without promoting it in the main navigation.
- Give old `/services/.../` URLs a relevant replacement or clear migration page rather than breaking them. Choose a redirect approach compatible with GitHub Pages if needed.
- Keep `/contact/` working, focused on one MCP conversation and email.
- Initially use the existing free-consultation link: `https://cal.com/rfive.ai/free-consultation`.
- Update the booking-page wording to match the MCP offer.
- Retain the existing contact email: `cesar@rfive.ai`.
- Update titles, descriptions, social preview images, canonical URLs, sitemap, and structured data alongside visible copy.
- Keep the custom domain `rfive.ai` through the published `CNAME` file.

## Current repository reference points

- `config/_default/hugo.toml`: site metadata, theme configuration, and deck mounts.
- `assets/css/_override.scss`: current Prussian-blue palette.
- `layouts/index.html` and `content/_index.md`: current homepage.
- `content/contact/_index.md` and `data/booking_options.yaml`: current contact and booking options.
- `.github/workflows/gh-pages.yml`: current Hugo build and Pages deployment.
- `docs/products.md`: existing workshops, audits, and custom-solutions positioning; revisit for consistency once the MCP offering is settled.

## Recommended first release

One polished landing page, one primary CTA, and one clear offer: **custom MCP servers**.

Keep the blog and legacy links in the background. Do not build a marketplace, pricing configurator, or complex content system yet.

Before launch, verify responsive layouts, accessibility, internal links, preserved routes, metadata, and the published artifact contents.

## Resume here

1. Confirm custom development versus ready-made servers as the initial commercial model.
2. Finalize the offer, deliverables, evidence, and homepage copy.
3. Implement the monochrome static site.
4. Migrate retained content and URLs.
5. Verify the replacement, switch deployment, and remove Hugo.
