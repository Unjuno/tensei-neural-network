# EVT-012 三つの記憶を一成分ずつ比べる

状態: `ACTION_LOCKED / PROVISIONAL`

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

以下を結果計算前に固定する。

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

結果は次の観測記録として受理する。

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

## Resolver may use

- locked M1/M2/M3/Q
- integer addition
- Hamming distance
- EVT-011までのstory-visible knowledge

## Resolver must not use for condition selection

- 1985年以降のmixture-state formula
- 現代側EXP-003〜005
- 第4話の望ましい展開
- outcomeを見た後の追加rule探索

## Resolution provenance target

`LOCKED`
