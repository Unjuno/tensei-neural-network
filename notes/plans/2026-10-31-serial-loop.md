# 連載公開ループ 設計・実装計画

目的: 既存の日次制作タスクと、検証済み本文を1日最大1話公開する決定論的な工程を接続する。

## 許可と非目標
2026-10-31のユーザー依頼を、既存のGitHub公開先に対する継続的な連載版公開の委任として記録する。mainへのwork branch一括merge/fast-forward、Canon昇格、他サイト投稿、有料API追加は含まない。
mainへの変更は公開機構（publication/、tools/serial_publish.py、tests/test_serial_publish.py、専用workflow）と生成物docs/serial/に限定する。既存のdocs/novel/・research/や正史を置き換えない。

## 方式比較
全work branchをmainへ自動mergeする案は未受理研究とCanonを混ぜるため不採用。別ホスティング追加は接続・費用を増やすため不採用。既存main/docsへ新しいserial領域を追加し、固定commitの本文だけ公開する方式を選ぶ。

## 仕組み
制作: ChatGPT既存タスクを毎日午前8時ごろ継続。一回一つの有限作業。自然な読書単位ができた場合だけ章化。各話の再現検証・意味レビュー・読者視点レビューを分離。
公開: mainの専用workflowが毎日UTC 02:17（JST 11:17）と手動起動、mainの機構変更で稼働。固定work HEADに対するCI success、gate、全review-lock、本文と対応する読者レビュー、章順を確認。実行するのはmainの信頼済みPythonだけ。work側コードを公開用write-tokenの下で実行しない。
公開台帳: docs/serial/manifest.json。既刊HTML/Markdownを内容hashで凍結。1日最大1話。配信未確認の台帳がある場合は新話を作らず配信を再試行する。競合はnon-force git pushで停止。
公開先: 既存Pages設定をGETしmain/docsのbranch公開なら明示的なPages buildを要求、Actions公開ならdocsだけartifactとしてdeploy。設定が異なる場合は書込前に停止し、勝手に切り替えない。
緊急停止: main/publication/policy.jsonのenabled=false。CI successは文学的成功・実読者評価ではない。

## 実装計画
- [x] tests/test_serial_publish.py: stale lock、draft、章飛ばし、重複、日次上限、停止、script埋込、symlink、reader版不一致、旧CI、台帳破損をREDで確認。
- [x] tools/serial_publish.py: 読取/審査/安全HTML/台帳/CLI。標準ライブラリのみ。26 tests PASS。
- [x] main専用workflowを作成: 固定HEAD/CI照合、最小書込、排他、Pages設定確認/配信、HTML/hash確認。
- [x] 第1話だけ実読・既存根拠照合してpublication/reviews/001.json作成。他章は自動承認しない。
- [ ] work CI→mainへ公開機構のみ導入→実配信結果確認。失敗は未公開として記録。
- [ ] 既存Automationsのpromptを更新。モデル/Pro指定を勝手に保証しない。

## 完了基準と限界
機械検査の正常/破壊fixture、再実行時の無変更、対象版鮮度、公開経路の実行結果を確認する。実読者をAIで代替せず、未来プロットを増やさない。配信障害は工程完了としない。計測値は実行件数・公開結果だけで、品質改善率は捏造しない。
