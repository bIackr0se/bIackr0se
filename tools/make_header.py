"""Build assets/header.svg: the portfolio palette, fonts and rose curve.

Run: python3 tools/make_header.py tools/fonts assets/header.svg
The fonts are subsets of Archivo and IBM Plex Mono (SIL OFL, licences beside them).
"""
import base64, math, sys
from pathlib import Path

here = Path(sys.argv[1]); out = Path(sys.argv[2])
b64 = lambda f: base64.b64encode((here / f).read_bytes()).decode()
W, H = 1280, 300

def rose(k_num, k_den, R, cx, cy, steps=2400):
    # r = R cos(k theta), k = n/d, closes after pi*d (n*d odd) or 2*pi*d
    turns = k_den * (1 if (k_num * k_den) % 2 else 2)
    pts = []
    for i in range(steps + 1):
        t = math.pi * turns * i / steps
        r = R * math.cos(k_num / k_den * t)
        pts.append(f"{cx + r * math.cos(t):.1f},{cy + r * math.sin(t):.1f}")
    return "M" + " L".join(pts)

cx, cy = 1120, 150
outer = rose(5, 4, 122, cx, cy)
inner = rose(5, 1, 62, cx, cy, 900)

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="Jaafer Rahmani. AI red teaming and security engineering.">
<style>
@font-face {{ font-family: "Archivo"; src: url(data:font/woff2;base64,{b64("archivo-sub.woff2")}) format("woff2"); font-weight: 100 900; font-stretch: 62% 125%; }}
@font-face {{ font-family: "Plex"; src: url(data:font/woff2;base64,{b64("plex-sub.woff2")}) format("woff2"); }}
.name {{ font: 800 86px "Archivo", "Arial Black", sans-serif; font-stretch: 112.5%; letter-spacing: -0.015em; fill: #ece7de; }}
.kick {{ font: 400 25px "Plex", ui-monospace, monospace; letter-spacing: 0.18em; fill: #ff2a4d; }}
.sub {{ font: 400 31px "Plex", ui-monospace, monospace; letter-spacing: 0.1em; fill: #9a938a; }}
.slash {{ fill: #ff2a4d; }}
.curve {{ fill: none; stroke: #ff2a4d; stroke-linejoin: round; stroke-linecap: round; }}
.outer {{ stroke-width: 1.1; stroke-opacity: .55; stroke-dasharray: 9000; stroke-dashoffset: 9000; animation: draw 7s cubic-bezier(.4,0,.2,1) .3s forwards; }}
.inner {{ stroke-width: 1.6; stroke-opacity: .9; stroke-dasharray: 2400; stroke-dashoffset: 2400; animation: draw 4.5s cubic-bezier(.4,0,.2,1) 1.2s forwards; }}
.spin {{ transform-origin: {cx}px {cy}px; animation: spin 120s linear infinite; }}
.cursor {{ animation: blink 1.1s steps(1) infinite; }}
@keyframes draw {{ to {{ stroke-dashoffset: 0; }} }}
@keyframes spin {{ to {{ transform: rotate(360deg); }} }}
@keyframes blink {{ 50% {{ opacity: 0; }} }}
@media (prefers-reduced-motion: reduce) {{ .outer, .inner {{ animation: none; stroke-dashoffset: 0; }} .spin, .cursor {{ animation: none; }} }}
</style>
<defs>
<radialGradient id="glow" cx="{cx}" cy="{cy}" r="190" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#ff2a4d" stop-opacity=".16"/><stop offset="1" stop-color="#ff2a4d" stop-opacity="0"/></radialGradient>
<pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse"><path d="M40 0H0V40" fill="none" stroke="#e8e4dd" stroke-opacity=".045"/></pattern>
<clipPath id="card"><rect width="{W}" height="{H}" rx="14"/></clipPath>
</defs>
<g clip-path="url(#card)">
<rect width="{W}" height="{H}" fill="#060407"/>
<rect width="{W}" height="{H}" fill="url(#grid)"/>
<circle cx="{cx}" cy="{cy}" r="190" fill="url(#glow)"/>
<g class="spin"><path class="curve outer" d="{outer}"/></g>
<path class="curve inner" d="{inner}"/>
<circle cx="{cx}" cy="{cy}" r="3.2" fill="#ff2a4d"/>
<text class="kick" x="72" y="96">// bIackr0se<tspan class="cursor">_</tspan></text>
<text class="name" x="68" y="184">JAAFER RAHMANI</text>
<text class="sub" x="72" y="240">AI RED TEAMING <tspan class="slash">//</tspan> SECURITY ENGINEERING</text>
<rect x="0" y="{H-3}" width="{W}" height="3" fill="#ff2a4d" fill-opacity=".85"/>
</g>
<rect x=".5" y=".5" width="{W-1}" height="{H-1}" rx="14" fill="none" stroke="#ff2a4d" stroke-opacity=".16"/>
</svg>'''
out.write_text(svg)
import os
if os.environ.get("STATIC"):
    svg = svg.replace("animation: draw", "animation-name: none; --x: draw").replace("stroke-dashoffset: 9000", "stroke-dashoffset: 0").replace("stroke-dashoffset: 2400", "stroke-dashoffset: 0")
    out.write_text(svg)
print(out, len(svg.encode()), "bytes")
