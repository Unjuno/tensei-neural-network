# 第4話「五と二十一」公開前検証

状態: `IN_PROGRESS`

更新: 2026-09-11
対象: `novel/chapters/004.md`
採用event: EVT-012 -> EVT-013。

## 現在の再検証

2026-09-11の読者視点監査で、Qの成分多数と安定性の導出は正確だが、距離→内積→入力式という説明が連続し、最も読書速度を失う章と判断した。

EVT-012/013の数値・式・結論は変えず、既知の「5と21」を先に謎として置き、成分比較がその二つの値を説明する順へNarrativeProjectionを再構成する。完全な証明はverification側へ保持し、本文では読者が因果を追える最小限の式だけ残す。

旧 `PREPUBLICATION_GATE_PASSED` は改稿版へ自動継承しない。改稿後、既存検証・用語・意味レビューを再確認し、`review-lock.json` を新しい本文版へ更新してからcandidate gateへ進める。

## 既存検証資産

- `verification.md`
- `run.py`
- `results.json`
- `terminology.md`
- `semantic-review.md`

数理条件は今回変更しない。

## Gateの意味

科学的真理、文学的完成、独立した読者評価、人間の受理を自動保証しない。main反映・PR・docs同期・公開は別工程。
