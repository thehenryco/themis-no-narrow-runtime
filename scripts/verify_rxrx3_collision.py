#!/usr/bin/env python3
"""
Optional independent verifier for the RxRx3-core duplicate embedding collision.

Usage:
  python scripts/verify_rxrx3_collision.py --rxrx3-dir path/to/rxrx3_core

Expected local files:
  metadata_rxrx3_core.csv
  OpenPhenom_rxrx3_core_embeddings.parquet
"""

from __future__ import annotations

import argparse
import hashlib
from pathlib import Path

import numpy as np
import pandas as pd


EXPECTED_DIGEST = "923e8f259a606dd40355f0fe0b2cecc473dd3755cf7b3ed9c2403c34e2423d60"


def feature_digest(row) -> str:
    arr = np.asarray(row, dtype=np.float64)
    return hashlib.sha256(arr.tobytes()).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--rxrx3-dir", required=True, help="Directory containing RxRx3-core files")
    args = parser.parse_args()

    root = Path(args.rxrx3_dir)
    meta_files = list(root.rglob("metadata_rxrx3_core.csv"))
    emb_files = list(root.rglob("OpenPhenom_rxrx3_core_embeddings.parquet"))

    if not meta_files:
        raise SystemExit("metadata_rxrx3_core.csv not found")
    if not emb_files:
        raise SystemExit("OpenPhenom_rxrx3_core_embeddings.parquet not found")

    meta = pd.read_csv(meta_files[0], dtype=str, low_memory=False)
    emb = pd.read_parquet(emb_files[0])

    feature_cols = [c for c in emb.columns if c.startswith("feature_")]
    if len(feature_cols) != 384:
        raise SystemExit(f"expected 384 feature columns, found {len(feature_cols)}")

    df = emb.merge(meta, on="well_id", how="left", validate="one_to_one")
    X = df[feature_cols].astype("float64").to_numpy()
    X = np.nan_to_num(X, nan=0.0, posinf=0.0, neginf=0.0)

    digests = [feature_digest(row) for row in X]
    df = df.copy()
    df["sample_index"] = range(len(df))
    df["feature_digest_sha256"] = digests

    dups = df[df.duplicated("feature_digest_sha256", keep=False)].sort_values("feature_digest_sha256")

    print("rows:", len(df))
    print("feature_columns:", len(feature_cols))
    print("unique_well_ids:", df["well_id"].nunique())
    print("unique_feature_digests:", pd.Series(digests).nunique())
    print("duplicate_rows:", len(dups))

    if len(dups) != 2:
        raise SystemExit("expected exactly 2 duplicate embedding rows")

    digest_set = set(dups["feature_digest_sha256"])
    if digest_set != {EXPECTED_DIGEST}:
        raise SystemExit(f"unexpected duplicate digest set: {digest_set}")

    cols = [
        "sample_index",
        "well_id",
        "experiment_name",
        "plate",
        "address",
        "gene",
        "treatment",
        "SMILES",
        "perturbation_type",
        "cell_type",
        "well_type_label",
        "feature_digest_sha256",
    ]

    print(dups[cols].to_string(index=False))
    print("RXRX3 COLLISION VERIFIER: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
