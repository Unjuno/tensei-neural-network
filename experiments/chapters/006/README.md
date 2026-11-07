# 第6話「二つの時計」公開前検証

状態: `PREPUBLICATION_GATE_PASSED`

対象本文: `novel/chapters/006.md`
採用event: EVT-019 -> EVT-020 -> EVT-021

- `verification.md`: PASS / MIXED（1975年原著の範囲と人物の知識境界を実際に照合）
- `semantic-review.md`: PASS / AI再読。実読者・独立blindの代替ではない
- `terminology.md`: PASS、blocking未検証語なし
- `review-lock.json`: 本文、採用EVT、必須依存のGit blob SHA-1を対象版として固定
- `publication/reviews/006.json`: 同一本文/lock blobに対する五観点のAI限定編集評価
- 新しい数値実験は発生していないため、この話に`run.py`/`results.json`はない。既刊の実行可能話別検査は全repo CIで再実行する

**このgateが意味すること:** 採用EVT・史料・観測境界に照らし公開を妨げる既知矛盾が見つからない候補版。新しい科学的発見、実読者評価、Human Review、Canon受理ではない。main/docs/serialへの出版はSerial Publicationだけが実施する。source HEADのCI成功前・Pages配信確認前は`DEPLOYED`ではない。
