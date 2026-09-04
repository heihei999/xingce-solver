# Quantity Relation Implementation Plan v0.1

## 1. Recommended route

**推荐路线：先 scaffold，再 isolated small solver，分阶段推进。**

理由：

- 数量关系题型（工程问题、行程问题、排列组合、概率、利润、容斥等）高度依赖数学建模能力，纯规则 solver 难以覆盖。
- 先做 scaffold 可以验证方法论是否完整，为后续 solver 提供结构化约束。
- scaffold 完成后，可以针对首批可规则化题型（如工程问题、利润问题）做 isolated small solver。
- 不建议 scaffold 与 solver 同步开发，避免职责混淆。
- 不建议跳过 scaffold 直接做 solver，避免重复 analogy_reasoning 早期硬堆规则的教训。

## 2. Stage plan

### Stage 1: quantity_relation_scaffold v0.1 isolated

**目标**：新增数量关系方法脚手架，仅提供 guidance，不输出答案。

**新增文件建议**：

- `src/xingce_solver/scaffolds/quantity_relation_scaffold.py`
- `tests/test_quantity_relation_scaffold.py`
- `docs/quantity_relation_v0_1_scaffold_design.md`

**公开函数建议**：

```python
build_quantity_relation_scaffold() -> dict
get_quantity_relation_stage_order() -> list[str]
get_quantity_relation_problem_type_router() -> dict
get_quantity_relation_structure_checklists() -> dict
render_quantity_relation_prompt_template() -> str
```

**顶层字段建议**：

- `module`: "quantity_relation"
- `version`: "v0.1"
- `mode`: "method_scaffold_only"
- `positioning`: 说明本模块不是 solver，不直接枚举答案
- `stage_order`: 思考阶段顺序
- `problem_type_router`: 题型路由（工程、行程、排列组合、利润、容斥等）
- `structure_templates`: 结构模板（方程表、比例轴、树形图、枚举表等）
- `constraint_extraction`: 约束条件抽取清单
- `option_verification`: 选项代入验证步骤
- `response_template`: 响应模板
- `uncertainty_policy`: 不确定性约束
- `must_not_do`: 禁止事项

**测试建议**：

- 基础结构测试（返回 dict、module、version、mode）
- 顶层字段完整性
- stage_order 包含关键阶段
- 关键题型覆盖
- prompt template 格式
- 禁止依赖检查
- 禁止 solver 行为（无 answer / selected_option / prediction 顶层字段）

**禁止事项**：

- 不输出答案
- 不接收题目输入
- 不进行数学计算
- 不调用 solver
- 不接入 CLI/MCP
- 不引入第三方依赖

**验收标准**：

- 所有测试通过
- 输出 audit 通过
- 无 forbidden dependencies
- 无 solver answer fields

### Stage 2: quantity_relation_solver_core v0.1 isolated

**目标**：新增数量关系 isolated solver core，仅支持首批可规则化题型。

**优先支持题型**：

- 工程问题（合作/交替/效率变化）
- 利润问题（成本/售价/折扣/利润率）
- 行程问题（相遇/追及/流水）
- 排列组合基础（分类/分步/捆绑/插空）
- 容斥原理基础（两集合/三集合）

**输入输出结构**：

- 输入：`case: dict`，包含 `question_text`、`options` 等
- 输出：`QuantityRelationResult` dataclass，包含 `solved`、`answer`、`analysis_only`、`method_tag` 等
- `analysis_only` 策略：无法唯一确定时必须输出 analysis_only

**analysis_only 策略**：

- 多个选项同时满足 → analysis_only
- 约束条件不足 → analysis_only
- 需要外部专业知识且无法确认 → analysis_only
- 题型不在首批支持范围 → analysis_only

**禁止接入 CLI/MCP**：

- 仅作为 isolated core 测试
- 不修改 mcp_server.py
- 不修改 cli.py

**测试建议**：

- 基础结构测试
- 首批题型覆盖测试
- guardrail 测试（无 forbidden dependencies、无 answer fields）
- wrong=0 验证（需要真题包，本阶段仅做结构验证）

### Stage 3: future user-provided real-case audit package

**注意：本阶段不制作真题包。**

本阶段只写未来接入原则，不找题、不造题、不联网、不 OCR、不生成题干、不生成选项、不生成标准答案。

**未来真题包接入原则**：

