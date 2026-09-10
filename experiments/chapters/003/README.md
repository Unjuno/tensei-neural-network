# 第3話「表の外」公開前検証

状態: `IN_PROGRESS`

更新: 2026-09-11
対象: `novel/chapters/003.md`
採用event: EVT-009 -> EVT-010 -> EVT-011。

## 現在の再検証

2026-09-11の読者視点監査で、六素子模型の空白から1983年文献へ移る因果は明瞭だが、文献選択説明と16素子候補の検算が続く中盤で、人物の発見感より手続き説明が前景化すると判断した。

EVT・一次資料・Qの安定性・stored/negation外という結論は変えず、「この模型にはない」から「別条件ではある」へ移る落差と、Qが残った瞬間を前面に出す。

旧 `PREPUBLICATION_GATE_PASSED` は改稿版へ自動継承しない。改稿後に既存検証を再確認し、`review-lock.json` を更新してからcandidate gateへ進める。

## 既存検証資産

- `verification.md`
- `run.py`
- `results.json`
- `terminology.md`
- `semantic-review.md`

数理条件・歴史資料は今回変更しない。

## Gateの意味

科学的真理、文学的完成、独立した読者評価、人間の受理を自動保証しない。main反映・PR・docs同期・公開は別工程。
