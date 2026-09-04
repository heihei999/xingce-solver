# MCP Client Smoke After Runtime Usage Docs

## 1. Baseline

- HEAD: 0a9b541
- tag: stable-mcp-runtime-usage-docs-0a9b541

## 2. Environment

- PYTHONPATH: E:\project\xingce-solver-migration-final\xingce-solver\src
- xingce_solver import: E:\project\xingce-solver-migration-final\xingce-solver\src\xingce_solver\__init__.py
- xingce_solver.mcp_server import: mcp_server import ok
- xingce_solver.cli import: cli import ok

## 3. MCP server startup

- startup command: `python -m xingce_solver.mcp_server`
- process stayed alive after 2 seconds: True
- process was stopped cleanly: True
- interpretation: MCP server starts successfully and waits for stdio input (expected behavior for stdio transport)

## 4. Tool inventory

**Actual Claude Code client inventory (verified after restart):**

- Total visible MCP tools: 12
- Core practical tools: 8
- Additional legacy/base knowledge tools: 4

### Core practical tools: 8

- route_xingce_question
- compose_xingce_analysis_prompt
- get_graphic_reasoning_scaffold
- get_definition_judgement_scaffold
- get_analogy_reasoning_scaffold
- get_logic_analysis_scaffold
- get_quantity_relation_scaffold
- get_verbal_reasoning_scaffold

### Additional legacy/base knowledge tools: 4

- classify_question
- search_methods
- get_method_card
- get_source_reference

## 5. Guarded client workflow

Intended client workflow:

1. User sends question text/options/context to LLM.
2. LLM calls route_xingce_question.
3. LLM calls compose_xingce_analysis_prompt.
4. LLM optionally calls recommended get_*_scaffold.
5. LLM performs option-by-option analysis.
6. If not unique, output analysis_only.

## 6. Fallback behavior smoke

### route_uncertain

Confirmed:

- route_uncertain exists in mcp_server.py (lines 291, 295)
- fallback_policy = analysis_only_if_uncertain
- no answer / selected_option / prediction in return dict

### route_uncertain hardening (added in v0.1 hardening)

When strict_mode=True, insufficient signals now properly route to route_uncertain:
- "条件不足" + options=None → route_uncertain (was incorrectly routing to logic_analysis)
- "信息不足" → route_uncertain
- empty text → route_uncertain
- too short text (< 4 chars) → route_uncertain
- no options + short text → route_uncertain

logic_analysis now requires stronger structural signals:
- Strong keywords: 甲乙丙, 排序, 位置, 真假, 命题, 如果那么, 只有才, 除非否则
- OR at least 3 structure keywords with "条件" present

### scaffold_guidance

Confirmed:

- recommended scaffold tools exist (6 tools)
- compose prompt requires option verification (line 393: "逐项核验选项 A/B/C/D")
- compose prompt requires analysis_only if uncertain (line 394: "若不唯一或信息不足，输出 analysis_only")

### solver_candidate

Confirmed:

- solver_candidate route exists (line 285)
- compose prompt states solver is not called (line 398: "本 compose tool 不调用 solver")
- no direct answer is returned (line 402: "不能把 solver_candidate 等同于直接答案")

## 7. Test results

- tests/test_mcp_guidance_tools_preview.py -q: 99 passed (was 77, added 22 new tests for route_uncertain hardening)
- python -m pytest -q: 430 passed (was 408, added 22 new tests)

## 8. Boundary check

Confirmed:

- no mcp_server.py modification
- no cli.py modification
- no all_cards.jsonl modification
- no solver modification
- no scaffold source modification
- no MCP tool added
- no CLI integration
- no real-case package
- no fabricated questions
- no OCR/OpenCV/PIL/ML dependency
- no external LLM/API
- no network

## 9. Conclusion

The current project is ready for manual MCP client configuration testing with 8 tools. The fallback layer is policy/prompt-level, not an automatic executor.
