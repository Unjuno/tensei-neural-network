# 第3話「表の外」公開前検証

状態: `IN_PROGRESS`

対象本文:

- `novel/chapters/003.md`
- `novel/chapters/003-outline.md`

採用event:

`EVT-009 -> EVT-010 -> EVT-011`

## 現在の位置

第3話本文を成立済みeventからNarrativeProjection済み。

Mandatory Verificationは実行済みで`PASS`。terminology review / semantic review / CI strict gateを確認してから公開候補化する。

## Mandatory Verification

- `verification.md`
- `run.py`
- `results.json`

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

## Remaining gate work

- `terminology.md` のblocking項目確認
- `semantic-review.md` の固定format review
- CIでchapter experiments / strict validator再実行

現時点では `PREPUBLICATION_GATE_PASSED` としない。
