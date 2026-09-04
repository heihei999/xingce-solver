# MCP Runtime Usage Smoke After Prompt Composer

## 1. Baseline

- HEAD: a68ac8a
- tag: stable-compose-analysis-prompt-composer-a68ac8a

## 2. Environment

- Python executable: C:\Users\22006\.hermes\hermes-agent\venv\Scripts\python.exe
- Python version: 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)]
- PYTHONPATH: E:\project\xingce-solver-migration-final\xingce-solver\src
- xingce_solver import: E:\project\xingce-solver-migration-final\xingce-solver\src\xingce_solver\__init__.py
- xingce_solver.cli import: cli import ok

## 3. Tool inventory

8 MCP tools:

- route_xingce_question
- compose_xingce_analysis_prompt
- get_graphic_reasoning_scaffold
- get_definition_judgement_scaffold
- get_analogy_reasoning_scaffold
- get_logic_analysis_scaffold
- get_quantity_relation_scaffold
- get_verbal_reasoning_scaffold

## 4. Runtime contract

Confirmed:

- route-only router exists
- prompt-composition composer exists
- 6 scaffold tools exist
- no direct answer selection in route/compose
- no solver call in route/compose
- no CLI integration

## 5. Test results

```powershell
$env:PYTHONPATH = (Resolve-Path .\src).Path
python -m pytest tests/test_mcp_guidance_tools_preview.py -q
python -m pytest tests/test_verbal_reasoning_scaffold.py -q
python -m pytest tests/test_quantity_relation_scaffold.py -q
python -m pytest tests/test_graphic_reasoning_scaffold.py -q
python -m pytest tests/test_judgement_reasoning_scaffolds.py -q
python -m pytest -q
```

Results:

- tests/test_mcp_guidance_tools_preview.py -q: 77 passed
- tests/test_verbal_reasoning_scaffold.py -q: 23 passed
- tests/test_quantity_relation_scaffold.py -q: 22 passed
- tests/test_graphic_reasoning_scaffold.py -q: 23 passed
- tests/test_judgement_reasoning_scaffolds.py -q: 48 passed
- python -m pytest -q: 408 passed

## 6. Boundary check

Confirmed:

- no all_cards.jsonl modification
- no mcp_server.py modification
- no cli.py modification
- no solver modification
- no scaffold source modification
- no real-case package
- no fabricated questions
- no OCR/OpenCV/PIL/ML dependency
- no external LLM/API
- no network

## 7. Conclusion

The MCP runtime usage layer is documented. The current stable point is ready for client-side MCP configuration testing.
