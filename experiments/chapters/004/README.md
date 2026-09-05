# 第4話「五と二十一」公開前検証

状態: `GATE_CANDIDATE`

対象本文:

- `novel/chapters/004.md`
- `novel/chapters/004-outline.md`

採用event:

`EVT-012 -> EVT-013`

## 現在の位置

第4話本文を成立済みeventからNarrativeProjection済み。

Mandatory Verification、terminology review、semantic reviewは完了し、公開前本番相当のstrict CIを通すcandidate状態へ進めた。

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

## Candidate gate

次をCIで確認する。

1. validator unit tests
2. executable chapter verifications
3. strict workflow validator

candidate CIがPASSするまでは`PREPUBLICATION_GATE_PASSED`へ変更しない。
