# 定期制作・連載公開ループ

状態: ACTIVE / DELEGATED_SERIAL_ONLY
委任根拠: 2026-10-31の「定期実行で公開するプロセスを組み、話数を更新するシステムとして作業開始」というユーザー依頼。

## 許可の範囲

既存GitHubリポジトリとPagesの**連載版**について、ここに定めるゲート後の新規章公開を継続委任として扱う。過去の「毎回公開承認が必要」という運用に対する今回の限定的な許可であり、Canon・研究Findingの科学的真理・実読者合格・全work branchのmain受理を意味しない。

自律的に変更してよい公開先はmainの`docs/serial/`のみ。初回導入では本書、`publication/policy.json`、`tools/serial_publish.py`、`tests/test_serial_publish.py`、`.github/workflows/serial-publication.yml`をmainへ追加する。work branchをmainへmerge/fast-forwardしない。既存docs/novel・research・Canonを置換しない。PR・他サイトへの投稿・API契約・費用追加はしない。

## 二つの実行主体

制作担当: 既存ChatGPT日次タスク（日本時間の朝8時ごろ）。work/story-bootstrapで状態復元→人物/世界→自然な読書単位→本文→話別検証→意味レビュー→読者視点レビューを行う。1回に一つの有限な成果を残し、未完の章は翌回へ引き継ぐ。研究のために章や事件を作らない。未採用scene-probeをEVTや公開本文と取り違えない。

公開担当: mainのGitHub Actions。毎日UTC 02:17（日本時間11:17）、source CI完了、機構変更、手動起動で候補を確認。スケジュールは遅延し得る。mainの信頼済みコードだけを実行し、work側の実験コードをwrite権限の下で実行しない。

## 公開条件

1. 最新work HEADを固定し、同じSHA・同じrepo・指定workflowの最新CI runがcompleted/successである。
2. 章は既刊直後の番号で、packageがPREPUBLICATION_GATE_PASSED。未解決EVT・blocking用語・検証失敗を含まない。
3. review-lockの必須依存と全記録hashが一致する。コード実験には個別checksが全てtrueの結果を要求する。再実行はsource CI側で行う。
4. `publication/reviews/NNN.json`が同一本文blobと同一review-lock blobを指定し、5観点の具体的編集評価、空のblocking_issues、PASSを持つ。AIの役割変更を独立読者に数えない。
5. 既刊のHTML/Markdown hashが台帳と一致し、同日未公開である。日本時間で最大1話/日。章の欠番を飛び越さない。
6. 前回の配信が未確認なら新規公開せず、前の配信を再試行。実際の公開manifestと最新HTMLのhashが一致して初めてDEPLOYEDと報告する。

## レビューを書く方法

`001.json`が書式例。本文を実際に読み、reader_question（何を知りたいか）、character_agency（人物の選択）、exposition_load（説明負荷）、event_fidelity（成立済みEVTとの対応）、ending（自然な切れ目）を具体箇所で記録する。未読の章に例を機械コピーしてPASSにしない。

本文または証拠を改稿したら既存話別gateを再実行し、reader-reviewも再読して更新する。hashだけ更新しない。実読者5名のpilotは別系統のOPEN課題として保持するが、ユーザーが委任した暫定連載の公開と混同しない。

## 台帳・失敗・停止

`docs/serial/manifest.json`に公開番号、日付、source SHA、CI run、本文/HTMLのSHA-256、レビューblobを保存する。これは公開用スナップショットでありsource fileは公開後も研究側に残す。既刊内容を黙って置換する機能はない。改訂は別途人間承認と版番号の設計が必要。

`PAUSED`、`NO_READY_CHAPTER`、`DAILY_LIMIT`は正常な無変更。`BLOCKED`は検証/権限/整合の障害。`RETRY_DEPLOY`は以前の成果物を配信する。`READY`は生成準備であって公開完了ではない。`DEPLOYED`はURL内容一致を観測した場合のみ。

緊急停止: **main/publication/policy.jsonのenabledをfalseにする**。制作タスクは既刊を保ったまま停止理由を報告する。接続権限を回避しない。mainとworkの同名policyが異なればmainを公開権限の正本とする。

競合時はnon-force pushで停止し、次回最新HEADから復元する。複数publish jobは同じconcurrency groupで直列化。最大実行時間15分。失敗を成功に書き換えず、同じ障害が続く場合は新規話数を稼がず原因を修正する。

## Pages前提

既存Pagesがmain/docsのbranch公開の場合、GITHUB_TOKENのcommitが自動ビルドを誘発しないため、Pages APIでbuildを明示要求する。Actions公開の場合はdocsのみをartifact化してdeploy-pagesへ渡す。別branch・別path・別ドメインの場合は勝手に設定を変えず停止する。

公式根拠:
- https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows
- https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site
- https://docs.github.com/en/rest/pages/pages

## 実装変数・条件

| 識別子 | 意味 | SI単位 | 定義 | 範囲・前提 | 型 |
|---|---|---|---|---|---|
| head | 読取対象版 | 非該当 | Git commit SHA | 40桁小文字hex・CI対象と同一 | 文字列 |
| chapter | 話番号 | 1 | 既刊数の次の3桁番号 | 001〜999、連続 | 文字列 |
| date | 日次上限の基準日 | 非該当 | Asia/Tokyo暦日 | ISO日付・過去台帳より前にしない | 文字列 |
| files | 生成対象 | 非該当 | docs/serial配下の本文・HTML・台帳 | 許可pathのみ | 辞書 |
| enabled | 緊急停止 | 1 | main側の公開許可 | true/false | 真偽値 |

日時を物語時間と混同しない。hashと件数は物理量ではなく、実行上限だけが時間量。数字の増加を文学的成功の指標にしない。
