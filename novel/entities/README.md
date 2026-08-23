# World Entity / State Model

このディレクトリは、物語世界に存在し、時間とeventによって状態が変わる対象を、人物だけに限定せず統一的に扱うための概念モデルを定義する。

## 基本原則

`persona` は世界状態主体の一種であり、世界全体そのものではない。

物語世界は概念的に、異なるscaleと境界を持つentityの集合として扱う。

```text
Universe / physical regime
└─ world / planet / global environment
   ├─ nation / jurisdiction / economy / culture
   │  └─ organization / institution / community
   │     └─ group / household / laboratory
   │        ├─ person / artificial agent
   │        ├─ animal / pet
   │        └─ object / device / document
   └─ natural environment / infrastructure / location
```

これは固定された木構造ではない。あるentityは複数のrelationを持ち、包含関係だけでは表現できない。したがって実装上は**typed hierarchical graph**として扱う。

## Entity class

必要に応じて次のclassを使用する。

- `PER`: 人物、AI instance等、局所的な認知・目的・観測・記憶を持つ主体
- `ANI`: 動物・ペット等。生理・行動・学習・関係状態を追跡する必要がある主体
- `OBJ`: 装置、媒体、文書、建物、試料等、物理状態や来歴が因果へ効く対象
- `ORG`: 企業、研究所、大学、行政組織等、制度的目的・資源・規則・記憶を持つ主体
- `GRP`: 研究室、家族、チーム、非公式集団等
- `LOC`: 部屋、研究所敷地、都市、地域等の場所
- `POL`: 国家、自治体、法域等、法・政策・制度状態が独立して因果へ効く主体
- `ENV`: 気候、生態、経済環境、情報環境等、個別主体へ還元できない環境状態
- `SYS`: 電力網、通信網、計算基盤、市場等のシステム
- `PHY`: 物理法則・定数・宇宙論的条件等。通常は不変constraintとして扱い、作品設定上変化する場合だけstate化する

IDを発行するのは、個別状態履歴を追跡する必要が生じた対象だけとする。背景に存在する全てをentity化しない。

## Stateとscale

各entity `X_i` はstory time `t` に状態 `S_i(t)` を持ち得る。

状態はclassごとに異なる。

- 人物: knowledge, beliefs, goals, memory, physiology, relations
- 動物: physiology, learned behavior, attachment, location
- 物: location, ownership, integrity, configuration, contents, provenance
- 組織: mission, resources, governance, membership, institutional memory
- 国家: law, policy, institutions, diplomatic/economic conditions
- 環境: temperature, weather, ecology, information availability等

上位entityのstateは下位entityを完全には決定しない。下位entityのstateも上位entityの単純な総和ではない。

## Context inheritance

下位entityは上位contextから制約を受ける。

例:

```text
1984年の世界技術水準
→ 日本の制度・市場
→ ORG-001の予算・設備・規則
→ 研究室の利用可能資源
→ 高橋の実行可能な行動
→ 使用する計算機の具体状態
```

ただし情報は自動継承しない。

国家が知っていることを企業が知るとは限らず、企業が保持する情報を従業員が知るとも限らない。`constraint propagation` と `knowledge propagation` を分離する。

## Eventによる世界更新

世界進行は、未来プロットを直接生成するのではなく、現在のentity statesとeventから次状態を解決する。

概念モデル:

```text
Context(t) = ResolveContext({S_i(t)}, relations, constraints)
Actions(t) = SelectActions(active agents, observations)
E_k        = ResolveEvent(Context(t), Actions(t))
S_i(t+1)   = Apply(E_k, S_i(t))  # affected entities only
```

すべてのentityを毎event更新する必要はない。影響を受けたentityだけdeltaを記録し、未変更stateは継承する。

## Upward / downward causation

物語因果は階層の両方向へ流れる。

### downward

- 法改正 → 企業規則 → 研究予算 → 人物の選択肢
- 景気後退 → 親会社 → 研究所 → 設備更新停止
- 停電 → 建物 → 計算機 → 実験中断

### upward

- 個人の発見 → 研究室 → 研究所方針 → 学会・産業への影響
- 一つの事故 → 組織調査 → 規制変更
- 文書の保存 → 後世の史料環境 → 現代人物の知識

これにより、人物だけを原因主体とするモデルを避ける。

## Fact generation

`EVT-xxx`で解決された結果は、その時点の世界で成立したfact候補となる。

ただし階層を区別する。

1. local fact: 個人・物・場所だけに成立
2. institutional fact: 組織記録・制度へ成立
3. public fact: 公開情報として成立
4. canon fact: 長期的に重要で、人間レビュー後に`canon.md`へ昇格

人物の信念や発言はfactと同一ではない。

## Narrative projection

小説本文はworld stateそのものではなく、world stateから特定sceneの観測可能範囲を投影したものとする。

```text
World state
→ scene scope
→ viewpoint observation
→ narrative projection
```

したがって本文のために未確定stateを勝手に補完しない。一方、stateに存在する全情報を本文へ説明する必要もない。

## 目的

このモデルの目的は世界を完全シミュレーションすることではない。

**物語因果へ効く状態を、適切なscaleで明示し、人物・組織・物・制度・環境の相互作用から世界を前進させること**である。
