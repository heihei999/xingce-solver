# Project Regression Summary After Quantity Relation MCP Guidance

## Baseline

- HEAD: `6593690`
- commit: `update MCP guidance smoke for quantity relation`

## Test results

- `python -m pytest tests/test_mcp_guidance_tools_preview.py -q`: 34 passed
- `python -m pytest tests/test_quantity_relation_scaffold.py -q`: 22 passed
- `python -m pytest tests/test_graphic_reasoning_scaffold.py -q`: 23 passed
- `python -m pytest tests/test_judgement_reasoning_scaffolds.py -q`: 48 passed
- `python -m pytest -q`: 342 passed

## Changed scope

- get_quantity_relation_scaffold added to MCP guidance preview
- MCP guidance smoke report updated for quantity relation
- MCP guidance preview now contains 5 read-only scaffold tools

## Protected file check

以下文件无 diff：

- `src/xingce_solver/cli.py`
- `src/xingce_solver/solvers/data_analysis.py`
- `src/xingce_solver/solvers/logic_reasoning.py`
- `src/xingce_solver/scaffolds/graphic_reasoning_scaffold.py`
- `src/xingce_solver/scaffolds/definition_judgement_scaffold.py`
- `src/xingce_solver/scaffolds/analogy_reasoning_scaffold.py`
- `src/xingce_solver/scaffolds/logic_analysis_scaffold.py`
- `src/xingce_solver/scaffolds/quantity_relation_scaffold.py`
- `knowledge_base/all_cards.jsonl`

## MCP guidance contract check

- five guidance tools are read-only
- no question/option/image input
- no answer / selected_option / prediction
- no solver call
- no automatic answer selection

## Boundary check

- no CLI integration
- no solver modification
- no scaffold source modification
- no real-case package created
- no fabricated questions
- no OCR/OpenCV/PIL/ML dependency
- no external LLM/API
- no network

## Status

Passed.
