# EXP-010 — nonzero-margin仮定を外す反例探索

状態: `PREREGISTERED / NOT RUN`

由来: EXP-007解析証明の仮定アブレーション。

## Q-010

P=3 / symmetric Hebbian / asynchronous one-unit updateは維持し、Qのstabilityを`h_i Q_i > 0`から、zero-field保持規則の下での`h_i Q_i >= 0`へ弱めた場合、split one-bit perturbationのcoordinate-minority escape制約は維持されるか。

## H-010

nonzero-marginは実質的仮定であり、Qにzero local inputを含むstable majority stateでは固定探索範囲内に旧制約の反例が存在する。

## Locked search space

- N=`8,12,16,20,24`
- P=3
- RNG=`random.Random(1000000 + N)`
- 各Nで最初の128 eligible triple
- 最大200,000 candidate / N

eligible:

1. 3 stored patternsが相異なる
2. componentwise-majority Qがstored / global-negation外
3. 全iで `Q_i h_i(Q) >= 0`
4. 少なくとも1 coordinateで `h_i(Q)=0`
5. split coordinateが1個以上

ここでzero fieldはcurrent bit保持なのでQ自体はfixed pointとして扱う。

## Initial states / schedules

全split coordinateのone-bit flipを使用。

各Nで、

- cyclic rotations N本
- `random.Random(1010000 + N)`による32 random permutations

を結果前固定順で使用する。

## Update

asynchronous one-unit update。positive→+1、negative→-1、zero→current保持。一巡前後同一で停止、最大100 sweeps。

## Counterexample

Qへ戻らないtrajectoryが、その反転coordinateでQと異なる唯一のstored pattern以外へ到達、stored negation / other nonstored / nonconvergenceになれば反例。

## Stopping

N昇順 → eligible生成順 → coordinate昇順 → schedule固定順。最初の反例で停止。

全範囲反例0なら`NO_COUNTEREXAMPLE_IN_SEARCH`。

## Interpretation

- `COUNTEREXAMPLE_FOUND`: nonzero-marginが旧定理に本質的
- `NO_COUNTEREXAMPLE_IN_SEARCH`: 有限探索では破れず。証明ではない
- `UNCERTAIN`: eligible不足等

作者側研究。人物stateへ自動注入しない。
