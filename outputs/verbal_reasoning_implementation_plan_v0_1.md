# Verbal Reasoning Implementation Plan v0.1

## 1. Recommended route

**推荐路线：先 verbal_reasoning_scaffold v0.1 isolated，不建议直接做强规则 solver。**

理由：

- 言语理解 77 张卡片覆盖 3 个子模块（主旨意图 32、语句表达 25、逻辑填空 20），但所有题型都依赖深层语义理解。
- A_solver_first 可以为空，没有任何题型适合纯规则 solver 直接覆盖。
- 即使是 B 类的语句排序/填入/标题/下文推断，也需要 scaffold 先约束大模型，后续只能做局部辅助规则（如首句判断、转折捆绑），不能直接自动选答案。
- 逻辑填空和主旨意图是最高频题型，但高度依赖语义和语感，必须走 scaffold + LLM 路线。

## 2. Stage plan

### Stage 1: verbal_reasoning_scaffold v0.1 isolated

**目标**：新增言语理解方法脚手架，仅提供 guidance，不输出答案。

**新增文件建议**：

- `src/xingce_solver/scaffolds/verbal_reasoning_scaffold.py`
- `tests/test_verbal_reasoning_scaffold.py`
- `docs/verbal_reasoning_v0_1_scaffold_design.md`
- `outputs/verbal_reasoning_scaffold_v0_1_smoke.md`
- `outputs/verbal_reasoning_scaffold_v0_1_output_audit.md`

**公开函数建议**：

```python
build_verbal_reasoning_scaffold() -> dict
get_verbal_reasoning_stage_order() -> list[str]
get_verbal_reasoning_question_type_router() -> dict
get_verbal_reasoning_discourse_checklists() -> dict
get_verbal_reasoning_cloze_checklists() -> dict
get_verbal_reasoning_sentence_expression_checklists() -> dict
render_verbal_reasoning_prompt_template() -> str
```

**顶层字段建议**：

- `module`: "verbal_reasoning"
- `version`: "v0.1"
- `mode`: "method_scaffold_only"
- `positioning`: 说明本模块不是 solver，不直接输出答案
- `stage_order`: 思考阶段顺序
- `question_type_router`: 题型路由
- `discourse_structure_checklists`: 文段结构检查清单
- `cloze_context_checklists`: 逻辑填空语境检查清单
- `sentence_expression_checklists`: 语句表达检查清单
- `option_verification`: 选项验证步骤
- `response_template`: 响应模板
- `uncertainty_policy`: 不确定性约束
- `must_not_do`: 禁止事项

**测试建议**：

- 基础结构测试
- 顶层字段完整性
- stage_order 包含关键阶段
- 题型覆盖
- 方法覆盖
- prompt template 格式
- 禁止依赖检查
- 禁止 solver 行为

**禁止事项**：

- 不输出答案
- 不接收题目输入
- 不进行语义判断
- 不调用 solver
- 不接入 CLI/MCP
- 不引入第三方依赖

**验收标准**：

- 所有测试通过
- 输出 audit 通过
- 无 forbidden dependencies
- 无 solver answer fields

### Stage 2: optional sub-scaffold split

**建议不拆子 scaffold。**

理由：

- 言语理解 3 个子模块（主旨意图、语句表达、逻辑填空）共享大量方法（转折、递进、因果、干扰项排除等）。
- 拆分会导致方法清单重复维护。
- 一个统一的 verbal_reasoning_scaffold 通过 question_type_router 区分题型即可。
- 如果后续某个子模块复杂度显著增加，可以再考虑拆分。

### Stage 3: future user-provided real-case audit package

**注意：本阶段不制作真题包。**

本阶段只写未来接入原则，不找题、不造题、不联网、不 OCR、不生成题干、不生成选项、不生成标准答案。

**未来真题包接入原则**：

- 真题来源由用户提供
- 题干、选项、标准答案必须来自已核验资料
- 不能由 Claude / Codex 杜撰
- 不能联网搜索题目
- 不能把标准答案写进 solver/scaffold 规则
- 不能根据 case_id、题号、文件名、答案位置写规则
- 测试包建议放在 `text-image/verbal_reasoning_real_cases_verified_v1/` 这类本地目录
- 测试包默认保持 untracked，不直接提交 git
- 审计脚本只用于计算 correct / wrong / null / analysis_only
- wrong = 0 优先于 correct 数量
- 不唯一必须 analysis_only

### Stage 4: read-only MCP guidance preview integration

**接入条件**：

- verbal_reasoning_scaffold v0.1 已通过全部测试和 output audit
- 独立审批通过

**tool 命名建议**：

- `get_verbal_reasoning_scaffold`（MCP tool）

**read-only contract**：

- 不接收题目/选项/图片
- 只返回 scaffold dict
- 不返回 answer / selected_option / prediction
- 不调用 solver
- 不接 CLI

## 3. Proposed file layout

**本阶段建议文件**：

```text
src/xingce_solver/scaffolds/verbal_reasoning_scaffold.py
tests/test_verbal_reasoning_scaffold.py
docs/verbal_reasoning_v0_1_scaffold_design.md
outputs/verbal_reasoning_scaffold_v0_1_smoke.md
outputs/verbal_reasoning_scaffold_v0_1_output_audit.md
```

**未来真题包文件（本阶段不得创建）**：

```text
text-image/verbal_reasoning_real_cases_verified_v1/
outputs/verbal_reasoning_real_case_audit_v0_1.md
```

## 4. Suggested top-level fields

- module
- version
- mode
- positioning
- stage_order
- question_type_router
- discourse_structure_checklists
- cloze_context_checklists
- sentence_expression_checklists
- option_verification
- response_template
- uncertainty_policy
- must_not_do

## 5. Guardrails

- wrong=0 first
- analysis_only when not unique
- no keyword-only matching
- no default option
- no case_id rule
- no answer leakage
- no solver integration before audit
- no CLI/MCP before isolated tests
- no ML/OCR/external dependency
- no self-made real cases
- no fabricated answer key
- no web-sourced questions by Claude/Codex

## 6. Exit criteria

**Stage 1 → Stage 2 (或直接 Stage 3)**：

- verbal_reasoning_scaffold v0.1 全部测试通过
- scaffold output audit 通过
- 无 forbidden dependencies
- 无 solver answer fields

**Stage 3 → Stage 4**：

- 用户提供真题包（不是 AI 生成）
- 真题包通过 wrong=0 审计
- 人工核验确认无 answer leakage
- 独立审批通过

**Stage 4 → 正式集成**：

- MCP guidance preview 测试通过
- 无 regression
- wrong 保持 0
