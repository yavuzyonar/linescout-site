# LineScout

A static site for LineScout, an independent US sports betting / online casino content site. Hosted free on GitHub Pages.

## Structure

- `index.html`, `about.html`, `disclosure.html`, `responsible-gambling.html`, `privacy.html` — core pages
- `articles/` — one HTML file per article, plus `articles/manifest.json` which drives the homepage and guides-index listings
- `assets/style.css`, `assets/main.js` — shared styling and behavior (age gate, article listing renderer)

## Adding a new article

1. Copy an existing file in `articles/` as a template.
2. Add a matching entry to `articles/manifest.json` (slug, title, excerpt, category, date, readTime).
3. Commit and push — GitHub Pages redeploys automatically within about a minute.

This repo is also written to automatically by a daily scheduled Claude task (see project notes) that adds one new evergreen article per day and pushes it here directly.
