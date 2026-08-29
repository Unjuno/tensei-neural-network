# 第1話 Mandatory Verification

状態: `PASS`

種別: `EXECUTABLE_REPRODUCTION`

## 検証対象

第1話が依存する最も壊れやすい主張として、EVT-004の6要素networkにおける更新順序依存を選ぶ。

## なぜこの検証を選ぶか

第1話の中心的な認識変化は、同一初期状態・同一結合・同一更新規則でも、更新順序だけでA/Bの異なる安定状態へ到達する具体例に依存するため。

話数を成立させるために新しい実験現象を追加したのではなく、成立済みEVTを本文へ投影した後、その本文が依存する主張を公開前に再確認している。

## Evidence

- `experiment.md` — 検証条件、事前合否条件、解釈
- `run.py` — 再実行可能な最小実装
- `results.json` — 保存済み結果
- `novel/events/EVT-004-same-cue-two-returns.md`
- `novel/chapters/001.md`

## 実行結果

`experiment.md` の条件で再実行し、

- alpha -> A
- beta -> B
- 到達後の次の一巡で双方とも変化なし

を確認した。

判定: `PASS`

## 境界

このPASSはEVT-004の数理的再現性を確認する。

EVT-004生成時の`UNBLINDED` provenanceやselection biasを解消しない。また、人間の記憶一般についての主張を検証したものではない。

## 本文への反映

中心描写と再現結果は一致したため、この検証による本文修正は不要。
