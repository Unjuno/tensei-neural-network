# EXP-008 — 非同期更新仮定を外す反例探索

状態: `PREREGISTERED / NOT RUN`

由来: EXP-007で証明したcoordinate-minority escape定理の仮定アブレーション。

## Q-008

P=3のstable nonstored componentwise-majority mixture Qについて、更新を非同期one-unit updateから**同期一括更新**へ変えた場合にも、split coordinateを1 bit反転した初期状態は、Qまたはそのcoordinateのminority stored pattern以外へ行かないか。

## H-008

EXP-007の結論は同期更新では一般に維持されない。固定探索範囲内に、少なくとも1件、Q / coordinate-minority stored pattern以外のfixed point、周期軌道、または100 step非収束が存在する。

これはEXP-007の解析証明が使う「実bit flipごとのHopfield energy strict descent」を外す検査である。

## Locked search space

- N = `8, 12, 16, 20, 24`
- P = 3
- NごとのRNG: `random.Random(800000 + N)`
- 各Nで最初の128 eligible tripleを採用
- 最大100,000 candidate / N

eligible条件:

1. 3 stored patternsは互いに異なる
2. Qは3 stored patternsおよびglobal negationのいずれでもない
3. Qの各local inputはnonzeroでQと同符号
4. split coordinateを1個以上持つ

## Initial states

各eligible tripleの全split coordinateについて、Qのその1 bitだけを反転した状態を全件含める。

## Update

Hebbian symmetric weights:

`T_ij = Σ_s ξ_i^s ξ_j^s`, `T_ii = 0`。

1 stepで**全unitを同じ旧状態から同時更新**する。

- `h_i > 0` → `+1`
- `h_i < 0` → `-1`
- `h_i = 0` → 現在値を保持

同じstateが再出現したらcycleとして停止する。最大100 synchronous steps。

## Counterexample definition

各split coordinateには、その位置でQと異なるstored patternが一つだけ存在し、それをminority stored patternとする。

initial stateからのtrajectoryが、

- Q fixed point
- coordinate-minority stored pattern fixed point

のいずれかで終われば`CONSISTENT_WITH_ASYNC_RULE`。

次のいずれかなら**反例**:

- 上記以外のfixed point
- 周期2以上のcycle
- 100 stepで未停止

## Stopping rule

探索順はN昇順、eligible生成順、split coordinate昇順。

最初の反例を発見した時点で停止し、そのtriple / coordinate / trajectoryを保存する。

全固定範囲を完走して反例がなければ`NO_COUNTEREXAMPLE_IN_SEARCH`。

## Interpretation

- `COUNTEREXAMPLE_FOUND`: asynchronous one-unit update仮定がEXP-007定理に実質的であることを有限反例で示す
- `NO_COUNTEREXAMPLE_IN_SEARCH`: 同期更新でも固定探索では破れなかった。証明ではない
- `UNCERTAIN`: eligible不足など

P=3、binary Hebbian、zero-input保持という他の仮定は維持する。作者側研究であり、1980年代人物へ自動注入しない。
