# Module Context Edge-Case Hardening v0.5.1 Smoke Report

## Test results

- tests/test_mcp_guidance_tools_preview.py: 261 passed (was 245, +16)
- python -m pytest: 592 passed (was 576, +16)

## Fix 1: module_hint overrides insufficient_phrase_detected

| Sample | module_hint | Expected | Actual | Status |
|--------|------------|----------|--------|--------|
| 作者接下来最可能论述的是： | 言语理解 | verbal_reasoning | verbal_reasoning | ✅ |
| 作者接下来 + answer_prompt | 言语理解 | answer_allowed=true | true | ✅ |
| 条件不足 (no hint) | none | route_uncertain | route_uncertain | ✅ |

## Fix 2: plain graph words don't trigger data_analysis

| Sample | module_hint | Expected | Actual | Status |
|--------|------------|----------|--------|--------|
| 人际关系图...下列属于 | 定义判断 | definition_judgement | definition_judgement | ✅ |
| 人际关系图 + answer_prompt | 定义判断 | answer_allowed=true | true | ✅ |
| 下图是一种关系图示... | 定义判断 | definition_judgement | definition_judgement | ✅ |
| 下图关系图示 + answer_prompt | 定义判断 | answer_allowed=true | true | ✅ |

## Strong material signals still work

| Sample | module_hint | Expected | Actual | Status |
|--------|------------|----------|--------|--------|
| 图中数据显示...比重 | 数量关系 | answer_allowed=false | false | ✅ |
| 表中...增长量 | 数量关系 | answer_allowed=false | false | ✅ |

## v0.5.0 regression (no退化)

| Sample | module_hint | Expected | Actual | Status |
|--------|------------|----------|--------|--------|
| 石头∶雕刻∶雕塑 | 类比推理 | analogy_reasoning | analogy_reasoning | ✅ |
| 构图方式...概括 | 言语理解 | verbal_reasoning | verbal_reasoning | ✅ |
| 男生占比...多少人 | 数量关系 | quantity_relation | quantity_relation | ✅ |
| 2022年A市...多少万人 | 资料分析 | answer_allowed=false | false | ✅ |
| 选择最合适...规律 | 图形推理 | answer_allowed=false | false | ✅ |
| 四本书从左到右 | none | logic_analysis | logic_analysis | ✅ |
| 所谓机会成本 | none | definition_judgement | definition_judgement | ✅ |

## Security

- No answer / selected_option / prediction in MCP output: ✅ (0 leaks)
- No external LLM/API call: ✅
- No analyze_xingce_question: ✅
- No solver/scaffold/knowledge_base modification: ✅
