#!/usr/bin/env python3
"""Build canonical SHA-256 manifest of historical idea files at base commit 3bf758f."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
IDEAS_DIR = ROOT / "ideas"
OUTPUT_FILE = ROOT / "scripts" / "historical_manifest_3bf758f.json"


def compute_sha256(path: Path) -> str:
    hasher = hashlib.sha256()
    with path.open("rb") as f:
        while chunk := f.read(65536):
            hasher.update(chunk)
    return hasher.hexdigest()


def build_manifest() -> dict[str, str]:
    manifest = {}
    for path in sorted(IDEAS_DIR.rglob("*")):
        if path.is_file():
            # Only track raw, evidence, and output directories
            rel_parts = path.relative_to(ROOT).parts
            if len(rel_parts) >= 3 and rel_parts[0] == "ideas" and rel_parts[2] in {"raw", "evidence", "output"}:
                rel_path = path.relative_to(ROOT).as_posix()
                manifest[rel_path] = compute_sha256(path)
    return manifest


def main() -> None:
    manifest = build_manifest()
    payload = {
        "base_commit": "3bf758f",
        "description": "Historical immutability manifest for ideas raw/evidence/output files",
        "file_count": len(manifest),
        "files": manifest,
    }
    OUTPUT_FILE.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"Recorded {len(manifest)} files into {OUTPUT_FILE.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
