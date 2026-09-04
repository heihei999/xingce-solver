# Truth Reasoning Core v0.5 — Normalization & First-Order Audit Summary

## Overall

- total: 12
- solved: 4
- ambiguous: 8
- inconsistent: 0
- analysis_only: 0

## Option Mapping Results

- unique_supported: 3
- ambiguous_options: 0
- no_supported_option: 9
- not_attempted: 0

## Option Correctness

- correct: 3
- wrong: 0
- null: 9

## Failure Stage Distribution

- assignment: 8
- none: 4

## Binary Domains

- cases with binary domains: 3

## Per-Case Results

| case_id | expected | status | option_status | predicted | correct | bin_domains |
|---|---|---|---|---|---|---|
| LTRUTH-REAL-001 | A | ambiguous | no_supported_option | - | - | 0 |
| LTRUTH-REAL-002 | A | solved | unique_supported | A | Y | 1 |
| LTRUTH-REAL-003 | D | ambiguous | no_supported_option | - | - | 0 |
| LTRUTH-REAL-004 | D | ambiguous | no_supported_option | - | - | 0 |
| LTRUTH-REAL-005 | C | solved | unique_supported | C | Y | 1 |
| LTRUTH-REAL-006 | C | ambiguous | no_supported_option | - | - | 0 |
| LTRUTH-REAL-007 | A | ambiguous | no_supported_option | - | - | 0 |
| LTRUTH-REAL-008 | C | ambiguous | no_supported_option | - | - | 0 |
| LTRUTH-REAL-009 | A | solved | no_supported_option | - | - | 0 |
| LTRUTH-REAL-010 | B | ambiguous | no_supported_option | - | - | 0 |
| LTRUTH-REAL-011 | B | solved | unique_supported | B | Y | 0 |
| LTRUTH-REAL-012 | C | ambiguous | no_supported_option | - | - | 1 |

## Option Trace Detail

### LTRUTH-REAL-001 (status=ambiguous, option_status=no_supported_option)
- A: unknown [?, ?, F, ?] 甲说的不对，小赵没有写完作业
- B: unknown [?, F, ?, ?] 乙说的不对，小李写完了作业
- C: unknown [?, ?, F, ?] 丙说的不对，小赵没有写完作业
- D: unknown [?, ?, ?, ?] 丁说的不对，小赵写完了作业

### LTRUTH-REAL-002 (status=solved, option_status=unique_supported)
- A: entailed_by_all [T] 左手是水果糖，右手是奶糖
- B: unknown [?] 左手水果糖，右手水果糖
- C: unknown [?] 左手奶糖，右手奶糖
- D: unknown [?] 左手奶糖，右手水果糖

### LTRUTH-REAL-003 (status=ambiguous, option_status=no_supported_option)
- A: unknown [?, ?, ?] 没有人达标
- B: unknown [?, ?, ?] 全队都达标了
- C: unknown [?, ?, ?] 省运会冠军达标
- D: unknown [?, ?, ?] 国家队队员未达标

### LTRUTH-REAL-004 (status=ambiguous, option_status=no_supported_option)
- A: unknown [?, ?, ?, ?] 所有的柜子里都是购物袋
- B: unknown [?, ?, ?, ?] 所有的柜子里都没有购物袋
- C: unknown [?, ?, ?, ?] 所有的柜子里都没有购物礼品
- D: unknown [?, ?, ?, ?] 第三个柜子里有食品

### LTRUTH-REAL-005 (status=solved, option_status=unique_supported)
- A: contradicted_by_all [F] 乙不是爆炸案的元凶
- B: unknown [?] 甲不是爆炸案的元凶
- C: entailed_by_all [T] 丙是爆炸案的元凶
- D: unknown [?] 甲是爆炸案的元凶

### LTRUTH-REAL-006 (status=ambiguous, option_status=no_supported_option)
- A: unknown [?, ?, ?, ?] 白某预测是正确的
- B: unknown [?, ?, ?, ?] 邓某预测是正确的
- C: unknown [?, ?, ?, ?] 如果甲队能够晋级，那么方某的预测是正确的
- D: unknown [?, ?, ?, ?] 如果甲队不能晋级，那么方某的预测是正确的

### LTRUTH-REAL-007 (status=ambiguous, option_status=no_supported_option)
- A: unknown [?, ?, ?, ?] 甲、乙入选
- B: unknown [F, F, ?, F] 甲、丁入选
- C: unknown [?, ?, ?, F] 乙、丙入选
- D: unknown [F, F, ?, F] 乙、丁入选

### LTRUTH-REAL-008 (status=ambiguous, option_status=no_supported_option)
- A: unknown [?, ?, ?, ?, ?, ?] 甲、丁二人合伙作案
- B: unknown [?, ?, ?, ?, ?, ?] 丙、丁二人合伙作案
- C: unknown [?, ?, ?, ?, ?, ?] 甲、丙二人合伙作案
- D: unknown [?, ?, ?, ?, ?, ?] 甲、乙二人合伙作案

### LTRUTH-REAL-009 (status=solved, option_status=no_supported_option)
- A: unknown [?] 去了四姑娘山、塔公草原、墨石公园
- B: unknown [?] 去了塔公草原、墨石公园，没去四姑娘山
- C: unknown [?] 去了四姑娘山，没去塔公草原、墨石公园
- D: contradicted_by_all [F] 没去四姑娘山、塔公草原，去了墨石公园

### LTRUTH-REAL-010 (status=ambiguous, option_status=no_supported_option)
- A: unknown [?, ?, ?] 第一个
- B: unknown [?, ?, ?] 第二个
- C: unknown [?, ?, ?] 第三个
- D: unknown [?, ?, ?] 第四个

### LTRUTH-REAL-011 (status=solved, option_status=unique_supported)
- A: contradicted_by_all [F] 甲、乙都被录取
- B: entailed_by_all [T] 甲、乙都未被录取
- C: contradicted_by_all [F] 甲被录取，乙未被录取
- D: contradicted_by_all [F] 甲未被录取，乙被录取

### LTRUTH-REAL-012 (status=ambiguous, option_status=no_supported_option)
- A: unknown [?, ?, ?] 甲、戊、己
- B: unknown [?, ?, ?] 丙、戊、己
- C: unknown [?, ?, ?] 甲、乙、丁
- D: unknown [?, ?, ?] 甲、丙、丁

## Analysis

### unique_supported cases
- LTRUTH-REAL-002: predicted=A, expected=A, correct=True
- LTRUTH-REAL-005: predicted=C, expected=C, correct=True
- LTRUTH-REAL-011: predicted=B, expected=B, correct=True

## Recommendation

**Continue core enhancement.** Option mapping accuracy too low for integration.
