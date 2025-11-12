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

## Deployment

GitHub Actions (`.github/workflows/gh-pages.yml`) builds on pushes to `main` and publishes the `public/` folder to the `gh-pages` branch for GitHub Pages. A `static/CNAME` file keeps the custom domain `rfive.ai` configured.
