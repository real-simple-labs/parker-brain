#!/usr/bin/env python3
"""Render a weekly creative report from its data file into one HTML page.

    python3 render_report.py report-data.json report.html [--embed-images] [--pdf]

The data file follows report-schema.md in this folder. Charts are inline SVG and
there is no chart library or script, so the file opens the same way in a browser,
an email attachment, or a shared drive. The only outside request is the Parker
typefaces (Fraunces and DM Sans) from Google Fonts; offline, the page falls back
to the system's serif and sans and still looks right.

The look follows the Parker V2 visual direction: a light canvas with soft prism
washes, frosted glass panels with 24px corners and no shadows, Fraunces 300 for
display moments, DM Sans for everything else, and dark glass play buttons over
video.

Every ad on the page links to its public media (the video or image file Parker
stores), so a reader can click any ad name or thumbnail and see the actual ad
with no login.

--embed-images  inlines each thumbnail so the report keeps its pictures however
                it's shared. Statics use their own image. Video ads get a frame
                pulled from the video with ffmpeg when it's installed; without
                it the page shows the video's first frame live in the browser,
                and a labeled placeholder in print.
--pdf           also writes report.pdf next to the HTML when Chrome, Chromium, or
                Edge is installed. Otherwise it says so and the HTML stands.

Standard library only, so it runs anywhere python3 does.
"""

import base64
from decimal import Decimal
import html
import ipaddress
import json
import math
import os
import shutil
import socket
import subprocess
import sys
import urllib.error
import urllib.request
from urllib.parse import urlsplit

SECTION_ORDER = [
    "headline",
    "scorecard",
    "trend",
    "top_creatives",
    "launches",
    "watch_list",
    "format_mix",
    "insights",
    "next_week",
    "all_ads",
]

# Chart colors come from the validated default palette (dataviz skill); the glass
# and prism washes are page chrome and never carry data. The page is light only
# on purpose: a report that gets forwarded and printed should look the same on
# every screen and match its PDF.
SERIES_1 = "#2a78d6"
SPARK_GRAY = "#b5b3ad"

FONTS = ("https://fonts.googleapis.com/css2?family=DM+Sans:opsz,wght@9..40,400;9..40,500;"
         "9..40,600;9..40,700&family=Fraunces:opsz,wght@9..144,300;9..144,400&display=swap")


def esc(value):
    return html.escape("" if value is None else str(value), quote=True)


# ---------------------------------------------------------------- formatting

def compact(n):
    """Short enough for a tile, exact enough for an exec: 1,534 / 48.2K / 215.4K / 1.2M."""
    a = abs(n)
    if a >= 1_000_000:
        return f"{n / 1_000_000:.1f}M".replace(".0M", "M")
    if a >= 10_000:
        return f"{n / 1_000:.1f}K".replace(".0K", "K")
    return f"{n:,.0f}"


def exact(d, min_dp=0):
    """A Decimal written out in full: thousands commas, every digit it has, at least min_dp decimals."""
    d = d.normalize()
    text = format(d, "f")
    sign = "-" if text.startswith("-") else ""
    text = text.lstrip("-")
    whole, _, frac = text.partition(".")
    frac = frac.ljust(min_dp, "0")
    return f"{sign}{int(whole):,}" + (f".{frac}" if frac else "")


class ExactFloat(float):
    """A number from the data file that remembers exactly how it was written.
    It does math like any float (charts, deltas), but formatting reads its
    original text, so 1.23456789012345678 prints with every digit."""

    def __new__(cls, text):
        number = super().__new__(cls, text)
        number.text = text
        return number


def to_decimal(value):
    """The value as an exact Decimal, or None if it isn't a usable number.
    Whole numbers go in as-is (no float step that could change a big one);
    floats go in by their shortest exact form; NaN and infinity are rejected."""
    if isinstance(value, bool) or value is None:
        return None
    try:
        if isinstance(value, ExactFloat):
            d = Decimal(value.text)
        elif isinstance(value, int):
            d = Decimal(value)
        else:
            d = Decimal(repr(float(value)))
    except (TypeError, ValueError, ArithmeticError):
        return None
    return d if d.is_finite() else None


def calc_percent(fraction):
    """A share or rate Parker calculated, which can carry float noise
    (0.30000000000000004): shown to two decimals, the rule for calculated numbers."""
    d = to_decimal(fraction)
    if d is None:
        return "n/a"
    return exact((d * 100).quantize(Decimal("0.01")), 0) + "%"


def fmt(value, kind, currency="$", full=False):
    """Format one number by its kind, exactly as it was pulled. The report never
    rounds or shortens a number (no 48.2K): a team checks these against Ads Manager.
    `full` is kept for callers; every number is already full."""
    d = to_decimal(value)
    if d is None:
        return "n/a" if value is None or isinstance(value, (int, float)) else str(value)
    if kind == "currency":
        return f"{currency}{exact(d, 2)}"
    if kind == "ratio":
        return f"{exact(d, 2)}x"
    if kind == "percent":
        return f"{exact(d * 100)}%"
    if kind == "decimal":
        return exact(d, 2)
    return exact(d)


def delta_parts(kpi):
    """Return (text, tone, arrow) for a KPI's change against the prior week."""
    value, prior = kpi.get("value"), kpi.get("prior")
    if value is None or prior in (None, 0):
        return None
    kind = kpi.get("format", "number")
    # A change is calculated, not pulled, so it can run on forever (50.4134...%).
    # It's the one number shown to two decimals.
    if kind == "percent":
        change = (value - prior) * 100
        text = f"{change:+.2f} pts"
    else:
        change = (value - prior) / abs(prior) * 100
        text = f"{change:+.2f}%"
    if abs(change) < 0.005:
        return ("Flat vs last week", "neutral", "&#9654;")
    direction = kpi.get("good_direction", "up")
    up = change > 0
    if direction == "neutral":
        tone = "neutral"
    else:
        tone = "good" if (up == (direction == "up")) else "bad"
    arrow = "&#9650;" if up else "&#9660;"
    return (f"{text} vs last week", tone, arrow)


def nice_ticks(lo, hi, count=4):
    """Clean axis steps (0 / 20K / 40K, or 2.2x / 2.4x / 2.6x) that cover lo..hi."""
    if hi <= lo:
        hi = lo + (abs(lo) or 1)
    raw = (hi - lo) / count
    exp = 10 ** math.floor(math.log10(raw))
    step = next(m * exp for m in (1, 2, 2.5, 5, 10) if m * exp >= raw)
    start = math.floor(lo / step) * step
    ticks = [start]
    while ticks[-1] < hi - 1e-9:
        ticks.append(ticks[-1] + step)
    return ticks


