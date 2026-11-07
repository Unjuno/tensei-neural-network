# 現在の状態

更新: 2026-11-08。これは索引。直接のEVT・state・実験記録・公開台帳・実際のCIを優先する。

## 現在位置と公開

- 制作branch: `work/story-bootstrap`
- 1980年代側resolved head: **EVT-021**。現代側: none
- active: PER-005 高橋修一 / PER-006 佐伯玲子 / ORG-001 光陵化学生命科学研究所
- 第1〜6話はPREPUBLICATION_GATE_PASSED。ただし連載配信の確認済みは第1〜5話のみ（第6話は候補、source CI・公開workflow確認待ち）。独立試読・Human Reviewは未実施
- **連載版の第1話「戻る先」を2026-10-31に公開済み。** 第2話「選ばなかった答え」は2026-11-02に連載版へ公開・実配信照合済み。第3話『表の外』は2026-11-03にAI編集レビュー・source CI・連載公開・live URL/hash照合まで確認済み。第4話「五と二十一」は2026-11-04に公開用AI編集レビュー・source CI・連載公開・live URL/hash照合成功。第5話「最初に動いたもの」は2026-11-06に公開用AI編集レビュー・source CI・Pages実配信のSHA-256照合まで確認済み
- 公開目次: https://unjuno.github.io/tensei-neural-network/serial/
- 第1話: https://unjuno.github.io/tensei-neural-network/serial/001.html
- 第5話: https://unjuno.github.io/tensei-neural-network/serial/005.html

## 今回の継続委任の境界

ユーザーは2026-10-31に、定期制作・検証・連載版公開のループを明示依頼した。この限定範囲の公開は毎回の承認待ちにしない。詳細と停止スイッチの正本は**mainのpublication/README.md / publication/policy.json**。

mainへ追加したのは公開機構とdocs/serialの生成物だけ。work全体のmerge/fast-forward、研究/本文原稿/Canonの一括受理、PR、他サイト投稿は行っていない。公開とCanon受理は別。既存docs/novel・docs/researchはそのまま保持した。

## 定期ループ

制作: 既存ChatGPTタスク「研究小説の制作・検証・連載」を更新して有効化。毎日午前8時ごろ（Asia/Tokyo）。最も古い未公開章を実読・改稿・検証し、publication/reviews/NNN.jsonへ対象版付き編集評価を記録する。未読の一括PASSは禁止。

公開: mainのSerial Publication workflow。毎日UTC 02:17（日本時間11:17）とsource CI完了等で確認。最新work SHAのCI、話別gate、review-lock、用語・EVT・編集レビューを照合し、既刊直後の1話だけを最大1日1話で出力。配信未確認時は新話を足さず前回配信を再試行する。

停止: main/publication/policy.jsonのenabled=false。機構の権限・ゲートを制作タスク自身で緩めない。

## 初回の実測検証

- work候補commit: `7820573205f29e6d626952f914d469f0f9982802`
- Story Workflow Validation: run `41176570607` success。既存5話・研究実験・EXP-013結果照合・構造検査を通過
- 追加公開エンジンのunit tests: 29件成功（ローカルCPython 3.13.5、Actions CPython 3.12.15）
- Serial Publication: run `41176658296` / job `124465509267` success
- 公開先manifestと最新HTMLのSHA-256一致を同jobで確認しDEPLOYEDとした。GitにHTMLが存在するだけでは公開成功としない
- 失敗履歴: 初回run `41176298501` は旧EVTのPROVISIONAL表記を拒否して停止。成立済み旧EVT-001〜004だけを正確なblob hashで識別する互換修正と回帰テストを追加。過去EVTや本文の書換え、未確認PROVISIONALの一括容認はしていない

今回の記録: `notes/runs/2026-10-31-publication-loop.md`。公開原稿と根拠の版はmainの`docs/serial/manifest.json`を参照。

## 小説・未採用案

