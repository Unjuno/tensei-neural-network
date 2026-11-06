# 作業コンテキスト

更新: 2026-11-07。再開のための索引。秘密情報や逐語的内部推論は保存しない。

## 現在位置

repo: Unjuno/tensei-neural-network。制作はwork/story-bootstrap。story headはEVT-019、現代側none。PER-005高橋修一・PER-006佐伯玲子・ORG-001がactive。章1〜5は技術gate済み。

**2026-10-31の新しいユーザー委任で、連載版の定期公開を開始した。** 古い記録の「公開は毎回承認待ち」をそのまま適用しない。許可はmain/publication/README.mdとpolicy.jsonの範囲に限る。mainへのwork全体merge、Canon昇格、PR、他サイト投稿は含まない。

## 制作・公開の分業

- 既存日次タスクは「研究小説の制作・検証・連載」に更新。有効、毎日午前8時ごろJST
- エージェントはwork上で1つの有限な成果を作る。最も古い未公開章の不足解消を優先
- mainのSerial Publicationは毎日JST11:17とsource CI完了等で公開ゲートを確認。最大1日1話
- mainへ書くのは公開workflowが生成したdocs/serialの本文・HTML・台帳だけ。公開エンジンはmainのコードのみ実行し、workコードは読取データとして扱う
- publication/reviews/NNN.jsonには本文blobとreview-lock blob、5項目の具体的編集評価とblocking_issuesを保存。AI_EDITORIAL_NOT_EXTERNAL_READERを明示
- main/publication/policy.jsonのenabled=falseなら制作/公開を停止。ゲートを弱めて先へ進めない

## 公開済み

第1話「戻る先」は2026-10-31に連載版として公開。
URL: https://unjuno.github.io/tensei-neural-network/serial/001.html
初回source SHA: 7820573205f29e6d626952f914d469f0f9982802
source CI: 41176570607 success
公開run: 41176658296 / job124465509267 success（manifestと最新HTMLの内容一致も観測）
既刊のHTMLとMarkdownはmainのmanifest記録hashで凍結。無断で上書きしない。

第2話「選ばなかった答え」は2026-11-02に連載公開済み。源版 `3e363989f25fccdfb3c4b75dd6a169f48f85da16`、CI `41360865674` success、公開run `41360920516` success、実配信manifestと002.htmlのSHA-256一致を確認した。公開台帳はmain/docs/serial/manifest.json。EVT-005旧状態表記のBLOCKEDは2026-11-01の履歴として保持。第3話は2026-11-03に公開用AI編集レビュー・source CI・Serial Publicationでの配信URL/hash照合を完了。第4話は2026-11-04公開・live照合成功。第5話は2026-11-06に同一本文・review-lock版のAI編集レビュー、制作CI、連載公開、live manifest/HTML照合までsuccess。公開版はmain台帳を正本とし、レビューを機械コピーしない。

## 初回統合で得た修正

初回は旧EVTの状態がPROVISIONALで止まった。成立済みの初期4eventだけを固定blob hashで識別する互換adapterを追加し、未知/改変PROVISIONALやACTION_LOCKEDは引き続き拒否。29件のエンジン回帰テストが成功。詳細はnotes/runs/2026-10-31-publication-loop.md。

## 物語状態と未採用場面

EVT-014〜018はQのone-bit近傍の256件（Q112、保存3記憶各48）、距離分類、最初の実flip、不安定4点、円環gapによる件数説明を扱った。割合を自然確率にしない。

古いsnapshotがEVT-007で止まっていても、EVT-008〜018と対応deltaから一度だけ復元する。作者側EXP-006以後の一般化や証明は人物へ自動注入しない。

novel/scene-probes/2026-10-31-circle-and-original-records.mdは未採用。発話や資料保存、研究所提出を事実に昇格していない。採用したいなら現在personaの観測とGoals、ORGの制約から正規のworld advancementとして判断する。

## 継続時の確認

最初にmainの停止スイッチ、最新source HEAD、直接EVT、CI、公開台帳と公開workflowの観測結果を確認。公開失敗はREADY/記録済みとDEPLOYEDを分ける。競合なら最新HEADから読み直しforce pushしない。結果に影響する実験は結果前commit、成果は失敗も保持。

実読者5名、Human Review/Canon受理、独立した別主体の意味復元は未完。定期公開が始まっても完了扱いしない。未確定の具体年/所在地/職位/計算機/人物の生活史を章都合で埋めない。

## 2026-11-01の原因・再開点

