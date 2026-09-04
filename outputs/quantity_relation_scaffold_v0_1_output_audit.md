# Quantity Relation Scaffold v0.1 Output Audit

## 1. Audit scope

本次只审计 quantity_relation_scaffold v0.1 输出，不开发 solver，不接 MCP/CLI，不修改知识库，不制作真题包。

## 2. Baseline

- HEAD: 4342951
- commit: audit quantity relation scope
- current untracked scaffold files: 4 (scaffold, tests, design doc, smoke report)
- test baseline: 22 + 28 + 23 + 48 = 121 scaffold tests, 336 full suite passed

## 3. Public functions checked

- `build_quantity_relation_scaffold()` → dict, 12 top-level keys
- `get_quantity_relation_stage_order()` → list[str], 11 stages
- `get_quantity_relation_problem_type_checklists()` → dict (router + checklists)
- `get_quantity_relation_method_checklists()` → dict, 12 methods
- `render_quantity_relation_prompt_template()` → str, 11 sections

## 4. Top-level field audit

All 12 required fields present: module, version, mode, positioning, stage_order, problem_type_router, problem_type_checklists, method_checklists, option_verification, response_template, uncertainty_policy, must_not_do.

Confirmed NOT present: answer, selected_option, prediction.

## 5. Stage order audit

All 11 stages present in correct order:
题型识别 → 问法识别 → 已知量抽取 → 未知量设定 → 单位统一 → 方法选择 → 模型建立 → 计算/代入验证 → 量级检查 → 唯一性判断 → 不确定性约束

## 6. Problem type checklist audit

24 problem types in router, 11 detailed checklists. All required types present:
工程问题 ✅, 行程问题 ✅, 经济利润问题 ✅, 浓度/溶液混合问题 ✅, 容斥/集合问题 ✅, 排列组合 ✅, 概率问题 ✅, 几何问题 ✅, 鸡兔同笼 ✅, 日期星期问题 ✅, 特征余数 ✅, 牛吃草 ✅, 抽屉原理 ✅ (in router).

Each detailed checklist contains: signals, quantities_to_extract, modeling_steps, verification, analysis_only_when.

## 7. Method checklist audit

12 methods covered: 代入排除, 特值法, 方程法, 赋值法, 枚举法, 十字交叉法, 比例法, 图表辅助, 公式法, 构造极端, 估算量级, 分类讨论.

Each method contains: scenarios, steps, verification, risk, analysis_only_when.

## 8. Prompt template audit

Template contains all required sections:
【题型识别】, 【问法目标】, 【已知量】, 【未知量】, 【单位统一】, 【方法选择】, 【模型建立】, 【计算/代入验证】, 【量级检查】, 【唯一性判断】, 【不确定性说明】.

Contains "analysis_only" for uncertainty handling.

## 9. Boundary audit

- no solver added ✅
- no MCP integration ✅
- no CLI integration ✅
- no knowledge base modification ✅
- no real-case package created ✅
- no fabricated questions ✅
- no OCR/OpenCV/PIL/ML dependency ✅
- no external LLM/API ✅
- no answer / selected_option / prediction top-level fields ✅

## 10. Findings

### Passed

- 顶层字段完整，12 个字段全部存在。
- module/version/mode 正确。
- stage_order 11 个阶段按设计顺序覆盖。
- 24 种题型路由覆盖，11 种重点题型有详细 checklist。
- 12 种方法覆盖，每种包含 scenarios/steps/verification/risk/analysis_only_when。
- prompt template 11 个节适合大模型按模板作答。
- uncertainty_policy 8 个触发条件明确 analysis_only。
- must_not_do 10 条禁止事项覆盖硬套公式、忽略单位、默认选第一个、把 scaffold 当 solver、使用 case_id/答案写规则、自造真题。
- 无 answer/selected_option/prediction 顶层字段。
- 无 forbidden dependencies。

### Minor concerns

none

### Blocking issues

none

## 11. Recommendation

quantity_relation_scaffold v0.1 outputs are acceptable as isolated LLM guidance scaffold. It can be committed as an isolated scaffold stage and should remain disconnected from solver, CLI, and MCP until a separate integration task is explicitly approved.
