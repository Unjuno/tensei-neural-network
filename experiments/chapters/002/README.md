# 第2話「選ばなかった答え」公開前検証

状態: `IN_PROGRESS`

対象本文:

- `novel/chapters/002.md`
- `novel/chapters/002-outline.md`

採用event:

`EVT-005 -> EVT-006 -> EVT-007 -> EVT-008`

## 現在の位置

第2話本文の初稿を作成した。まだ `PREPUBLICATION_GATE_PASSED` ではない。

Mandatory Verification、terminology review、semantic reviewを実施してから公開候補判定する。

## 主な検証対象

- EVT-005の6 cyclic ordersと結果 A:1 / B:2 / D:3
- EVT-006の6 balanced cues × 6 orders = 36 trialsという手順
- EVT-007の64 states × 6 orders = 384 trials、6 fixed points、D=-C
- EVT-008のglobal sign-inversion symmetryの説明
- 本文が有限toy networkの結果を一般の記憶・脳へ一般化していないこと
- 「先に検査集合を固定する」という研究手順が、1980年代人物の観測可能範囲だけから描かれていること

## Mandatory Verification

`verification.md` を参照。

現段階では `IN_PROGRESS`。第2話では、EVT-005〜008の数理結果を独立に再計算する executable reproduction を第一候補とする。

## Semantic Review

未実施。`semantic-review.md` を作成して固定フォーマットで確認する。

## Terminology

未実施。本文で実際に使用した語だけを `terminology.md` へ抽出する。

## 公開判定

現時点: `NOT READY FOR PUBLICATION`

理由:

- 初稿は成立済みEVTからprojection済み
- ただしMandatory Verification未完了
- terminology review未完了
- semantic review未完了
