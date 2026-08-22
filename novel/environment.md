# 物語環境

このファイルは、個人persona・組織主体・世界の相互作用を受け止める**環境の定義と解決規則**を管理する。

環境は未来の筋書きを知る脚本家ではない。Canon、物理・技術・歴史、制度、権限、利用可能な道具、現在state、各主体の行動から次に成立する結果を解決する。

## 権威関係

- 世界の確定事実: `canon.md`
- 世界・環境の解決規則: このファイル
- 時間依存world state: `state/world.md`
- 個人persona定義: `personas/`
- 時間依存persona state: `state/personas/`
- 組織定義: `organizations/`
- 時間依存organization state: `state/organizations/`
- 結合event: `events/`
- 時系列索引: `timeline.md`
- 現実の技術・歴史的制約: `research/` と `references/`

## 独立性

個人、組織、世界を一つの巨大stateへ統合しない。

- persona: Knowledge / Beliefs / Goals / Relations / Memory / Situational state
- organization: Mission / Resources / Governance / Policies / Membership / Institutional memory / External relations
- world: 場所、物理条件、公開制度、社会・経済・技術環境等の客観状態

ただし時系列では同じeventで結合する。

## 状態遷移

概念的に、worldを `W(t)`、personaを `P_i(t)`、organizationを `G_j(t)` とする。

```text
O_i(t) = Observe(W(t), P_i(t), visible(G(t)))
A_i(t) = Act(P_i(t), O_i(t))

I_j(t) = InstitutionalInput(W(t), G_j(t), visible({P_i(t)}))
D_j(t) = InstitutionalDecision(G_j(t), I_j(t))

E_k = ResolveEvent(W(t), {A_i(t)}, {D_j(t)}, constraints)

W(t+1)   = UpdateWorld(W(t), E_k)
P_i(t+1) = UpdatePersona(P_i(t), Observed_i(E_k))
G_j(t+1) = UpdateOrganization(G_j(t), InstitutionalObserved_j(E_k))
```

この記法は因果分離の概念モデルであり、数値simulationを必須にしない。

## 組織を擬人化しない

ORGは一人の巨大personaではない。

組織の「判断」は、

- 予算配分
- 人事
- 設備利用規則
- 研究テーマ承認
- 発表・知財手続き
- 会議・管理者判断
- 親会社からの指示

など具体的な制度経路を通して成立させる。

特定管理者の個人的判断が因果上重要になった場合、その人物は別PERとして生成する。逆に管理者の人格を追う必要がなければ、制度結果だけをorganization deltaとして扱う。

## ORG化の境界

会社・大学・学会・研究室を背景に登場しただけではORG化しない。

独立したMission / Resources / Governance / Institutional memoryが後続因果へ効く場合だけ `ORG-xxx` を作る。

親会社、部署、委員会等も同様で、必要になるまでworld entityでよい。

## 解決規則

1. 望ましい物語展開を理由に結果を決めない。
2. personaの意図と実際の結果を分離する。
3. organizationの公式方針と構成員個人の信念を同一視しない。
4. 組織が知っていることと所属personaが知っていることを自動同期しない。
5. 個人の私的ノートを、提出・共有eventなしにInstitutional memoryへ入れない。
6. 逆に組織内部で予算変更が成立しても、未公表なら個人personaは知らない。
7. 合併・再編・閉鎖は未来プロットとして初期stateへ置かず、制度・経済・経営判断からeventとして成立させる。
8. 技術的・歴史的に重要な結果は必要時に現実側調査で制約する。
9. world / persona / organizationの重要deltaは同じstory time / EVTから追跡可能にする。
10. 結果へ影響する自由度がある重要eventではACTION_LOCKEDを使う。

## Resolver provenance

生成者がpersonaには見えない作者側結果を既に知り、pattern / seed / order / trial selection等でoutcomeを寄せられる場合は、結果前に条件またはdeterministic selection ruleをlockする。

- `LOCKED`: outcome-sensitive条件を結果前に固定
- `UNBLINDED`: 結果知識を持つcontextで条件選択しpre-lockなし
- `AUTHOR_CONDITIONED`: 作者が望む結果へ意図的に介入

詳細は `events/README.md` と `../notes/generation-validation.md`。

## 現在の1980年代観測境界

### PER-005 高橋修一

観測可能:

- 本人が入手した当時の文献
- 自分のノート・計算結果
- ORG-001で公開された設備利用規則・研究手続き
- 実際に共有された佐伯その他の発言

観測不能:

- ORG-001経営側の未公表方針
- 将来の合併・閉鎖・史料利用
- 現代側EXP結果
- 作者側長期仮説

### PER-006 佐伯玲子

観測可能:

- 自分の時代の神経生理・memory研究
- ORG-001で本人に公開された制度・設備
- 高橋が実際に共有したmodel説明・共同記録

観測不能:

- 高橋の未共有私的ノート
- 組織の未公表経営判断
- 現代側研究結果・未来技術

### ORG-001 光陵化学生命科学研究所

制度として保持可能:

- 公式研究テーマ、提出済み内部報告、設備記録、予算・人員・発表手続き

自動的に保持しない:

- 高橋・佐伯の内面
- 未提出私的メモ
- 将来の閉鎖
- 作者側探索仮説

## 現在状態への入口

- world: `state/world.md`
- personas: `state/personas/`
- organizations: `state/organizations/`

重要eventは必要に応じて `world delta / persona delta / organization delta` を分けて記録する。