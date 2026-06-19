# Themis Final Full Current Surface Verification Voice

Mode: source-locked Themis surface voice, no Chat hidden biology.

This is the full current surface voice for human verification. It is not a final biological proof.

## Authorship boundary

- `chat_role`: `source_locked_file_assembler_only`
- `chat_adds_hidden_biology`: `False`
- `chat_adds_final_scientific_conclusion`: `False`
- `themis_surface_voice_emitted`: `True`
- `themis_final_biological_conclusion_emitted`: `False`
- `human_verification_required`: `True`

## Current surface conclusion

- Status: `THEMIS_SURFACE_CONCLUSION_FOR_HUMAN_VERIFICATION`
- Voice: Themis reports an exact representation duplicate across distinct metadata identities, preserves the identity gap, carries theta_axis10_residual_star, and routes the event into a verification frontier rather than a final biological mechanism.

## Themis voice rows

### T1 - THEMIS_SURFACE_EMITTED

The observed surface event is an exact shared 384-feature embedding digest across two distinct metadata identities.

Source paths:
- `rxrx3_biological_frontier_sefer_english.json.observed_event`
- `rxrx3_core_result_discovery_micro.json.observed_collision`

Source values:

```json
{
  "digest": "923e8f259a606dd40355f0fe0b2cecc473dd3755cf7b3ed9c2403c34e2423d60",
  "identity_a": "PLK1 / PLK1_guide_1 / CRISPR Gene Positive Controls",
  "identity_b": "AKR1C3 / AKR1C3_guide_5 / Query guides",
  "meaning": "same 384-feature embedding digest across distinct metadata identities"
}
```

### T2 - THEMIS_SURFACE_EMITTED

The shared digest does not erase metadata distinction: the rows share cell type, experiment, perturbation type, and plate, while gene, treatment, address, well_id, and well_type_label differ.

Source paths:
- `rxrx3_biological_frontier_sefer_english.json.common_fields_between_target_rows`
- `rxrx3_biological_frontier_sefer_english.json.different_fields_between_target_rows`
- `rxrx3_biological_frontier_sefer_english.json.target_rows`

Source values:

```json
{
  "common_fields": {
    "SMILES": "",
    "cell_type": "HUVEC",
    "concentration": "",
    "experiment_name": "gene-134",
    "perturbation_type": "CRISPR",
    "plate": "2"
  },
  "different_fields": {
    "address": [
      "L39",
      "N26"
    ],
    "gene": [
      "PLK1",
      "AKR1C3"
    ],
    "treatment": [
      "PLK1_guide_1",
      "AKR1C3_guide_5"
    ],
    "well_id": [
      "gene-134_2_L39",
      "gene-134_2_N26"
    ],
    "well_type_label": [
      "CRISPR Gene Positive Controls",
      "Query guides"
    ]
  },
  "target_rows": [
    {
      "well_id": "gene-134_2_L39",
      "experiment_name": "gene-134",
      "plate": "2",
      "address": "L39",
      "gene": "PLK1",
      "treatment": "PLK1_guide_1",
      "SMILES": "",
      "concentration": "",
      "perturbation_type": "CRISPR",
      "cell_type": "HUVEC",
      "well_type_label": "CRISPR Gene Positive Controls"
    },
    {
      "well_id": "gene-134_2_N26",
      "experiment_name": "gene-134",
      "plate": "2",
      "address": "N26",
      "gene": "AKR1C3",
      "treatment": "AKR1C3_guide_5",
      "SMILES": "",
      "concentration": "",
      "perturbation_type": "CRISPR",
      "cell_type": "HUVEC",
      "well_type_label": "Query guides"
    }
  ]
}
```

### T3 - THEMIS_KERNEL_EMITTED

The runtime preserves identity, carries theta_axis10_residual_star as RESIDUAL_CARRIED, and closes as CLOSED_WITH_RESIDUAL_CARRIED with score 9 / 9.

Source paths:
- `rxrx3_biological_frontier_sefer_english.json.runtime_state`
- `rxrx3_core_result_discovery_micro.json.Axis10.theta_axis10_residual_star`
- `rxrx3_core_result_discovery_micro.json.closure`

Source values:

