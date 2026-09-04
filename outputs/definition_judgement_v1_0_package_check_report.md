# Definition Judgement v1.0 — Package Check Report

## Manifest Format

- Format: JSON with nested `cases` array
- Total cases: 12
- Schema version: 1.0

## Case Structure

Each case contains:
- `case_id`: string (e.g., "dj_open_v1_001")
- `question_type`: "definition_judgement"
- `subtype`: string (single_definition_match, single_definition_not_match, multi_definition_match_specific, multi_definition_classification)
- `polarity`: string (match, not_match, match_specific_definition, classification_match)
- `question_text`: string (full question with definition)
- `options`: dict {A: string, B: string, C: string, D: string}
- `answer`: string (A/B/C/D)
- `expected_answer`: string (A/B/C/D)
- `definition_terms`: list of strings
- `tags`: list of strings

## Answer Key

- ANSWER_KEY.md: ✅ exists, 12 answers parseable
- SOURCES.md: ✅ exists
- AUDIT_NOTES.md: ✅ exists
- CANDIDATES_REVIEW_NEEDED.json: ✅ exists
- README.md: ✅ exists

## Readiness

**Ready for isolated core audit.**
