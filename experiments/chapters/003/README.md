# 第3話「表の外」公開前検証

状態: `GATE_CANDIDATE`

対象本文:

- `novel/chapters/003.md`
- `novel/chapters/003-outline.md`

採用event:

`EVT-009 -> EVT-010 -> EVT-011`

## 現在の位置

第3話本文を成立済みeventからNarrativeProjection済み。

Mandatory Verification、terminology review、semantic reviewは完了し、公開前本番相当のstrict CIを通すcandidate状態へ進めた。

`GATE_CANDIDATE`は公開候補化済みを意味しない。strict CI PASS後のみ`PREPUBLICATION_GATE_PASSED`へ昇格する。

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

## Candidate gate

次をCIで確認する。

1. validator unit tests
2. executable chapter verifications
3. strict workflow validator

candidate CIがPASSするまでは`PREPUBLICATION_GATE_PASSED`へ変更しない。
