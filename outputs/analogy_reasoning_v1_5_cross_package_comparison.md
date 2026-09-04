# analogy_reasoning v1.5 Cross-Package Comparison

## Package 1 (v1.4) vs Package 2 (v1.5)

| 指标 | 第一批 (v1.4) | 第二批 (v1.5) |
|------|---------------|---------------|
| Total | 12 | 12 |
| Solved | 2 | 0 |
| Ambiguous | 5 | 4 |
| Analysis_only | 5 | 8 |
| Correct | 2 | 0 |
| Wrong | 0 | 0 |

## 为什么第二批 correct=0

第二批题包以强结构关系为主，但这些关系不在当前 core 的 SAFE_RELATION_TYPES 中：

| 第二批需要的关系 | 当前 core 是否支持 |
|-----------------|-------------------|
| tool_function | ✅ 有检测器，但不在 SAFE_RELATION_TYPES |
| profession_object | ✅ 有检测器，但不在 SAFE_RELATION_TYPES |
| species_genus | ✅ 有检测器，且在 SAFE_RELATION_TYPES |
| cause_effect | ✅ 有检测器，但被列为 WEAK |
| action_compound (教+学=教学) | ❌ 无检测器 |
| necessary_attribute | ❌ 无检测器 |
| state_progression | ❌ 无检测器 |
| attribute_modifier | ❌ 无检测器 |

主要差距：
1. 三词型过多（8/12），当前 core 对三词型非常保守
2. species_genus 虽在 SAFE_RELATION_TYPES，但检测器不够精确
3. tool_function/profession_object 不在 SAFE_RELATION_TYPES

## 结论

当前 v1.4 core 对 material_product / naming_convention 等强结构关系有一定可用性，但对 tool-function-profession、species-genus、necessary-attribute 等关系覆盖不足。

**未达到 integration gate (correct >= 4, wrong = 0)。**

## 下一步建议

1. 将 tool_function, profession_object 加入 SAFE_RELATION_TYPES（需验证不引入 wrong）
2. 改进 species_genus 检测器精度
3. 考虑是否值得继续扩充关系类型 vs 暂停类比推理
