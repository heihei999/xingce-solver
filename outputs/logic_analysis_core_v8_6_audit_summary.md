# Logic Analysis Reasoning Core v8.0 — Audit Summary

## Overall

- total: 12
- solved: 2
- ambiguous: 7
- inconsistent: 0
- analysis_only: 3

## Option Mapping Results

- unique_supported: 2
- ambiguous_options: 1
- no_supported_option: 6
- not_attempted: 3

## Option Correctness

- correct: 2
- wrong: 0
- null: 10

## Failure Stage Distribution

- option_mapping: 6
- none: 3
- assignment_search: 1
- entity_domain_extract: 1
- constraint_parse: 1

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
| LANALYSIS-REAL-001 | comparison | ambiguous | ambiguous_options | - | - |
| LANALYSIS-REAL-002 | ordering_adjacency | ambiguous | no_supported_option | - | - |
| LANALYSIS-REAL-003 | grouping | analysis_only | not_attempted | - | - |
| LANALYSIS-REAL-004 | half_true_half_false | solved | unique_supported | C | Y |
| LANALYSIS-REAL-005 | matching | solved | unique_supported | C | Y |
| LANALYSIS-REAL-006 | half_true_half_false | ambiguous | no_supported_option | - | - |
| LANALYSIS-REAL-007 | half_true_half_false | ambiguous | no_supported_option | - | - |
| LANALYSIS-REAL-008 | ordering | analysis_only | not_attempted | - | - |
| LANALYSIS-REAL-009 | matching | analysis_only | not_attempted | - | - |
| LANALYSIS-REAL-010 | comparison | ambiguous | no_supported_option | - | - |
| LANALYSIS-REAL-011 | ordering | ambiguous | no_supported_option | - | - |
| LANALYSIS-REAL-012 | comparison | ambiguous | no_supported_option | - | - |

## Recommendation

**Continue core enhancement.** Parser and constraint logic need improvement.
