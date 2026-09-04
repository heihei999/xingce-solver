# graphic_reasoning v0.1 scaffold output audit

## 1. Audit scope

本次只审计 graphic_reasoning v0.1 method scaffold 的实际输出质量。不开发新功能，不接入 CLI/MCP，不修改 solver。

## 2. Baseline

- HEAD: `66b1d91`
- commit: `add graphic reasoning method scaffold`
- scaffold tests: 23 passed
- full pytest: 238 passed

## 3. Public functions checked

| 函数 | 返回类型 | 说明 |
|------|---------|------|
| `build_graphic_reasoning_scaffold()` | dict | 完整 scaffold 结构 |
| `get_graphic_reasoning_stage_order()` | list[str] | 十层观察顺序 |
| `get_graphic_reasoning_visual_checklists()` | dict | 15 个视觉检查清单 |
| `render_graphic_reasoning_prompt_template()` | str | 多模态大模型作答模板 |

## 4. Top-level scaffold fields

| 字段 | 类型 | 内容 |
|------|------|------|
| module | str | "graphic_reasoning" |
| version | str | "v0.1" |
| mode | str | "method_scaffold_only" |
| positioning | dict | is_solver=False, is_image_recognizer=False, outputs_answer=False |
| stage_order | list | 10 items |
| composition_router | dict | 4 keys |
| visual_checklists | dict | 15 keys |
| response_template | str | 416 chars |
| uncertainty_policy | dict | 6 keys |
| must_not_do | list | 7 items |

**结论**: 顶层字段完整，无 answer/selected_option/prediction 字段。

## 5. Stage order audit

十层顺序完整且正确：

1. 命题形式
2. 组成关系
3. 属性规律
4. 数量规律
5. 位置规律
6. 样式规律
7. 特殊题型
8. 空间类题型
9. 选项验证
10. 不确定性约束

## 6. Composition router audit

| 路由 | 优先路径 | 关键 patterns | 约束 |
|------|---------|---------------|------|
| 组成相同 | 位置规律 | 平移、旋转、翻转、移动路径 | 不要一上来数点线面 |
| 组成相似 | 样式规律 | 遍历、加减同异、黑白运算 | 不要一上来数数量 |
| 组成不同 | 属性和数量 | 点、线、面、角、素 | 再系统检查属性和数量 |
| 特殊图形 | 专项检查 | 六面体展开图、截面图、三视图、立体拼合 | 优先触发专项检查 |

**结论**: 路由清晰，约束合理。

## 7. Visual checklist coverage audit

| 清单 | 存在 | 关键内容 |
|------|------|---------|
| 命题形式 | ✅ | 一组图/两组图/九宫格/分组分类/空间重构 |
| 属性规律 | ✅ | 对称性/开闭性/曲直性 |
| 数量规律 | ✅ | 点/线/面/角/素/一笔画/部分数 |
| 位置规律 | ✅ | 平移/旋转/翻转 |
| 样式规律 | ✅ | 遍历/加减同异/黑白运算 |
| 图形间关系 | ✅ | 相离/相交/包含/公共边/点/面 |
| 功能元素 | ✅ | 标记点/线/面/角/相对位置/特殊关系 |
| 黑白块 | ✅ | 13 项检查 + 7 步推荐顺序 + 3 条约束 |
| 汉字类 | ✅ | 结构/封闭面/笔画数/部分数 |
| 数字类 | ✅ | 10 个分类表（轴对称/全曲/全直/开放/封闭/面数） |
| 字母类 | ✅ | 11 个分类表 + 字体注意事项 |
| 六面体展开图 | ✅ | 4 类结构 + 7 项检查 + 时针法约束 |
| 截面图 | ✅ | 5 条规则 + 曲面约束 |
| 三视图 | ✅ | 3 个视图 + 3 条规则 + 3 条核心规则 |
| 立体拼合 | ✅ | 10 项检查 + 6 步流程 + 严丝合缝约束 |

