# RXRX3 Biological Frontier — Sefer English

Mode: source-field translation and question routing.

This document does not assert a new biological mechanism. It translates the RxRx3 Sefer/runtime fields into scientist-facing questions and next checks.

## What was seen

- Dataset: `RxRx3-core`
- Sample count: `222601`
- Observed event: `same 384-feature embedding digest across distinct metadata identities`
- Shared digest: `923e8f259a606dd40355f0fe0b2cecc473dd3755cf7b3ed9c2403c34e2423d60`
- First identity: `PLK1 / PLK1_guide_1 / CRISPR Gene Positive Controls`
- Second identity: `AKR1C3 / AKR1C3_guide_5 / Query guides`

## Metadata rows

### Row 1

- `address`: `L39`
- `cell_type`: `HUVEC`
- `experiment_name`: `gene-134`
- `gene`: `PLK1`
- `perturbation_type`: `CRISPR`
- `plate`: `2`
- `treatment`: `PLK1_guide_1`
- `well_id`: `gene-134_2_L39`
- `well_type_label`: `CRISPR Gene Positive Controls`

### Row 2

- `address`: `N26`
- `cell_type`: `HUVEC`
- `experiment_name`: `gene-134`
- `gene`: `AKR1C3`
- `perturbation_type`: `CRISPR`
- `plate`: `2`
- `treatment`: `AKR1C3_guide_5`
- `well_id`: `gene-134_2_N26`
- `well_type_label`: `Query guides`

## What is shared between the two rows

- `cell_type`: `HUVEC`
- `experiment_name`: `gene-134`
- `perturbation_type`: `CRISPR`
- `plate`: `2`

## What differs between the two rows

- `address`:
  - Row 1: `L39`
  - Row 2: `N26`
- `gene`:
  - Row 1: `PLK1`
  - Row 2: `AKR1C3`
- `treatment`:
  - Row 1: `PLK1_guide_1`
  - Row 2: `AKR1C3_guide_5`
- `well_id`:
  - Row 1: `gene-134_2_L39`
  - Row 2: `gene-134_2_N26`
- `well_type_label`:
  - Row 1: `CRISPR Gene Positive Controls`
  - Row 2: `Query guides`

## Runtime state

- Identity preserved: `True`
- Witness operator: `witness_passive_observation`
- Delta event under witness: `0`
- Backaction: `0`
- Source unchanged: `True`
- Unit boundary held: `True`
- No radial drift: `True`
- Carried object: `theta_axis10_residual_star`
- Carried object status: `RESIDUAL_CARRIED`
- Closure verdict: `CLOSED_WITH_RESIDUAL_CARRIED`
- Closure score: `9 / 9`

## Frontier paths for scientist

### identity-accounting path

Question opened: When two distinct metadata identities share one embedding digest, what identity relation must downstream analysis preserve?

Why it matters: The sample reports identity preservation as true while the representation digest is shared.

Next checks:
- Keep well_id, gene, treatment, plate, address, cell_type, perturbation_type, and well_type_label attached to every embedding row.
- Do not use embedding equality alone as biological identity equality.
- Report the equality as a representation event plus metadata distinction.

### metadata-alignment path

Question opened: Does the shared digest arise from metadata alignment, export alignment, feature duplication, or intended representation degeneracy?

Why it matters: The two wells carry different identities while the digest is identical.

Next checks:
- Check whether the two well_ids map to different source images or image sets.
- Check whether feature extraction/export duplicated a vector.
- Check whether metadata row order and embedding row order are aligned.
- Check whether either well is a control/query alias or normalization artifact.

### biological-review path

Question opened: What biological interpretation, if any, is justified when distinct perturbation identities share the same representation?

Why it matters: The sample alone shows representation equality, not biological equivalence.

Next checks:
- Ask a domain scientist whether PLK1 guide/control and AKR1C3 query guide should ever collapse at the embedding level.
- Review whether both rows share cell type and perturbation modality.
- Separate biological equivalence, representation degeneracy, and data-pipeline duplication as different hypotheses.

### frontier-discovery path

Question opened: What new question is opened by carrying the unresolved identity gap instead of resolving it away?

Why it matters: The runtime names theta_axis10_residual_star as the remaining carried object and lands the finding as a carried-residual discovery record.

Next checks:
- Treat the event as a prompt for follow-up curation, not as a final biological conclusion.
- Create a review queue for exact embedding duplicates across distinct biological metadata.
- Rank similar events by whether they cross gene, guide, control/query, experiment, plate, or cell-type boundaries.

## Null-state note

The 16 package null states are classified separately from the RxRx3 biological sample. They correspond to absent candidate outputs in the micro sandbox trace, while the micro sample itself has one null field: Axis10.quarantine.

Null classification method: `JSON structure walk and filesystem existence checks only; no regex classification`

Counts by kind:
- `loaded_output_status_null`: `15`
- `raw_jsonl_status_null`: `1`
- `trace_status_null`: `16`
- `micro_sample_value_null`: `1`

## Sefer voice anchor

The system lands the finding as a carried-residual discovery record across all available depth levels.

## Source seals

- `micro_sample_sha256`: `03c16a22614d1e89d42150be8b56900e14bee4040e7f0117bbfdc32b7ac90685`
- `voice_card_sha256`: `ecda4ebfda285364b12abf648ea15daa5cf415f16ac90caa0b923bafe07745a5`
- `voice_card_seal`: `fa3a9208d7c64bcb2727354c79acee98196a91be9ef8fb2a7d778b12afade422`