def tick_label(v, kind, currency):
    if kind == "currency":
        return f"{currency}{compact(v)}" if abs(v) >= 1000 else f"{currency}{v:,.0f}"
    if kind == "ratio":
        return f"{v:.1f}x" if abs(v * 10 - round(v * 10)) < 1e-9 else f"{v:.2f}x"
    if kind == "percent":
        return f"{v * 100:.0f}%" if abs(v * 100 - round(v * 100)) < 1e-9 else f"{v * 100:.1f}%"
    return compact(v)


# ---------------------------------------------------------------- ad media

def is_video(item):
    kind = (item.get("media_type") or "").lower()
    if kind:
        return kind == "video"
    url = (item.get("media_url") or "").lower().split("?")[0]
    return url.endswith((".mp4", ".mov", ".webm", ".m4v"))


# ---------------------------------------------------------------- safe urls
# The data file is written by Parker from its own pulls, but the page is shared
# and the renderer runs on a team's own machine, so treat every address in it
# as untrusted: links must be http(s), and downloads must reach the public
# internet, never this machine or a private network.

def safe_url(url):
    """The address if it's http(s), otherwise "" so nothing links to it."""
    if not isinstance(url, str):
        return ""
    url = url.strip()
    try:
        scheme = urlsplit(url).scheme.lower()
    except ValueError:
        return ""
    return url if scheme in ("http", "https") else ""


def safe_src(url):
    """An image source: an inline image, or a safe http(s) address."""
    if isinstance(url, str) and url.startswith("data:image/"):
        return url
    return safe_url(url)


def public_host(url):
    """True only when every address the host resolves to is on the public internet."""
    try:
        host = urlsplit(url).hostname
        if not host:
            return False
        infos = socket.getaddrinfo(host, None)
        addresses = {ipaddress.ip_address(info[4][0].split("%")[0]) for info in infos}
    except (ValueError, OSError):
        return False
    return bool(addresses) and all(a.is_global for a in addresses)


def fetchable(url):
    return bool(safe_url(url)) and public_host(url)


class _PublicRedirects(urllib.request.HTTPRedirectHandler):
    """Recheck every redirect, so a public address can't bounce us somewhere private."""

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        if not fetchable(newurl):
            raise urllib.error.URLError("redirected to a non-public address")
        return super().redirect_request(req, fp, code, msg, headers, newurl)


_OPENER = urllib.request.build_opener(_PublicRedirects)


def ad_link(item):
    """Where an ad's name and thumbnail point: its public media first."""
    return safe_url(item.get("media_url")) or safe_url(item.get("link"))


def placeholder_thumb(label, video=False):
    text = esc((label or "Creative")[:18])
    # A video's play button sits on top of the thumbnail, so its placeholder
    # carries no icon of its own.
    icon = ("" if video else
            "<rect x='150' y='190' width='100' height='80' rx='10' fill='none' stroke='#9a98a8' stroke-width='6'/>"
            "<circle cx='178' cy='218' r='10' fill='#9a98a8'/>"
            "<path d='M156 262 l30-28 22 18 16-12 22 22z' fill='#9a98a8'/>")
    svg = (
        "<svg xmlns='http://www.w3.org/2000/svg' width='400' height='500' viewBox='0 0 400 500'>"
        "<defs><linearGradient id='g' x1='0' y1='0' x2='1' y2='1'>"
        "<stop offset='0' stop-color='#ece9f7'/><stop offset='1' stop-color='#e3eef6'/></linearGradient></defs>"
        f"<rect width='400' height='500' fill='url(#g)'/>{icon}"
        f"<text x='200' y='{330 if video else 320}' font-family='system-ui,sans-serif' font-size='22' fill='#7d7b8c' text-anchor='middle'>{text}</text>"
        "</svg>"
    )
    return "data:image/svg+xml;base64," + base64.b64encode(svg.encode()).decode()


def fetch_image(url):
    if not fetchable(url):
        return None
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with _OPENER.open(req, timeout=15) as resp:
            ctype = resp.headers.get_content_type()
            if not ctype.startswith("image/"):
                return None
            data = resp.read(8_000_000)
        return f"data:{ctype};base64," + base64.b64encode(data).decode()
    except Exception:
        return None


def video_frame(url):
    """Pull one frame a second in, as a JPEG data URI. None if ffmpeg isn't here."""
    ffmpeg = shutil.which("ffmpeg")
    if not ffmpeg or not fetchable(url):
        return None
    try:
        # The whitelist keeps ffmpeg on the web: no local files, no other protocols.
        out = subprocess.run(
            [ffmpeg, "-v", "error", "-protocol_whitelist", "http,https,tls,tcp",
             "-ss", "1", "-i", url, "-frames:v", "1",
             "-vf", "scale=540:-2", "-f", "image2", "-c:v", "mjpeg", "pipe:1"],
            capture_output=True, timeout=45, check=True,
        ).stdout
        return "data:image/jpeg;base64," + base64.b64encode(out).decode() if out else None
    except Exception:
        return None


_FRAMES = {}


def media_html(item, ctx):
    """The ad's picture: an embedded image, a live first frame, or a placeholder."""
    video = is_video(item)
    alt = esc(item.get("name"))
    thumb = safe_src(item.get("thumbnail"))
    media = safe_url(item.get("media_url"))
    if not thumb and media and not video:
        thumb = media
    src = None
    if thumb and thumb.startswith("data:"):
        src = thumb
    elif ctx["embed"]:
        key = thumb or media
        if key not in _FRAMES:
            _FRAMES[key] = (fetch_image(thumb) if thumb else None) or (video_frame(media) if video and media else None)
        src = _FRAMES[key]
    elif thumb:
        src = thumb
    if src:
        return f'<img src="{esc(src)}" alt="{alt}" loading="lazy">'
    if video and media:
        # No frame to embed: let the browser show the video's own first frame.
        # Print can't, so a placeholder sits underneath.
        return (f'<img class="under" src="{placeholder_thumb(item.get("format"), True)}" alt="">'
                f'<video src="{esc(media)}#t=1" preload="metadata" muted playsinline aria-label="{alt}"></video>')
    return f'<img src="{placeholder_thumb(item.get("format"), video)}" alt="{alt}">'


PLAY = ('<span class="play" aria-hidden="true"><svg viewBox="0 0 24 24" width="18" height="18">'
        '<path d="M8 5.5v13l11-6.5z" fill="#fff"/></svg></span>')


def media_wrap(inner, url):
    """The thumbnail frame: a link to the ad when there is one, a plain box otherwise."""
    if url:
        return f'<a class="media" href="{esc(url)}" target="_blank" rel="noopener">{inner}</a>'
    return f'<span class="media">{inner}</span>'