| 話 | 採用EVT | 状態 |
|---|---|---|
| 1 戻る先 | EVT-001〜004 | 技術gate済み、編集レビュー済み、連載公開済み |
| 2 選ばなかった答え | EVT-005〜008 | 技術gate・編集レビュー済み。2026-11-02に公開・live URL/hash照合成功。旧BLOCKED履歴は保持 |
| 3 表の外 | EVT-009〜011 | 技術gate・公開用AI編集レビューPASS。2026-11-03連載公開、live URL/hash照合成功 |
| 4 五と二十一 | EVT-012〜013 | 技術gate・AI編集レビュー済み、2026-11-04連載公開、live照合成功 |
| 5 最初に動いたもの | EVT-014〜018 | 技術gate・AI編集レビュー済み、2026-11-06連載公開・live照合成功 |

`novel/scene-probes/2026-10-31-circle-and-original-records.md`は未採用。そこに書いた会話・保存・組織への提出は未成立のまま。今回新EVT・新personaは追加していない。

## 状態復元・研究

BOOT-002 / T0-1980S起点。具体年月日は未確定。古いworld/persona snapshotへ巻き戻さずEVT-008〜018と対応deltaを一度だけ適用する。人物は作者側の一般定理・EXP結果を自動的には知らない。

EVT-018までの局所結果は、16素子Qの一bit近傍と16巡回順の256件がQ112・保存記憶各48となり、first-flip・4点の不安定集合・円環gapで説明できたこと。112/256を自然確率へ一般化しない。

作者側EXP-006〜013の研究状況は`notes/roadmap-progress-2026-10-30.md`と各実験正本へ。EXP-013は640適格模型・139440軌道が保存結果と一致、CI組込済み。EXP-009は事前登録された条件を確認して扱い、未実行と実行済みを混同しない。

## 次回の一手・残課題

第1〜5話の連載版が公開済み。最後の新規公開の根拠は `notes/runs/2026-11-06-chapter-005-editorial-and-publication.md`、公開済み版のSHA-256はmainの`docs/serial/manifest.json`を正本とする。第5話の公開review追加commit `f737e2b097b3ecfd66bbd37e9c65e70c34cdf0ae` に対するCI run `42191688452` とSerial Publication run `42191877896` はともにsuccess。今回の公開はCanon・Human Review・独立実読者評価ではない。

次の制作単位: EVT-020後の二人の異なる問いを、各人の観測境界とORGの制約から進める。未採用の`novel/scene-probes/2026-10-31-circle-and-original-records.md`の台詞や出来事を既成事実にしない。第6話を公開ノルマのために作らない。実在読者5名のpilot、真の独立restore、人間Canon受理はOPEN。

日次制作タスクが2026-11-06の作業開始時にはdisabledだったため、有効へ戻した。ただし過去実行がfailed扱いとなった原因は未確定で、**次回の実行成功を確認するまでは運用の完全性を主張しない**。公開エンジンはmainの`publication/policy.json`のenabledに従う。

## 2026-11-01 第2話の再編集評価と公開阻止

- 起点work HEAD `1b20820e`。新章・新EVT・Canon変更はなし。第2話の原文とEVT-005〜008、話別verification、terminology、semantic-review、resultsとreview-lockを照合。
- `publication/reviews/002.json`を本文blob `c3b4cbb1`、review-lock blob `6e2691b5`に固定して追加。編集レビューはAIによるもので、実読者の合格ではない。
- レビュー保存commit `18e34614b1ec0e0ff15779e9cfa375e47788208d` のCI run `41252392042` は全step成功。Python標準ライブラリで6/36/384件・18/46分類・符号反転可換性を別実装でも照合。
- 公開run `41252464100` は **BLOCKED: unresolved event: EVT-005** で停止。`EVT-005`の `状態: PROVISIONAL / RESOLVED` が現行ゲートの許容表記に一致しない。ゲートもmainも改変していない。連載版は第1話まで。
- 実行記録: `notes/runs/2026-11-01-chapter-002-editorial.md`。本索引変更後のHEADにもCIが必要。

## 2026-11-02 EVT-005状態表記監査と第2話公開（確認済み）

