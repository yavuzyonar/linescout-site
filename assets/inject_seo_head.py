#!/usr/bin/env python3
"""Injects/refreshes canonical, Open Graph, Twitter Card, favicon, and
JSON-LD structured-data tags into every page's <head>, plus a visible
breadcrumb nav right after <header> and FAQPage JSON-LD auto-extracted from
any <section class="faq"> content already in the page. Driven by
articles/manifest.json for article-specific data.

Idempotent: looks for `<!-- SEO:START -->`/`<!-- SEO:END -->` and
`<!-- BREADCRUMB:START -->`/`<!-- BREADCRUMB:END -->` marker blocks and
replaces them if present, otherwise inserts them. Safe to re-run any time
(e.g. after the daily content engine adds a new article) — run
gen_sitemap.py and gen_og_images.py first so this can reference the new
files.
"""
import json, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # site/
BASE_URL = "https://oddslighthouse.com"
SITE_NAME = "OddsLighthouse"
DEFAULT_OG = "/assets/og/site-default.png"

with open(os.path.join(ROOT, "articles", "manifest.json")) as f:
    MANIFEST = {a["slug"]: a for a in json.load(f)["articles"]}

# path (relative to site/) -> breadcrumb list of (name, url_or_None)
STATIC_PAGES = {
    "index.html": [("Home", None)],
    "betting.html": [("Home", "/"), ("Sports Betting", None)],
    "casino.html": [("Home", "/"), ("Casino", None)],
    "responsible-gambling.html": [("Home", "/"), ("Responsible Gambling", None)],
    "about.html": [("Home", "/"), ("About", None)],
    "disclosure.html": [("Home", "/"), ("Advertising Disclosure", None)],
    "privacy.html": [("Home", "/"), ("Privacy Policy", None)],
    "articles/index.html": [("Home", "/"), ("All Guides", None)],
    "odds-calculator.html": [("Home", "/"), ("Odds Calculator", None)],
}

def get_tag_content(html, tag_pattern):
    m = re.search(tag_pattern, html, re.S)
    return m.group(1).strip() if m else ""

def unesc(s):
    return (s.replace("&amp;", "&").replace("&quot;", '"')
             .replace("&lt;", "<").replace("&gt;", ">"))

def esc(s):
    s = unesc(s)
    return s.replace("&", "&amp;").replace('"', "&quot;").replace("<", "&lt;").replace(">", "&gt;")

def strip_tags(s):
    return re.sub(r"\s+", " ", re.sub(r"<[^<]+?>", "", s)).strip()

def compute_crumbs(rel_path, title):
    is_article = rel_path.startswith("articles/") and rel_path != "articles/index.html"
    if is_article:
        slug = rel_path.split("/")[-1].replace(".html", "")
        art = MANIFEST.get(slug, {})
        is_casino = art.get("category") == "Casino Guides"
        return [("Home", "/"),
                ("Casino" if is_casino else "Sports Betting", "/casino.html" if is_casino else "/betting.html"),
                (art.get("title", title), None)]
    return STATIC_PAGES.get(rel_path, [("Home", None)])

def build_breadcrumb_jsonld(crumbs):
    items = []
    for i, (name, url) in enumerate(crumbs, start=1):
        entry = {"@type": "ListItem", "position": i, "name": name}
        if url is not None:
            entry["item"] = BASE_URL + url
        items.append(entry)
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": items}

