# EVT-007 小さい系なら全状態を見る

状態: `RESOLVED / PROVISIONAL`

Resolution provenance: `LOCKED`

Action-lock commit: `3c1034c70853c5704d4064f71ef4e989b4dc296f`

Resolution table: `EVT-007-state-space.csv`

## Story time

`T0-1980S + exhaustive small-state check after EVT-006`

## Timeline position

- Parent: `EVT-006`
- Previous event: `EVT-006`
- Next event: 未成立

## Participants

- PER-005
- PER-006

新しい独立主体は、このactionの選択・実行には必要なかった。

## World before

- 6-unit / 3-stored-patternのtoy networkが成立している
- EVT-006でA/B-balanced cue全6種類 × 6 cyclic update ordersを結果前に固定して全36 trialを確認した
- pairwiseなA/B等距離cueでも、第三stored pattern Cやnonstored fixed point Dとの関係が入ることを二人が観測した
- PER-005はpairwiseな曖昧さとnetwork全体のbasin構造を混同しないことを局所目標にしている
- PER-006はselected pairだけでなくstored set全体との関係を先に記録し、initial fixedとdynamical returnを分けることを要求している
- 現代側EXP-003〜005の結果は二人のKnowledgeではない

## Action selection rule

このeventでは、結果を知らずに次のactionを選ぶため、story-visibleな現在状態だけを使った。

現在のtoy networkは6 unitなので、binary state space全体は

```text
2^6 = 64 states
```

しかない。

EVT-006で「A/Bの間」という部分集合の選び方自体がnetwork全体の関係を隠し得ると分かったため、PER-005 / PER-006は**新しいcueを選ぶのではなく、現在の6-unit networkの全initial statesを列挙する**ことを選んだ。

このactionの選択は、特定のattractorや面白いoutcomeを探すことを目的にしない。

目的は、現在の小さい系についてsamplingをやめ、

- どのinitial stateがすでにfixed pointか
- 各initial stateが既存6 cyclic update ordersでどこへ到達するか
- stored patterns以外のstable stateが何種類あるか
- update orderによってbasin assignmentが変わるstateがどれだけあるか

を全件記録すること。

---

# ACTION LOCK

以下は結果解決前にcommit `3c1034c70853c5704d4064f71ef4e989b4dc296f` で固定した。

## Locked network

```text
A = (-1, +1, +1, +1, -1, -1)
B = (+1, -1, +1, -1, -1, +1)
C = (-1, -1, -1, -1, +1, -1)
```

weights:

- 3 stored patternsのHebbian outer-product和
- self connection = 0
- 全体の正のscaleは用いない

unit update:

- asynchronous
- local field > 0 -> +1
- local field < 0 -> -1
- local field = 0 -> current valueを保持

## Locked initial-state set

全binary stateを使う。

```text
S = {-1,+1}^6
|S| = 64
```

列挙順はunit 1を最上位、unit 6を最下位とし、`-1 < +1` の辞書順とする。

結果を見てstateを追加・削除しない。

## Locked update-order set

EVT-005 / EVT-006と同じ6 cyclic rotationsを使う。

```text
r1 = (1,2,3,4,5,6)
r2 = (2,3,4,5,6,1)
r3 = (3,4,5,6,1,2)
r4 = (4,5,6,1,2,3)
r5 = (5,6,1,2,3,4)
r6 = (6,1,2,3,4,5)
```

## Locked trial set

```text
64 initial states x 6 cyclic orders = 384 trials
```

384 trialをすべて含める。

## Locked stopping rule

1. 指定orderを1 sweepとして繰り返す
2. sweep終了時にstateがsweep開始時と同一ならstableとして停止
3. 最大20 sweeps
4. 20 sweepsでstableでなければ`NONCONVERGED`

## Locked records

各initial stateについて最低限、

- initial state
- A / B / CへのHamming distance
- initial stateがfixed pointか
- r1〜r6それぞれのfinal state
- 各runのsweeps
- final stateがA / B / C / nonstoredのどれか

を記録する。

全trial集計として、

- unique stable final states
- orderごとのbasin size
- initial stateごとのdistinct final count
- 6 ordersで同じfinalになるstate数
- 2種類以上のfinalへ分岐するstate数
- NONCONVERGED数

