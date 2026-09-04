# Definition Judgement v1.4 — Failure Diagnostic

## Per-Case Analysis

| case_id | expected | polarity | status | elements | assessments | main_reason |
|---|---|---|---|---|---|---|
| 001 | B | positive | ambiguous | 6 | all violate (0 matched, 6 missing) | Elements too specific, no keyword overlap with options |
| 002 | B | positive | ambiguous | 3 | all violate (0 matched, 3 missing) | Same — elements don't match option text |
| 003 | C | positive | ambiguous | 2 | all violate (0 matched, 2 missing) | Same |
| 004 | B | negative | ambiguous | 1 | all violate (0 matched, 1 missing) | Only 1 element extracted |
| 005 | D | positive | ambiguous | 15 | all unknown | Multi-definition, elements not matched to options |
| 006 | B | negative | ambiguous | 8 | A/B/C match, D unknown | Closer! But can't distinguish A/B/C |
| 007 | D | negative | ambiguous | 5 | all unknown | Elements not matching option text |
| 008 | A | unknown | analysis_only | 1 | all violate | Polarity detection failed |
| 009 | C | positive | ambiguous | 1 | all violate | Only 1 element extracted |
| 010 | B | unknown | analysis_only | 1 | all violate | Polarity detection failed |
| 011 | D | positive | analysis_only | 0 | none | Definition not parsed at all |
| 012 | B | positive | ambiguous | 3 | all unknown | Elements not matching |

## Key Issues

1. **Element extraction too narrow**: Elements like "案件现场有关物质材料" are too specific. Need broader keyword extraction.
2. **Option matching too strict**: All options show "violates" because element text doesn't appear in option text.
3. **Term parsing bugs**: "本质就" instead of "预判设计", "即使面对的" instead of "院墙外正义"
4. **Polarity detection**: 008 and 010 return "unknown"
5. **No definition parsed for 011**: "田园综合体：指..." format not handled

## Safe Refinement Candidates

1. Fix term parsing regex
2. Add ":" definition format
3. Fix polarity for "下列说法正确/错误"
4. Use keyword-based scoring instead of element matching
5. Extract broader definition keywords
