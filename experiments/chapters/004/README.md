# 第4話「五と二十一」公開前検証

状態: `GATE_CANDIDATE`

更新: 2026-09-11
対象: `novel/chapters/004.md`
採用event: EVT-012 -> EVT-013。

## 読者ロス改稿

距離→内積→入力式という説明順を、既知の5/21を先に謎として置き、成分比較と一つの式で解く順へ再構成した。完全な導出はverification側へ残し、本文では因果を追うために必要な式だけを保持した。

EVT-012/013の数値・式・結論は変更していない。詳細は `../../../notes/reader-loss-audit-2026-09-11.md`。

## 再レビュー

- `verification.md`: 既存数理条件を再確認
- `run.py` / `results.json`: 変更なし
- `terminology.md`: 新規blocking語なし
- `semantic-review.md`: knowledge / projection / interpretation boundaryを改稿版で再確認
- `review-lock.json`: 改稿後本文blobへ更新済み

candidate CI成功後のみ `PREPUBLICATION_GATE_PASSED` へ戻す。

## Gateの意味

科学的真理、文学的完成、独立した読者評価、人間の受理を自動保証しない。main反映・PR・docs同期・公開は別工程。
