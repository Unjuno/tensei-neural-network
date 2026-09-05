# 参考文献

小説・研究・実験で参照する外部資料を記録します。

可能な限り一次資料を優先し、技術史上の事実や実験条件を追跡できるようにします。

## 記録形式

```markdown
## REF-001

- 著者:
- 題名:
- 年:
- 種別: 論文 / 書籍 / 公式資料 / その他
- DOI / URL:
- 確認日:
- 関連: Q-..., H-..., EXP-..., EVT-..., 章
- メモ:
```

## REF-001 Hopfield (1982)

- 著者: J. J. Hopfield
- 題名: Neural networks and physical systems with emergent collective computational abilities
- 年: 1982
- 種別: 論文
- 掲載誌: Proceedings of the National Academy of Sciences of the United States of America, 79(8), 2554–2558
- DOI: 10.1073/pnas.79.8.2554
- 一次資料: CaltechAUTHORS（著者所属機関リポジトリ）およびPNAS/PMC公開版
- 確認日: 2026-08-17
- 関連: Q-001, H-001, EXP-001, EVT-001〜008, 第1〜2話
- メモ: 二値状態を持つ相互結合networkの集団dynamicsとしてcontent-addressable memoryを説明し、部分的・不完全な入力から記憶全体を回復する性質、非同期更新、誤り訂正等を論じる。本projectの追試では原論文とstory-side toy modelの差異を明示する。

## REF-002 Hopfield / Feinstein / Palmer (1983)

- 著者: J. J. Hopfield, D. I. Feinstein, R. G. Palmer
- 題名: ‘Unlearning’ has a stabilizing effect in collective memories
- 年: 1983
- 種別: 論文
- 掲載誌: Nature 304(5922), 158–159
- DOI: 10.1038/304158a0
- 公刊日: 1983-07-14
- 一次資料: Nature公式書誌/abstract、著者所属Caltechで公開されている本文PDF
- 確認日: 2026-09-06
- 関連: EVT-010, EVT-011, 第3話
- メモ: 30〜1,000 neuronesのmathematical / computer modelling、stored memories以外のspurious memories、noise inputからの逆符号learningによるunlearningを扱う。本文はbinary `μ_i=±1`、`T_ij=Σ_s μ_i^s μ_j^s`, `T_ii=0`を記載し、16-neurone / 3-memoryの具体的spurious-memory candidateを掲載する。EVT-011ではこの掲載例をそのまま再計算し、stored / stored-negation外のstable stateであることを確認した。1985年以降のmixture-state理論をこの文献の記載として逆輸入しない。

## 現在

- REF-001: Hopfield 1982 — associative-memory dynamicsの基礎
- REF-002: Hopfield / Feinstein / Palmer 1983 — spurious memory / unlearningと16-neurone掲載例

story-side人物が参照できるかは各EVTのstory time / knowledge boundaryで別途判定する。
