#!/usr/bin/env python3
"""Generates consistent, on-brand SVG header illustrations for OddsLighthouse articles.
Shared style: soft teal/navy gradient card, faint corner light-rays (brand motif), a
centered navy/teal line-art icon, and a small amber accent dot matching the logo mark.
Zero external assets, zero licensing concerns, fast to extend for new articles.
"""
import os

W, H = 1200, 400
OUT_DIR = os.path.join(os.path.dirname(__file__), "article-images")

FRAME_OPEN = f'''<svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#eaf4f3"/>
      <stop offset="100%" stop-color="#f6faf9"/>
    </linearGradient>
    <linearGradient id="beam" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0e7c86" stop-opacity="0.14"/>
      <stop offset="100%" stop-color="#0e7c86" stop-opacity="0"/>
    </linearGradient>
  </defs>
  <rect width="{W}" height="{H}" fill="url(#bg)"/>
  <polygon points="{W},0 {W},110 {W-420},{H} {W-560},{H}" fill="url(#beam)"/>
  <g stroke="#0e7c86" stroke-opacity="0.10" fill="none" stroke-width="2">
    <circle cx="{W-40}" cy="-30" r="140"/>
    <circle cx="{W-40}" cy="-30" r="240"/>
    <circle cx="{W-40}" cy="-30" r="340"/>
  </g>
  <circle cx="70" cy="60" r="7" fill="#b8862b"/>
'''
FRAME_CLOSE = "\n</svg>\n"

def wrap(icon_svg: str) -> str:
    return FRAME_OPEN + icon_svg + FRAME_CLOSE

CX, CY = W // 2, H // 2 + 10
NAVY = "#16233d"
TEAL = "#0e7c86"

