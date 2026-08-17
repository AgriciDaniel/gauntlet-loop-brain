#!/usr/bin/env python3
from __future__ import annotations

import argparse
import html
import json
import re
from pathlib import Path
from typing import Any


BRAIN_TITLE = "Gauntlet Loop Brain"
BRAIN_DOMAIN = "designing, running, evaluating, and governing one-prompt multi-agent improvement loops"
BRAIN_TAGLINE = "Source cited Obsidian operating brain for designing, running, evaluating, and governing one-prompt multi-agent improvement loops."

CB = "#22D3EE"
CR = "#8B5CF6"
CY = "#FB7185"
CG = "#FBBF24"
OB = "#8BE9F7"
TB = "#12364B"
TR = "#2B214D"
TY = "#472439"
TG = "#493919"
NB = "#C8F8FF"
NR = "#E9DCFF"
NY = "#FFE3E9"
NG = "#FFF0B8"
INK = "#F8FAFC"
SUB = "#AAB4DB"
LINE = "#303866"
PANEL = "#111631"
CANVAS = "#070A1D"
FONT = '"Google Sans","Product Sans",Roboto,"Segoe UI",Arial,sans-serif'
REDUCED = "@media (prefers-reduced-motion:reduce){*{animation:none!important}}"


def esc(value: object) -> str:
    return html.escape(str(value), quote=True)


def doc(w: int, h: int, title: str, desc: str, style: str, body: str, bg: str = "#fff") -> str:
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img" '
        f'aria-labelledby="title desc" font-family=\'{FONT}\'>\n'
        f'<title id="title">{esc(title)}</title>\n'
        f'<desc id="desc">{esc(desc)}</desc>\n'
        f"<style>\n  {REDUCED}\n{style}\n</style>\n"
        f'<rect width="{w}" height="{h}" fill="{bg}"/>\n{body}\n</svg>\n'
    )


def card(w: int, h: int, bg: str = PANEL, border: str = LINE, r: int = 26) -> str:
    return f'<rect x="10" y="10" width="{w - 20}" height="{h - 20}" rx="{r}" fill="{bg}" stroke="{border}"/>'


def wrap(value: object, limit: int, max_lines: int) -> list[str]:
    words = " ".join(str(value).split()).split()
    if not words:
        return []
    lines: list[str] = []
    current = ""
    for word in words:
        candidate = f"{current} {word}".strip()
        if len(candidate) <= limit or not current:
            current = candidate
            continue
        lines.append(current)
        current = word
        if len(lines) == max_lines:
            break
    if current and len(lines) < max_lines:
        lines.append(current)
    return lines[:max_lines]


def load_json(path: Path) -> dict[str, Any] | None:
    if not path.exists():
        return None
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None
    return data if isinstance(data, dict) else None


def count_json_sources(path: Path) -> int | None:
    data = load_json(path)
    if data is None:
        return None
    for key in ("sources", "entries"):
        value = data.get(key)
        if isinstance(value, list):
            return len([item for item in value if isinstance(item, dict)])
    return None


def source_metric(vault: Path, repo: Path) -> tuple[int | None, str]:
    candidates = [
        (vault / "references" / "source-ledger.json", "source ledger entries"),
        (repo / "references" / "source-ledger.json", "source ledger entries"),
        (vault / ".raw" / ".manifest.json", "raw manifest sources"),
    ]
    for path, label in candidates:
        count = count_json_sources(path)
        if count is not None and count > 0:
            return count, label
    return None, ""


def concept_metric(vault: Path) -> int | None:
    folder = vault / "wiki" / "concepts"
    if not folder.exists():
        return None
    count = len([path for path in folder.glob("*.md") if path.name != "_index.md"])
    return count if count > 0 else None


def canon_index_count(path: Path) -> int | None:
    if not path.exists():
        return None
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except OSError:
        return None
    count = 0
    for line in lines:
        item = line.strip()
        if not item.startswith("- "):
            continue
        lowered = item.lower()
        if "placeholder" in lowered or "add researched" in lowered or "template" in lowered:
            continue
        if re.search(r"\[[^\]]+\]\((?!NNN-)[^)]+\.md\)", item):
            count += 1
    return count if count > 0 else None


def canon_metric(vault: Path, repo: Path) -> int | None:
    for root in (vault, repo):
        folder = root / "references" / "canon"
        if not folder.exists():
            continue
        files = [path for path in folder.glob("*.md") if path.name != "_index.md"]
        if files:
            return len(files)
        indexed = canon_index_count(folder / "_index.md")
        if indexed is not None:
            return indexed
    return None


def metrics(vault: Path, repo: Path) -> list[tuple[int, str, str, str, str]]:
    items: list[tuple[int, str, str, str, str]] = []
    sources, source_label = source_metric(vault, repo)
    if sources is not None:
        items.append((sources, source_label, CB, TB, NB))
    concepts = concept_metric(vault)
    if concepts is not None:
        items.append((concepts, "concept notes", CR, TR, NR))
    canon = canon_metric(vault, repo)
    if canon is not None:
        items.append((canon, "canon entries", CY, TY, NY))
    return items


