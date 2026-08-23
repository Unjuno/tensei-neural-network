# 物語Bootstrap

このディレクトリは、あるstory timeで**階層的World Stateを同じ背景から同期初期化・再初期化するBootstrap Frame**を管理する。

Bootstrapは未来の筋書きではない。対象時点までに成立している背景を一つの初期化源へまとめ、world、人物、組織、物、動物、場所、制度、環境等の必要なentity stateへ、それぞれ異なる情報境界で射影する制作上の同期点である。

## 基本モデル

```text
B_k
 ├─ background/opening frame
 ├─ global context projection
 ├─ entity discovery
 │   ├─ PER / ANI / OBJ
 │   ├─ ORG / GRP
 │   ├─ LOC / POL
 │   └─ ENV / SYS / ...
 ├─ relation discovery
 └─ entity-specific projections -> S_i(t)
```

同じBootstrapから初期化しても、各entityが同じ情報を保持するわけではない。

人物のknowledge、組織のinstitutional memory、物のphysical state、国家のpolicy state等は別々にprojectionする。

## IDと物語順

`BOOT-001`, `BOOT-002` ... は安定識別子であり、story timeやnarrative orderを表さない。

## Bootstrapが保持するもの

各`BOOT-xxx`は最低限、次を持つ。

- Target story time
- Parent event head
- Authority inputs
- Opening / Background frame
- Global/world projection
- Entity discovery
- Relation discovery
- Entity-specific projections
- Forbidden leakage / forbidden inheritance
- Outputs
- Unresolved slots

## Entity discovery

背景に存在する全対象をID化しない。

独立state履歴が後続因果へ必要な場合だけentity化する。

例:

- 独立した認知・目的・観測が必要 → `PER`
- ペットの生理・学習・関係が継続因果へ効く → `ANI`
- 装置・文書・試料の状態や来歴が効く → `OBJ`
- 組織の資源・規則・制度記憶が効く → `ORG`
- 国家・法域の政策状態を独立追跡する必要がある → `POL`

class定義は`../entities/README.md`を参照する。

## 初期化手順

1. target story timeとParent event headを確定する。
2. Canon、timeline、対象時点までのevent/state、研究根拠からbackground frameを作る。
3. その時点のglobal physical / historical / technological / institutional constraintsを抽出する。
4. `entity discovery`を行い、因果上必要な対象だけを独立entity化する。
5. entity間の包含・所属・所有・場所・権限等のrelationを確定する。
6. 各entityへ、そのclassと境界に応じたstateをprojectionする。
7. 上位contextから下位entityへのconstraintを解決する。
8. knowledge / memory / private stateが階層を越えて自動漏洩していないか検査する。
9. 同じ同期キーでstate群を保存する。

同期キー:

```text
BOOT-xxx @ <story time> @ <parent event head>
```

## 階層初期化の例

```text
BOOT-002 @ T0-1980S @ none
  ↓
world: 1984-85前後の技術史・社会背景
  ↓
POL: 日本の制度的context（必要になれば独立state化）
  ↓
ORG-001: 研究所のmission/resources/governance
  ↓
PER-005: 高橋が実際に利用可能・観測可能な範囲
  ↓
OBJ: 計算機・ノート等（因果上必要になった時点で独立化）
```

ここで上位stateを下位へ丸ごとコピーしない。

## 再初期化

長い中断、別AI session、model交換等では、設定を寄せ集めて現在世界を推測し直さない。

対象Bootstrap、story time、parent event head、その時点までのentity states / relationsから再構成する。

再初期化は制作上の操作であり、それ自体を物語eventにはしない。

## Lazy expansion

Bootstrap時点で宇宙全体を詳細化しない。

上位scaleはconstraintとして粗く保持し、現在の物語因果へ必要になった部分だけ独立entityへ展開する。

これにより、宇宙・国家・企業・人物・物を同じ概念体系へ置きながら、不要なstate explosionを防ぐ。

## Narrativeとの関係

Bootstrap/state graphは本文ではない。

本文はWorldStateからscene/viewpointに必要な部分だけをNarrativeProjectionする。未来の結末をBootstrapへ入れず、world advancementによって成立したfactを後から本文へ投影する。
