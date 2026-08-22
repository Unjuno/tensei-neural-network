# 組織主体の運用

このディレクトリは、物語内で独立した制度的目的・資源・意思決定・記憶を持つ組織を `ORG-xxx` として管理する。

## 組織をORG化する条件

背景に存在する会社・大学・学会・研究室を機械的にORG化しない。次のいずれかが後続因果へ効く場合だけ独立主体として追跡する。

- 予算、人員、設備、研究テーマ、公開・非公開を独立に決める
- 個人personaと異なる長期Goalや制約を持つ
- 人事・合併・再編・閉鎖等の制度的stateが物語へ影響する
- 組織として保持する記録・アーカイブ・規則が後続eventへ影響する
- 一個人のBeliefへ還元できない意思決定過程を持つ

単なる建物、親会社名、学会名、背景部署は必要になるまでworld entityのまま扱う。

## 定義とstateを分ける

- `ORG-xxx-*.md`: 比較的安定した組織定義、設立目的、統治、資源、文化、観測境界
- `../state/organizations/ORG-xxx.md`: 時間依存する予算・人員・研究方針・制度状況・アーカイブ等

組織stateを個人persona stateへ混ぜない。

## 組織状態

概念的には、時点 t の組織状態を次で扱う。

`O_j(t) = {Mission, Resources, Governance, Policies, Membership, InstitutionalMemory, ExternalRelations, SituationalState}`

組織は擬人化しない。実際の行為は、規則、会議、管理者、予算配分、設備利用条件等を通して解決する。組織の判断を一人の人格の発言のように生成しない。

## Bootstrapでの初期化

1. 対象story timeのworldを復元する
2. 個人persona discoveryと別にorganization discoveryを行う
3. 上記ORG化条件を満たす組織だけ定義する
4. Bootstrapから組織へ、その時点までに成立している制度的情報だけを投影する
5. `state/organizations/`へ同期stateを作る
6. world / persona / organization のstory timeとparent event headを一致させる
7. 将来の合併・閉鎖・史料散逸を初期stateへ未来知識として入れない

## event更新

重要eventでは必要に応じて、

- world delta
- persona delta
- organization delta

を分けて記録する。

研究者が研究所の将来を知らなくても、組織側で予算削減が成立していることはあり得る。ただし、その情報を観測していないpersonaへ自動共有しない。

## 実在組織との関係

架空組織は、複数の実在例から史実上可能な制度・設備・文化を組み合わせてよい。ただし、特定の実在研究所で架空人物が実際に勤務したと誤認させる書き方は避ける。

実在組織を直接舞台にする場合は、所属・設備・制度・年代を一次資料または高品質な機関史料で確認する。