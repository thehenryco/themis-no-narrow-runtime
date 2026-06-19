# Themis Residual Translation Surface Index

Mode: surface index only, no interpretation.

This file does not say what the residual means. It shows where each residual atom points before translation.

## Formula registry

- `truth_identity`: `T(Psi_J) == T(lambda * Psi_J)`
- `relation`: `Lambda_3(t) = R(lambda_1(t), lambda_2(t), lambda_3(t))`
- `witness`: `O_Lambda = W(Lambda_3), Delta Lambda_3|W = 0`
- `boundary`: `s_pi = Psi / ||Psi||, ||s_pi|| = 1, s_pi^T dot{s_pi} = 0`
- `qpe_8k`: `Q_8K(E) -> phi_hat_8K(t)`
- `mirror_record`: `L_{t+1} = L_t union M_ring(E), Delta E = 0`
- `residual_budget`: `a9 = |a5| + |a7| + |a8| + delta_hidden`
- `equilibrium`: `a10 = 1 / (1 + |a3| + a4 + a9)`
- `closure_object`: `theta_axis10_residual_star = (a9, a5, a7, a8, delta_hidden)`
- `no_narrow`: `O_NN(E) = {success,null,unknown,nonmatch,error,timeout,break} -> preserve all`

## Core metrics

- `a5_gap_surface`: `0.7638888888888888`
- `a7_raw_or_phase_residual`: `0.00022150707649535271`
- `a8_boundary_or_closure_residual`: `0.7641103959653842`
- `a9_unresolved_or_void_residual`: `1.5282207919307684`
- `a10_equilibrium_or_rest`: `0.6328875746760656`
- `visible_sum`: `1.5282207919307684`
- `delta_hidden`: `0.0`
- `theta_object`: `theta_axis10_residual_star`
- `residual_formula`: `a9 = |a5| + |a7| + |a8| + delta_hidden`
- `equilibrium_formula`: `a10 = 1 / (1 + |a3| + a4 + a9)`

## RxRx3 surface fields

### observed_collision

```json
{
  "digest": "923e8f259a606dd40355f0fe0b2cecc473dd3755cf7b3ed9c2403c34e2423d60",
  "identity_a": "PLK1 / PLK1_guide_1 / CRISPR Gene Positive Controls",
  "identity_b": "AKR1C3 / AKR1C3_guide_5 / Query guides",
  "meaning": "same 384-feature embedding digest across distinct metadata identities"
}
```

### relation_mix_summary

```json
{
  "sample_count": 222601,
  "time_count": 222601,
  "identity_preserved": true
}
```

### witness

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

### Axis10_residual_budget

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

### theta_axis10_residual_star

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

```json
{
  "verdict": "CLOSED_WITH_RESIDUAL_CARRIED",
  "closure_signal_score": 9,
  "closure_signal_possible": 9,
  "remaining_object": "theta_axis10_residual_star"
}
```

## Candidate translation buckets

### residual_fields

Count: `28`

#### residual_fields item 1

```json
{
  "path": "known_closed_state.residual_closed_as",
  "key": "residual_closed_as",
  "value": "CLOSED_WITH_RESIDUAL_CARRIED",
  "source": "themis_residual_identity_question_card.json"
}
```

#### residual_fields item 2

```json
{
  "path": "Axis10.residual_budget",
  "key": "residual_budget",
  "value": {
    "a9": 1.5282207919307684,
    "a5": 0.7638888888888888,
    "a7_8K": 0.00022150707649535271,
    "a8_8K": 0.7641103959653842,
    "visible_sum": 1.5282207919307684,
    "delta_hidden_8K": 0.0
  },
  "source": "rxrx3_core_result_discovery_micro.json"
}
```

#### residual_fields item 3

```json
{
  "path": "Axis10.residual_budget.a9",
  "key": "a9",
  "value": 1.5282207919307684,
  "source": "rxrx3_core_result_discovery_micro.json"
}
```

#### residual_fields item 4

```json
{
  "path": "Axis10.residual_budget.a5",
  "key": "a5",
  "value": 0.7638888888888888,
  "source": "rxrx3_core_result_discovery_micro.json"
}
```

#### residual_fields item 5

```json
{
  "path": "Axis10.residual_budget.a7_8K",
  "key": "a7_8K",
  "value": 0.00022150707649535271,
  "source": "rxrx3_core_result_discovery_micro.json"
}
```

