# judgement_reasoning_scaffolds v0.1 output audit

## 1. Audit scope

本次只审计 definition_judgement、analogy_reasoning、logic_analysis 三个 isolated scaffold 的实际输出质量。不开发、不接入、不改 solver。

## 2. Baseline

- HEAD: `0373a17`
- commit: `document project status after graphic scaffold`
- tag: `stable-graphic-scaffold-0373a17`
- tests/test_judgement_reasoning_scaffolds.py: **48 passed**
- tests/test_graphic_reasoning_scaffold.py: **23 passed**
- python -m pytest (full): **286 passed**

## 3. Public functions checked

### definition_judgement

- `build_definition_judgement_scaffold()` → dict, 11 top-level keys
- `get_definition_judgement_stage_order()` → list[str], 8 stages
- `get_definition_judgement_element_checklists()` → dict (elements, rules, option_verification)
- `render_definition_judgement_prompt_template()` → str, 7 sections

### analogy_reasoning

- `build_analogy_reasoning_scaffold()` → dict, 12 top-level keys
- `get_analogy_reasoning_stage_order()` → list[str], 8 stages
- `get_analogy_reasoning_relation_checklists()` → dict (relation_types, verification_steps, verification_rules, comparison_steps)
- `render_analogy_reasoning_prompt_template()` → str, 8 sections

### logic_analysis

- `build_logic_analysis_scaffold()` → dict, 12 top-level keys
- `get_logic_analysis_stage_order()` → list[str], 9 stages
- `get_logic_analysis_structure_checklists()` → dict (problem_types, frameworks, structure_templates, constraints)
- `render_logic_analysis_prompt_template()` → str, 9 sections

## 4. Definition judgement scaffold audit

### Top-level fields ✅

All 11 required fields present: module, version, mode, positioning, stage_order, question_polarity, definition_elements, option_verification, response_template, uncertainty_policy, must_not_do.

### Stage order ✅

```
问法识别 → 定义句定位 → 定义要素抽取 → 必要条件区分 → 选项逐项匹配 → 选是/选非校验 → 唯一性判断 → 不确定性约束
```

All 8 stages present in correct order.

### Question polarity ✅

- positive_forms: 符合定义、属于、正确、选是
- negative_forms: 不符合定义、不属于、错误、选非
- rule: "先识别问法正负极性。选非题必须反向验证，不能按符合定义直接选择。"

### Definition elements ✅

14 elements: 主体、客体、条件、方式、目的、结果、原因、时间、地点、对象范围、排除项、例外项、必要条件、附加描述.

Rules:
- 必要条件缺失时优先排除
- 附加描述不能当成必要条件
- 词面不一致不等于语义不一致
- 语义等价时不得因关键词不重合直接排除

### Option verification ✅

5 steps covering: 逐选项列出、先找核心必要条件、再看附加条件、再处理选是/选非、若多个选项都满足或都不满足则 analysis_only.

### Response template ✅

7 sections: 【问法极性】【定义要素】【必要条件】【选项核验】【排除理由】【唯一性判断】【不确定性说明】

### Uncertainty policy ✅

6 triggers, all ending with `→ analysis_only`.

### Must not do ✅

7 items including: 不得只按关键词重合判断、不得忽略选是/选非、不得把附加描述当必要条件、不得在多个选项都可解释时强行选、不得默认选择第一个选项、不得用题号/case_id/标准答案写规则.

## 5. Analogy reasoning scaffold audit

### Top-level fields ✅

All 12 required fields present.

### Stage order ✅

```
题干形式识别 → 词性与结构检查 → 题干关系造句 → 关系类型识别 → 选项关系套入 → 横纵比较 → 最优关系判断 → 不确定性约束
```

All 8 stages present in correct order.

### Question forms ✅

5 forms: 二词型、三词型、填空型、括号型、对应型.

### Relation types ✅

23 types covering: 近义、反义、种属、组成、整体-部分、功能、属性、因果、条件、目的、工具-用途、职业-工具、地点-行为、主体-动作、动作-对象、原材料-成品、作品-作者、象征、并列、顺承、程度、必然、或然.

### Relation verification ✅

7 steps: 造句、套入选项、方向一致、词性一致、层级一致、强弱一致、必然/或然.

Rules: "能说通不等于最优" and "类比题要找与题干关系最一致的选项".

### Option comparison ✅

6 steps: 词性 → 方向 → 类型 → 强弱 → 层级 → analysis_only if multiple成立.

### Response template ✅

