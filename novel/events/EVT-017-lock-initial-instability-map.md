# EVT-017 分岐前の不安定unit集合を固定して調べる

状態: `ACTION_LOCKED`

Resolution provenance: `LOCKED`

## Story time

`T0-1980S + local-field mechanism check after EVT-016`

## Timeline position

- Parent: `EVT-016`
- Previous event: `EVT-016`
- Next event: 未成立

## Resolution scope

- PER-005 高橋修一
- PER-006 佐伯玲子
- EVT-011のM1/M2/M3/Q / Hebbian weights
- EVT-014〜016で扱った12個のsplit one-bit initial states

作者側EXP-006以降はscope外。

## World before

EVT-016では192 trialのfinalがfirst actual flip categoryで完全分離した。

- damaged coordinate k が最初にrepair → Q
- k以外が最初にflip → coordinate-minority stored pattern

ただし、なぜ最初の状態でその競争が存在するかは未説明。

## ACTION LOCK

各split coordinate kについて、Qのkだけを反転したinitial state `s^(k)` を作る。

**更新を一度も行う前に**全16 unitのlocal fieldを計算する。

各unit iを次で分類する。

- `FLIP_IF_UPDATED`: local fieldが現在bitと反対符号で、今更新すれば実flipする
- `HOLD_TIE`: local field 0
- `STAY`: 現在bitと同符号

各kについて同時に、coordinate-minority stored pattern `M(k)` がQと異なる4 coordinateの集合 `D(k)` を記録する。kはその4個の一つ。

## Predeclared comparisons

1. `FLIP_IF_UPDATED`集合にkが含まれるか
2. `D(k) \ {k}` の3 coordinateが何個`FLIP_IF_UPDATED`に含まれるか
3. `D(k)`外で`FLIP_IF_UPDATED`なunitがあるか
4. initial instability mapだけでEVT-016のfirst-flip competitionを説明できるか

## Outcome categories

- `FOUR_WAY_COMPETITION`: 全12 initial statesで`FLIP_IF_UPDATED = D(k)`。kを更新すればrepair、他3を更新すればminority側への最初のflipとなる
- `PARTIAL_COMPETITION`: unstable setはD(k)の部分集合/関連集合だが完全一致しない
- `EXTRA_INSTABILITY`: D(k)外のunitもinitially unstable
- `NO_STATIC_EXPLANATION`: initial field分類ではEVT-016を説明できない

## Stopping

12 initial states × 16 local fieldsを全件計算して停止。結果後に別状態や別patternを追加しない。

## Generation validation

- EVT-016後のpersona goalから直接生じる
- trajectory finalを選ばず12 initial statesを全件扱う
- 作者側一般proofを使わず、この16-unit掲載例のinitial local fieldsだけを計算する
