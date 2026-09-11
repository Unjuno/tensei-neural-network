# EXP-007 — split one-bit escapeの反例探索

状態: `PREREGISTERED / NOT RUN`

由来: EXP-006 secondary finding。

## Q-007

3-pattern componentwise-majority mixture Qがstored / negation外のnonzero-margin stable stateであるとき、split coordinateを一つ反転した初期状態から非同期更新し、Qへ戻らなかったtrajectoryは必ずそのcoordinateのminority stored patternへ行くのか。

EXP-006では固定N=16 / cyclic ordersの17,488 non-Q trajectoriesすべてで成立した。今回はこれを支持する例を増やすより、**反例を探す**。

## Falsifiable hypothesis H-007

固定探索範囲内で、split one-bit initial stateからQ以外へ収束したtrajectoryのfinalは、そのcoordinateのminority stored patternである。

一件でも、

- 別のstored pattern
- stored negation
- other nonstored fixed point / cycle
- nonconvergence

へ行けば反例として`COUNTEREXAMPLE_FOUND`。

## Locked search space

Nを `8, 12, 16, 20, 24` とする。P=3固定。

各Nについて `random.Random(700000 + N)` でindependent uniform binary pattern tripleを生成する。

eligible条件:

1. 3 patternsが互いに異なる
2. majority Qが3 stored / 3 global negationのいずれでもない
3. Qの全local inputがnonzeroかつQと同符号
4. split coordinateが1個以上存在

各Nで最初の128 eligible triplesまで採用。100,000 candidatesで不足ならそのNを`INSUFFICIENT_ELIGIBLE`。

## Schedules

各eligible tripleについて、split coordinateを一つ反転したinitial stateをすべて使う。

各initial stateに対し、

- `1..N` のcyclic rotations N本
- `random.Random(710000 + N)` から生成する32 random permutations

を使う。

random permutationsはcandidate結果に依存せず、Nごとに固定系列から順に生成する。重複しても結果後に差し替えない。

## Update

Hebbian `T_ij=Σ ξ_i^s ξ_j^s`, `T_ii=0`。

非同期one-unit update。zero local inputはcurrent value保持。

sweep前後が同一なら停止。最大100 sweeps。

## Stopping

探索順はN昇順、eligible生成順、coordinate昇順、schedule列順。

**最初の反例を発見した時点で停止し、その反例を保存する。**

全固定探索範囲を完走して反例がなければ`NO_COUNTEREXAMPLE_IN_SEARCH`。

## Interpretation

- `COUNTEREXAMPLE_FOUND`: H-007をこの形では棄却
- `NO_COUNTEREXAMPLE_IN_SEARCH`: 固定探索で反例なし。定理の証明ではない
- `UNCERTAIN`: eligible不足等で固定探索を実施できない

EXP-006を見た後の反例探索であり、1980年代人物へ結果を自動注入しない。
