# 階層World State運用ポリシー

状態: `ACTIVE / PROVISIONAL`

この文書は、`novel/entities/`, `novel/state/`, `novel/bootstrap/`, `novel/environment.md`, `novel/events/` を使って物語世界を進行させる際の運用規則を定める。

`POLICY.md` の一般方針に従い、この文書は**階層World Stateに関する詳細ポリシー**として扱う。矛盾する場合はroot `POLICY.md` を優先し、この文書を修正する。

---

## 1. 基本原則

物語は人物だけから生成しない。

人物、動物、物、組織、集団、場所、国家・法域、システム、自然環境、物理的constraint等が、異なるscaleで相互作用する世界として扱う。

ただし全世界を完全simulationしない。

**現在の因果へ効く範囲だけを展開し、eventで世界を前進させ、成立したfactをNarrativeProjectionとして小説へ投影する。**

---

## 2. Personaはentity classの一種とする

`PER-xxx` は、独立した認知・目的・観測・記憶・判断を持つ主体のclassである。

企業、国家、物、ペット、装置、環境を無理にpersonaと呼ばない。

必要に応じて次のclassを使う。

- `PER`: 人物、AI instance等の認知主体
- `ANI`: 動物・ペット等
- `OBJ`: 装置、文書、試料、建物、媒体等
- `ORG`: 企業、研究所、大学、行政組織等
- `GRP`: 研究室、家族、チーム、非公式集団等
- `LOC`: 部屋、施設、都市、地域等
- `POL`: 国家、自治体、法域等
- `ENV`: 気候、生態、経済環境、情報環境等
- `SYS`: 通信網、電力網、計算基盤、市場等
- `PHY`: 物理法則、定数、宇宙論的constraint等

詳細は `entities/README.md` を参照する。

---

## 3. Entity化の必要条件

背景に存在するだけではIDを発行しない。

次のいずれかを満たす場合に独立entity化を検討する。

1. 状態変化が後続eventの因果へ影響する
2. 独立した観測境界または情報境界を追跡する必要がある
3. 所有・所属・権限・場所・来歴等を複数eventにわたり追跡する必要がある
4. その対象の状態を他entityへ還元すると重要な因果差が消える
5. 後世の史料・証拠・記録のprovenanceへ影響する

単に名前が出た、背景に人がいる、机の上に物がある、というだけではentity化しない。

---

## 4. Entityを過剰生成しない

世界を細かく作り込むこと自体を目的にしない。

禁止:

- sceneに出た全人物をPER化
- 部屋にある全物品をOBJ化
- すべての会社・行政機関・学会をORG/POL化
- 物語因果に関係しない生理・経済・気象変数を追跡
- 「いつか使うかもしれない」という理由だけで大量IDを発行

必要になった時点でlazy expansionする。

---

## 5. 階層は固定木ではなくtyped graphとして扱う

包含関係だけで世界を表現しない。

entity間には少なくとも次のrelationがあり得る。

- `located_in`
- `member_of`
- `employed_by`
- `owned_by`
- `controlled_by`
- `funded_by`
- `reports_to`
- `has_access_to`
- `stores`
- `observes`
- `communicates_with`
- `regulated_by`
- `parent_organization`

一つのentityは複数の上位contextへ同時に属し得る。

---

## 6. 上位contextはconstraintを与えるがknowledgeを自動共有しない

例:

```text
世界技術水準
→ 国家制度
→ 企業環境
→ 研究所資源
→ 研究室設備
→ 人物の実行可能行動
```

このconstraint chainは許容する。

しかし、

```text
国家が知っている
→ 企業も知っている
→ 研究所も知っている
→ 全研究者も知っている
```

とはしない。

**constraint propagationとknowledge propagationを必ず分離する。**

情報は、公開、通知、会話、文書、観測、権限等の経路を通った場合だけ下位・上位entityへ伝わる。

---

## 7. 個人stateと組織stateを混同しない

人物のGoalと組織のMissionは別である。

人物の私的ノート、未共有仮説、感情、記憶は、自動的に組織のInstitutional memoryへ入らない。

逆に、組織内部の未公表方針、予算判断、人事計画も、所属personasへ自動共有しない。

組織が行動したように見える場合でも、必要なら意思決定構造・規則・責任者personaへ因果を分解する。

組織を「一人の巨大人格」として擬人化しない。

---

