# EVT-015 反転した一ビットが少数派の記憶を近づける

状態: `RESOLVED / PROVISIONAL`

Resolution provenance: `LOCK_NOT_REQUIRED`

## Story time

`T0-1980S + immediate classification after EVT-014`

## Timeline position

- Parent: `EVT-014`
- Previous event: `EVT-014`
- Next event: 未成立

## Why no action lock

EVT-014で固定・完了した16個の一ビット近傍と、EVT-012で既に確定したQ/M1/M2/M3の成分関係を、追加trialなしで決定的に再分類するだけである。

新しいinitial state、schedule、parameter、候補patternを選ばない。したがって結果選択を防ぐための新しいACTION LOCKは不要。

## World before

EVT-014では、Qの一ビット近傍16状態 × 16 cyclic ordersの256 trial中112件がQへ戻り、残り144件はM1/M2/M3へ各48件ずつ到達した。

全員一致4位置を反転した場合は16/16 orderでQへ戻った。2対1の12位置を反転した場合はorder-dependentで、Qへ戻らないtrialはその位置の少数派stored patternへだけ到達した。

## Classification

EVT-012で、QはM1/M2/M3の各々からHamming距離4だった。

### 2対1位置を反転する場合

ある位置kで、二つのstored patternがQと同符号、一つだけがQと反対符号だとする。その反対側の一つを`minority memory`と呼ぶ。

Qのkだけを反転すると、

- minority memoryとは、その位置が「不一致 → 一致」になるため距離 `4 -> 3`
- 残る二つとは、その位置が「一致 → 不一致」になるため距離 `4 -> 5`

したがって、その一ビット反転状態は三つのstored patternsのうち**少数派memoryに一意に最も近い**。

同じことをoverlapで書けば、Qでは三つともoverlap 8だったものが、

- minority memory: `8 -> 10`
- majority側の二つ: `8 -> 6`

となる。

### 全員一致位置を反転する場合

三つすべてがQと同符号だった位置を反転すると、三つすべてについて

- distance `4 -> 5`
- overlap `8 -> 6`

となる。

したがって特定のstored patternだけを近づけない。

## Resolved consequence

EVT-014のescape先が少数派memoryだけだったことには、少なくとも明確な幾何学的対応がある。

```text
2対1位置をQから反転
→ その位置の少数派memoryだけが distance 3
→ 他二つは distance 5
→ EVT-014でQへ戻らないtrialは、その少数派memoryへ到達
```

一方、全員一致位置の反転では三つへの距離はすべて5のままで、今回の16 cyclic ordersでは全trialがQへ戻った。

ただし、**nearest stored patternであることだけから非同期力学のfinalを一般に決定できるとは主張しない**。EVT-014自体がorder dependenceを示している。ここで説明できたのは、なぜ2対1位置の反転が特定のstored patternとの競合方向を作るのか、という初期状態の幾何学である。

## Persona deltas

### PER-005 高橋修一

Beliefs:

- 5/21というstability marginの違いと、Q近傍でどのstored patternが競合するかは、同じ三patternの成分構造から読める
- 2対1位置を反転すると、その位置の少数派memoryが距離3まで近づく
- ただし距離だけでfinalを決めることはできず、更新順序の力学は残る

Goals:

- 「近いから戻る」と「力学がそこへ運ぶ」を再び混同しない
- 次に進むなら、全state-space basinへ広げる前に、今回のorder dependenceをどこまで解析的に説明できるかを見る

### PER-006 佐伯玲子

Beliefs:

- EVT-014のpost-hoc observationは、少なくとも距離とoverlapの変化として再記述できる
- Qの局所近傍は一様な球ではなく、どの成分を壊すかでstored patternsとの関係が変わる

Goals:

- 「Qから距離1」という一語で16初期状態を同質扱いしない
- 距離の説明と実際の到達結果を別欄で保持する

## Organization / world delta

ORG-001の変更なし。追加計算資源なし。

Fact level:

- local story fact: 上記distance / overlap分類をPER-005 / PER-006が共有
- institutional fact: 未成立
- canon fact: 未昇格

## Interesting finding

今回の系列で初めて、EVT-013の`5 / 21`、EVT-014の局所到達性、EVT-015の`distance 3 / 5`が同じ成分構造へ接続した。

```text
stored patternsが全員一致する位置
→ Qのmargin 21
→ 1-bit flip後も三stored memoriesは等距離5
→ 今回の16 cyclic ordersでは16/16でQへ復帰

stored patternsが2対1の位置
→ Qのmargin 5
→ flipすると少数派memoryだけ距離3、他二つは5
→ 今回はorderによりQまたは少数派memoryへ分岐
```

これはこの掲載例に対する説明であり、一般定理ではない。

## Generation validation

- EVT-014の全結果を見た後の分類であることを明記
- post-hoc observationを事前仮説へ偽装していない
- 新trialを追加していない
- nearest-memory heuristicを一般的なdynamics lawへ昇格させていない
