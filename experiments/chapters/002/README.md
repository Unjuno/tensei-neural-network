# 第2話「選ばなかった答え」公開前検証

状態: `PREPUBLICATION_GATE_PASSED`

更新: 2026-09-11
対象: `novel/chapters/002.md`
採用event: EVT-005 -> EVT-006 -> EVT-007 -> EVT-008。

## 読者ロス改稿

6件→36件→384件という検査手続きの反復を圧縮し、Dの出現、Cへの到達、D=-Cの再分類を読書上の三つの転換として前景化した。

EVT・数値・認識順序・符号反転対称性は変更していない。詳細は `../../../notes/reader-loss-audit-2026-09-11.md`。

## 再レビュー

- `verification.md`: 既存数理条件を再確認
- `run.py` / `results.json`: 変更なし
- `terminology.md`: 新規blocking語なし
- `semantic-review.md`: 既存判定項目に対して改稿版を再確認
- `review-lock.json`: 改稿後本文blobへ更新済み

## Candidate CI

candidate commit: `bdc69e9f91ba08428c556e488fa66eccb9d97668`
GitHub Actions run: `34503727557`
job: `102960602443`
result: `success`

validator tests、4話の実行可能verification、保存結果照合、review-lockを含むworkflow検査が成功した後にgateへ戻した。

## Gateの意味

科学的真理、文学的完成、独立した読者評価、人間の受理を自動保証しない。main反映・PR・docs同期・公開は別工程。
