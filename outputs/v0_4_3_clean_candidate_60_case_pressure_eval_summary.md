# v0.4.3 Clean Candidate 60-case Pressure Test Summary

## Test target

- Package: xingce-solver_mcp_final_v0_4_3_bfa00f9_clean_runtime_candidate.zip
- Source HEAD: bfa00f9
- Candidate type: clean runtime candidate
- Tester: ChatGPT sandbox-side direct function test

## Package check

- zip entries: 85
- SHA256: 3FED1DC76E4CFF5098AAAE0577C5BC37D2D1071CC6E5CFD3467EF5DC0F0B1636
- Excluded: .git / backups / text-image / outputs / tests / cache / egg-info / old zip

## 60-case pressure test result

- Total cases: 60
- Exact route matches: 57 / 60
- Safety gate passed: 60 / 60
- Prompt core constraints passed: 60 / 60
- Missing visual/table/material constraints passed: 60 / 60
- Top-level answer leakage: 0 / 60
- Top-level selected_option leakage: 0 / 60
- Top-level prediction leakage: 0 / 60

## Route distribution

- data_analysis: 12
- quantity_relation: 8
- graphic_reasoning: 10
- logic_analysis: 7
- unknown: 5
- definition_judgement: 8
- analogy_reasoning: 4
- verbal_reasoning: 3
- logic_reasoning: 3

## Key fixes verified

### v0.4.3 route coverage fixes

- text-based arrangement/sequencing questions route to logic_analysis
- clear definition judgement questions route to definition_judgement

### v0.4.2 material gate remains stable

- 表中 / 根据表格 / 上述资料 / 图中数据 route to data_analysis
- missing material/table context blocks answer_allowed
- answer_block_reason=missing_table_or_material

### v0.4.1 visual gate remains stable

- graphic reasoning without visual content blocks answer_allowed
- answer_block_reason=missing_visual_content

## Remaining low-priority coverage items

No safety-level bug found.

Remaining low-priority route_uncertain cases:

1. 三辆车依次通过收费站，货车早于客车，小轿车不在最后...
2. 下列句子中，没有语病的一项是：
3. 作者接下来最可能论述的是：

These cases are conservatively blocked:

- answer_allowed=false
- answer_block_reason=route_uncertain_without_semantic_override

## Conclusion

v0.4.3 clean candidate passed the 60-case pressure test.

No safety-level issue was found. Remaining issues are conservative coverage limitations, not unsafe answer release.

Recommended next step:

- tag
- tracked backup
- build final clean / online / offline runtime packages
