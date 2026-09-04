# Actual Claude Code MCP v0.4.1 Regression

## 1. Baseline

- HEAD: 395d2f3
- Commit: harden conservative answer gates
- Previous stable record: cfcefed
- Expected MCP tools: 15
- Source MCP guidance tests: 198 passed
- Source full pytest: 529 passed

## 2. Actual Claude Code MCP client status

- Claude Code was restarted before testing.
- xingce-solver MCP status: Connected.
- Actual visible MCP tools: 15.
- compose_xingce_answer_prompt is visible.
- MCP server error: none.
- Source working tree: only four text-image directories remain untracked.

## 3. v0.4.1 route regression

### Sample 1: person arrangement with 左边

Input:

```text
甲乙丙丁排成一排，甲不在两端，乙在丙左边，问下列哪项可能正确？
```

Options:

```json
{"A": "甲在最左边", "B": "乙在最右边", "C": "丙在甲左边", "D": "丁在最左边"}
```

Actual result:

- module_guess: logic_analysis
- confidence: high
- recommended_tool: get_logic_analysis_scaffold
- reasoning_signals: logic_arrangement_signals
- not graphic_reasoning
- expected behavior: **passed**

### Sample 2: graphic left/right wording

Input:

```text
左边给定的是纸盒的展开图，右边哪一项可以由它折叠而成？
```

Options:

```json
{"A": "图形A", "B": "图形B", "C": "图形C", "D": "图形D"}
```

Actual result:

- module_guess: graphic_reasoning
- confidence: high
- recommended_tool: get_graphic_reasoning_scaffold
- reasoning_signals: graphic_strong_keywords
- expected behavior: **passed**

## 4. v0.4.1 answer gate regression

### Sample 3: graphic reasoning without image

Input:

```text
从所给四个选项中，选择最合适的一个，使之呈现一定规律。
```

Arguments:

- image_present: false
- visual_description: empty

Actual result:

- route.module_guess: graphic_reasoning
- answer_allowed: false
- answer_block_reason: missing_visual_content
- context_requirements.requires_visual: true
- context_requirements.image_present: false
- context_requirements.visual_description_present: false
- answer_prompt includes Answer Gate
- answer_prompt requires mode = analysis_only
- answer_prompt requires answer = null
- No top-level answer / selected_option / prediction
- expected behavior: **passed**

### Sample 4: graphic reasoning with image flag

Arguments:

- image_present: true

Actual result:

- route.module_guess: graphic_reasoning
- answer_allowed: true
- answer_block_reason: null
- context_requirements.requires_visual: true
- context_requirements.image_present: true
- answer_prompt still contains "Do not invent visual features"
- No top-level answer / selected_option / prediction
- expected behavior: **passed**

### Sample 5: data analysis without material

Input:

```text
2022年中部六省中型灌区新增节水能力占全国中型灌区的比重约为多少？
```

Arguments:

- material_present: false
- table_present: false
- material_text: empty

Actual result:

- route.module_guess: data_analysis
- answer_allowed: false
- answer_block_reason: missing_table_or_material
- context_requirements.requires_table_or_material: true
- answer_prompt includes Answer Gate
- answer_prompt requires mode = analysis_only
- answer_prompt requires answer = null
- No top-level answer / selected_option / prediction
- expected behavior: **passed**

### Sample 6: data analysis with material flag

Arguments:

- material_present: true

Actual result:

- route.module_guess: data_analysis
- answer_allowed: true
- answer_block_reason: null
- context_requirements.requires_table_or_material: true
- context_requirements.material_present: true
- No top-level answer / selected_option / prediction
- expected behavior: **passed**

### Sample 7: route_uncertain

Input:

```text
条件不足
```

Arguments:

- options: empty
- strict_mode: true
- allow_answer: true

Actual result:

- route.module_guess: unknown
- route.recommended_track: route_uncertain
- route.reasoning_signals: insufficient_phrase_detected
- answer_allowed: false
- answer_block_reason: route_uncertain_without_semantic_override
- No top-level answer / selected_option / prediction
- expected behavior: **passed**

### Sample 8: allow_answer=false

Input:

```text
感想∶主观性∶体会
```

Options:

```json
{"A": "示范性∶形象∶展示", "B": "规律∶客观性∶发现", "C": "标准∶统一性∶判断", "D": "情绪∶波动性∶表达"}
```

Arguments:

- allow_answer: false

Actual result:

- route.module_guess: analogy_reasoning
- route.confidence: high
- route.recommended_tool: get_analogy_reasoning_scaffold
- answer_allowed: false
- answer_block_reason: answer_mode_disabled
- answer_prompt requires mode = analysis_only regardless of confidence
- No top-level answer / selected_option / prediction
- expected behavior: **passed**

## 5. Safety check

All actual client calls returned no top-level:

- answer
- selected_option
- prediction

Note:

The words `answer` and `prediction` may appear inside `answer_prompt` or `output_schema`, but the MCP tool itself does not return a final selected option.

## 6. Boundary check

Confirmed:

- No external LLM/API call
- No API key configuration
- No analyze_xingce_question
- No solver modification
- No scaffold modification
- No knowledge base modification
- No CLI integration
- No new MCP tool
- No OCR/ML dependency

## 7. Conclusion

v0.4.1 passed actual Claude Code MCP client regression.

The route hardening and conservative answer gates work as intended:

- person arrangement with 左边/右边 no longer misroutes to graphic_reasoning
- graphic left/right packaging wording still correctly routes to graphic_reasoning
- graphic_reasoning without visual content blocks answer_allowed
- data_analysis without material/table/chart data blocks answer_allowed
- route_uncertain blocks answer_allowed
- allow_answer=false has highest priority
- answer_block_reason and context_requirements are present
- no final answer field is leaked by the MCP tool
