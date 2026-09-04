# Conservative Answer Gate Hardening v0.4.1 Smoke Report

## 1. Baseline

- HEAD: cfcefed (before)
- Commit: document actual v0.4 MCP regression
- Version: v0.4 → v0.4.1

## 2. Fixes Applied

### Fix 1: Person arrangement routing priority

Problem: "甲乙丙丁排成一排，甲不在两端，乙在丙左边" was routing to graphic_reasoning because "左边/右边" triggered graphic_keywords.

Solution: Added person arrangement signal detection before weak graphic keywords.

- Person signals: 甲, 乙, 丙, 丁, 小王, 小李, 小张, 小赵, 张, 王, 李, 杨
- Position signals: 排成一排, 排列, 座位, 坐在, 站在, 相邻, 不相邻, 两端, 中间, 位置, 顺序
- Condition signals: 条件, 可能正确, 一定正确, 不可能, 至少, 至多, 左边, 右边, 前面, 后面

Logic: person + position OR person + condition → logic_analysis (before weak graphic check)

Strong graphic signals (图形, 展开图, 折叠, 纸盒, etc.) still take priority.

### Fix 2: Answer gate for missing context

Added context parameters to compose_xingce_answer_prompt:
- visual_description: str | None
- material_present: bool
- material_text: str | None
- table_present: bool

Gate logic:
- graphic_reasoning without image/visual_description → answer_allowed=false, reason=missing_visual_content
- data_analysis without material/table/material_text → answer_allowed=false, reason=missing_table_or_material
- route_uncertain → answer_allowed=false, reason=route_uncertain_without_semantic_override
- allow_answer=false → answer_allowed=false, reason=answer_mode_disabled

### Fix 3: New return fields

- answer_block_reason: str | None
- context_requirements: dict

## 3. Verification Results

### Routing fix

| Sample | Expected | Actual |
|--------|----------|--------|
| 甲乙丙丁排成一排，乙在丙左边 | logic_analysis | logic_analysis ✅ |
| 左边给定的是纸盒的展开图 | graphic_reasoning | graphic_reasoning ✅ |
| 从所给四个选项中，选择最合适的一个，使之呈现一定规律 | graphic_reasoning | graphic_reasoning ✅ |

### Answer gate

| Sample | answer_allowed | answer_block_reason |
|--------|----------------|---------------------|
| graphic_reasoning, image_present=false | false | missing_visual_content ✅ |
| graphic_reasoning, image_present=true | true | null ✅ |
| graphic_reasoning, visual_description="详细描述..." | true | null ✅ |
| data_analysis, material_present=false | false | missing_table_or_material ✅ |
| data_analysis, material_present=true | true | null ✅ |
| data_analysis, table_present=true | true | null ✅ |
| data_analysis, material_text="详细材料..." | true | null ✅ |
| route_uncertain | false | route_uncertain_without_semantic_override ✅ |
| allow_answer=false | false | answer_mode_disabled ✅ |

### New fields

| Field | Present | Type |
|-------|---------|------|
| answer_block_reason | ✅ | str | None |
| context_requirements | ✅ | dict |
| context_requirements.requires_visual | ✅ | bool |
| context_requirements.requires_table_or_material | ✅ | bool |
| context_requirements.image_present | ✅ | bool |
| context_requirements.visual_description_present | ✅ | bool |
| context_requirements.material_present | ✅ | bool |
| context_requirements.table_present | ✅ | bool |
| context_requirements.material_text_present | ✅ | bool |

## 4. Test Results

- MCP guidance tests: 198 passed (was 181, +17)
- Full pytest: 529 passed (was 512, +17)

## 5. Safety

- No answer / selected_option / prediction in tool return
- No external LLM/API call
- No solver/scaffold/all_cards/cli modification
- No analyze_xingce_question developed

## 6. Note

MCP server needs restart to load v0.4.1 code. Python direct verification passed all tests.
