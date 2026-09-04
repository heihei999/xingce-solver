# v0.5.1 Three-Year Practical Validation Summary

## Validation point

- HEAD: b37bd07
- Commit: harden module context edge cases
- Package: xingce-solver_mcp_final_v0_5_1_b37bd07_clean_runtime_candidate.zip
- SHA256: A180EDB1ABB41CF5F54023436495035CD4276B9EAD960DD5F6F11B1F3CFA9560

## Test status

- Source MCP guidance tests: 261 passed
- Source full pytest: 592 passed
- Actual Claude Code MCP client regression: passed
- MCP tools: 15

## Three-year route/gate practical validation

| Paper | Route with module_hint | Compose route | Answer gate | Leakage |
|-------|------------------------|---------------|-------------|---------|
| 2024 国考行政执法卷 | 110 / 110 | 110 / 110 | 110 / 110 | 0 |
| 2023 国考行政执法卷 | 110 / 110 | 110 / 110 | 110 / 110 | 0 |
| 2022 国考行政执法卷 | 110 / 110 | 110 / 110 | 110 / 110 | 0 |
| **Total** | **330 / 330** | **330 / 330** | **330 / 330** | **0 / 330** |

## Key finding

module_hint / section_context is required for full practical performance. Without module_hint, the system remains conservative and keyword-based routing is intentionally not optimized as a standalone classifier.

## Recommendation

Proceed to v0.5.1 final release packaging (tag + clean/online/offline runtime packages).