ICONS = {
    "how-betting-odds-work": f'''
  <!-- probability gauge -->
  <g transform="translate({CX},{CY})">
    <path d="M -110 20 A 110 110 0 0 1 110 20" fill="none" stroke="{NAVY}" stroke-width="14" stroke-linecap="round"/>
    <path d="M -110 20 A 110 110 0 0 1 -10 -108" fill="none" stroke="{TEAL}" stroke-width="14" stroke-linecap="round"/>
    <circle cx="0" cy="20" r="10" fill="{NAVY}"/>
    <line x1="0" y1="20" x2="55" y2="-55" stroke="{NAVY}" stroke-width="8" stroke-linecap="round"/>
    <text x="-100" y="55" font-family="Arial" font-size="20" fill="{NAVY}" opacity="0.6">0%</text>
    <text x="82" y="55" font-family="Arial" font-size="20" fill="{NAVY}" opacity="0.6">100%</text>
  </g>''',

    "bankroll-management-basics": f'''
  <!-- ascending bar stack / bankroll -->
  <g transform="translate({CX-140},{CY+70})">
    <rect x="0" y="-60" width="46" height="60" rx="6" fill="{TEAL}" opacity="0.55"/>
    <rect x="70" y="-100" width="46" height="100" rx="6" fill="{TEAL}" opacity="0.75"/>
    <rect x="140" y="-150" width="46" height="150" rx="6" fill="{NAVY}"/>
    <rect x="210" y="-115" width="46" height="115" rx="6" fill="{TEAL}"/>
    <circle cx="243" cy="-165" r="20" fill="none" stroke="#b8862b" stroke-width="5"/>
    <text x="243" y="-158" font-family="Arial" font-size="18" fill="#b8862b" text-anchor="middle">$</text>
  </g>''',

    "bet-types-explained": f'''
  <!-- grid of 4 ticket cards -->
  <g transform="translate({CX-150},{CY-90})">
    <rect x="0" y="0" width="130" height="80" rx="10" fill="none" stroke="{NAVY}" stroke-width="6"/>
    <rect x="160" y="0" width="130" height="80" rx="10" fill="none" stroke="{TEAL}" stroke-width="6"/>
    <rect x="0" y="100" width="130" height="80" rx="10" fill="none" stroke="{TEAL}" stroke-width="6"/>
    <rect x="160" y="100" width="130" height="80" rx="10" fill="none" stroke="{NAVY}" stroke-width="6"/>
    <line x1="20" y1="40" x2="110" y2="40" stroke="{NAVY}" stroke-width="5" opacity="0.4"/>
    <line x1="180" y1="40" x2="270" y2="40" stroke="{TEAL}" stroke-width="5" opacity="0.4"/>
    <line x1="20" y1="140" x2="110" y2="140" stroke="{TEAL}" stroke-width="5" opacity="0.4"/>
    <line x1="180" y1="140" x2="270" y2="140" stroke="{NAVY}" stroke-width="5" opacity="0.4"/>
  </g>''',

    "responsible-gambling-guide": f'''
  <!-- shield with check -->
  <g transform="translate({CX},{CY+15})">
    <path d="M0 -110 L95 -75 L95 5 C95 65 55 105 0 125 C-55 105 -95 65 -95 5 L-95 -75 Z"
          fill="none" stroke="{NAVY}" stroke-width="10" stroke-linejoin="round"/>
    <path d="M-45 -5 L-10 30 L55 -50" fill="none" stroke="{TEAL}" stroke-width="12" stroke-linecap="round" stroke-linejoin="round"/>
  </g>''',

    "sports-betting-glossary": f'''
  <!-- open book -->
  <g transform="translate({CX},{CY+40})">
    <path d="M0 -80 C-50 -105 -130 -100 -160 -85 L-160 70 C-130 55 -50 60 0 80 Z" fill="none" stroke="{NAVY}" stroke-width="8" stroke-linejoin="round"/>
    <path d="M0 -80 C50 -105 130 -100 160 -85 L160 70 C130 55 50 60 0 80 Z" fill="none" stroke="{TEAL}" stroke-width="8" stroke-linejoin="round"/>
    <line x1="-130" y1="-55" x2="-30" y2="-45" stroke="{NAVY}" stroke-width="5" opacity="0.5"/>
    <line x1="-130" y1="-20" x2="-30" y2="-10" stroke="{NAVY}" stroke-width="5" opacity="0.5"/>
    <line x1="30" y1="-45" x2="130" y2="-55" stroke="{TEAL}" stroke-width="5" opacity="0.5"/>
    <line x1="30" y1="-10" x2="130" y2="-20" stroke="{TEAL}" stroke-width="5" opacity="0.5"/>
  </g>''',

    "house-edge-explained": f'''
  <!-- balance scale -->
  <g transform="translate({CX},{CY-30})">
    <line x1="0" y1="-10" x2="0" y2="120" stroke="{NAVY}" stroke-width="10"/>
    <line x1="-120" y1="-10" x2="120" y2="-10" stroke="{NAVY}" stroke-width="8"/>
    <circle cx="0" cy="-10" r="10" fill="{NAVY}"/>
    <path d="M-120 -10 L-160 55 A45 30 0 0 0 -80 55 Z" fill="none" stroke="{TEAL}" stroke-width="7" stroke-linejoin="round"/>
    <path d="M120 -10 L80 65 A55 36 0 0 0 160 65 Z" fill="none" stroke="#b8862b" stroke-width="7" stroke-linejoin="round"/>
    <path d="M-40 120 L40 120 L25 140 L-25 140 Z" fill="{NAVY}"/>
  </g>''',

    "blackjack-basic-strategy": f'''
  <!-- two fanned playing cards -->
  <g transform="translate({CX},{CY+20})">
    <g transform="rotate(-12)">
      <rect x="-60" y="-95" width="120" height="170" rx="12" fill="#fff" stroke="{NAVY}" stroke-width="6"/>
      <text x="-38" y="-55" font-family="Georgia, serif" font-size="34" fill="{NAVY}">A</text>
      <path d="M-38 -25 l6 12 l12 2 l-9 8 l2 12 l-11 -6 l-11 6 l2 -12 l-9 -8 l12 -2 Z" fill="{NAVY}"/>
    </g>
    <g transform="rotate(10)">
      <rect x="-60" y="-95" width="120" height="170" rx="12" fill="#fff" stroke="{TEAL}" stroke-width="6"/>
      <text x="-40" y="-55" font-family="Georgia, serif" font-size="34" fill="{TEAL}">K</text>
      <path d="M-40 -18 l24 24 m0 -24 l-24 24" stroke="{TEAL}" stroke-width="6" stroke-linecap="round"/>
    </g>
  </g>''',
    "fanatics-nfl-sportsbook-deal": f'''
  <!-- megaphone / announcement -->
  <g transform="translate({CX-30},{CY})">
    <path d="M-100 -20 L20 -70 L20 70 L-100 20 Z" fill="none" stroke="{NAVY}" stroke-width="8" stroke-linejoin="round"/>
    <rect x="-130" y="-25" width="32" height="50" rx="6" fill="{TEAL}"/>
    <path d="M20 -70 L110 -95 L110 95 L20 70" fill="none" stroke="{TEAL}" stroke-width="8" stroke-linejoin="round"/>
    <path d="M-70 25 L-55 80 A20 20 0 0 0 -15 80 L-30 20" fill="none" stroke="{NAVY}" stroke-width="7" stroke-linejoin="round"/>
  </g>''',

    "florida-sweepstakes-casino-lawsuit": f'''
  <!-- gavel / regulatory action -->
  <g transform="translate({CX},{CY+10})">
    <g transform="rotate(-35)">
      <rect x="-90" y="-22" width="90" height="44" rx="8" fill="none" stroke="{NAVY}" stroke-width="8"/>
      <rect x="-20" y="-34" width="30" height="68" rx="6" fill="none" stroke="{TEAL}" stroke-width="8"/>
    </g>
    <rect x="-90" y="70" width="180" height="16" rx="4" fill="{NAVY}"/>
    <line x1="-60" y1="70" x2="-60" y2="40" stroke="{NAVY}" stroke-width="8"/>
    <line x1="60" y1="70" x2="60" y2="40" stroke="{TEAL}" stroke-width="8"/>
  </g>''',
}

if __name__ == "__main__":
    os.makedirs(OUT_DIR, exist_ok=True)
    for slug, icon in ICONS.items():
        path = os.path.join(OUT_DIR, f"{slug}.svg")
        with open(path, "w") as f:
            f.write(wrap(icon))
        print("wrote", path)