- 第2話編集評価は `publication/reviews/002.json`、根拠はEVT-005〜008と話別packを直接参照。第2話本文の改稿なし、EVT headは018のまま。
- 現行mainの `tools/serial_publish.py` の `event_resolved` は `RESOLVED / PROVISIONAL` を認めるが、EVT-005は `PROVISIONAL / RESOLVED`。順序だけが逆で、内容にはaction-lockとresolved consequenceがある。公開workflowはここでfail-closed。次話を公開したと偽らない。
- **次回は、公開エンジン・許可条件に触れず**、EVT-005の歴史的状態表記を修正できるかと、その影響を受ける第2〜5話のreview-lock/意味レビューの再評価範囲を調べる。版整合の確認を省いた機械的hash更新は禁止。困難なら人間による信頼済みゲート修正の要否を報告し、無断でmainを変更しない。
- 2026-11-01 run: `notes/runs/2026-11-01-chapter-002-editorial.md`。旧主張を上書きせず、公開保留を明示する。

## 2026-11-02 解消済みの公開障害・次の再開点

2026-11-01に検出した `BLOCKED: unresolved event: EVT-005` は公開ゲートの変更ではなく、work側の `EVT-005` の見出し `PROVISIONAL / RESOLVED` を `RESOLVED / PROVISIONAL` へ正規化する方針で解消を図る。内容は同一で、6本の更新順・LOCKEDのcommit・結果・world/persona deltaを変更しない。第2/3/4話の本文と根拠を実読して限定再レビューを追記し、依存blobを更新。第5話review-lockは旧EVTを参照していない。

`publication/reviews/002.json`の同一本文と新review-lockを対応付け直した。正規化後のsource CI `41360865674` completed/success、Serial Publication `41360920516` completed/success。公開URL https://unjuno.github.io/tensei-neural-network/serial/002.html の実配信manifest・HTML内容照合は成功。第3〜5話の読者視点レビューは未実施なので一括PASSにしない。次は最も古い未公開の第3話の本文・EVT-009〜011・用語/意味/数理レビューを再読して公開用 `publication/reviews/003.json` を作ること。実読者5名、独立復元、Human Review、Canon受理は依然OPEN。

## 2026-11-03 第3話レビューと再開点

- 最古の未公開第3話を通読。EVT-009の六素子残差なし、EVT-010の1983年文献へ戻る選択、EVT-011の論文掲載十六素子Qの再計算と本文を照合。具体的な登場人物の選択は高橋の恣意的な規模変更の中止と佐伯のゼロ入力判定保留。未成立の組織判断や後続EVTを追加しない。
- `publication/reviews/003.json` に5項目、限定PASS、blocking_issues空、本文blob `802424a3fc3504e766a6fdb24a791a455151900a`、review-lock blob `339a92b80ea84c604384ee0353b98e78f00f493f` を固定。AI_EDITORIAL_NOT_EXTERNAL_READER。技術再実行は新source CIで確認する。
- 直前の公開台帳は001/002のみ。latest Serial Publication `41422224575`はDAILY_LIMIT / 既刊002 DEPLOYEDの再照合。第3話は2026-11-03にSerial Publication run 41547099942でDEPLOYEDを確認。
- 今回新EVT、新実験、新章本文改稿、Canon昇格なし。CI・live配信の検証成功を観測。次は第4話を個別に再読・編集評価する。

### 2026-11-03 実測追記

- review生成commit `412fe914976bdf7e36a29dd3d8c44ee2a3345c7e` のsource CI `41546992324` はcompleted/success。unit tests、話別再計算と保存結果一致、研究実験、EXP-013保存JSON照合、workflow validatorの全step success。
- Serial Publication `41547099942` はcompleted/success、生成判断READY 003→Pages配信のlive manifest / 003.html hash照合DEPLOYED。配信遅延で途中のlive probeは未確認だったが同一runで再検証して成功。
- 公開台帳: 003、日付 `2026-11-03`、source SHA `412fe914976bdf7e36a29dd3d8c44ee2a3345c7e`、CI `41546992324`、HTML SHA-256 `56bcad73c6a45c402d5735b848b9fb48e56ce85efe10d9fbb447be1315a6db5a`、MD SHA-256 `656487e0395f0458cfb396e6063a2a6897b7aedfc8910294925e9635a3030594`。URL: https://unjuno.github.io/tensei-neural-network/serial/003.html
- 本追記を含む後続source HEADのCIは先行runの成功を流用せず別途確認する。既刊1〜3は改変しない。


## 2026-11-04 第4話の公開用AI編集レビュー

- 起点work `d75879ec212090f496cffb8b36cc1a149cdb7607`。最新story head EVT-018のまま。新EVT・研究実験・本文改稿なし。
- 公開は第1〜3話まで。最古の未公開第4話「五と二十一」について、本文、EVT-012/013、話別outline/verification/terminology/semantic-review/results/review-lockを通読し、個別に検証した。
- 本文blob `c215811ded93e9f05fce8864fceb9f996f767709`、review-lock blob `7d7810800b308ebe7f23fff382677465c6f9dc71` の同一版に `publication/reviews/004.json` で5観点の具体箇所とAI限定PASSを記録。既刊や根拠ファイルは変更していない。
- 16位置の多数側・4/12分類、距離4/8、overlap8、local inputsの5/21を整数別計算で照合。本文は固定点とQへの到達を区別しており、後続256 trialはまだ描いていない。
- この新source commitのCIと、公開エンジンの実配信照合を別途確認する必要がある。次は第5話を独立に読む。試読5名・独立restore・Human Review・Canon受理はOPEN。
- 作業記録: `notes/runs/2026-11-04-chapter-004-editorial.md`。


