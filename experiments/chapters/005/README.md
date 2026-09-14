# 第5話「最初に動いたもの」公開前検証

状態: `GATE_CANDIDATE`

対象: `novel/chapters/005.md`
採用event: EVT-014 -> EVT-018。

## Mandatory Verification

- `verification.md`: PASS
- `run.py` / `results.json`: EVT-014〜018の中心数値を再現
- `terminology.md`: PASS
- `semantic-review.md`: PASS
- `review-lock.json`: 対象本文・採用EVT・検証入力を固定済み

## Candidate gate

この状態でGitHub Actionsを実行し、

- validator tests
- 第1〜5話の実行可能verification
- EXP-006〜011再実行
- review-lock鮮度
- strict workflow validation

が成功した場合のみ`PREPUBLICATION_GATE_PASSED`へ進める。

## Gateの意味

数理・event整合の公開前gateであり、独立実読者の理解、文学的完成、Human Review、main反映を意味しない。