```json
{
  "identity_preserved": true,
  "carried_object": "theta_axis10_residual_star",
  "carried_object_status": "RESIDUAL_CARRIED",
  "closure_verdict": "CLOSED_WITH_RESIDUAL_CARRIED",
  "closure_score": {
    "score": 9,
    "possible": 9
  },
  "residual_budget": {
    "a9": 1.5282207919307684,
    "a5": 0.7638888888888888,
    "a7_8K": 0.00022150707649535271,
    "a8_8K": 0.7641103959653842,
    "visible_sum": 1.5282207919307684,
    "delta_hidden_8K": 0.0
  }
}
```

### T4 - THEMIS_FIELD_BOUNDARY_EMITTED

The residual atoms are emitted as abstract-layer fields, while the visible surface fields are present without a direct emitted atom-to-observed-collision link.

Source paths:
- `themis_full_surface_layer_voice.json.residual_atom_surface_map`
- `themis_full_surface_layer_voice.json.visible_surface_fields`
- `themis_full_surface_layer_voice.json.canvas_statement`

Source values:

```json
{
  "residual_atom_surface_map": [
    {
      "atom": "a9",
      "label": "a9_unresolved_or_void_residual",
      "raw_value": 1.5282207919307684,
      "source_hits": [
        {
          "path": "Axis10.residual_budget.a9",
          "key": "a9",
          "value": 1.5282207919307684,
          "source": "rxrx3_core_result_discovery_micro.json"
        },
        {
          "path": "Axis10.theta_axis10_residual_star.tuple.a9",
          "key": "a9",
          "value": 1.5282207919307684,
          "source": "rxrx3_core_result_discovery_micro.json"
        }
      ],
      "surface_pointer_status": "ABSTRACT_LAYER_ONLY",
      "surface_pointer_path": null,
      "note": "Path-only report. No biological interpretation emitted."
    },
    {
      "atom": "a5",
      "label": "a5_gap_surface",
      "raw_value": 0.7638888888888888,
      "source_hits": [
        {
          "path": "Axis10.residual_budget.a5",
          "key": "a5",
          "value": 0.7638888888888888,
          "source": "rxrx3_core_result_discovery_micro.json"
        },
        {
          "path": "Axis10.theta_axis10_residual_star.tuple.a5",
          "key": "a5",
          "value": 0.7638888888888888,
          "source": "rxrx3_core_result_discovery_micro.json"
        }
      ],
      "surface_pointer_status": "ABSTRACT_LAYER_ONLY",
      "surface_pointer_path": null,
      "note": "Path-only report. No biological interpretation emitted."
    },
    {
      "atom": "a7",
      "label": "a7_raw_or_phase_residual",
      "raw_value": 0.00022150707649535271,
      "source_hits": [
        {
          "path": "Axis10.residual_budget.a7_8K",
          "key": "a7_8K",
          "value": 0.00022150707649535271,
          "source": "rxrx3_core_result_discovery_micro.json"
        },
        {
          "path": "Axis10.theta_axis10_residual_star.tuple.a7_8K",
          "key": "a7_8K",
          "value": 0.00022150707649535271,
          "source": "rxrx3_core_result_discovery_micro.json"
        }
      ],
      "surface_pointer_status": "ABSTRACT_LAYER_ONLY",
      "surface_pointer_path": null,
      "note": "Path-only report. No biological interpretation emitted."
    },
    {
      "atom": "a8",
      "label": "a8_boundary_or_closure_residual",
      "raw_value": 0.7641103959653842,
      "source_hits": [
        {
          "path": "Axis10.residual_budget.a8_8K",
          "key": "a8_8K",
          "value": 0.7641103959653842,
          "source": "rxrx3_core_result_discovery_micro.json"
        },
        {
          "path": "Axis10.theta_axis10_residual_star.tuple.a8_8K",
          "key": "a8_8K",
          "value": 0.7641103959653842,
          "source": "rxrx3_core_result_discovery_micro.json"
        }
      ],
      "surface_pointer_status": "ABSTRACT_LAYER_ONLY",
      "surface_pointer_path": null,
      "note": "Path-only report. No biological interpretation emitted."
    },
    {
      "atom": "delta_hidden",
      "label": "delta_hidden",
      "raw_value": 0.0,
      "source_hits": [
        {
          "path": "Axis10.residual_budget.delta_hidden_8K",
          "key": "delta_hidden_8K",
          "value": 0.0,
          "source": "rxrx3_core_result_discovery_micro.json"
        },
        {
          "path": "Axis10.theta_axis10_residual_star.tuple.delta_hidden_8K",
          "key": "delta_hidden_8K",
          "value": 0.0,
          "source": "rxrx3_core_result_discovery_micro.json"
        }
      ],
      "surface_pointer_status": "ABSTRACT_LAYER_ONLY",
      "surface_pointer_path": null,
      "note": "Path-only report. No biological interpretation emitted."
    }
  ],
  "visible_surface_fields": [
    {
      "surface_path": "observed_collision",
      "raw_value": {
        "digest": "923e8f259a606dd40355f0fe0b2cecc473dd3755cf7b3ed9c2403c34e2423d60",
        "identity_a": "PLK1 / PLK1_guide_1 / CRISPR Gene Positive Controls",
        "identity_b": "AKR1C3 / AKR1C3_guide_5 / Query guides",
        "meaning": "same 384-feature embedding digest across distinct metadata identities"
      },
      "status": "SURFACE_PRESENT_NO_ATOM_LINK"
    },
    {
      "surface_path": "relation_mix_summary",
      "raw_value": {
        "sample_count": 222601,
        "time_count": 222601,
        "identity_preserved": true
      },
      "status": "SURFACE_PRESENT_NO_ATOM_LINK"
    },
    {
      "surface_path": "witness",
      "raw_value": {
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
      },
      "status": "SURFACE_PRESENT_NO_ATOM_LINK"
    },
    {
      "surface_path": "Axis10.s_pi",
      "raw_value": [
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
      "status": "SURFACE_PRESENT_NO_ATOM_LINK"
    },
    {
      "surface_path": "Axis10.residual_budget",
      "raw_value": {
        "a9": 1.5282207919307684,
        "a5": 0.7638888888888888,
        "a7_8K": 0.00022150707649535271,
        "a8_8K": 0.7641103959653842,
        "visible_sum": 1.5282207919307684,
        "delta_hidden_8K": 0.0
      },
      "status": "SURFACE_PRESENT_NO_ATOM_LINK"
    },
    {
      "surface_path": "Axis10.theta_axis10_residual_star",
      "raw_value": {
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
      "status": "SURFACE_PRESENT_NO_ATOM_LINK"
    },
    {
      "surface_path": "closure",
      "raw_value": {
        "verdict": "CLOSED_WITH_RESIDUAL_CARRIED",
        "closure_signal_score": 9,
        "closure_signal_possible": 9,
        "remaining_object": "theta_axis10_residual_star"
      },
      "status": "SURFACE_PRESENT_NO_ATOM_LINK"
    },
    {
      "surface_path": "Sefer",
      "raw_value": {
        "landed": 1,
        "source": "axis10_estuary_no_narrow_orchestration",
        "seal": "270968ffcd29de57b4a7fcb054d8e518fec610d7842b118f5645d8438b2c447b",
        "db_path": "<private-sefer-db>"
      },
      "status": "SURFACE_PRESENT_NO_ATOM_LINK"
    },
    {
      "surface_path": "outcome_counts",
      "raw_value": {
        "success": 9,
        "null": 0,
        "unknown": 0,
        "nonmatch": 0,
        "error": 0,
        "timeout": 0,
        "break": 0
      },
      "status": "SURFACE_PRESENT_NO_ATOM_LINK"
    }
  ],
  "canvas_statement": {
    "result": "The full surface layer is now painted as paths and raw values only.",
    "interpretation": "none",
    "biological_claims": "none",
    "atom_to_observed_collision_relation": "NOT_EMITTED_IN_SOURCE_FIELDS"
  }
}
```

