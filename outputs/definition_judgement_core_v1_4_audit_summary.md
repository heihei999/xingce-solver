# Definition Judgement Core — Audit Summary

## Overall

- total: 12
- solved: 0
- ambiguous: 10
- analysis_only: 2
- inconsistent: 0

## Option Mapping Results

- unique_supported: 0
- ambiguous_options: 1
- no_supported_option: 9
- not_attempted: 2

## Option Correctness

- correct: 0
- wrong: 0
- null: 12

## Failure Stage Distribution

- option_assessment: 10
- definition_parse: 2

## Per-Case Results

| case_id | expected | status | polarity | option_status | predicted | correct | failure_stage |
|---|---|---|---|---|---|---|---|
| dj_open_v1_001 | B | ambiguous | positive | no_supported_option | - | - | option_assessment |
| dj_open_v1_002 | B | ambiguous | positive | no_supported_option | - | - | option_assessment |
| dj_open_v1_003 | C | ambiguous | positive | no_supported_option | - | - | option_assessment |
| dj_open_v1_004 | B | ambiguous | negative | ambiguous_options | - | - | option_assessment |
| dj_open_v1_005 | D | ambiguous | positive | no_supported_option | - | - | option_assessment |
| dj_open_v1_006 | B | analysis_only | negative | not_attempted | - | - | definition_parse |
| dj_open_v1_007 | D | ambiguous | negative | no_supported_option | - | - | option_assessment |
| dj_open_v1_008 | A | ambiguous | positive | no_supported_option | - | - | option_assessment |
| dj_open_v1_009 | C | ambiguous | positive | no_supported_option | - | - | option_assessment |
| dj_open_v1_010 | B | analysis_only | unknown | not_attempted | - | - | definition_parse |
| dj_open_v1_011 | D | ambiguous | positive | no_supported_option | - | - | option_assessment |
| dj_open_v1_012 | B | ambiguous | positive | no_supported_option | - | - | option_assessment |

## Option Assessment Details

### dj_open_v1_001 (polarity=positive)
- A: violates matched=[] missing=['object'] violated=[] score=0.00
- B: violates matched=[] missing=['object'] violated=[] score=0.00
- C: violates matched=[] missing=['object'] violated=[] score=0.00
- D: violates matched=[] missing=['object'] violated=[] score=0.00

### dj_open_v1_002 (polarity=positive)
- A: violates matched=[] missing=['result'] violated=[] score=0.00
- B: violates matched=[] missing=['result'] violated=[] score=0.00
- C: violates matched=[] missing=['result'] violated=[] score=0.00
- D: violates matched=[] missing=['result'] violated=[] score=0.00

### dj_open_v1_003 (polarity=positive)
- A: violates matched=[] missing=['result'] violated=[] score=0.00
- B: violates matched=[] missing=['result'] violated=[] score=0.00
- C: violates matched=[] missing=['result'] violated=[] score=0.00
- D: violates matched=[] missing=['result'] violated=[] score=0.00

### dj_open_v1_004 (polarity=negative)
- A: violates matched=[] missing=['object'] violated=[] score=0.00
- B: violates matched=[] missing=['object'] violated=[] score=0.00
- C: violates matched=[] missing=['object'] violated=[] score=0.00
- D: violates matched=[] missing=['object'] violated=[] score=0.00

### dj_open_v1_005 (polarity=positive)
- A: unknown matched=[] missing=[] violated=[] score=0.00
- B: unknown matched=[] missing=[] violated=[] score=0.00
- C: unknown matched=[] missing=[] violated=[] score=0.00
- D: unknown matched=[] missing=[] violated=[] score=0.00

### dj_open_v1_007 (polarity=negative)
- A: unknown matched=[] missing=[] violated=[] score=0.00
- B: unknown matched=[] missing=[] violated=[] score=0.00
- C: unknown matched=[] missing=[] violated=[] score=0.00
- D: unknown matched=[] missing=[] violated=[] score=0.00

### dj_open_v1_008 (polarity=positive)
- A: unknown matched=[] missing=[] violated=[] score=0.00
- B: unknown matched=[] missing=[] violated=[] score=0.00
- C: unknown matched=[] missing=[] violated=[] score=0.00
- D: unknown matched=[] missing=[] violated=[] score=0.00

### dj_open_v1_009 (polarity=positive)
- A: unknown matched=[] missing=[] violated=[] score=0.00
- B: unknown matched=[] missing=[] violated=[] score=0.00
- C: unknown matched=[] missing=[] violated=[] score=0.00
- D: unknown matched=[] missing=[] violated=[] score=0.00

### dj_open_v1_011 (polarity=positive)
- A: unknown matched=[] missing=[] violated=[] score=0.00
- B: unknown matched=[] missing=[] violated=[] score=0.00
- C: unknown matched=[] missing=[] violated=[] score=0.00
- D: unknown matched=[] missing=[] violated=[] score=0.00

### dj_open_v1_012 (polarity=positive)
- A: unknown matched=[] missing=[] violated=[] score=0.00
- B: unknown matched=[] missing=[] violated=[] score=0.00
- C: unknown matched=[] missing=[] violated=[] score=0.00
- D: unknown matched=[] missing=[] violated=[] score=0.00

## Recommendation

**Focus on parser improvements.** Most cases fail at definition parsing or element extraction.
