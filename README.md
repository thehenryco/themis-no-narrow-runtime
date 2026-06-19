# Themis No-Narrow Runtime

Themis is a no-narrow identity-preservation runtime.

## Public Result

Themis was run against RxRx3-core, a public biological embedding dataset.

| Item | Value |
|---|---:|
| Dataset rows | 222,601 |
| Metadata columns | 11 |
| Embedding features | 384 |
| Unique well IDs | 222,601 |
| Unique feature digests | 222,600 |
| Duplicate embedding collision rows | 2 |
| Runtime verdict | CLOSED_WITH_RESIDUAL_CARRIED |
| Closure score | 9 / 9 |
| Unit boundary held | true |
| No radial drift | true |
| Error outcomes | 0 |
| Timeout outcomes | 0 |
| Null outcomes | 0 |
| Runtime milliseconds | 4,210 |
| Full result JSON size | 185,891,563 bytes |

## Public Collision Event

The run found one duplicate 384-feature embedding digest across two distinct biological identities.

Shared digest:

923e8f259a606dd40355f0fe0b2cecc473dd3755cf7b3ed9c2403c34e2423d60

| sample_index | well_id | gene | treatment | perturbation_type | cell_type | label |
|---:|---|---|---|---|---|---|
| 192182 | gene-134_2_L39 | PLK1 | PLK1_guide_1 | CRISPR | HUVEC | CRISPR Gene Positive Controls |
| 192184 | gene-134_2_N26 | AKR1C3 | AKR1C3_guide_5 | CRISPR | HUVEC | Query guides |

The collision was not dropped, hidden, or narrowed away. It was preserved as an identity event.

## No-Narrow Contract

Every state must land somewhere.
Every field must be accounted for.
Every collision must remain visible.
Every residual must be carried.
Every quarantine must be recorded.
Every failure must be preserved as an outcome.
No filter may silently delete a field or state.

## Run Public Harness

python tests/public_harness.py

Expected:

THEMIS PUBLIC HARNESS: PASS

## Core Principle

Identity is the authority of the system.

Tools can compute.
Runtimes can route.
Ledgers can record.

The system is valid only if identity is preserved, residuals are carried, and no state is silently narrowed away.
