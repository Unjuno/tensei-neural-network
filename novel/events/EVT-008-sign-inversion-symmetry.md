# EVT-008 裏返しは別の記憶なのか

状態: `RESOLVED / PROVISIONAL`

Resolution provenance: `LOCKED`

Action-lock commit: `f02d78ddbec2b166fb4e1a346f6cf0e969cb8fc5`

## Story time

`T0-1980S + symmetry check after EVT-007`

## Timeline position

- Parent: `EVT-007`
- Previous event: `EVT-007`
- Next event: 未成立

## Resolution scope

今回、高解像度化したentity / contextは次だけ。

- PER-005 高橋修一
- PER-006 佐伯玲子
- EVT-007までに成立した6-unit toy network
- ORG-001が許容する紙上計算・共同検討という研究環境
- 1980年代時点で二人が利用できる線形代数・離散力学の知識

独立entity化しなかったもの:

- 共用計算機 `SYS/OBJ`: 今回の問いはweight/update ruleの代数だけで解け、機種・OS・言語が結果へ影響しない
- 親会社: 今回の局所行動へ制度判断を行わない
- ノート/紙: 保存来歴や物理状態がまだ後続因果を決めない

これは`WORLD_POLICY.md`のlazy expansion / resolution scopeを実運転した結果である。階層モデルを導入したこと自体を理由に不要なentityを増やさなかった。

## World before

- EVT-007で全64 states × 6 cyclic ordersを列挙した
- fixed pointsは `A/B/C/-A/-B/-C` の6種類だった
- 以前Dと呼んだstateは `-C` だった
- PER-005 / PER-006は、`stored / nonstored`という分類より先にweight/update ruleの対称性を調べることを局所目標としていた
- 現代側EXP-003〜005の結果は二人のKnowledgeではない

## Story-visible action selection

PER-005は、三つの符号反転stateを新しい経験的カテゴリとして増やす前に、現在のweight ruleそのものを符号反転stateへ適用して比較した。

PER-006は、A/B/Cという具体patternに依存した説明と、任意stateに成り立つ構造的説明を分けるよう要求した。

新しいnetworkやpatternは導入せず、action-lockで固定した代数確認だけを行った。

---

# ACTION LOCK

結果解決前の固定内容はcommit `f02d78ddbec2b166fb4e1a346f6cf0e969cb8fc5` を正本とする。

現在のnetworkについて、

- `s_i ∈ {-1,+1}`
- `h_i(s) = Σ_j w_ij s_j`
- zero local fieldでは現在値保持
- `h_i(-s)`の導出
- `h_i > 0`, `< 0`, `= 0` の三場合でupdateの符号反転可換性を確認
- fixed point対称性を確認
- 補助的に`E(-s)`と`E(s)`を比較

することを固定した。

---

# RESOLUTION

## 1. Local field

任意のstate `s`について、全成分を反転した`-s`を代入すると、

```text
h_i(-s)
= Σ_j w_ij (-s_j)
= - Σ_j w_ij s_j
= -h_i(s)
```

となる。

この関係にはA/B/Cという具体patternは使っていない。現在のzero-bias local fieldがstateに対して線形であることだけを使った。

## 2. One-unit asynchronous update

### `h_i(s) > 0`

`s`側ではunit `i`は`+1`になる。

`h_i(-s) = -h_i(s) < 0`なので、`-s`側では同じunitは`-1`になる。

したがって更新後も両者は符号反転関係にある。

### `h_i(s) < 0`

`s`側ではunit `i`は`-1`になる。

`h_i(-s) > 0`なので、`-s`側では`+1`になる。

ここでも更新後は符号反転関係にある。

### `h_i(s) = 0`

`h_i(-s)`も0になる。

locked ruleではzero field時に現在値を保持する。`s_i`を保持する側に対して、`-s`側は現在値`-s_i`を保持する。

したがってzero fieldでも符号反転関係は壊れない。

以上から、同じunitを更新する写像を`U_i`とすれば、現在のruleでは

```text
U_i(-s) = -U_i(s)
```

が三場合すべてで成立する。

同一のupdate orderを順に適用してもこの関係は保たれる。

## 3. Fixed-point pairing

`s*`がfixed pointなら、どのunitを更新してもstateは変わらない。

```text
U_i(s*) = s*
```

符号反転可換性から、

```text
U_i(-s*)
= -U_i(s*)
= -s*
```

となる。

したがって`-s*`もfixed pointである。

EVT-007でA/B/Cがfixed pointであり、同時に-A/-B/-Cがfixed pointだったことは、このtoy network固有の偶然として別々に暗記する必要がない。現在のupdate ruleが持つglobal sign-inversion symmetryから対で生じる。

## 4. Energy check

補助的に、

```text
E(s) = -1/2 Σ_i Σ_j w_ij s_i s_j
```

へ`-s`を代入すると、

