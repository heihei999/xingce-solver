# Project Regression Summary After Graphic Scaffold

## Baseline

- HEAD: `92e8319`
- commit: audit graphic reasoning scaffold output

## Test results

- `pytest tests/test_graphic_reasoning_scaffold.py -q`: 23 passed
- `python -m pytest -q`: 238 passed

## Changed scope

本阶段新增/已提交内容：

- graphic visual checklist supplement
- graphic reasoning scaffold (v0.1)
- scaffold tests (23 tests)
- scaffold design doc
- scaffold output audit

## Protected file check

| 文件 | 状态 |
|------|------|
| `src/xingce_solver/solvers/data_analysis.py` | unchanged |
| `src/xingce_solver/solvers/logic_reasoning.py` | unchanged |
| `knowledge_base/all_cards.jsonl` | unchanged |
| `src/xingce_solver/cli.py` | unchanged |
| `src/xingce_solver/mcp_server.py` | unchanged |

## Dependency check

未新增以下依赖：

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

## Status

Passed.
