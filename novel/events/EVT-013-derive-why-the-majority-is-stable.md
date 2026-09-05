# EVT-013 なぜ多数側の形が自分を支えるのか

状態: `RESOLVED / PROVISIONAL`

Resolution provenance: `LOCKED`

Action-lock commit: `a44b9e605576e8896b8b296f0ec3c2b01c28c972`

## Story time

`T0-1980S + stability derivation after EVT-012`

## Timeline position

- Parent: `EVT-012`
- Previous event: `EVT-012`
- Next event: 未成立

## Resolution scope

- PER-005 高橋修一
- PER-006 佐伯玲子
- EVT-011/012のM1 / M2 / M3 / Q
- EVT-011のHebbian connection rule
- EVT-012のHamming distancesとcomponentwise majority classification
- 1980年代時点で利用可能な線形代数・二値vectorの内積

独立entity化しないもの:

- 共用計算機SYS/OBJ: 16成分vectorの内積と代数変形だけで完結可能
- 新しい文献OBJ: 今回は既に共有済み1983論文と現在の計算結果だけを使う

## World before

EVT-012で、1983論文掲載Qについて次が成立した。

```text
d(Q,M1)=d(Q,M2)=d(Q,M3)=4
Q_i = sign(M1_i + M2_i + M3_i)   for all i
```

またM1/M2/M3相互はdistance 8である。

EVT-011ではQのlocal inputが各位置で `±21` または `±5` となり、全てQと同符号だったためQはstableと確認済み。

PER-005の現在goalは、EVT-011のlocal-input値とEVT-012のmajority / distance構造を同じ式で結び付けること。

PER-006は、静的な「多数側」という記述をdynamical stabilityの原因と混同せず、Hebbian weightsから明示的に導出するよう要求している。

## Story-visible action selection

二人は新しいtrialを行わない。

Qと各stored patternのHamming distanceをbipolar vectorの内積へ変換し、そのoverlapをHebbian local input式へ代入する。

結果の`5 / 21`に合わせて式を選ばず、一般的なbipolar Hamming/inner-product identityとEVT-011のconnection ruleだけを使う。

---

# ACTION LOCK

以下を結果導出前にcommit `a44b9e605576e8896b8b296f0ec3c2b01c28c972` で固定した。

## Locked identities

bipolar vector `x,y ∈ {-1,+1}^N` について、

```text
x · y = N - 2 d_H(x,y)
```

を使う。

EVT-012で観測済みの `N=16`, `d_H(Q,Ms)=4` から各overlap `Ms·Q` を計算する。

## Locked connection / local input

EVT-011と同一。

```text
T_ij = Σ_s M^s_i M^s_j    (i != j)
T_ii = 0

h_i(Q) = Σ_j T_ij Q_j
```

## Locked derivation route

self-connection exclusion `j != i` を明示したまま、

```text
h_i(Q)
= Σ_{j != i} Σ_s M^s_i M^s_j Q_j
```

からstored-pattern overlap `M^s · Q` を使う形へexactに変形する。

記録するもの:

1. 各 `M^s · Q`
2. `h_i(Q)` のoverlap表示
3. EVT-012の `c_i = M1_i+M2_i+M3_i` を使った簡約形
4. unanimity位置 `|c_i|=3` で予測されるlocal input
5. 2:1 split位置 `|c_i|=1` で予測されるlocal input
6. EVT-011の16 local inputsとの全件一致/不一致

---

# RESOLUTION

## 1. Hamming distanceからoverlapへ

EVT-012で、

```text
N = 16
d_H(Q,M1)=d_H(Q,M2)=d_H(Q,M3)=4
```

だった。

したがって各stored patternについて、

```text
M^s · Q
= 16 - 2×4
= 8
```

となる。

よって、

```text
M1·Q = M2·Q = M3·Q = 8
```

である。

## 2. Local inputをoverlapで書く

Hebbian connectionから、

```text
h_i(Q)
= Σ_{j != i} T_ij Q_j
= Σ_{j != i} Σ_s M^s_i M^s_j Q_j
= Σ_s M^s_i Σ_{j != i} M^s_j Q_j
```

である。

内側の和はself termを除いているため、

```text
Σ_{j != i} M^s_j Q_j
= M^s · Q - M^s_i Q_i
```

となる。

したがって、

```text
h_i(Q)
= Σ_s M^s_i (M^s·Q - M^s_i Q_i)
```

各overlapは8、かつ `(M^s_i)^2=1` なので、

```text
h_i(Q)
= Σ_s [8 M^s_i - Q_i]
= 8(M1_i+M2_i+M3_i) - 3Q_i
```

を得る。

EVT-012の

```text
c_i = M1_i+M2_i+M3_i
```

を使えば、

```text
h_i(Q) = 8 c_i - 3 Q_i
```

である。

## 3. Unanimity位置

三stored patternsが同符号なら、EVT-012よりQも同符号なので、

```text
c_i = 3 Q_i
```

となる。

したがって、

```text
h_i(Q)
= 8(3Q_i) - 3Q_i
= 21 Q_i
```

