# EXP-008 — 非同期更新仮定を外す反例探索

状態: `COMPLETED / COUNTEREXAMPLE FOUND`

事前登録commit: `3be803411f1f74b8daf218f68ef2305885fa75f5`

由来: EXP-007で証明したcoordinate-minority escape定理の仮定アブレーション。

## Q-008

P=3のstable nonstored componentwise-majority mixture Qについて、更新を非同期one-unit updateから**同期一括更新**へ変えた場合にも、split coordinateを1 bit反転した初期状態は、Qまたはそのcoordinateのminority stored pattern以外へ行かないか。

## Locked hypothesis

EXP-007の結論は同期更新では一般に維持されない。固定探索範囲内に、少なくとも1件、Q / coordinate-minority stored pattern以外のfixed point、周期軌道、または100 step非収束が存在する。

探索条件は事前登録版から変更していない。

## Result

最初のN=8 blockで、24 candidate中2番目のeligible tripleまでに反例が出た。事前登録順で確認したsplit initial stateの8件目。

stored patterns:

```text
M1 = (+,+,+,+,-,+,-,+)
M2 = (-,+,+,+,+,+,-,+)
M3 = (-,+,-,+,-,+,+,+)
Q  = (-,+,+,+,-,+,-,+)
```

split coordinate 3を反転する。この位置のminority stored patternはM3。

initial:

```text
(-,+,-,+,-,+,-,+)
```

同期一括更新では、

```text
(-,+,-,+,-,+,-,+)
→ (-,+,+,+,-,+,+,+)
→ (-,+,-,+,-,+,-,+)
```

となり、**period-2 cycle**を形成した。

QにもM3にも収束しないため、事前定義どおり`COUNTEREXAMPLE_FOUND`。

## Interpretation

EXP-007で得た非同期更新下の定理は、更新を同期一括へ替えるとそのまま維持されない。

特に解析証明で使った「実bit flipごとにHopfield energyがstrictに低下し、有限state spaceなのでfixed pointへ到達する」という部分は同期更新では使えない。今回のperiod-2 orbitは、その仮定差が結果を実際に変える具体例になった。

したがって**asynchronous one-unit updateは単なる実装細部ではなく、定理の実質的仮定**である。

これは同期Hopfield dynamics一般の分類ではない。P=3 / binary Hebbian / zero-input保持 / 固定探索の一反例で十分に旧結論の一般化を棄却しただけである。

実装: `run.py`
保存結果: `results.json`
作者側研究でありPER-005/PER-006へ自動注入しない。