## 8. 物・文書・装置にもstateとprovenanceを持たせられる

`OBJ`を独立化した場合、最低限必要に応じて次を追跡する。

- identity
- location
- ownership / custody
- physical integrity
- configuration / contents
- provenance
- access boundary
- last relevant event

文書については「誰が書いたか」「誰が読めるか」「公式記録か私的記録か」「後にどこへ移管されたか」を区別する。

後世の人格再構成や史料探索に使う場合、史料provenanceを本文都合で後付けしない。

---

## 9. 動物・ペットは必要ならANIとして追跡する

動物を単なる小道具にしない。

継続的な因果へ効く場合、

- physiology
- learned behavior
- attachment / relation
- location
- health
- observed cues

等を状態として持たせられる。

ただし人間personaと同じ認知モデルをそのまま適用しない。

---

## 10. 国家・経済・文化・世界環境を人物の背景説明だけにしない

法、景気、研究政策、産業構造、通信環境、文化規範等が人物の選択肢へ影響する場合、それらをworld constraintまたは必要に応じた`POL/ENV/SYS` stateとして扱う。

歴史小説では、人物が歴史を知っているから影響されるのではなく、**知らなくても制度・物価・雇用・設備・移動可能性等を通じて影響される**ことを許容する。

---

## 11. PHYは通常constraintであり、毎event state化しない

物理法則、定数、宇宙論的条件等は通常、resolverの不変constraintとして扱う。

作品世界で変化する、観測差が出る、または宇宙規模のeventが物語因果へ届く場合だけ独立state化する。

宇宙全体を毎event更新しない。

---

## 12. Resolution Scopeを毎eventで限定する

event解決前に、現在の因果へ届くentity/contextだけを`resolution scope`として選ぶ。

選定基準:

- active agentが観測・操作する対象
- action結果を制約する上位context
- event結果で直接stateが変わり得る対象
- 証拠・記録・所有・権限の経路に必要な対象
- 時間経過で外生変化が届く対象

scope外は、既知constraintまたは`UNRESOLVED`背景として保持する。

面白い結果を出すためにscopeを都合よく追加しない。

---

## 13. World Advancementの標準手順

物語世界を一段進めるときは原則として次を行う。

1. current event headとstory timeを確認
2. resolution scopeを決定
3. scope内のentity state / relationを読む
4. 上位physical / historical / institutional constraintsを解決
5. active agentsへ観測可能情報だけをprojection
6. agent actionを現在stateから生成
7. 必要な外生変化を、歴史・物理・制度・事前規則から解決
8. outcome-sensitiveな自由度があれば`ACTION_LOCKED`
9. environment resolverで`EVT-xxx`を解決
10. affected entity statesだけdelta update
11. relation changesを更新
12. fact levelを分類
13. timeline / STATUS / working-context等の索引を同期
14. 読書単位が成立した場合だけNarrativeProjectionを更新

話数や起承転結を理由にworld advancementを発生させない。

---

## 14. 外生eventを許容するが脚本装置にしない

人物が何もしなくても世界は変化できる。

例:

- 天候
- 経済変化
- 法改正
- 論文公開
- 組織再編
- 設備故障
- 物の劣化
- 動物の生理変化
- インフラ障害

外生eventは次のいずれかを根拠とする。

- 実際の歴史
- 物理・生物学的因果
- 現在stateから自然に生じる制度的因果
- 結果前に固定した生成規則

「ここで転が必要」「悲劇が欲しい」「伏線回収したい」を原因にしない。

---

## 15. Upward / Downward causationを両方許容する

### Downward

上位状態が下位の選択肢を変える。

例:

```text
景気後退
→ 親会社の予算削減
→ 研究所の設備更新停止
→ 高橋が利用できる計算資源減少
```

### Upward

下位eventが上位状態を変える。

例:

```text
研究者の発見
→ 内部報告
→ 研究所の研究方針変更
→ 親会社の投資判断
```

どちらも、途中の因果linkを省略してテレポートさせない。

---

## 16. Factは成立範囲を分類する

`EVT-xxx`で成立したfactを次のlevelで区別する。

### LOCAL

個人、物、場所、限定された観測者の範囲だけで成立。

### INSTITUTIONAL

組織内記録、正式判断、提出資料等として成立。

### PUBLIC

論文、報道、公開記録、法令等として公開情報になった。

### CANON