### 数字分类表验证

```
轴对称: 0, 3, 6, 8, 9 ✅
全曲: 0, 3, 6, 8, 9 ✅
全直: 1, 4, 7 ✅
曲直混合: 2, 5 ✅
开放: 1, 2, 3, 5, 7 ✅
全封闭: 0, 8 ✅
半封闭: 4, 6, 9 ✅
0个面: 1, 2, 3, 5, 7 ✅
1个面: 0, 4, 6, 9 ✅
2个面: 8 ✅
```

### 字母分类表验证

```
轴对称: A, B, C, D, E, H, I, K, M, O, T, U, V, W, X, Y ✅
中心对称: N, S, Z ✅
全曲: C, O, S, U ✅
全直: A, E, F, H, I, K, L, M, N, T, V, W, X, Y, Z ✅
曲直混合: B, D, G, J, P, Q, R ✅
开放: C, E, F, G, H, I, J, K, L, M, N, S, T, U, V, W, X, Y, Z ✅
全封闭: B, D, O ✅
半封闭: A, P, Q, R ✅
```

## 8. Prompt template audit

模板包含以下章节：

| 章节 | 存在 | 内容 |
|------|------|------|
| 命题形式 | ✅ | 说明是一组图、两组图等 |
| 组成判断 | ✅ | 说明图形组成是相同、相似等 |
| 优先规律 | ✅ | 根据组成判断选择路径 |
| 视觉证据 | ✅ | 逐条列出证据，不得跳过 |
| 候选规律 | ✅ | 最多 1-2 个 |
| 选项验证 | ✅ | 逐一验证 A/B/C/D |
| 唯一性判断 | ✅ | 唯一才输出答案 |
| 不确定性说明 | ✅ | 说明看不清的细节 |
| analysis_only | ✅ | 不唯一时输出 analysis_only |

**结论**: 模板适合作为后续多模态大模型的提示词。

## 9. Uncertainty policy audit

| 条件 | 输出 |
|------|------|
| 规律无法统一解释 | analysis_only ✅ |
| 多个选项都符合 | analysis_only ✅ |
| 小图细节无法确认 | analysis_only ✅ |
| 图形识别不可靠 | analysis_only ✅ |
| 空间折叠无法唯一排除 | analysis_only ✅ |
| 黑白运算表无法唯一确定 | analysis_only ✅ |

**结论**: 6 种 analysis_only 触发条件全部覆盖。

## 10. Boundary audit

| 检查项 | 结果 |
|--------|------|
| 未接入 CLI | ✅ |
| 未接入 MCP | ✅ |
| 未接入 solve_logic_reasoning | ✅ |
| 未修改 data_analysis.py | ✅ |
| 未修改 logic_reasoning.py | ✅ |
| 未修改 all_cards.jsonl | ✅ |
| 未新增 OCR/OpenCV/PIL/ML 依赖 | ✅ |
| 无 answer/selected_option/prediction 顶层字段 | ✅ |

## 11. Findings

```text
Passed:
- scaffold 顶层字段完整
- 十层观察顺序正确
- composition_router 四类路由清晰
- 15 个视觉检查清单全部覆盖
- 数字分类表完整（10 个分类）
- 字母分类表完整（11 个分类）
- 功能元素清单完整（6 类）
- 黑白块检查顺序和约束完整
- 六面体展开图 4 类结构 + 时针法完整
- prompt template 包含全部 8 个章节
- uncertainty_policy 6 种 analysis_only 条件完整
- must_not_do 7 条约束完整
- 无 answer/selected_option/prediction 字段
- 无 forbidden 依赖

Minor concerns:
- 无

Blocking issues:
- none
```

## 12. Recommendation

graphic_reasoning v0.1 method scaffold output is acceptable for future MCP multimodal guidance integration, but it should remain isolated until a separate MCP/CLI integration task is explicitly approved.
