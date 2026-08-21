# EVT-007 小さい系なら全状態を見る

状態: `ACTION_LOCKED / PROVISIONAL`

Resolution provenance: `LOCKED_PENDING`

## Story time

`T0-1980S + exhaustive small-state check after EVT-006`

## Timeline position

- Parent: `EVT-006`
- Previous event: `EVT-006`
- Next event: 未成立

## Participants

- PER-005
- PER-006

新しい独立主体は、このactionの選択・実行には必要ない。

## World before

- 6-unit / 3-stored-patternのtoy networkが成立している
- EVT-006でA/B-balanced cue全6種類 × 6 cyclic update ordersを結果前に固定して全36 trialを確認した
- pairwiseなA/B等距離cueでも、第三stored pattern Cやnonstored fixed point Dとの関係が入ることを二人が観測した
- PER-005はpairwiseな曖昧さとnetwork全体のbasin構造を混同しないことを局所目標にしている
- PER-006はselected pairだけでなくstored set全体との関係を先に記録し、initial fixedとdynamical returnを分けることを要求している
- 現代側EXP-003〜005の結果は二人のKnowledgeではない

## Action selection rule

このeventでは、結果を知らずに次のactionを選ぶため、story-visibleな現在状態だけを使う。

現在のtoy networkは6 unitなので、binary state space全体は

```text
2^6 = 64 states
```

しかない。

EVT-006で「A/Bの間」という部分集合の選び方自体がnetwork全体の関係を隠し得ると分かったため、PER-005 / PER-006は**新しいcueを選ぶのではなく、現在の6-unit networkの全initial statesを列挙する**。

このactionの選択は、特定のattractorや面白いoutcomeを探すことを目的にしない。

目的は、現在の小さい系についてsamplingをやめ、

- どのinitial stateがすでにfixed pointか
- 各initial stateが既存6 cyclic update ordersでどこへ到達するか
- stored patterns以外のstable stateが何種類あるか
- update orderによってbasin assignmentが変わるstateがどれだけあるか

を全件記録すること。

---

# ACTION LOCK

以下を結果解決前に固定する。

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

## Resolution procedure

このcommit後に、locked network / 64 states / 6 orders / stopping ruleを機械的に解決する。

どのoutcomeが出ても、条件を差し替えず全結果を受理する。

## Generation validation purpose

このeventは、Test-004として次を確認するためにも使う。

- EVT-006後のstory-visibleな局所目標から、特定outcomeを指定せずactionを選べるか
- subset samplingではなく有限state-spaceの全列挙というdeterministic actionへ落とせるか
- 結果前commit後に384 trialを選別せず受理できるか

成功条件は面白いattractorが見つかることではない。

**locked actionから得られた結果を、その内容にかかわらず物語状態へ返せること**を成功条件とする。
