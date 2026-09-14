# EVT-018 巡回順の件数は4点の隙間で決まる

状態: `RESOLVED / PROVISIONAL`

Resolution provenance: `LOCK_NOT_REQUIRED`

## Story time

`T0-1980S + deterministic counting after EVT-017`

## Timeline position

- Parent: `EVT-017`
- Previous event: `EVT-017`
- Next event: 未成立

## Why no action lock

EVT-017で確定した12個のunstable setsと、EVT-014で最初から固定されていた16 cyclic ordersを、追加simulationなしで数え直すだけである。

新pattern、schedule、candidate、parameterを選ばないため結果選択を防ぐ新ACTION LOCKは不要。

## World before

EVT-017では各split one-bit initial stateについて、initially unstableな4 unitがminority stored patternとQのdifference set `D(k)`そのものだと分かった。

EVT-016では、4候補のうちdamaged coordinate kが最初に実flipすればQ、他3のどれかが先ならminority memoryへ行った。

したがって16 cyclic ordersでQへ戻る本数は、「巡回順の開始点から見てkがD(k)中の最初のunitになる開始点が何個あるか」だけで数えられる。

## Deterministic count

16 unitを円周上に`1,2,...,16`と並べる。

4点集合Dを昇順に並べ、あるkの直前にあるDの要素を`p(k)`とする。16→1をまたぐ場合も円周として数える。

kがD中で最初に現れるcyclic startは、`p(k)`の次からkまでのstart位置である。

したがってQ-return countは円周gap

```text
g(k) = (k - p(k)) mod 16
```

ただし値域は1〜16とする。

## M3 group

```text
D = {3,4,5,6}
```

gaps:

```text
k=3: previous=6, wrap gap=13
k=4: gap=1
k=5: gap=1
k=6: gap=1
```

予測Q counts:

```text
13,1,1,1
```

EVT-014 observed countsと完全一致。

## M2 group

```text
D = {9,11,12,15}
```

gaps:

```text
k=9 : previous=15, wrap gap=10
k=11: gap=2
k=12: gap=1
k=15: gap=3
```

予測:

```text
10,2,1,3
```

EVT-014と完全一致。

## M1 group

```text
D = {10,13,14,16}
```

gaps:

```text
k=10: previous=16, wrap gap=10
k=13: gap=3
k=14: gap=1
k=16: gap=2
```

予測:

```text
10,3,1,2
```

EVT-014と完全一致。

## Aggregate

3 groupのgap合計はそれぞれ16なので、Q-returnは

```text
16 + 16 + 16 = 48
```

split 192 trial中、残り

```text
192 - 48 = 144
```

がminority memory branch。

EVT-016のfirst-flip集計48/144をsimulation結果からではなく、4点集合の円周配置だけで再現した。

unanimity positions 1,2,7,8の64 trialはEVT-014で全Qなので、全256 trialでは

```text
Q = 64 + 48 = 112
stored = 144
```

となり、EVT-014 aggregate `Q=112, M1=M2=M3=48`も再現する。

## Resolved consequence

この固定exampleと固定cyclic schedule familyでは、256 trajectoryのaggregateは最終的に、

```text
three stored patternsのcomponent structure
→ Qと各minority memoryの4-bit difference sets
→ initial unstable sets
→ 4点のcircular gaps
→ cyclic order counts
```

だけで説明できる。

これは「43.75%という自然確率」を意味しない。むしろ逆で、112/256という比率が**人工的に選んだcyclic schedule familyと4点の配置から組合せ的に決まった値**だと明確になった。

## Persona deltas

### PER-005 高橋修一

Beliefs:

- 256 trialのaggregateはこの例ではsimulation固有の不可解な頻度ではなく、4点の円周gapへ還元できる
- 更新順依存を理解するには「何通り試したか」より、schedule familyの構造を明示する必要がある

Goals:

- この局所問題については追加trialを増やさず、何がexample固有で何が一般的な力学かを整理する
- 次に計算を広げるなら、目的を明示して共用計算資源を使う

### PER-006 佐伯玲子

Beliefs:

- 43.75%を確率と呼ばない理由が、単なる注意書きではなく構成から説明できた
- schedule designが観測頻度そのものを作る場合がある

Goals:

- 以後、trial fractionを提示するときはsampling / schedule constructionを同時に記録する
- このexampleの局所説明を一度閉じ、必要なら別の問いへ移る

## Organization / world delta

ORG-001変更なし。

今回の結果は追加計算機利用を必要としない。むしろ既存256 trialの多くが組合せ的に圧縮できた。

## Structure impact

EVT-014〜018で一つのreading unitが自然に閉じた。

```text
stable Qは近傍から戻れるか
→ one-bit近傍でorder-dependent
→ minority memoryだけが近づく
→ first actual flipがbranchを分ける
→ initial unstable setは4-bit difference set
→ cyclic countsは4点のgapだけで再現
```

この範囲は第5話候補としてNarrativeProjection可能。

## Generation validation

- 新trialなし
- EVT-014〜017の成立済みfactsだけを決定的に再分類
- 112/256を自然確率へ一般化せず、schedule-family依存をむしろ明示
- 作者側EXP-006〜011を人物Knowledgeへ使用していない
