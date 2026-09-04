# Definition Judgement v1 — Preflight Report

## 1. Current Git State

- HEAD: 94cb9e2
- commit message: finalize logic analysis core refinement pass
- git status: clean (only untracked `text-image/logic_analysis_real_cases_open_verified_v1/` test data directory)

## 2. Verification Results

- pytest: 158 passed ✅
- smoke test: passed ✅
- logic_reasoning.py: no diff ✅
- data_analysis.py: no diff ✅
- knowledge_base/all_cards.jsonl: no diff ✅

## 3. Definition Judgement Question Pack

**NOT FOUND.**

Checked path:
```
text-image/definition_judgement_real_cases_open_verified_v1/questions_manifest.json
```

The directory `text-image/definition_judgement_real_cases_open_verified_v1/` does not exist.

**Cannot enter definition_judgement solver development.**

## 4. Current Logic Reasoning Sub-module Status

| Sub-module | Question Pack | Results | Integration Status |
|---|---|---|---|
| 论证类 (Argument) | lr2_real_verified_20_images | 18/20 correct, 0 wrong, 2 null | Integrated |
| 翻译推理 (Translation) | logic_translation_real_cases_open_verified_v2 | 16/16 correct, 0 wrong, 0 null | Integrated |
| 真假推理 (Truth) | logic_truth_real_cases_open_verified_v1 | 4/12 correct, 0 wrong, 8 null | Integrated (conservative) |
| 分析推理 (Analysis) | logic_analysis_real_cases_open_verified_v1 | 2/12 correct, 0 wrong, 10 null | Integrated (conservative) |

## 5. What is Needed to Proceed

The user needs to provide:
```
definition_judgement_real_cases_open_verified_v1.zip
```

This should be extracted to:
```
text-image/definition_judgement_real_cases_open_verified_v1/
```

The pack should contain at minimum:
- `questions_manifest.json` — question cases with case_id, question_text, options
- `ANSWER_KEY.md` — standard answers for audit

**Do NOT let Claude Code find or create real exam questions.** The user must provide the verified question pack.

## 6. Next Steps

Once the question pack is provided:
1. Run package format check
2. Run current solver baseline on definition judgement cases
3. Begin `definition_judgement v1` isolated core audit