def link_wrap(inner, url, cls=""):
    c = f' class="{cls}"' if cls else ""
    return f'<a{c} href="{esc(url)}" target="_blank" rel="noopener">{inner}</a>' if url else inner


# ---------------------------------------------------------------- svg charts

def runs(coords):
    """Split (index, ...) points into runs of back-to-back weeks, so a missing
    week breaks the line instead of being drawn as if nothing happened."""
    out = []
    for c in coords:
        if out and c[0] == out[-1][-1][0] + 1:
            out[-1].append(c)
        else:
            out.append([c])
    return out


def run_path(run):
    return " ".join(f"{'M' if i == 0 else 'L'}{c[1]:.1f},{c[2]:.1f}" for i, c in enumerate(run))


def no_data_chart(title, w=440, h=220):
    return (f'<svg class="chart" viewBox="0 0 {w} {h}" role="img" aria-label="{esc(title)}: no data">'
            f'<rect x="1" y="1" width="{w - 2}" height="{h - 2}" rx="12" class="nodata"/>'
            f'<text x="{w / 2}" y="{h / 2 + 4}" class="tick" text-anchor="middle">No data for these weeks</text></svg>')


def sparkline(values, width=120, height=32):
    pts = [v for v in values if v is not None]
    if len(pts) < 2:
        return ""
    lo, hi = min(pts), max(pts)
    span = (hi - lo) or 1
    step = (width - 8) / (len(values) - 1)
    coords = []
    for i, v in enumerate(values):
        if v is None:
            continue
        x = 4 + i * step
        y = 4 + (height - 8) * (1 - (v - lo) / span)
        coords.append((i, x, y))
    path = " ".join(run_path(r) for r in runs(coords))
    _, lx, ly = coords[-1]
    return (
        f'<svg class="spark" viewBox="0 0 {width} {height}" width="{width}" height="{height}" aria-hidden="true">'
        f'<path d="{path}" fill="none" stroke="{SPARK_GRAY}" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>'
        f'<circle cx="{lx:.1f}" cy="{ly:.1f}" r="4" class="spark-dot"/></svg>'
    )


def column_chart(labels, values, kind, currency, title):
    w, h = 440, 220
    left, right, top, bottom = 52, 12, 18, 30
    pw, ph = w - left - right, h - top - bottom
    if all(v is None for v in values):
        return no_data_chart(title, w, h)
    ticks = nice_ticks(0, max(v for v in values if v is not None))
    vmax = ticks[-1]
    band = pw / len(values)
    bar = min(24, band * 0.56)
    parts = [f'<svg class="chart" viewBox="0 0 {w} {h}" role="img" aria-label="{esc(title)}">']
    for i, tv in enumerate(ticks):
        y = top + ph * (1 - tv / vmax)
        parts.append(f'<line x1="{left}" x2="{w - right}" y1="{y:.1f}" y2="{y:.1f}" class="grid{" base" if i == 0 else ""}"/>')
        parts.append(f'<text x="{left - 8}" y="{y + 4:.1f}" class="tick" text-anchor="end">{esc(tick_label(tv, kind, currency))}</text>')
    last = max(i for i, v in enumerate(values) if v is not None)
    for i, (lab, v) in enumerate(zip(labels, values)):
        cx = left + band * i + band / 2
        parts.append(f'<text x="{cx:.1f}" y="{h - 10}" class="tick" text-anchor="middle">{esc(lab)}</text>')
        if v is None:
            continue
        bh = max(1.0, ph * v / vmax)
        x, y = cx - bar / 2, top + ph - bh
        r = min(4, bh)
        d = (f"M{x:.1f},{top + ph:.1f} V{y + r:.1f} Q{x:.1f},{y:.1f} {x + r:.1f},{y:.1f} "
             f"H{x + bar - r:.1f} Q{x + bar:.1f},{y:.1f} {x + bar:.1f},{y + r:.1f} V{top + ph:.1f} Z")
        cls = "col current" if i == last else "col"
        parts.append(f'<g class="hit"><rect x="{cx - band / 2:.1f}" y="{top}" width="{band:.1f}" height="{ph}" fill="transparent"/>'
                     f'<path d="{d}" class="{cls}"/><title>{esc(lab)}: {esc(fmt(v, kind, currency, full=True))}</title></g>')
        if i == last:
            parts.append(f'<text x="{cx:.1f}" y="{y - 6:.1f}" class="vlabel" text-anchor="middle">{esc(fmt(v, kind, currency))}</text>')
    parts.append("</svg>")
    return "".join(parts)


def line_chart(labels, values, kind, currency, title, target=None):
    w, h = 440, 220
    left, right, top, bottom = 52, 40, 18, 30
    pw, ph = w - left - right, h - top - bottom
    pts = [v for v in values if v is not None]
    if not pts:
        return no_data_chart(title, w, h)
    hi = max(pts + ([target] if target is not None else []))
    lo = min(pts + ([target] if target is not None else []))
    ticks = nice_ticks(lo, hi)
    vmin, vmax = ticks[0], ticks[-1]
    step = pw / max(1, len(values) - 1)

    def ypos(v):
        return top + ph * (1 - (v - vmin) / (vmax - vmin))

    parts = [f'<svg class="chart" viewBox="0 0 {w} {h}" role="img" aria-label="{esc(title)}">']
    for i, tv in enumerate(ticks):
        y = ypos(tv)
        parts.append(f'<line x1="{left}" x2="{w - right}" y1="{y:.1f}" y2="{y:.1f}" class="grid{" base" if i == 0 else ""}"/>')
        parts.append(f'<text x="{left - 8}" y="{y + 4:.1f}" class="tick" text-anchor="end">{esc(tick_label(tv, kind, currency))}</text>')
    if target is not None:
        ty = ypos(target)
        parts.append(f'<line x1="{left}" x2="{w - right}" y1="{ty:.1f}" y2="{ty:.1f}" class="target"/>')
        parts.append(f'<text x="{w - right + 4}" y="{ty + 4:.1f}" class="tick">Goal</text>')
    coords = [(i, left + i * step, ypos(v), v, lab) for i, (lab, v) in enumerate(zip(labels, values)) if v is not None]
    for i, lab in enumerate(labels):
        parts.append(f'<text x="{left + i * step:.1f}" y="{h - 10}" class="tick" text-anchor="middle">{esc(lab)}</text>')
    for r in runs(coords):
        if len(r) < 2:
            continue
        path = run_path(r)
        parts.append(f'<path d="{path} L{r[-1][1]:.1f},{top + ph:.1f} L{r[0][1]:.1f},{top + ph:.1f} Z" class="area"/>')
        parts.append(f'<path d="{path}" class="line"/>')
    for i, (_, x, y, v, lab) in enumerate(coords):
        last = i == len(coords) - 1
        parts.append(f'<g class="hit"><circle cx="{x:.1f}" cy="{y:.1f}" r="12" fill="transparent"/>'
                     f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{5 if last else 3.5}" class="dot{" current" if last else ""}"/>'
                     f'<title>{esc(lab)}: {esc(fmt(v, kind, currency, full=True))}</title></g>')
    _, lx, ly, lv, _ = coords[-1]
    parts.append(f'<text x="{lx:.1f}" y="{ly - 12:.1f}" class="vlabel" text-anchor="middle">{esc(fmt(lv, kind, currency))}</text>')
    parts.append("</svg>")
    return "".join(parts)


