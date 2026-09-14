# EXP-009 — P=3仮定を外す反例探索

状態: `PREREGISTERED / NOT RUN`

由来: EXP-007で証明したP=3 coordinate-minority escape定理の仮定アブレーション。

## Q-009

保存パターン数をP=3からP=5へ増やし、componentwise-majority Qがstored / negation外のnonzero-margin stable stateである場合、Qのsplit coordinateを1 bit反転した非同期trajectoryがQへ戻らないとき、そのfinalは必ず**そのcoordinateでminority側にいたstored pattern集合**のどれかになるか。

P=5ではsplitが4:1または3:2になり、minority stored patternは1個または2個である。

## H-009

P=3で証明した制約はP=5では一般に破れる。固定探索範囲内に、Qへ戻らず、かつ反転coordinateのminority stored pattern集合にも属さないfinalまたはnonconvergenceが少なくとも1件存在する。

## Locked search space

- N = `12, 16, 20, 24`
- P = 5
- RNG: Nごとに `random.Random(900000 + N)`
- 各Nで最初の128 eligible quintupleを採用
- 最大200,000 candidate / N

eligible条件:

1. 5 stored patternsが互いに異なる
2. Qが5 stored patternsおよびglobal negationのいずれでもない
3. Qの全local inputがnonzeroかつQと同符号
4. split coordinateが1個以上存在

## Initial states

各eligible quintupleの全split coordinateについて、Qのその1 bitだけを反転した状態を全件使用する。

## Schedules

各Nについて結果前に、

- `1..N` のcyclic rotations N本
- `random.Random(910000 + N)` から生成する32 random permutations

を固定順で使用する。

重複scheduleがあっても結果後に差し替えない。

## Update

symmetric Hebbian weights:

`T_ij = Σ_{s=1..5} ξ_i^s ξ_j^s`, `T_ii=0`。

asynchronous one-unit update。

- positive → +1
- negative → -1
- zero → current value保持

一巡前後が同一ならfixed pointとして停止。最大100 sweeps。

## Counterexample

各反転coordinate iについて、`ξ_i^s != Q_i` を満たすstored patternsをminority set `L_i` とする。

trajectoryがQ以外へ行ったとき、finalが`L_i`のstored patternのどれかなら`CONSISTENT_WITH_EXTENSION`。

次のいずれかなら反例:

- Q以外かつ`L_i`外のstored pattern
- stored negation
- other nonstored fixed point
- nonconvergence

## Stopping rule

探索順はN昇順 → eligible生成順 → coordinate昇順 → cyclic schedules → random schedules。

最初の反例で停止し、そのケースを保存する。

全固定範囲完走で反例0なら`NO_COUNTEREXAMPLE_IN_SEARCH`。

## Interpretation

- `COUNTEREXAMPLE_FOUND`: P=3という仮定が旧定理に本質的であることを有限反例で示す
- `NO_COUNTEREXAMPLE_IN_SEARCH`: P=5でも固定探索では拡張規則が破れなかった。証明ではない
- `UNCERTAIN`: eligible不足等

作者側研究であり、結果をPER-005/PER-006へ自動注入しない。
