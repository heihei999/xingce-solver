# Actual Claude Code MCP v0.4 Regression

## 1. Baseline

- HEAD: c47b633
- Commit: add conservative answer prompt composer
- Previous stable point: 6bc28ed
- New MCP tool: compose_xingce_answer_prompt
- Expected MCP tool count: 15
- Source MCP guidance tests: 181 passed
- Source full pytest: 512 passed

## 2. Actual Claude Code MCP client status

- xingce-solver MCP status: Connected.
- Actual visible MCP tools: 15.
- New tool visible: compose_xingce_answer_prompt.
- MCP server error: none.

Note:

The actual client loaded v0.4 successfully and exposed 15 MCP tools.

## 3. Tool inventory

The actual visible tools included:

- classify_question
- compose_xingce_analysis_prompt
- compose_xingce_answer_prompt
- get_analogy_reasoning_scaffold
- get_definition_judgement_scaffold
- get_graphic_reasoning_scaffold
- get_logic_analysis_scaffold
- get_quantity_relation_scaffold
- get_verbal_reasoning_scaffold
- get_method_card
- get_source_reference
- route_xingce_question
- search_methods
- solve_data_analysis
- solve_logic_reasoning

Total:

- 15 tools
- 8 core practical tools
- 4 legacy/base knowledge tools
- 2 solver candidate tools
- 1 conservative answer prompt composer

## 4. compose_xingce_answer_prompt actual calls

### Sample 1: analogy reasoning

Input:

```text
感想∶主观性∶体会
```

Options:

```text
A. 示范性∶形象∶展示
B. 规律∶客观性∶发现
C. 标准∶统一性∶判断
D. 情绪∶波动性∶表达
```

Actual result:

* route.module_guess: analogy_reasoning
* confidence: high
* answer_allowed: true
* answer_prompt: present
* output_schema: present
* safety_contract: present
* analysis_only_required_if: present

Prompt constraints confirmed:

* MCP route is advisory
* exactly one option is justified
* analysis_only
* Do not guess
* Do not invent missing visual/table content

### Sample 2: graphic reasoning with missing visual content

Input:

```text
从所给四个选项中，选择最合适的一个，使之呈现一定规律。
```

Actual result:

* route.module_guess: graphic_reasoning
* prompt requires missing visual content -> analysis_only
* prompt requires not inventing visual features
* prompt requires not inventing missing visual/table content

### Sample 3: data analysis with missing material

Input:

```text
2022年中部六省中型灌区新增节水能力占全国中型灌区的比重约为多少？
```

Actual result:

* route.module_guess: data_analysis
* prompt requires missing table/material -> analysis_only
* prompt requires calculations to be reproducible
* analysis_only_required_if includes calculation_not_reproducible

### Sample 4: route_uncertain conservative case

Input:

```text
条件不足
```

Actual result:

* route.module_guess: unknown
* route.recommended_track: route_uncertain
* route.recommended_tool: null
* answer_allowed: false
* analysis_only_required_if includes route_uncertain_without_semantic_override

### Sample 5: allow_answer=false

Input:

```text
感想∶主观性∶体会
```

Actual result:

* answer_allowed: false
* answer_prompt contains Answer Mode Disabled
* prompt requires mode = analysis_only regardless of confidence

## 5. Compatibility regression

route_xingce_question actual regression:

* 感想∶主观性∶体会 -> analogy_reasoning
* 卫冕∶夺冠 without options -> route_uncertain, expected due to no-options short-text hardening
* 卫冕∶夺冠 with options -> analogy_reasoning
* 酒器∶尊∶爵 without options -> route_uncertain, expected due to no-options short-text hardening
* 酒器∶尊∶爵 with options -> analogy_reasoning
* 图形规律题 -> graphic_reasoning
* 条件不足 -> route_uncertain
* 甲乙丙 排序 位置 条件 -> logic_analysis

## 6. Safety check

All compose_xingce_answer_prompt calls and route_xingce_question calls returned no:

* answer
* selected_option
* prediction

Important boundary:

compose_xingce_answer_prompt only creates a strict answer prompt. It does not return the final answer.

## 7. Boundary check

Confirmed:

* No external LLM/API call
* No API key configuration
* No analyze_xingce_question
* No solver modification
* No scaffold modification
* No knowledge base modification
* No CLI integration
* No new business solver
* No OCR/ML dependency

## 8. Conclusion

v0.4 conservative answer prompt mode passed actual Claude Code MCP client regression.

The new compose_xingce_answer_prompt tool is visible and works as intended. It enables LLM-in-the-loop conservative answer prompting while preserving the safety boundary: the MCP tool itself does not output answer, selected_option, or prediction.
