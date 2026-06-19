#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CARD = ROOT / "evidence" / "rxrx3_core_public_evidence_card.json"

FORBIDDEN_TRACKED_PATTERNS = [
    r"(^|/)\.env$",
    r"(^|/)\.ibm_quantum\.env$",
    r"(^|/)\.venv",
    r"(^|/)runs/",
    r"(^|/)data_real/",
    r"(^|/)data_public_matt/",
    r"\.jsonl$",
    r"\.ndjson$",
    r"\.db$",
    r"\.sqlite",
    r"operator_cards/",
    r"raw_identity_output\.json$",
    r"garden_full_run\.json$",
    r"themis_clean_root_.*\.zip$",
    r"themis_source_only_.*\.zip$",
]

SECRET_CONTENT_PATTERNS = [
    r"ghp_[A-Za-z0-9_]+",
    r"github_pat_[A-Za-z0-9_]+",
    r"sk-[A-Za-z0-9]{20,}",
    r"AKIA[0-9A-Z]{16}",
    r"-----BEGIN [A-Z ]*PRIVATE KEY-----",
]

def run(cmd: list[str]) -> str:
    proc = subprocess.run(
        cmd,
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if proc.returncode != 0:
        raise RuntimeError(
            f"command failed: {' '.join(cmd)}\nSTDOUT:\n{proc.stdout}\nSTDERR:\n{proc.stderr}"
        )
    return proc.stdout

def tracked_files() -> list[str]:
    return [line.strip() for line in run(["git", "ls-files"]).splitlines() if line.strip()]

def check_no_forbidden_tracked_files(files: list[str]) -> None:
    failures = []
    for f in files:
        normalized = f.replace("\\", "/")
        for pattern in FORBIDDEN_TRACKED_PATTERNS:
            if re.search(pattern, normalized):
                failures.append((f, pattern))

    if failures:
        for f, pattern in failures:
            print(f"FORBIDDEN_TRACKED_FILE {f} matched {pattern}")
        raise AssertionError("forbidden tracked files found")

def check_no_secret_content(files: list[str]) -> None:
    text_suffixes = {
        ".py", ".md", ".json", ".toml", ".yaml", ".yml", ".txt",
        ".sql", ".sh", ".ps1", ".cfg", ".ini", ".gitignore"
    }

    failures = []
    for rel in files:
        path = ROOT / rel
        if path.suffix.lower() not in text_suffixes:
            continue

        try:
            text = path.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue

        for pattern in SECRET_CONTENT_PATTERNS:
            if re.search(pattern, text):
                failures.append((rel, pattern))

    if failures:
        for rel, pattern in failures:
            print(f"SECRET_PATTERN {rel} matched {pattern}")
        raise AssertionError("secret-like content found")

def check_evidence_card() -> None:
    if not CARD.exists():
        raise AssertionError(f"missing evidence card: {CARD}")

    card = json.loads(CARD.read_text(encoding="utf-8-sig"))

    expected = {
        "kind": "themis_public_evidence_card",
        "dataset": "RxRx3-core",
        "rows": 222601,
        "metadata_columns": 11,
        "embedding_features": 384,
        "unique_well_ids": 222601,
        "unique_feature_digests": 222600,
        "duplicate_embedding_collision_rows": 2,
        "duplicate_embedding_digest": "923e8f259a606dd40355f0fe0b2cecc473dd3755cf7b3ed9c2403c34e2423d60",
        "themis_verdict": "CLOSED_WITH_RESIDUAL_CARRIED",
        "closure_score": "9 / 9",
        "unit_boundary_held": True,
        "no_radial_drift": True,
        "runtime_ms": 4210,
        "result_json_size_bytes": 185891563,
        "sefer_seal": "270968ffcd29de57b4a7fcb054d8e518fec610d7842b118f5645d8438b2c447b",
    }

    for key, value in expected.items():
        if card.get(key) != value:
            raise AssertionError(f"evidence mismatch for {key}: {card.get(key)!r} != {value!r}")

    counts = card.get("outcome_counts", {})
    for key in ["null", "unknown", "nonmatch", "error", "timeout", "break"]:
        if counts.get(key) != 0:
            raise AssertionError(f"outcome_counts.{key} must be 0, found {counts.get(key)!r}")

    if counts.get("success") != 9:
        raise AssertionError(f"outcome_counts.success must be 9, found {counts.get('success')!r}")

    collision = card.get("duplicate_collision", [])
    if len(collision) != 2:
        raise AssertionError("duplicate_collision must contain exactly 2 rows")

    genes = {row.get("gene") for row in collision}
    if genes != {"PLK1", "AKR1C3"}:
        raise AssertionError(f"unexpected collision genes: {genes!r}")

    labels = {row.get("well_type_label") for row in collision}
    required_labels = {"CRISPR Gene Positive Controls", "Query guides"}
    if not required_labels.issubset(labels):
        raise AssertionError(f"unexpected collision labels: {labels!r}")

def main() -> int:
    files = tracked_files()
    check_no_forbidden_tracked_files(files)
    check_no_secret_content(files)
    check_evidence_card()

    print("THEMIS PUBLIC HARNESS: PASS")
    print(f"tracked_files_checked: {len(files)}")
    print("no_confidential_tracked_files: true")
    print("no_secret_patterns_detected: true")
    print("rxrx3_public_evidence_card_valid: true")
    print("duplicate_embedding_collision_preserved: true")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
