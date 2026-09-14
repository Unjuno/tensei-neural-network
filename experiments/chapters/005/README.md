# 第5話「最初に動いたもの」公開前検証

状態: `PREPUBLICATION_GATE_PASSED`

対象: `novel/chapters/005.md`
採用event: EVT-014 -> EVT-018。

## Mandatory Verification

- `verification.md`: PASS
- `run.py` / `results.json`: EVT-014〜018の中心数値を再現
- `terminology.md`: PASS
- `semantic-review.md`: PASS
- `review-lock.json`: 対象本文・採用EVT・検証入力を固定済み

## Candidate CI

candidate commit: `87e15a6e37182e295d9c5c338115de05ef586039`
GitHub Actions run: `34817720509`
job: `103891943770`
result: `success`

validator tests、第1〜5話の実行可能verification、作者側research experiment再実行、review-lock鮮度、strict workflow validationが成功した後にgateへ昇格した。

## Gateの意味

数理・event整合の公開前gateであり、独立実読者の理解、文学的完成、Human Review、main反映を意味しない。
