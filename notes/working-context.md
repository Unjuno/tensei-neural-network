# 作業コンテキスト

更新: 2026-10-31。再開のための索引。秘密情報や逐語的内部推論は保存しない。

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

第2〜5話は未公開。現時点でpublication/reviewsは001だけ。次回002を実読してレビューし、必要なら本文→意味/用語/数理→lock→CIへ戻す。レビューを機械コピーしない。

## 初回統合で得た修正

初回は旧EVTの状態がPROVISIONALで止まった。成立済みの初期4eventだけを固定blob hashで識別する互換adapterを追加し、未知/改変PROVISIONALやACTION_LOCKEDは引き続き拒否。29件のエンジン回帰テストが成功。詳細はnotes/runs/2026-10-31-publication-loop.md。

## 物語状態と未採用場面

EVT-014〜018はQのone-bit近傍の256件（Q112、保存3記憶各48）、距離分類、最初の実flip、不安定4点、円環gapによる件数説明を扱った。割合を自然確率にしない。

古いsnapshotがEVT-007で止まっていても、EVT-008〜018と対応deltaから一度だけ復元する。作者側EXP-006以後の一般化や証明は人物へ自動注入しない。

novel/scene-probes/2026-10-31-circle-and-original-records.mdは未採用。発話や資料保存、研究所提出を事実に昇格していない。採用したいなら現在personaの観測とGoals、ORGの制約から正規のworld advancementとして判断する。

## 継続時の確認

最初にmainの停止スイッチ、最新source HEAD、直接EVT、CI、公開台帳と公開workflowの観測結果を確認。公開失敗はREADY/記録済みとDEPLOYEDを分ける。競合なら最新HEADから読み直しforce pushしない。結果に影響する実験は結果前commit、成果は失敗も保持。

実読者5名、Human Review/Canon受理、独立した別主体の意味復元は未完。定期公開が始まっても完了扱いしない。未確定の具体年/所在地/職位/計算機/人物の生活史を章都合で埋めない。
