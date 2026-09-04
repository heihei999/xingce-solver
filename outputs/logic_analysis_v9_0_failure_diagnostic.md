# Logic Analysis Reasoning v9.0 — Failure Diagnostic

## Summary

- solved: 2 (004, 005)
- ambiguous: 7 (001, 002, 006, 007, 010, 011, 012)
- analysis_only: 3 (003, 008, 009)

## Per-Case Diagnosis

### 001 (expected D, ambiguous, ambiguous_options)
- 3 vars, 9 constraints, 2 assignments
- Options A and B are "possible" → ambiguous_options
- Comparison constraints not strong enough to eliminate one assignment
- **Safe refinement**: strengthen comparison enforcement

### 002 (expected C, ambiguous, no_supported_option)
- 7 vars, 4 constraints, 5040 assignments
- Adjacency constraints not filtering permutations
- **Safe refinement**: enforce adjacency in permutation filtering

### 003 (expected D, analysis_only, not_attempted)
- 9 vars, 4 constraints, 0 assignments (search_space_too_large)
- Variables are noise (too many extracted)
- **Safe refinement**: limit variables to meaningful entities

### 004 (expected C, solved, unique_supported) ✅
- Correctly solved

### 005 (expected C, solved, unique_supported) ✅
- Correctly solved

### 006 (expected D, ambiguous, no_supported_option)
- 1 variable, 0 constraints, 3 assignments
- Variables not properly extracted
- **Safe refinement**: extract box/color variables

### 007 (expected C, ambiguous, no_supported_option)
- 5 variables, 1 constraint, 120 assignments
- Half-true constraints not fully parsed
- **Safe refinement**: improve half-true parsing

### 008 (expected B, analysis_only, not_attempted)
- 0 variables - no extraction
- **Safe refinement**: extract vehicle types and positions

### 009 (expected D, analysis_only, not_attempted)
- 4 variables, 0 constraints - domain not extracted
- **Safe refinement**: extract skills domain

### 010 (expected A, ambiguous, no_supported_option)
- 3 vars, 4 constraints, 6 assignments
- Comparison constraints not enforced
- **Safe refinement**: enforce comparison in filtering

### 011 (expected B, ambiguous, no_supported_option)
- 6 vars, 3 constraints, 360 assignments
- Ordering constraints not enforced
- **Safe refinement**: enforce ordering

### 012 (expected D, ambiguous, ambiguous_options)
- 6 vars, 3 constraints, 720 assignments
- Comparison constraints not enforced
- **Safe refinement**: enforce comparison
