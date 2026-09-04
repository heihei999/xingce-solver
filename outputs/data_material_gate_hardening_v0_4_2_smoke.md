# Data Material Gate Hardening v0.4.2 Smoke Report

## 1. Fix Background

External clean runtime 60-case stress test found a routing vulnerability:

**Problem sample**: "表中2018—2022年工业增加值平均每年增长量约为多少亿元？"

**Expected**: route.module_guess = data_analysis, answer_allowed = false (missing table)

**Actual (before fix)**: route.module_guess = quantity_relation, answer_allowed = true

**Root cause**: "表中" was not recognized as a data_analysis strong signal, so the question was routed to quantity_relation, bypassing the missing_table_or_material gate.

## 2. Route Fix Results

| Sample | Expected | Actual |
|--------|----------|--------|
| 表中2018—2022年工业增加值平均每年增长量约为多少亿元？ | data_analysis | data_analysis ✅ |
| 根据表格，2021年甲地区生产总值同比增长率约为多少？ | data_analysis | data_analysis ✅ |
| 上述资料显示，2022年A市常住人口比上年增加了多少万人？ | data_analysis | data_analysis ✅ |
| 图中数据显示，第三季度销售额占全年销售额的比重约为多少？ | data_analysis | data_analysis ✅ |

## 3. Independent Data Material Gate Results

| Sample | material_present | answer_allowed | answer_block_reason |
|--------|------------------|----------------|---------------------|
| 表中...增长量 | false | false | missing_table_or_material ✅ |
| 表中...增长量 | true | true | null ✅ |
| 根据表格...增长率 | false | false | missing_table_or_material ✅ |
| 上述资料...增加 | false | false | missing_table_or_material ✅ |
| 图中数据...比重 | false | false | missing_table_or_material ✅ |

## 4. context_requirements.requires_table_or_material

All samples with material signals correctly set requires_table_or_material = true, even when route_module_guess is not data_analysis.

## 5. Ordinary Quantity Relation Negative Cases

| Sample | Expected | Actual |
|--------|----------|--------|
| 一个水池甲管注满需8小时，乙管注满需12小时，两管同时开几小时注满？ | quantity_relation | quantity_relation ✅ |
| 甲乙两车相向而行，甲车每小时60公里，乙车每小时80公里，几小时相遇？ | quantity_relation | quantity_relation ✅ |

## 6. Test Results

- tests/test_mcp_guidance_tools_preview.py: 210 passed (was 198, +12)
- python -m pytest: 541 passed (was 529, +12)

## 7. Safety

- No answer / selected_option / prediction top-level output
- No external LLM/API call
- No solver/scaffold/all_cards/cli modification
- No analyze_xingce_question developed
