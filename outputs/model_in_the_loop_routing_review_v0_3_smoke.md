# Model-in-the-Loop Routing Review v0.3 Smoke Report

## 1. Baseline

- HEAD before: a0fb94c
- tag: stable-v0.2-true-question-routing-mcp-a0fb94c
- commit: document actual v0.2 MCP routing regression

## 2. v0.3 Changes

### New route fields

Added to all route_xingce_question responses:

- `possible_modules`: list of candidate modules with reasons and priority
- `model_review_required`: boolean indicating if Claude must review the route
- `override_allowed`: boolean (always true) allowing Claude to override the route
- `review_instruction`: advisory text for Claude
- `conflict_signals`: list of detected conflict signals

### Improved routing for edge cases

1. **Sentence ordering**: "重新排列"/"语序正确" → verbal_reasoning (was quantity_relation)
2. **Sentence insertion**: "填入文中哪个位置" → verbal_reasoning (was logic_analysis)
3. **Main idea**: "主要介绍/讲/说明" → verbal_reasoning
4. **Three-part analogy**: "感想∶主观性∶体会" → analogy_reasoning (relaxed length limit from 6 to 8)
5. **Data analysis extended**: "占全国/比重/同比增长/上述资料" → data_analysis (before logic_reasoning)

### Compose prompt changes

- Added "题型复核提示" section at the beginning
- Added possible_modules, model_review_required, override_allowed, conflict_signals to route result
- Added review_instruction to option verification section

## 3. Test results

- tests/test_mcp_guidance_tools_preview.py -q: 145 passed (was 110, +35)
- tests/test_verbal_reasoning_scaffold.py -q: 23 passed
- tests/test_quantity_relation_scaffold.py -q: 22 passed
- tests/test_graphic_reasoning_scaffold.py -q: 23 passed
- tests/test_judgement_reasoning_scaffolds.py -q: 48 passed
- python -m pytest -q: 476 passed (was 441, +35)

## 4. v0.3 routing regression results

### Sentence ordering

- "将以上6个句子重新排列，语序正确的一项是" → verbal_reasoning / high
- conflict_signals: contains_排列_but_sentence_order_pattern
- model_review_required: true

### Sentence insertion

- "下面这段文字最适合填入文中哪个位置？" → verbal_reasoning / high
- conflict_signals: contains_位置_but_sentence_insertion_pattern
- model_review_required: true

### Main idea

- "这段文字主要介绍的是：" → verbal_reasoning / high
- "这段文字主要讲的是：" → verbal_reasoning / high
- "这段文字主要说明：" → verbal_reasoning / high

### Three-part analogy

- "感想∶主观性∶体会" → analogy_reasoning / high
- conflict_signals: analogy_symbol_detected

### Data analysis extended

- "2022年中部六省中型灌区新增节水能力占全国中型灌区的（ ）" → data_analysis / medium
- "2022年某地区GDP占全国的比重是多少？" → data_analysis
- "2022年某市GDP同比增长多少？" → data_analysis
- "能够从上述资料中推出的是：" → data_analysis / medium

### Preserved behaviors

- "条件不足" → route_uncertain (preserved)
- "条件" → route_uncertain (preserved)
- "甲乙丙 排序 位置 条件" → logic_analysis / high (preserved)
- "卫冕∶夺冠" → analogy_reasoning / high (preserved)
- "酒器∶尊∶爵" → analogy_reasoning / high (preserved)
- 经济比例题 → quantity_relation / high (preserved)
- 人员-月份-城市排布题 → logic_analysis / high (preserved)

## 5. Safety check

All actual calls returned no:

- answer
- selected_option
- prediction

## 6. Boundary

- No analyze_xingce_question developed.
- No external LLM/API/OCR/ML dependency added.
- No all_cards.jsonl modification.
- No solver modification.
- No scaffold source modification.
- No CLI integration.
- No new MCP tool added.

## 7. Conclusion

v0.3 model-in-the-loop routing review is implemented. The MCP route is now advisory, with Claude required to review and allowed to override based on full question semantics. Edge case routing is improved without adding new MCP tools or automatic answer execution.

## 8. v0.3.1 Analogy Priority Bugfix

### Issue found in actual Claude Code MCP regression

`感想∶主观性∶体会` was incorrectly routed to `graphic_reasoning` because option A "规律∶客观性∶发现" contained "规律" which triggered graphic_keywords before analogy structure detection.

### Fix

Moved analogy structure detection to before graphic_keywords check in `src/xingce_solver/mcp_server.py`. No logic changes, only ordering change.

### Verified after fix

- 感想∶主观性∶体会 (options with 规律) → analogy_reasoning ✅
- 卫冕∶夺冠 → analogy_reasoning ✅
- 酒器∶尊∶爵 → analogy_reasoning ✅
- 图形规律题 → graphic_reasoning ✅ (not degraded)

### Test results after fix

- tests/test_mcp_guidance_tools_preview.py -q: 153 passed (was 145, +8)
- python -m pytest -q: 484 passed (was 476, +8)

## 9. v0.3.1 Actual Claude Code MCP Regression After Restart

- Claude Code was restarted before testing.
- xingce-solver MCP status: Connected.
- Actual visible tools: 14.
- "感想∶主观性∶体会" → analogy_reasoning / high / get_analogy_reasoning_scaffold. Bug fixed, not misrouted to graphic_reasoning.
- "从所给四个选项中，选择最合适的一个，使之呈现一定规律。" → graphic_reasoning / high / get_graphic_reasoning_scaffold. Not regressed.
- v0.3 fields preserved: possible_modules, model_review_required, override_allowed, review_instruction, conflict_signals.
- No answer / selected_option / prediction in any result.
- No MCP server error.
- v0.3.1 passed actual Claude Code MCP regression after restart.
