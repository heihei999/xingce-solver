# Project Final Architecture Inventory

## 1. Solver track

| Module | Component | Status | Notes |
|--------|-----------|--------|-------|
| 资料分析 | solve_data_analysis v5 | stable_frozen | frozen, 不建议修改 |
| 判断推理-翻译推理 | solve_logic_reasoning.translation | stable | 16 correct / 0 wrong / 0 null |
| 判断推理-论证推理 | solve_logic_reasoning.argument_reasoning | stable | 18 correct / 0 wrong / 2 null |
| 判断推理-真假推理 | solve_logic_reasoning.truth_reasoning_guarded | guarded | 4 correct / 0 wrong / 8 null |
| 判断推理-分析推理 | solve_logic_reasoning.logic_analysis_guarded | guarded | 2 correct / 0 wrong / 10 null |

## 2. Scaffold track

| Module | Scaffold file | Test file | Status | MCP exposed |
|--------|--------------|-----------|--------|-------------|
| 图形推理 | graphic_reasoning_scaffold.py | test_graphic_reasoning_scaffold.py | complete | yes |
| 定义判断 | definition_judgement_scaffold.py | test_judgement_reasoning_scaffolds.py | complete | yes |
| 类比推理 | analogy_reasoning_scaffold.py | test_judgement_reasoning_scaffolds.py | complete | yes |
| 分析推理 | logic_analysis_scaffold.py | test_judgement_reasoning_scaffolds.py | complete | yes |
| 数量关系 | quantity_relation_scaffold.py | test_quantity_relation_scaffold.py | complete | yes |
| 言语理解 | verbal_reasoning_scaffold.py | test_verbal_reasoning_scaffold.py | complete | yes |

## 3. MCP guidance tools

| Tool name | Source scaffold | Contract | Status |
|-----------|----------------|----------|--------|
| get_graphic_reasoning_scaffold | graphic_reasoning_scaffold | read-only | complete |
| get_definition_judgement_scaffold | definition_judgement_scaffold | read-only | complete |
| get_analogy_reasoning_scaffold | analogy_reasoning_scaffold | read-only | complete |
| get_logic_analysis_scaffold | logic_analysis_scaffold | read-only | complete |
| get_quantity_relation_scaffold | quantity_relation_scaffold | read-only | complete |
| get_verbal_reasoning_scaffold | verbal_reasoning_scaffold | read-only | complete |

## 4. Knowledge modules

| Knowledge module | Card count | Current route |
|-----------------|------------|---------------|
| 数量关系 | 65 | scope audit completed, scaffold_first |
| 判断推理-逻辑判断 | 42 | translation/argument/truth/logic_analysis integrated |
| 判断推理-图形推理 | 39 | scaffold only |
| 资料分析 | 33 | solver v5 stable |
| 言语理解-主旨意图 | 32 | scope audit completed, scaffold_first |
| 言语理解-语句表达 | 25 | scope audit completed, scaffold_first |
| 判断推理-类比推理 | 23 | isolated core completed |
| 言语理解-逻辑填空 | 20 | scope audit completed, scaffold_first |
| 判断推理-定义判断 | 13 | isolated core completed |

## 5. Frozen / protected files

- `src/xingce_solver/solvers/data_analysis.py`
- `src/xingce_solver/solvers/logic_reasoning.py`
- `knowledge_base/all_cards.jsonl`
- `src/xingce_solver/scaffolds/graphic_reasoning_scaffold.py`
- `src/xingce_solver/scaffolds/definition_judgement_scaffold.py`
- `src/xingce_solver/scaffolds/analogy_reasoning_scaffold.py`
- `src/xingce_solver/scaffolds/logic_analysis_scaffold.py`
- `src/xingce_solver/scaffolds/quantity_relation_scaffold.py`
- `src/xingce_solver/scaffolds/verbal_reasoning_scaffold.py`
- `src/xingce_solver/mcp_server.py` (unless MCP update)
- `src/xingce_solver/cli.py` (unless CLI update)

## 6. Test inventory

| Test file | Tests | Status |
|-----------|-------|--------|
| test_mcp_guidance_tools_preview.py | 40 | passed |
| test_verbal_reasoning_scaffold.py | 23 | passed |
| test_quantity_relation_scaffold.py | 22 | passed |
| test_graphic_reasoning_scaffold.py | 23 | passed |
| test_judgement_reasoning_scaffolds.py | 48 | passed |
| test_analogy_reasoning_core.py | 41 | passed |
| other existing tests | 174 | passed |
| **full pytest** | **371** | **passed** |

## 7. Backup / tag inventory

| Tag | Commit | Description |
|-----|--------|-------------|
| stable-graphic-scaffold-0373a17 | 0373a17 | after graphic reasoning scaffold |
| stable-judgement-scaffolds-81355ce | 81355ce | after judgement reasoning scaffolds |
| stable-mcp-guidance-tools-3ba360e | 3ba360e | after MCP guidance tools |
| stable-quantity-relation-scaffold-173da7b | 173da7b | after quantity relation scaffold |
| stable-quantity-relation-mcp-guidance-78a7ee6 | 78a7ee6 | after quantity relation MCP guidance |
| stable-verbal-reasoning-scaffold-1a28f69 | 1a28f69 | after verbal reasoning scaffold |
| stable-verbal-reasoning-mcp-guidance-02cfe35 | 02cfe35 | after verbal reasoning MCP guidance |
