#!/usr/bin/env python3
"""Regenerate README.md from data/events.json.

Run from the repository root:  python3 scripts/build_readme.py
"""
import json
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
data = json.loads((ROOT / "data" / "events.json").read_text(encoding="utf-8"))
events = data["events"]
today = date.today().isoformat()


def when(ev):
    d = date.fromisoformat(ev["date"])
    s = d.strftime("%-d %b %Y")
    if ev.get("end_date"):
        e = date.fromisoformat(ev["end_date"])
        s = f"{d.day}–{e.strftime('%-d %b %Y')}" if (d.month, d.year) == (e.month, e.year) else f"{s} – {e.strftime('%-d %b %Y')}"
    return s


def place(ev):
    if ev.get("mode") == "online":
        return "Online"
    venue, city = ev.get("venue"), ev.get("city")
    if venue and city and city in venue:
        city = None
    return ", ".join(x for x in (venue, city, ev.get("country")) if x)


def links(ev):
    out = []
    l = ev.get("links", {})
    if l.get("slides"):
        out.append(f"[Slides]({l['slides']})")
    if l.get("recording"):
        out.append(f"[Recording]({l['recording']})")
    if l.get("event"):
        out.append(f"[Event]({l['event']})")
    return " · ".join(out) or "–"


def table(rows):
    lines = ["| Date | Event | Talk | Role | Where | Links |", "|---|---|---|---|---|---|"]
    for ev in rows:
        talk = ev.get('title', '') + (f" (with {', '.join(ev['with'])})" if ev.get('with') else '')
        lines.append(f"| {when(ev)} | {ev['event']} | {talk} | {ev.get('role', '')} | {place(ev)} | {links(ev)} |")
    return "\n".join(lines)


upcoming = sorted([e for e in events if (e.get("end_date") or e["date"]) >= today], key=lambda e: e["date"])
past = sorted([e for e in events if (e.get("end_date") or e["date"]) < today], key=lambda e: e["date"], reverse=True)

parts = [
    "# Talks",
    "",
    "Talks, workshops and training by [Samantha Cruz](https://github.com/sammcruz), Data Engineering Team Lead: Microsoft Fabric, Databricks, data agents and AI data pipelines. Browse them with filters on [sammcruz.github.io/talks](https://sammcruz.github.io/talks.html).",
    "",
    "Slides are in [`slides/`](slides) as PDF, named `YYYY-MM-DD-event.pdf`. The single source of truth is [`data/events.json`](data/events.json); this README and my website are generated from it.",
    "",
]
if upcoming:
    parts += ["## Upcoming", "", table(upcoming), ""]
parts += ["## Past events", "", table(past), ""]
parts += [
    "## Use of the slides",
    "",
    "Slides are shared for learning. Please credit the author when you reuse parts of them. Some talks use event or sponsor templates; those logos belong to their owners.",
    "",
    "## Add an event",
    "",
    "1. Add an object to `data/events.json` (copy an existing one).",
    "2. Put the PDF in `slides/` and reference it in `links.slides`.",
    "3. Run `python3 scripts/build_readme.py` and commit.",
    "",
]
(ROOT / "README.md").write_text("\n".join(parts), encoding="utf-8")
print(f"README.md written: {len(upcoming)} upcoming, {len(past)} past")
