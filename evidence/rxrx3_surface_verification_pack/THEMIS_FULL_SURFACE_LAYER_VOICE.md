# Themis Full Surface Layer Voice

Mode: field canvas only, no interpretation.

This document does not say what the residual means. It voices the full surface layer as source paths, raw values, and emitted/absent pointer status.

## Closure object

- `theta_axis10_residual_star = (a9, a5, a7, a8, delta_hidden)`

## Residual atom surface map

### a9

- Label: `a9_unresolved_or_void_residual`
- Raw value: `1.5282207919307684`
- Surface pointer status: `ABSTRACT_LAYER_ONLY`
- Surface pointer path: `None`

Source hits:

- `rxrx3_core_result_discovery_micro.json` -> `Axis10.residual_budget.a9` = `1.5282207919307684`
- `rxrx3_core_result_discovery_micro.json` -> `Axis10.theta_axis10_residual_star.tuple.a9` = `1.5282207919307684`

### a5

- Label: `a5_gap_surface`
- Raw value: `0.7638888888888888`
- Surface pointer status: `ABSTRACT_LAYER_ONLY`
- Surface pointer path: `None`

Source hits:

- `rxrx3_core_result_discovery_micro.json` -> `Axis10.residual_budget.a5` = `0.7638888888888888`
- `rxrx3_core_result_discovery_micro.json` -> `Axis10.theta_axis10_residual_star.tuple.a5` = `0.7638888888888888`

### a7

- Label: `a7_raw_or_phase_residual`
- Raw value: `0.00022150707649535271`
- Surface pointer status: `ABSTRACT_LAYER_ONLY`
- Surface pointer path: `None`

Source hits:

- `rxrx3_core_result_discovery_micro.json` -> `Axis10.residual_budget.a7_8K` = `0.00022150707649535271`
- `rxrx3_core_result_discovery_micro.json` -> `Axis10.theta_axis10_residual_star.tuple.a7_8K` = `0.00022150707649535271`

### a8

- Label: `a8_boundary_or_closure_residual`
- Raw value: `0.7641103959653842`
- Surface pointer status: `ABSTRACT_LAYER_ONLY`
- Surface pointer path: `None`

Source hits:

- `rxrx3_core_result_discovery_micro.json` -> `Axis10.residual_budget.a8_8K` = `0.7641103959653842`
- `rxrx3_core_result_discovery_micro.json` -> `Axis10.theta_axis10_residual_star.tuple.a8_8K` = `0.7641103959653842`

### delta_hidden

- Label: `delta_hidden`
- Raw value: `0.0`
- Surface pointer status: `ABSTRACT_LAYER_ONLY`
- Surface pointer path: `None`

Source hits:

- `rxrx3_core_result_discovery_micro.json` -> `Axis10.residual_budget.delta_hidden_8K` = `0.0`
- `rxrx3_core_result_discovery_micro.json` -> `Axis10.theta_axis10_residual_star.tuple.delta_hidden_8K` = `0.0`

## Visible surface fields

### observed_collision

- Status: `SURFACE_PRESENT_NO_ATOM_LINK`

```json
{
  "digest": "923e8f259a606dd40355f0fe0b2cecc473dd3755cf7b3ed9c2403c34e2423d60",
  "identity_a": "PLK1 / PLK1_guide_1 / CRISPR Gene Positive Controls",
  "identity_b": "AKR1C3 / AKR1C3_guide_5 / Query guides",
  "meaning": "same 384-feature embedding digest across distinct metadata identities"
}
```

### relation_mix_summary

- Status: `SURFACE_PRESENT_NO_ATOM_LINK`

```json
{
  "sample_count": 222601,
  "time_count": 222601,
  "identity_preserved": true
}
```

### witness

- Status: `SURFACE_PRESENT_NO_ATOM_LINK`

```json
{
  "operator": "witness_passive_observation",
  "observed_digest": "c61162d1487164c6a29ed5268218a66b44bb0f486e71f571c995ffba6c2b0bd7",
  "observation": {
    "source_ids": [
      "0",
      "1"
    ],
    "time_count": 222601,
    "sample_count": 222601,
    "mix_energy_proxy": 5769642.419650231
  },
  "delta_event_under_witness": 0,
  "backaction": 0,
  "source_unchanged": true
}
```

### Axis10.s_pi

- Status: `SURFACE_PRESENT_NO_ATOM_LINK`

```json
[
  2.42130914723405e-05,
  0.99999999289192,
  0.00011643850587615089,
  3.438999589113451e-07,
  3.4316661431226663e-06,
  1.060696807874279e-06,
  9.950901838313688e-10,
  3.4326612333064977e-06,
  6.865322466612995e-06,
  1.5749422905978407e-07
]
```

### Axis10.residual_budget

- Status: `SURFACE_PRESENT_NO_ATOM_LINK`