def metric_row(items: list[tuple[int, str, str, str, str]]) -> str:
    if not items:
        return ""
    x0 = 50
    y = 308
    width = 250
    gap = 18
    row = f'<text class="metric" x="{x0}" y="{y - 14}" font-size="12" letter-spacing="2.2" font-weight="800" fill="{OB}">LIVE VAULT SIGNALS</text>'
    for i, (value, label, solid, tint, on_tint) in enumerate(items[:4]):
        x = x0 + i * (width + gap)
        row += (
            f'<g class="metric" style="animation-delay:{0.86 + i * 0.08:.2f}s">'
            f'<rect x="{x}" y="{y}" width="{width}" height="54" rx="16" fill="{tint}" stroke="{solid}" stroke-opacity=".45"/>'
            f'<circle class="pulse" cx="{x + 28}" cy="{y + 27}" r="7" fill="{solid}"/>'
            f'<text x="{x + 48}" y="{y + 24}" font-size="18" font-weight="800" fill="{on_tint}">{value}</text>'
            f'<text x="{x + 48}" y="{y + 42}" font-size="12" font-weight="700" fill="{on_tint}">{esc(label)}</text>'
            f"</g>"
        )
    return row


def build_svg(vault: Path, repo: Path) -> str:
    subtitle = BRAIN_TAGLINE or f"Source cited Obsidian operating brain for {BRAIN_DOMAIN}."
    subtitle_lines = wrap(subtitle, 96, 2)
    subtitle_svg = "".join(
        f'<text class="head" style="animation-delay:{0.08 + i * 0.04:.2f}s" x="50" y="{115 + i * 18}" font-size="13" fill="{SUB}">{esc(line)}</text>'
        for i, line in enumerate(subtitle_lines)
    )
    stages = [
        ("Evidence", "immutable inputs", CB),
        ("Memory", "linked notes and canon", CR),
        ("Gates", "tests, sources, confidence", CY),
        ("Decisions", "bounded, honest outputs", CG),
    ]
    cw = 264
    y = 146
    xs = [42, 326, 610, 894]
    chips = ""
    for i, (label, sub, col) in enumerate(stages):
        x = xs[i]
        chips += (
            f'<g class="chip" style="animation-delay:{0.30 + i * 0.16:.2f}s">'
            f'<rect x="{x}" y="{y}" width="{cw}" height="104" rx="20" fill="#151B43" stroke="{col}" stroke-opacity=".55"/>'
            f'<rect x="{x}" y="{y}" width="7" height="104" rx="3.5" fill="{col}"/>'
            f'<circle class="pulse" cx="{x + 35}" cy="{y + 35}" r="10" fill="{col}"/>'
            f'<text x="{x + 58}" y="{y + 41}" font-size="19" font-weight="800" fill="{INK}">{esc(label)}</text>'
            f'<text x="{x + 24}" y="{y + 75}" font-size="13" fill="{SUB}">{esc(sub)}</text>'
            f'<text x="{x + cw - 24}" y="{y + 78}" font-size="40" font-weight="900" fill="{col}" opacity=".16" text-anchor="end">0{i + 1}</text>'
            f"</g>"
        )
    arrows = ""
    for i in range(3):
        ax = xs[i] + cw + 4
        arrows += (
            f'<g class="arrow" style="animation-delay:{0.50 + i * 0.16:.2f}s">'
            f'<line class="flow" x1="{ax}" y1="{y + 52}" x2="{ax + 12}" y2="{y + 52}" stroke="{SUB}" stroke-width="3" stroke-linecap="round"/>'
            f'<path d="M{ax + 8},{y + 46} L{ax + 16},{y + 52} L{ax + 8},{y + 58}" fill="none" stroke="{SUB}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>'
            f"</g>"
        )
    style = """  .head,.chip,.arrow,.metric{animation:fu .55s ease backwards}
  .flow{stroke-dasharray:5 7;animation:dash 1.6s linear infinite}
  .pulse{transform-box:fill-box;transform-origin:center;animation:pulse 3s ease-in-out infinite}
  @keyframes fu{from{opacity:0;transform:translateY(10px)}}
  @keyframes dash{to{stroke-dashoffset:-24}}
  @keyframes pulse{0%,100%{transform:scale(1);opacity:1}50%{transform:scale(1.15);opacity:.72}}"""
    body = (
        f"{card(1200, 390)}\n"
        f'<text class="head" x="50" y="60" font-size="12" letter-spacing="2.4" font-weight="800" fill="{OB}">THE EVIDENCE CIRCUIT</text>'
        f'<text class="head" x="50" y="88" font-size="24" font-weight="800" fill="{INK}">How {esc(BRAIN_TITLE)} turns sources into bounded decisions</text>'
        f"{subtitle_svg}{chips}{arrows}{metric_row(metrics(vault, repo))}"
        f'<g class="metric" style="animation-delay:1.12s"><rect x="866" y="308" width="292" height="54" rx="16" fill="#171D46" stroke="{LINE}"/><path d="M892 335c13-17 33-17 46 0-13 17-33 17-46 0z" fill="none" stroke="{CB}" stroke-width="2"/><circle cx="915" cy="335" r="6" fill="{CY}"/><text x="952" y="331" font-size="13" font-weight="800" fill="{INK}">inspect, challenge, stop</text><text x="952" y="350" font-size="12" fill="{SUB}">human authority stays outside the loop</text></g>'
    )
    return doc(1200, 390, f"{BRAIN_TITLE} relationship map", "Evidence moves through linked memory and protected gates into bounded decisions.", style, body, bg=CANVAS)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate vault visual assets.")
    parser.add_argument("--vault", required=True)
    args = parser.parse_args(argv)
    repo = Path(__file__).resolve().parent.parent
    vault = Path(args.vault).resolve()
    out = vault / "_attachments" / "brain-relationship-map.svg"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(build_svg(vault, repo), encoding="utf-8")
    print(out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
