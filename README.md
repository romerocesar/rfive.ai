# rfive.ai

R5’s static marketing site powered by [Hugo](https://gohugo.io/) and the [LoveIt theme](https://github.com/dillonzq/LoveIt).

## Prerequisites

- Hugo Extended `v0.125+`
- Go (for Hugo modules) `1.21+`

## Local Development

```bash
hugo server -D
```

Then open `http://localhost:1313`.

## Building

```bash
hugo --gc --minify
```

Generated assets land in `public/`.

## Presentation Deck

Edit `docs/decks/custom-ai-solution.html` for the interactive deck and
`docs/decks/custom-ai-solution.md` for its companion content and presenter notes.
The PDF in the same directory is an existing export; builds do not regenerate it.

Hugo's file mounts publish the HTML as `/decks/custom-ai-solution/index.html`
and copy `docs/decks/assets/` alongside it. The normal build and local server
both use these mounts, so no separate copy or build step is needed. The Markdown,
PDF, and other documentation are not included in this route.

- Local preview: `http://localhost:1313/decks/custom-ai-solution/`
- Published URL: `https://rfive.ai/decks/custom-ai-solution/`

## Publishing a Blog Article

Create a page bundle for the article:

```bash
hugo new content posts/my-article/index.md
```

Then:

1. Paste and adapt the LinkedIn post in the generated `index.md`.
2. Add a short `description` for the blog index and search previews.
3. If the LinkedIn version is public, set `linkedinURL` to its URL.
4. Optionally place a cover image named `cover.webp` in the same folder. PNG and JPEG also work.
5. Preview unpublished articles with `hugo server -D`.
6. Set `draft = false`, then commit and push the article to publish it.

Article URLs use `/blog/<slug>/`, and the blog RSS feed is available at `/blog/index.xml`.

## Deployment

GitHub Actions (`.github/workflows/gh-pages.yml`) builds on pushes to `main` and publishes the `public/` folder to the `gh-pages` branch for GitHub Pages. A `static/CNAME` file keeps the custom domain `rfive.ai` configured.
