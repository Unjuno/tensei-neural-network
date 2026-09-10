# 第2話「選ばなかった答え」公開前検証

状態: `IN_PROGRESS`

更新: 2026-09-11
対象: `novel/chapters/002.md`
採用event: EVT-005 -> EVT-006 -> EVT-007 -> EVT-008。

## 現在の再検証

2026-09-11の読者視点監査で、数理的不整合ではなく、6件→36件→384件という検査手続きの反復が発見そのものより前景化し、読書速度を落とす箇所があると判断した。

EVT・数値・認識順序を変えず、Dの出現、Cへの到達、D=-Cの再分類という三つの転換を前面に出すNarrativeProjectionへ改稿する。

旧 `PREPUBLICATION_GATE_PASSED` は改稿版へ自動継承しない。改稿後、既存Mandatory Verification / terminology / semantic reviewを再確認し、`review-lock.json` を新しい本文版へ更新してから `GATE_CANDIDATE` へ進める。

## 既存検証資産

- `verification.md`
- `run.py`
- `results.json`
- `terminology.md`
- `semantic-review.md`

数理条件は今回変更しない。

## Gateの意味

科学的真理、文学的完成、独立した読者評価、人間の受理を自動保証しない。main反映・PR・docs同期・公開は別工程。
