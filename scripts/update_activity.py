"""Draw the last 30 days of contributions as assets/activity.svg.

Reads MaxonT's public contribution calendar from the GitHub GraphQL API and
writes a small dark area chart, so the profile has no third-party image that
can run out of quota. Needs GITHUB_TOKEN. Stdlib only.

    GITHUB_TOKEN=... python3 scripts/update_activity.py
    python3 scripts/update_activity.py --from-file days.json   # [{"date": "...", "count": 3}, ...]
"""
from __future__ import annotations

import argparse
import json
import os
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path

USER = "MaxonT"
DAYS = 30
OUT = Path(__file__).resolve().parents[1] / "assets" / "activity.svg"
QUERY = """query($login:String!,$from:DateTime!,$to:DateTime!){user(login:$login){
contributionsCollection(from:$from,to:$to){contributionCalendar{totalContributions
weeks{contributionDays{date contributionCount}}}}}}"""


def fetch() -> list[dict]:
    now = datetime.now(timezone.utc)
    body = {"query": QUERY, "variables": {
        "login": USER,
        "from": (now - timedelta(days=DAYS + 1)).strftime("%Y-%m-%dT00:00:00Z"),
        "to": now.strftime("%Y-%m-%dT%H:%M:%SZ")}}
    req = urllib.request.Request(
        "https://api.github.com/graphql", data=json.dumps(body).encode(),
        headers={"Authorization": f"Bearer {os.environ['GITHUB_TOKEN']}", "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        data = json.load(resp)
    if "errors" in data:
        raise SystemExit(f"GraphQL error: {data['errors']}")
    weeks = data["data"]["user"]["contributionsCollection"]["contributionCalendar"]["weeks"]
    days = [{"date": d["date"], "count": d["contributionCount"]} for w in weeks for d in w["contributionDays"]]
    return days


def svg(days: list[dict]) -> str:
    days = sorted(days, key=lambda d: d["date"])[-DAYS:]
    w, h, left, right, top, bottom = 840, 220, 44, 24, 54, 34
    peak = max([d["count"] for d in days] + [4])
    peak = (peak + 3) // 4 * 4
    px = lambda i: left + i * (w - left - right) / max(len(days) - 1, 1)
    py = lambda v: top + (h - top - bottom) * (1 - v / peak)
    pts = [(px(i), py(d["count"])) for i, d in enumerate(days)]
    line = " ".join(f"{x:.1f},{y:.1f}" for x, y in pts)
    area = f"{left},{h - bottom} {line} {pts[-1][0]:.1f},{h - bottom}"
    total = sum(d["count"] for d in days)
    grid = "".join(
        f'<line x1="{left}" x2="{w - right}" y1="{py(v):.1f}" y2="{py(v):.1f}" stroke="#2f2b4a" stroke-width="1"/>'
        f'<text x="{left - 8}" y="{py(v) + 4:.1f}" text-anchor="end" fill="#a9a7c4" font-size="11">{v}</text>'
        for v in range(0, peak + 1, peak // 4))
    ticks = "".join(
        f'<text x="{px(i):.1f}" y="{h - 12}" text-anchor="middle" fill="#a9a7c4" font-size="11">{days[i]["date"][5:]}</text>'
        for i in range(0, len(days), 6))
    dots = "".join(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="2.6" fill="#f8d847"/>' for x, y in pts)
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" role="img" aria-label="Contributions in the last {DAYS} days: {total}" font-family="Segoe UI, Ubuntu, sans-serif">
<defs><linearGradient id="fill" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fe428e" stop-opacity=".55"/><stop offset="1" stop-color="#fe428e" stop-opacity="0"/></linearGradient></defs>
<rect width="{w}" height="{h}" rx="10" fill="#141321"/>
<text x="{left}" y="30" fill="#fe428e" font-size="16" font-weight="600">MaxonT contributions, last {DAYS} days: {total}</text>
{grid}{ticks}
<polygon points="{area}" fill="url(#fill)"/>
<polyline points="{line}" fill="none" stroke="#fe428e" stroke-width="2.2" stroke-linejoin="round"/>
{dots}
</svg>
"""


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--from-file")
    args = ap.parse_args()
    days = json.loads(Path(args.from_file).read_text()) if args.from_file else fetch()
    if len(days) < 2:
        raise SystemExit("not enough days returned, keeping the old chart")
    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(svg(days), encoding="utf-8")
    print("activity:", sum(d["count"] for d in days[-DAYS:]), "contributions in", min(len(days), DAYS), "days")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