### T5 - THEMIS_ENGLISH_SURFACE_MEANING_EMITTED

The emitted meaning is a verification frontier: identity accounting, metadata alignment, biological review, and frontier discovery.

Source paths:
- `rxrx3_biological_frontier_sefer_english.json.frontier_paths_for_scientist`

Source values:

```json
{
  "frontier_paths_for_scientist": [
    {
      "path": "identity-accounting path",
      "source_fields": [
        "micro_sample.observed_collision.identity_a",
        "micro_sample.observed_collision.identity_b",
        "micro_sample.relation_mix_summary.identity_preserved"
      ],
      "question_opened": "When two distinct metadata identities share one embedding digest, what identity relation must downstream analysis preserve?",
      "why_it_matters": "The sample reports identity preservation as true while the representation digest is shared.",
      "next_checks": [
        "Keep well_id, gene, treatment, plate, address, cell_type, perturbation_type, and well_type_label attached to every embedding row.",
        "Do not use embedding equality alone as biological identity equality.",
        "Report the equality as a representation event plus metadata distinction."
      ]
    },
    {
      "path": "metadata-alignment path",
      "source_fields": [
        "metadata rows for gene-134_2_L39 and gene-134_2_N26",
        "micro_sample.observed_collision.digest"
      ],
      "question_opened": "Does the shared digest arise from metadata alignment, export alignment, feature duplication, or intended representation degeneracy?",
      "why_it_matters": "The two wells carry different identities while the digest is identical.",
      "next_checks": [
        "Check whether the two well_ids map to different source images or image sets.",
        "Check whether feature extraction/export duplicated a vector.",
        "Check whether metadata row order and embedding row order are aligned.",
        "Check whether either well is a control/query alias or normalization artifact."
      ]
    },
    {
      "path": "biological-review path",
      "source_fields": [
        "gene",
        "treatment",
        "perturbation_type",
        "cell_type",
        "well_type_label"
      ],
      "question_opened": "What biological interpretation, if any, is justified when distinct perturbation identities share the same representation?",
      "why_it_matters": "The sample alone shows representation equality, not biological equivalence.",
      "next_checks": [
        "Ask a domain scientist whether PLK1 guide/control and AKR1C3 query guide should ever collapse at the embedding level.",
        "Review whether both rows share cell type and perturbation modality.",
        "Separate biological equivalence, representation degeneracy, and data-pipeline duplication as different hypotheses."
      ]
    },
    {
      "path": "frontier-discovery path",
      "source_fields": [
        "micro_sample.Axis10.theta_axis10_residual_star",
        "micro_sample.closure.remaining_object",
        "voice_card.voice_extract"
      ],
      "question_opened": "What new question is opened by carrying the unresolved identity gap instead of resolving it away?",
      "why_it_matters": "The runtime names theta_axis10_residual_star as the remaining carried object and lands the finding as a carried-residual discovery record.",
      "next_checks": [
        "Treat the event as a prompt for follow-up curation, not as a final biological conclusion.",
        "Create a review queue for exact embedding duplicates across distinct biological metadata.",
        "Rank similar events by whether they cross gene, guide, control/query, experiment, plate, or cell-type boundaries."
      ]
    }
  ]
}
```