# ---------------------------------------------------------------- sections

def section(key, title, body, kicker=None):
    k = f'<p class="kicker">{esc(kicker)}</p>' if kicker else ""
    return f'<section class="block glass" id="{key}">{k}<h2>{esc(title)}</h2>{body}</section>'


def render_headline(d, ctx):
    takeaways = d.get("takeaways") or []
    items = "".join(
        f'<li><span class="tnum">{i + 1}</span><p>{esc(t)}</p></li>' for i, t in enumerate(takeaways[:3])
    )
    return (
        '<section class="block glass hero" id="headline">'
        '<p class="kicker">The week in one line</p>'
        f'<p class="headline">{esc(d.get("headline", ""))}</p>'
        f'<ol class="takeaways">{items}</ol></section>'
    )


def render_scorecard(d, ctx):
    tiles = []
    for k in d.get("kpis") or []:
        kind = k.get("format", "number")
        delta = delta_parts(k)
        dhtml = ""
        if delta:
            text, tone, arrow = delta
            dhtml = f'<p class="delta {tone}"><span aria-hidden="true">{arrow}</span> {esc(text)}</p>'
        goal = ""
        if k.get("target") is not None:
            goal = f'<p class="goal">Goal {esc(fmt(k["target"], kind, ctx["cur"]))}</p>'
        lead = " lead" if k.get("lead") else ""
        tiles.append(
            f'<div class="tile{lead}"><p class="label">{esc(k.get("label"))}</p>'
            f'<p class="value">{esc(fmt(k.get("value"), kind, ctx["cur"]))}</p>{dhtml}'
            f'<div class="tile-foot">{goal}{sparkline(k.get("trend") or [])}</div>'
            + (f'<p class="tile-note">{esc(k["note"])}</p>' if k.get("note") else "")
            + "</div>"
        )
    return section("scorecard", "Scorecard", f'<div class="tiles">{"".join(tiles)}</div>',
                   "This week against last week, with the last 8 weeks as the small line")


def render_trend(d, ctx):
    t = d.get("trend") or {}
    labels = t.get("weeks") or []
    charts = []
    for s in t.get("series") or []:
        kind = s.get("format", "number")
        title = s.get("label", "")
        if s.get("chart", "column" if kind == "currency" else "line") == "column":
            svg = column_chart(labels, s.get("values") or [], kind, ctx["cur"], title)
        else:
            svg = line_chart(labels, s.get("values") or [], kind, ctx["cur"], title, s.get("target"))
        note = f'<p class="chart-note">{esc(s["note"])}</p>' if s.get("note") else ""
        charts.append(f'<figure class="chart-card"><figcaption>{esc(title)}</figcaption>{svg}{note}</figure>')
    body = f'<div class="chart-row">{"".join(charts)}</div>'
    if t.get("read"):
        body += f'<p class="read">{esc(t["read"])}</p>'
    return section("trend", "The last 8 weeks", body)


def stat_list(stats, cur):
    return "".join(
        f'<div><dt>{esc(s.get("label"))}</dt><dd>{esc(fmt(s.get("value"), s.get("format", "number"), cur))}</dd></div>'
        for s in stats or []
    )


def render_top(d, ctx):
    cards = []
    for i, c in enumerate(d.get("top_creatives") or []):
        url = ad_link(c)
        play = PLAY if is_video(c) else ""
        thumb = media_wrap(f'{media_html(c, ctx)}{play}', url)
        badge = f'<span class="badge">{esc(c["status"])}</span>' if c.get("status") else ""
        pm = c.get("primary_metric") or {}
        primary = ""
        if pm:
            primary = (f'<p class="primary"><span>{esc(fmt(pm.get("value"), pm.get("format", "ratio"), ctx["cur"]))}</span> '
                       f'{esc(pm.get("label", ""))} on {esc(fmt(c.get("spend"), "currency", ctx["cur"]))} spend</p>')
        view = link_wrap("Watch the ad &#8599;" if is_video(c) else "See the ad &#8599;", url, "view") if url else ""
        cards.append(
            f'<article class="creative"><div class="thumb">{thumb}<span class="rank">{i + 1}</span>{badge}</div>'
            f'<div class="creative-body"><p class="fmt">{esc(c.get("format", ""))}</p>'
            f'<h3>{link_wrap(esc(c.get("name")), url)}</h3>{primary}'
            f'<dl class="stats">{stat_list(c.get("stats"), ctx["cur"])}</dl>'
            f'<p class="why">{esc(c.get("why", ""))}</p>{view}</div></article>'
        )
    return section("top_creatives", "What's carrying the account", f'<div class="creatives">{"".join(cards)}</div>',
                   "Top creatives this week, ranked by spend")


def render_launches(d, ctx):
    l = d.get("launches") or {}
    count = l.get("count", 0)
    prior = l.get("prior_count")
    vs = f' <span class="muted">vs {esc(prior)} last week</span>' if prior is not None else ""
    chips = "".join(f'<li><b>{esc(f.get("count"))}</b> {esc(f.get("label"))}</li>' for f in l.get("by_format") or [])
    early = "".join(
        f'<li><b>{link_wrap(esc(e.get("name")), ad_link(e))}</b> <span>{esc(e.get("note"))}</span></li>'
        for e in l.get("early_signals") or []
    )
    body = (
        f'<div class="launch-head"><p class="big">{esc(count)}<small> new ads live</small>{vs}</p>'
        f'<ul class="chips">{chips}</ul></div>'
        + (f'<p class="read">{esc(l["summary"])}</p>' if l.get("summary") else "")
        + (f'<h3 class="sub">Early signals</h3><ul class="signals">{early}</ul>' if early else "")
    )
    return section("launches", "New this week", body)


