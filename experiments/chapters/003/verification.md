# 第3話 Mandatory Verification

状態: `PASS`

Verification type: `EXECUTABLE_REPRODUCTION + HISTORICAL_SOURCE_CHECK`

## Fragile claims

第3話が依存する最も壊れやすい主張は次の二点。

1. EVT-009の6-unit toyでは、全64 binary statesを確認するとfixed pointは `A/B/C/-A/-B/-C` だけで、stored / stored-negationを除くresidualは0である。
2. Hopfield / Feinstein / Palmer (1983)が掲載した16-neurone / 3-memory例では、同論文のHebbian connection ruleから作ったweightsに対して、掲載candidate Qはstored patternでもそのglobal negationでもないstable stateである。

## Historical source check

主一次資料:

J. J. Hopfield, D. I. Feinstein, R. G. Palmer, “‘Unlearning’ has a stabilizing effect in collective memories,” *Nature* 304, 158–159 (1983), DOI `10.1038/304158a0`。

確認事項:

- Natureの書誌記録でpublished 14 July 1983
- abstractで30〜1,000 neuronesのmathematical / computer modellingを明示
- stored memoriesの学習に伴いspurious memoriesもcreated / evokedされ得ると明示
- 本文でbinary `μ_i = ±1`、asynchronous update、`T_ij = Σ_s μ_i^s μ_j^s`, `T_ii = 0`を記載
- 本文で16 neuronesのMemory 1 / 2 / 3とSpurious memoryの具体的符号列を掲載
- 本文はこのclassのspurious statesについて、elementary formがtriplesにoriginを持つと記述

今回のstory timeは1984〜1985年前後の候補範囲であり、この1983論文は人物が利用可能な過去資料として扱える。

## Executable procedure

`run.py` はPython標準ライブラリだけで次を独立再計算する。

### EVT-009 side

- A/B/Cから6-unit Hebbian weightsを再構成
- `{-1,+1}^6` 全64 statesを列挙
- zero-field hold ruleでfixed pointを全件検査
- fixed point集合が `A/B/C/-A/-B/-C` と一致することを確認
- residual countが0であることを確認

### EVT-011 side

- 1983論文掲載のM1/M2/M3/Qを固定値として入力
- `T_ij = Σ_s M_s,i M_s,j`, `T_ii=0`を再構成
- Qの全16 local inputsを計算
- expected vector

```text
(+21,+21,+5,+5,-5,-5,-21,-21,+5,-5,-5,+5,+5,-5,-5,+5)
```

と一致することを確認
- zero local inputが0件であることを確認
- 全16 unitで `Q_i * h_i > 0` を確認
- QがM1/M2/M3および-M1/-M2/-M3のどれとも一致しないことを確認

実行:

```bash
python experiments/chapters/003/run.py --check
```

保存結果: `results.json`

## PASS condition

上記checkが全て真。

## Actual result

- EVT-009 fixed points: 6 states、residual count = 0
- EVT-011 local inputs: expected vectorと完全一致
- EVT-011 zero local inputs: 0
- EVT-011 minimum signed margin: 5
- EVT-011 stored / negation match: false

判定: `PASS`

## Chapter impact

`novel/chapters/003.md` の中心描写、

- 6-unit toyでは三分類目が空
- 文献選択条件を先に固定して1983論文へ戻る
- 16-neurone掲載例をそのまま再計算する
- local inputが全てnonzeroでQと同符号
- Qがstored pattern / global negationの外にある

は再現結果と一致する。

本文はQを生物学的な「偽記憶」と断定せず、model-levelのspurious memoryという論文上の呼称と、二人が再計算したstable/nonstored classificationを分離しているため、このverificationからの修正は不要。

## Boundary

このPASSは、

- Qの一般的なmixture-state理論を証明しない
- basin sizeを測っていない
- unlearning効果を再現していない
- 大規模Hopfield network一般の頻度を主張しない
- 生物学的memoryの現象を証明しない

第3話の公開前integration checkとしてのみ有効。