```json
{
  "a9": 1.5282207919307684,
  "a5": 0.7638888888888888,
  "a7_8K": 0.00022150707649535271,
  "a8_8K": 0.7641103959653842,
  "visible_sum": 1.5282207919307684,
  "delta_hidden_8K": 0.0
}
```

### Axis10.theta_axis10_residual_star

- Status: `SURFACE_PRESENT_NO_ATOM_LINK`

```json
{
  "name": "theta_axis10_residual_star",
  "status": "RESIDUAL_CARRIED",
  "tuple": {
    "a9": 1.5282207919307684,
    "a5": 0.7638888888888888,
    "a7_8K": 0.00022150707649535271,
    "a8_8K": 0.7641103959653842,
    "delta_hidden_8K": 0.0
  }
}
```

### closure

- Status: `SURFACE_PRESENT_NO_ATOM_LINK`

```json
{
  "verdict": "CLOSED_WITH_RESIDUAL_CARRIED",
  "closure_signal_score": 9,
  "closure_signal_possible": 9,
  "remaining_object": "theta_axis10_residual_star"
}
```

### Sefer

- Status: `SURFACE_PRESENT_NO_ATOM_LINK`

```json
{
  "landed": 1,
  "source": "axis10_estuary_no_narrow_orchestration",
  "seal": "270968ffcd29de57b4a7fcb054d8e518fec610d7842b118f5645d8438b2c447b",
  "db_path": "<private-sefer-db>"
}
```

### outcome_counts

- Status: `SURFACE_PRESENT_NO_ATOM_LINK`

```json
{
  "success": 9,
  "null": 0,
  "unknown": 0,
  "nonmatch": 0,
  "error": 0,
  "timeout": 0,
  "break": 0
}
```

## Null surfaces

Count: `15`

- `<private-themis-root>\runs\rxrx3_core_discovery_micro_sandbox\runs\axis10_estuary_no_narrow\full_rich_result.json` -> `NULL_SURFACE`
- `<private-themis-root>\runs\rxrx3_core_discovery_micro_sandbox\runs\axis10_estuary_no_narrow\orchestration_result.json` -> `NULL_SURFACE`
- `<private-themis-root>\runs\rxrx3_core_discovery_micro_sandbox\runs\axis10_estuary_ibm_qshot\ibm_qshot_result.json` -> `NULL_SURFACE`
- `<private-themis-root>\runs\rxrx3_core_discovery_micro_sandbox\runs\axis10_estuary_ibm_qshot\axis10_from_full_rich.json` -> `NULL_SURFACE`
- `<private-themis-root>\runs\rxrx3_core_discovery_micro_sandbox\runs\axis10_estuary_ibm_qshot\axis10_orchestration_result.json` -> `NULL_SURFACE`
- `<private-themis-root>\runs\rxrx3_core_discovery_micro_sandbox\runs\axis10_final_research_architecture\themis_axis10_final_research_architecture_closure_package.json` -> `NULL_SURFACE`
- `<private-themis-root>\runs\rxrx3_core_discovery_micro_sandbox\runs\axis10_all_direction_system_voice\axis10_closure_signal_discovery.json` -> `NULL_SURFACE`
- `<private-themis-root>\runs\rxrx3_core_discovery_micro_sandbox\runs\axis10_all_direction_system_voice\axis10_closure_signal_truth_guidance.json` -> `NULL_SURFACE`
- `<private-themis-root>\runs\rxrx3_core_discovery_micro_sandbox\runs\axis10_natural_law_residual_discovery\natural_law_residual_discovery.json` -> `NULL_SURFACE`
- `<private-themis-root>\runs\rxrx3_core_discovery_micro_sandbox\runs\themis_no_narrow_L1_L52_full_audit\summary.json` -> `NULL_SURFACE`
- `<private-themis-root>\runs\rxrx3_core_discovery_micro_sandbox\runs\themis_no_narrow_L1_L52_full_audit\counts.json` -> `NULL_SURFACE`
- `<private-themis-root>\runs\rxrx3_core_discovery_micro_sandbox\runs\themis_no_narrow_L1_L52_full_audit\failures.json` -> `NULL_SURFACE`
- `<private-themis-root>\runs\rxrx3_core_discovery_micro_sandbox\runs\themis_no_narrow_L1_L52_full_audit\module_inventory.json` -> `NULL_SURFACE`
- `<private-themis-root>\runs\rxrx3_core_discovery_micro_sandbox\runs\themis_no_narrow_L1_L52_full_audit\callable_inventory.json` -> `NULL_SURFACE`
- `<private-themis-root>\runs\rxrx3_core_discovery_micro_sandbox\runs\themis_no_narrow_L1_L52_full_audit\raw_records.jsonl` -> `NULL_SURFACE`

## Canvas statement

- The atom tuple is emitted.
- The visible surface fields are emitted.
- The direct atom-to-observed-collision relation is not emitted in the source fields.
- No biological meaning is inferred.
