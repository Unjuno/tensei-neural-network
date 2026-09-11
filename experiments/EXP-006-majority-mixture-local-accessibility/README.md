# EXP-006 — 3-pattern majority mixtureの局所到達性

状態: `PREREGISTERED / NOT RUN`

由来: EVT-014 / EVT-015。

## Q-006

ランダムな3-pattern Hebbian networkで、3-pattern componentwise-majority mixture Qがstored / negation外のstable stateになる例に限定したとき、Qの一ビット近傍からの局所到達性は、三pattern全員一致coordinateと2対1coordinateで系統的に異なるか。

## H-006

対象例の平均で、全員一致coordinateを反転したinitial stateのQ-return fractionは、2対1coordinateを反転した場合より高い。

これはEVT-014の一例を見た後に立てた**作者側の新仮説**であり、1980年代人物の事前知識ではない。

## Model

- N = 16
- P = 3
- patterns: independent uniform `{-1,+1}`
- weights: `T_ij = Σ_s ξ_i^s ξ_j^s`, `T_ii = 0`
- Q: coordinatewise majority of the three patterns
- update: asynchronous, one unit at a time
- zero local input: current value retained

## Sampling lock

Python標準ライブラリ `random.Random(19830914)` を使う。

各candidate tripleを順に生成し、次をすべて満たすものだけeligibleとする。

1. M1/M2/M3が互いに異なる
2. QがM1/M2/M3およびそのglobal negationのいずれでもない
3. Qの16 local inputsがすべてnonzeroでQと同符号（tie conventionに依存せずstable）
4. unanimous coordinateと2対1 coordinateが少なくとも1個ずつ存在

最初の256 eligible triplesを採用して停止する。結果を見てcandidateを飛ばさない。

最大100,000 candidate triplesまでに256 eligibleが得られなければ`INSUFFICIENT_ELIGIBLE`として停止する。

## Local-accessibility protocol

各eligible tripleについて、Qの16 coordinatesを一つずつ反転した16 initial statesをすべて使う。

各initial stateについて `1..16` のcyclic rotation 16本をすべて使う。

1 eligible tripleあたり256 trajectories。

各trajectoryはsweep前後が同一なら停止、最大100 sweeps。100 sweepsで止まらなければnonconverged。

## Primary measure

各eligible triple内で、

- unanimous-flip trialsのQ-return fraction `r_u`
- split-flip trialsのQ-return fraction `r_s`

を計算する。

主要集計:

- `mean(r_u - r_s)`
- `median(r_u - r_s)`
- `count(r_u > r_s)`, `count(r_u = r_s)`, `count(r_u < r_s)`

## Secondary descriptive outputs

- eligible / generated candidate数
- unanimous / split coordinate数の分布
- Q以外finalのstored / nonstored分類
- nonconverged数
- EVT-014と同じ「split coordinateを反転したとき、そのcoordinateのminority stored patternへ逃げる」現象の出現割合

## Decision

`SUPPORT`:

- 256 eligible triplesが得られ、`median(r_u-r_s) > 0` かつ `count(r_u>r_s) > count(r_u<r_s)`

`NOT_SUPPORT`:

- 256 eligible triplesが得られるが上記を満たさない

`UNCERTAIN`:

- eligible不足またはnonconvergence等でprimary measureを定義できない

この判定はN=16/P=3/固定sampling/update familyに限定する。一般定理や自然確率とはしない。

## Implementation assumptions

- CPython標準ライブラリのみ
- exact integer arithmetic
- RNG: Python `random.Random`, seed固定
- NumPy / BLAS / GPUなし
- performance benchmarkは目的外