- 真题来源由用户提供
- 题干、选项、标准答案必须来自已核验资料
- 不能由 Claude / Codex 杜撰
- 不能联网搜索题目
- 不能把标准答案写进 solver 规则
- 不能根据 case_id、题号、文件名、答案位置写规则
- 测试包建议放在 `text-image/quantity_relation_real_cases_verified_v1/` 这类本地目录
- 测试包默认保持 untracked，不直接提交 git
- 审计脚本只用于计算 correct / wrong / null / analysis_only
- wrong = 0 优先于 correct 数量
- 不唯一必须 analysis_only

**建议真题包字段格式**：

```json
{
  "case_id": "qr_001",
  "question_text": "...",
  "options": {"A": "...", "B": "...", "C": "...", "D": "..."},
  "answer": "B",
  "source_note": "2024年国考第XX题",
  "method_tag": "工程问题",
  "expected_behavior": "solved",
  "audit_result": "pending"
}
```

**验收口径**：

- case_id: 唯一标识
- question_text: 完整题干
- options: 选项字典
- answer: 标准答案（来自用户核验资料）
- source_note: 真题来源说明
- method_tag: 预期方法标签
- expected_behavior: 预期行为（solved / analysis_only）
- audit_result: 审计结果（correct / wrong / null / analysis_only）

### Stage 4: guarded integration preview

**接入条件**：

- isolated solver core 已通过全部单元测试
- 用户提供真题包已通过 wrong=0 审计
- 人工核验确认无 answer leakage
- 独立审批通过

**tool 命名建议**：

- `solve_quantity_relation`（MCP tool）
- `quantity-relation-solve`（CLI command）

**guardrail 测试**：

- no forbidden dependencies
- no answer fields in scaffold
- no solver call in scaffold
- wrong=0 on audit package
- analysis_only when not unique
- no case_id rule
- no answer leakage

**不允许**：

- 未通过 isolated audit 前接入正式 solver
- 未通过人工核验真题包前扩大覆盖范围
- 未通过审批前接入 CLI/MCP

## 3. Proposed file layout

**本阶段建议文件**：

```text
src/xingce_solver/scaffolds/quantity_relation_scaffold.py
tests/test_quantity_relation_scaffold.py
docs/quantity_relation_v0_1_scaffold_design.md

src/xingce_solver/solvers/quantity_relation.py
tests/test_quantity_relation_solver_core.py
docs/quantity_relation_solver_core_v0_1_design.md

outputs/quantity_relation_solver_core_audit.md
```

**未来真题包文件（本阶段不得创建）**：

```text
text-image/quantity_relation_real_cases_verified_v1/
outputs/quantity_relation_real_case_audit_v0_1.md
```

## 4. First target problem types

首批目标题型（3~5 个）：

1. **工程问题**：合作完成、交替工作、效率变化
2. **利润问题**：成本/售价/折扣/利润率计算
3. **行程问题**：相遇、追及、流水行船
4. **排列组合基础**：分类计数、分步计数、捆绑法、插空法
5. **容斥原理基础**：两集合、三集合容斥

选择理由：

- 这些题型有明确的数学模型和公式
- 可以用规则化方法覆盖核心逻辑
- 是行测数量关系高频题型
- 适合做 isolated solver 验证

## 5. Guardrails

- wrong=0 first（wrong 数量必须为 0，即使 correct 降低）
- no default option（不得默认选择第一个选项）
- no case_id rule（不得根据 case_id / 题号写规则）
- no answer leakage（不得把标准答案写进 solver 规则）
- no solver integration before audit（未通过 isolated audit 前不得接入正式 solver）
- no CLI/MCP before isolated tests（未通过 isolated tests 前不得接入 CLI/MCP）
- no ML/OCR/external dependency（不得引入机器学习、OCR、外部依赖）
- no self-made real cases（不得自行编造真题）
- no fabricated answer key（不得杜撰标准答案）
- no web-sourced questions by Claude/Codex（不得由 AI 联网搜索题目）

## 6. Exit criteria

**进入下一阶段的条件**：

**Stage 1 → Stage 2**：

- quantity_relation_scaffold v0.1 全部测试通过
- scaffold output audit 通过
- 无 forbidden dependencies
- 无 solver answer fields

**Stage 2 → Stage 3**：

- quantity_relation_solver_core v0.1 全部测试通过
- 首批题型结构验证通过
- guardrail 测试通过
- 无 forbidden dependencies

**Stage 3 → Stage 4**：

- 用户提供真题包（不是 AI 生成）
- 真题包通过 wrong=0 审计
- 人工核验确认无 answer leakage
- 独立审批通过

**Stage 4 → 正式集成**：

- guarded integration preview 测试通过
- MCP/CLI 接入审批通过
- 无 regression
- wrong 保持 0
