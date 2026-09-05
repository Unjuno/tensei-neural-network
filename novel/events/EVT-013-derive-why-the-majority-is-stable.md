# EVT-013 なぜ多数側の形が自分を支えるのか

状態: `ACTION_LOCKED / PROVISIONAL`

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

結果の`5 / 21`に合わせて式を選ばず、次の一般的な恒等式だけを使う。

---

# ACTION LOCK

以下を結果導出前に固定する。

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

## Predeclared outcome

`PASS`:

- locked identitiesだけから得た簡約式がEVT-011の16 local inputsを全件exactに再現する
- その式からunanimity / 2:1 splitでQと同符号のnonzero local inputになる理由を説明できる

`FAIL`:

- 一つでもlocal inputがEVT-011と一致しない

`UNCERTAIN`:

- self-connection除外やoverlap変換の条件を追加解釈しないと一意に導出できない

## Stopping rule

上記6項目を完了し、PASS / FAIL / UNCERTAINを一つ記録した時点で停止する。

結果後に別の学習則、bias、threshold、patternを追加しない。

## Resolver may use

- EVT-011/012のlocked patternsと観測結果
- bipolar Hamming/inner-product identity
- finite sums / algebra

## Resolver must not use for condition selection or interpretation

- 1985年以降のmixture-state formula
- spin-glass order parameters
- 現代側EXP-003〜005
- 第4話の望ましい展開
- outcomeを見た後の別derivation routeへの差し替え

## Resolution provenance target

`LOCKED`
