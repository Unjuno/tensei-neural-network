# EVT-006 全balanced cueを先に固定する

状態: `RESOLVED / PROVISIONAL`

Resolution provenance: `LOCKED`

Action-lock commit: `97ee4b3d322d367468258775443d6f2aa3551ef1`

## Story time

`T0-1980S + systematic cue check after EVT-005`

## Timeline position

- Parent: `EVT-005`
- Previous event: `EVT-005`
- Next event: 未成立

## Participants

- PER-005
- PER-006

新しい独立主体は、このactionの選択・実行には必要なかった。

## World before

- EVT-005で、EVT-004と同じ6-unit network・同じ一つのbalanced cueについて、結果前に固定した6 cyclic update ordersをすべて調べた
- 結果はA / B / nonstored stable Dへ分かれた
- PER-005はDがA/B/Cとどう関係するstateかを問題にしている
- PER-006は条件を変えるなら、変更条件と検査集合を結果前に固定することを要求している
- 現代側EXP-003 / EXP-004の統計結果は二人のKnowledgeではない

## Action selection

PER-006は、EVT-005でorder選択の自由度は減ったが、balanced cue自体はEVT-004で一つだけ選ばれたものだと指摘した。

PER-005は、新しいcueを一つずつ都合よく試すのではなく、A/Bが異なる4 unitから作れる**A/B等距離cueをすべて列挙する**ことを選んだ。

その全cueに対して、EVT-005と同じ6 cyclic update ordersをすべて適用する。

結果を見てcueやorderを追加・削除しない。

---

# ACTION LOCK

以下は結果解決前にcommit `97ee4b3d322d367468258775443d6f2aa3551ef1` で固定した。

## Locked network

```text
A = (-1, +1, +1, +1, -1, -1)
B = (+1, -1, +1, -1, -1, +1)
C = (-1, -1, -1, -1, +1, -1)
```

Hebbian outer-product和、self connection=0。

unit update:

- asynchronous
- local field > 0 -> +1
- local field < 0 -> -1
- local field = 0 -> current valueを保持

## Locked balanced-cue construction

A/Bが異なるunit indexは、

```text
{1, 2, 4, 6}
```

である。

この4位置のうちちょうど2位置ではAの値を取り、残り2位置ではBの値を取る。A/Bが同じ位置 `3, 5` は共通値を使う。

A側に取る位置集合をcue IDとし、全6組合せを固定した。

```text
q12
q14
q16
q24
q26
q46
```

EVT-004 / EVT-005で使ったcueは `q46`。

## Locked update-order set

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
6 balanced cues x 6 cyclic orders = 36 trials
```

36 trialを全て含める。

## Locked stopping rule

1. 指定orderを1 sweepとして繰り返す
2. sweep終了時にstateがsweep開始時と同一ならstableとして停止
3. 最大20 sweeps
4. 20 sweepsでstableでなければ`NONCONVERGED`

## Locked outcome categories

- `A_EXACT`
- `B_EXACT`
- `C_EXACT`
- `OTHER_STABLE`
- `NONCONVERGED`

OTHER_STABLEは具体final stateも保持する。

## Inclusion / exclusion rule

- 36 trialを全て含める
- A/Bへ行かなかったtrialも削除しない
- cue単位で結果が平凡でも除外しない
- outcomeを見てcue construction、order集合、stopping ruleを変更しない
- 「面白いcue」を追加探索しない

---

# RESOLUTION

Action lock後、36 trialをlocked条件どおりexactに解決した。

## Cue definitions

```text
q12 = (-1, +1, +1, -1, -1, +1)
q14 = (-1, -1, +1, +1, -1, +1)
q16 = (-1, -1, +1, -1, -1, -1)
q24 = (+1, +1, +1, +1, -1, +1)
q26 = (+1, +1, +1, -1, -1, -1)
q46 = (+1, -1, +1, +1, -1, -1)
```

全cueで、

```text
Hamming(cue, A) = 2
Hamming(cue, B) = 2
```

である。

## Resolved table

```text
        r1   r2   r3   r4   r5   r6