を記録する。

## Locked inclusion / exclusion rule

- 384 trialをすべて含める
- stored patternへ行かないstateを除外しない
- update orderで結果が変わらないstateも除外しない
- initial fixed stateも除外しない
- outcomeを見てinitial-state集合、order集合、stopping ruleを変更しない
- outcomeを見た後に追加のorderや別networkをこのeventへ足さない

## Locked interpretation boundary

このeventで言えるのは、この6-unit toy networkと固定した6 cyclic ordersの全状態遷移についてだけである。

- 生物学的memoryへ一般化しない
- 大規模Hopfield networkの一般的basin構造へ一般化しない
- 現代EXP-003〜005の結果を人物へ与えない
- 望ましい章末や研究結論に合うようoutcomeを選別しない

---

# RESOLUTION

Action lock後、locked network / 64 initial states / 6 cyclic orders / stopping ruleを変更せず384 trialすべてを解決した。

row-level結果は `EVT-007-state-space.csv` に保存した。

## Convergence

```text
TOTAL_TRIALS       384
CONVERGED           384
NONCONVERGED          0
MAX_SWEEPS             2
```

全trialが2 sweeps以内にstableになった。

## Initial fixed points

64 initial statesのうち、最初からfixed pointだったstateは6個だけだった。

```text
C  = (-1,-1,-1,-1,+1,-1)
-B = (-1,+1,-1,+1,+1,-1)
A  = (-1,+1,+1,+1,-1,-1)
-A = (+1,-1,-1,-1,+1,+1)
B  = (+1,-1,+1,-1,-1,+1)
-C = (+1,+1,+1,+1,-1,+1)
```

重要な再分類:

EVT-005 / EVT-006で `D` と呼んでいた

```text
D = (+1,+1,+1,+1,-1,+1)
```

は、

```text
D = -C
```

だった。

したがってDは「stored patternではないfixed point」という観測自体は正しいが、このtoy networkでは任意の未知spurious stateではなく、保存pattern Cの全符号反転である。

同様に、全状態列挙では `-A` と `-B` もfixed pointとして現れた。

## Unique stable final states

384 trialのfinal stateは、この6種類だけだった。

```text
A, B, C, -A, -B, -C
```

この全状態列挙では、これ以外のstable final stateは現れなかった。

## Basin size by update order

64 initial statesを各orderで一度ずつ数えたbasin size:

| order | A | B | C | -A | -B | -C |
|---|---:|---:|---:|---:|---:|---:|
| r1 | 10 | 10 | 12 | 10 | 10 | 12 |
| r2 | 10 | 12 | 10 | 10 | 12 | 10 |
| r3 | 10 | 12 | 10 | 10 | 12 | 10 |
| r4 | 10 | 12 | 10 | 10 | 12 | 10 |
| r5 | 12 | 10 | 10 | 12 | 10 | 10 |
| r6 | 10 | 10 | 12 | 10 | 10 | 12 |

全384 trialを合計すると:

```text
A   62
B   66
C   64
-A  62
-B  66
-C  64
```

各stored patternとその符号反転は、今回の6 order集合では同じ総basin countを持った。

## Update-order dependence across initial states

64 initial statesのうち:

```text
6 ordersすべてで同じfinal      18
2種類以上のfinalへ分岐          46
```

initial stateごとのdistinct final count:

```text
1 final : 18 states
2 finals: 16 states
3 finals: 22 states
4 finals:  4 states
5 finals:  4 states
6 finals:  0 states
```

したがって、このtoy networkでは多くのinitial stateでupdate orderがbasin assignmentへ影響した。

ただしこの比率を一般的なHopfield networkの頻度とは扱わない。

## Resolved consequence

- pairwise balanced cueだけでなく全64 initial statesを調べても、update order依存は広く残った
- stable final stateはA/B/Cだけではなく、その全符号反転 `-A/-B/-C` を含む6種類だった
- これまでnonstored Dとして扱っていたstateは `-C` だった
- このtoy networkでは、全状態列挙の範囲でA/B/Cおよびその符号反転以外のstable final stateは見つからなかった
- `stored / nonstored` だけの分類では、符号反転対称性という構造を隠してしまう
- 「A/Bの間」というpairwise表現を捨て、network全体のstate spaceを見たことで、前の分類自体を修正する必要が生じた

