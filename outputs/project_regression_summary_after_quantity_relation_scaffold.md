# Project Regression Summary After Quantity Relation Scaffold

## Baseline

- HEAD: `ae4902b`
- commit: `add quantity relation method scaffold`

## Test results

- `python -m pytest tests/test_quantity_relation_scaffold.py -q`: 22 passed
- `python -m pytest tests/test_mcp_guidance_tools_preview.py -q`: 28 passed
- `python -m pytest tests/test_graphic_reasoning_scaffold.py -q`: 23 passed
- `python -m pytest tests/test_judgement_reasoning_scaffolds.py -q`: 48 passed
- `python -m pytest -q`: 336 passed

## Changed scope

本阶段新增/已提交内容：

- quantity_relation_scaffold
- quantity scaffold tests
- quantity scaffold design doc
- quantity scaffold smoke report
- quantity scaffold output audit

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
- `knowledge_base/all_cards.jsonl`

## Boundary check

- no solver added
- no MCP/CLI integration
- no real-case package created
- no fabricated questions
- no OCR/OpenCV/PIL/ML dependency
- no external LLM/API
- no network

## Status

Passed.
