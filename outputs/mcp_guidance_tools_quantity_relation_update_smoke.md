# MCP Guidance Tools Quantity Relation Update Smoke Report

## 1. Baseline

- HEAD before change: 173da7b
- tag: stable-quantity-relation-scaffold-173da7b

## 2. Files changed

- `src/xingce_solver/mcp_server.py`
- `tests/test_mcp_guidance_tools_preview.py`
- `docs/mcp_guidance_tools_preview_v0_1_design.md`
- `docs/mcp_guidance_tools_quantity_relation_update_v0_1.md`
- `outputs/mcp_guidance_tools_quantity_relation_update_smoke.md`

## 3. Tool added

- `get_quantity_relation_scaffold`

## 4. Return source

- `build_quantity_relation_scaffold()`

## 5. Contract check

- read-only
- no question input
- no option input
- no image input
- no answer / selected_option / prediction
- no solver call
- no CLI integration

## 6. Test results

- tests/test_mcp_guidance_tools_preview.py -q: 34 passed
- tests/test_quantity_relation_scaffold.py -q: 22 passed
- tests/test_graphic_reasoning_scaffold.py -q: 23 passed
- tests/test_judgement_reasoning_scaffolds.py -q: 48 passed
- python -m pytest -q: 342 passed

## 7. Boundary check

- no all_cards.jsonl modification
- no solver modification
- no scaffold source modification
- no real-case package
- no fabricated questions
- no OCR/OpenCV/PIL/ML dependency
- no external LLM/API
- no network

## 8. Conclusion

MCP guidance tools preview now exposes quantity_relation_scaffold as read-only guidance. It does not perform solving or answer selection.
