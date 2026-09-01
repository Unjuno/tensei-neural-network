# 第2話「選ばなかった答え」公開前検証

状態: `PREPUBLICATION_GATE_PASSED`

対象本文:

- `novel/chapters/002.md`
- `novel/chapters/002-outline.md`

採用event:

`EVT-005 -> EVT-006 -> EVT-007 -> EVT-008`

## Mandatory Verification

`verification.md`: `PASS`

独立した`run.py`でEVT-005〜008を再構成し、6 cyclic orders、36 balanced-cue trials、384 full-state trials、6 fixed points、D=-C、符号反転可換性を再現した。保存結果は`results.json`。

検証初回にはD/-Cの時点別label衝突により1 checkがFAILした。これは隠さずverificationへ記録し、EVT-005/006のhistorical label `D` とEVT-007以降のcanonical classification `-C`を分離して修正した。

## Semantic Review

`semantic-review.md`: `PASS`

- EVT/stateからのknowledge leakageなし
- 具体年月日・機種・OS・languageを捏造していない
- finite toy networkを一般の脳・記憶へ一般化していない
- D→-Cの認識転換順を保持
- LOCKED event結果を章末都合で変更していない

## Terminology

`terminology.md`: `PASS`

本文で実使用した語だけを確認。第1話と同じく日本語説明を優先し、不要な英語ルビ・後世語彙を導入していない。

## Gate verdict

第2話は現在のevidenceに対して公開前gateを通過した。

これは人間による最終採用・`main`への昇格を意味しない。また、歴史・科学上の絶対的正しさを保証するものではない。
