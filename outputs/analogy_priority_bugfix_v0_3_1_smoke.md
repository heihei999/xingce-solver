# Analogy Priority Bugfix v0.3.1 Smoke Report

## Baseline

- HEAD before fix: bfe6c3a
- v0.3 code commit: 10d0709
- Issue found in actual Claude Code MCP regression (2026-06-16)

## Bug

`感想∶主观性∶体会` was routed to `graphic_reasoning` because option text contained `规律`, which triggered graphic_keywords before analogy structure detection.

**Root cause**: graphic_keywords check (line 269-274) ran before analogy structure detection (line 305-324). The `combined = text + options_text` included "规律" from option A, causing graphic_keywords to match first.

## Fix

Moved analogy structure detection to before graphic_keywords check. Analogy structure detection now has priority over graphic keywords for clear A∶B / A∶B∶C patterns with analogy-structured options.

**Modified file**: `src/xingce_solver/mcp_server.py`
- Moved analogy reasoning check block (lines 305-324) to before graphic reasoning check (line 263)
- No logic changes, only ordering change

## Verified cases

### Analogy routing (should be analogy_reasoning)

| Input | Expected | Actual | Status |
|-------|----------|--------|--------|
| 感想∶主观性∶体会 (options with 规律) | analogy_reasoning | analogy_reasoning | ✅ |
| 卫冕∶夺冠 | analogy_reasoning | analogy_reasoning | ✅ |
| 酒器∶尊∶爵 | analogy_reasoning | analogy_reasoning | ✅ |

### Graphic routing (should be graphic_reasoning)

| Input | Expected | Actual | Status |
|-------|----------|--------|--------|
| 从所给四个选项中，选择最合适的一个，使之呈现一定规律。 | graphic_reasoning | graphic_reasoning | ✅ |
| 黑白块位置变化 | graphic_reasoning | graphic_reasoning | ✅ |
| 图形推理：哪一项与题干图形规律一致？ | graphic_reasoning | graphic_reasoning | ✅ |

### v0.3 fields

All analogy/graphic route results contain:
- possible_modules ✅
- model_review_required ✅
- override_allowed ✅
- review_instruction ✅
- conflict_signals ✅

### Safety

- No answer / selected_option / prediction fields ✅
- route/compose do not call solver ✅
- no automatic answer executor ✅
- no new MCP tool ✅
- no CLI integration ✅

## Tests

- tests/test_mcp_guidance_tools_preview.py -q: 153 passed (was 145, +8)
- python -m pytest -q: 484 passed (was 476, +8)

## Commit

- Message: fix analogy routing priority before graphic keywords
- Files modified:
  - src/xingce_solver/mcp_server.py
  - tests/test_mcp_guidance_tools_preview.py
- Files added:
  - outputs/analogy_priority_bugfix_v0_3_1_smoke.md

## Actual Claude Code MCP Regression After Restart (2026-06-16)

- Claude Code was restarted before testing.
- xingce-solver MCP status: Connected.
- Actual visible tools: 14.
- "感想∶主观性∶体会" → analogy_reasoning / high / get_analogy_reasoning_scaffold. Bug fixed, not misrouted to graphic_reasoning.
- "从所给四个选项中，选择最合适的一个，使之呈现一定规律。" → graphic_reasoning / high / get_graphic_reasoning_scaffold. Not regressed.
- v0.3 fields preserved: possible_modules, model_review_required, override_allowed, review_instruction, conflict_signals.
- No answer / selected_option / prediction in any result.
- No MCP server error.
- No file modified during regression.
- v0.3.1 passed actual Claude Code MCP regression after restart.
