# 2026-11-07 制作記録 — EVT-019 二つの問い

## 起点・委任

- 開始main HEAD: `919e1b8541c2627ad2210c086b9861892cb250bc`。
- 開始work HEAD: `5a784ddea18e6da5ee3bc6444eff399508286c61`。
- main `publication/policy.json`: `enabled=true`、公開の委任は連載スナップショットだけ。mainへのwork merge、Canon受理、PR、外部投稿をしない。
- main `docs/serial/manifest.json`: 第001〜005話。最新Serial Publication run `42195420441`（2026-11-06 09:29 UTC）はsuccess、live manifestと005.htmlのhash照合step成功。新規公開対象なし。

## 今回の有限制作単位

- 前story head: `EVT-018` → 後: `EVT-019`（1980年代側）。現代側head: none。
- 新event: `novel/events/EVT-019-two-questions.md`。PER-005とPER-006の既知の結果と別々のGoalsから、追加計算と生理学的観測可能性を別の未解決問いとして残す対話を解決。
- 同期state: `novel/state/personas/deltas/EVT-019.md`。ORG-001のinstitutional memory・権限・資源は変更なし。古いworld checkpointは書き換えずevent/delta overlayを維持。
- 変更章: なし。第6話は自然な読書単位未成立。既刊第001〜005話、publication/reviews、review-lock、Canon、mainの公開機構は不変。新規研究EXPなし。
- 生成方式: `UNBLINDED`。同一制作文脈での社会的対話を独立創発・科学的実証として主張しない。未採用scene-probeは未採用のまま。

## 検証・CI

- 事前確認: mainの停止switch、work HEAD、最新CI run `42192415686` success（開始HEAD）、既刊台帳と最新公開run、EVT-018・persona/ORG定義と状態・差分・第5話・未採用scene-probeを照合。
- 変更はMarkdown event/state/index/runに限定。新数値trialがないため話別結果JSONやreview-lockを再生成する対象はない。
- 新commit: CI実行後に追記。workflow validator、unit tests、既存話別再実行と保存JSON、研究再実行の結果は新commitのCIで確認する。未確認の段階ではPASSとしない。

## 公開状態・残課題・次の一手

- 第001〜005話は既刊。第006話は未作成・未公開。新しい実公開の断定なし。
- 未解決: 実読者5名の試読、独立restore、Human Review、Canon受理、当時の具体的測定手段、追加schedule familyの事前条件。
- 次: EVT-019後の局所状態から、佐伯の観測可能量の文献探索または高橋の拡張条件の選択を、当時利用可能な一次資料・ORG制約で解決する。実験は条件を結果前commitしてから。読書単位が成立した場合だけ第6話へ投影する。