#### residual_fields item 6

```json
{
  "path": "Axis10.residual_budget.a8_8K",
  "key": "a8_8K",
  "value": 0.7641103959653842,
  "source": "rxrx3_core_result_discovery_micro.json"
}
```

#### residual_fields item 7

```json
{
  "path": "Axis10.residual_budget.visible_sum",
  "key": "visible_sum",
  "value": 1.5282207919307684,
  "source": "rxrx3_core_result_discovery_micro.json"
}
```

#### residual_fields item 8

```json
{
  "path": "Axis10.residual_budget.delta_hidden_8K",
  "key": "delta_hidden_8K",
  "value": 0.0,
  "source": "rxrx3_core_result_discovery_micro.json"
}
```

#### residual_fields item 9

```json
{
  "path": "Axis10.theta_axis10_residual_star",
  "key": "theta_axis10_residual_star",
  "value": {
    "name": "theta_axis10_residual_star",
    "status": "RESIDUAL_CARRIED",
    "tuple": {
      "a9": 1.5282207919307684,
      "a5": 0.7638888888888888,
      "a7_8K": 0.00022150707649535271,
      "a8_8K": 0.7641103959653842,
      "delta_hidden_8K": 0.0
    }
  },
  "source": "rxrx3_core_result_discovery_micro.json"
}
```

#### residual_fields item 10

```json
{
  "path": "Axis10.theta_axis10_residual_star.name",
  "key": "name",
  "value": "theta_axis10_residual_star",
  "source": "rxrx3_core_result_discovery_micro.json"
}
```

#### residual_fields item 11

```json
{
  "path": "Axis10.theta_axis10_residual_star.status",
  "key": "status",
  "value": "RESIDUAL_CARRIED",
  "source": "rxrx3_core_result_discovery_micro.json"
}
```

#### residual_fields item 12

```json
{
  "path": "Axis10.theta_axis10_residual_star.tuple",
  "key": "tuple",
  "value": {
    "a9": 1.5282207919307684,
    "a5": 0.7638888888888888,
    "a7_8K": 0.00022150707649535271,
    "a8_8K": 0.7641103959653842,
    "delta_hidden_8K": 0.0
  },
  "source": "rxrx3_core_result_discovery_micro.json"
}
```

#### residual_fields item 13

```json
{
  "path": "Axis10.theta_axis10_residual_star.tuple.a9",
  "key": "a9",
  "value": 1.5282207919307684,
  "source": "rxrx3_core_result_discovery_micro.json"
}
```

#### residual_fields item 14

```json
{
  "path": "Axis10.theta_axis10_residual_star.tuple.a5",
  "key": "a5",
  "value": 0.7638888888888888,
  "source": "rxrx3_core_result_discovery_micro.json"
}
```

#### residual_fields item 15

```json
{
  "path": "Axis10.theta_axis10_residual_star.tuple.a7_8K",
  "key": "a7_8K",
  "value": 0.00022150707649535271,
  "source": "rxrx3_core_result_discovery_micro.json"
}
```

#### residual_fields item 16

```json
{
  "path": "Axis10.theta_axis10_residual_star.tuple.a8_8K",
  "key": "a8_8K",
  "value": 0.7641103959653842,
  "source": "rxrx3_core_result_discovery_micro.json"
}
```

#### residual_fields item 17

```json
{
  "path": "Axis10.theta_axis10_residual_star.tuple.delta_hidden_8K",
  "key": "delta_hidden_8K",
  "value": 0.0,
  "source": "rxrx3_core_result_discovery_micro.json"
}
```

#### residual_fields item 18

```json
{
  "path": "records[0].card.residual_components",
  "key": "residual_components",
  "value": {
    "total": 0.013349279708594872,
    "parts": {
      "C_a8_closure_residual": 0.011,
      "gap_a5_surface_gap": 0.001723084288078749,
      "R_a7_raw_residual": 0.0006261954205161247
    },
    "percentages": {
      "C_a8_closure_residual": 82.4014496671135,
      "gap_a5_surface_gap": 12.907694839665012,
      "R_a7_raw_residual": 4.690855493221493
    },
    "dominant": "C_a8_closure_residual"
  },
  "source": "themis_universal_depth_speech_extract_deduped.json"
}
```

#### residual_fields item 19

