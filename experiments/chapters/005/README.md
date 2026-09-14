# 第5話「最初に動いたもの」公開前検証

状態: `IN_PROGRESS`

対象: `novel/chapters/005.md`
採用event: EVT-014 -> EVT-018。

## Mandatory Verification

- `verification.md`: PASS
- `run.py` / `results.json`: EVT-014〜018の中心数値を再現
- `terminology.md`: PASS
- `semantic-review.md`: PASS

## 現在位置

本文・outline・verification・terminology・semantic reviewは作成済み。

次に`review-lock.json`で対象版を固定し、`GATE_CANDIDATE`へ上げてCIを通す。

## Gateの意味

数理・event整合の公開前gateであり、独立実読者の理解、文学的完成、Human Review、main反映を意味しない。