def build_faq_jsonld(html):
    items = re.findall(
        r'<div class="faq-item">\s*<h3 class="faq-q">(.*?)</h3>\s*<div class="faq-a">(.*?)</div>\s*</div>',
        html, re.S)
    if not items:
        return None
    entities = []
    for q, a_html in items:
        entities.append({
            "@type": "Question",
            "name": strip_tags(q),
            "acceptedAnswer": {"@type": "Answer", "text": strip_tags(a_html)}
        })
    return {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": entities}

def build_head_block(rel_path, html, crumbs):
    is_article = rel_path.startswith("articles/") and rel_path != "articles/index.html"
    depth = rel_path.count("/")
    prefix = "../" * depth

    title = get_tag_content(html, r"<title>(.*?)</title>")
    description = get_tag_content(html, r'<meta name="description" content="(.*?)">')
    url_path = "/" + rel_path.replace("index.html", "") if rel_path != "index.html" else "/"
    canonical = BASE_URL + url_path

    ld_blocks = []

    if is_article:
        slug = rel_path.split("/")[-1].replace(".html", "")
        art = MANIFEST.get(slug, {})
        og_image = f"/assets/og/{slug}.png"
        og_type = "article"
        ld_blocks.append({
            "@context": "https://schema.org",
            "@type": "Article",
            "headline": art.get("title", title),
            "description": art.get("excerpt", description),
            "image": BASE_URL + og_image,
            "datePublished": art.get("date", ""),
            "dateModified": art.get("date", ""),
            "author": {"@type": "Organization", "name": SITE_NAME, "url": BASE_URL},
            "publisher": {
                "@type": "Organization", "name": SITE_NAME,
                "logo": {"@type": "ImageObject", "url": BASE_URL + "/assets/apple-touch-icon.png"}
            },
            "mainEntityOfPage": {"@type": "WebPage", "@id": canonical}
        })
    else:
        og_image = DEFAULT_OG
        og_type = "website"
        if rel_path == "index.html":
            ld_blocks.append({
                "@context": "https://schema.org",
                "@type": "Organization",
                "name": SITE_NAME,
                "url": BASE_URL + "/",
                "logo": BASE_URL + "/assets/apple-touch-icon.png"
            })
            ld_blocks.append({
                "@context": "https://schema.org",
                "@type": "WebSite",
                "name": SITE_NAME,
                "url": BASE_URL + "/"
            })

    if len(crumbs) > 1:
        ld_blocks.append(build_breadcrumb_jsonld(crumbs))

    faq_ld = build_faq_jsonld(html)
    if faq_ld:
        ld_blocks.append(faq_ld)

    og_image_abs = BASE_URL + og_image

    lines = []
    lines.append('<!-- SEO:START (generated by assets/inject_seo_head.py — do not hand-edit, re-run script) -->')
    lines.append(f'<link rel="canonical" href="{canonical}">')
    lines.append(f'<link rel="icon" type="image/svg+xml" href="{prefix}assets/favicon.svg">')
    lines.append(f'<link rel="icon" type="image/png" sizes="32x32" href="{prefix}assets/favicon-32.png">')
    lines.append(f'<link rel="apple-touch-icon" sizes="180x180" href="{prefix}assets/apple-touch-icon.png">')
    lines.append('<meta name="theme-color" content="#16233d">')
    lines.append(f'<meta property="og:site_name" content="{SITE_NAME}">')
    lines.append(f'<meta property="og:type" content="{og_type}">')
    lines.append(f'<meta property="og:title" content="{esc(title)}">')
    lines.append(f'<meta property="og:description" content="{esc(description)}">')
    lines.append(f'<meta property="og:url" content="{canonical}">')
    lines.append(f'<meta property="og:image" content="{og_image_abs}">')
    lines.append('<meta property="og:image:width" content="1200">')
    lines.append('<meta property="og:image:height" content="630">')
    lines.append('<meta property="og:locale" content="en_US">')
    lines.append('<meta name="twitter:card" content="summary_large_image">')
    lines.append(f'<meta name="twitter:title" content="{esc(title)}">')
    lines.append(f'<meta name="twitter:description" content="{esc(description)}">')
    lines.append(f'<meta name="twitter:image" content="{og_image_abs}">')
    for block in ld_blocks:
        lines.append('<script type="application/ld+json">' + json.dumps(block, ensure_ascii=False) + '</script>')
    lines.append('<!-- SEO:END -->')
    return "\n".join(lines)

def crumb_href(url, prefix):
    if url == "/":
        return (prefix + "index.html") if prefix else "index.html"
    return prefix + url.lstrip("/")

def build_breadcrumb_html(crumbs, prefix):
    if len(crumbs) <= 1:
        return None
    lis = []
    for name, url in crumbs:
        if url is not None:
            lis.append(f'<li><a href="{crumb_href(url, prefix)}">{esc(name)}</a></li>')
        else:
            lis.append(f'<li aria-current="page">{esc(name)}</li>')
    inner = "".join(lis)
    return (
        '<!-- BREADCRUMB:START (generated by assets/inject_seo_head.py — do not hand-edit, re-run script) -->\n'
        f'<nav class="breadcrumb" aria-label="Breadcrumb"><div class="container"><ol>{inner}</ol></div></nav>\n'
        '<!-- BREADCRUMB:END -->'
    )

def process_file(path, rel_path):
    with open(path) as f:
        html = f.read()

    title = get_tag_content(html, r"<title>(.*?)</title>")
    crumbs = compute_crumbs(rel_path, title)
    depth = rel_path.count("/")
    prefix = "../" * depth

    head_block = build_head_block(rel_path, html, crumbs)
    if "<!-- SEO:START" in html:
        html = re.sub(r"<!-- SEO:START.*?<!-- SEO:END -->", head_block, html, flags=re.S)
    else:
        marker = re.search(r'<meta name="description" content=".*?">\n', html)
        if not marker:
            print(f"  SKIP (no description tag found): {rel_path}")
            return
        idx = marker.end()
        html = html[:idx] + head_block + "\n" + html[idx:]

    bc_block = build_breadcrumb_html(crumbs, prefix)
    if "<!-- BREADCRUMB:START" in html:
        if bc_block:
            html = re.sub(r"<!-- BREADCRUMB:START.*?<!-- BREADCRUMB:END -->", bc_block, html, flags=re.S)
        else:
            html = re.sub(r"\s*<!-- BREADCRUMB:START.*?<!-- BREADCRUMB:END -->\n?", "", html, flags=re.S)
    elif bc_block:
        marker = re.search(r"</header>\n?", html)
        if marker:
            idx = marker.end()
            html = html[:idx] + bc_block + "\n" + html[idx:]

    with open(path, "w") as f:
        f.write(html)
    print(f"  updated {rel_path}")

def main():
    for rel_path in list(STATIC_PAGES.keys()):
        process_file(os.path.join(ROOT, rel_path), rel_path)
    art_dir = os.path.join(ROOT, "articles")
    for fname in sorted(os.listdir(art_dir)):
        if fname.endswith(".html") and fname != "index.html":
            rel_path = f"articles/{fname}"
            process_file(os.path.join(ROOT, rel_path), rel_path)

if __name__ == "__main__":
    main()