```json
{
  "path": "records[0].card.residual_components.total",
  "key": "total",
  "value": 0.013349279708594872,
  "source": "themis_universal_depth_speech_extract_deduped.json"
}
```

#### residual_fields item 20

```json
{
  "path": "records[0].card.residual_components.parts",
  "key": "parts",
  "value": {
    "C_a8_closure_residual": 0.011,
    "gap_a5_surface_gap": 0.001723084288078749,
    "R_a7_raw_residual": 0.0006261954205161247
  },
  "source": "themis_universal_depth_speech_extract_deduped.json"
}
```

#### residual_fields item 21

```json
{
  "path": "records[0].card.residual_components.parts.C_a8_closure_residual",
  "key": "C_a8_closure_residual",
  "value": 0.011,
  "source": "themis_universal_depth_speech_extract_deduped.json"
}
```

#### residual_fields item 22

```json
{
  "path": "records[0].card.residual_components.parts.gap_a5_surface_gap",
  "key": "gap_a5_surface_gap",
  "value": 0.001723084288078749,
  "source": "themis_universal_depth_speech_extract_deduped.json"
}
```

#### residual_fields item 23

```json
{
  "path": "records[0].card.residual_components.parts.R_a7_raw_residual",
  "key": "R_a7_raw_residual",
  "value": 0.0006261954205161247,
  "source": "themis_universal_depth_speech_extract_deduped.json"
}
```

#### residual_fields item 24

```json
{
  "path": "records[0].card.residual_components.percentages",
  "key": "percentages",
  "value": {
    "C_a8_closure_residual": 82.4014496671135,
    "gap_a5_surface_gap": 12.907694839665012,
    "R_a7_raw_residual": 4.690855493221493
  },
  "source": "themis_universal_depth_speech_extract_deduped.json"
}
```

#### residual_fields item 25

```json
{
  "path": "records[0].card.residual_components.percentages.C_a8_closure_residual",
  "key": "C_a8_closure_residual",
  "value": 82.4014496671135,
  "source": "themis_universal_depth_speech_extract_deduped.json"
}
```

#### residual_fields item 26

```json
{
  "path": "records[0].card.residual_components.percentages.gap_a5_surface_gap",
  "key": "gap_a5_surface_gap",
  "value": 12.907694839665012,
  "source": "themis_universal_depth_speech_extract_deduped.json"
}
```

#### residual_fields item 27

```json
{
  "path": "records[0].card.residual_components.percentages.R_a7_raw_residual",
  "key": "R_a7_raw_residual",
  "value": 4.690855493221493,
  "source": "themis_universal_depth_speech_extract_deduped.json"
}
```

#### residual_fields item 28

```json
{
  "path": "records[0].card.residual_components.dominant",
  "key": "dominant",
  "value": "C_a8_closure_residual",
  "source": "themis_universal_depth_speech_extract_deduped.json"
}
```

### axis10_fields

Count: `29`

#### axis10_fields item 1

```json
{
  "path": "Axis10",
  "key": "Axis10",
  "value": {
    "carrier": "Axis10",
    "s_pi": [
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
    ],
    "norm_sq": 0.9999999999999997,
    "unit_boundary_held": true,
    "tangent_condition": 0.0,
    "no_radial_drift": true,
    "quarantine": null,
    "residual_budget": {
      "a9": 1.5282207919307684,
      "a5": 0.7638888888888888,
      "a7_8K": 0.00022150707649535271,
      "a8_8K": 0.7641103959653842,
      "visible_sum": 1.5282207919307684,
      "delta_hidden_8K": 0.0
    },
    "theta_axis10_residual_star": {
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
  },
  "source": "rxrx3_core_result_discovery_micro.json"
}
```

#### axis10_fields item 2

```json
{
  "path": "Axis10.unit_boundary_held",
  "key": "unit_boundary_held",
  "value": true,
  "source": "rxrx3_core_result_discovery_micro.json"
}
```

#### axis10_fields item 3

```json
{
  "path": "Axis10.residual_budget",
  "key": "residual_budget",
  "value": {
    "a9": 1.5282207919307684,
    "a5": 0.7638888888888888,
    "a7_8K": 0.00022150707649535271,
    "a8_8K": 0.7641103959653842,
    "visible_sum": 1.5282207919307684,
    "delta_hidden_8K": 0.0
  },
  "source": "rxrx3_core_result_discovery_micro.json"
}
```

