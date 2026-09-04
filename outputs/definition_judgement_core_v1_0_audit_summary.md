# Definition Judgement Core — Audit Summary

## Overall

- total: 12
- solved: 0
- ambiguous: 9
- analysis_only: 3
- inconsistent: 0

## Option Mapping Results

- unique_supported: 0
- ambiguous_options: 0
- no_supported_option: 9
- not_attempted: 3

## Option Correctness

- correct: 0
- wrong: 0
- null: 12

## Failure Stage Distribution

- option_assessment: 11
- definition_parse: 1

## Per-Case Results

| case_id | expected | status | polarity | option_status | predicted | correct | failure_stage |
|---|---|---|---|---|---|---|---|
| dj_open_v1_001 | B | ambiguous | positive | no_supported_option | - | - | option_assessment |
| dj_open_v1_002 | B | ambiguous | positive | no_supported_option | - | - | option_assessment |
| dj_open_v1_003 | C | ambiguous | positive | no_supported_option | - | - | option_assessment |
| dj_open_v1_004 | B | ambiguous | negative | no_supported_option | - | - | option_assessment |
| dj_open_v1_005 | D | ambiguous | positive | no_supported_option | - | - | option_assessment |
| dj_open_v1_006 | B | ambiguous | negative | no_supported_option | - | - | option_assessment |
| dj_open_v1_007 | D | ambiguous | negative | no_supported_option | - | - | option_assessment |
| dj_open_v1_008 | A | analysis_only | unknown | not_attempted | - | - | option_assessment |
| dj_open_v1_009 | C | ambiguous | positive | no_supported_option | - | - | option_assessment |
| dj_open_v1_010 | B | analysis_only | unknown | not_attempted | - | - | option_assessment |
| dj_open_v1_011 | D | analysis_only | positive | not_attempted | - | - | definition_parse |
| dj_open_v1_012 | B | ambiguous | positive | no_supported_option | - | - | option_assessment |

## Option Assessment Details

### dj_open_v1_001 (polarity=positive)
- A: violates matched=[] missing=['action', 'action'] violated=[] score=0.00
- B: violates matched=[] missing=['action', 'action'] violated=[] score=0.00
- C: violates matched=[] missing=['action', 'action'] violated=[] score=0.00
- D: violates matched=[] missing=['action', 'action'] violated=[] score=0.00

### dj_open_v1_002 (polarity=positive)
- A: violates matched=[] missing=['result', 'action', 'action'] violated=[] score=0.00
- B: violates matched=[] missing=['result', 'action', 'action'] violated=[] score=0.00
- C: violates matched=[] missing=['result', 'action', 'action'] violated=[] score=0.00
- D: violates matched=[] missing=['result', 'action', 'action'] violated=[] score=0.00

### dj_open_v1_003 (polarity=positive)
- A: violates matched=[] missing=['result', 'action'] violated=[] score=0.00
- B: violates matched=[] missing=['result', 'action'] violated=[] score=0.00
- C: violates matched=[] missing=['result', 'action'] violated=[] score=0.00
- D: violates matched=[] missing=['result', 'action'] violated=[] score=0.00

### dj_open_v1_004 (polarity=negative)
- A: unknown matched=[] missing=[] violated=[] score=0.00
- B: unknown matched=['keyword'] missing=[] violated=[] score=0.20
- C: unknown matched=[] missing=[] violated=[] score=0.00
- D: unknown matched=[] missing=[] violated=[] score=0.00

### dj_open_v1_005 (polarity=positive)
- A: unknown matched=[] missing=[] violated=[] score=0.00
- B: unknown matched=[] missing=[] violated=[] score=0.00
- C: unknown matched=[] missing=[] violated=[] score=0.00
- D: unknown matched=[] missing=[] violated=[] score=0.00

### dj_open_v1_006 (polarity=negative)
- A: unknown matched=['keyword'] missing=[] violated=[] score=0.20
- B: unknown matched=['keyword'] missing=[] violated=[] score=0.20
- C: unknown matched=['keyword'] missing=[] violated=[] score=0.20
- D: unknown matched=[] missing=[] violated=[] score=0.00

### dj_open_v1_007 (polarity=negative)
- A: unknown matched=[] missing=[] violated=[] score=0.00
- B: unknown matched=[] missing=[] violated=[] score=0.00
- C: unknown matched=[] missing=[] violated=[] score=0.00
- D: unknown matched=[] missing=[] violated=[] score=0.00

### dj_open_v1_008 (polarity=unknown)
- A: violates matched=[] missing=['condition'] violated=[] score=0.00
- B: violates matched=[] missing=['condition'] violated=[] score=0.00
- C: violates matched=[] missing=['condition'] violated=[] score=0.00
- D: violates matched=[] missing=['condition'] violated=[] score=0.00

### dj_open_v1_009 (polarity=positive)
- A: violates matched=[] missing=['condition'] violated=[] score=0.00
- B: violates matched=[] missing=['condition'] violated=[] score=0.00
- C: violates matched=[] missing=['condition'] violated=[] score=0.00
- D: violates matched=[] missing=['condition'] violated=[] score=0.00

### dj_open_v1_010 (polarity=unknown)
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
