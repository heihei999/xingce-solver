# Actual Claude Code MCP v0.4.3 Regression

## Baseline

- HEAD: bfa00f9
- Commit: harden conservative route coverage
- Previous: a8f7cae
- Expected MCP tools: 15
- Source MCP guidance tests: 220 passed
- Source full pytest: 551 passed

## Actual Claude Code MCP client status

- Claude Code was restarted before testing.
- xingce-solver MCP status: Connected.
- Actual visible MCP tools: 15.
- compose_xingce_answer_prompt is visible.
- MCP server error: none.

## Route coverage regression

Passed samples:

| Sample | Expected | Actual | Signal |
|--------|----------|--------|--------|
| 四本书从左到右摆放，语文书不在最左边，数学书在英语书左边，以下哪项可能为真？ | logic_analysis | logic_analysis | text_arrangement_signals |
| A、B、C、D四名选手按顺序出场，A早于C，B不相邻D，问可能的出场顺序是？ | logic_analysis | logic_analysis | text_arrangement_signals |
| 五个节目依次演出，舞蹈在合唱前面，小品不在最后，以下安排可能正确的是？ | logic_analysis | logic_analysis | text_arrangement_signals |
| 所谓机会成本，是指为了得到某种东西而放弃的其他选择中价值最高者。下列体现机会成本的是？ | definition_judgement | definition_judgement | definition_intro_question_pattern |
| 概念界定：信息茧房是指人们只接触自己感兴趣的信息。下列属于信息茧房的是？ | definition_judgement | definition_judgement | definition_keywords |
| 行政许可是指行政机关根据公民、法人或者其他组织的申请，经依法审查，准予其从事特定活动的行为。下列属于行政许可的是？ | definition_judgement | definition_judgement | definition_keywords |

## Non-regression samples

| Sample | Expected | Actual | Signal |
|--------|----------|--------|--------|
| 左边给定的是纸盒的展开图，右边哪一项可以由它折叠而成？ | graphic_reasoning | graphic_reasoning | graphic_strong_keywords |
| 表中2018—2022年工业增加值平均每年增长量约为多少亿元？ | data_analysis | data_analysis | data_material_strong_signal |
| 一个水池甲管注满需8小时，乙管注满需12小时，两管同时开几小时注满？ | quantity_relation | quantity_relation | quantity_keywords |
| 甲乙两车相向而行，甲车每小时60公里，乙车每小时80公里，几小时相遇？ | quantity_relation | quantity_relation | quantity_keywords |

## Answer gate regression

| Sample | Expected | Actual |
|--------|----------|--------|
| graphic_reasoning without visual content | answer_allowed=false / missing_visual_content | false / missing_visual_content |
| data_analysis without material/table | answer_allowed=false / missing_table_or_material | false / missing_table_or_material |
| route_uncertain | answer_allowed=false / route_uncertain_without_semantic_override | false / route_uncertain_without_semantic_override |
| allow_answer=false | answer_allowed=false / answer_mode_disabled | false / answer_mode_disabled |

## Safety check

No top-level output fields:

- answer: 0/14
- selected_option: 0/14
- prediction: 0/14

## Boundary check

Confirmed:

- No external LLM/API call
- No analyze_xingce_question
- No solver/scaffold/all_cards/cli modification
- No answer gate relaxation
