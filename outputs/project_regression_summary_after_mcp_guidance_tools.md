# Project Regression Summary After MCP Guidance Tools Preview

## Baseline

- HEAD: `36b40ef`
- commit: `add MCP guidance tools preview`

## Test results

- `python -m pytest tests/test_mcp_guidance_tools_preview.py -q`: 28 passed
- `python -m pytest tests/test_graphic_reasoning_scaffold.py -q`: 23 passed
- `python -m pytest tests/test_judgement_reasoning_scaffolds.py -q`: 48 passed
- `python -m pytest -q`: 314 passed

## Changed scope

本阶段新增/已提交内容：

- MCP read-only guidance tool: `get_graphic_reasoning_scaffold`
- MCP read-only guidance tool: `get_definition_judgement_scaffold`
- MCP read-only guidance tool: `get_analogy_reasoning_scaffold`
- MCP read-only guidance tool: `get_logic_analysis_scaffold`
- MCP guidance preview tests
- MCP guidance preview design doc
- MCP guidance preview smoke report

## Protected file check

以下文件无 diff：

- `src/xingce_solver/solvers/data_analysis.py`
- `src/xingce_solver/solvers/logic_reasoning.py`
- `src/xingce_solver/solvers/definition_judgement.py`
- `src/xingce_solver/solvers/analogy_reasoning.py`
- `src/xingce_solver/solvers/logic_analysis_reasoning.py`
- `src/xingce_solver/scaffolds/graphic_reasoning_scaffold.py`
- `src/xingce_solver/scaffolds/definition_judgement_scaffold.py`
- `src/xingce_solver/scaffolds/analogy_reasoning_scaffold.py`
- `src/xingce_solver/scaffolds/logic_analysis_scaffold.py`
- `knowledge_base/all_cards.jsonl`
- `src/xingce_solver/cli.py`

## MCP guidance contract check

- guidance tools are read-only
- no question input
- no option input
- no image input
- no answer / selected_option / prediction
- no solver call
- no automatic answer selection

## Dependency check

确认未新增：

- OCR
- OpenCV
- PIL/Pillow
- cv2
- pytesseract
- sklearn
- torch
- tensorflow
- statsmodels
- xgboost
- lightgbm
- external LLM/API
- network dependency

## Status

Passed.
