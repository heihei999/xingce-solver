# True-question Routing Hardening v0.2 Smoke Report

## 1. Baseline

- HEAD before change: fed079f
- tag: stable-final-claude-code-mcp-closure-fed079f

## 2. Problems found in true-question coverage testing

- Analogy symbol `∶` was not recognized.
- Economic/proportion quantity relation questions were not recognized.
- Person-month-city arrangement logic analysis questions were not recognized.

## 3. Fix scope

Only route_xingce_question routing hardening.

No solver modification.
No scaffold modification.
No knowledge base modification.
No CLI integration.
No automatic answer executor.

## 4. Changes made

### 4.1 Analogy reasoning: support `∶` symbol

Modified `_route_xingce_question_core` in `mcp_server.py`:
- Added `∶` (Chinese ratio symbol) to analogy separator list
- Support 2-part and 3-part analogies (e.g., "卫冕∶夺冠", "酒器∶尊∶爵")

### 4.2 Quantity relation: economic/proportion keywords

Added economic/proportion keywords:
- 收入, 支出, 盈余, 成本, 万元, 元
- 上半年, 下半年, 全年, 比例, 百分比
- 比去年, 比上年, 增长, 下降

Requires number context to avoid false positives from standalone "增加/减少".

### 4.3 Logic analysis: person-month-city arrangement

Added arrangement detection signals:
- Person keywords: 张, 王, 李, 杨, 甲, 乙, 丙, 丁
- Time keywords: 月, 每月, 每个月, 周, 每周
- Place keywords: 城市, 上海, 苏州, 杭州, 南京, 北京, 广州
- Arrange keywords: 安排, 排布, 对应, 均不同, 不同, 不可能, 一定, 至少, 至多

Requires person + (time or place) + arrange to trigger.

## 5. Route expectations after fix

### Analogy reasoning with ∶

Input: "卫冕∶夺冠"
Options: {"A": "火器∶枪", "B": "演员∶歌唱", "C": "教师∶教书", "D": "运动员∶比赛"}

Result:
- module_guess: analogy_reasoning
- confidence: high
- recommended_track: scaffold_guidance
- recommended_tool: get_analogy_reasoning_scaffold

Input: "酒器∶尊∶爵"
Options: {"A": "兵器∶剑∶矛", "B": "家具∶桌∶椅", "C": "乐器∶琴∶瑟", "D": "文具∶笔∶墨"}

Result:
- module_guess: analogy_reasoning
- confidence: high
- recommended_tool: get_analogy_reasoning_scaffold

### Quantity relation economic

Input: "某企业去年全年收入1200万元，支出960万元。今年收入增加，支出减少，问今年上半年支出比下半年如何？"

Result:
- module_guess: quantity_relation
- recommended_track: scaffold_guidance
- recommended_tool: get_quantity_relation_scaffold

### Logic analysis arrangement

Input: "张、王、李、杨4人到上海、苏州、杭州和南京调研，每个月城市均不同，问以下哪项不可能？"

Result:
- module_guess: logic_analysis
- confidence: high or medium
- recommended_track: scaffold_guidance
- recommended_tool: get_logic_analysis_scaffold

### Route uncertain preserved

Input: "条件不足"
Result: route_uncertain (no change)

Input: "条件"
Result: route_uncertain (not high confidence logic_analysis)

### Strong logic_analysis preserved

Input: "甲乙丙 排序 位置 条件"
Result: logic_analysis / high (no change)

## 6. MCP inventory check

Source tool registration:
- 14 @server.tool() decorators found in mcp_server.py

Registered tools:
1. get_method_card
2. search_methods
3. classify_question
4. get_source_reference
5. solve_data_analysis
6. solve_logic_reasoning
7. get_graphic_reasoning_scaffold
8. get_definition_judgement_scaffold
9. get_analogy_reasoning_scaffold
10. get_logic_analysis_scaffold
11. get_quantity_relation_scaffold
12. get_verbal_reasoning_scaffold
13. route_xingce_question
14. compose_xingce_analysis_prompt

Actual Claude Code visible tools: **14** (verified 2026-06-16 after restart)

- solve_data_analysis: visible
- solve_logic_reasoning: visible
- v0.2 did not add new MCP tools
- The 14 tools were the actual Claude Code visible inventory after restart

## 7. Test results

- tests/test_mcp_guidance_tools_preview.py -q: 110 passed (was 99, added 11 new tests)
- tests/test_verbal_reasoning_scaffold.py -q: 23 passed
- tests/test_quantity_relation_scaffold.py -q: 22 passed
- tests/test_graphic_reasoning_scaffold.py -q: 23 passed
- tests/test_judgement_reasoning_scaffolds.py -q: 48 passed
- python -m pytest -q: 441 passed (was 430, added 11 new tests)

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

## 9. Conclusion

True-question routing coverage is hardened without turning MCP into an automatic answer executor.

The router now properly handles:
1. Analogy questions with ∶ symbol
2. Economic/proportion quantity relation questions
3. Person-month-city arrangement logic analysis questions

Route_uncertain hardening is preserved. Safety fields (no answer/selected_option/prediction) are maintained.

### Actual Claude Code MCP regression (2026-06-16)

- Actual visible MCP tools: **14** (not 12)
- solve_data_analysis: visible
- solve_logic_reasoning: visible
- v0.2 did not add new MCP tools
- The 14 tools were the actual Claude Code visible inventory after restart
- All v0.2 routing scenarios verified in actual client