### T6 - NOT_EMITTED_AS_BIOLOGICAL_MECHANISM

The current surface does not assert a new biological mechanism or biological equivalence between PLK1 and AKR1C3.

Source paths:
- `rxrx3_biological_frontier_sefer_english.json.guardrail`
- `rxrx3_biological_frontier_sefer_english.json.frontier_paths_for_scientist.biological-review path`

Source values:

```json
{
  "guardrail": "No new biological mechanism is asserted. This record translates source fields into scientist-facing questions and next checks.",
  "biological_review_path": [
    {
      "path": "biological-review path",
      "source_fields": [
        "gene",
        "treatment",
        "perturbation_type",
        "cell_type",
        "well_type_label"
      ],
      "question_opened": "What biological interpretation, if any, is justified when distinct perturbation identities share the same representation?",
      "why_it_matters": "The sample alone shows representation equality, not biological equivalence.",
      "next_checks": [
        "Ask a domain scientist whether PLK1 guide/control and AKR1C3 query guide should ever collapse at the embedding level.",
        "Review whether both rows share cell type and perturbation modality.",
        "Separate biological equivalence, representation degeneracy, and data-pipeline duplication as different hypotheses."
      ]
    }
  ]
}
```

### T7 - NULL_SURFACES_PRESERVED

Null states are preserved and classified separately from the RxRx3 biological sample.

Source paths:
- `rxrx3_biological_frontier_sefer_english.json.null_state_note`
- `themis_full_surface_layer_voice.json.null_surfaces`

Source values:

