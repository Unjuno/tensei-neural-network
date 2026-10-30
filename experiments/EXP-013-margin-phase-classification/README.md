# EXP-013 — P=3 one-bit perturbationのmargin相図

状態: `COMPLETED / PHASE_RULE_MATCHED_SEARCH`

由来: EXP-007/011の解析証明をさらに精密化する。

## Q-013

P=3 componentwise-majority Qがzero-field保持規則の下でstableなとき、split coordinate kを一つ反転した非同期trajectoryの最終状態は、kと同じminority pattern typeのQ上local margin `a`だけで次の3領域へ完全分類できるか。

## H-013 / 事前予測

同じminority typeに属する全unitはQ上で同じgauge local margin `a=Q_i h_i(Q)>=0`を持つ。

予測:

1. `a = 0`:
   - damaged kはzero fieldで保持
   - 他の同型unitはflip可能
   - 全scheduleでcoordinate-minority stored patternへ到達

2. `0 < a < 6`:
   - damaged kも他の同型unitもinitially flip可能
   - kが同型unit集合の中で最初に更新されればQ
   - k以外が先ならcoordinate-minority stored pattern

3. `a >= 6`:
   - damaged kだけがrepair方向へflip可能（`a=6`では他同型unitはtie保持）
   - 全scheduleでQへ到達

`a`は整数なので実際のmiddle regimeは通常`1..5`。

## Locked finite validation

- N = `7,8,9,10,11,12,13,14,15,16`
- P=3
- Nごとに`random.Random(1300000+N)`
- 各Nで最初の64 eligible triples
- 最大100,000 candidate / N

eligible:

1. stored patternsは相異なる
2. majority Qはstored / global-negation外
3. Qはzero-field保持規則でstable: 全i `Q_i h_i(Q)>=0`
4. split coordinateが存在

各split coordinateを一つ反転したinitial stateを全件含める。

Schedules:

- cyclic rotations N本
- `random.Random(1310000+N)`から16 random permutations

を固定する。

## Prediction check

各trajectoryについて、minority pattern typeのdifference set Dとmargin aを計算し、上の3-regime ruleだけからfinal Q / minority storedを予測する。

middle regimeではschedule中でDのうち最初に現れるunitがkか否かだけを見る。

実際の非同期trajectoryを最大100 sweepsまで実行し、予測とfinalを照合する。

一件でも、

- predicted finalとactual finalが違う
- Q/minority以外へ到達
- nonconvergence

なら`COUNTEREXAMPLE_FOUND`で停止。

固定範囲完走で`PHASE_RULE_MATCHED_SEARCH`。

## Recorded outputs

- eligible / trajectories
- a=0 / 0<a<6 / a>=6 のinitial-state数とtrajectory数
- 各regimeのQ/minority final数
- 最初のcounterexample（あれば）

## Interpretation

有限検証が一致しても定理の根拠は解析証明側に置く。実験は実装・代数の取り違えを反証する回帰検査として扱う。

作者側研究であり、結果・一般則を1980年代人物へ自動注入しない。

---

## 実行結果（事前登録後）

状態: `PHASE_RULE_MATCHED_SEARCH`。事前登録したN=7〜16、各Nで最初の64 eligible triples（合計640）を除外・追加せず検査した。split coordinateに対する全139,440 trajectoriesで、保存された事前予測と非同期逐次更新の実際のfinalが一致し、非収束・反例は0だった。

| Q上の同型局所余裕 `a` | 1-bit初期状態件数 | trajectory件数 | Qへ復帰 | 少数派storedへ到達 |
|---|---:|---:|---:|---:|
| `a=0` | 624 | 16,234 | 0 | 16,234 |
| `0<a<6` | 2,904 | 81,257 | 32,853 | 48,404 |
| `a>=6` | 1,400 | 41,949 | 41,949 | 0 |
| **計** | **4,928** | **139,440** | **74,802** | **64,638** |

集計単位を区別する。1-bit初期状態件数は各eligible triple内で異なるsplit coordinateを反転したケース数、trajectory件数はさらにscheduleを掛けた件数。640個の異なるnetwork例と、139,440個の独立な無作為標本を意味しない。

実装: `run.py`。結果: `results.json`。CPython標準ライブラリの固定seed・整数演算・非同期one-unit更新・ゼロ入力保持を使用。別実装で2026-10-30に同一の全体集計・N別件数・余裕別件数を照合済み。最新GitHub Actionsでの再実行照合はCI設定追加後に別途確認する。

結果を踏まえて実験対象や判定規則を差し替えてはいない。有限検証の成功は、全Nや任意の更新規則に関する一般定理ではない。予測根拠は別途の解析証明に置き、実読者評価・人物Knowledgeへの移行を意味しない。
