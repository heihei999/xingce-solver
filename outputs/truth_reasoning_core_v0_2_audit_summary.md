# Truth Reasoning Core v0.2 — Real Case Audit Summary

## Overall

- total: 12
- solved: 1
- ambiguous: 10
- inconsistent: 0
- analysis_only: 1

## Failure Stage Distribution

- assignment: 10
- extract_statements: 1
- none: 1

## Per-Case Results

| case_id | expected | status | failure_stage | num_stmts | facts |
|---|---|---|---|---|---|
| LTRUTH-REAL-001 | A | ambiguous | assignment | 4 | 3 |
| LTRUTH-REAL-002 | A | ambiguous | assignment | 4 | 2 |
| LTRUTH-REAL-003 | D | ambiguous | assignment | 4 | 6 |
| LTRUTH-REAL-004 | D | analysis_only | extract_statements | 0 | 0 |
| LTRUTH-REAL-005 | C | ambiguous | assignment | 3 | 2 |
| LTRUTH-REAL-006 | C | ambiguous | assignment | 4 | 1 |
| LTRUTH-REAL-007 | A | ambiguous | assignment | 4 | 4 |
| LTRUTH-REAL-008 | C | ambiguous | assignment | 4 | 4 |
| LTRUTH-REAL-009 | A | solved | none | 3 | 2 |
| LTRUTH-REAL-010 | B | ambiguous | assignment | 4 | 4 |
| LTRUTH-REAL-011 | B | ambiguous | assignment | 3 | 3 |
| LTRUTH-REAL-012 | C | ambiguous | assignment | 3 | 3 |

## Analysis

### Core engine can handle

- LTRUTH-REAL-009: none

### Blocked at extract_statements

- LTRUTH-REAL-004: num_statements=0

### Blocked at parse_statement

- (none)

### Blocked at assignment (constraint + statements parsed, but not solved)

- LTRUTH-REAL-001: num_assignments=4
- LTRUTH-REAL-002: num_assignments=4
- LTRUTH-REAL-003: num_assignments=4
- LTRUTH-REAL-005: num_assignments=3
- LTRUTH-REAL-006: num_assignments=4
- LTRUTH-REAL-007: num_assignments=4
- LTRUTH-REAL-008: num_assignments=6
- LTRUTH-REAL-010: num_assignments=4
- LTRUTH-REAL-011: num_assignments=2
- LTRUTH-REAL-012: num_assignments=3

## Next Steps

- solved count too low; continue core enhancement before integration.
- assignment logic needs improvement; check constraint parsing and contradiction detection.
- Do NOT enter v7 integration until solved >= 4 on these 12 cases.

## Recommendation

**Continue core v0.3 enhancement.** Do not enter v7 integration yet.