長期物語上の確定事項として人間レビュー後に`canon.md`へ昇格。

LOCAL factを、本文に書かれたという理由だけでPUBLIC/CANONへ昇格しない。

---

## 17. Fact、Belief、Claim、Recordを分離する

最低限、次を区別する。

- `Fact`: resolver上成立した客観結果
- `Belief`: entityが真だと信じている内容
- `Claim`: 人物・組織が外部へ主張した内容
- `Record`: 何らかの媒体へ記録された内容

Recordが存在しても内容がFactとは限らない。

人物が嘘をつく、組織が誤認する、史料が間違う、記録が欠落することを許容する。

---

## 18. Historical factとfictional factを混同しない

実在の歴史、制度、技術、企業、人物に関する事実は`research/` / `references/`で確認する。

架空ORGや架空人物は、確認済みhistorical constraintsの中でのみ構成する。

実在組織をモデルにした架空組織を、実在組織の事実として書かない。

歴史的に未確認の具体機種・職位・制度・地理情報を本文の自然さだけで固定しない。

---

## 19. Future leakageを階層全体で禁止する

未来知識漏洩はpersonaだけの問題ではない。

禁止:

- 1980年代ORG stateへ将来の倒産・閉鎖を既知方針として入れる
- 過去のOBJへ後世のprovenanceを初期状態として持たせる
- 国家・企業へ未来の技術史を前提にした意思決定をさせる
- resolverが未来プロットを理由に経済・制度eventを発生させる

未来結果はそのstory timeに到達した時点でのみeventとして解決する。

---

## 20. NarrativeProjectionはWorldStateを変更しない

小説本文はWorldStateからのprojectionである。

本文の都合で、

- entityを新設
- stateを変更
- relationを変更
- fact levelを昇格
- historical constraintを変更

してはいけない。

本文とstateが矛盾した場合、まず本文を直す。

本文上どうしても新しい重要事実が必要なら、本文を書く前にstate/event側へ戻して成立させる。

---

## 21. Minimum Causal Outlineを章ごとに持てる

章を作る場合、必要に応じて「これ以上削ると因果が壊れる最小あらすじ」を保持できる。

Minimum Causal Outlineは未来eventを作るための脚本ではなく、**すでに成立したevent/stateを一つの読書単位へ投影するための因果骨格**とする。

章本文はこの骨格を超えて新factを生成しない。

---

## 22. State explosionを防ぐ

次の条件を満たさないstateは原則として保存しない。

- 後続因果へ必要
- observation boundaryへ必要
- provenanceへ必要
- ownership / authority / location等の継続追跡へ必要
- 重要な不確実性を保持するため必要

細かいscene描写はstate化せずNarrativeProjectionで処理してよい。

---

## 23. 不確定性を無理に埋めない

`UNRESOLVED`を正式な状態として許容する。

特に、

- 正確な年月日
- 所在地
- 機種
- 職位
- 組織構成
- 所有関係
- 将来の再編

等は、現在eventへ必要になるまで固定しない。

ただし必要になった時点では、歴史調査・world resolver・human review等で解決する。

---

## 24. Human interventionを偽装しない

作者が、舞台、人物名、組織名、技術条件等を明示的に固定した場合、それはauthor interventionとして扱う。

それをpersonaの自発的選択やworld resolverから自然発生したfactと偽装しない。

必要に応じてdecision logへ理由を残す。

---

## 25. 検証可能性

重要なworld advancementでは、後から次を辿れることを目標とする。

- どのstateから開始したか
- どのentityがscopeに入ったか
- 誰が何を観測したか
- 何がactionで何が外生変化か
- resolverが何をconstraintとして使ったか
- どのfactが成立したか
- どのentity stateが変わったか
- 何が未確定のまま残ったか

この追跡可能性を、小説本文へそのまま表示する必要はない。

---

## 26. 現在の実装

現時点では、

- entity model: `entities/README.md`
- global state: `state/world.md`
- persona state: `state/personas/`
- organization state: `state/organizations/`
- bootstrap: `bootstrap/`
- resolver: `environment.md`
- events: `events/`
- narrative projection: `chapters/`

を使う。

新class用directoryは、実際に独立stateが必要になった時点で追加する。

専用database、ECS engine、simulation frameworkは現時点では導入しない。Markdown + stable ID + event sourcingで限界が生じた場合に改めて検討する。