- 直前の公開run `41292885268` も `BLOCKED: unresolved event: EVT-005`。第1話だけがmain公開台帳にある。
- EVT-005冒頭の状態表記のみ `PROVISIONAL / RESOLVED` → `RESOLVED / PROVISIONAL` へ正規化。既存EVT-006〜018の表記と一致させた。ACTION_LOCK commit `59ff6530`、実験条件/全6順序/結果・人物世界差分は変えない。
- 第2〜4話を実読して意味レビューへ再監査を追記し、各review-lockを新しい対象blobへ更新。第5話review-lockはEVT-005を依存に含まないため変更不要と確認。
- 第2話のpublication/reviews/002.jsonを同一本文blobと新review-lock blobへ紐づけ直し、限定再読を明記。技術的整合性はCIで確認する。独立読者・Canon受理ではない。
- 正規化実装commit `3e363989f25fccdfb3c4b75dd6a169f48f85da16` のsource CI `41360865674` は全step success（unit tests、話別再実行、研究再実行、EXP-013保存JSON照合、workflow validator）。公開run `41360920516` はcompleted/success、live manifestと `002.html` のSHA-256照合成功でDEPLOYED。公開日2026-11-02、URL https://unjuno.github.io/tensei-neural-network/serial/002.html 。mainの台帳にも同一source SHA/CIを記録。新たなEVT・研究試行・章の追加なし。
- 作業記録 `notes/runs/2026-11-02-evt005-status-normalization.md`。歴史的な失敗記録は上書きせず残す。

## 2026-11-03 第3話「表の外」公開用編集レビュー

- 出発点: work HEAD `0dcbcaffadaed8f837d8b56a9dcd4d8142731a4f`。最新story headはEVT-018、人物・世界の新事実追加なし。mainの公開台帳は第1・2話、latest Serial Publication run `41422224575` success（DAILY_LIMIT、公開済み002のDEPLOYEDを再照合）。
- 第3話本文とEVT-009〜011、一次資料識別子、review-lock、話別verification/terminology/semantic-reviewを照合。独立の整数計算で文献掲載16素子Qの局所入力16件が保存値に一致、ゼロなし・最小符号付き余裕5を確認。
- `publication/reviews/003.json` を本文blob `802424a3fc3504e766a6fdb24a791a455151900a` とreview-lock blob `339a92b80ea84c604384ee0353b98e78f00f493f` に固定し、5観点・blocking_issues空の限定AI編集PASSとして記録。本文・EVT・Canon・既刊スナップショットは変更しない。
- 第3話の準備commit 412fe914976bdf7e36a29dd3d8c44ee2a3345c7e のStory Workflow Validation run 41546992324はcompleted/success（unit tests、章別再実行と保存JSON、研究再実行、EXP-013照合、workflow validatorの各step成功）。Serial Publication run 41547099942はcompleted/success。2026-11-03 08:40 JSTにlive manifestと003.htmlのSHA-256一致を観測してDEPLOYED。公開URL: https://unjuno.github.io/tensei-neural-network/serial/003.html。公開台帳の003はsource SHAとCI、html SHA-256を記録。次は第4話を個別に編集レビューする。


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


## 2026-11-07 EVT-019「二つの問い」成立（第6話は未成立）

- 開始work HEAD: `5a784ddea18e6da5ee3bc6444eff399508286c61`。mainの公開許可はenabled=true。main公開台帳は第1〜5話で、第5話まで配信照合済み。最新観測Serial Publication run `42195420441` はsuccessで、live manifest/005.htmlを照合。新規公開はない。
- EVT-018後、PER-005は別の更新順への拡張を問いとして提示したが実験条件を決めず、PER-006は「同じ最終状態でも初期状態・経路が異なる」ことを実際の観測で区別する条件を自分で考える道を選んだ。二人は数学的検討と生理学的観測可能性を別々の問いとして残し、無目的なtrial追加と研究所への正式提出を見送った。
- 直接正本: `novel/events/EVT-019-two-questions.md`、`novel/state/personas/deltas/EVT-019.md`。ORG-001の権限・制度・institutional memoryは不変。古いworld snapshotを上書きせず、EVT-008〜019を一度だけoverlayして復元する。
- 結果選択を伴う新規trialなし。創作上の対話解決は同一制作文脈なのでprovenanceは`UNBLINDED`、独立生成の検証ではない。本文・話別pack・既刊・Canon・公開機構を変更しない。第6話はまだ自然な読書単位として確定していない。
- 実施・CI・未完了の詳細は`notes/runs/2026-11-07-evt019-two-questions.md`。実読者5名、独立restore、Human Review/Canon受理は引き続きOPEN。

