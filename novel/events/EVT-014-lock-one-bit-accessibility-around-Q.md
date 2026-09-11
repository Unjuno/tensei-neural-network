# EVT-014 Qの一ビット近傍からの到達性を固定する

状態: `ACTION_LOCKED`

Resolution provenance: `LOCKED`

## Story time

`T0-1980S + immediate follow-up after EVT-013`

## Timeline position

- Parent: `EVT-013`
- Previous event: `EVT-013`
- Next event: 未成立

## Resolution scope

- PER-005 高橋修一
- PER-006 佐伯玲子
- EVT-011〜013で共有済みの16素子 / 3記憶 / Q
- ORG-001の紙上計算環境

## World before

EVT-013までに、Qはstableであり、その局所入力が三つの保存パターンとの重なりから説明できた。しかし二人はQそのものを初期状態として置いただけであり、Q以外からQへ到達できるかは未確認。

高橋の局所目標は、basin全体や頻度を語る前に、Qの最小近傍から実際に戻れるかを見ること。佐伯の局所目標は、初期状態と更新順序を結果前に固定し、成功例だけを選ばないこと。

## Story-visible action selection

最初のfollow-upでは全 `2^16` 状態を列挙しない。QからHamming距離1にある16状態だけを完全に含める。

更新順序について、16!通りの全順列を扱わず、`1,2,...,16` の巡回回転16本を結果前に固定する。これは頻度推定ではなく、各unitを一度ずつ先頭にする有限のschedule familyで、EVT-005の考え方を16素子へ拡張したもの。

したがってtrial集合は `16 initial states × 16 cyclic orders = 256` 件。

紙上で完全追跡可能ではあるが反復量が大きい。今回のeventではまず条件と結果を成立させ、計算資源の具体SYS/OBJ化は、人物が実際に共用計算機を使うsceneが必要になった時点まで保留する。作者側再現はexact integer arithmeticで行う。

---

# ACTION LOCK

## Fixed model

EVT-011のM1/M2/M3/QとHebbian結合を変更しない。

## Initial states

Qの16成分について、ちょうど1成分だけ符号反転した16状態 `Q^(k)` (`k=1..16`) をすべて含める。

除外・追加なし。

## Update schedules

基準順序 `1,2,...,16` と、その巡回回転16本をすべて含める。

例:

- r1 = 1,2,...,16
- r2 = 2,3,...,16,1
- ...
- r16 = 16,1,...,15

## Update rule

各unitを一つずつ非同期に更新する。

`h_i = Σ_j T_ij s_j`

- `h_i > 0` → `+1`
- `h_i < 0` → `-1`
- `h_i = 0` → 現在値を保持

一巡の前後で状態が同じなら停止。最大100巡。100巡で停止しなければ`NONCONVERGED`。

## Recorded outputs

256 trialすべてについて少なくとも、

- initial flipped position
- cyclic order
- final state
- Qへ到達したか
- convergence sweeps

を記録する。

集計として、

- Q到達trial数 / 256
- 16 initial statesのうち全16 orderでQへ行く数
- orderによりQ到達可否が変わるinitial state数
- Q以外のfinal state集合
- nonconverged数

を記録する。

## Predeclared interpretation

この検査はQの**Hamming距離1近傍 × 16 cyclic schedules**だけを扱う。

`PASS` / `FAIL`という単一の成功判定は置かない。結果を次の観測カテゴリで記録する。

- `ROBUST_LOCAL_ATTRACTION`: 256/256でQへ到達
- `ORDER_DEPENDENT_LOCAL_ATTRACTION`: Qへ行くtrialと行かないtrialが混在
- `NO_LOCAL_RETURN_IN_FAMILY`: 0/256でQへ到達
- `MIXED_WITH_NONCONVERGENCE`: nonconvergedを含み上記だけでは記述できない

いずれの結果でも、全state-space basin size、random-start probability、人間の記憶、一般のHopfield networkへ一般化しない。

## Stopping rule

256件をすべて実行し、結果後にinitial state / orderを追加・削除しない。集計が完成した時点でEVT-014をresolveする。
