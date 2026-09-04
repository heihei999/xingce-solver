# analogy_reasoning core v1_5_strong Audit Summary

## Overview

- Total: 12
- Solved: 0
- Ambiguous: 4
- Analysis_only: 8
- Inconsistent: 0

## Option Status Distribution

- ambiguous: 4
- no_supported_option: 6
- not_attempted: 2

## Option Correctness

- Correct: 0
- Wrong: 0
- Null: 12

## Failure Stage Distribution

- none: 4
- relation_detect: 6
- stem_parse: 2

## Per-Case Results

| case_id | status | stem_relation | option_status | predicted | expected | correct |
|---------|--------|---------------|---------------|-----------|----------|---------|
| analog_strong_001_tool_profession_object | analysis_only | — | not_attempted | — | A | — |
| analog_strong_002_place_attribute_modifier | analysis_only | unknown | no_supported_option | — | A | — |
| analog_strong_003_action_pair_compound | ambiguous | same_category, unknown | ambiguous | — | A | — |
| analog_strong_004_necessary_attribute | analysis_only | grammar_structure | no_supported_option | — | B | — |
| analog_strong_005_problem_treatment | analysis_only | degree, degree | no_supported_option | — | A | — |
| analog_strong_006_state_progression | ambiguous | grammar_structure, grammar_structure | ambiguous | — | B | — |
| analog_strong_007_event_action_effect | ambiguous | unknown, unknown | ambiguous | — | A | — |
| analog_strong_008_avoidance_purpose | ambiguous | unknown, unknown | ambiguous | — | C | — |
| analog_strong_009_passive_object_place | analysis_only | — | not_attempted | — | D | — |
| analog_strong_010_species_genus_1 | analysis_only | material_product | no_supported_option | — | A | — |
| analog_strong_011_species_genus_2 | analysis_only | whole_part | no_supported_option | — | B | — |
| analog_strong_012_tool_function | analysis_only | unknown | no_supported_option | — | A | — |

## Recommendation

✅ No wrong predictions. Continue refinement to increase solved count.
