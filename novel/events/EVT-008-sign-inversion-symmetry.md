# EVT-008 裏返しは別の記憶なのか

状態: `ACTION_LOCKED / PROVISIONAL`

Resolution provenance: `LOCKED`

## Story time

`T0-1980S + symmetry check after EVT-007`

## Timeline position

- Parent: `EVT-007`
- Previous event: `EVT-007`
- Next event: 未成立

## Resolution scope

今回、高解像度化するentity / contextは次だけとする。

- PER-005 高橋修一
- PER-006 佐伯玲子
- EVT-007までに成立した6-unit toy network
- ORG-001が許容する紙上計算・共同検討という研究環境
- 1980年代時点で二人が利用できる線形代数・離散力学の知識

独立entity化しないもの:

- 共用計算機 `SYS/OBJ`: 今回の問いはweight/update ruleの代数だけで解け、機種・OS・言語が結果へ影響しない
- 親会社: 今回の局所行動へ制度判断を行わない
- ノート/紙: 保存来歴や物理状態がまだ後続因果を決めない

この判断自体を、`WORLD_POLICY.md` のlazy expansion / resolution scopeの実運転テストとする。

## World before

- EVT-007で全64 states × 6 cyclic ordersを列挙した
- fixed pointsは `A/B/C/-A/-B/-C` の6種類だった
- 以前Dと呼んだstateは `-C` だった
- PER-005 / PER-006は、`stored / nonstored`という分類より先にweight/update ruleの対称性を調べることを局所目標としている
- 現代側EXP-003〜005の結果は二人のKnowledgeではない

## Story-visible action selection

PER-005は、全状態列挙で現れた三つの符号反転stateを新しい経験的カテゴリとして増やす前に、現在のweight ruleそのものを符号反転したstateへ適用して比較する。

PER-006は、A/B/Cという具体patternに依存した説明と、任意stateに成り立つ構造的説明を分けるよう要求する。

二人は新しいnetworkや新しいpatternを探さず、EVT-007と同一のnetwork定義について次だけを検査する。

1. state `s` と全符号反転 `-s` でlocal fieldがどう変わるか
2. asynchronous unit updateが符号反転と可換か
3. `s` がfixed pointなら `-s` もfixed pointになるか
4. zero local fieldで「現在値を保持」する規則でも対称性が壊れないか
5. 必要ならenergyを使い、`E(s)` と `E(-s)` の関係を確認する

---

# ACTION LOCK

## Locked definitions

現在のnetworkだけを使う。

- state components: `s_i ∈ {-1,+1}`
- symmetric weights: EVT-007と同じHebbian outer-product和、`w_ii = 0`
- local field: `h_i(s) = Σ_j w_ij s_j`
- asynchronous update:
  - `h_i > 0` → `+1`
  - `h_i < 0` → `-1`
  - `h_i = 0` → 現在の `s_i` を保持

## Locked derivation target

結果を見る前に、次を順に代数変形する。

```text
h_i(-s)
```

を `h_i(s)` で表す。

その結果をupdate ruleへ代入し、任意の一unit update `U_i` について

```text
U_i(-s) = -U_i(s)
```

が成立するかを、`h_i > 0`, `< 0`, `= 0` の三場合すべてで確認する。

成立する場合のみ、fixed point `s*` に対して `-s*` もfixed pointであると結論する。

## Locked energy check

補助確認として、対称weightの通常の二値network energy

```text
E(s) = -1/2 Σ_i Σ_j w_ij s_i s_j
```

について `E(-s)` を直接代入して比較する。

energy checkはupdate-ruleの三場合確認を置き換えない。

## Locked interpretation boundary

このeventで説明対象にするのは、**現在のzero-bias二値toy networkが持つglobal sign-inversion symmetry**だけである。

結果が対称でも、次を主張しない。

- `-A/-B/-C` が生物学的な「反対の記憶」である
- 一般のHopfield networkが必ず同じ対称性を持つ
- bias / threshold / non-bipolar codingを加えても同じである
- mixture stateや他のspurious stateが符号反転だけで説明できる
- 現代側研究結果を1980年代人物が知った

## Locked stopping rule

上記5項目の代数確認が終わった時点で停止する。

面白い追加結果を探すために別network、別pattern、別thresholdをこのEVTへ追加しない。