```json
{
  "null_state_note": {
    "method": "JSON structure walk and filesystem existence checks only; no regex classification",
    "counts_by_kind": {
      "loaded_output_status_null": 15,
      "raw_jsonl_status_null": 1,
      "trace_status_null": 16,
      "micro_sample_value_null": 1
    },
    "translation": "The 16 package null states are classified separately from the RxRx3 biological sample. They correspond to absent candidate outputs in the micro sandbox trace, while the micro sample itself has one null field: Axis10.quarantine."
  },
  "null_surfaces": [
    {
      "path": "<private-themis-root>\\runs\\rxrx3_core_discovery_micro_sandbox\\runs\\axis10_estuary_no_narrow\\full_rich_result.json",
      "status": "NULL_SURFACE",
      "data": null
    },
    {
      "path": "<private-themis-root>\\runs\\rxrx3_core_discovery_micro_sandbox\\runs\\axis10_estuary_no_narrow\\orchestration_result.json",
      "status": "NULL_SURFACE",
      "data": null
    },
    {
      "path": "<private-themis-root>\\runs\\rxrx3_core_discovery_micro_sandbox\\runs\\axis10_estuary_ibm_qshot\\ibm_qshot_result.json",
      "status": "NULL_SURFACE",
      "data": null
    },
    {
      "path": "<private-themis-root>\\runs\\rxrx3_core_discovery_micro_sandbox\\runs\\axis10_estuary_ibm_qshot\\axis10_from_full_rich.json",
      "status": "NULL_SURFACE",
      "data": null
    },
    {
      "path": "<private-themis-root>\\runs\\rxrx3_core_discovery_micro_sandbox\\runs\\axis10_estuary_ibm_qshot\\axis10_orchestration_result.json",
      "status": "NULL_SURFACE",
      "data": null
    },
    {
      "path": "<private-themis-root>\\runs\\rxrx3_core_discovery_micro_sandbox\\runs\\axis10_final_research_architecture\\themis_axis10_final_research_architecture_closure_package.json",
      "status": "NULL_SURFACE",
      "data": null
    },
    {
      "path": "<private-themis-root>\\runs\\rxrx3_core_discovery_micro_sandbox\\runs\\axis10_all_direction_system_voice\\axis10_closure_signal_discovery.json",
      "status": "NULL_SURFACE",
      "data": null
    },
    {
      "path": "<private-themis-root>\\runs\\rxrx3_core_discovery_micro_sandbox\\runs\\axis10_all_direction_system_voice\\axis10_closure_signal_truth_guidance.json",
      "status": "NULL_SURFACE",
      "data": null
    },
    {
      "path": "<private-themis-root>\\runs\\rxrx3_core_discovery_micro_sandbox\\runs\\axis10_natural_law_residual_discovery\\natural_law_residual_discovery.json",
      "status": "NULL_SURFACE",
      "data": null
    },
    {
      "path": "<private-themis-root>\\runs\\rxrx3_core_discovery_micro_sandbox\\runs\\themis_no_narrow_L1_L52_full_audit\\summary.json",
      "status": "NULL_SURFACE",
      "data": null
    },
    {
      "path": "<private-themis-root>\\runs\\rxrx3_core_discovery_micro_sandbox\\runs\\themis_no_narrow_L1_L52_full_audit\\counts.json",
      "status": "NULL_SURFACE",
      "data": null
    },
    {
      "path": "<private-themis-root>\\runs\\rxrx3_core_discovery_micro_sandbox\\runs\\themis_no_narrow_L1_L52_full_audit\\failures.json",
      "status": "NULL_SURFACE",
      "data": null
    },
    {
      "path": "<private-themis-root>\\runs\\rxrx3_core_discovery_micro_sandbox\\runs\\themis_no_narrow_L1_L52_full_audit\\module_inventory.json",
      "status": "NULL_SURFACE",
      "data": null
    },
    {
      "path": "<private-themis-root>\\runs\\rxrx3_core_discovery_micro_sandbox\\runs\\themis_no_narrow_L1_L52_full_audit\\callable_inventory.json",
      "status": "NULL_SURFACE",
      "data": null
    },
    {
      "path": "<private-themis-root>\\runs\\rxrx3_core_discovery_micro_sandbox\\runs\\themis_no_narrow_L1_L52_full_audit\\raw_records.jsonl",
      "status": "NULL_SURFACE",
      "data": null
    }
  ]
}
```

## Not claimed

