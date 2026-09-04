# Actual Claude Code MCP Regression After route_uncertain Hardening

## 1. Baseline

- HEAD: 743208d
- commit: harden route-uncertain MCP fallback
- date: 2026-06-16

## 2. Actual client

- Client: Claude Code (CLI)
- Scope: user-level MCP config (C:\Users\22006\.claude.json)
- Server: xingce-solver
- Command: python -m xingce_solver.mcp_server
- PYTHONPATH: E:\project\xingce-solver-migration-final\xingce-solver\src
- Status: ✔ Connected

## 3. Actual visible MCP tools

**Total visible tools in actual Claude Code client: 14** (verified 2026-06-16 after restart)

### Core practical tools: 8

These are the tools developed and verified in the current migration phase:

1. `route_xingce_question` - route-only question router
2. `compose_xingce_analysis_prompt` - prompt-composition-only analysis prompt generator
3. `get_graphic_reasoning_scaffold` - graphic reasoning method scaffold
4. `get_definition_judgement_scaffold` - definition judgement method scaffold
5. `get_analogy_reasoning_scaffold` - analogy reasoning method scaffold
6. `get_logic_analysis_scaffold` - logic analysis method scaffold
7. `get_quantity_relation_scaffold` - quantity relation method scaffold
8. `get_verbal_reasoning_scaffold` - verbal reasoning method scaffold

### Additional legacy/base knowledge tools: 4

These tools exist in the MCP server codebase and are visible to the client, but were not part of the current migration phase's core deliverables:

1. `classify_question` - route question to preliminary modules and method cards
2. `search_methods` - search method cards in knowledge base
3. `get_method_card` - get full method card by method_id
4. `get_source_reference` - get source files, pages, confidence for a method

### Solver candidate tools: 2

These tools are registered in the server and visible to the client:

1. `solve_data_analysis` - data analysis solving draft
2. `solve_logic_reasoning` - logic reasoning solving draft

## 4. route_uncertain regression

### Input

```json
{
  "question_text": "条件不足",
  "options": null,
  "strict_mode": true
}
```

### Actual result

```json
{
  "mode": "route_only",
  "module_guess": "unknown",
  "confidence": "unknown",
  "recommended_track": "route_uncertain",
  "recommended_tool": null,
  "reasoning_signals": ["insufficient_phrase_detected"],
  "fallback_policy": "analysis_only_if_uncertain",
  "answer_policy": "do_not_answer_inside_router",
  "warnings": ["route_uncertain_due_to_insufficient_signal"]
}
```

### Expected result

- module_guess: unknown
- confidence: unknown
- recommended_track: route_uncertain
- recommended_tool: null
- fallback_policy: analysis_only_if_uncertain
- answer_policy: do_not_answer_inside_router
- warnings: contains insufficient/uncertain signal

### Confirmed absent

- No `answer` field
- No `selected_option` field
- No `prediction` field

### Verdict: ✅ PASS

The "条件不足" input correctly routes to `route_uncertain` instead of misrouting to `logic_analysis`. The hardening is effective in the actual Claude Code MCP client after restart.

## 5. Strong logic_analysis regression

### Input

```json
{
  "question_text": "甲乙丙 排序 位置 条件",
  "options": {"A": "选项A", "B": "选项B", "C": "选项C", "D": "选项D"},
  "strict_mode": true
}
```

### Actual result

```json
{
  "mode": "route_only",
  "module_guess": "logic_analysis",
  "confidence": "high",
  "recommended_track": "scaffold_guidance",
  "recommended_tool": "get_logic_analysis_scaffold",
  "reasoning_signals": ["logic_analysis_keywords"],
  "fallback_policy": "analysis_only_if_uncertain",
  "answer_policy": "do_not_answer_inside_router",
  "warnings": []
}
```

### Expected result

- module_guess: logic_analysis
- confidence: high
- recommended_track: scaffold_guidance
- recommended_tool: get_logic_analysis_scaffold

### Confirmed absent

- No `answer` field
- No `selected_option` field
- No `prediction` field

### Verdict: ✅ PASS

Strong logic_analysis signals correctly route to `logic_analysis` with high confidence. The hardening does not break normal routing behavior.

## 6. Inventory interpretation

### Why previous documents stated "8 tools"

Previous documentation referred to "8 MCP tools" because:

1. The current migration phase focused on developing and verifying 8 core practical tools.
2. These 8 tools are the primary deliverables of the migration project.
3. The 4 additional tools (`classify_question`, `search_methods`, `get_method_card`, `get_source_reference`) are legacy/base knowledge tools that already existed in the codebase.

### Why actual client sees 14 tools

The MCP server exposes all registered tools to the client. The 4 additional tools and 2 solver candidate tools are registered in the server and thus visible to Claude Code. They provide supplementary knowledge base and solver functionality but were not the focus of the current migration phase.

### No new tool introduced by hardening

The route_uncertain hardening (commit 743208d) and v0.2 true-question routing hardening (commit 55938e6) did not add any new MCP tool. They only modified routing logic in `mcp_server.py` and added tests.

## 7. Boundary check

Confirmed in this stage:

- ✅ No code modification (only documentation/report updates)
- ✅ No solver modification
- ✅ No scaffold modification
- ✅ No all_cards.jsonl modification
- ✅ No cli.py modification
- ✅ No MCP tool added
- ✅ No CLI integration
- ✅ No real-case package
- ✅ No fabricated questions
- ✅ No OCR/OpenCV/PIL/ML dependency
- ✅ No external LLM/API
- ✅ No network access

## 8. Conclusion

1. **route_uncertain hardening is effective** in the actual Claude Code MCP client after restart.
2. **Actual visible MCP inventory is 14 total tools**, comprising 8 core practical tools, 4 legacy/base knowledge tools, and 2 solver candidate tools.
3. **Previous "12 tools" wording** did not include the 2 solver candidate tools (solve_data_analysis, solve_logic_reasoning).
4. **No code changes** were made in this documentation stage.
5. **Both regression tests passed**: route_uncertain (weak signal) and logic_analysis (strong signal).

---

## 9. True-question Routing Hardening v0.2

**Updated**: 2026-06-16

### New routing capabilities

**Analogy reasoning with ∶ symbol**:
- "卫冕∶夺冠" → analogy_reasoning / high
- "酒器∶尊∶爵" → analogy_reasoning / high

**Quantity relation economic/proportion**:
- "某企业去年全年收入1200万元，支出960万元..." → quantity_relation / high

**Logic analysis arrangement**:
- "张、王、李、杨4人到上海、苏州、杭州和南京调研..." → logic_analysis / high

### Preserved behaviors

- "条件不足" → route_uncertain (preserved)
- "条件" → route_uncertain (not high confidence logic_analysis)
- "甲乙丙 排序 位置 条件" → logic_analysis / high (preserved)

### Safety fields

All route results confirmed:
- No `answer` field
- No `selected_option` field
- No `prediction` field
- No solver call

### Test results

- tests/test_mcp_guidance_tools_preview.py: 110 passed (was 99, +11)
- full pytest: 441 passed (was 430, +11)

### Actual Claude Code MCP regression (2026-06-16)

- Actual visible MCP tools: **14** (not 12)
- solve_data_analysis: visible
- solve_logic_reasoning: visible
- v0.2 did not add new MCP tools
- The 14 tools were the actual Claude Code visible inventory after restart
- All v0.2 routing scenarios verified in actual client
