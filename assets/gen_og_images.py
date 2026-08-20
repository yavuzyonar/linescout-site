#!/usr/bin/env python3
"""Generates 1200x630 Open Graph share images for OddsLighthouse.
Zero-cost: renders HTML/SVG via headless Chromium, no external image APIs.
Re-run whenever a new article is added to articles/manifest.json.
"""
import json, os, subprocess, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.dirname(ROOT)
CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
OUT_DIR = os.path.join(ROOT, "og")
TMP_HTML = os.path.join(ROOT, "_og_render.html")

NAVY = "#16233d"; NAVY2 = "#1f3864"; TEAL = "#0e7c86"; AMBER = "#b8862b"

WORDMARK = """
<div style="display:flex;align-items:center;gap:14px;">
  <svg width="46" height="46" viewBox="0 0 64 64">
    <rect width="64" height="64" rx="14" fill="{navy}"/>
    <path d="M27 14 L37 14 L41 46 L23 46 Z" fill="#f3f6f9"/>
    <rect x="24.5" y="38" width="15" height="8" fill="{navy2}"/>
    <rect x="26" y="20" width="12" height="5" fill="{teal}"/>
    <polygon points="32,6 37,15 27,15" fill="{amber}"/>
    <circle cx="32" cy="12" r="2.4" fill="#fff9ec"/>
  </svg>
  <span style="font:700 30px/1 Arial, sans-serif;color:#f3f6f9;letter-spacing:-0.5px;">OddsLighthouse</span>
</div>
""".format(navy=NAVY, navy2=NAVY2, teal=TEAL, amber=AMBER)

def render(html, out_png):
    with open(TMP_HTML, "w") as f:
        f.write(html)
    raw = out_png + ".raw.png"
    subprocess.run([
        CHROME, "--headless", "--no-sandbox", "--disable-gpu",
        "--window-size=1200,900", "--hide-scrollbars",
        f"--screenshot={raw}", f"file://{TMP_HTML}"
    ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    subprocess.run(["convert", raw, "-crop", "1200x630+0+0", "+repage", out_png], check=True)
    os.remove(raw)

def default_card():
    html = f"""<!doctype html><html><head><style>
    html,body{{margin:0;padding:0;width:1200px;height:630px;font-family:Arial,sans-serif;}}
    .wrap{{width:1200px;height:630px;position:relative;background:{NAVY};
      background-image:url("file://{ROOT}/hero-bg.svg");background-size:cover;background-position:center;overflow:hidden;}}
    .overlay{{position:absolute;inset:0;background:linear-gradient(180deg, rgba(22,35,61,0.55) 0%, rgba(22,35,61,0.82) 100%);}}
    .content{{position:absolute;left:80px;top:0;bottom:0;display:flex;flex-direction:column;justify-content:center;max-width:900px;}}
    h1{{font:700 54px/1.15 Arial, sans-serif;color:#fff;margin:26px 0 0;}}
    p{{font:400 26px/1.5 Arial, sans-serif;color:#dbe3f0;margin:22px 0 0;max-width:760px;}}
    </style></head><body>
    <div class="wrap"><div class="overlay"></div>
      <div class="content">
        {WORDMARK}
        <h1>Straight answers on sports betting &amp; online casinos.</h1>
        <p>No hype, no jargon — independent guides to odds, bankroll strategy, and responsible gambling.</p>
      </div>
    </div>
    </body></html>"""
    render(html, os.path.join(OUT_DIR, "site-default.png"))
    print("wrote og/site-default.png")

def article_card(article):
    slug = article["slug"]; title = article["title"]; category = article["category"]
    icon_path = os.path.join(SITE, "assets", "article-images", slug + ".svg")
    with open(icon_path) as f:
        icon_svg = f.read()
    # strip xml/doctype declarations if present, keep the <svg ...> root
    html = f"""<!doctype html><html><head><style>
    html,body{{margin:0;padding:0;width:1200px;height:630px;font-family:Arial,sans-serif;background:{NAVY};}}
    .wrap{{width:1200px;height:630px;position:relative;background:{NAVY};overflow:hidden;}}
    .top{{position:absolute;left:64px;top:44px;}}
    .art{{position:absolute;left:0;top:118px;width:1200px;height:280px;overflow:hidden;}}
    .art svg{{width:1200px;height:400px;display:block;margin-top:-60px;}}
    .fade{{position:absolute;left:0;top:118px;width:1200px;height:280px;background:linear-gradient(180deg, rgba(22,35,61,0) 55%, rgba(22,35,61,0.9) 100%);}}
    .bottom{{position:absolute;left:64px;right:64px;bottom:46px;}}
    .kicker{{display:inline-block;font:700 20px/1 Arial, sans-serif;color:{AMBER};letter-spacing:1px;text-transform:uppercase;margin-bottom:14px;}}
    h1{{font:700 44px/1.25 Arial, sans-serif;color:#fff;margin:0;max-width:1080px;}}
    </style></head><body>
    <div class="wrap">
      <div class="top">{WORDMARK}</div>
      <div class="art">{icon_svg}</div>
      <div class="fade"></div>
      <div class="bottom">
        <div class="kicker">{category}</div>
        <h1>{title}</h1>
      </div>
    </div>
    </body></html>"""
    render(html, os.path.join(OUT_DIR, slug + ".png"))
    print(f"wrote og/{slug}.png")

def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    default_card()
    with open(os.path.join(SITE, "articles", "manifest.json")) as f:
        data = json.load(f)
    for a in data["articles"]:
        article_card(a)
    if os.path.exists(TMP_HTML):
        os.remove(TMP_HTML)

if __name__ == "__main__":
    main()
