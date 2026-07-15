#!/usr/bin/env python3
"""Rebuild the 'Fresh off the push' section of README.md from the GitHub API.

Design rule: if anything fails, leave the README exactly as it is and exit 0.
A stale section is fine; a broken profile is not.
"""

import json
import os
import sys
import urllib.request
from datetime import datetime, timezone

USER = "V-prajit"
EXCLUDE = {"V-prajit", "sdgfhgjk", "CTextEditor"}
START = "<!-- recent starts -->"
END = "<!-- recent ends -->"


def fetch_repos():
    req = urllib.request.Request(
        f"https://api.github.com/users/{USER}/repos?sort=pushed&per_page=50",
        headers={"Accept": "application/vnd.github+json", "User-Agent": USER},
    )
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(req, timeout=20) as r:
        return json.load(r)


def main():
    try:
        repos = fetch_repos()
    except Exception as e:
        print(f"API unavailable, keeping the current section ({e})")
        return 0

    rows = []
    for r in repos:
        if r.get("fork") or r.get("private") or r["name"] in EXCLUDE:
            continue
        desc = (r.get("description") or "").strip()
        pushed = r["pushed_at"][:10]
        line = f"- [{r['name']}]({r['html_url']})"
        if desc:
            line += f" · {desc}"
        line += f" · pushed {pushed}"
        rows.append(line)
        if len(rows) == 5:
            break

    if not rows:
        print("No rows produced, keeping the current section")
        return 0

    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    block = "\n".join([START] + rows + [f"\n<sub>Last self-update: {stamp}</sub>", END])

    readme = open("README.md").read()
    if START not in readme or END not in readme:
        print("Markers missing, refusing to touch README")
        return 0
    head, rest = readme.split(START, 1)
    _, tail = rest.split(END, 1)
    new = head + block + tail
    if new != readme:
        open("README.md", "w").write(new)
        print("README section rebuilt")
    else:
        print("No changes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
