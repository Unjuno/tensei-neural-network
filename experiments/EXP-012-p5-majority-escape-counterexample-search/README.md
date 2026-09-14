# EXP-012 — P=3仮定を外す反例探索

状態: `COMPLETED / COUNTEREXAMPLE FOUND`

旧仮ID: `EXP-009-p5-majority-escape-counterexample-search`。既存正本`EXP-009-exact-update-boundary`とのID衝突をCIで検出したため、結果・条件を変えずEXP-012へ改番した。

事前登録commit: `310ccd20a006cd13d7ff50c2f5120f73f5804804`

由来: EXP-007で証明したP=3 coordinate-minority escape定理の仮定アブレーション。

## Q-012

保存パターン数をP=3からP=5へ増やし、componentwise-majority Qがstored / negation外のnonzero-margin stable stateである場合、Qのsplit coordinateを1 bit反転した非同期trajectoryがQへ戻らないとき、そのfinalは必ずそのcoordinateでminority側にいたstored pattern集合のどれかになるか。

## Locked hypothesis

P=3で証明した制約はP=5では一般に破れる。固定探索範囲内に、Qへ戻らず、かつ反転coordinateのminority stored pattern集合にも属さないfinalまたはnonconvergenceが少なくとも1件存在する。

探索条件は事前登録版から変更していない。

## Result

N=12 blockの最初のeligible quintupleで反例が出た。事前登録探索順で59本目のtrajectory。

反転coordinateは2。QのこのcoordinateでminorityなのはM1だけ。

```text
Q       = (-,+,+,+,-,-,-,-,-,+,-,-)
initial = (-,-,+,+,-,-,-,-,-,+,-,-)
```

使用したrandom schedule:

```text
7,10,11,6,3,9,1,5,12,8,4,2
```

2 sweepsで、

```text
final = (+,-,-,+,-,-,-,-,-,+,+,-)
```

へ収束した。

このfinalはQでもstored patternでもglobal negationでもなく、`OTHER_NONSTORED` fixed pointである。

事前定義どおり`COUNTEREXAMPLE_FOUND`。

## Interpretation

P=3で証明した「Qへ戻らないなら反転coordinateのminority stored patternへ行く」という制約はP=5へそのまま拡張できない。

P=5では、一coordinateの多数/少数関係だけではtrajectoryの行き先を閉じ込められず、別のnonstored attractorへ逃げることがある。

したがって**P=3は旧定理の実質的仮定**である。

実装: `run.py`
保存結果: `results.json`
作者側研究であり、PER-005/PER-006へ自動注入しない。