#### axis10_fields item 4

```json
{
  "path": "Axis10.residual_budget.a9",
  "key": "a9",
  "value": 1.5282207919307684,
  "source": "rxrx3_core_result_discovery_micro.json"
}
```

#### axis10_fields item 5

```json
{
  "path": "Axis10.residual_budget.a5",
  "key": "a5",
  "value": 0.7638888888888888,
  "source": "rxrx3_core_result_discovery_micro.json"
}
```

#### axis10_fields item 6

```json
{
  "path": "Axis10.residual_budget.a7_8K",
  "key": "a7_8K",
  "value": 0.00022150707649535271,
  "source": "rxrx3_core_result_discovery_micro.json"
}
```

#### axis10_fields item 7

```json
{
  "path": "Axis10.residual_budget.a8_8K",
  "key": "a8_8K",
  "value": 0.7641103959653842,
  "source": "rxrx3_core_result_discovery_micro.json"
}
```

#### axis10_fields item 8

```json
{
  "path": "Axis10.residual_budget.visible_sum",
  "key": "visible_sum",
  "value": 1.5282207919307684,
  "source": "rxrx3_core_result_discovery_micro.json"
}
```

#### axis10_fields item 9

```json
{
  "path": "Axis10.residual_budget.delta_hidden_8K",
  "key": "delta_hidden_8K",
  "value": 0.0,
  "source": "rxrx3_core_result_discovery_micro.json"
}
```

#### axis10_fields item 10

```json
{
  "path": "Axis10.theta_axis10_residual_star",
  "key": "theta_axis10_residual_star",
  "value": {
    "name": "theta_axis10_residual_star",
    "status": "RESIDUAL_CARRIED",
    "tuple": {
      "a9": 1.5282207919307684,
      "a5": 0.7638888888888888,
      "a7_8K": 0.00022150707649535271,
      "a8_8K": 0.7641103959653842,
      "delta_hidden_8K": 0.0
    }
  },
  "source": "rxrx3_core_result_discovery_micro.json"
}
```

#### axis10_fields item 11

```json
{
  "path": "Axis10.theta_axis10_residual_star.name",
  "key": "name",
  "value": "theta_axis10_residual_star",
  "source": "rxrx3_core_result_discovery_micro.json"
}
```

#### axis10_fields item 12

```json
{
  "path": "Axis10.theta_axis10_residual_star.status",
  "key": "status",
  "value": "RESIDUAL_CARRIED",
  "source": "rxrx3_core_result_discovery_micro.json"
}
```

#### axis10_fields item 13

```json
{
  "path": "Axis10.theta_axis10_residual_star.tuple",
  "key": "tuple",
  "value": {
    "a9": 1.5282207919307684,
    "a5": 0.7638888888888888,
    "a7_8K": 0.00022150707649535271,
    "a8_8K": 0.7641103959653842,
    "delta_hidden_8K": 0.0
  },
  "source": "rxrx3_core_result_discovery_micro.json"
}
```

#### axis10_fields item 14

```json
{
  "path": "Axis10.theta_axis10_residual_star.tuple.a9",
  "key": "a9",
  "value": 1.5282207919307684,
  "source": "rxrx3_core_result_discovery_micro.json"
}
```

#### axis10_fields item 15

```json
{
  "path": "Axis10.theta_axis10_residual_star.tuple.a5",
  "key": "a5",
  "value": 0.7638888888888888,
  "source": "rxrx3_core_result_discovery_micro.json"
}
```

#### axis10_fields item 16

```json
{
  "path": "Axis10.theta_axis10_residual_star.tuple.a7_8K",
  "key": "a7_8K",
  "value": 0.00022150707649535271,
  "source": "rxrx3_core_result_discovery_micro.json"
}
```

#### axis10_fields item 17

```json
{
  "path": "Axis10.theta_axis10_residual_star.tuple.a8_8K",
  "key": "a8_8K",
  "value": 0.7641103959653842,
  "source": "rxrx3_core_result_discovery_micro.json"
}
```

#### axis10_fields item 18

```json
{
  "path": "Axis10.theta_axis10_residual_star.tuple.delta_hidden_8K",
  "key": "delta_hidden_8K",
  "value": 0.0,
  "source": "rxrx3_core_result_discovery_micro.json"
}
```

#### axis10_fields item 19

