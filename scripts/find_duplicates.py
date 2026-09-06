#!/usr/bin/env python3
"""Reports likely duplicate evidence by URL and independence_key."""
from __future__ import annotations

import json
import sys
from collections import defaultdict
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit, parse_qsl, urlencode

TRACKING_PREFIXES = ("utm_",)
TRACKING_KEYS = {"ref", "source", "fbclid", "gclid"}


def canonical_url(url: str) -> str:
    try:
        p = urlsplit(url)
        kept = []
        for k, v in parse_qsl(p.query, keep_blank_values=True):
            if k.lower().startswith(TRACKING_PREFIXES) or k.lower() in TRACKING_KEYS:
                continue
            kept.append((k, v))
        path = p.path.rstrip("/") or "/"
        return urlunsplit((p.scheme.lower(), p.netloc.lower(), path, urlencode(kept), ""))
    except Exception:
        return url


def main() -> int:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("ideas/deck-automation/raw")
    files = sorted(root.rglob("evidence.jsonl")) if root.is_dir() else [root]
    by_url = defaultdict(list)
    by_key = defaultdict(list)

    for file in files:
        with file.open("r", encoding="utf-8") as f:
            for line_no, raw in enumerate(f, 1):
                raw = raw.strip()
                if not raw:
                    continue
                try:
                    rec = json.loads(raw)
                except json.JSONDecodeError:
                    continue
                loc = f"{file}:{line_no}:{rec.get('id', '?')}"
                if rec.get("source_url"):
                    by_url[canonical_url(rec["source_url"])].append(loc)
                if rec.get("independence_key"):
                    by_key[rec["independence_key"]].append(loc)

    url_dupes = {k: v for k, v in by_url.items() if len(v) > 1}
    key_dupes = {k: v for k, v in by_key.items() if len(v) > 1}

    print(f"Duplicate canonical URLs: {len(url_dupes)}")
    for k, vals in sorted(url_dupes.items()):
        print(f"\nURL {k}")
        for v in vals:
            print(f"  - {v}")

    print(f"\nRepeated independence keys: {len(key_dupes)}")
    for k, vals in sorted(key_dupes.items()):
        print(f"\nKEY {k}")
        for v in vals:
            print(f"  - {v}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
