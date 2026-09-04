# Conservative Route Coverage Hardening v0.4.3 Smoke Report

**Date**: 2026-06-16
**Commit**: (pending)
**Previous HEAD**: a8f7cae

## 1. Fix Background

v0.4.2 clean candidate 60-case pressure test revealed two coverage issues:

1. Text-based arrangement/sequencing questions (e.g., "四本书从左到右摆放") were misclassified as `graphic_reasoning` due to "左边" hitting graphic keywords.
2. Clear definition questions (e.g., "所谓机会成本，是指...下列体现") were routed to `route_uncertain` because the definition pattern was not recognized.

These are not safety issues (no incorrect answers were produced), but they block legitimate text-based questions from being processed.

## 2. Text-based Arrangement Coverage Enhancement

### New Detection Logic

Added `_arrangement_object_kw` and `_arrangement_order_kw` keyword lists for text-based arrangement scenarios:

**Object keywords**: 书, 语文书, 数学书, 英语书, 节目, 舞蹈, 合唱, 小品, 选手, 队员, 学生, 老师, 课程, 会议, 车辆, 部门

**Order keywords**: 从左到右, 从右到左, 从高到低, 从低到高, 依次, 顺序, 出场, 演出, 摆放, 排列, 安排, 可能为真, 可能正确, 一定为真, 一定正确, 早于, 晚于, 之前, 之后

**Position keywords**: 左边, 右边, 最左边, 最右边, 前面, 后面, 相邻, 不相邻, 两端, 中间, 位置

**Logic**: object + order + position → `logic_analysis`

### Verified Samples

| Sample | Expected | Actual | Signal |
|--------|----------|--------|--------|
| 四本书从左到右摆放，语文书不在最左边，数学书在英语书左边 | logic_analysis | logic_analysis | text_arrangement_signals |
| A、B、C、D四名选手按顺序出场，A早于C，B不相邻D | logic_analysis | logic_analysis | text_arrangement_signals |
| 五个节目依次演出，舞蹈在合唱前面，小品不在最后 | logic_analysis | logic_analysis | text_arrangement_signals |

## 3. Definition Judgement Coverage Enhancement

### New Detection Logic

Added `_definition_intro_kw` and `_definition_question_kw` keyword lists:

**Definition intro keywords**: 所谓, 是指, 指的是, 定义为, 是指在, 指在, 概念, 定义, 称为

**Definition question keywords**: 下列, 以下, 哪项, 属于, 不属于, 符合, 不符合, 体现, 没有体现, 最符合, 最不符合

**Logic**: definition_intro + definition_question → `definition_judgement`

### Verified Samples

| Sample | Expected | Actual | Signal |
|--------|----------|--------|--------|
| 所谓机会成本，是指...下列体现机会成本的是？ | definition_judgement | definition_judgement | definition_intro_question_pattern |
| 概念界定：信息茧房是指...下列属于信息茧房的是？ | definition_judgement | definition_judgement | definition_keywords |
| 行政许可是指...下列属于行政许可的是？ | definition_judgement | definition_judgement | definition_keywords |

## 4. Graphic "左边给定" No Regression

| Sample | Expected | Actual |
|--------|----------|--------|
| 左边给定的是纸盒的展开图，右边哪一项可以由它折叠而成？ | graphic_reasoning | graphic_reasoning |

## 5. v0.4.2 Data Material Gate No Regression

| Sample | Expected | Actual | Signal |
|--------|----------|--------|--------|
| 表中2018—2022年工业增加值平均每年增长量约为多少亿元？ | data_analysis | data_analysis | data_material_strong_signal |

## 6. Quantity Relation No Regression

| Sample | Expected | Actual |
|--------|----------|--------|
| 一个水池甲管注满需8小时，乙管注满需12小时，两管同时开几小时注满？ | quantity_relation | quantity_relation |

## 7. Test Results

- tests/test_mcp_guidance_tools_preview.py: 220 passed (was 210, +10)
- python -m pytest: 551 passed (was 541, +10)

## 8. Safety Confirmations

- No solver/scaffold/all_cards/cli modification
- No external LLM/API call
- No analyze_xingce_question development
- No answer/selected_option/prediction top-level field leakage
- MCP route remains advisory
- MCP does not output final answer
- Answer gates (missing_visual_content, missing_table_or_material, route_uncertain) unchanged