8 sections: 【题干形式】【词性结构】【题干造句】【关系类型】【选项套入】【横纵比较】【唯一性判断】【不确定性说明】

### Uncertainty policy ✅

6 triggers, all ending with `→ analysis_only`.

### Must not do ✅

8 items including: 不得只凭"有关"就判断、不得忽略关系方向、不得忽略词性一致性、不得在多个选项都能说通时强行选、不得用题号/case_id/标准答案写规则.

## 6. Logic analysis scaffold audit

### Top-level fields ✅

All 12 required fields present.

### Stage order ✅

```
题型识别 → 对象集合抽取 → 属性集合抽取 → 约束条件抽取 → 结构框架建立 → 条件传播 → 选项代入验证 → 唯一性判断 → 不确定性约束
```

All 9 stages present in correct order.

### Problem type router ✅

8 types with frameworks:
- 排序题 → 建排序轴
- 分组题 → 建分组框
- 匹配题 → 建对象-属性表
- 位置关系题 → 建位置槽
- 真假话题 → 建真假约束
- 半真半假题 → 拆分每句话的前半/后半
- 条件组合题 → 建条件列表并逐步传播
- 最大最小题 → 建边界条件和极值约束

### Structure templates ✅

8 templates: 对象-属性表、排序轴、分组框、位置槽、真假矩阵、半真半假拆句表、条件传播表、选项代入表.

### Constraint extraction ✅

20 constraints: 确定条件、否定条件、至少、至多、恰好、相邻、不相邻、在……之前、在……之后、同组、不同组、对应、不对应、包含、排除、如果……那么……、只有……才……、除非……否则……、半真半假、一真一假.

### Option verification ✅

6 steps: 逐项代入、检查确定条件、检查否定条件、检查数量约束、检查排序/位置/分组/匹配关系、analysis_only if multiple成立.

### Response template ✅

9 sections: 【题型识别】【对象集合】【属性集合】【约束条件】【结构化表格/框架】【条件推导】【选项代入】【唯一性判断】【不确定性说明】

### Uncertainty policy ✅

6 triggers, all ending with `→ analysis_only`.

### Must not do ✅

8 items including: 不得凭直觉跳过建表、不得忽略否定条件、不得忽略至少/至多/恰好、不得忽略选项代入验证、不得用题号/case_id/标准答案写规则.

## 7. Prompt template audit

### definition template ✅

Contains: 【问法极性】【定义要素】【必要条件】【选项核验】【排除理由】【唯一性判断】【不确定性说明】and `analysis_only`.

### analogy template ✅

Contains: 【题干形式】【词性结构】【题干造句】【关系类型】【选项套入】【横纵比较】【唯一性判断】【不确定性说明】and `analysis_only`.

### logic_analysis template ✅

Contains: 【题型识别】【对象集合】【属性集合】【约束条件】【结构化表格/框架】【条件推导】【选项代入】【唯一性判断】【不确定性说明】and `analysis_only`.

## 8. Boundary audit

- ✅ 未接入 CLI
- ✅ 未接入 MCP
- ✅ 未接入 solve_logic_reasoning
- ✅ 未修改 data_analysis.py
- ✅ 未修改 logic_reasoning.py
- ✅ 未修改 all_cards.jsonl
- ✅ 未修改 graphic_reasoning_scaffold.py
- ✅ 未新增 OCR/OpenCV/PIL/ML 依赖
- ✅ 未出现 answer / selected_option / prediction 顶层字段

## 9. Findings

### Passed

- 三个 scaffold 顶层字段完整，符合设计要求。
- stage_order 顺序正确，覆盖所有关键阶段。
- definition_judgement 覆盖问法极性、定义要素、必要条件/附加描述区分、选是/选非。
- analogy_reasoning 覆盖题干形式、词性结构、造句、23 种关系类型、横纵比较。
- logic_analysis 覆盖 8 种题型路由、8 种结构模板、20 种约束条件。
- 三个 prompt template 结构清晰，可直接用于大模型作答。
- 三个 uncertainty_policy 明确 analysis_only 触发条件。
- 三个 must_not_do 明确禁止强猜、跳过验证、题包特判。
- 所有 286 个测试通过。

### Minor concerns

none

### Blocking issues

none

## 10. Recommendation

judgement_reasoning_scaffolds v0.1 outputs are acceptable as isolated LLM guidance scaffolds for future MCP preview integration. They should remain isolated until a separate MCP/CLI integration task is explicitly approved.
