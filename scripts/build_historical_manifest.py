#!/usr/bin/env python3
"""Build canonical Git blob SHA-256 manifest of historical idea files at base commit 3bf758f.

Uses canonical Git blob bytes from the Git object database at 3bf758f,
independent of working-tree line-ending configurations (CRLF/LF).
"""
from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTPUT_FILE = ROOT / "scripts" / "historical_manifest_3bf758f.json"
BASE_COMMIT = "3bf758f"


def get_git_tree_at_commit(commit: str) -> list[tuple[str, str, str]]:
    """Return list of (mode, blob_sha, rel_path) from git ls-tree."""
    cmd = ["git", "ls-tree", "-r", commit, "ideas"]
    res = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True, check=True)
    items = []
    for line in res.stdout.splitlines():
        if not line.strip():
            continue
        meta, rel_path = line.split("\t", 1)
        mode, kind, sha = meta.split()
        if kind == "blob":
            items.append((mode, sha, rel_path))
    return items


def get_git_blob_bytes(blob_sha: str) -> bytes:
    """Retrieve canonical blob bytes directly from git object database."""
    cmd = ["git", "cat-file", "blob", blob_sha]
    res = subprocess.run(cmd, cwd=ROOT, capture_output=True, check=True)
    return res.stdout


def build_manifest() -> dict:
    tree = get_git_tree_at_commit(BASE_COMMIT)
    file_hashes = {}
    blob_shas = {}

    for mode, sha, rel_path in tree:
        parts = rel_path.split("/")
        # Track raw, evidence, and output in ideas/<idea>/
        if len(parts) >= 3 and parts[0] == "ideas" and parts[2] in {"raw", "evidence", "output"}:
            blob_bytes = get_git_blob_bytes(sha)
            sha256 = hashlib.sha256(blob_bytes).hexdigest()
            file_hashes[rel_path] = sha256
            blob_shas[rel_path] = sha

    return {
        "base_commit": BASE_COMMIT,
        "description": "Canonical Git blob SHA-256 manifest of historical idea files at commit 3bf758f",
        "file_count": len(file_hashes),
        "files": file_hashes,
        "git_blob_shas": blob_shas,
    }


def main() -> None:
    manifest = build_manifest()
    OUTPUT_FILE.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"Recorded {manifest['file_count']} canonical Git blob hashes into {OUTPUT_FILE.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
