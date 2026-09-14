# EVT-017 分岐前から4つの不安定unitが競合する

状態: `RESOLVED / PROVISIONAL`

Resolution provenance: `LOCKED`

Action-lock commit: `f9450660a103c9b033519d17e9bc874dc96cdf5c`

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

## Locked classification

各split coordinate kについて、Qのkだけを反転したinitial stateで、更新前に全16 local fieldsを計算する。

各unitを、

- `FLIP_IF_UPDATED`
- `HOLD_TIE`
- `STAY`

へ分類し、coordinate-minority stored patternがQと異なる4-coordinate集合`D(k)`と比較する規則を結果前に固定した。

## Resolution

12 initial states × 16 fieldsを全件計算した。

結果は12 / 12で、

```text
FLIP_IF_UPDATED = D(k)
```

だった。

`HOLD_TIE`は全件0。`D(k)`外のextra unstable unitも0。

Predeclared outcome: **`FOUR_WAY_COMPETITION`**。

### Difference sets

minority memoryごとにD(k)は次の4位置。

```text
M3 minority group: {3,4,5,6}
M2 minority group: {9,11,12,15}
M1 minority group: {10,13,14,16}
```

たとえばk=3を反転したinitial stateでは、不安定なのは3,4,5,6だけ。

- unit 3を先に更新すれば、壊したbitがQへrepairする方向
- unit 4/5/6のどれかを先に更新すれば、M3へ近づく方向

になる。

同じ構造が残る11 initial statesでも成立した。

## Local-field examples

k=3 initial stateのunstable fields:

```text
unit 3: +5   # currentは-Q側なのでrepair方向
unit 4: -1
unit 5: +1
unit 6: +1
```

k=14では、unstable setは`{10,13,14,16}`で、

```text
unit 10: +1
unit 13: -1
unit 14: -5  # damaged coordinateのrepair方向
unit 16: -1
```

となる。

絶対値は同じではないが、**今更新すればflipする候補が4つ同時に存在する**点は共通する。

## Resolved consequence

EVT-016のfirst-flip separationは、trajectoryを走らせる前のlocal fieldだけでも説明できる。

```text
split one-bit initial state
→ ちょうど4 unitがinitially unstable
→ その4 unitはminority stored patternとQが異なる4位置そのもの
→ damaged k が最初ならrepair branch
→ 他3のどれかが最初ならminority branch
```

したがってこの具体例では、order dependenceの源は「16 unit全部の複雑な順序」ではなく、**4つの不安定候補の相対的な先着順**へ縮約された。

これはEVT-016の192 trialを結果後に説明するための固定例解析であり、一般定理ではない。

## Persona deltas

### PER-005 高橋修一

Beliefs:

- order dependenceの有効自由度は16!のような全順序ではなく、今回の初期状態では4つのunstable unitの先着競争に縮められる
- minority memoryの4-bit difference setが、そのままinitial instability setとして現れる

Goals:

- cyclic order 16本で観測したQ/minority件数が、この4点の円周上の並びだけから計算できるか確認する
- 計算できるなら192 trajectoryを個別に追わず、combinatorialに説明する

### PER-006 佐伯玲子

Beliefs:

- first-flip分類が完全分離した理由を、更新前の観測量として記述できた
- 「順序依存」という語だけでは粗く、実際には候補unit集合と先着関係が必要

Goals:

- cyclic schedule family固有の数え上げと、network dynamics一般を分離する
- 16本という人工的なschedule familyの比率を自然確率と呼ばない

## Organization / world delta

変更なし。

今回の12×16 field表は有限で、紙上でも検算可能。共用計算機の具体化は引き続き未確定。

## Fact level

- local story fact: 12 / 12で`FLIP_IF_UPDATED=D(k)`をPER-005/PER-006が共有
- institutional / public / canon fact: 未成立

## Structure impact

EVT-014〜017は、accessibility→geometry→first flip→initial instabilityという連続した局所説明になった。

次に自然に残る問いは、cyclic orderで得た13/3、1/15、10/6等の件数を、4 unstable positionsの配置から計算だけで再現できるか。

## Generation validation

- 12 initial statesを全件使用
- field分類を結果前に固定
- 作者側一般proofを人物へ使用していない
- fixed exampleの完全一致を一般networkへ一般化していない
