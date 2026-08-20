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

研究の因果関係は小説の章構成とは別です。

## 物語由来研究の実例

### EVT-001 → EXP-003

PER-005:

> 保存していないところで止まるなら、その状態は何からできている？

この問いからQ-003 / H-003 / EXP-003を独立に作り、EXP-002の `NONSTORED_CONVERGED` を3-pattern majority mixtureとの関係から解析した。

- EXP-003: PASS
- F-003: PROVISIONAL
- report: `reports/EXP-003.md`

### EVT-002 → EXP-004

PER-006:

> 手掛かりだけを見たときに二つの記憶が同じくらいもっともらしかったら、networkはどちらを「正解」だと知る？

この問いからQ-004 / H-004 / EXP-004を独立に作った。

二つのstored patternsへHamming等距離となる同一cueを固定し、非同期update orderだけを変更した。

- balanced cues: 200
- runs: 4000
- BIDIRECTIONAL cues: 122
- EXP-004: PASS
- F-004: PROVISIONAL
- report: `reports/EXP-004.md`

いずれも研究結果は、PER-005 / PER-006の物語内Knowledgeではない。

## 次の研究

EXP-005を研究都合で自動生成しません。

次の物語相互作用で実際に生じた問い、または明確に独立した研究価値がある問題だけを次のQ / H / EXPへ分離します。