q12      B    B    A    A    A    A
q14      D    A    B    B    A    A
q16      B    A    C    A    C    B
q24      D    D    D    D    D    D
q26      A    B    D    D    B    B
q46      A    D    B    B    D    D
```

ここで、

```text
D = (+1, +1, +1, +1, -1, +1)
```

はEVT-005で観測済みのnonstored fixed point。

## Aggregate

```text
TOTAL          36
A_EXACT        11
B_EXACT        11
C_EXACT         2
OTHER_STABLE   12
NONCONVERGED    0
```

stable final stateはA / B / C / Dの4種類。

- A: 11
- B: 11
- C: 2
- D: 12

30 trialは2 sweepsでstable判定。

`q24`の6 trialは1 sweepでstable判定した。これはq24自体がDと同一であり、initial cueの時点ですでにfixed pointだからである。

## Locked consistency check

`q46` の6結果はEVT-005と一致した。

```text
q46: A / D / B / B / D / D
```

## Additional geometry observed

`q16` はA/BだけでなくCにも同距離だった。

```text
Hamming(q16, A) = 2
Hamming(q16, B) = 2
Hamming(q16, C) = 2
```

このcueからは、locked orderのうち2本でCへexactに到達した。

一方 `q24` は、A/Bへの距離は2/2だが、nonstored fixed point Dそのものである。

```text
Hamming(q24, A) = 2
Hamming(q24, B) = 2
q24 = D
```

したがって、**A/BへHamming等距離であることは、そのcueがA/Bだけの曖昧さを表すことを保証しない。**

stored setの第三patternや、stored set外のfixed pointとの関係も同時に入る。

## Resolved consequence

- pairwiseなA/B等距離cueを全列挙しても、結果はA/Bの二者択一にはならなかった
- stored pattern Cへ到達するcue/orderが存在した
- balanced cueそのものがnonstored fixed point Dである場合もあった
- 「AとBの間」というpairwiseな表現だけでは、複数patternを持つnetwork全体の状態幾何を十分に記述できない
- EVT-005で成立した「stored集合外の戻り先」の問題に加え、**選んだ二原像以外のstored patternも候補になる**ことを二人が観測した
- ただし、一つの6-unit networkの全balanced cue×6 cyclic ordersに限る

## Persona deltas

### PER-005

Beliefs:

- `A/B等距離`は、A/Bだけを競合させる操作ではない
- cueと保存集合全体の関係を見ずに「二つの記憶の間」と呼ぶと、第三patternやnonstored fixed pointを見落とす
- final stateだけでなく、cueが全stored patternsとどの距離関係にあるかも記録する必要がある

Goals:

- pairを選んで`ambiguous`と呼ぶ前に、cueと**保存集合全体**の関係を記述する方法を考える
- Dのようにcue自体がnonstored fixed pointである場合を、recall trialとしてどう扱うか整理する

Memory:

- 6 balanced cue × 6 cyclic ordersの全36結果を保持する
- q16からCへ到達したこと、q24がDそのものだったことを保持する

PER-005は共同メモに、

> AとBの間、と書いた時点で、ほかの戻り先を消していたのかもしれない。
>
> 手掛かりは二つの原像だけでは定義できない。

と追記する。

### PER-006

Beliefs:

- pairwiseな等距離条件を満たしても、実験上の候補集合がA/Bだけになるとは限らない
- `ambiguous between A and B`という言葉を使うなら、他のstored / nonstored stateへの関係を確認すべき
- model内の操作的定義を狭く保つ必要がさらに強まった

Goals:

- 今後cueを比較する場合、selected pairだけでなくstored set全体への距離を先に記録させる
- `initial state already fixed`と`dynamicsで別stateへ移った`を分類上分ける

Memory:

- q16がA/B/Cへ2 bitずつだったこと
- q24がinitial stateからDだったこと
- 全36 trialを結果選別なしで記録したこと

## World delta

共同記録に、

- A/B-balanced cue全6種類
- 6 cyclic ordersとの全36結果
- q16のA/B/C三者等距離
- q24 = nonstored fixed point D

が追加された。

具体的な機種名・programming language・所属機関はまだ固定しない。

## Who observed what

- PER-005 / PER-006: 全36結果、cue geometry、C/Dへの到達
- 他ペルソナ: 未観測
- 現代側persona: 自動的には未観測

## Research branch after resolution

このeventから即座に新EXPは作らない。

既存EXP-004はすでにfinal分類として `OTHER_STORED` / `NONSTORED_CONVERGED` を記録しており、第三stored patternやnonstored stateの存在自体は研究側で扱える。

ただしEVT-006で人物側から新しく明示された、

> pairwiseなbalanced cueを、保存集合全体に対してどう定義・評価すべきか

という問いは、既存Q-004の「同一cueがA/B双方へ行く例が存在するか」とは判定対象が異なり得る。

後続で現実側の検証可能な定義へ落とせる場合、Q-005候補として切り出す。

このeventだけを理由に、まだEXP-005を自動生成しない。

## Structure impact

結果を見てから整理すると、EVT-004〜005の`転`で崩れたのは「一つのcueに一つのtarget」という前提だけではなかった。

EVT-006では「A/Bの間」というpairwiseな問題設定そのものが、network全体の状態空間を隠す場合があると判明した。

ただし、これを予定された`結`や第2話の章末とは指定しない。

## Generation validation

outcome-sensitiveなcue集合・order集合・stopping / inclusion ruleはcommit `97ee4b3d322d367468258775443d6f2aa3551ef1` で結果前に固定し、その後変更していない。

EVT-006はTest-003のclean resolver validationとして利用できる。
