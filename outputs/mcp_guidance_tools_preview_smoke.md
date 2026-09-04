# MCP Guidance Tools Preview Smoke Report

## 1. Baseline

- HEAD before change: 81355ce
- tag: stable-judgement-scaffolds-81355ce

## 2. Changed files

- `src/xingce_solver/mcp_server.py` (modified)
- `tests/test_mcp_guidance_tools_preview.py` (new)
- `docs/mcp_guidance_tools_preview_v0_1_design.md` (new)
- `outputs/mcp_guidance_tools_preview_smoke.md` (new)

## 3. Tools added

- `get_graphic_reasoning_scaffold`
- `get_definition_judgement_scaffold`
- `get_analogy_reasoning_scaffold`
- `get_logic_analysis_scaffold`
- `get_quantity_relation_scaffold`
- `get_verbal_reasoning_scaffold`
- `route_xingce_question` (route-only, not a scaffold tool)

## 4. Tool contract

- read-only
- no question input
- no option input
- no image input
- return scaffold dict only
- no answer / selected_option / prediction
- no solver call

## 5. Test results

- `python -m pytest tests/test_mcp_guidance_tools_preview.py -q`: 59 passed
- `python -m pytest tests/test_verbal_reasoning_scaffold.py -q`: 23 passed
- `python -m pytest tests/test_quantity_relation_scaffold.py -q`: 22 passed
- `python -m pytest tests/test_graphic_reasoning_scaffold.py -q`: 23 passed
- `python -m pytest tests/test_judgement_reasoning_scaffolds.py -q`: 48 passed
- `python -m pytest -q`: 390 passed

## 6. Boundary check

- 未修改 all_cards.jsonl
- 未修改 data_analysis.py
- 未修改 logic_reasoning.py
- 未修改 4 个 scaffold 源码
- 未接 CLI
- 未新增 OCR/OpenCV/PIL/ML 依赖
- 未调用外部 LLM/API
- 未联网

## 7. Conclusion

MCP guidance tools preview integration is implemented as read-only scaffold access. It does not perform solving or answer selection.
