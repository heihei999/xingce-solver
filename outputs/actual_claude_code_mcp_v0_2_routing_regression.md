# Actual Claude Code MCP v0.2 Routing Regression

## 1. Baseline

- Baseline before v0.2: fed079f
- HEAD after v0.2 hardening: 55938e6
- Commit: harden true-question MCP routing
- Previous final closure tag: stable-final-claude-code-mcp-closure-fed079f

## 2. Actual client

- Client: Claude Code
- MCP server: xingce-solver
- Status: Connected
- Claude Code was restarted before testing.

## 3. Actual MCP tool inventory

Actual visible MCP tools: **14**

### Core practical tools: 8

- route_xingce_question
- compose_xingce_analysis_prompt
- get_graphic_reasoning_scaffold
- get_definition_judgement_scaffold
- get_analogy_reasoning_scaffold
- get_logic_analysis_scaffold
- get_quantity_relation_scaffold
- get_verbal_reasoning_scaffold

### Legacy/base knowledge tools: 4

- classify_question
- search_methods
- get_method_card
- get_source_reference

### Solver candidate tools: 2

- solve_data_analysis
- solve_logic_reasoning

## 4. v0.2 routing regression results

### Analogy reasoning with ∶

- "卫冕∶夺冠" → analogy_reasoning / high / get_analogy_reasoning_scaffold
- "酒器∶尊∶爵" → analogy_reasoning / high / get_analogy_reasoning_scaffold

### Quantity relation economic/proportion

- income/expense/economic proportion sample → quantity_relation / high / get_quantity_relation_scaffold

### Logic analysis arrangement

- person-month-city arrangement sample → logic_analysis / high / get_logic_analysis_scaffold

### route_uncertain preservation

- "条件不足" → route_uncertain / insufficient_phrase_detected
- "条件" → route_uncertain / text_too_short

### Strong logic_analysis preservation

- "甲乙丙 排序 位置 条件" → logic_analysis / high / logic_analysis_keywords

## 5. Safety check

All actual calls returned no:

- answer
- selected_option
- prediction

## 6. Boundary

- No code change in this documentation stage.
- No MCP tool added in v0.2 documentation stage.
- No CLI integration.
- No solver modification.
- No scaffold modification.
- No knowledge base modification.
- No OCR/OpenCV/PIL/ML dependency.
- No external LLM/API.

## 7. Conclusion

v0.2 true-question routing hardening is verified in the actual Claude Code MCP client. The final actual client-visible inventory is **14 tools**.
