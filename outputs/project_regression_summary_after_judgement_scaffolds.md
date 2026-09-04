# Project Regression Summary After Judgement Scaffolds

## Baseline

- HEAD: `ba6549a`
- commit: `add judgement reasoning method scaffolds`

## Test results

- `python -m pytest tests/test_judgement_reasoning_scaffolds.py -q`: 48 passed
- `python -m pytest tests/test_graphic_reasoning_scaffold.py -q`: 23 passed
- `python -m pytest -q`: 286 passed

## Changed scope

本阶段新增/已提交内容：

- `src/xingce_solver/scaffolds/definition_judgement_scaffold.py`
- `src/xingce_solver/scaffolds/analogy_reasoning_scaffold.py`
- `src/xingce_solver/scaffolds/logic_analysis_scaffold.py`
- `tests/test_judgement_reasoning_scaffolds.py`
- `docs/judgement_reasoning_scaffolds_v0_1_design.md`
- `outputs/judgement_reasoning_scaffolds_output_audit.md`

## Protected file check

以下文件无 diff：

- `src/xingce_solver/solvers/data_analysis.py`
- `src/xingce_solver/solvers/logic_reasoning.py`
- `src/xingce_solver/solvers/definition_judgement.py`
- `src/xingce_solver/solvers/analogy_reasoning.py`
- `src/xingce_solver/solvers/logic_analysis_reasoning.py`
- `knowledge_base/all_cards.jsonl`
- `src/xingce_solver/cli.py`
- `src/xingce_solver/mcp_server.py`
- `src/xingce_solver/scaffolds/graphic_reasoning_scaffold.py`

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
