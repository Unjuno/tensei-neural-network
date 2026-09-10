# 第3話「表の外」公開前検証

状態: `GATE_CANDIDATE`

更新: 2026-09-11
対象: `novel/chapters/003.md`
採用event: EVT-009 -> EVT-010 -> EVT-011。

## 読者ロス改稿

文献選択の説明と16素子Qの検算を圧縮し、六素子表の空白から別模型のQが残るまでを一本の読書導線にした。5/21の二種類だけが残ることを次話の謎として明示した。

EVT・一次資料・Qの安定性・stored/negation外という結論は変更していない。詳細は `../../../notes/reader-loss-audit-2026-09-11.md`。

## 再レビュー

- `verification.md`: 既存数理条件を再確認
- `run.py` / `results.json`: 変更なし
- `terminology.md`: 新規blocking語なし
- `semantic-review.md`: knowledge / history / projection / provenanceを改稿版で再確認
- `review-lock.json`: 改稿後本文blobへ更新済み

candidate CI成功後のみ `PREPUBLICATION_GATE_PASSED` へ戻す。

## Gateの意味

科学的真理、文学的完成、独立した読者評価、人間の受理を自動保証しない。main反映・PR・docs同期・公開は別工程。
