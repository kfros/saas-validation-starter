#!/usr/bin/env python3
"""Lightweight structural validator for Stage 1 JSONL evidence.
Uses only Python stdlib so it can run anywhere.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

REQUIRED = {
    "id", "idea", "type", "observed_at", "source_type", "source_tier",
    "source_url", "observation", "interpretation", "polarity", "strength",
    "independence_key", "agent", "audit_status"
}

ENUMS = {
    "type": {"market", "pain", "wtp", "recurrence", "workflow", "gap", "reachability", "substitute", "risk"},
    "source_tier": {"A", "B", "C"},
    "polarity": {"supports", "contradicts", "neutral"},
    "audit_status": {"PENDING", "VERIFIED", "PARTIALLY_VERIFIED", "REJECTED"},
}


def validate_record(rec: dict, file: Path, line_no: int) -> list[str]:
    errors: list[str] = []
    missing = sorted(REQUIRED - rec.keys())
    if missing:
        errors.append(f"missing required fields: {', '.join(missing)}")
    for field, allowed in ENUMS.items():
        if field in rec and rec[field] not in allowed:
            errors.append(f"invalid {field}={rec[field]!r}")
    if "strength" in rec and (not isinstance(rec["strength"], int) or not 1 <= rec["strength"] <= 5):
        errors.append("strength must be integer 1..5")
    if "source_url" in rec and not isinstance(rec["source_url"], str):
        errors.append("source_url must be string")
    if "observation" in rec and (not isinstance(rec["observation"], str) or len(rec["observation"].strip()) < 10):
        errors.append("observation too short")
    return [f"{file}:{line_no}: {e}" for e in errors]


def main() -> int:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("ideas/deck-automation/raw")
    files = sorted(root.rglob("evidence.jsonl")) if root.is_dir() else [root]
    if not files:
        print(f"No evidence.jsonl files found under {root}")
        return 2

    errors: list[str] = []
    records = 0
    ids: dict[str, str] = {}
    for file in files:
        with file.open("r", encoding="utf-8") as f:
            for line_no, raw in enumerate(f, 1):
                raw = raw.strip()
                if not raw:
                    continue
                try:
                    rec = json.loads(raw)
                except json.JSONDecodeError as exc:
                    errors.append(f"{file}:{line_no}: invalid JSON: {exc}")
                    continue
                if not isinstance(rec, dict):
                    errors.append(f"{file}:{line_no}: record must be JSON object")
                    continue
                records += 1
                errors.extend(validate_record(rec, file, line_no))
                rid = rec.get("id")
                if rid:
                    where = f"{file}:{line_no}"
                    if rid in ids:
                        errors.append(f"{where}: duplicate id {rid!r}; first seen {ids[rid]}")
                    else:
                        ids[rid] = where

    print(f"Validated {records} records from {len(files)} file(s).")
    if errors:
        print(f"FAILED with {len(errors)} issue(s):")
        for e in errors:
            print(f"- {e}")
        return 1
    print("OK: no structural issues found.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