def render_watch(d, ctx):
    rows = []
    for w in d.get("watch_list") or []:
        url = ad_link(w)
        play = PLAY if is_video(w) else ""
        mini = media_wrap(f'{media_html(w, ctx)}{play}', url)
        rows.append(
            f'<li class="watch"><div class="mini">{mini}</div><div>'
            f'<p class="watch-name">{link_wrap(esc(w.get("name")), url)}'
            f' <span class="flag"><span aria-hidden="true">&#9888;</span> {esc(w.get("issue"))}</span></p>'
            f'<p class="evidence">{esc(w.get("evidence"))}</p>'
            f'<p class="action"><b>Our call:</b> {esc(w.get("action"))}</p></div></li>'
        )
    if not rows:
        body = '<p class="read">Nothing is slipping enough to flag this week.</p>'
    else:
        body = f'<ul class="watchlist">{"".join(rows)}</ul>'
    return section("watch_list", "What we're watching", body, "Ads slipping, tiring, or wasting spend")


def render_mix(d, ctx):
    m = d.get("format_mix") or {}
    rows = m.get("rows") or []
    top = max([r.get("share", 0) for r in rows] + [0.0001])
    bars = []
    for r in rows:
        share = r.get("share", 0)
        width = 100 * share / top
        bars.append(
            f'<div class="mix-row" title="{esc(r.get("label"))}: {calc_percent(share)} of spend">'
            f'<span class="mix-label">{esc(r.get("label"))}</span>'
            f'<span class="mix-track"><span class="mix-bar" style="width:{width:.1f}%"></span></span>'
            f'<span class="mix-val">{calc_percent(share)}</span>'
            f'<span class="mix-meta">{esc(r.get("metric", ""))}</span></div>'
        )
    body = f'<div class="mix">{"".join(bars)}</div>'
    if m.get("read"):
        body += f'<p class="read">{esc(m["read"])}</p>'
    return section("format_mix", m.get("title") or "Where the spend went", body, "Share of this week's spend")


def render_insights(d, ctx):
    items = "".join(
        f'<article class="insight"><h3>{esc(i.get("title"))}</h3><p>{esc(i.get("body"))}</p></article>'
        for i in d.get("insights") or []
    )
    return section("insights", "What we learned", f'<div class="insights">{items}</div>')


def render_next(d, ctx):
    items = []
    for i, n in enumerate(d.get("next_week") or []):
        owner = f'<span class="owner">{esc(n["owner"])}</span>' if n.get("owner") else ""
        items.append(
            f'<li><span class="step">{i + 1}</span><div><p class="do">{esc(n.get("action"))} {owner}</p>'
            f'<p class="because">{esc(n.get("why"))}</p></div></li>'
        )
    return section("next_week", "The plan for next week", f'<ol class="plan">{"".join(items)}</ol>')


def render_all_ads(d, ctx):
    table = d.get("all_ads") or {}
    cols = table.get("columns") or []
    rows = table.get("rows") or []
    if not cols or not rows:
        return ""
    first_text = next((c.get("key") for c in cols if c.get("format", "text") == "text"), None)
    head = "".join(f'<th class="{"num" if c.get("format") not in (None, "text") else ""}">{esc(c.get("label"))}</th>' for c in cols)
    body = []
    for r in rows:
        cells = []
        for c in cols:
            kind = c.get("format", "text")
            v = r.get(c.get("key"))
            if kind == "text":
                inner = esc(v)
                if c.get("key") == first_text and ad_link(r):
                    inner = link_wrap(f'{inner} <span class="ext" aria-hidden="true">&#8599;</span>', ad_link(r))
                cells.append(f"<td>{inner}</td>")
            elif v is None:
                cells.append('<td class="num empty">&ndash;</td>')
            else:
                cells.append(f'<td class="num">{esc(fmt(v, kind, ctx["cur"], full=True))}</td>')
        body.append(f"<tr>{''.join(cells)}</tr>")
    t = f'<div class="table-wrap"><table><thead><tr>{head}</tr></thead><tbody>{"".join(body)}</tbody></table></div>'
    return section("all_ads", table.get("title") or "Every ad that spent this week", t, "The full table")


RENDERERS = {
    "headline": render_headline,
    "scorecard": render_scorecard,
    "trend": render_trend,
    "top_creatives": render_top,
    "launches": render_launches,
    "watch_list": render_watch,
    "format_mix": render_mix,
    "insights": render_insights,
    "next_week": render_next,
    "all_ads": render_all_ads,
}

HAS_DATA = {
    "headline": lambda d: d.get("headline"),
    "scorecard": lambda d: d.get("kpis"),
    "trend": lambda d: (d.get("trend") or {}).get("series"),
    "top_creatives": lambda d: d.get("top_creatives"),
    "launches": lambda d: d.get("launches"),
    "watch_list": lambda d: "watch_list" in d,
    "format_mix": lambda d: (d.get("format_mix") or {}).get("rows"),
    "insights": lambda d: d.get("insights"),
    "next_week": lambda d: d.get("next_week"),
    "all_ads": lambda d: (d.get("all_ads") or {}).get("rows"),
}


# ---------------------------------------------------------------- page

