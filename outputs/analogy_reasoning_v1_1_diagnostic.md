# analogy_reasoning v1.1 Diagnostic

## v1.0 → v1.1 Changes

1. **Removed specific test entity words** from solver source: 黑陶, 白瓷, 青瓷, 红砖, 棉布, 棉纱, 脱脂棉, 原棉, 黏土, 春季过敏, 花粉, 喷嚏, 猛药去疴, 重典治乱, 匿名投票, 实名投票, 现场投票
2. **Raised threshold for three-word stems** (+0.2 penalty)
3. **Filtered weak-only relation types**: when only sequence/degree/grammar_structure detected, cannot predict
4. **Removed medical-specific detection code** that contained test-specific words

## v1.0 vs v1.1 Comparison

| Metric | v1.0 | v1.1 |
|--------|------|------|
| Total | 12 | 12 |
| Solved | 4 | 0 |
| Ambiguous | 3 | 6 |
| Analysis_only | 5 | 6 |
| Correct | 2 | 0 |
| Wrong | 2 | 0 |
| Null | 8 | 12 |

## Correct Drop Explanation

Correct dropped from 2 to 0 because:
- v1.0 had 2 wrong predictions (analog_006, analog_011)
- The wrong predictions were caused by insufficient relation detection quality
- Rather than adding test-specific rules, the solver was made more conservative
- This is the correct approach: wrong=0 is the hard requirement

## Next Steps

1. Improve generic relation detection (especially for three-word and four-character phrases)
2. Add more structural pattern matching without specific entity words
3. Goal: correct >= 3 with wrong = 0
