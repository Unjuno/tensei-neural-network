# EVT-012 三つの記憶を一成分ずつ比べる

状態: `RESOLVED / PROVISIONAL`

Resolution provenance: `LOCKED`

Action-lock commit: `9b0b3c8c13138df50876f038612189bf487ab15f`

## Story time

`T0-1980S + componentwise structure check after EVT-011`

## Timeline position

- Parent: `EVT-011`
- Previous event: `EVT-011`
- Next event: 未成立

## Resolution scope

- PER-005 高橋修一
- PER-006 佐伯玲子
- EVT-011で固定済みのM1 / M2 / M3 / Q
- Hopfield / Feinstein / Palmer (1983)本文の「spurious statesのelementary formはtriplesにoriginを持つ」という記述
- 紙上の符号比較とHamming distance

今回独立entity化しないもの:

- 共用計算機SYS/OBJ: 16成分の符号分類と距離計算だけなので不要
- 文献コピーOBJ: provenanceが今回の結果を左右しない

## World before

EVT-011で、1983論文掲載の16-neurone candidate Qについて、

- 16 local inputsが全てnonzero
- 全unitでlocal-input符号とQの符号が一致
- QはM1/M2/M3でも、そのglobal negationでもない

ことを確認した。

PER-005はQへ意味を与える前に、Qが三つのstored patternsからどのような成分関係として作られているかを説明したい。

PER-006は、後世のmixture-state理論を持ち込まず、掲載patternそのものの操作的関係だけを先に記録することを要求している。

## Story-visible action selection

二人は新しいpatternやnetworkを作らない。

QとM1/M2/M3を16位置すべてについて横に並べ、各位置で三つのstored patternsが、

- 全て同じ符号
- 2対1に分かれる

のどちらかを記録する。

2対1の場合は、Qが多数側と少数側のどちらに一致するかを記録する。

さらに、QからM1/M2/M3へのHamming distanceと、M1/M2/M3相互のHamming distanceを全て記録する。

このprocedureは、Qがどの単純構造に一致してほしいかを先に仮定しない。

---

# ACTION LOCK

以下を結果計算前にcommit `9b0b3c8c13138df50876f038612189bf487ab15f` で固定した。

## Locked inputs

EVT-011と同一。

```text
M1 = (+,+,+,+,-,-,-,-, +,+,-,+,-,+,-,-)
M2 = (+,+,+,+,-,-,-,-, -,-,+,-,+,-,+,+)
M3 = (+,+,-,-,+,+,-,-, +,-,-,+,+,-,-,+)
Q  = (+,+,+,+,-,-,-,-, +,-,-,+,+,-,-,+)
```

## Locked component classification

各位置 `i=1..16` について、

```text
c_i = M1_i + M2_i + M3_i
```

を計算する。

三patternなので `c_i` は `-3,-1,+1,+3` のいずれかで0にはならない。

記録:

- `|c_i| = 3`: 三pattern unanimity
- `|c_i| = 1`: 2対1 split
- `Q_i = sign(c_i)` か
- 2対1の場合、どのstored patternがminorityか

全16位置を含める。

## Locked distance check

次を全てHamming distanceで計算する。

```text
d(Q,M1)
d(Q,M2)
d(Q,M3)
d(M1,M2)
d(M1,M3)
d(M2,M3)
```

## Predeclared outcome categories

このeventでは特定の構造をPASS条件にしない。

- `MAJORITY_ALL`: 全16位置でQが三patternのcomponentwise majorityと一致
- `MIXED_RULE`: 一部位置でmajority、一部でminority
- `OTHER`: 上記で十分記述できない

どのcategoryになっても採用する。

## Stopping rule

- 16位置のclassificationを全件完了
- 6個のHamming distanceを全件計算
- outcome categoryを一つ記録

した時点で停止する。

結果後に別のBoolean rule・別pattern・別networkを追加探索しない。

---

# RESOLUTION

locked inputsだけを使い、16位置を全件分類した。

## Componentwise table

| i | M1 | M2 | M3 | Q | c_i | class | minority |
|---:|:--:|:--:|:--:|:--:|---:|---|---|
| 1 | + | + | + | + | +3 | unanimity | — |
| 2 | + | + | + | + | +3 | unanimity | — |
| 3 | + | + | - | + | +1 | 2:1 | M3 |
| 4 | + | + | - | + | +1 | 2:1 | M3 |
| 5 | - | - | + | - | -1 | 2:1 | M3 |
| 6 | - | - | + | - | -1 | 2:1 | M3 |
| 7 | - | - | - | - | -3 | unanimity | — |
| 8 | - | - | - | - | -3 | unanimity | — |
| 9 | + | - | + | + | +1 | 2:1 | M2 |
| 10 | + | - | - | - | -1 | 2:1 | M1 |
| 11 | - | + | - | - | -1 | 2:1 | M2 |
| 12 | + | - | + | + | +1 | 2:1 | M2 |
| 13 | - | + | + | + | +1 | 2:1 | M1 |
| 14 | + | - | - | - | -1 | 2:1 | M1 |
| 15 | - | + | - | - | -1 | 2:1 | M2 |
| 16 | - | + | + | + | +1 | 2:1 | M1 |

