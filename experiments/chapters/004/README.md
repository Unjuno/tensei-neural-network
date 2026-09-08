# 第4話「五と二十一」公開前検証

状態: `GATE_CANDIDATE`

更新: 2026-09-08
対象: `novel/chapters/004.md`
採用event: EVT-012 -> EVT-013。

## 今回の再検証

旧稿のgate通過を新稿へ流用しない。改稿後の本文・outline・検証・意味レビュー・用語・採用EVTを `review-lock.json` で版指定した。

- Mandatory Verification: `verification.md` / `run.py` / `results.json`
- Semantic Review: `semantic-review.md`
- Terminology: `terminology.md`
- 評価と長期目標: `../../../notes/assessment-and-roadmap.md`

ローカル再実行はPASS。独立試読・人間の受理は未実施。候補commitに対する全repo CIを確認してから、工程gateの通過状態へ進める。

## Gate条件

テスト、全話コード再実行と保存JSON照合、review-lock鮮度、厳格workflow検査が全て成功すること。CIはreview-lockやresultsを自動更新しない。

`PREPUBLICATION_GATE_PASSED`は科学的真理や文学的完成の保証ではなく、現在対象版に対する工程判定。main反映・PR・docs同期・公開の承認ではない。
