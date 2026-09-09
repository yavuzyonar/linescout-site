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

    "nfl-betting-guide": f'''
  <!-- american football -->
  <g transform="translate({CX},{CY})">
    <ellipse cx="0" cy="0" rx="150" ry="78" fill="none" stroke="{NAVY}" stroke-width="9"/>
    <line x1="-55" y1="0" x2="55" y2="0" stroke="{TEAL}" stroke-width="6"/>
    <line x1="-30" y1="-16" x2="-30" y2="16" stroke="{TEAL}" stroke-width="6"/>
    <line x1="-10" y1="-16" x2="-10" y2="16" stroke="{TEAL}" stroke-width="6"/>
    <line x1="10" y1="-16" x2="10" y2="16" stroke="{TEAL}" stroke-width="6"/>
    <line x1="30" y1="-16" x2="30" y2="16" stroke="{TEAL}" stroke-width="6"/>
  </g>''',

    "nfl-player-props-explained": f'''
  <!-- stat clipboard -->
  <g transform="translate({CX-80},{CY-90})">
    <rect x="0" y="24" width="170" height="212" rx="12" fill="none" stroke="{NAVY}" stroke-width="8"/>
    <rect x="50" y="0" width="70" height="34" rx="7" fill="{TEAL}"/>
    <line x1="25" y1="90" x2="145" y2="90" stroke="{NAVY}" stroke-width="7" opacity="0.5"/>
    <line x1="25" y1="128" x2="145" y2="128" stroke="{NAVY}" stroke-width="7" opacity="0.5"/>
    <line x1="25" y1="166" x2="110" y2="166" stroke="{TEAL}" stroke-width="7"/>
    <circle cx="128" cy="166" r="11" fill="none" stroke="{TEAL}" stroke-width="5"/>
  </g>''',

    "nba-betting-guide": f'''
  <!-- basketball -->
  <g transform="translate({CX},{CY})">
    <circle cx="0" cy="0" r="112" fill="none" stroke="{NAVY}" stroke-width="8"/>
    <line x1="-112" y1="0" x2="112" y2="0" stroke="{TEAL}" stroke-width="6"/>
    <line x1="0" y1="-112" x2="0" y2="112" stroke="{TEAL}" stroke-width="6"/>
    <path d="M-79 -79 A112 112 0 0 1 79 79" fill="none" stroke="{TEAL}" stroke-width="6"/>
    <path d="M-79 79 A112 112 0 0 1 79 -79" fill="none" stroke="{TEAL}" stroke-width="6"/>
  </g>''',

    "nba-player-props-injuries-rest": f'''
  <!-- pulse / vitals line -->
  <g transform="translate({CX-150},{CY})">
    <polyline points="0,0 55,0 85,-55 120,55 155,-28 185,0 300,0" fill="none" stroke="{TEAL}" stroke-width="9" stroke-linejoin="round" stroke-linecap="round"/>
    <circle cx="300" cy="0" r="11" fill="{NAVY}"/>
  </g>''',

    "nhl-betting-guide": f'''
  <!-- hockey stick and puck -->
  <g transform="translate({CX-20},{CY+20})">
    <ellipse cx="-60" cy="55" rx="55" ry="17" fill="{NAVY}"/>
    <path d="M110 -100 L45 85 L5 85" fill="none" stroke="{TEAL}" stroke-width="11" stroke-linecap="round" stroke-linejoin="round"/>
    <path d="M5 85 L-25 95" stroke="{TEAL}" stroke-width="11" stroke-linecap="round"/>
  </g>''',

    "nhl-goaltending-betting": f'''
  <!-- goal net -->
  <g transform="translate({CX},{CY-15})">
    <rect x="-120" y="-70" width="240" height="140" fill="none" stroke="{NAVY}" stroke-width="8"/>
    <line x1="-80" y1="-70" x2="-80" y2="70" stroke="{TEAL}" stroke-width="3" opacity="0.55"/>
    <line x1="-40" y1="-70" x2="-40" y2="70" stroke="{TEAL}" stroke-width="3" opacity="0.55"/>
    <line x1="0" y1="-70" x2="0" y2="70" stroke="{TEAL}" stroke-width="3" opacity="0.55"/>
    <line x1="40" y1="-70" x2="40" y2="70" stroke="{TEAL}" stroke-width="3" opacity="0.55"/>
    <line x1="80" y1="-70" x2="80" y2="70" stroke="{TEAL}" stroke-width="3" opacity="0.55"/>
    <line x1="-120" y1="-35" x2="120" y2="-35" stroke="{TEAL}" stroke-width="3" opacity="0.55"/>
    <line x1="-120" y1="0" x2="120" y2="0" stroke="{TEAL}" stroke-width="3" opacity="0.55"/>
    <line x1="-120" y1="35" x2="120" y2="35" stroke="{TEAL}" stroke-width="3" opacity="0.55"/>
    <circle cx="25" cy="12" r="15" fill="{NAVY}"/>
  </g>''',

    "college-football-vs-nfl-betting": f'''
  <!-- pennant flag -->
  <g transform="translate({CX-30},{CY})">
    <line x1="0" y1="-115" x2="0" y2="115" stroke="{NAVY}" stroke-width="11" stroke-linecap="round"/>
    <path d="M0 -105 L165 -60 L0 -15 Z" fill="{TEAL}"/>
  </g>''',

    "college-football-spreads-blowouts": f'''
  <!-- scoreboard -->
  <g transform="translate({CX},{CY-15})">
    <rect x="-145" y="-62" width="290" height="124" rx="10" fill="none" stroke="{NAVY}" stroke-width="8"/>
    <text x="-90" y="22" font-family="Arial" font-size="62" fill="{TEAL}" text-anchor="middle" font-weight="bold">42</text>
    <text x="90" y="22" font-family="Arial" font-size="62" fill="{NAVY}" text-anchor="middle" font-weight="bold">10</text>
    <line x1="0" y1="-62" x2="0" y2="62" stroke="{NAVY}" stroke-width="4" opacity="0.4"/>
  </g>''',

    "nfl-totals-weather-dome-vs-outdoor": f'''
  <!-- stadium roof half-open with a snowflake / wind lines -->
  <g transform="translate({CX},{CY})">
    <path d="M-160 40 A160 120 0 0 1 0 -80" fill="none" stroke="{NAVY}" stroke-width="9" stroke-linecap="round"/>
    <path d="M0 -80 A160 120 0 0 1 160 40" fill="none" stroke="{TEAL}" stroke-width="9" stroke-linecap="round" stroke-dasharray="4 14"/>
    <line x1="-160" y1="40" x2="160" y2="40" stroke="{NAVY}" stroke-width="9" stroke-linecap="round"/>
    <g transform="translate(80,-10)" stroke="{TEAL}" stroke-width="6" stroke-linecap="round">
      <line x1="0" y1="-26" x2="0" y2="26"/>
      <line x1="-22" y1="-13" x2="22" y2="13"/>
      <line x1="-22" y1="13" x2="22" y2="-13"/>
    </g>
    <path d="M-110 -20 q10 -16 20 0 t20 0" fill="none" stroke="{NAVY}" stroke-width="6" opacity="0.55" stroke-linecap="round"/>
    <path d="M-115 5 q10 -16 20 0 t20 0" fill="none" stroke="{NAVY}" stroke-width="6" opacity="0.4" stroke-linecap="round"/>
  </g>''',

    "slot-volatility-explained": f'''
  <!-- volatility waveform: calm line vs spiky line -->
  <g transform="translate({CX-155},{CY-40})">
    <polyline points="0,0 40,0 80,0 120,0 160,0 200,0 240,0 280,0 310,0" fill="none" stroke="{TEAL}" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/>
  </g>
  <g transform="translate({CX-155},{CY+70})">
    <polyline points="0,0 30,0 55,-70 85,50 115,-90 145,60 175,-40 205,20 240,0 310,0" fill="none" stroke="{NAVY}" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/>
  </g>''',

    "ryan-gold-cardinals-second-gambling-investigation": f'''
  <!-- magnifying glass over a document -->
  <g transform="translate({CX-10},{CY})">
    <rect x="-120" y="-110" width="150" height="200" rx="10" fill="none" stroke="{NAVY}" stroke-width="8"/>
    <line x1="-95" y1="-70" x2="-5" y2="-70" stroke="{NAVY}" stroke-width="6" opacity="0.5"/>
    <line x1="-95" y1="-35" x2="-5" y2="-35" stroke="{NAVY}" stroke-width="6" opacity="0.5"/>
    <line x1="-95" y1="0" x2="-30" y2="0" stroke="{NAVY}" stroke-width="6" opacity="0.5"/>
    <circle cx="70" cy="60" r="60" fill="none" stroke="{TEAL}" stroke-width="10"/>
    <line x1="113" y1="103" x2="160" y2="150" stroke="{TEAL}" stroke-width="12" stroke-linecap="round"/>
  </g>''',

    "venetian-nevada-aml-fine-bowyer": f'''
  <!-- gavel over stacked currency -->
  <g transform="translate({CX+10},{CY-25})">
    <g transform="rotate(-35)">
      <rect x="-90" y="-22" width="90" height="44" rx="8" fill="none" stroke="{NAVY}" stroke-width="8"/>
      <rect x="-20" y="-34" width="30" height="68" rx="6" fill="none" stroke="{TEAL}" stroke-width="8"/>
    </g>
  </g>
  <g transform="translate({CX-140},{CY+95})">
    <rect x="0" y="-14" width="150" height="28" rx="6" fill="none" stroke="{NAVY}" stroke-width="6"/>
    <rect x="12" y="-32" width="150" height="28" rx="6" fill="none" stroke="{TEAL}" stroke-width="6"/>
    <text x="87" y="-11" font-family="Arial" font-size="24" fill="{TEAL}" text-anchor="middle">$</text>
  </g>''',

    "college-football-buy-games-early-season-spreads": f'''
  <!-- small pennant vs large pennant across a wide spread number -->
  <g transform="translate({CX-160},{CY+40})">
    <line x1="0" y1="-40" x2="0" y2="40" stroke="{TEAL}" stroke-width="8" stroke-linecap="round"/>
    <path d="M0 -34 L55 -18 L0 -2 Z" fill="{TEAL}"/>
  </g>
  <g transform="translate({CX+140},{CY-10})">
    <line x1="0" y1="-90" x2="0" y2="90" stroke="{NAVY}" stroke-width="11" stroke-linecap="round"/>
    <path d="M0 -80 L120 -45 L0 -10 Z" fill="{NAVY}"/>
  </g>
  <line x1="{CX-90}" y1="{CY+95}" x2="{CX+30}" y2="{CY+95}" stroke="{NAVY}" stroke-width="4" opacity="0.35" stroke-dasharray="2 10"/>''',

    "baccarat-basics-banker-player-tie": f'''
  <!-- two facing cards with a small crown -->
  <g transform="translate({CX},{CY+15})">
    <g transform="translate(-90,0) rotate(-8)">
      <rect x="-55" y="-90" width="110" height="160" rx="12" fill="#fff" stroke="{NAVY}" stroke-width="6"/>
      <text x="-30" y="-48" font-family="Georgia, serif" font-size="30" fill="{NAVY}">9</text>
    </g>
    <g transform="translate(90,0) rotate(8)">
      <rect x="-55" y="-90" width="110" height="160" rx="12" fill="#fff" stroke="{TEAL}" stroke-width="6"/>
      <text x="-30" y="-48" font-family="Georgia, serif" font-size="30" fill="{TEAL}">8</text>
    </g>
    <path d="M-24 -140 L-14 -118 L0 -134 L14 -118 L24 -140 L18 -108 L-18 -108 Z" fill="#b8862b"/>
  </g>''',

    "kalshi-red-sox-massachusetts-prediction-market-fight": f'''
  <!-- stadium pennant beside a small gavel -->
  <g transform="translate({CX-110},{CY+10})">
    <line x1="0" y1="-95" x2="0" y2="95" stroke="{NAVY}" stroke-width="10" stroke-linecap="round"/>
    <path d="M0 -85 L140 -50 L0 -15 Z" fill="{TEAL}"/>
  </g>
  <g transform="translate({CX+130},{CY-10})">
    <g transform="rotate(-35)">
      <rect x="-70" y="-18" width="70" height="36" rx="7" fill="none" stroke="{NAVY}" stroke-width="7"/>
      <rect x="-16" y="-27" width="24" height="54" rx="5" fill="none" stroke="{TEAL}" stroke-width="7"/>
    </g>
    <rect x="-70" y="55" width="140" height="13" rx="4" fill="{NAVY}"/>
  </g>''',

    "caesars-olympus-1-5-million-loyalty-tier": f'''
  <!-- laurel wreath around a loyalty card -->
  <g transform="translate({CX},{CY+10})">
    <rect x="-100" y="-60" width="200" height="120" rx="14" fill="none" stroke="{NAVY}" stroke-width="9"/>
    <circle cx="0" cy="0" r="34" fill="none" stroke="#b8862b" stroke-width="6"/>
    <text x="0" y="9" font-family="Arial" font-size="26" fill="#b8862b" text-anchor="middle">$</text>
    <path d="M-100 -100 C-140 -70 -150 -20 -120 20" fill="none" stroke="{TEAL}" stroke-width="7" stroke-linecap="round"/>
    <path d="M100 -100 C140 -70 150 -20 120 20" fill="none" stroke="{TEAL}" stroke-width="7" stroke-linecap="round"/>
  </g>''',

    "nfl-alternate-spreads-totals-pricing": f'''
  <!-- ladder of alternate-line rungs, one highlighted as the main line -->
  <g transform="translate({CX-150},{CY-90})">
    <line x1="0" y1="0" x2="300" y2="0" stroke="{NAVY}" stroke-width="2" opacity="0.35"/>
    <line x1="40" y1="40" x2="260" y2="40" stroke="{NAVY}" stroke-width="2" opacity="0.35"/>
    <line x1="10" y1="80" x2="290" y2="80" stroke="{TEAL}" stroke-width="9" stroke-linecap="round"/>
    <circle cx="150" cy="80" r="10" fill="#b8862b"/>
    <line x1="55" y1="120" x2="245" y2="120" stroke="{NAVY}" stroke-width="2" opacity="0.35"/>
    <line x1="20" y1="160" x2="280" y2="160" stroke="{NAVY}" stroke-width="2" opacity="0.35"/>
    <path d="M150 -30 L150 210" stroke="{NAVY}" stroke-width="4" stroke-dasharray="2 10" opacity="0.4"/>
  </g>''',

    "blackjack-side-bets-house-edge": f'''
  <!-- main card plus a smaller fanned side card with a percent mark -->
  <g transform="translate({CX-40},{CY+10})">
    <rect x="-70" y="-100" width="130" height="185" rx="12" fill="#fff" stroke="{NAVY}" stroke-width="7"/>
    <text x="-46" y="-58" font-family="Georgia, serif" font-size="32" fill="{NAVY}">Q</text>
  </g>
  <g transform="translate({CX+110},{CY+55}) rotate(18)">
    <rect x="-46" y="-72" width="92" height="130" rx="10" fill="#fff" stroke="{TEAL}" stroke-width="6"/>
    <circle cx="-16" cy="-30" r="9" fill="none" stroke="{TEAL}" stroke-width="5"/>
    <circle cx="16" cy="12" r="9" fill="none" stroke="{TEAL}" stroke-width="5"/>
    <line x1="-20" y1="18" x2="20" y2="-36" stroke="{TEAL}" stroke-width="5"/>
  </g>''',

    "ninth-circuit-kalshi-nevada-scotus": f'''
  <!-- scale of justice with a forked path beneath, representing a circuit split -->
  <g transform="translate({CX},{CY-30})">
    <line x1="0" y1="-30" x2="0" y2="90" stroke="{NAVY}" stroke-width="10"/>
    <line x1="-110" y1="-30" x2="110" y2="-30" stroke="{NAVY}" stroke-width="7"/>
    <circle cx="0" cy="-30" r="9" fill="{NAVY}"/>
    <path d="M-110 -30 L-145 30 A40 26 0 0 0 -75 30 Z" fill="none" stroke="{TEAL}" stroke-width="6" stroke-linejoin="round"/>
    <path d="M110 -30 L75 30 A40 26 0 0 0 145 30 Z" fill="none" stroke="#b8862b" stroke-width="6" stroke-linejoin="round"/>
  </g>
  <g transform="translate({CX},{CY+110})" stroke="{NAVY}" stroke-width="6" fill="none" stroke-linecap="round">
    <path d="M0 -20 L0 0"/>
    <path d="M0 0 L-55 40"/>
    <path d="M0 0 L55 40"/>
  </g>''',

    "ontario-igaming-record-july-2026": f'''
  <!-- ascending bar chart topped with a small maple-leaf accent mark -->
  <g transform="translate({CX-140},{CY+70})">
    <rect x="0" y="-50" width="42" height="50" rx="6" fill="{TEAL}" opacity="0.55"/>
    <rect x="64" y="-85" width="42" height="85" rx="6" fill="{TEAL}" opacity="0.75"/>
    <rect x="128" y="-125" width="42" height="125" rx="6" fill="{NAVY}"/>
    <rect x="192" y="-170" width="42" height="170" rx="6" fill="{TEAL}"/>
    <path d="M213 -215 l7 14 l15 2 l-11 11 l3 15 l-14 -8 l-14 8 l3 -15 l-11 -11 l15 -2 Z" fill="#b8862b"/>
  </g>''',
    "nba-home-road-back-to-back-scheduling": f'''
  <!-- basketball beside a travel/calendar rest icon -->
  <g transform="translate({CX-90},{CY})">
    <circle cx="0" cy="0" r="95" fill="none" stroke="{NAVY}" stroke-width="8"/>
    <line x1="-95" y1="0" x2="95" y2="0" stroke="{TEAL}" stroke-width="5"/>
    <line x1="0" y1="-95" x2="0" y2="95" stroke="{TEAL}" stroke-width="5"/>
    <path d="M-67 -67 A95 95 0 0 1 67 67" fill="none" stroke="{TEAL}" stroke-width="5"/>
    <path d="M-67 67 A95 95 0 0 1 67 -67" fill="none" stroke="{TEAL}" stroke-width="5"/>
  </g>
  <g transform="translate({CX+130},{CY-30})">
    <rect x="-55" y="-40" width="110" height="100" rx="10" fill="none" stroke="{NAVY}" stroke-width="7"/>
    <line x1="-55" y1="-14" x2="55" y2="-14" stroke="{NAVY}" stroke-width="6"/>
    <line x1="-28" y1="-52" x2="-28" y2="-28" stroke="{TEAL}" stroke-width="6" stroke-linecap="round"/>
    <line x1="28" y1="-52" x2="28" y2="-28" stroke="{TEAL}" stroke-width="6" stroke-linecap="round"/>
    <circle cx="-16" cy="16" r="7" fill="{TEAL}"/>
    <circle cx="16" cy="16" r="7" fill="{TEAL}" opacity="0.4"/>
    <circle cx="-16" cy="40" r="7" fill="{TEAL}" opacity="0.4"/>
  </g>''',

    "slot-hit-frequency-vs-rtp": f'''
  <!-- slot reel beside a percentage gauge -->
  <g transform="translate({CX-100},{CY})">
    <rect x="-70" y="-90" width="140" height="180" rx="14" fill="none" stroke="{NAVY}" stroke-width="8"/>
    <line x1="-23" y1="-90" x2="-23" y2="90" stroke="{NAVY}" stroke-width="3" opacity="0.4"/>
    <line x1="23" y1="-90" x2="23" y2="90" stroke="{NAVY}" stroke-width="3" opacity="0.4"/>
    <circle cx="-46" cy="-30" r="14" fill="none" stroke="{TEAL}" stroke-width="5"/>
    <path d="M-9 -45 L9 -15 M9 -45 L-9 -15" stroke="{TEAL}" stroke-width="5" stroke-linecap="round"/>
    <path d="M35 -45 L58 15" stroke="{TEAL}" stroke-width="5" stroke-linecap="round"/>
    <circle cx="35" cy="-45" r="7" fill="{TEAL}"/>
    <circle cx="58" cy="15" r="7" fill="{TEAL}"/>
  </g>
  <g transform="translate({CX+130},{CY+15})">
    <path d="M -70 15 A 70 70 0 0 1 70 15" fill="none" stroke="{NAVY}" stroke-width="12" stroke-linecap="round"/>
    <path d="M -70 15 A 70 70 0 0 1 -5 -69" fill="none" stroke="#b8862b" stroke-width="12" stroke-linecap="round"/>
  </g>''',

    "fanduel-vip-program-congressional-inquiry": f'''
  <!-- document with magnifying glass, congressional inquiry -->
  <g transform="translate({CX-20},{CY})">
    <rect x="-120" y="-110" width="150" height="200" rx="10" fill="none" stroke="{NAVY}" stroke-width="8"/>
    <line x1="-95" y1="-70" x2="-5" y2="-70" stroke="{NAVY}" stroke-width="6" opacity="0.5"/>
    <line x1="-95" y1="-35" x2="-5" y2="-35" stroke="{NAVY}" stroke-width="6" opacity="0.5"/>
    <line x1="-95" y1="0" x2="-30" y2="0" stroke="{NAVY}" stroke-width="6" opacity="0.5"/>
    <circle cx="70" cy="60" r="60" fill="none" stroke="{TEAL}" stroke-width="10"/>
    <line x1="113" y1="103" x2="160" y2="150" stroke="{TEAL}" stroke-width="12" stroke-linecap="round"/>
  </g>''',

    "maverick-gaming-tukwila-casino-closures": f'''
  <!-- building outline with a closed sign -->
  <g transform="translate({CX},{CY+10})">
    <path d="M-110 90 L-110 -20 L0 -95 L110 -20 L110 90 Z" fill="none" stroke="{NAVY}" stroke-width="8" stroke-linejoin="round"/>
    <line x1="-110" y1="90" x2="110" y2="90" stroke="{NAVY}" stroke-width="8"/>
    <rect x="-40" y="10" width="80" height="80" fill="none" stroke="{TEAL}" stroke-width="6"/>
    <line x1="-40" y1="50" x2="40" y2="50" stroke="{TEAL}" stroke-width="4" opacity="0.5"/>
    <g transform="translate(55,-55) rotate(-18)">
      <rect x="-45" y="-18" width="90" height="36" rx="6" fill="#b8862b"/>
      <line x1="-45" y1="0" x2="45" y2="0" stroke="{NAVY}" stroke-width="3" opacity="0.5"/>
    </g>
  </g>''',

    "arbitrage-betting-explained": f'''
  <!-- two overlapping circles (two sportsbooks) with a dollar sign in the shared middle -->
  <g transform="translate({CX},{CY})">
    <circle cx="-75" cy="0" r="115" fill="none" stroke="{NAVY}" stroke-width="8"/>
    <circle cx="75" cy="0" r="115" fill="none" stroke="{TEAL}" stroke-width="8"/>
    <circle cx="0" cy="0" r="30" fill="none" stroke="#b8862b" stroke-width="6"/>
    <text x="0" y="9" font-family="Arial" font-size="26" fill="#b8862b" text-anchor="middle">$</text>
  </g>''',

    "continuous-shuffling-machines-blackjack": f'''
  <!-- shuffling machine: a card slot box with cards cycling through via circular arrows -->
  <g transform="translate({CX},{CY})">
    <rect x="-95" y="-70" width="190" height="140" rx="16" fill="none" stroke="{NAVY}" stroke-width="8"/>
    <rect x="-46" y="-98" width="92" height="46" rx="8" fill="#fff" stroke="{TEAL}" stroke-width="6"/>
    <path d="M-60 40 A60 60 0 1 1 40 78" fill="none" stroke="{TEAL}" stroke-width="7" stroke-linecap="round"/>
    <path d="M30 65 L40 78 L52 62" fill="none" stroke="{TEAL}" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>
  </g>''',

    "new-jersey-supreme-court-kalshi-petition": f'''
  <!-- courthouse columns beneath a scale, with an upward arrow toward a higher court -->
  <g transform="translate({CX},{CY+25})">
    <line x1="-120" y1="60" x2="120" y2="60" stroke="{NAVY}" stroke-width="9" stroke-linecap="round"/>
    <path d="M-130 20 L0 -55 L130 20 Z" fill="none" stroke="{NAVY}" stroke-width="8" stroke-linejoin="round"/>
    <line x1="-85" y1="20" x2="-85" y2="60" stroke="{TEAL}" stroke-width="8"/>
    <line x1="-28" y1="20" x2="-28" y2="60" stroke="{TEAL}" stroke-width="8"/>
    <line x1="28" y1="20" x2="28" y2="60" stroke="{TEAL}" stroke-width="8"/>
    <line x1="85" y1="20" x2="85" y2="60" stroke="{TEAL}" stroke-width="8"/>
  </g>
  <g transform="translate({CX+140},{CY-70})" stroke="#b8862b" stroke-width="8" fill="none" stroke-linecap="round" stroke-linejoin="round">
    <line x1="0" y1="35" x2="0" y2="-35"/>
    <path d="M-18 -15 L0 -35 L18 -15"/>
  </g>''',

    "encore-boston-harbor-casino-strike": f'''
  <!-- casino building outline with a raised picket sign -->
  <g transform="translate({CX-35},{CY+10})">
    <path d="M-100 85 L-100 -15 L0 -85 L100 -15 L100 85 Z" fill="none" stroke="{NAVY}" stroke-width="8" stroke-linejoin="round"/>
    <line x1="-100" y1="85" x2="100" y2="85" stroke="{NAVY}" stroke-width="8"/>
    <rect x="-38" y="5" width="76" height="80" fill="none" stroke="{TEAL}" stroke-width="6"/>
    <line x1="-38" y1="45" x2="38" y2="45" stroke="{TEAL}" stroke-width="4" opacity="0.5"/>
  </g>
  <g transform="translate({CX+130},{CY-30})" stroke="{NAVY}" stroke-width="7" stroke-linecap="round">
    <line x1="0" y1="60" x2="0" y2="-60"/>
    <rect x="-45" y="-95" width="90" height="42" rx="6" fill="#b8862b" stroke="none"/>
  </g>''',

    "nba-playoff-series-betting-vs-regular-season": f'''
  <!-- basketball with a row of 7 series-game dots beneath, four filled -->
  <g transform="translate({CX-30},{CY-40})">
    <circle cx="0" cy="0" r="88" fill="none" stroke="{NAVY}" stroke-width="8"/>
    <line x1="-88" y1="0" x2="88" y2="0" stroke="{TEAL}" stroke-width="5"/>
    <line x1="0" y1="-88" x2="0" y2="88" stroke="{TEAL}" stroke-width="5"/>
    <path d="M-62 -62 A88 88 0 0 1 62 62" fill="none" stroke="{TEAL}" stroke-width="5"/>
    <path d="M-62 62 A88 88 0 0 1 62 -62" fill="none" stroke="{TEAL}" stroke-width="5"/>
  </g>
  <g transform="translate({CX-121},{CY+110})">
    <circle cx="0" cy="0" r="12" fill="{NAVY}"/>
    <circle cx="35" cy="0" r="12" fill="{NAVY}"/>
    <circle cx="70" cy="0" r="12" fill="{NAVY}"/>
    <circle cx="105" cy="0" r="12" fill="{NAVY}"/>
    <circle cx="140" cy="0" r="12" fill="none" stroke="{NAVY}" stroke-width="4" opacity="0.4"/>
    <circle cx="175" cy="0" r="12" fill="none" stroke="{NAVY}" stroke-width="4" opacity="0.4"/>
    <circle cx="210" cy="0" r="12" fill="none" stroke="{NAVY}" stroke-width="4" opacity="0.4"/>
  </g>''',

    "slot-rtp-variants-across-casinos": f'''
  <!-- single slot reel splitting into two diverging paths tagged with different percentages -->
  <g transform="translate({CX-150},{CY-10})">
    <rect x="-55" y="-75" width="110" height="150" rx="14" fill="none" stroke="{NAVY}" stroke-width="8"/>
    <line x1="-18" y1="-75" x2="-18" y2="75" stroke="{NAVY}" stroke-width="3" opacity="0.4"/>
    <line x1="18" y1="-75" x2="18" y2="75" stroke="{NAVY}" stroke-width="3" opacity="0.4"/>
  </g>
  <path d="M{CX-90} {CY-10} C {CX-10} {CY-10} {CX-10} {CY-80} {CX+90} {CY-80}" fill="none" stroke="{TEAL}" stroke-width="6" stroke-linecap="round"/>
  <path d="M{CX-90} {CY-10} C {CX-10} {CY-10} {CX-10} {CY+70} {CX+90} {CY+70}" fill="none" stroke="#b8862b" stroke-width="6" stroke-linecap="round"/>
  <text x="{CX+95}" y="{CY-73}" font-family="Arial" font-size="30" fill="{TEAL}" font-weight="bold">97%</text>
  <text x="{CX+95}" y="{CY+77}" font-family="Arial" font-size="30" fill="#b8862b" font-weight="bold">94%</text>''',

    "bet365-washington-dc-launch": f'''
  <!-- map pin marking a new-market launch, with a small betting-ticket check -->
  <g transform="translate({CX-20},{CY-30})">
    <path d="M0 -110 C60 -110 100 -68 100 -18 C100 55 0 130 0 130 C0 130 -100 55 -100 -18 C-100 -68 -60 -110 0 -110 Z" fill="none" stroke="{NAVY}" stroke-width="8" stroke-linejoin="round"/>
    <circle cx="0" cy="-15" r="42" fill="none" stroke="{TEAL}" stroke-width="8"/>
    <path d="M-20 -15 L-5 0 L25 -35" fill="none" stroke="{TEAL}" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/>
  </g>
  <circle cx="{CX+140}" cy="{CY-90}" r="9" fill="#b8862b"/>''',

    "clairvest-mgm-springfield-sale-report": f'''
  <!-- building outline with a curved ownership-transfer arrow overhead -->
  <g transform="translate({CX},{CY+15})">
    <path d="M-100 80 L-100 -25 L0 -95 L100 -25 L100 80 Z" fill="none" stroke="{NAVY}" stroke-width="8" stroke-linejoin="round"/>
    <line x1="-100" y1="80" x2="100" y2="80" stroke="{NAVY}" stroke-width="8"/>
    <rect x="-38" y="0" width="76" height="80" fill="none" stroke="{TEAL}" stroke-width="6"/>
    <line x1="-38" y1="40" x2="38" y2="40" stroke="{TEAL}" stroke-width="4" opacity="0.5"/>
  </g>
  <g transform="translate({CX},{CY-90})" fill="none" stroke="#b8862b" stroke-width="7" stroke-linecap="round">
    <path d="M-95 10 A95 45 0 0 1 95 10"/>
    <path d="M78 -8 L95 10 L74 22"/>
  </g>''',
}

if __name__ == "__main__":
    os.makedirs(OUT_DIR, exist_ok=True)
    for slug, icon in ICONS.items():
        path = os.path.join(OUT_DIR, f"{slug}.svg")
        with open(path, "w") as f:
            f.write(wrap(icon))
        print("wrote", path)