```json
{
  "path": "records[0].card.latest.C_a8",
  "key": "C_a8",
  "value": 0.011,
  "source": "themis_universal_depth_speech_extract_deduped.json"
}
```

#### axis10_fields item 20

```json
{
  "path": "records[0].card.latest.R_a7",
  "key": "R_a7",
  "value": 0.0006261954205161247,
  "source": "themis_universal_depth_speech_extract_deduped.json"
}
```

#### axis10_fields item 21

```json
{
  "path": "records[0].card.latest.gap_a5",
  "key": "gap_a5",
  "value": 0.001723084288078749,
  "source": "themis_universal_depth_speech_extract_deduped.json"
}
```

#### axis10_fields item 22

```json
{
  "path": "records[0].card.latest.unresolved_a9",
  "key": "unresolved_a9",
  "value": 0.013529356415102065,
  "source": "themis_universal_depth_speech_extract_deduped.json"
}
```

#### axis10_fields item 23

```json
{
  "path": "records[0].card.residual_components.parts.C_a8_closure_residual",
  "key": "C_a8_closure_residual",
  "value": 0.011,
  "source": "themis_universal_depth_speech_extract_deduped.json"
}
```

#### axis10_fields item 24

```json
{
  "path": "records[0].card.residual_components.parts.gap_a5_surface_gap",
  "key": "gap_a5_surface_gap",
  "value": 0.001723084288078749,
  "source": "themis_universal_depth_speech_extract_deduped.json"
}
```

#### axis10_fields item 25

```json
{
  "path": "records[0].card.residual_components.parts.R_a7_raw_residual",
  "key": "R_a7_raw_residual",
  "value": 0.0006261954205161247,
  "source": "themis_universal_depth_speech_extract_deduped.json"
}
```

#### axis10_fields item 26

```json
{
  "path": "records[0].card.residual_components.percentages.C_a8_closure_residual",
  "key": "C_a8_closure_residual",
  "value": 82.4014496671135,
  "source": "themis_universal_depth_speech_extract_deduped.json"
}
```

#### axis10_fields item 27

```json
{
  "path": "records[0].card.residual_components.percentages.gap_a5_surface_gap",
  "key": "gap_a5_surface_gap",
  "value": 12.907694839665012,
  "source": "themis_universal_depth_speech_extract_deduped.json"
}
```

#### axis10_fields item 28

```json
{
  "path": "records[0].card.residual_components.percentages.R_a7_raw_residual",
  "key": "R_a7_raw_residual",
  "value": 4.690855493221493,
  "source": "themis_universal_depth_speech_extract_deduped.json"
}
```

#### axis10_fields item 29

```json
{
  "path": "records[0].card.C_a8_definition",
  "key": "C_a8_definition",
  "value": "closure-residual holder remaining after gap and raw residual are small",
  "source": "themis_universal_depth_speech_extract_deduped.json"
}
```

### shape_vector_wave_fields

Count: `0`

### frequency_fields

Count: `0`

### closure_fields

Count: `10`

#### closure_fields item 1

```json
{
  "path": "known_closed_state",
  "key": "known_closed_state",
  "value": {
    "residual_closed_as": "CLOSED_WITH_RESIDUAL_CARRIED",
    "remaining_object": "theta_axis10_residual_star"
  },
  "source": "themis_residual_identity_question_card.json"
}
```

#### closure_fields item 2

```json
{
  "path": "known_closed_state.residual_closed_as",
  "key": "residual_closed_as",
  "value": "CLOSED_WITH_RESIDUAL_CARRIED",
  "source": "themis_residual_identity_question_card.json"
}
```

#### closure_fields item 3

```json
{
  "path": "known_closed_state.remaining_object",
  "key": "remaining_object",
  "value": "theta_axis10_residual_star",
  "source": "themis_residual_identity_question_card.json"
}
```

#### closure_fields item 4

```json
{
  "path": "closure",
  "key": "closure",
  "value": {
    "verdict": "CLOSED_WITH_RESIDUAL_CARRIED",
    "closure_signal_score": 9,
    "closure_signal_possible": 9,
    "remaining_object": "theta_axis10_residual_star"
  },
  "source": "rxrx3_core_result_discovery_micro.json"
}
```

#### closure_fields item 5

