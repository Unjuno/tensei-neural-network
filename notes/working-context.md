# 作業コンテキスト

更新: 2026-11-03。再開のための索引。秘密情報や逐語的内部推論は保存しない。

## 現在位置

repo: Unjuno/tensei-neural-network。制作はwork/story-bootstrap。story headはEVT-018、現代側none。PER-005高橋修一・PER-006佐伯玲子・ORG-001がactive。章1〜5は技術gate済み。

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

第2話「選ばなかった答え」は2026-11-02に連載公開済み。源版 `3e363989f25fccdfb3c4b75dd6a169f48f85da16`、CI `41360865674` success、公開run `41360920516` success、実配信manifestと002.htmlのSHA-256一致を確認した。公開台帳はmain/docs/serial/manifest.json。EVT-005旧状態表記のBLOCKEDは2026-11-01の履歴として保持。第3話は2026-11-03にAIによる公開用編集レビューを作成（新source CIと配信の確認は未了）。第4〜5話は未公開・公開用編集レビュー未実施。レビューを機械コピーしない。

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
- 直前の公開台帳は001/002のみ。latest Serial Publication `41422224575`はDAILY_LIMIT / 既刊002 DEPLOYEDの再照合。第3話の配信成功は未確認。
- 今回新EVT、新実験、新章本文改稿、Canon昇格なし。次はCI/公開配信を検証し、未公開なら阻害要因を先に解消。公開が成立したら第4話を個別に再読・編集評価する。
