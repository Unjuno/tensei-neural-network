# 第3話「表の外」公開前検証

状態: `PREPUBLICATION_GATE_PASSED`

対象本文:

- `novel/chapters/003.md`
- `novel/chapters/003-outline.md`

採用event:

`EVT-009 -> EVT-010 -> EVT-011`

## 現在の位置

第3話本文を成立済みeventからNarrativeProjection済み。

Mandatory Verification、terminology review、semantic reviewを完了し、`GATE_CANDIDATE`状態で本番相当のstrict CIを通過したため`PREPUBLICATION_GATE_PASSED`へ昇格した。

これはCanon昇格・main反映・実公開の承認ではない。Human Reviewを別途必要とする。

## Mandatory Verification

- `verification.md`: `PASS`
- `run.py`
- `results.json`: `PASS`

中心check:

- 6-unit toyの全64 statesからfixed pointを再列挙しresidual=0を確認
- 1983論文掲載16-neurone例のQを同じHebbian connection ruleで再計算
- 16 local inputsがexpected vectorと一致
- zero inputなし
- 全unitでQとlocal-inputの符号一致
- Qはstored / stored-negation外

実行:

```bash
python experiments/chapters/003/run.py --check
```

## Historical evidence

主資料:

Hopfield, Feinstein & Palmer (1983), “‘Unlearning’ has a stabilizing effect in collective memories,” *Nature* 304, 158–159, DOI `10.1038/304158a0`。

1983-07-14公刊。第3話の候補story time（1984〜1985年前後）より前。

## Terminology

`terminology.md`: `PASS`

blocking uncertaintyなし。`spurious memory`を心理学的な「偽記憶」と固定せず、1983論文上のmodel-level呼称として扱う。

## Semantic Review

`semantic-review.md`: `PASS`

knowledge boundary / historical anachronism / NarrativeProjection fidelity / plot conditioning / interpretation boundaryを確認済み。

## Candidate CI

`GATE_CANDIDATE` commit `249c18677be725f0bfc1e8e96cf2db93fc49d7a4` に対するGitHub Actions run `33995822802` はsuccess。

成功したstep:

1. validator unit tests
2. executable chapter verifications
3. strict workflow validator

## Gate meaning

`PREPUBLICATION_GATE_PASSED`は、現在のevent/state/evidenceに対して公開前工程を通過したことだけを意味する。

- 科学的完全性の最終保証ではない
- 歴史的完全性の最終保証ではない
- 文学的完成の最終保証ではない
- Canon昇格ではない
- main反映・公開承認ではない
