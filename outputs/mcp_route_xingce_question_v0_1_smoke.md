# MCP route_xingce_question v0.1 Smoke Report

## 1. Baseline

- HEAD before change: 6fcf83e
- tag: stable-final-solver-scaffold-mcp-closure-6fcf83e

## 2. Files changed

- `src/xingce_solver/mcp_server.py`
- `tests/test_mcp_guidance_tools_preview.py`
- `docs/mcp_guidance_tools_preview_v0_1_design.md`
- `docs/mcp_route_xingce_question_v0_1_design.md`
- `outputs/mcp_route_xingce_question_v0_1_smoke.md`

## 3. Tool added

- `route_xingce_question`

## 4. Contract check

- route-only
- accepts question_text/options/module_hint/image_present/strict_mode
- no answer / selected_option / prediction
- no solver call
- no CLI integration

## 5. Routing smoke cases

- graphic_reasoning: image_present=true → scaffold
- definition_judgement: "属于" keyword → scaffold
- analogy_reasoning: "A：B" structure → scaffold
- logic_reasoning: "削弱" keyword → solver_candidate
- logic_analysis: "甲乙丙" keyword → scaffold
- quantity_relation: "工程" keyword → scaffold
- verbal_reasoning: "主旨" keyword → scaffold
- data_analysis: "增长率" keyword → solver_candidate
- unknown: random text → route_uncertain

### 5.1 route_uncertain hardening (added in v0.1 hardening)

- "条件不足" + options=None + strict_mode=True → route_uncertain
- "信息不足" + strict_mode=True → route_uncertain
- "无法判断" + strict_mode=True → route_uncertain
- empty text + strict_mode=True → route_uncertain
- too short text (< 4 chars) + strict_mode=True → route_uncertain
- no options + short text + strict_mode=True → route_uncertain

## 6. Test results

- tests/test_mcp_guidance_tools_preview.py -q: 99 passed (was 59, added 40 new tests)
- tests/test_verbal_reasoning_scaffold.py -q: 23 passed
- tests/test_quantity_relation_scaffold.py -q: 22 passed
- tests/test_graphic_reasoning_scaffold.py -q: 23 passed
- tests/test_judgement_reasoning_scaffolds.py -q: 48 passed
- python -m pytest -q: 430 passed (was 390, added 40 new tests)

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

route_xingce_question v0.1 provides conservative MCP routing only. It does not perform solving or answer selection.
