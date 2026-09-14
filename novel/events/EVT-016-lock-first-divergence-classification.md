# EVT-016 最初の実bit flipが分岐を分ける

状態: `RESOLVED / PROVISIONAL`

Resolution provenance: `LOCKED`

Action-lock commit: `a1677e110a7be35fcb5068484a4de4b395770230`

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

EVT-015では、initial geometryとしてminority memoryだけがQからdistance 4→3へ近づくことを確認した。しかし「更新順のどこで分岐が決まるか」は未説明だった。

## Locked classification

commit `a1677e110a7be35fcb5068484a4de4b395770230` で、192 trial全件について最初の実bit flipを次のcategoryへ固定分類した。

- `REPAIR_K_FIRST`: 最初の実flipが壊したcoordinate kをQへ戻す
- `OTHER_FLIP_FIRST`: k以外のunitが最初にQから離れる方向へflip
- `NO_FLIP_FIRST_SWEEP`
- `OTHER`

同時にfirst-flip unit / update位置 / final / 総実flip数を記録する規則を結果前固定した。

## Resolution

192 trial全件を同一規則で再計算した。

### First-flip category × final

| first actual flip | final Q | final minority memory | other | total |
|---|---:|---:|---:|---:|
| `REPAIR_K_FIRST` | 48 | 0 | 0 | 48 |
| `OTHER_FLIP_FIRST` | 0 | 144 | 0 | 144 |
| other categories | 0 | 0 | 0 | 0 |

**192 / 192で完全分離**した。

Predeclared outcome: `FIRST_FLIP_SEPARATES`。

### Total actual flips

- `REPAIR_K_FIRST → Q`: 48 / 48 trialで実flipは**1回だけ**
- `OTHER_FLIP_FIRST → minority memory`: 144 / 144 trialで実flipは**3回**

後者ではinitial stateですでにminority memoryとの差の4 bitのうち1 bitが揃っている。さらに3 bitがflipし、stored patternへ一致する。

### By coordinate

EVT-014のfinal集計と同じ比率がfirst-flip分類として再現された。

例:

- k=3: repair first 13 / other first 3
- k=4,5,6: repair first 1 / other first 15
- k=9,10: repair first 10 / other first 6
- k=14: repair first 1 / other first 15

全12 coordinateで、repair-first件数がそのままQ final件数に一致した。

## Resolved consequence

この具体的16-unit exampleの固定192 trialでは、order dependenceは最終結果を直接見なくても、**最初に実際にどのbitが動くか**まで縮約できた。

```text
壊したbit k が最初に修復
→ その後に実flipなし
→ Q

別unitが先にQから離れる
→ 合計3回の実flip
→ kでminorityだったstored memory
```

したがって「更新順そのもの」が魔法のようにfinalを決めるのではなく、更新順が**最初の有効な状態変化の競争**を決め、その最初の変化がこの例ではbranchを完全分離している。

ただし今回確認したのは、

- 1983掲載16-unit example
- split one-bit initial states
- 16 cyclic orders

だけである。一般のnetwork / order family / perturbation sizeへ自動一般化しない。

## Persona deltas

### PER-005 高橋修一

Beliefs:

- 今回のorder dependenceは、192 trialでは「最初の実flip」の競争へ縮められる
- damaged bitが先に戻ればQで終わり、別bitが先に動けばstored memory側へcascadeする
- 5/21 margin、distance 3/5、first-flip competitionが一つの局所構造として接続し始めた

Goals:

- なぜ別unitが先にflipすると残り2 bitまで同じstored pattern側へ続くのか、固定例の局所入力から説明できるか調べる
- 192件の経験則を一般法則とは呼ばない

Memory:

- 48 repair-first→Q
- 144 other-first→minority
- flip count 1 vs 3

### PER-006 佐伯玲子

Beliefs:

- finalだけでなく最初の実変化を記録すると、order dependenceの記述が大幅に単純化した
- 「順番が違うから違う結果」より「最初にどの変化が許されたか」の方が操作的に明確

Goals:

- first-flip分類を結果後の都合よい説明へ変えないため、今回の192件全件一致をそのまま限定して保存する
- 次に解析する場合も、具体例のどこまでが証明可能かと一般化を分離する

## Organization / world delta

ORG-001 governance変更なし。

192 trajectoryのunit-level traceは紙上で不可能ではないが反復量が大きい。本文でこの作業sceneを具体化する場合、共用計算資源の利用をresolution scopeへ入れる合理性が高まった。

まだ具体machine / OS / languageはCanon固定しない。

## Fact level

- local story fact: first-flip classificationと192/192完全分離をPER-005 / PER-006が共有
- institutional fact: 未成立
- public story fact: 未成立
- canon fact: 未昇格

## Research branch

このeventだけから新しい作者側EXPを人物へ返さない。

作者側では既に別系列の一般研究が存在するが、人物Knowledgeへ流入させない。

## Structure impact

EVT-014〜016で、

```text
Qは近傍から到達可能だがorder-dependent
→ どのbitを壊したかで競合memoryが変わる
→ order dependenceはfirst actual flipの競争へ縮約
```

という一つの局所的認識遷移が成立した。

自然なreading unit候補になり得るが、chapter化は成立済みeventだけから別途判定する。

## Generation validation

- classification ruleは結果計算前commit済み
- 192 trial全件使用
- 作者側EXP-006〜011 / proofを人物へ使用していない
- complete separationを一般定理へ昇格していない
