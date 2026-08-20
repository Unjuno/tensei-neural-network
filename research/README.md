# Research

このディレクトリは、現実世界の調査・問い・仮説・研究レポート・知見を管理します。

**小説本文とは分離します。**

小説を研究レポート風に構成せず、物語中で人物が実際に観測したこと・口にした言葉・失敗・違和感から、検証可能な問いが生じた場合だけ研究側へ切り出します。

## 基本ループ

```text
物語の現在状態
    ↓
人物と世界が動く
    ↓
実際に出た言葉・観測・疑問
    ↓
検証可能か判断
    ↓ yes
research/questions.md
    ↓
research/hypotheses.md
    ↓
experiments/EXP-xxx-*/
    ↓
research/reports/EXP-xxx.md
    ↓
research/findings.md
```

研究結果を物語へ戻す場合も、人物がその結果を物語世界で実際に観測できるかを確認します。

現代の作者側で行った実験結果を、1980年代の人物へ未来知識として直接与えません。

## ファイルの役割

- `questions.md` — 現実側で答える問い `Q-xxx`
- `hypotheses.md` — 反証可能な仮説 `H-xxx`
- `reports/` — 個別実験を研究として読める形にしたレポート
- `findings.md` — 複数の証拠から現時点で言えること `F-xxx`
- `pre-hopfield-background.md` — Hopfield以前〜1980年代の背景調査
- `1980s-research-environment.md` — 1980年代の研究環境調査
- `../experiments/` — 実行条件、コード、raw result、PASS/FAIL/UNCERTAINの正本

## 一話と実験を対応させない

- 一話 = 一実験にしない
- 一つの話から複数の研究課題が生じてもよい
- 研究課題が一つも生じない話があってよい
- 一つの実験結果が複数の後続場面へ影響してよい
- EXP番号を話数として使わない

## 派生実験

追試やExtensionから新しい問いが生じた場合、判定対象が変わるなら新しいEXPとして分離します。

例:

```text
EXP-001 Replication
    ↓
EXP-002 boundary Extension
    ↓
物語EVT-001で「その状態は何からできている？」という問いが成立
    ↓
Q-003 / H-003
    ↓
EXP-003 mixture structure
    ↓
research/reports/EXP-003.md
```

この系列は研究の因果関係であり、小説の章構成ではありません。

## 最初の実例

`EVT-001` でPER-005が、

> 保存していないところで止まるなら、その状態は何からできている？

という問いを残した。

そこから現実側でQ-003 / H-003 / EXP-003を独立に作り、EXP-002の `NONSTORED_CONVERGED` を3-pattern majority mixtureとの関係から解析した。

結果は `research/reports/EXP-003.md` に保存する。

この結果はPER-005の物語内知識ではない。
