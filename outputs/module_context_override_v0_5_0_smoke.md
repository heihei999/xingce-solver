# v0.5.0 Module Context Override Smoke Report

## Summary

**Date**: 2026-06-20
**Feature**: module_hint / section_context override for MCP route tools
**Tests**: 245 MCP guidance passed, 576 full pytest passed

## Behavioral Verification

### 1. module_hint=类比推理 overrides route_uncertain

| Sample | module_hint | Expected | Actual | Status |
|--------|-------------|----------|--------|--------|
| 石头∶雕刻∶雕塑 | 类比推理 | analogy_reasoning | analogy_reasoning | ✅ |
| 卫冕∶夺冠 | 判断推理-类比推理 | analogy_reasoning | analogy_reasoning | ✅ |

### 2. module_hint=言语理解 prevents "构图" false positive

| Sample | module_hint | Expected | Actual | Status |
|--------|-------------|----------|--------|--------|
| 这段文字通过分析艺术作品的构图方式... | 言语理解 | verbal_reasoning | verbal_reasoning | ✅ |
| (answer prompt) | 言语理解 | answer_allowed=true | true, block_reason=None | ✅ |

### 3. module_hint=数量关系 prevents "占比" false positive

| Sample | module_hint | Expected | Actual | Status |
|--------|-------------|----------|--------|--------|
| 某班男生人数占全班人数的40%... | 数量关系 | quantity_relation | quantity_relation | ✅ |
| (answer prompt) | 数量关系 | answer_allowed=true | true, block_reason=None | ✅ |

### 4. module_hint=资料分析 still requires material

| Sample | module_hint | Expected | Actual | Status |
|--------|-------------|----------|--------|--------|
| 2022年A市常住人口... | 资料分析 | answer_allowed=false | false | ✅ |
| block_reason | - | missing_table_or_material | missing_table_or_material | ✅ |

### 5. module_hint=图形推理 still requires image

| Sample | module_hint | Expected | Actual | Status |
|--------|-------------|----------|--------|--------|
| 从所给四个选项中... | 图形推理 | answer_allowed=false | false | ✅ |
| block_reason | - | missing_visual_content | missing_visual_content | ✅ |

### 6. Strong material signal overrides module_hint

| Sample | module_hint | Expected | Actual | Status |
|--------|-------------|----------|--------|--------|
| 表中2018—2022年... | 数量关系 | data_analysis | data_analysis | ✅ |
| block_reason | - | missing_table_or_material | missing_table_or_material | ✅ |
| 根据表格，2020年GDP... | 数量关系 | data_analysis | data_analysis | ✅ |

### 7. module_hint conflict fields

| Scenario | module_hint_applied | module_hint_conflict | heuristic_module_guess |
|----------|--------------------|--------------------|----------------------|
| hint matches heuristic | True | False | (same as module_guess) |
| hint overrides heuristic | True | True | (original heuristic) |
| strong material overrides hint | False | True | (original heuristic) |

### 8. v0.4.3 regression (no module_hint)

| Sample | Expected | Actual | Status |
|--------|----------|--------|--------|
| 四本书从左到右摆放 | logic_analysis | logic_analysis | ✅ |
| 所谓机会成本...下列体现 | definition_judgement | definition_judgement | ✅ |
| 表中...平均每年增长量 | data_analysis | data_analysis | ✅ |
| 左边给定纸盒展开图 | graphic_reasoning | graphic_reasoning | ✅ |
| 水池题 | quantity_relation | quantity_relation | ✅ |
| 条件不足 | route_uncertain | route_uncertain | ✅ |

### 9. Safety fields

| Check | Result |
|-------|--------|
| answer field in route result | 0/245 |
| selected_option in route result | 0/245 |
| prediction in route result | 0/245 |
| answer field in compose result | 0/245 |
| External LLM/API call | No |
| analyze_xingce_question developed | No |
| solver/scaffold/all_cards/cli modified | No |

## Test Counts

| Test Suite | Before | After | Delta |
|------------|--------|-------|-------|
| test_mcp_guidance_tools_preview.py | 220 | 245 | +25 |
| Full pytest | 551 | 576 | +25 |

## Files Modified

- `src/xingce_solver/mcp_server.py` — Added `_normalize_module_hint()`, `section_context` param, module_hint override logic, v0.5.0 return fields
- `tests/test_mcp_guidance_tools_preview.py` — Updated 4 existing tests, added 25 new tests

## Files Added

- `docs/module_context_override_v0_5_0.md` — Feature documentation
- `outputs/module_context_override_v0_5_0_smoke.md` — This smoke report
