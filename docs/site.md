# Site redesign: plain HTML and an MCP-first offering

Status: implemented and approved for release from branch `bw`. GitHub Pages publishes the static site when the release reaches `main`.

The marketing pages are plain HTML/CSS in `site/`. The existing nontech deck is retained separately with its original design and behavior.

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
| What could your users do through their agents? | Show concrete product interactions: ordering pizza, buying movie tickets, and invoicing client work. |
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

Implemented examples, refined during review (not verbatim script):

- **Ordering:** “Order my usual pizza.” The agent finds the saved order and prepares a new one. The sentence about user confirmation before checkout was removed during review.
- **Movie tickets:** “Buy movie tickets for me and my kids after school on Thursday.” Using shared family details and location, the agent knows to book three tickets for a 5pm PG movie within driving distance.
- **Client billing:** “Invoice Acme for last month’s work at our agreed rates.” The agent finds unbilled time, applies the contracted rates, and drafts an itemized invoice. This replaces the generic sales comparison.

Supporting copy: **Your users already know what they want to do. We build and manage the MCP server that lets their AI agents do it through your product.**

Keep these three examples compact and directly connected to the offer, not a broad industry/use-case catalog. Actual capabilities depend on the product API, permissions, and implementation. The FAQ explains authorization and confirmation controls for sensitive actions.

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

The site now uses actual static files in a dedicated publish directory:

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

Updated `.github/workflows/gh-pages.yml`:

1. Removed the Hugo setup and build steps.
2. Added `python3 scripts/check-site.py` validation.
3. Upload `site/` directly as the Pages artifact.
4. Retained the GitHub Pages deployment job and `main` trigger.

Deployment still uses Pages artifacts and `actions/deploy-pages`, not branch-based publishing. There is no site generation step.

### Completed cleanup

- Removed Hugo configuration, templates, archetypes, content sources, booking data, Go module files, old theme/marketing assets, and generated output after verifying the replacement.
- Copied the retained deck and company logos into the publish directory before removing the old setup.
- Updated `README.md` with plain-HTML development, validation, publishing, and asset-editing instructions.
- Updated the repository release instructions to run static-site validation instead of Hugo.
- Left unrelated repository files and work untouched. Old tracked content remains recoverable from Git history.

## URL and content migration

- Existing blog URLs and the RSS feed do not need to be preserved. Blog migration is outside the initial launch scope.
- Preserved `/decks/nontech/` as static files copied from `docs/decks/nontech.html` and `docs/decks/assets/`. Run `python3 scripts/sync-assets.py` after changing those sources; validation checks that the published copies match.
- Keep the older deck accessible without promoting it in the main navigation.
- Old `/services/.../` URLs do not need to be preserved. No redirects or migration pages are required for retired blog or services routes; they can return the site's standard 404 page.
- Keep `/contact/` working, focused on one MCP conversation and email.
- Initially use the existing free-consultation link: `https://cal.com/rfive.ai/free-consultation`.
- Still to do outside this repository: update the Cal.com booking-page wording to match the MCP offer.
- Retain the existing contact email: `cesar@rfive.ai`.
- Update titles, descriptions, social preview images, canonical URLs, sitemap, and structured data alongside visible copy.
- Keep the custom domain `rfive.ai` through the published `CNAME` file.

## Current repository reference points

- `site/index.html`: hero, experience logos, product interactions, offer, process, FAQ, and consultation CTA.
- `site/styles.css`: shared monochrome palette and responsive layouts.
- `site/contact/index.html`: MCP-focused consultation and email contact.
- `site/404.html`: retired/missing page experience.
- `site/assets/social-preview.svg` and `.png`: editable social artwork and published preview image.
- `site/robots.txt`, `site/sitemap.xml`, and `site/CNAME`: discovery and custom-domain configuration.
- `scripts/check-site.py`: dependency-free static-site validation.
- `scripts/sync-assets.py`: retained deck and logo synchronization.
- `.github/workflows/gh-pages.yml`: static validation and Pages deployment.
- `docs/products.md`: updated development-and-management offering; other products deferred.

## Recommended first release

One polished landing page and one clear offer: **custom MCP server development and management**. Use the hero buttons **Learn more** and **Schedule a free consultation**, with consultation as the primary conversion goal.

Do not carry over the old blog or services navigation. Do not build a marketplace, pricing configurator, or complex content system yet.

Before launch, verify responsive layouts, accessibility, internal links, retained contact and deck routes, standard 404 behavior for retired routes, metadata, and the published artifact contents.

## Verification completed

- `python3 scripts/check-site.py`: all four HTML pages passed local link/anchor, metadata, structured-data, XML, publish-file, and asset-sync checks.
- Chromium checks at 1440, 1024, 768, 390, and 320px: no horizontal overflow on homepage, contact, or 404; logos loaded; Learn more navigated correctly; FAQ worked with keyboard input.
- JavaScript-disabled check: homepage and native FAQ remained usable, with consultation links available.
- Automated axe WCAG 2 A/AA and 2.1 AA checks: no violations reported on homepage, contact, and 404 at desktop and mobile widths. This is not a substitute for a complete accessibility audit.
- Visually reviewed desktop/mobile hero layouts, full desktop page, and social preview image.
- Retained deck route and logos loaded; published files match the original source.
- `git diff --check` passed.

## Release notes and follow-up

- Release approved after the homepage examples were refined and the legal entity name was corrected to **R5 AI LLC** in all marketing-page footers and structured data.
- No fixed pricing, timeline, uptime, or support-hours guarantees are published. Define these per engagement.
- External follow-up: update the Cal.com event wording; it is managed outside this repository.
- Verify the GitHub Pages deployment after pushing `main`. Local preview and validation instructions are in `README.md`.
