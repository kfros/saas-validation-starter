#!/usr/bin/env python3
"""Seal a Stage 1 v2 review snapshot deterministically without python -c.

Computes canonical SHA-256 file hashes, binds reviewed/blocked IDs from review-log.jsonl,
and generates/updates ideas/<idea>/reassessment-v2/evidence/snapshot.json.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

SCRIPTS_DIR = str(Path(__file__).resolve().parent)
if SCRIPTS_DIR not in sys.path:
    sys.path.insert(0, SCRIPTS_DIR)
import stage1_policy

ROOT = Path(__file__).resolve().parents[1]
BASE_COMMIT = "3bf758f"
REQUIRED_FILES = (
    "evidence.jsonl",
    "scope-map.json",
    "review-log.jsonl",
    "audit-summary.md",
    "high-impact-review.md",
)


def compute_sha256(path: Path) -> str:
    hasher = hashlib.sha256()
    with path.open("rb") as f:
        while chunk := f.read(65536):
            hasher.update(chunk)
    return hasher.hexdigest()


def get_head_commit() -> str:
    try:
        res = subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT, capture_output=True, text=True, check=True)
        return res.stdout.strip()
    except Exception:
        return "uncommitted"


def seal_snapshot(idea: str, snapshot_id: str | None = None, unexamined_budget: str = "Bounded budget complete.") -> Path:
    ev_dir = ROOT / "ideas" / idea / "reassessment-v2" / "evidence"
    if not ev_dir.is_dir():
        raise stage1_policy.PolicyError(f"missing v2 evidence directory: {ev_dir.relative_to(ROOT)}")

    # Verify required files exist
    for name in REQUIRED_FILES:
        fpath = ev_dir / name
        if not fpath.is_file():
            raise stage1_policy.PolicyError(f"missing required snapshot file: {name}")

    # Compute hashes
    file_hashes = {}
    for name in REQUIRED_FILES:
        file_hashes[name] = compute_sha256(ev_dir / name)

    # Read evidence.jsonl
    evidence_records = {}
    for line in (ev_dir / "evidence.jsonl").read_text(encoding="utf-8").splitlines():
        if line.strip():
            rec = json.loads(line)
            evidence_records[rec["id"]] = rec

    # Parse scope-map.json
    scope_records = {}
    scope_path = ev_dir / "scope-map.json"
    if scope_path.is_file():
        scope_data = json.loads(scope_path.read_text(encoding="utf-8"))
        for entry in scope_data.get("records", []):
            if isinstance(entry, dict) and "evidence_id" in entry:
                scope_records[entry["evidence_id"]] = entry

    # Load baseline records
    baseline_records = stage1_policy.load_historical_baseline_evidence(idea, repo_root=ROOT)

    # Parse and validate review-log.jsonl
    review_log_entries = stage1_policy.validate_review_log(
        ev_dir / "review-log.jsonl",
        evidence_records=evidence_records,
        scope_records=scope_records,
        baseline_records=baseline_records,
    )

    reviewed_ids = [
        eid for eid, entry in review_log_entries.items()
        if entry["retrieval_outcome"] == "SUCCESS"
    ]
    blocked_ids = [
        eid for eid, entry in review_log_entries.items()
        if entry["retrieval_outcome"] in {"BLOCKED", "NOT_FOUND", "ERROR"}
    ]
    repaired_ids = [
        eid for eid, entry in review_log_entries.items()
        if entry.get("repaired", False) or bool(entry.get("repaired_fields")) or bool(entry.get("modifications"))
    ]

    snap_id = snapshot_id or f"snap-{idea}-v2-{datetime.now(timezone.utc).strftime('%Y%m%d%H%M%S')}"
    tooling_commit = get_head_commit()

    payload = {
        "snapshot_id": snap_id,
        "created_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "source_baseline_commit": BASE_COMMIT,
        "tooling_commit": tooling_commit,
        "idea_id": idea,
        "policy_version": "v2",
        "files": file_hashes,
        "reviewed_evidence_ids": reviewed_ids,
        "blocked_evidence_ids": blocked_ids,
        "repaired_evidence_ids": repaired_ids,
        "unexamined_budget_remaining": unexamined_budget,
    }

    snap_file = ev_dir / "snapshot.json"
    snap_file.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    # Validate sealed snapshot
    stage1_policy.validate_v2_snapshot(
        payload,
        ev_dir,
        review_log_entries=review_log_entries,
        evidence_records=evidence_records,
        expected_idea_id=idea,
    )
    print(f"OK: sealed snapshot {snap_id} in {snap_file.relative_to(ROOT)}")
    return snap_file


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--idea", required=True, help="Idea name (e.g. geo-monitoring, deck-automation)")
    parser.add_argument("--snapshot-id", default=None, help="Optional snapshot ID")
    parser.add_argument("--budget-notes", default="Bounded budget complete.", help="Unexamined budget notes")
    args = parser.parse_args()

    try:
        seal_snapshot(args.idea, args.snapshot_id, args.budget_notes)
        return 0
    except (stage1_policy.PolicyError, OSError, ValueError) as exc:
        print(f"FAILED: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
