# 第4話「五と二十一」公開前検証

状態: `PREPUBLICATION_GATE_PASSED`

対象本文:

- `novel/chapters/004.md`
- `novel/chapters/004-outline.md`

採用event:

`EVT-012 -> EVT-013`

## 現在の位置

第4話本文を成立済みeventからNarrativeProjection済み。

Mandatory Verification、terminology review、semantic reviewを完了し、`GATE_CANDIDATE`状態で本番相当のstrict CIを通過したため`PREPUBLICATION_GATE_PASSED`へ昇格した。

これはCanon昇格・main反映・実公開の承認ではない。Human Reviewを別途必要とする。

## Mandatory Verification

- `verification.md`: `PASS`
- `run.py`
- `results.json`: `PASS`

中心check:

- Qがcomponentwise majorityと16/16位置で一致
- unanimity 4 / split 12
- minority counts M1/M2/M3 = 4/4/4
- Q distances = 4/4/4
- stored pair distances = 8/8/8
- overlaps = 8/8/8
- `h_i=8(M1_i+M2_i+M3_i)-3Q_i`
- direct / derived local inputsが16/16一致

実行:

```bash
python experiments/chapters/004/run.py --check
```

## Terminology

`terminology.md`: `PASS`

- `多数決`をmechanism名にしない
- `多数側 / 成分多数`として操作的に限定
- stabilityとreachabilityを分離
- mixture-state用語を人物へ導入しない

## Semantic Review

`semantic-review.md`: `PASS`

knowledge boundary / unresolved fact / anachronism / projection fidelity / provenance / narrative-meta leakageを確認済み。

## Candidate CI

`GATE_CANDIDATE` commit `72cbd3b1f7fcd7a55c8d760606261af4d374f783` に対するGitHub Actions run `33996369324` はsuccess。

成功step:

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
