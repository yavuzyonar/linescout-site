# OddsLighthouse

A static site for OddsLighthouse, an independent US sports betting / online casino content site. Hosted free on GitHub Pages.

## Structure

- `index.html`, `betting.html`, `casino.html`, `news.html`, `nfl.html`, `nba.html`, `nhl.html`, `college-football.html`, `about.html`, `disclosure.html`, `responsible-gambling.html`, `privacy.html`, `odds-calculator.html` — core pages
- `articles/` — one HTML file per article (evergreen guides and dated news briefs alike), plus `articles/manifest.json` which drives every listing page (`type`: `"evergreen"` or `"news"`; `category` drives routing — see below)
- `assets/style.css`, `assets/main.js` — shared styling and behavior (age gate, article listing renderer)
- `assets/calculator.js` — client-side odds converter powering `odds-calculator.html` (no backend, nothing tracked)

## Adding a new evergreen article

1. Copy an existing file in `articles/` as a template — `articles/how-betting-odds-work.html` has a working FAQ section to copy the markup from.
2. Add a matching entry to `articles/manifest.json` (slug, title, excerpt, category, date, readTime, `"type": "evergreen"`).
3. Add a header image at `assets/article-images/<slug>.svg` (see `assets/gen_article_images.py` for style reference).
4. Aim for ~1,200-1,800 words with real structure; add a table of contents (`.toc` class) if it runs long, and an FAQ section (`.faq`/`.faq-item`/`.faq-q`/`.faq-a` classes, 3-5 Q&As) near the end — the SEO script auto-generates `FAQPage` schema from that markup.
5. Run the SEO pipeline, in order: `python3 assets/gen_og_images.py`, `python3 assets/gen_sitemap.py`, `python3 assets/inject_seo_head.py`.
6. Commit and push — GitHub Pages redeploys automatically within about a minute.

## Adding a news brief

News lives in a separate category from evergreen guides and has stricter rules, since it makes factual claims about real, current events rather than durable explainer content:

1. Every claim must trace back to a genuinely researched, dated, named source (live web search + fetch, not training-data recall) — write an original summary, never copied text.
2. Category must be exactly `"Sports Betting News"` or `"Casino News"`, and manifest `"type"` must be `"news"` — this is what routes it onto `news.html` (and keeps it out of `betting.html`/`casino.html`'s evergreen grids) and gives it `NewsArticle` JSON-LD instead of `Article`.
3. Use `articles/fanatics-nfl-sportsbook-deal.html` and `articles/florida-sweepstakes-casino-lawsuit.html` as reference templates: a `<span class="news-badge">News</span>` badge next to the category kicker, a shorter body (~300-600 words), and a `.sources-box` at the end listing every source actually used, in place of the usual "further reading" links. No FAQ section on news briefs.
4. If there's no genuinely verifiable, on-topic story for a given category on a given day, skip it rather than inventing or padding — `news.html` says as much to readers, so this is expected behavior, not a failure.
5. Same SEO pipeline as evergreen articles, run once after all of a day's articles (evergreen + news) are in place.

## No disclosure-box (as of Aug 20, 2026)

Articles previously had a per-article `.disclosure-box` div ("we may be paid a commission by operators linked on this page..."). This was removed sitewide on Aug 20, 2026, because no article currently has a real, live, monetized affiliate link — the claim was inaccurate everywhere, not just on the one article a reader flagged. `disclosure.html` (the standalone advertising-disclosure policy page) is unaffected and keeps its own "contact us" callout. Do not reintroduce a per-article disclosure-box until a real affiliate program actually launches, at which point it should come back with accurate wording; the daily automation's prompt has a matching note telling it not to add one.

## Sport-specific hub pages

`nfl.html`, `nba.html`, `nhl.html`, and `college-football.html` (added Aug 20, 2026, timed for the 2026 NFL season) are dedicated hub pages, each showing only articles with an exact matching category (`"NFL"`, `"NBA"`, `"NHL"`, `"College Football"`). `betting.html`'s general grid excludes all four of these categories so sport-specific guides live only on their own page, with a "Betting by sport" cross-link row in `betting.html`'s intro linking out to all four. Sport-specific articles get 4-level breadcrumbs (Home > Sports Betting > \<Sport\> > Article) automatically via `inject_seo_head.py`'s `SPORT_CATEGORIES` map — no manual wiring needed, just use the exact category string.

## The daily automation

This repo is written to automatically by a daily scheduled Claude task (see project notes) that publishes up to four items per day — one sports-betting evergreen guide (drawn from either the general pool or one of the four sport-specific pools, weighted toward NFL through the 2026 season), one casino evergreen guide, one sports-betting news brief, and one casino news brief (the two news briefs are skipped on days with no verifiable story) — and pushes them here directly, including the SEO pipeline steps above.

## Keeping hub pages from growing unbounded

`betting.html` and `casino.html` show only the 12 most recent matching articles; `news.html` shows the 20 most recent items. Each has a "View all guides" link to `articles/index.html`, which is the full, uncapped archive — `sitemap.xml` and `articles/manifest.json` always list every article regardless of what's capped on the hub pages, so nothing is ever de-indexed or unreachable, this only trims what renders on the three hub grids. If `articles/index.html` itself eventually gets unwieldy (worth revisiting once the archive passes ~100-150 articles), the next step would be real pagination or a "load more" control there.

## SEO

- `robots.txt` and `sitemap.xml` (auto-generated) at the site root.
- Every page has a self-referencing canonical tag, Open Graph + Twitter Card tags, a favicon (`assets/favicon.svg` + PNG fallbacks), and a visible breadcrumb nav right after `<header>`.
- Every page carries JSON-LD structured data: `Organization`/`WebSite` on the homepage, `Article` (evergreen) or `NewsArticle` (news) + `BreadcrumbList` (+ `FAQPage` if the page has an FAQ section) on article pages, `BreadcrumbList` elsewhere.
- These are generated/refreshed by `assets/inject_seo_head.py` inside `<!-- SEO:START -->`/`<!-- SEO:END -->` and `<!-- BREADCRUMB:START -->`/`<!-- BREADCRUMB:END -->` blocks — don't hand-edit those blocks, re-run the script instead.
- Per-article Open Graph share images (1200x630) are generated by `assets/gen_og_images.py` into `assets/og/`.
- `betting.html`, `casino.html`, `news.html`, `nfl.html`, `nba.html`, `nhl.html`, and `college-football.html` are hand-written hub pages (intro copy, and for betting/casino a "start here" reading list) on top of the auto-generated, capped article grid — that intro content is not touched by any script.
- **Not yet done:** the site isn't verified/submitted in Google Search Console or Bing Webmaster Tools, so `sitemap.xml` isn't being actively crawled from a submitted sitemap yet; author identity is still a generic "Editorial Team" rather than a named person — see the audit notes for both.
