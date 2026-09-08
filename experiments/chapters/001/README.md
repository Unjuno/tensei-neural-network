# 第1話「戻る先」公開前検証

状態: `PREPUBLICATION_GATE_PASSED`

更新: 2026-09-08
対象: `novel/chapters/001.md`
採用event: EVT-001 -> EVT-002 -> EVT-003 -> EVT-004。

## 今回の再検証

旧稿のgate通過を新稿へ流用せず、改稿後の本文・outline・検証・意味レビュー・用語・採用EVTを `review-lock.json` で版指定した。

Mandatory Verificationは `verification.md` / `run.py` / `results.json`、意味レビューは `semantic-review.md`、用語検証は `terminology.md`。全体評価と長期目標は `../../../notes/assessment-and-roadmap.md`。

## Candidate CIの実測結果

候補commit: `8818e03ca04555c52baf65ac5fd3be00bc38596d`
GitHub Actions run: `34173177998`
Job: `101897324083`、完了結果 `success`。

https://github.com/Unjuno/tensei-neural-network/actions/runs/34173177998

CPython 3.12.14 / Ubuntu 24.04.4上で、40件のunit tests、4話すべてのコード再実行と保存JSON全項目照合、対象版の鮮度を含むworkflow検査が成功した。候補版には未完成状態の章はなく、4話とも本番相当のgate条件を適用した。

作業branchの実行コマンドは `--strict --allow-drafts`。免除対象のWF060は今回のrepo検査で発生していない。unit test内で表示されるFAILは意図的に壊したfixtureの期待結果である。

## Gateの意味

今回の昇格は上記候補CI成功の後に行った。CIはreview-lockやresultsを自動更新しない。

科学的真理、文学的完成、独立した読者評価、人間の受理を保証する状態ではない。独立試読・公開承認は未実施。main反映・PR・docs同期・公開は行っていない。
