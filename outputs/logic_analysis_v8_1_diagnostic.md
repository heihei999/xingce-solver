# Logic Analysis Reasoning v8.1 — Diagnostic

## v8.0 Failure Summary

| case_id | status | vars | constraints | assignments | failure_stage | main_reason |
|---|---|---|---|---|---|---|
| 001 | analysis_only | 2 | 0 | 0 | entity_domain_extract | Variables wrong ("有教师" instead of "甲"); domain empty |
| 002 | analysis_only | 15 | 4 | 0 | entity_domain_extract | 15 vars with domain 1-15; should be 7 stars with domain 1-7 |
| 003 | analysis_only | 4 | 4 | 1 | entity_domain_extract | Domain wrong; constraints are noise |
| 004 | analysis_only | 0 | 0 | 0 | entity_domain_extract | No variables; half-true-half-false not supported |
| 005 | analysis_only | 5 | 0 | 0 | entity_domain_extract | Variables extracted but domain empty |
| 006 | analysis_only | 0 | 0 | 0 | entity_domain_extract | No variables; half-true-half-false not supported |
| 007 | analysis_only | 0 | 0 | 0 | entity_domain_extract | No variables; half-true-half-false not supported |
| 008 | analysis_only | 0 | 0 | 0 | entity_domain_extract | No variables extracted |
| 009 | analysis_only | 0 | 0 | 0 | entity_domain_extract | No variables extracted |
| 010 | ambiguous | 3 | 3 | 6 | option_mapping | Variables/domain correct; option mapping not attempted |
| 011 | ambiguous | 4 | 6 | 24 | option_mapping | Partial success; option mapping not attempted |
| 012 | ambiguous | 3 | 2 | 6 | option_mapping | Variables/domain correct; option mapping not attempted |

## Key Issues

1. **Variable extraction**: Pattern `X、Y、Z三人` fails for many formats
2. **Domain extraction**: Most cases have empty domains
3. **Half-true-half-false**: Not implemented (004, 006, 007)
4. **Option parsing**: Not extracting variable/domain from options
5. **Constraint parsing**: Many constraints not parsed or parsed as noise

## Safe Refinement Candidates

1. Extract variables from options (A/B/C/D options contain "甲是教师" → domain includes "教师")
2. Improve variable extraction patterns
3. Improve domain extraction from context
4. Add half-true-half-false basic support
5. Add option mapping for cases with consistent assignments