### 2026-11-04 第4話配信の実測確認

- `3832df3279b718c9ed222b65aff6fad55a87a7bd` のsource CI `41738589401` completed/success。全step（unit tests/章別再実行と保存JSON/研究再実行/EXP-013保存JSON/workflow validator）成功。
- Serial Publication `41738736750`: 初回pushは `remote: fatal error in commit_refs` でfailure。公開ゲートREADY自体は成立していたが、公開はその時点で未成立。同じ公開workflowのfailed jobsを**一度だけ**再実行してattempt 2はcompleted/success。job `126274931514` がlive URL/hash一致で第4話 `DEPLOYED` を記録。
- main台帳の第4話: released_on=2026-11-04、source_sha=`3832df3279b718c9ed222b65aff6fad55a87a7bd`、ci_run=41738589401、HTML SHA-256 `65b2b117df4e6e1d7266521888dcf1d4c361d7e98f376928596f347e84638192`、Markdown SHA-256 `0a6a038aa89eff4ae9a3066d2cb51808e1732993be180beb3fc5ce01bad3f379`。URL: https://unjuno.github.io/tensei-neural-network/serial/004.html 。既刊1〜3は保持。
- story headはEVT-018のまま。第5話は未読PASSとせず、次回個別に読む。外部読者・独立restore・人間Canon受理は未実施。
- 詳細: `notes/runs/2026-11-04-chapter-004-editorial.md`。

## 2026-11-06 第5話公開・再開点

- 機械的公開阻止の原因: 2026-11-05のrun `42003745924` は `publication/reviews/005.json` の欠落でBLOCKED。技術gateの失敗ではなかった。
- 第5話 `novel/chapters/005.md`、EVT-014〜018、verification/results/terminology/semantic-review/review-lockを通読し、五観点のAI編集レビュー `publication/reviews/005.json`を対象blob付きで新規保存（commit `f737e2b097b3ecfd66bbd37e9c65e70c34cdf0ae`）。本文・EVT・既刊を変更しない。
- 別ルートの円周16起点計算で各4点gapと Q=112、stored=144 の固定例を確認。新研究結果ではない。
- Story Workflow Validation `42191688452` success。Serial Publication `42191877896` success。Pages build/deploy `42191912882` success。第5話の実配信URL/hash一致を公開workflowが確認。main公開台帳に第1〜5話。
- 詳細は `notes/runs/2026-11-06-chapter-005-editorial-and-publication.md`。
- ChatGPT日次制作タスクはdisabledであることを確認し、enabled=trueへ再開した。先行実行がfailedであった根本原因は未確認。次回タスクの成功と公開workflowの冪等性を継続監視する。

### 次の有限制作単位

現在のstory headはEVT-018。次はPER-005とPER-006が、既存のQ局所問題の結果を誰が再検証できる記録にするのか、情報公開がどの組織権限に関わるかを、当人が知る既存事実だけから考える。未採用scene-probeは観測済みeventでない。人物・組織の行動が実際に成立してからEVTを作成し、自然な読書単位が成立したときだけ第6話を執筆する。作者側EXPの一般証明を人物へ漏らさない。独立試読、Human Review、Canon受理はOPEN。


## 2026-11-07 最新再開点（EVT-019）

第1〜5話はmainの公開台帳にあり、最新Serial Publication run `42195420441` は第5話のlive manifest/HTML一致を確認してsuccess。公開待ちの既存章なし。次の読書単位を話数から逆算しない。

EVT-019では、EVT-018後の共同研究を一つの追加trialへ直結させず、高橋は「別のupdate scheduleでも同じ説明が成り立つか」を未実行の問いとして残し、佐伯は「最終状態だけでなく経路の差を実際の生理学的観測へ対応させられるか」を独立に考えることを選んだ。二人の共同メモには異なる問いが並ぶが、実験条件、機器、計算機、発表、正式提出、組織保存は未成立。創作上の対話解決は`UNBLINDED`であり独立検証ではない。未採用scene-probeは引き続き未採用。

再開時は`novel/events/EVT-019-two-questions.md`と`novel/state/personas/deltas/EVT-019.md`を、旧snapshot・EVT-008〜018・ORG-001の不変境界の上へ重複適用せず復元する。次は二人のうち誰が何を実際に観測・選択するかを確認し、必要なら当時の一次資料を調べる。自然な読書単位になるまでは第6話・新EXPを作らない。実読者5名・独立restore・Human Review/Canon受理はOPEN。