CSS = """
:root{color-scheme:light;
--canvas:#f6f5fa;--ink:#16151c;--ink-2:#4d4b59;--muted:#8a8898;
--glass:rgba(255,255,255,.58);--glass-edge:rgba(255,255,255,.85);--glass-line:rgba(22,21,28,.07);
--solid:#ffffff;--soft:rgba(255,255,255,.72);--grid:#e6e4ee;--axis:#cfccdb;
--series:SERIES1;--good:#11734b;--bad:#b4363c;--warn-bg:rgba(250,178,25,.18);--warn-ink:#7a5200;
--chip:rgba(22,21,28,.06);--ink-pill:#1f1d2b;
--display:"Fraunces","Iowan Old Style","Georgia",serif;
--sans:"DM Sans",system-ui,-apple-system,"Segoe UI",Roboto,Helvetica,Arial,sans-serif}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--canvas);color:var(--ink);font:15px/1.55 var(--sans);position:relative;min-height:100vh}
.prism{position:fixed;inset:0;z-index:0;pointer-events:none;overflow:hidden;
background:
radial-gradient(42% 38% at 8% 4%,rgba(186,176,255,.55),transparent 70%),
radial-gradient(36% 32% at 92% 10%,rgba(150,214,255,.50),transparent 70%),
radial-gradient(40% 36% at 78% 62%,rgba(255,196,214,.40),transparent 72%),
radial-gradient(44% 40% at 12% 78%,rgba(170,236,214,.42),transparent 72%),
radial-gradient(30% 26% at 50% 40%,rgba(255,228,180,.30),transparent 75%)}
a{color:inherit;text-decoration-color:rgba(22,21,28,.25);text-underline-offset:3px}
a:hover{text-decoration-color:currentColor}
.wrap{position:relative;z-index:1;max-width:1040px;margin:0 auto;padding:0 16px 40px}
.cover{padding:48px 4px 18px}
.brandline{display:flex;align-items:center;gap:10px;margin:0 0 28px}
.logo{height:30px;width:auto;display:block}
.brandname{font-weight:600;font-size:14px;letter-spacing:.01em;margin:0;padding:6px 14px;border-radius:999px;background:var(--glass);
border:1px solid var(--glass-edge);-webkit-backdrop-filter:blur(16px) saturate(140%);backdrop-filter:blur(16px) saturate(140%)}
.cover h1{font-family:var(--display);font-weight:300;font-size:clamp(40px,6.4vw,64px);line-height:1.04;letter-spacing:-.02em;margin:0 0 12px}
.cover .dates{font-size:17px;color:var(--ink-2);margin:0}
.glass{background:var(--glass);border:1px solid var(--glass-edge);border-radius:24px;
-webkit-backdrop-filter:blur(22px) saturate(150%);backdrop-filter:blur(22px) saturate(150%)}
.block{padding:28px;margin-top:18px}
.kicker{margin:0 0 6px;font-size:12px;letter-spacing:.06em;text-transform:uppercase;color:var(--muted);font-weight:600}
h2{margin:0 0 18px;font-size:22px;line-height:1.25;font-weight:600;letter-spacing:-.01em}
h3{margin:0;font-size:16px;line-height:1.3;font-weight:600}
p{margin:0}
.muted{color:var(--muted);font-weight:400}
.read{color:var(--ink-2);margin-top:16px;max-width:72ch}
.headline{font-family:var(--display);font-weight:300;font-size:clamp(24px,3.2vw,32px);line-height:1.28;letter-spacing:-.01em;margin:4px 0 24px;max-width:40ch}
.takeaways{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:12px}
.takeaways li{display:flex;gap:12px;background:var(--soft);border-radius:16px;padding:14px 16px}
.tnum,.step{flex:none;display:grid;place-items:center;background:var(--ink-pill);color:#fff;font-weight:600}
.tnum{width:24px;height:24px;border-radius:50%;font-size:12px;margin-top:1px}
.takeaways p{color:var(--ink-2)}
.tiles{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:12px}
.tile{background:var(--solid);border-radius:16px;padding:16px 16px 14px;display:flex;flex-direction:column;gap:4px;border:1px solid var(--glass-line)}
.tile.lead{border:1.5px solid var(--ink-pill)}
.tile .label{font-size:13px;color:var(--ink-2);font-weight:500}
.tile .value{font-size:26px;overflow-wrap:anywhere;font-weight:600;line-height:1.15;letter-spacing:-.015em}
.delta{font-size:13px;font-weight:600}
.delta.good{color:var(--good)}.delta.bad{color:var(--bad)}.delta.neutral{color:var(--muted)}
.tile-foot{display:flex;justify-content:space-between;align-items:flex-end;margin-top:auto;padding-top:8px;gap:8px}
.goal{font-size:12px;color:var(--muted)}
.tile-note{font-size:12px;color:var(--ink-2);border-top:1px solid var(--grid);padding-top:8px;margin-top:6px}
.spark{display:block;margin-left:auto}.spark-dot{fill:var(--series);stroke:var(--solid);stroke-width:2}
.chart-row{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:12px}
.chart-card{margin:0;background:var(--solid);border-radius:16px;padding:16px;border:1px solid var(--glass-line)}
figcaption{font-size:14px;font-weight:600;margin-bottom:8px}
.chart{width:100%;height:auto;display:block}
.chart-note{font-size:12px;color:var(--muted);margin-top:6px}
.grid{stroke:var(--grid);stroke-width:1}.grid.base{stroke:var(--axis)}
.tick{font-size:11px;fill:var(--muted);font-variant-numeric:tabular-nums;font-family:var(--sans)}
.vlabel{font-size:12px;fill:var(--ink);font-weight:600;font-family:var(--sans)}
.col{fill:var(--series);opacity:.42}.col.current{opacity:1}
.hit:hover .col{opacity:.85}
.line{fill:none;stroke:var(--series);stroke-width:2;stroke-linejoin:round;stroke-linecap:round}
.area{fill:var(--series);opacity:.10}
.dot{fill:var(--series);stroke:var(--solid);stroke-width:2}
.nodata{fill:rgba(22,21,28,.03);stroke:var(--grid)}
.target{stroke:var(--ink-2);stroke-width:1;stroke-dasharray:4 4;opacity:.55}
.creatives{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:14px}
.creative{background:var(--solid);border-radius:24px;overflow:hidden;display:flex;flex-direction:column;break-inside:avoid;border:1px solid var(--glass-line)}
.thumb{position:relative;aspect-ratio:4/5;background:#ece9f4;overflow:hidden}
.media{display:block;position:absolute;inset:0}
.media img,.media video{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;display:block}
.media img.under{z-index:0}.media video{z-index:1;background:transparent}
.play{position:absolute;z-index:2;left:50%;top:50%;width:48px;height:48px;margin:-24px 0 0 -24px;border-radius:50%;display:grid;place-items:center;
background:rgba(0,0,0,.32);border:1px solid rgba(255,255,255,.35);-webkit-backdrop-filter:blur(12px);backdrop-filter:blur(12px)}
.play svg{margin-left:2px}
.mini .play{width:28px;height:28px;margin:-14px 0 0 -14px}.mini .play svg{width:12px;height:12px}
.media:hover .play{background:rgba(0,0,0,.45)}
.rank,.badge{position:absolute;z-index:3;top:12px;font-weight:600;color:var(--ink);background:rgba(255,255,255,.9);
-webkit-backdrop-filter:blur(12px);backdrop-filter:blur(12px)}
.rank{left:12px;width:30px;height:30px;border-radius:50%;font-size:14px;display:grid;place-items:center}
.badge{right:12px;font-size:12px;border-radius:999px;padding:4px 11px}
.creative-body{padding:16px 18px 18px;display:flex;flex-direction:column;gap:8px;flex:1}
.fmt{font-size:12px;color:var(--muted);text-transform:uppercase;letter-spacing:.05em;font-weight:600}
.creative h3 a{text-decoration:none}.creative h3 a:hover{text-decoration:underline}
.primary{font-size:14px;color:var(--ink-2)}.primary span{font-size:20px;font-weight:600;color:var(--ink)}
.stats{display:grid;grid-template-columns:repeat(3,1fr);gap:6px;margin:0;padding:10px 0;border-top:1px solid var(--grid);border-bottom:1px solid var(--grid)}
.stats dt{font-size:11px;color:var(--muted)}.stats dd{margin:0;font-weight:600;font-size:14px;font-variant-numeric:tabular-nums}
.why{color:var(--ink-2);font-size:14px}
.view{margin-top:auto;align-self:flex-start;font-size:13px;font-weight:600;text-decoration:none;padding:6px 14px;border-radius:999px;background:var(--chip)}
.view:hover{background:rgba(22,21,28,.1)}
.launch-head{display:flex;flex-wrap:wrap;align-items:center;gap:12px 28px}
.big{font-family:var(--display);font-weight:300;font-size:52px;line-height:1}.big small{font-family:var(--sans);font-size:16px;font-weight:600;margin-left:8px}
.big .muted{font-family:var(--sans);font-size:14px;margin-left:8px}
.chips{display:flex;flex-wrap:wrap;gap:8px;list-style:none;margin:0;padding:0}
.chips li{background:var(--soft);border:1px solid var(--glass-line);border-radius:999px;padding:5px 12px;font-size:13px;color:var(--ink-2)}
.chips b{color:var(--ink)}
.sub{margin:20px 0 8px;font-size:14px}
.signals{margin:0;padding:0;list-style:none;display:grid;gap:8px}
.signals li{background:var(--soft);border-radius:14px;padding:11px 14px;font-size:14px}
.signals span{color:var(--ink-2)}
.watchlist{list-style:none;margin:0;padding:0;display:grid;gap:10px}
.watch{display:flex;gap:16px;align-items:flex-start;padding:14px;border-radius:18px;background:var(--solid);border:1px solid var(--glass-line);break-inside:avoid}
.mini{flex:none;position:relative;width:64px;aspect-ratio:4/5;border-radius:12px;overflow:hidden;background:#ece9f4}
.watch-name{font-weight:600}.watch-name a{text-decoration:none}.watch-name a:hover{text-decoration:underline}
.flag{display:inline-block;background:var(--warn-bg);color:var(--warn-ink);font-size:12px;font-weight:600;border-radius:999px;padding:2px 10px;margin-left:6px;vertical-align:1px}
.evidence{color:var(--ink-2);font-size:14px;margin-top:4px}
.action{font-size:14px;margin-top:6px}
.mix{display:grid;gap:10px}
.mix-row{display:grid;grid-template-columns:minmax(110px,180px) 1fr minmax(64px,auto) minmax(90px,150px);align-items:center;gap:12px;font-size:14px}
.mix-label{font-weight:500}
.mix-track{height:14px;display:block;background:rgba(22,21,28,.05);border-radius:999px}
.mix-bar{display:block;height:14px;background:var(--series);border-radius:999px;min-width:4px}
.mix-val{font-weight:600;text-align:right;font-variant-numeric:tabular-nums}
.mix-meta{color:var(--muted);font-size:13px}
.insights{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:12px}
.insight{background:var(--solid);border-radius:18px;padding:18px;border:1px solid var(--glass-line)}
.insight h3{font-family:var(--display);font-weight:400;font-size:19px;line-height:1.3;margin-bottom:8px}
.insight p{color:var(--ink-2);font-size:14px}
.plan{list-style:none;margin:0;padding:0;display:grid;gap:10px}
.plan li{display:flex;gap:14px;align-items:flex-start;background:var(--soft);border-radius:16px;padding:14px 16px}
.step{width:28px;height:28px;border-radius:50%;font-size:13px}
.do{font-weight:600}.because{color:var(--ink-2);font-size:14px;margin-top:2px}
.owner{display:inline-block;font-size:12px;font-weight:600;color:var(--ink-2);background:var(--chip);border-radius:999px;padding:1px 9px;margin-left:6px}
.table-wrap{overflow-x:auto;-webkit-overflow-scrolling:touch;background:var(--solid);border-radius:16px;border:1px solid var(--glass-line)}
table{border-collapse:collapse;width:100%;font-size:13px}
th{text-align:left;font-weight:600;color:var(--ink-2);border-bottom:1px solid var(--axis);padding:10px 12px;white-space:nowrap}
td{border-bottom:1px solid var(--grid);padding:9px 10px;vertical-align:top}
td:first-child{overflow-wrap:anywhere;min-width:160px;max-width:300px}
th{padding:10px}
tbody tr:last-child td{border-bottom:0}
td a{text-decoration:none}td a:hover{text-decoration:underline}
.ext{color:var(--muted);font-size:11px}
td.num,th.num{text-align:right;font-variant-numeric:tabular-nums;white-space:nowrap}
tbody tr:hover{background:#faf9fd}
td.empty{color:var(--muted)}
.byline{margin:26px 4px 0;font-size:12.5px;color:var(--ink-2);display:flex;flex-wrap:wrap;gap:4px 18px}
.byline b{color:var(--ink);font-weight:600}
.byline .mark{margin-left:auto;color:var(--muted)}
@media (max-width:640px){.block{padding:20px 16px}.mix-row{grid-template-columns:1fr auto;row-gap:4px}.mix-track{grid-column:1/-1;order:3}.mix-meta{grid-column:1/-1;order:4}
.stats{grid-template-columns:repeat(2,1fr)}.cover{padding-top:32px}.byline .mark{margin-left:0}}
@media (prefers-reduced-transparency:reduce){.glass,.brandname{background:rgba(255,255,255,.94);-webkit-backdrop-filter:none;backdrop-filter:none}}
@page{size:letter;margin:12mm 11mm}
@media print{body{font-size:12.5px;-webkit-print-color-adjust:exact;print-color-adjust:exact}
.prism{position:absolute;height:100%}
.wrap{max-width:none;padding:0}.cover{padding:8px 4px 6px}
.glass,.brandname{background:rgba(255,255,255,.72);-webkit-backdrop-filter:none;backdrop-filter:none}
.block{break-inside:avoid;padding:18px;margin-top:12px}
#top_creatives,#all_ads{break-inside:auto}.creatives{grid-template-columns:repeat(3,1fr)}
.creative,.watch,.tile,.insight,.chart-card{break-inside:avoid}tbody tr:hover{background:none}
.media video{display:none}}
"""