となる。

よってunanimityの4位置では、local inputはQと同符号でabsolute value 21。

## 4. 2:1 split位置

2対1に分かれる位置では、Qはcomponentwise majorityと一致するため、

```text
c_i = Q_i
```

となる。

したがって、

```text
h_i(Q)
= 8Q_i - 3Q_i
= 5Q_i
```

となる。

よってsplitの12位置では、local inputはQと同符号でabsolute value 5。

## 5. EVT-011との全件照合

この導出が予測する16 local inputsは、

```text
(+21,+21,+5,+5,-5,-5,-21,-21,
 +5,-5,-5,+5,+5,-5,-5,+5)
```

となる。

EVT-011でexact arithmeticにより得たvectorと16 / 16成分で完全一致した。

## Outcome

`PASS`

## Resolved consequence

- この16-neurone掲載例では、Qがstableである理由を、三stored patternsへの等しいoverlap `8` とcomponentwise majority構造からexactに説明できる
- unanimity位置ではQを支えるlocal inputのmarginが21、2:1 split位置では5になる
- EVT-011で経験的に確認した`5 / 21`が、EVT-012の静的pattern構造とHebbian connection ruleから一つの式で導出された
- Qは単に「保存していないのに止まるstate」ではなく、この具体例では三stored patternsの相関構造から自己支持されるstateとして記述できる
- ただし、この導出は**この掲載例のM1/M2/M3/Qと等overlap構造**に対する説明であり、一般のspurious states全てへcomponentwise-majority formulaを一般化しない
- 1985年以降のmixture-state理論・spin-glass解析を人物Knowledgeへ追加していない

## Persona deltas

### PER-005 高橋修一

Beliefs:

- Qのstabilityは「spurious」という名称だけでなく、stored patternsへのoverlapとHebbian weightsから説明できる
- componentwise majorityという静的構造が、この具体例では`h_i=21Q_i`または`5Q_i`という自己支持へ結び付く
- 「記憶していないstateがなぜ止まるか」という最初の問いに対し、少なくとも一つの具体例ではstored memories同士の重なりから説明できる

Goals:

- 次に進むなら、この一例の構造説明を一般化する前に、1983論文が行ったrandom-start accessibilityやunlearningの操作へ進む必要があるかを検討する
- その場合、紙上計算を超えるtrial数・randomness・計算資源を事前固定する

Memory:

- `M1·Q=M2·Q=M3·Q=8`
- `h_i(Q)=8(M1_i+M2_i+M3_i)-3Q_i`
- unanimity: `h_i=21Q_i`
- 2:1 split: `h_i=5Q_i`
- EVT-011 local-input vectorと16/16一致

### PER-006 佐伯玲子

Beliefs:

- 「多数側」という見た目だけでなく、connection ruleからQのstabilityまで導出できた
- それでもQを生物学的な偽記憶や認知現象として読む根拠はない
- 一具体例のexact derivationと一般的なnetwork現象を区別する必要がある

Goals:

- 次にrandom-start / unlearningへ進むなら、何を観測すれば論文再現と呼べるかを先に固定する
- random seed / starting-state集合 / update schedule / learning decrement / stopping ruleを結果前に明示する

Memory:

- overlapからlocal inputへの導出
- unanimity 21 / split 5という二種類のmargin
- 一例の説明であって一般理論ではないというboundary

## Organization / world delta

ORG-001のmission / governance / institutional memoryに変更なし。

今回も紙上代数で完結したため、共用計算機SYS/OBJを展開しない。

結果はPER-005 / PER-006のlocal shared recordとして成立し、正式なinstitutional reportは未成立。

## Who observed what

- PER-005 / PER-006: overlap計算、local-input導出、16/16照合を共同確認
- ORG-001: 内容を組織として承認したとは扱わない
- 他persona: 未観測
- 現代側persona: 未観測

## Research branch after resolution

このevent自体から新しいauthor-side EXPは作らない。

次に論文のrandom-start accessibilityやunlearning効果をstory-sideで再現する場合は、乱数・trial集合・更新規則・unlearning stepを伴うため、独立したACTION_LOCKと、必要ならauthor-side reproductionを分離する。

## Structure impact

EVT-011〜013で、

```text
stored / negation外のstable Qを確認
→ Qが三patternのcomponentwise majorityと分かる
→ そのmajority構造がなぜstableかをHebbian weightsから導出
```

という局所的な説明単位が完成した。

ここは一つの小さな`結`になり得るが、起承転結ラベルはevent発生原因ではなく、成立後の分類にすぎない。

次のworld advancementでは、この局所的説明を一般化するのではなく、人物の現在goalから「accessibility / unlearningへ進むか」「別の問いへ移るか」を解決する。

## Generation validation

- derivation routeを結果前commitで固定した
- Hamming/inner-product identityと既存Hebbian rule以外を追加していない
- EVT-011の16 local inputsと16/16で照合した
- 1985年以降のmixture-state理論を使っていない
- 第4話の望ましい展開を原因にしていない
