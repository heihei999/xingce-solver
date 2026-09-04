# Truth Reasoning v7.1 — Ambiguous Case Diagnostic

## Summary

8 cases remain analysis_only in v7. All have core_status=ambiguous with multiple consistent assignments.

## Per-Case Diagnosis

### LTRUTH-REAL-001 (expected A)
- **core_status**: ambiguous (4 assignments)
- **option_status**: no_supported_option
- **failure_category**: speaker_truth_gap
- **main_reason**: Options use "甲说的不对" (statement 0 is false) + fact claim. Core doesn't map speaker truth to statement assignment.
- **safe_refinement**: speaker-truth option mapping (通用)
- **unsafe_risks**: none

### LTRUTH-REAL-003 (expected D)
- **core_status**: ambiguous (3 assignments)
- **option_status**: no_supported_option
- **failure_category**: option_mapping_gap
- **main_reason**: Options ("没有人达标", "国家队队员未达标") are domain facts not directly tied to statement structure. Core can't derive these from the 3 assignments.
- **safe_refinement**: none identified — requires deeper domain reasoning
- **unsafe_risks**: forcing an answer without logical support

### LTRUTH-REAL-004 (expected D)
- **core_status**: ambiguous (4 assignments)
- **option_status**: no_supported_option
- **failure_category**: statement_parse_gap
- **main_reason**: Statement 1 ("本柜子中有购物礼品") parsed as None. Options reference "第三个柜子里有食品" which is the negation of statement 2.
- **safe_refinement**: improve statement parser for "本柜子中" pattern
- **unsafe_risks**: none

### LTRUTH-REAL-006 (expected C)
- **core_status**: ambiguous (4 assignments)
- **option_status**: no_supported_option
- **failure_category**: option_mapping_gap
- **main_reason**: Options are conditional statements ("如果甲队能够晋级，那么方某的预测是正确的") requiring complex implication evaluation.
- **safe_refinement**: none identified — requires conditional option evaluation
- **unsafe_risks**: forcing an answer without logical support

### LTRUTH-REAL-007 (expected A)
- **core_status**: ambiguous (4 assignments)
- **option_status**: no_supported_option
- **failure_category**: multi_assignment_but_same_option_possible
- **main_reason**: Options B, C, D are contradicted by some assignments. Option A ("甲、乙入选") is not contradicted by any assignment but also not positively entailed. All 4 assignments support the same outcome.
- **safe_refinement**: unique_supported_across_assignments (通用)
- **unsafe_risks**: need to verify no assignment contradicts A

### LTRUTH-REAL-008 (expected C)
- **core_status**: ambiguous (6 assignments)
- **option_status**: no_supported_option
- **failure_category**: multi_assignment_but_same_option_possible
- **main_reason**: 6 consistent assignments for "2 true, 2 false" among 4 suspects. Options are pairs of suspects. Need to check if all assignments support the same pair.
- **safe_refinement**: unique_supported_across_assignments (通用)
- **unsafe_risks**: 6 assignments is a lot — need careful verification

### LTRUTH-REAL-010 (expected B)
- **core_status**: ambiguous (3 assignments)
- **option_status**: no_supported_option
- **failure_category**: option_mapping_gap
- **main_reason**: Options are positional ("第一个", "第二个") — not directly mappable to statement facts. Requires domain reasoning about team ordering.
- **safe_refinement**: none identified
- **unsafe_risks**: forcing an answer without logical support

### LTRUTH-REAL-012 (expected C)
- **core_status**: ambiguous (3 assignments)
- **option_status**: no_supported_option
- **failure_category**: statement_parse_gap + option_mapping_gap
- **main_reason**: Statement 2 ("戊和己两所高校均未中标") parsed as None. Options are triples of schools. Requires negation-based reasoning.
- **safe_refinement**: improve parser for "X和Y均未Z" pattern
- **unsafe_risks**: none

## Safe Refinement Priority

1. **unique_supported_across_assignments** (007, 008) — highest impact, general
2. **speaker-truth option mapping** (001) — general
3. **statement parser improvement** (004, 012) — general
4. **No safe refinement** (003, 006, 010) — must remain analysis_only
