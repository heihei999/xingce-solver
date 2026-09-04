# Actual Claude Code MCP v0.3.1 Regression

## 1. Baseline

- HEAD before documentation: a938097
- Commit: fix analogy routing priority before graphic keywords
- Previous v0.3 commit: 10d0709
- Previous documentation fix commit: bfe6c3a
- Actual Claude Code visible tools: 14

## 2. Actual client status

- Claude Code was restarted before testing.
- xingce-solver MCP status: Connected.
- MCP server responded normally.
- No MCP server error occurred.

## 3. v0.3.1 bugfix verification

### Bug sample

Input:

```text
感想∶主观性∶体会
```

Options included:

```text
规律∶客观性∶发现
示范性∶形象∶展示
标准∶统一性∶判断
情绪∶波动性∶表达
```

Actual result after restart:

- module_guess: analogy_reasoning
- confidence: high
- recommended_tool: get_analogy_reasoning_scaffold
- reasoning_signals: analogy_structure
- conflict_signals: analogy_symbol_detected

Conclusion:

- The previous graphic_reasoning misroute is fixed.
- The option text containing `规律` no longer steals routing priority from analogy structure.

## 4. Graphic reasoning non-regression

Input:

```text
从所给四个选项中，选择最合适的一个，使之呈现一定规律。
```

Actual result:

- module_guess: graphic_reasoning
- confidence: high
- recommended_tool: get_graphic_reasoning_scaffold
- reasoning_signals: graphic_keywords
- conflict_signals: empty

Conclusion:

- Graphic reasoning did not regress.

## 5. v0.3 model-in-the-loop fields

All route results still include:

- possible_modules
- model_review_required
- override_allowed
- review_instruction
- conflict_signals

## 6. Safety check

All actual route results returned no:

- answer
- selected_option
- prediction

## 7. Boundary check

This actual regression stage made no source code change.

Confirmed:

- No solver modification
- No scaffold modification
- No knowledge base modification
- No CLI integration
- No new MCP tool
- No automatic answer executor
- No analyze_xingce_question
- No external LLM/API/OCR/ML dependency

## 8. Conclusion

v0.3.1 passed actual Claude Code MCP regression after restart.

The analogy priority bug is fixed, graphic reasoning is not regressed, v0.3 model-in-the-loop fields remain available, and safety fields are still absent.
