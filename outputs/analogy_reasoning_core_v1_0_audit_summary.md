# analogy_reasoning core v1_0 Audit Summary

## Overview

- Total: 12
- Solved: 4
- Ambiguous: 3
- Analysis_only: 5
- Inconsistent: 0

## Option Status Distribution

- ambiguous: 3
- no_supported_option: 5
- unique_supported: 4

## Option Correctness

- Correct: 2
- Wrong: 2
- Null: 8

## Failure Stage Distribution

- none: 7
- relation_detect: 5

## Per-Case Results

| case_id | status | stem_relation | option_status | predicted | expected | correct |
|---------|--------|---------------|---------------|-----------|----------|---------|
| analog_001_2023_gk_xz_091 | solved | material_product, naming_convention | unique_supported | A | A | ✅ |
| analog_002_2023_gk_xz_092 | ambiguous | aggregation, degree | ambiguous | — | D | — |
| analog_003_2023_gk_xz_093 | solved | material_product | unique_supported | A | A | ✅ |
| analog_004_2023_gk_xz_094 | analysis_only | unknown | no_supported_option | — | C | — |
| analog_005_2023_gk_xz_095 | ambiguous | grammar_structure | ambiguous | — | D | — |
| analog_006_2023_gk_xz_096 | solved | sequence | unique_supported | C | D | ❌ |
| analog_007_2023_gk_xz_097 | analysis_only | degree | no_supported_option | — | B | — |
| analog_008_2023_gk_xz_098 | ambiguous | degree, grammar_structure | ambiguous | — | D | — |
| analog_009_2023_gk_xz_099 | analysis_only | unknown | no_supported_option | — | C | — |
| analog_010_2023_gk_xz_100 | analysis_only | unknown | no_supported_option | — | B | — |
| analog_011_2023_gk_ds_093 | solved | sequence, purpose | unique_supported | B | A | ❌ |
| analog_012_2023_gk_ds_094 | analysis_only | unknown | no_supported_option | — | C | — |

## ⚠️ Warning

Found 2 wrong predictions. Must tighten rules before integration.

## Recommendation

❌ Has wrong predictions. Must fix before proceeding.