```json
{
  "path": "closure.verdict",
  "key": "verdict",
  "value": "CLOSED_WITH_RESIDUAL_CARRIED",
  "source": "rxrx3_core_result_discovery_micro.json"
}
```

#### closure_fields item 6

```json
{
  "path": "closure.closure_signal_score",
  "key": "closure_signal_score",
  "value": 9,
  "source": "rxrx3_core_result_discovery_micro.json"
}
```

#### closure_fields item 7

```json
{
  "path": "closure.closure_signal_possible",
  "key": "closure_signal_possible",
  "value": 9,
  "source": "rxrx3_core_result_discovery_micro.json"
}
```

#### closure_fields item 8

```json
{
  "path": "closure.remaining_object",
  "key": "remaining_object",
  "value": "theta_axis10_residual_star",
  "source": "rxrx3_core_result_discovery_micro.json"
}
```

#### closure_fields item 9

```json
{
  "path": "records[0].card.residual_components.parts.C_a8_closure_residual",
  "key": "C_a8_closure_residual",
  "value": 0.011,
  "source": "themis_universal_depth_speech_extract_deduped.json"
}
```

#### closure_fields item 10

```json
{
  "path": "records[0].card.residual_components.percentages.C_a8_closure_residual",
  "key": "C_a8_closure_residual",
  "value": 82.4014496671135,
  "source": "themis_universal_depth_speech_extract_deduped.json"
}
```

### outcome_fields

Count: `1`

#### outcome_fields item 1

```json
{
  "path": "Axis10.theta_axis10_residual_star.status",
  "key": "status",
  "value": "RESIDUAL_CARRIED",
  "source": "rxrx3_core_result_discovery_micro.json"
}
```

## Blank or null surfaces

Count: `15`

- `<private-themis-root>\runs\rxrx3_core_discovery_micro_sandbox\runs\axis10_estuary_no_narrow\full_rich_result.json` -> `null`
- `<private-themis-root>\runs\rxrx3_core_discovery_micro_sandbox\runs\axis10_estuary_no_narrow\orchestration_result.json` -> `null`
- `<private-themis-root>\runs\rxrx3_core_discovery_micro_sandbox\runs\axis10_estuary_ibm_qshot\ibm_qshot_result.json` -> `null`
- `<private-themis-root>\runs\rxrx3_core_discovery_micro_sandbox\runs\axis10_estuary_ibm_qshot\axis10_from_full_rich.json` -> `null`
- `<private-themis-root>\runs\rxrx3_core_discovery_micro_sandbox\runs\axis10_estuary_ibm_qshot\axis10_orchestration_result.json` -> `null`
- `<private-themis-root>\runs\rxrx3_core_discovery_micro_sandbox\runs\axis10_final_research_architecture\themis_axis10_final_research_architecture_closure_package.json` -> `null`
- `<private-themis-root>\runs\rxrx3_core_discovery_micro_sandbox\runs\axis10_all_direction_system_voice\axis10_closure_signal_discovery.json` -> `null`
- `<private-themis-root>\runs\rxrx3_core_discovery_micro_sandbox\runs\axis10_all_direction_system_voice\axis10_closure_signal_truth_guidance.json` -> `null`
- `<private-themis-root>\runs\rxrx3_core_discovery_micro_sandbox\runs\axis10_natural_law_residual_discovery\natural_law_residual_discovery.json` -> `null`
- `<private-themis-root>\runs\rxrx3_core_discovery_micro_sandbox\runs\themis_no_narrow_L1_L52_full_audit\summary.json` -> `null`
- `<private-themis-root>\runs\rxrx3_core_discovery_micro_sandbox\runs\themis_no_narrow_L1_L52_full_audit\counts.json` -> `null`
- `<private-themis-root>\runs\rxrx3_core_discovery_micro_sandbox\runs\themis_no_narrow_L1_L52_full_audit\failures.json` -> `null`
- `<private-themis-root>\runs\rxrx3_core_discovery_micro_sandbox\runs\themis_no_narrow_L1_L52_full_audit\module_inventory.json` -> `null`
- `<private-themis-root>\runs\rxrx3_core_discovery_micro_sandbox\runs\themis_no_narrow_L1_L52_full_audit\callable_inventory.json` -> `null`
- `<private-themis-root>\runs\rxrx3_core_discovery_micro_sandbox\runs\themis_no_narrow_L1_L52_full_audit\raw_records.jsonl` -> `null`
