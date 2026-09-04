# Conservative Answer Prompt Mode v0.4 Smoke Report

## Baseline

- HEAD before: 6bc28ed
- tag: stable-v0.3.1-analogy-priority-bugfix-6bc28ed
- commit: document actual v0.3.1 MCP regression

## New MCP tool

- `compose_xingce_answer_prompt`: Generates conservative answer prompt for LLM-in-the-loop answering.

## Test results

- tests/test_mcp_guidance_tools_preview.py -q: 181 passed (was 153, +28)
- python -m pytest -q: 512 passed (was 484, +28)

## compose_xingce_answer_prompt verification

### Required fields

All returns contain:
- tool ✅
- version ✅
- route ✅
- answer_prompt ✅
- output_schema ✅
- safety_contract ✅
- answer_allowed ✅
- analysis_only_required_if ✅
- model_review_required ✅
- override_allowed ✅

### Forbidden fields

No returns contain:
- answer ✅
- selected_option ✅
- prediction ✅

### answer_prompt content

- "MCP route is advisory, not final" ✅
- "exactly one option is justified" ✅
- "analysis_only" ✅
- "Do not invent missing visual/table content" ✅
- "Do not guess" ✅
- "Do not default to A or the first option" ✅

### Module-specific constraints

- graphic_reasoning: missing visual → analysis_only ✅
- data_analysis: missing table/material → analysis_only ✅
- analogy_reasoning: relationship identification required ✅

### Routing preserved

- 感想∶主观性∶体会 → analogy_reasoning / high ✅
- 图形规律题 → graphic_reasoning / high ✅
- 条件不足 → route_uncertain / answer_allowed=false ✅
- 甲乙丙 排序 位置 条件 → logic_analysis / high ✅

### output_schema

Contains:
- mode ✅
- module ✅
- safety_checks ✅
- read_full_question, unique_option_justified, no_guessing ✅

### safety_contract

- no_answer_field_in_tool_return: true ✅
- no_solver_call: true ✅
- no_external_llm_api: true ✅
- answer_only_when_unique: true ✅
- no_default_to_first_option: true ✅

### analysis_only_required_if

Contains:
- missing_visual_content ✅
- missing_table_or_material ✅
- multiple_plausible_options ✅
- low_confidence ✅
- route_uncertain_without_semantic_override ✅

### allow_answer parameter

- allow_answer=false → answer_allowed=false, "Answer Mode Disabled" in prompt ✅

## MCP tool inventory

- Before v0.4: 14 tools
- After v0.4: 15 tools (+compose_xingce_answer_prompt)

## Safety

- No external LLM/API calls
- No solver/scaffold/knowledge base modification
- No analyze_xingce_question
- No answer/selected_option/prediction in tool output

## Conclusion

v0.4 conservative answer prompt mode is implemented. The new tool generates strict answer prompts without calling external LLMs or returning answers directly.