検証追記（2026-11-07）: EVT-019制作commit `ae15b0e4f408ff09eb6db4e429ee406d1b3512b7` のStory Workflow Validation `42313337636` は全step success。Serial Publication `42313435915` は`NO_READY_CHAPTER`で新規公開なし、既刊005のlive照合成功。後続の記録更新commitもCI対象。

## 2026-11-08 文献読解・人物独立state（EVT-020）

- 2026-11-07のdirect story head EVT-019から再開し、PER-006佐伯玲子だけの既知Goal「modelの経路を生理学的にどう観測するか」を進めた
- 1975年の久保田競の原著（DOI `10.2170/jjphysiol.25.481`、REF-003）を作者側で一次資料照合。佐伯はその原著を**個人で参照するstory action**を行い、同じ単一unitでも異なる遅延課題の放電差が必ず一致しないことを読み取った
- 原論文報告の95 unitは研究全体の記録数であり同時95-channel測定ではない。発火頻度、課題区間、model内部Q/updateを同一視しない
- 新EVT: `novel/events/EVT-020-the-same-neuron-different-task.md`。persona delta: `novel/state/personas/deltas/EVT-020.md`。REF-003〜007と作者側の測定境界: `research/1980s-neurophysiology-observation-boundary.md`
- **高橋はこの論文読解を未観測**。ORG-001の設備・予算・所蔵・公式記録不変。動物実験・新数値trial・第6話なし。文献選択は作者の事後探索を含むためprovenance `UNBLINDED`
- 第1〜5話の公開・review-lockは変更せず、mainの`docs/serial/manifest.json`が公開版の正本。第6話のためだけに事件を作らない
- 日次制作自動化は開始時 `recorded_status=failed` かつ `enabled=false` だった。2026-11-08に `enabled=true` へ更新し再読で有効を確認した。ただし前回runのfailed判定は消えず、次回の実行成功は未確認

**次の一手:** REF-003の課題条件と神経発火活動の対応について、佐伯が誰に何を共有するか、あるいは高橋が独立に別のupdate scheduleの条件を先に固定するかを、当人の知識のみから解決する。模型の二値状態を神経活動の直接観測と偽らない。実読者・独立restore・Human Review・Canonは未完。

本件の実行とCIは `notes/runs/2026-11-08-primary-neurophysiology.md` を参照する。

## 2026-11-08 第6話「二つの時計」候補とEVT-021

- 起点work `3cac67761ffbc80b392eb75bfdef09cbc478cde5`。main委任`enabled=true`。開始時main既刊001〜005、Serial Publication `42402513886` successで既刊005のlive検証成功、新章配信なし。
- story head `EVT-020 -> EVT-021`。佐伯の1975原著読解の**限定した口頭共有**を初めて高橋が聞き、模型の離散更新番号と生理学の課題区間/発火時刻の対応が未定義と二人で認め、私的共同メモへ別欄を作った。新試行・組織承認なし。UNBLINDEDな創作対話。
- EVT-019〜021の三段階が自然な読書単位になったため`novel/chapters/006.md`を制作。話別史料/knowledge boundary verification、意味レビュー、用語、review-lock、AI限定編集レビューを同一本文版で作成。001〜005本文と既刊スナップショット不変。
- この作業を含む新commitのCIと実公開は記録時点で未観測。mainのmanifestに第6話が追加され、Serial Publicationのlive manifest/006.html hash一致を確認するまでは**第6話は未公開**。Canon受理、独立読者5名・独立restoreは未実施。
- 再開: `notes/runs/2026-11-08-chapter-006-two-clocks.md`、`novel/events/EVT-021-two-clocks.md`、`novel/state/personas/deltas/EVT-021.md`。次のstory側は二人の局所目標から選択し、次の実験を第7話のノルマで作らない。
