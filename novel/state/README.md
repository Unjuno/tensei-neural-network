# 階層的な時系列World State

このディレクトリは、物語内の**時間に依存する可変状態**を管理する。

従来の「persona + world」の二分法を一般化し、人物、動物、物、組織、国家、場所、システム、環境等を、必要な粒度で独立entity stateとして扱う。entity classの定義は `../entities/README.md` を参照する。

## 基本モデル

世界状態は一枚の巨大snapshotではなく、entityごとの状態とrelationからなるtyped graphとして扱う。

```text
WorldState(t)
 = { entity states S_i(t), relations R(t), global constraints C(t) }
```

現在の保存先:

- `world.md`: global/world-level stateと、まだ独立entity化していない背景のmaterialized snapshot/checkpoint
- `personas/`: `PER-xxx` state
- `personas/deltas/`: personaへ届いたevent差分
- `organizations/`: `ORG-xxx` state
- `organizations/deltas/`: organizationへ届いたevent差分

今後 `ANI/OBJ/GRP/LOC/POL/ENV/SYS` の独立履歴が必要になった場合だけ対応directoryを追加する。

## Restore authority / snapshot semantics

`world.md`を「常に最新event headを含む巨大正本」とは扱わない。

本repoはevent sourcingを基本とするため、materialized snapshotと、それ以後のevent/entity deltaを組み合わせてcurrent stateを復元する。

概念的には、

```text
current state
= last trusted snapshot/checkpoint
+ all relevant resolved EVT after checkpoint
+ affected entity deltas after checkpoint
```

となる。

Restore時の優先:

1. `novel/events/EVT-*` の直接正本とparent chain
2. 対象entityのbaseline / latest trusted snapshot
3. snapshot以後の `state/**/deltas/EVT-*.md`
4. `STATUS.md`, `timeline.md`, `working-context.md` 等の索引

したがって、`world.md`の内部表示がcurrent event headより古くても、その後のdirect event/deltaが成立している場合は**古いsnapshotへ巻き戻さない**。

現在の1980年代側では、`world.md`にmaterializeされたglobal snapshotより後にもEVT-008以降が成立している。EVT-008以降の主な変化はPER-005/PER-006のlocal knowledge/goalsとORG-001の局所状態であり、対応するeventおよび`personas/deltas/`, `organizations/deltas/`をoverlayして復元する。

新しいglobal constraint / relation / environment factが成立し、`world.md`へmaterializeしないと復元が不安定になる場合はcheckpointを更新する。

checkpointは履歴を置換しない。詳細は `LIFECYCLE.md`。

## 定義と状態を分ける

entityの比較的安定したidentity / baselineと、story timeで変化するstateを分離する。

人物なら定義側に認知傾向や初期境界を置き、state側に現在のknowledge / beliefs / goals / relations / memory / physiology / situationを置く。

組織なら定義側にmission baselineやgovernance baselineを置き、state側に現在の予算、人員、設備、方針、institutional memory等を置く。

物や動物も同様に、identityと可変stateを混同しない。

## 階層とrelation

世界は単純な木ではない。

```text
Universe / physical regime
└─ world / global environment
   ├─ nation / jurisdiction / economy / culture
   │  └─ organization / institution
   │     └─ group / laboratory
   │        ├─ person / artificial agent
   │        ├─ animal / pet
   │        └─ object / device / document
   └─ natural environment / infrastructure / location
```

これは概念的なscale表示であり、実際には所属、所有、場所、雇用、通信、親子組織、法的管轄等のtyped relationsを持つgraphとして扱う。

## Context inheritance

下位entityは上位contextから制約を受ける。

例:

```text
1984年の世界技術水準
→ 日本の制度・経済
→ 企業・研究所の資源と規則
→ 研究室の利用可能設備
→ 高橋の実行可能な行動
→ 使用中の計算機の具体状態
```

ただし**constraint propagationとknowledge propagationを分離する**。

国家の政策が企業を制約しても、従業員がその政策判断の全情報を知るとは限らない。組織が保持する文書も、全構成員へ自動共有されない。

## 状態遷移

時点`t`のentity state群は、それ以前のstateと、その間に成立したeventから更新する。

```text
Context(t) = ResolveContext({S_i(t)}, R(t), C(t))
Actions(t) = SelectActions(active agents, observations)
E_k        = ResolveEvent(Context(t), Actions(t))
S_i(t+1)   = Apply(E_k, S_i(t))
```

すべてのentityを毎event更新しない。影響を受けたentityだけdeltaを記録し、未変更stateはcarry forwardする。

## World advancement

一回のworld advancementは原則として次の順序で行う。

1. direct event chainからcurrent event head / story timeを確定する
2. last trusted snapshotとsnapshot以後のrelevant deltasを復元する
3. 因果的に関係するentity stateを読み込む
4. 上位context、物理、歴史、制度constraintを解決する
5. active agentごとに観測可能情報だけを射影する
6. agent actionまたは外生変化を決定する
7. environment resolverでeventを解決する
8. 影響を受けたentity stateだけ更新する
9. relation変化を更新する
10. timeline / STATUS等の索引を同期する
11. 長期的に重要なfactはhuman review後にCanonへ昇格する

## Upward / downward causation

因果は階層の両方向へ流れる。

### downward

- 法改正 → 企業規則 → 研究予算 → 人物の選択肢
- 景気後退 → 親会社 → 研究所 → 設備更新停止
- 停電 → 建物 → 計算機 → 実験中断

### upward

- 個人の発見 → 研究室 → 研究所方針 → 学会・産業への影響
- 一つの事故 → 組織調査 → 規制変更
- 文書の保存 → 後世の史料環境 → 現代人物のknowledge

## Exogenous events

人物の行動がなくても世界は進む。

天候、経済変化、法改正、組織再編、設備故障、動物の生理変化、物の劣化、論文公開等は外生eventになり得る。

ただし「物語を面白くするため」に恣意的に発生させず、歴史的・物理的・制度的根拠、または事前に定めた生成規則を持たせる。

## Resolution scope / lazy expansion

全宇宙を毎step計算しない。

現在eventへ因果的に届く範囲を`resolution scope`として展開し、それより外側は既知constraintまたは未解決背景として保持する。必要になった時点でentity化・細分化する。

これにより階層モデルを導入してもstate explosionを避ける。

## Factの階層

解決されたeventから生じるfactもscaleを区別する。

1. `local fact`: 個人・物・場所等にだけ成立
2. `institutional fact`: 組織記録・制度へ成立
3. `public fact`: 公開情報として成立
4. `canon fact`: 長期的に重要で、人間レビュー後に`canon.md`へ昇格

人物のbelief、発言、組織の主張は客観factへ自動昇格しない。

## Narrative projection

小説本文はWorldStateそのものではなく、scene scopeとviewpointから得られる観測のprojectionである。

```text
WorldState
→ scene scope
→ viewpoint observation
→ narrative projection
```

本文の自然さのために未確定の重要stateを勝手に補完しない。一方、WorldStateに存在する全情報を説明する必要もない。

## 時間と語り順

`story time` と読者への提示順は別である。1984年のeventを現代場面の後に描いても、state履歴では1984年側へ属する。

このモデルの目的は完全な宇宙simulationではなく、**物語因果へ効く状態を適切なscaleで明示し、人物・組織・物・制度・環境の相互作用から世界を前進させること**である。