```text
E(-s)
= -1/2 Σ_i Σ_j w_ij (-s_i)(-s_j)
= -1/2 Σ_i Σ_j w_ij s_i s_j
= E(s)
```

となる。

energy landscapeもglobal sign inversionに対して対称である。

ただし、このenergy確認だけでzero-field tie ruleまで含む実際のupdate写像を確認したことにはしないため、上の三場合検査を主たる解決とする。

## Resolved consequence

- 現在のzero-bias bipolar toy networkでは、任意stateとその全符号反転のdynamicsが同じupdate orderの下で対称になる
- fixed pointは符号反転対を作る
- EVT-007の `A/B/C/-A/-B/-C` は、この対称性と整合する
- `-A/-B/-C`を単に「保存していない別の記憶」と呼ぶのは、model構造を隠す
- `stored / nonstored`は観測上の分類として残せるが、機構分類としては少なくとも`stored-pattern negation`を分ける必要がある
- mixtureやその他のspurious stateは今回説明していない

## Persona deltas

### PER-005 高橋修一

Beliefs:

- EVT-007の三つの反転fixed pointは、個別の偶然ではなく現在のzero-bias update ruleの対称性から対で生じる
- 「保存したpatternか否か」だけではnetwork dynamicsの構造を十分に分類できない
- memoryとして意味づける前に、表現とruleが作る数学的対称性を剥がす必要がある

Goals:

- 次に`nonstored`を扱うなら、少なくとも符号反転対称性で説明できるstateを除いてから残りを調べる
- 生物学的な記憶の意味と、bipolar codingが作る数学的同値性を混同しない

Memory:

- `h_i(-s) = -h_i(s)`
- zero fieldの保持規則を含めてもupdateは符号反転と可換
- fixed pointsは符号反転対になる
- `E(-s) = E(s)`

高橋は共同記録のD=-Cという行の横に、個別名を増やす代わりに、

> 名前をつける前に、対称性を見ろ。

と追記する。

### PER-006 佐伯玲子

Beliefs:

- `-C`を第三の原像や別記憶として生物学的に読む根拠はさらに弱くなった
- 現在観測した反転対は、少なくともこのmodelでは表現・update ruleの数学的構造として先に説明できる
- model内で説明できる構造を除去してからでなければ、生物学的解釈へ進むべきでない

Goals:

- 今後、数学的対称性で説明できない残差が本当に観測されるかを区別する
- 高橋がmodelの言葉からmemoryの言葉へ飛躍しないよう、観測カテゴリと解釈カテゴリを分ける

Memory:

- 符号反転対称性の導出
- zero-field caseを別途確認したこと
- energyも符号反転で不変だったこと

## Organization / world delta

ORG-001のmission / resources / governanceには変更なし。

今回の共同計算は引き続き研究所内で許容された局所的研究行為だが、**この導出が研究所のinstitutional memoryへ正式登録されたとはまだ扱わない**。

共用計算機の具体状態は今回の結果を左右しなかったため、`SYS` / `OBJ`へ展開しなかった。

共同記録には、EVT-007の経験的な6 fixed pointsに加えて、符号反転対称性の代数的説明が追加された。

Fact level:

- local fact: PER-005 / PER-006の共同記録と共有knowledgeとして成立
- institutional fact: 未成立
- public fact: 未成立
- canon fact: 未昇格

## Who observed what

- PER-005 / PER-006: 上記導出とその解釈境界を観測
- ORG-001: 組織として内容を観測・承認したとは扱わない
- 他persona: 未観測
- 現代側persona: 自動的には未観測

## Research branch after resolution

新しいQ/H/EXPはまだ作らない。

今回のeventは、EVT-007で人物自身が立てた局所問題を、当時利用可能な数学と既存toy networkだけで解いたものだからである。

一方、現実研究側で既存EXPの`NONSTORED_CONVERGED`を再分類する監査は依然として候補である。物語側で今後、符号反転を除いた残差について具体的な問いが成立した場合に切り出す。

## Structure impact

局所的には、EVT-007で生じた「保存していない状態とは何か」という混乱の一部が整理された。

しかし、これは`結`を先に作るための解決ではない。

むしろ二人の問いは、

> 数学的対称性で説明できるものを取り除いたあとに、まだ「記憶ではない安定状態」は残るのか。

へ狭まった。

次eventや第2話の切れ目は固定しない。

## Generation validation

- EVT-007後のpersona goalsだけからactionを選択した
- outcome-sensitiveな別network / parameter selectionを行わなかった
- derivation targetと停止条件をcommitしてから解決した
- 結果が単純な対称性の確認で終わっても、そのまま採用した
- ORG / SYS / OBJを「新しい階層モデルを使いたいから」という理由で増殖させなかった
- 現代EXPの結果を人物へ漏洩させなかった

`WORLD_POLICY.md`の最初の実運転として、resolution scopeを狭く保つこと自体が有効だった。