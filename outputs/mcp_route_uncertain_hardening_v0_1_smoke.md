# MCP route_uncertain Hardening v0.1 Smoke Report

## 1. Baseline

- HEAD before change: 08db5cc
- tag: stable-guarded-mcp-client-smoke-08db5cc

## 2. Problem observed in actual Claude Code client test

During Claude Code MCP client testing:

- route_xingce_question was visible and callable
- compose_xingce_analysis_prompt was visible and callable
- However, `question_text = "条件不足"`, `options = null`, `strict_mode = true` routed to logic_analysis with high confidence
- No answer / selected_option / prediction was returned (correct behavior)
- The issue was that "条件不足" was being matched by the "条件" keyword in logic_analysis

## 3. Fix scope

Only harden route_uncertain fallback behavior:

1. Add insufficient signal detection before keyword matching
2. Fix logic_analysis weak trigger (single "条件" keyword)
3. Ensure "条件不足", "信息不足", etc. route to route_uncertain
4. Add tests for edge cases

## 4. Changes made

### 4.1 src/xingce_solver/mcp_server.py

Added insufficient signal detection in `_route_xingce_question_core`:
- Empty/blank text detection
- Insufficient phrases detection (条件不足, 信息不足, 题干不足, 看不出来, 无法判断, 不确定, 缺少选项, 缺少图片, 无明显题型信号, 不知道, 不清楚, 不明白)
- Too short text detection (< 4 chars)
- No options + short text detection (< 8 chars)

Fixed logic_analysis weak trigger:
- Strong keywords now include: 甲乙丙, 甲乙丙丁, 排序, 位置, 真假, 命题, 如果那么, 只有才, 除非否则, 谁说真话, 谁说假话, 条件组合, 逻辑推理
- Structure keywords (条件, 甲, 乙, 丙, 丁) now require at least 3 matches + "条件" present

### 4.2 tests/test_mcp_guidance_tools_preview.py

Added 22 new tests in two new test classes:
- TestRouteUncertainHardening (14 tests)
- TestComposeRouteUncertainHardening (8 tests)

## 5. Expected behavior after fix

Under strict_mode=True:

- "条件不足" + options=None → route_uncertain
- "信息不足" → route_uncertain
- "无法判断" → route_uncertain
- "不确定" → route_uncertain
- empty text → route_uncertain
- too short text (< 4 chars) → route_uncertain
- no options + short text → route_uncertain

module_guess = unknown, confidence = unknown, recommended_tool = null, fallback_policy = analysis_only_if_uncertain

## 6. Regression expectations

Strong module signals still route normally:

- graphic_reasoning: image_present=true or "图形 规律 选择最合适的一项"
- definition_judgement: "定义 符合上述定义"
- analogy_reasoning: "医生：医院" with options containing "：" pattern
- quantity_relation: "工程 几天 多少"
- verbal_reasoning: "文段 主旨 意在说明"
- data_analysis: "同比 增长率 比重"
- logic_reasoning: "支持 加强 削弱 前提"
- logic_analysis: "甲乙丙三人排序 甲在乙前面 条件组合" (strong structural signals)

## 7. Test results

- tests/test_mcp_guidance_tools_preview.py -q: 99 passed (was 77, added 22 new tests)
- tests/test_verbal_reasoning_scaffold.py -q: 23 passed
- tests/test_quantity_relation_scaffold.py -q: 22 passed
- tests/test_graphic_reasoning_scaffold.py -q: 23 passed
- tests/test_judgement_reasoning_scaffolds.py -q: 48 passed
- python -m pytest -q: 430 passed (was 408, added 22 new tests)

## 8. Boundary check

Confirmed:

- no all_cards.jsonl modification
- no cli.py modification
- no solver modification
- no scaffold source modification
- no MCP tool added
- no CLI integration
- no real-case package
- no fabricated questions
- no OCR/OpenCV/PIL/ML dependency
- no external LLM/API
- no network

## 9. Actual Claude Code MCP inventory

Verified after Claude Code restart (2026-06-16):

- Total visible MCP tools: 12
- Core practical tools: 8 (route_xingce_question, compose_xingce_analysis_prompt, 6 scaffold tools)
- Additional legacy/base knowledge tools: 4 (classify_question, search_methods, get_method_card, get_source_reference)

The "8 tools" wording referred to the core practical tools, not the total client-visible count.

## 10. Conclusion

route_uncertain fallback is now hardened at policy/prompt layer. The router properly detects insufficient signals and routes to route_uncertain instead of misrouting to logic_analysis. It is still not an automatic solver executor.