def render(data, embed=False):
    meta = data.get("meta") or {}
    ctx = {"cur": meta.get("currency_symbol", "$"), "embed": embed}
    order = data.get("sections") or SECTION_ORDER
    body = []
    for key in order:
        fn = RENDERERS.get(key)
        if fn and HAS_DATA[key](data):
            body.append(fn(data, ctx))
    css = CSS.replace("SERIES1", SERIES_1)
    logo = ""
    if meta.get("logo"):
        src = safe_src(meta["logo"])
        if embed and src and not src.startswith("data:"):
            src = fetch_image(src) or ""
        if src:
            logo = f'<img class="logo" src="{esc(src)}" alt="{esc(meta.get("brand"))}">'
    brand_line = logo or f'<p class="brandname">{esc(meta.get("brand"))}</p>'
    scope = f' &middot; {esc(meta["scope_label"])}' if meta.get("scope_label") else ""
    byline = []
    if meta.get("prepared_by") or meta.get("prepared_for"):
        by = f'Prepared by <b>{esc(meta["prepared_by"])}</b>' if meta.get("prepared_by") else "Prepared"
        if meta.get("prepared_for"):
            by += f' for <b>{esc(meta["prepared_for"])}</b>'
        byline.append(f"<span>{by}</span>")
    if meta.get("attribution"):
        byline.append(f'<span>Results from {esc(meta["attribution"])}</span>')
    if meta.get("data_through"):
        byline.append(f'<span>Data through {esc(meta["data_through"])}</span>')
    gen = f' &middot; {esc(meta["generated_on"])}' if meta.get("generated_on") else ""
    byline.append(f'<span class="mark">Built with Parker{gen}</span>')
    title = f'{meta.get("brand", "")} weekly creative report, {meta.get("week_label", "")}'.strip(", ")
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{FONTS}">
<style>{css}</style>
</head>
<body>
<div class="prism" aria-hidden="true"></div>
<div class="wrap">
<header class="cover">
<div class="brandline">{brand_line}</div>
<h1>Weekly creative report</h1>
<p class="dates">{esc(meta.get("week_label", ""))}{" &middot; " if meta.get("week_label") else ""}{esc(meta.get("date_range", ""))}{scope}</p>
</header>
<main>
{"".join(body)}
</main>
<footer class="byline">{"".join(byline)}</footer>
</div>
</body>
</html>
"""


def find_chrome():
    candidates = [
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "/Applications/Chromium.app/Contents/MacOS/Chromium",
        "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    ]
    for name in ("google-chrome", "google-chrome-stable", "chromium", "chromium-browser", "msedge"):
        found = shutil.which(name)
        if found:
            candidates.insert(0, found)
    return next((c for c in candidates if os.path.exists(c)), None)


def write_pdf(html_path):
    chrome = find_chrome()
    if not chrome:
        print("PDF skipped: no Chrome, Chromium, or Edge found. Open the HTML and use Print > Save as PDF.")
        return None
    pdf_path = os.path.splitext(html_path)[0] + ".pdf"
    cmd = [chrome, "--headless=new", "--disable-gpu", "--no-pdf-header-footer", "--virtual-time-budget=8000",
           f"--print-to-pdf={os.path.abspath(pdf_path)}", "file://" + os.path.abspath(html_path)]
    try:
        subprocess.run(cmd, check=True, capture_output=True, timeout=120)
    except Exception as exc:
        print(f"PDF skipped: the browser couldn't print it ({exc}). The HTML is fine.")
        return None
    print(f"Wrote {pdf_path}")
    return pdf_path


def percent_values(data):
    """Every (where, value) the page will format as a percent."""
    out = []
    for k in data.get("kpis") or []:
        if k.get("format") == "percent":
            for field in ("value", "prior", "target"):
                out.append((f"KPI '{k.get('label')}' {field}", k.get(field)))
            out += [(f"KPI '{k.get('label')}' trend", v) for v in k.get("trend") or []]
    for s in (data.get("trend") or {}).get("series") or []:
        if s.get("format") == "percent":
            out += [(f"trend '{s.get('label')}'", v) for v in s.get("values") or []]
    for c in data.get("top_creatives") or []:
        for m in list(c.get("stats") or []) + [c.get("primary_metric") or {}]:
            if m.get("format") == "percent":
                out.append((f"'{c.get('name')}' {m.get('label')}", m.get("value")))
    table = data.get("all_ads") or {}
    for col in table.get("columns") or []:
        if col.get("format") == "percent":
            out += [(f"table '{r.get('name')}' {col.get('label')}", r.get(col.get("key"))) for r in table.get("rows") or []]
    return out


def check(data):
    """Catch the mistakes that would make a report look broken or mislead a reader."""
    problems = []
    meta = data.get("meta") or {}
    for field in ("brand", "date_range", "attribution"):
        if not meta.get(field):
            problems.append(f"meta.{field} is missing")
    if not data.get("headline"):
        problems.append("headline is missing")
    for k in data.get("kpis") or []:
        if k.get("value") is None:
            problems.append(f"KPI '{k.get('label')}' has no value")
    # The ad tool reports rates as percents (33.64 means 33.64%); the data file
    # wants fractions. No rate in this report runs past 150%, so a bigger
    # number is a percent that never got divided by 100.
    for where, v in percent_values(data):
        if isinstance(v, (int, float)) and v > 1.5:
            problems.append(f"{where} is {v}, which reads as {v * 100:.0f}%; write percents as fractions (33.64% is 0.3364)")
    for s in (data.get("trend") or {}).get("series") or []:
        if len(s.get("values") or []) != len((data.get("trend") or {}).get("weeks") or []):
            problems.append(f"trend series '{s.get('label')}' doesn't match the number of weeks")
    for c in data.get("top_creatives") or []:
        if not c.get("why"):
            problems.append(f"top creative '{c.get('name')}' has no 'why' line")
    for w in data.get("watch_list") or []:
        if not w.get("action"):
            problems.append(f"watch-list ad '{w.get('name')}' has no action")
    if not data.get("_fixture"):
        named = (list(data.get("top_creatives") or []) + list(data.get("watch_list") or [])
                 + list((data.get("launches") or {}).get("early_signals") or [])
                 + list((data.get("all_ads") or {}).get("rows") or []))
        for a in named:
            if not ad_link(a):
                problems.append(f"ad '{a.get('name')}' has no usable media_url (missing, or not an http/https address), so its name won't link to the ad")
    mix = (data.get("format_mix") or {}).get("rows") or []
    total = sum(r.get("share", 0) for r in mix)
    if mix and not 0.97 <= total <= 1.03:
        problems.append(f"format mix shares add up to {total:.0%}, not 100%")
    return problems


def main(argv):
    args = [a for a in argv if not a.startswith("--")]
    if len(args) != 2:
        print(__doc__)
        return 2
    src, out = args
    with open(src, encoding="utf-8") as fh:
        data = json.load(fh, parse_float=ExactFloat)
    problems = check(data)
    for p in problems:
        print(f"WARNING: {p}")
    page = render(data, embed="--embed-images" in argv)
    with open(out, "w", encoding="utf-8") as fh:
        fh.write(page)
    print(f"Wrote {out} ({len(page) // 1024} KB)")
    if "--pdf" in argv:
        write_pdf(out)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
