# 第2話 Mandatory Verification

状態: `IN_PROGRESS`

Verification type: `EXECUTABLE_REPRODUCTION`

## Fragile claim

第2話が依存する最も壊れやすい主張は、同一の6-unit / 3-pattern networkについて、EVT-005〜008で成立した次の結果が相互に整合していることである。

1. 6 cyclic ordersを同一cueへ適用すると A:1 / B:2 / D:3
2. A/B-balanced cueは6種類あり、6 ordersとの組合せは36 trials
3. 全binary initial stateは64、6 ordersとの組合せは384 trials
4. fixed pointsは A/B/C/-A/-B/-C の6状態
5. EVT-005でDと呼んだ状態は -C
6. zero-bias linear local field + zero-field hold ruleでは、同一update orderについて `U(-s) = -U(s)` が成立する

## Planned procedure

第1話の検証コードを流用せず、第2話package内で入力条件を明示した再現コードを作る。

- A/B/CからHebbian weight matrixを再構成
- EVT-005の6 cyclic ordersを生成
- EVT-004/005 cueについて6 runsを再現
- A/B balanced cuesを規則から全列挙して36 runsを再現
- `{-1,+1}^6` 全64 states × 6 ordersを再現
- fixed pointsとfinal-state集合を集計
- D=-Cをassert
- 任意64 statesについて各one-unit updateのsign inversion commutationをassert

## PASS condition

上記6項目がすべてEVT-005〜008正本と一致する。

## FAIL condition

一つでも不一致がある。

## UNCERTAIN condition

EVT正本間で条件定義が一致せず、同一実験として再構成できない。

## Current result

未実行。

本文はこのverificationがPASSするまで `PREPUBLICATION_GATE_PASSED` にしない。
