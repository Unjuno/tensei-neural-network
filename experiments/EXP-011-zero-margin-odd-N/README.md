# EXP-011 — 奇数Nでzero-margin仮定を外す

状態: `PREREGISTERED / NOT RUN`

由来: EXP-010のdesign-ineligible結果。偶数NではP=3 majority Qのlocal marginが奇数となりzeroが不可能だったため、奇数Nで改めて検査する。

## Q-011

P=3 / symmetric Hebbian / asynchronous one-unit update / zero-field保持の下で、componentwise-majority Qがstored / negation外かつzero local marginを含むfixed pointであるとき、split one-bit perturbationのcoordinate-minority escape制約は維持されるか。

## H-011

nonzero-margin仮定は実質的であり、奇数Nのzero-margin stable Qでは、固定探索範囲内に旧制約の反例が存在する。

## Locked search space

- N=`7,9,11,13,15,17`
- P=3
- RNG=`random.Random(1100000 + N)`
- 各Nで最初の128 eligible triple
- 最大200,000 candidate / N

eligible:

1. 3 stored patternsが相異なる
2. majority Qがstored / global-negation外
3. 全iで `Q_i h_i(Q) >= 0`
4. 少なくとも1 coordinateで `h_i(Q)=0`
5. split coordinateが1個以上

## Initial states / schedules

全split coordinateのone-bit flip。

各Nで、

- cyclic rotations N本
- `random.Random(1110000 + N)`による32 random permutations

を固定順で使う。

## Update / stopping

asynchronous one-unit update。zero local inputはcurrent value保持。一巡前後同一で停止。最大100 sweeps。

Qへ戻らないtrajectoryがcoordinate-minority stored pattern以外へ到達、stored negation / other nonstored / nonconvergenceなら反例。

N昇順 → eligible生成順 → coordinate → schedule。最初の反例で停止。

全固定範囲反例0なら`NO_COUNTEREXAMPLE_IN_SEARCH`。

## Interpretation

- `COUNTEREXAMPLE_FOUND`: strict positive marginが旧定理に本質的
- `NO_COUNTEREXAMPLE_IN_SEARCH`: zero-marginを許しても固定探索では破れず
- `UNCERTAIN`: eligible不足

作者側研究であり人物へ自動注入しない。