- PLK1 equals AKR1C3.
- The two perturbations are biologically equivalent.
- The duplicate digest is proven to be a data-pipeline error.
- The duplicate digest is proven to be intended representation degeneracy.
- a9, a5, a7, or a8 directly explain the observed collision.
- A new biological mechanism has been discovered.
- The human-verified scientific conclusion is complete.

## Human verification protocol

### 1. Duplicate digest confirmation

Re-read or recompute the 384-feature vectors for gene-134_2_L39 and gene-134_2_N26 and confirm the shared digest.

### 2. Metadata row confirmation

Verify both metadata rows in data_public_matt/rxrx3_core/metadata_rxrx3_core.csv.

### 3. Row alignment audit

Verify that embedding rows and metadata rows align and that no row-order shift occurred.

### 4. Source image audit

Verify whether the two well IDs map to distinct source images or image sets.

### 5. Export duplication audit

Check whether feature extraction or export duplicated a vector.

### 6. Representation degeneracy review

Check whether exact embedding equality across distinct metadata identities is expected or anomalous in this embedding surface.

### 7. Biological review

Ask a domain scientist whether this PLK1 guide/control and AKR1C3 query guide pair should ever collapse at representation level.

### 8. Scale frontier

Build a review queue for all exact embedding duplicates across distinct metadata identities, ranked by boundary crossed.

## Source seals

```json
{
  "micro_sample_sha256": "03c16a22614d1e89d42150be8b56900e14bee4040e7f0117bbfdc32b7ac90685",
  "voice_card_sha256": "ecda4ebfda285364b12abf648ea15daa5cf415f16ac90caa0b923bafe07745a5",
  "voice_card_seal": "fa3a9208d7c64bcb2727354c79acee98196a91be9ef8fb2a7d778b12afade422"
}
```

## Source hashes

```json
{
  "biological_frontier_english": {
    "path": "runs\\rxrx3_core_discovery_micro_sandbox\\rxrx3_biological_frontier_sefer_english.json",
    "exists": true,
    "sha256": "5f98d1acf1c264690f7f86388686d42981c7443d3fd5e0a9c3d17af7b98c7053"
  },
  "biological_frontier_md": {
    "path": "runs\\rxrx3_core_discovery_micro_sandbox\\RXRX3_BIOLOGICAL_FRONTIER_SEFER_ENGLISH.md",
    "exists": true,
    "sha256": "3a73845e214698a831d5803df3b4fbd2193157d406a2659c03ccdd33c9e62305"
  },
  "full_surface_layer_voice": {
    "path": "runs\\rxrx3_core_discovery_micro_sandbox\\themis_full_surface_layer_voice.json",
    "exists": true,
    "sha256": "aa678c270d50f18cafbe4cc76f67912010e55d84cc3a9af8006ac74c5948c3a1"
  },
  "full_surface_layer_md": {
    "path": "runs\\rxrx3_core_discovery_micro_sandbox\\THEMIS_FULL_SURFACE_LAYER_VOICE.md",
    "exists": true,
    "sha256": "489ebf8576dd4b49a1f8c1d8bc6aa7375c644ca05f37dc9d983af89f1dcb86f0"
  },
  "translation_surface_index": {
    "path": "runs\\rxrx3_core_discovery_micro_sandbox\\themis_residual_translation_surface_index.json",
    "exists": true,
    "sha256": "e7bcfd77e8b777f6f5f9b63757dc8a8ad1c98eea5fbb02004177ca47e9dbccb9"
  },
  "residual_voice_package": {
    "path": "runs\\rxrx3_core_discovery_micro_sandbox\\residual_identity_voice\\axis10_estuary_discovery_sefer_kernel_voice_package.json",
    "exists": true,
    "sha256": "383ac72d9b83dbacb41bff4b91fcc8187eead1a6a1cc6e7298b88c6a0b7af807"
  },
  "rxrx3_micro": {
    "path": "runs\\rxrx3_core_discovery_micro_sandbox\\rxrx3_core_result_discovery_micro.json",
    "exists": true,
    "sha256": "03c16a22614d1e89d42150be8b56900e14bee4040e7f0117bbfdc32b7ac90685"
  },
  "meaning_question_card": {
    "path": "runs\\rxrx3_core_discovery_micro_sandbox\\themis_surface_meaning_english_question_card.json",
    "exists": true,
    "sha256": "64e4d7c4108b15691cb6c1344ee3491e4b8df3ad2a70424b1180e624d0339cc2"
  }
}
```
