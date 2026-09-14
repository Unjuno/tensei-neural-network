# EVT-016 更新順のどこで分岐が始まるかを固定して調べる

状態: `ACTION_LOCKED`

Resolution provenance: `LOCKED`

## Story time

`T0-1980S + order-mechanism follow-up after EVT-015`

## Timeline position

- Parent: `EVT-015`
- Previous event: `EVT-015`
- Next event: 未成立

## Resolution scope

- PER-005 高橋修一
- PER-006 佐伯玲子
- EVT-011の16素子 / M1/M2/M3/Q / Hebbian結合
- EVT-014で既に固定・実行したsplit 12 initial states × cyclic 16 orders = 192 trajectories

作者側EXP-006〜011はscope外。人物はその結果・証明を観測していない。

## World before

EVT-014ではsplit coordinateを1 bit反転した192 trialについて、更新順によりQまたはそのcoordinateのminority stored patternへ分岐した。

EVT-015では、初期状態のgeometryとしてminority memoryだけがQからdistance 4→3へ近づくことを確認した。しかし「更新順のどこで分岐が決まるか」は未説明。

高橋の局所目標は、距離ではなく実際の一素子更新列を比較してbranching mechanismを見つけること。

佐伯の局所目標は、都合のよい2本だけでなく192本全部を同じ分類規則で見ること。

---

# ACTION LOCK

## Included trials

EVT-014の12 split initial states × 16 cyclic orders = 192 trialを全件再計算する。

unanimity 4 initial statesは今回の主分類から外す。EVT-014で全64 trialがQへ戻ることが既に分かっており、今回の問いはorder-dependentだったsplit statesのbranchingだからである。この除外は結果計算前に固定する。

## Fixed dynamics

EVT-014と同一:

- same M1/M2/M3/Q
- same Hebbian weights
- asynchronous one-unit update
- positive→+1 / negative→-1 / zero→current保持
- same 16 cyclic orders
- sweep前後同一で停止

## Recorded trace

各trialについてunit updateを一つずつ追い、各**実bit flip**を時系列で記録する。

initial stateでは反転coordinateを`k`とする。

最初の実bit flipを次の排他的categoryへ分類する。

- `REPAIR_K_FIRST`: 最初の実flipがkをQの値へ戻す
- `OTHER_FLIP_FIRST`: k以外のunitが最初にQから離れる方向へ実flipする
- `NO_FLIP_FIRST_SWEEP`: 最初の一巡で実flipなし
- `OTHER`: 上記に入らない

さらに、

- first flipのunit
- first flip時点のupdate index
- kが最初に更新された時点のlocal input符号
- 最終状態 Q / minority stored pattern / other
- 総実flip数

を記録する。

## Predeclared comparisons

1. `REPAIR_K_FIRST` / `OTHER_FLIP_FIRST`ごとのfinal集計
2. first-flip categoryがfinalを一意に決めるか
3. coordinateごとのcategory分布
4. 192 trialに`OTHER` / unexpected final / nonconvergenceがあるか

## Outcome labels

- `FIRST_FLIP_SEPARATES`: first-flip categoryだけでQ vs minority finalが完全分離する
- `PARTIAL_ASSOCIATION`: categoryとfinalに対応はあるが完全分離しない
- `NO_SIMPLE_ASSOCIATION`: 明瞭な対応なし
- `UNEXPECTED_DYNAMICS`: other final / nonconvergence等

どの結果でも後からcategory定義を変更しない。

## Stopping rule

192 trial全件を同じ規則で処理した時点で停止する。結果後に別schedule familyを追加しない。

## Generation validation

- 問いはEVT-015のpersona goalsから直接生じている
- 作者側EXP-006/007の一般則・proofを人物へ使っていない
- EVT-014で既に成立したtrial familyを全件再分類するため、結果を出すための新pattern / schedule選択をしない
