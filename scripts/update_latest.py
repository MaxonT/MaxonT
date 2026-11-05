"""Rewrite the Latest projects table in README.md and README.zh-CN.md.

Reads MaxonT's public repos from the GitHub API, keeps the most recently
pushed ones (skipping the profile repo, forks, archived repos and the
flagship systems already shown as cards) and replaces the text between
the LATEST markers. Stdlib only.

    python3 scripts/update_latest.py                  # live API
    python3 scripts/update_latest.py --from-file x.json
"""
from __future__ import annotations

import argparse
import json
import os
import re
import urllib.request
from pathlib import Path

USER = "MaxonT"
LIMIT = 7
SKIP = {"maxont", "aisync", "traces.md", "existence-trace"}
ROOT = Path(__file__).resolve().parents[1]
FILES = {
    "README.md": ("Project", "Updated", "What it is"),
    "README.zh-CN.md": ("项目", "更新", "做什么"),
}
START, END = "<!-- LATEST:START -->", "<!-- LATEST:END -->"


def fetch() -> list[dict]:
    url = f"https://api.github.com/users/{USER}/repos?type=owner&sort=pushed&per_page=100"
    req = urllib.request.Request(url, headers={"Accept": "application/vnd.github+json"})
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.load(resp)


def pick(repos: list[dict]) -> list[dict]:
    keep = [
        r for r in repos
        if not r.get("private") and not r.get("fork") and not r.get("archived")
        and r["name"].lower() not in SKIP and "archived" not in r["name"].lower()
    ]
    keep.sort(key=lambda r: r["pushed_at"], reverse=True)
    return keep[:LIMIT]


def clean(text: str | None) -> str:
    # The profile avoids dashes, and table cells cannot hold pipes.
    text = (text or "").replace("|", "/")
    text = re.sub(r"\s*[—–]\s*", ", ", text).strip(" ,")
    return text if len(text) <= 100 else text[:97].rstrip() + "..."


def table(repos: list[dict], cols: tuple[str, str, str]) -> str:
    name, updated, what = cols
    rows = [f"| {name} | ⭐ | {updated} | {what} |", "|:--|:-:|:-:|:--|"]
    for r in repos:
        n = r["name"]
        badge = f"https://img.shields.io/github/stars/{USER}/{n}?style=flat-square&label=&color=F5C518"
        rows.append(
            f"| [**{n}**](https://github.com/{USER}/{n}) | ![]({badge}) "
            f"| {r['pushed_at'][:10]} | {clean(r.get('description'))} |"
        )
    return "\n".join(rows)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--from-file", help="read repos JSON from a file instead of the API")
    args = ap.parse_args()
    repos = json.loads(Path(args.from_file).read_text()) if args.from_file else fetch()
    chosen = pick(repos)
    for fname, cols in FILES.items():
        path = ROOT / fname
        text = path.read_text(encoding="utf-8")
        if START not in text or END not in text:
            raise SystemExit(f"{fname}: missing {START} / {END} markers")
        block = f"{START}\n{table(chosen, cols)}\n{END}"
        text = re.sub(re.escape(START) + r".*?" + re.escape(END), lambda _: block, text, flags=re.S)
        path.write_text(text, encoding="utf-8")
    print("latest:", ", ".join(r["name"] for r in chosen))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
