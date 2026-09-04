# MCP compose_xingce_analysis_prompt v0.1 Smoke Report

## 1. Baseline

- HEAD before change: 9ddbd7e
- tag: stable-route-only-mcp-question-router-9ddbd7e

## 2. Files changed

- `src/xingce_solver/mcp_server.py`
- `tests/test_mcp_guidance_tools_preview.py`
- `docs/mcp_guidance_tools_preview_v0_1_design.md`
- `docs/mcp_compose_xingce_analysis_prompt_v0_1_design.md`
- `outputs/mcp_compose_xingce_analysis_prompt_v0_1_smoke.md`

## 3. Tool added

- `compose_xingce_analysis_prompt`

## 4. Contract check

- prompt-composition-only
- accepts question_text/options/module_hint/image_present/strict_mode/include_scaffold_summary
- returns route/prompt_text/prompt_contract/expected_response_schema/warnings
- no answer / selected_option / prediction
- no solver call
- no CLI integration

## 5. Prompt composition smoke cases

- graphic_reasoning: scaffold_guidance → prompt references scaffold
- definition_judgement: scaffold_guidance → prompt references scaffold
- analogy_reasoning: scaffold_guidance → prompt references scaffold
- logic_reasoning: solver_candidate → prompt notes no solver
- logic_analysis: scaffold_guidance → prompt references scaffold
- quantity_relation: scaffold_guidance → prompt references scaffold
- verbal_reasoning: scaffold_guidance → prompt references scaffold
- data_analysis: solver_candidate → prompt notes no solver
- unknown: route_uncertain → prompt requests clarification

### 5.1 route_uncertain hardening (added in v0.1 hardening)

When route.recommended_track = route_uncertain:
- prompt_text contains "模块不确定，不要直接作答"
- prompt_text contains "优先要求用户补充模块/题面/图片/选项"
- prompt_text contains "analysis_only"
- prompt_contract.must_not_force_answer = true
- prompt_contract.analysis_only_if_uncertain = true

## 6. Test results

- tests/test_mcp_guidance_tools_preview.py -q: 99 passed (was 77, added 22 new tests)
- tests/test_verbal_reasoning_scaffold.py -q: 23 passed
- tests/test_quantity_relation_scaffold.py -q: 22 passed
- tests/test_graphic_reasoning_scaffold.py -q: 23 passed
- tests/test_judgement_reasoning_scaffolds.py -q: 48 passed
- python -m pytest -q: 430 passed (was 408, added 22 new tests)

## 7. Boundary check

- no all_cards.jsonl modification
- no solver modification
- no scaffold source modification
- no real-case package
- no fabricated questions
- no OCR/OpenCV/PIL/ML dependency
- no external LLM/API
- no network

## 8. Conclusion

compose_xingce_analysis_prompt v0.1 provides structured prompt composition only. It does not perform solving or answer selection.
