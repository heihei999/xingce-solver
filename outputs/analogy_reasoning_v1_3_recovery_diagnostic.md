# analogy_reasoning v1.3 Recovery Diagnostic

## v1.0 → v1.1 回溯

### v1.0 correct cases (2)
| case_id | stem_relation | predicted | expected |
|---------|---------------|-----------|----------|
| analog_001 | material_product, naming_convention | A | A ✅ |
| analog_003 | material_product | A | A ✅ |

共同特征：stem 只有一个主关系 `material_product`，置信度高，选项中只有一个匹配。

### v1.0 wrong cases (2)
| case_id | stem_relation | predicted | expected | 失败原因 |
|---------|---------------|-----------|----------|---------|
| analog_006 | sequence | C | D | sequence 对三词型太弱，误匹配 |
| analog_011 | sequence, purpose, degree | B | A | 混合关系，purpose 对四字成语不可靠 |

共同特征：关系类型弱（sequence）或混合（sequence+purpose+degree），无法安全区分选项。

### v1.1 为什么全部收回
v1.1 增加了两个过滤器：
1. `has_mixed_relations`: stem 有多个 relation_type → 不预测
2. `has_only_weak`: stem 只有 sequence/degree/grammar_structure → 不预测

这两个过滤器把 analog_001 和 analog_003 的正确预测也挡住了（因为它们和 weak 关系一起出现在某些 pair 中）。

## 安全恢复策略

只恢复满足以下全部条件的预测：
1. stem 的主关系只有 `material_product` 或 `naming_convention`（非 weak）
2. 只有一个选项匹配该关系
3. 匹配分数明显高于第二名
4. 不涉及 three-word stem（三词型风险高）
5. 不涉及 fill-in-blank（填空型风险高）

## 预期恢复

- analog_001: 可安全恢复（material_product + naming_convention，二词型）
- analog_003: 可安全恢复（material_product，二词型）
- 其余 10 题：保持 ambiguous / analysis_only

预期 v1.3: correct=2, wrong=0