全16位置で、

```text
Q_i = sign(M1_i + M2_i + M3_i)
```

が成立した。

したがってoutcome categoryは、

`MAJORITY_ALL`

となった。

## Counts

- unanimity: 4 / 16
- 2:1 split: 12 / 16
- Qがcomponentwise majorityと一致: 16 / 16
- Qがminorityと一致: 0 / 16

2:1 splitの12位置でminorityになるstored pattern数:

- M1: 4
- M2: 4
- M3: 4

特定の一つのstored patternだけが一貫してminorityになる構造ではない。

## Hamming distances

```text
d(Q,M1) = 4
d(Q,M2) = 4
d(Q,M3) = 4

d(M1,M2) = 8
d(M1,M3) = 8
d(M2,M3) = 8
```

Qは三つのstored patternsから等しく4 bit離れている。

三stored patterns自身は互いに8 bitずつ離れている。

## Resolved consequence

- 1983論文掲載Qは、この具体例ではM1/M2/M3のcomponentwise majorityと全16位置で一致する
- Qは三stored patternsのいずれにも偏らず、Hamming distanceは全て4
- M1/M2/M3も互いに全てdistance 8で、この掲載例は三patternに対して対称的な配置を持つ
- EVT-011の「stored / negation外のstable state」という分類に、componentwise構造の説明が一段加わった
- ただし今回確認したのは**この掲載例の具体的構造**であり、「spurious memoryは一般にcomponentwise majorityである」とは一般化しない
- 1985年以降のmixture-state理論を人物Knowledgeへ追加していない

## Persona deltas

### PER-005 高橋修一

Beliefs:

- Qは三つのstored patternsを一成分ずつ見たとき、全位置で多数側を取っている
- Qが三つのどれとも同じでないのは、各stored patternが12個のsplit位置のうち4位置ずつminorityになるため説明できる
- 「spurious」という名称より、まず三patternからどう構成されるかを具体的に記述できる

Goals:

- なぜこのcomponentwise majority QがHebbian connectionの下でstableになるのか、EVT-011で観測したlocal-input値 `5 / 21` と現在のoverlap構造を結び付けて説明する
- 後世の一般理論を使わず、現在の16-neurone例だけから導出する

Memory:

- Qは16/16でcomponentwise majority
- Q-M1/M2/M3 distanceは4/4/4
- M1-M2/M3, M2-M3 distanceは8/8/8
- minority countsはM1/M2/M3各4

### PER-006 佐伯玲子

Beliefs:

- Qの構造は少なくともこの掲載例では操作的に「三patternの成分多数」と記述できる
- その記述と、一般のspurious-memory classの説明は分ける必要がある
- 「多数決」という比喩を生物学的決定機構の説明として扱ってはいけない

Goals:

- componentwise majorityという静的記述と、なぜdynamics上stableなのかという機構説明を分ける
- 高橋に、distance/overlapからlocal inputへ至る導出を明示させる

Memory:

- 16位置の全分類
- 三stored patternsへの等距離4
- stored patterns相互の等距離8

## Organization / world delta

ORG-001のmission / governance / institutional memoryに変更なし。

今回も紙上の16成分比較だけで完結したため共用計算機SYS/OBJを展開しない。

結果はPER-005 / PER-006のlocal shared recordとして成立し、組織への正式提出は未成立。

## Who observed what

- PER-005 / PER-006: 全16位置のclassification、6 Hamming distances、`MAJORITY_ALL`を共同確認
- ORG-001: 内容を組織として承認したとは扱わない
- 他persona: 未観測
- 現代側persona: 未観測

## Research branch after resolution

新しいauthor-side EXPはまだ作らない。

次の局所問題は、既存のlocked patternとHebbian weightsだけで解析できる「なぜmajority Qがstableなのか」であり、新しいランダムtrialや大規模計算を必要としない。

## Structure impact

EVT-011で成立した「stored / negation外のstable Q」が、EVT-012で単なる名前付きの異常stateから、三stored patternsのcomponentwise majorityという具体的構造へ変わった。

次の自然な問いは、

> 三つの記憶から多数側を取った形が、なぜ結合の下で自分自身を支えるのか。

である。

この問いは第4話の結末を先に作るためではなく、PER-005 / PER-006の現在goalから生じる。

## Generation validation

- componentwise classification / distances / outcome categoriesを結果前commitで固定した
- `MAJORITY_ALL`を期待して追加ruleを結果後に探索していない
- 全16位置と全6 distancesを含めた
- 1985年以降のmixture-state理論を条件選択・解釈へ使っていない
- 第4話の望ましい展開をevent発生原因にしていない
