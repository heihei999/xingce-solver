# Logic Analysis Reasoning v8.2 — Diagnostic

## v8.1 Failure Summary

| case_id | status | vars | constraints | assignments | option_status | failure_stage | main_reason |
|---|---|---|---|---|---|---|---|
| 001 | ambiguous | 3 | 9 | 2 | no_supported_option | constraint_parse | Comparison not enforced; 2 assignments remain |
| 002 | ambiguous | 7 | 4 | 5040 | no_supported_option | constraint_parse | Adjacency constraints not checked during filtering |
| 003 | analysis_only | 9 | 4 | 0 | not_attempted | entity_domain_extract | 9 vars (noise); domain wrong |
| 004 | ambiguous | 3 | 1 | 6 | no_supported_option | constraint_parse | Half-true-half-false not implemented |
| 005 | ambiguous | 5 | 10 | 120 | no_supported_option | constraint_parse | Half-true-half-false not implemented |
| 006 | ambiguous | 1 | 0 | 3 | no_supported_option | entity_domain_extract | Only 1 var; no constraints |
| 007 | ambiguous | 5 | 5 | 120 | no_supported_option | constraint_parse | Half-true-half-false not implemented |
| 008 | analysis_only | 0 | 0 | 0 | not_attempted | entity_domain_extract | No variables extracted |
| 009 | analysis_only | 4 | 0 | 0 | not_attempted | entity_domain_extract | 4 vars but no constraints |
| 010 | ambiguous | 3 | 4 | 6 | no_supported_option | constraint_parse | Comparison constraints not enforced |
| 011 | ambiguous | 6 | 6 | 360 | no_supported_option | constraint_parse | Truth-mixed constraints not implemented |
| 012 | ambiguous | 6 | 3 | 729 | no_supported_option | constraint_parse | Comparison constraints not enforced |

## v8.2 Priority Fixes

1. **Half-true-half-false** (004, 005, 007): Implement exactly-k-true constraint
2. **Comparison enforcement** (001, 010, 012): Make comparison constraints actually filter assignments
3. **Adjacency enforcement** (002): Make adjacency constraints filter assignments
4. **Option mapping**: Evaluate options against consistent assignments