## Persona deltas

### PER-005

Beliefs:

- Dは独立した未知の形ではなく、Cをすべて反転した `-C` だった
- stored patternの一覧だけを見ると、networkの対称なfixed pointを「保存していない別物」と一括してしまう
- stateの意味を考える前に、weight ruleが作る対称性を確認する必要がある
- update orderは64 statesの多くで到達先へ影響するが、このtoy networkの有限結果を一般頻度へ広げない

Goals:

- なぜA/B/Cの符号反転もfixed pointになるのか、weight/update ruleから説明する
- `antipattern`的な対称stateと、mixture等の別種のnonstored stateを区別する
- 大きなnetworkでも同じ分類上の問題が起きるかを、物語側の観測と現代側研究を混同せず考える

Memory:

- 全64 initial states × 6 ordersの結果を保持する
- fixed pointがA/B/C/-A/-B/-Cの6種類だったことを保持する
- D = -Cだったことを保持する

PER-005は共同記録に、

> 保存していない、だけでは足りない。
>
> Cを裏返したものまで、別の記憶と呼んでいた。

と記す。

### PER-006

Beliefs:

- `nonstored stable`は観測カテゴリとしては正しいが、機構の異なるstateをまとめる粗い分類である
- Dを生物学的memoryや第三の原像と呼ばず、まず`-C`というmodel上の関係として記述すべき
- selected cueだけを見るより、有限ならstate space全体を調べる方が分類の混同を発見しやすい

Goals:

- 今後nonstored stateを扱う際、stored patternの符号反転・mixture・その他を区別できるか確認する
- model対称性による結果と、生物学的memoryについての主張を分離する

Memory:

- D = -Cであること
- 6 fixed pointsと全384 trialの集計
- 46/64 initial statesでorderによるfinalの分岐があったこと

## World delta

共同記録に次が追加された。

- 全64 initial states × 6 cyclic ordersの384 trial
- 6 fixed points `A/B/C/-A/-B/-C`
- D = -Cという再分類
- order別basin size
- 18 statesはorder-invariant、46 statesはorder-dependentという有限集計

具体的な機種名・programming language・所属機関はまだ固定しない。

384 trialの機械的な列挙は、BOOT-002で既に許容している簡略network計算手段の範囲で解決した。具体実装環境が物語上の因果へ影響する段階までは機種をCanon固定しない。

## Who observed what

- PER-005 / PER-006: lockedした全state/order集合、全結果、D=-Cの関係、basin集計
- 他ペルソナ: 未観測
- 現代側persona: 自動的には未観測

## Research branch after resolution

このeventから即座に次EXPを自動生成しない。

ただし、人物側で新しく明示された

> `nonstored stable`のうち、stored patternの単純な符号反転として説明できるstateを分離すべきではないか

という問題は、既存EXP-002 / EXP-003の`NONSTORED_CONVERGED`分類の解釈に直接関係する。

現実側で検証可能な問いへ落とす場合、既存trial群のnonstored finalがstored patternのexact negationと一致する件数を監査する研究候補になる。

判定対象がEXP-003のmixture exact matchとは異なるため、実行する場合は新しいQ / H / EXPとして分離する。

## Structure impact

EVT-007で崩れたのは、単に「戻り先が複数ある」という前提だけではない。

`stored / nonstored`という二分類自体が、このtoy networkの対称性を隠していたことが分かった。

現在の局所的な`転`はさらに深まり、次の問いは

> 保存していない状態とは、本当に一種類の「別物」なのか。

へ移った。

これを第2話の章末や`結`として先に固定しない。

## Generation validation

- action selectionはEVT-006後のstory-visibleなGoalと有限state-space sizeだけから定義した
- initial-state集合は64状態の全列挙であり、outcome-sensitiveな選択余地を残していない
- update orders / stopping / inclusion ruleはaction-lock commitで固定済み
- 384 trialを結果選別せず全て受理した

Test-004の成功条件は「面白い結果」が出ることではなく、locked actionのoutcomeをそのまま物語へ返すことだった。この条件は満たした。

ただし、同じ生成contextがaction selection ruleを書いているため、別contextによるselector isolationそのものは依然として未検証とする。
