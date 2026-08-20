#!/usr/bin/env python3
"""Regenerates /sitemap.xml from the static page list + articles/manifest.json.
Zero-cost, no dependencies. Run this after adding/editing any page or article
(the daily content engine runs it automatically after publishing).
"""
import json, os
from datetime import date

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # site/
BASE_URL = "https://oddslighthouse.com"

# path, changefreq, priority
STATIC_PAGES = [
    ("/", "daily", "1.0"),
    ("/betting.html", "daily", "0.9"),
    ("/casino.html", "daily", "0.9"),
    ("/responsible-gambling.html", "monthly", "0.6"),
    ("/about.html", "monthly", "0.4"),
    ("/disclosure.html", "yearly", "0.3"),
    ("/privacy.html", "yearly", "0.3"),
    ("/articles/index.html", "daily", "0.7"),
    ("/odds-calculator.html", "monthly", "0.6"),
    ("/news.html", "daily", "0.9"),
]

NEWS_CATEGORIES = {"Sports Betting News", "Casino News"}

def main():
    today = date.today().isoformat()
    with open(os.path.join(ROOT, "articles", "manifest.json")) as f:
        data = json.load(f)
    articles = data["articles"]

    urls = []
    for path, freq, pri in STATIC_PAGES:
        urls.append((BASE_URL + path, today, freq, pri))
    for a in articles:
        is_news = a.get("type") == "news" or a.get("category") in NEWS_CATEGORIES
        freq, pri = ("daily", "0.7") if is_news else ("monthly", "0.8")
        urls.append((f"{BASE_URL}/articles/{a['slug']}.html", a.get("date", today), freq, pri))

    lines = ['<?xml version="1.0" encoding="UTF-8"?>',
             '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for loc, lastmod, freq, pri in urls:
        lines.append("  <url>")
        lines.append(f"    <loc>{loc}</loc>")
        lines.append(f"    <lastmod>{lastmod}</lastmod>")
        lines.append(f"    <changefreq>{freq}</changefreq>")
        lines.append(f"    <priority>{pri}</priority>")
        lines.append("  </url>")
    lines.append("</urlset>")
    lines.append("")

    out_path = os.path.join(ROOT, "sitemap.xml")
    with open(out_path, "w") as f:
        f.write("\n".join(lines))
    print(f"wrote sitemap.xml with {len(urls)} URLs")

if __name__ == "__main__":
    main()
