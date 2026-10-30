# Site redesign: plain HTML and an MCP-first offering

Status: proposed direction. Implementation has not started.

## Goals

- Remove Hugo, the LoveIt theme, and their build dependencies.
- Use a simple plain-HTML site with CSS and no required JavaScript.
- Replace Prussian blue with a black background, white foreground, and gray accents.
- Make custom MCP server development and management the core offering rather than broad AI consulting.

## Positioning

Treat this as a repositioning of R5, not just a theme change:

**R5 builds and manages custom MCP servers so your users can connect their AI agents to your product.**

Hero:

> **Can AI agents use your app yet?**
>
> Allow your users to get more done with their AI agents connected to the product they already use.
>
> **Learn more** · **Schedule a free consultation**

Briefly explain the protocol:

> Model Context Protocol (MCP) gives AI applications a standard way to access tools and data. We build the server that connects those applications to your business.

### Confirmed commercial focus

The primary offering is **custom MCP server development and management**. Ongoing management is part of the core offering, not merely an optional follow-on to a development project.

Workshops, ready-made servers, and other products can be added later. They are outside the initial launch scope and should not compete with the core offer in the homepage or navigation.

## Homepage structure

Build one focused sales page:

| Section | Purpose |
| --- | --- |
| Hero | Say what we build, who it helps, and how to start. |
| Social proof / experience | Establish credibility immediately with former employer and client logos from the nontech deck. |
| What could your users do through their agents? | Show concrete product interactions adapted from the VSL: ordering, buying tickets, booking appointments, and analyzing data. |
| What we build and manage | Lead with customer-facing MCP integrations that connect users' AI agents to the product; include internal servers as a secondary use case. |
| What you get | Clarify development deliverables, ongoing management, and ownership. |
| How an engagement works | Scope → build → validate → deploy → manage and evolve. |
| FAQ and contact | Address deployment, access, compatibility, and next steps. |

### Social proof immediately after the hero

Place the experience/logo section directly after the hero, before the details of what we offer and how we work. Reuse the logos already included in `docs/decks/nontech.html`, sourced from `docs/decks/assets/company-logos/`:

- Google
- Amazon
- Unity
- Walmart
- Ouva
- Ramen VR
- Medal.tv
- Demand-IQ
- Andesite
- Groundlight
- Valve

Suggested heading: **Experience includes**.

Add context such as **Former employers and clients** so the section does not imply that all of these companies are R5 clients, MCP customers, or endorsers. The deck currently describes these as companies where Cesar has worked; preserve that distinction when writing the final copy.

Use a compact, responsive logo grid with balanced visual sizing and accessible company names. Use suitable white or gray logo variants on black, respecting brand usage requirements and verifying contrast. Keep the section static rather than using an animated carousel. Copy the selected assets into the site's published assets directory during implementation.

### Concrete product interactions from the VSL

Replace the generic internal-operations / SaaS / private-systems use cases with examples of what users could do in a product through their AI agents.

The VSL examples transcript (`videos/mcp-vsl-clean/analysis/examples.transcript.json`) mentions ordering their usual pizza, buying tickets, booking an appointment, and analyzing data.

Suggested heading: **Your product. One request away.**

Possible user requests adapted from those examples (proposed website copy, not verbatim script):

- **Ordering:** “Order my usual pizza.”
- **Tickets:** “Find two tickets for Friday’s show.”
- **Appointments:** “Book my next appointment for Tuesday afternoon.”
- **Data:** “How did sales this month compare with last month?”

Supporting copy: **Your users already know what they want to do. We build and manage the MCP server that lets their AI agents do it through your product.**

Keep this compact and directly connected to the offer, not a broad industry/use-case catalog. Select the strongest two or three examples for the final layout. For purchases and bookings, demonstrate review or confirmation before committing; do not imply unrestricted agent actions. Actual capabilities depend on the product API, permissions, and implementation.

Label these as illustrative unless they are actual delivered projects. Do not invent customer evidence or results.

## Core offer

### Custom MCP server development and management

Proposed development deliverables:

- Workflow and API discovery
- Tool and resource design
- Authentication and authorization appropriate to the deployment
- Input validation, error handling, and tests
- Deployment instructions and client configuration
- Documentation and handoff

Ongoing management is a core part of the offer. Define the exact scope and service commitments before publishing; proposed responsibilities include:

- Deployment and operational monitoring
- Maintenance, dependency updates, and security updates
- Compatibility updates as the product API and MCP clients evolve
- Troubleshooting and reliability improvements
- Expansion of tools and capabilities as users' needs change

Do not imply specific uptime guarantees, support hours, or hosting arrangements until those terms are defined.

Defer workshops, ready-made servers, and other standalone products to a later release. Remove fractional CTO and recruiting calls from the primary sales path.

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

- Existing blog URLs and the RSS feed do not need to be preserved. Blog migration is outside the initial launch scope.
- Preserve `/decks/nontech/`, currently published through Hugo file mounts from `docs/decks/nontech.html` and `docs/decks/assets/`.
- Keep the older deck accessible without promoting it in the main navigation.
- Old `/services/.../` URLs do not need to be preserved. No redirects or migration pages are required for retired blog or services routes; they can return the site's standard 404 page.
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
- `docs/products.md`: existing workshops, audits, and custom-solutions positioning; update for consistency with the confirmed custom MCP development and management focus before launch.

## Recommended first release

One polished landing page and one clear offer: **custom MCP server development and management**. Use the hero buttons **Learn more** and **Schedule a free consultation**, with consultation as the primary conversion goal.

Do not carry over the old blog or services navigation. Do not build a marketplace, pricing configurator, or complex content system yet.

Before launch, verify responsive layouts, accessibility, internal links, retained contact and deck routes, standard 404 behavior for retired routes, metadata, and the published artifact contents.

## Resume here

1. Define the development and ongoing management scope, commercial terms, and service commitments.
2. Finalize deliverables, evidence, and homepage copy around the confirmed core offer; defer additional products.
3. Implement the monochrome static site.
4. Migrate only retained content and routes (contact and the nontech deck); skip old blog and services URLs.
5. Verify the replacement, switch deployment, and remove Hugo.
