## Summary

This issue records a reproducible identity-collision observation from the public RxRx3-core OpenPhenom embedding release.

Using the public metadata_rxrx3_core.csv and OpenPhenom_rxrx3_core_embeddings.parquet files, the verifier in this repository identifies one duplicate 384-feature embedding digest across two distinct biological metadata identities.

This is not being filed as an accusation or claim of dataset error. The question is whether consumers of RxRx3-core/OpenPhenom embeddings should treat embedding vectors or embedding digests as non-unique representation states rather than identity keys.

## Public verifier result

rows: 222601
feature_columns: 384
unique_well_ids: 222601
unique_feature_digests: 222600
duplicate_rows: 2
RXRX3 COLLISION VERIFIER: PASS

## Duplicate embedding digest

923e8f259a606dd40355f0fe0b2cecc473dd3755cf7b3ed9c2403c34e2423d60

## Duplicate rows

| sample_index | well_id | experiment_name | plate | address | gene | treatment | perturbation_type | cell_type | well_type_label |
|---:|---|---|---:|---|---|---|---|---|---|
| 192182 | gene-134_2_L39 | gene-134 | 2 | L39 | PLK1 | PLK1_guide_1 | CRISPR | HUVEC | CRISPR Gene Positive Controls |
| 192184 | gene-134_2_N26 | gene-134 | 2 | N26 | AKR1C3 | AKR1C3_guide_5 | CRISPR | HUVEC | Query guides |

## Why this matters

The two rows have distinct well_id, address, gene, treatment, and well_type_label values, but the same 384-feature embedding digest.

For downstream consumers, this suggests that embedding equality should not be treated as biological identity equality without carrying metadata identity alongside the embedding.

## Reproduction

Repo:

https://github.com/thehenryco/themis-no-narrow-runtime

Install:

python -m venv .venv_public
.\.venv_public\Scripts\Activate.ps1
python -m pip install -U pip
python -m pip install -r requirements-rxrx3.txt

Run against a local RxRx3-core download:

python scripts\verify_rxrx3_collision.py --rxrx3-dir <path-to-local-rxrx3_core>

Expected:

RXRX3 COLLISION VERIFIER: PASS

## Themis surface verification packet

Themis processed the full public RxRx3-core carrier and preserved this duplicate embedding event without silently narrowing it away.

Public evidence card:

evidence/rxrx3_core_public_evidence_card.json

The public harness also passes:

THEMIS PUBLIC HARNESS: PASS

## Question

Is this duplicate embedding vector expected behavior for OpenPhenom/RxRx3-core?

If yes, would the maintainers recommend documenting that consumers should preserve well_id and metadata identity separately from embedding-vector equality?

## Surface verification pack

The public verification packet is here:

evidence/rxrx3_surface_verification_pack/README.md

Full current Themis surface voice:

evidence/rxrx3_surface_verification_pack/THEMIS_FINAL_FULL_CURRENT_SURFACE_VERIFICATION_VOICE.md

This packet preserves the boundary: Themis reports a surface verification frontier, not a final biological mechanism.
