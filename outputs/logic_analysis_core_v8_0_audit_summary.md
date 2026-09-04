# Logic Analysis Reasoning Core v8.0 — Audit Summary

## Overall

- total: 12
- solved: 0
- ambiguous: 3
- inconsistent: 0
- analysis_only: 9

## Option Mapping Results

- unique_supported: 0
- ambiguous_options: 0
- no_supported_option: 0
- not_attempted: 12

## Option Correctness

- correct: 0
- wrong: 0
- null: 12

## Failure Stage Distribution

- entity_domain_extract: 5
- none: 3
- constraint_parse: 2
- assignment_search: 1
- option_mapping: 1

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
| LANALYSIS-REAL-001 | comparison | analysis_only | not_attempted | - | - |
| LANALYSIS-REAL-002 | ordering_adjacency | analysis_only | not_attempted | - | - |
| LANALYSIS-REAL-003 | grouping | analysis_only | not_attempted | - | - |
| LANALYSIS-REAL-004 | half_true_half_false | analysis_only | not_attempted | - | - |
| LANALYSIS-REAL-005 | matching | analysis_only | not_attempted | - | - |
| LANALYSIS-REAL-006 | half_true_half_false | analysis_only | not_attempted | - | - |
| LANALYSIS-REAL-007 | half_true_half_false | analysis_only | not_attempted | - | - |
| LANALYSIS-REAL-008 | ordering | analysis_only | not_attempted | - | - |
| LANALYSIS-REAL-009 | matching | analysis_only | not_attempted | - | - |
| LANALYSIS-REAL-010 | comparison | ambiguous | not_attempted | - | - |
| LANALYSIS-REAL-011 | ordering | ambiguous | not_attempted | - | - |
| LANALYSIS-REAL-012 | comparison | ambiguous | not_attempted | - | - |

## Recommendation

**Focus on parser improvements.** Most cases fail at entity/domain extraction or constraint parsing.
