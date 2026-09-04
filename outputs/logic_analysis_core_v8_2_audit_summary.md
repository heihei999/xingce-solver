# Logic Analysis Reasoning Core v8.0 — Audit Summary

## Overall

- total: 12
- solved: 1
- ambiguous: 7
- inconsistent: 1
- analysis_only: 3

## Option Mapping Results

- unique_supported: 0
- ambiguous_options: 0
- no_supported_option: 8
- not_attempted: 4

## Option Correctness

- correct: 1
- wrong: 0
- null: 11

## Failure Stage Distribution

- option_mapping: 7
- constraint_parse: 2
- assignment_search: 1
- none: 1
- entity_domain_extract: 1

## Task Type Distribution

- comparison: 3
- half_true_half_false: 3
- matching: 2
- ordering: 2
- ordering_adjacency: 1
- grouping: 1

## Per-Case Results

| case_id | task_type | status | option_status | predicted | correct |
|---|---|---|---|---|---|
| LANALYSIS-REAL-001 | comparison | ambiguous | no_supported_option | - | - |
| LANALYSIS-REAL-002 | ordering_adjacency | ambiguous | no_supported_option | - | - |
| LANALYSIS-REAL-003 | grouping | analysis_only | not_attempted | - | - |
| LANALYSIS-REAL-004 | half_true_half_false | solved | no_supported_option | C | Y |
| LANALYSIS-REAL-005 | matching | ambiguous | no_supported_option | - | - |
| LANALYSIS-REAL-006 | half_true_half_false | ambiguous | no_supported_option | - | - |
| LANALYSIS-REAL-007 | half_true_half_false | inconsistent | not_attempted | - | - |
| LANALYSIS-REAL-008 | ordering | analysis_only | not_attempted | - | - |
| LANALYSIS-REAL-009 | matching | analysis_only | not_attempted | - | - |
| LANALYSIS-REAL-010 | comparison | ambiguous | no_supported_option | - | - |
| LANALYSIS-REAL-011 | ordering | ambiguous | no_supported_option | - | - |
| LANALYSIS-REAL-012 | comparison | ambiguous | no_supported_option | - | - |

## Recommendation

**Focus on parser improvements.** Most cases fail at entity/domain extraction or constraint parsing.
