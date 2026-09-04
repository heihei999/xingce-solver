# Project Final Regression Summary

## Baseline

- HEAD: `02cfe35`
- tag: `stable-verbal-reasoning-mcp-guidance-02cfe35`

## Test results

- `python -m pytest tests/test_mcp_guidance_tools_preview.py -q`: 40 passed
- `python -m pytest tests/test_verbal_reasoning_scaffold.py -q`: 23 passed
- `python -m pytest tests/test_quantity_relation_scaffold.py -q`: 22 passed
- `python -m pytest tests/test_graphic_reasoning_scaffold.py -q`: 23 passed
- `python -m pytest tests/test_judgement_reasoning_scaffolds.py -q`: 48 passed
- `python -m pytest -q`: 371 passed

## Protected file check

以下文件无 diff：

- `src/xingce_solver/mcp_server.py`
- `src/xingce_solver/cli.py`
- `src/xingce_solver/solvers/data_analysis.py`
- `src/xingce_solver/solvers/logic_reasoning.py`
- `src/xingce_solver/scaffolds/graphic_reasoning_scaffold.py`
- `src/xingce_solver/scaffolds/definition_judgement_scaffold.py`
- `src/xingce_solver/scaffolds/analogy_reasoning_scaffold.py`
- `src/xingce_solver/scaffolds/logic_analysis_scaffold.py`
- `src/xingce_solver/scaffolds/quantity_relation_scaffold.py`
- `src/xingce_solver/scaffolds/verbal_reasoning_scaffold.py`
- `knowledge_base/all_cards.jsonl`

## Scope check

- no code modified
- no solver added
- no scaffold added
- no MCP tool added
- no CLI integration
- no real-case package created
- no fabricated questions
- no OCR/ML dependency
- no external LLM/API

## Status

Passed.
