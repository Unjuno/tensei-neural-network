# Organization Initialization

組織主体を新しいstory timeへ初期化・再初期化する標準手順。

## 0. 前提

組織は巨大なpersonaではない。個人のBeliefを持たせず、制度的なMission / Resources / Governance / Institutional memoryを追跡する。

## 1. 対象時点を固定

- target story time
- parent event head
- 対象Bootstrap
- current branch

を確認する。

## 2. Organization discovery

背景に存在する組織ごとに次を判定する。

### ORG化する

後続因果へ次のいずれかが効く場合:

- 独立した資源配分
- 人事・設備・発表・知財等の制度判断
- 個人とは異なる長期Mission
- 組織記録・アーカイブ
- 合併・再編・閉鎖等の制度state

### ORG化しない

- 名前だけ出る会社・大学・学会
- 一度しか使わない建物・部署
- 独立判断をまだ必要としない親会社
- 個人personaの行動だけで十分説明できる研究室

ORG化しない対象はworld entityとして残す。

## 3. Stable ID

`ORG-xxx` を採番する前にcurrent work branchとmainの双方で既存ORG IDを確認する。

IDは再利用しない。

## 4. Definition作成

`novel/organizations/ORG-xxx-*.md`へ最低限記録する。

- Identity / name
- fictional / real-world status
- founding context
- Mission baseline
- Resources baseline
- Governance baseline
- Institutional culture
- Institutional memory boundary
- External relations
- personaとの関係
- historical constraints
- future leakage禁止

## 5. Bootstrap projection

対象BOOTへ、

- なぜ独立ORGが必要か
- その時点で存在する制度事実
- organizationへ投影する情報
- personaへ公開される情報
- 非公開情報
- 将来情報として禁止するもの

を追加する。

## 6. State同期

`novel/state/organizations/ORG-xxx.md`へ、同じ同期キーでstateを生成する。

最低限:

- Mission
- Resources
- Governance / Policies
- Membership
- Institutional memory
- External relations
- Situational state
- Observation / disclosure boundary

## 7. 三層整合性チェック

同じstory timeで、

- world state
- active persona states
- active organization states

のevent head / Bootstrap lineageを照合する。

組織の公式情報を全所属personaへ自動コピーしない。公開・通知・会議・文書閲覧等の観測経路が必要。

## 8. Event後更新

重要eventで制度的変化があれば `Organization delta` を記録する。

例:

- 予算削減
- 研究テーマ承認・中止
- 新計算機導入
- 発表制限
- 人事異動
- 親会社統合
- 研究所名称変更
- 閉鎖決定
- 資料移管・廃棄

個人が制度変化を知らなければ、そのpersona stateは更新しない。

## 9. 再編・fork

後継組織が実質的に同じMission / Governance / Institutional memoryを継承する軽微変更なら同じORGのstate変化でよい。

独立した新Mission・統治・法的主体・記憶境界を持つ場合、新ORGへforkする。

旧ORGの過去stateは削除しない。

## 10. Validation

- [ ] 組織を背景だけで機械的にORG化していない
- [ ] personaとorganizationを混同していない
- [ ] 私的記憶とInstitutional memoryを分離した
- [ ] 経営未公表情報をpersonaへ漏らしていない
- [ ] 将来の合併・閉鎖を初期stateへ入れていない
- [ ] 実在組織をモデルにした場合、fictionalization境界を明記した
- [ ] world / persona / organizationの同期キーが整合している
