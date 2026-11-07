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

## REF-003 Kubota (1975)

- 著者: Kisou Kubota（久保田競）
- 題名: Prefrontal unit activity during delayed-response and delayed-alternation performances
- 年: 1975
- 種別: 原著論文
- 掲載誌: The Japanese Journal of Physiology 25(4), 481–493
- DOI: 10.2170/jjphysiol.25.481
- 一次資料: J-STAGE原論文 https://www.jstage.jst.go.jp/article/jjphysiol1950/25/4/25_4_481/_pdf / PubMed PMID 813043
- 確認日: 2026-11-08
- 関連: research/1980s-neurophysiology-observation-boundary.md, EVT-019以降の佐伯の問い
- メモ: サル前頭前野の同じunitをdelayed-responseとdelayed-alternationという二課題で細胞外記録した研究。95 unitは総記録件数であり、95 unit同時記録ではない。課題・時間窓と発火活動との関係を考える史料。模型の全state readoutではない。

## REF-004 Fuster / Alexander (1971)

- 著者: J. M. Fuster, G. E. Alexander
- 題名: Neuron activity related to short-term memory
- 年: 1971
- 種別: 原著論文
- 掲載誌: Science 173(3997), 652–654
- DOI: 10.1126/science.173.3997.652
- 一次資料: PubMed PMID 4998337 https://pubmed.ncbi.nlm.nih.gov/4998337/
- 確認日: 2026-11-08
- 関連: research/1980s-neurophysiology-observation-boundary.md
- メモ: サルの遅延課題と前頭前野・視床の神経細胞放電の関係を報告。遅延期の活動と模型の離散更新順を直接同一視できない。

## REF-005 McNaughton / O'Keefe / Barnes (1983)

- 著者: B. L. McNaughton, J. O'Keefe, C. A. Barnes
- 題名: The stereotrode: a new technique for simultaneous isolation of several single units in the central nervous system from multiple unit records
- 年: 1983
- 種別: 原著論文・測定技術
- 掲載誌: Journal of Neuroscience Methods 8(4), 391–397
- DOI: 10.1016/0165-0270(83)90097-3
- 一次資料: PubMed PMID 6621101 https://pubmed.ncbi.nlm.nih.gov/6621101/
- 確認日: 2026-11-08
- 関連: research/1980s-neurophysiology-observation-boundary.md
- メモ: ラット海馬で最大5 unitを同時に識別したと記載。特定論文内の実績であり、全研究所の最大機能やモデル16素子の完全観測を意味しない。

## REF-006 Barrionuevo / Brown (1983)

- 著者: G. Barrionuevo, T. H. Brown
- 題名: Associative long-term potentiation in hippocampal slices
- 年: 1983
- 種別: 原著論文
- 掲載誌: PNAS 80(23), 7347–7351
- DOI: 10.1073/pnas.80.23.7347
- 一次資料: PMC https://pmc.ncbi.nlm.nih.gov/articles/PMC390052/ / PubMed PMID 6316360
- 確認日: 2026-11-08
- 関連: research/1980s-neurophysiology-observation-boundary.md
- メモ: 海馬CA1切片で二つの入力経路の刺激と長期的なシナプス応答変化を比較。単一の記憶想起の中間経路を測定した実験ではない。

## REF-007 McNaughton / Barnes / O'Keefe (1983)

- 著者: B. L. McNaughton, C. A. Barnes, J. O'Keefe
- 題名: The contributions of position, direction, and velocity to single unit activity in the hippocampus of freely-moving rats
- 年: 1983
- 種別: 原著論文
- 掲載誌: Experimental Brain Research 52(1), 41–49
- DOI: 10.1007/BF00237147
- 一次資料: PubMed PMID 6628596 https://pubmed.ncbi.nlm.nih.gov/6628596/
- 確認日: 2026-11-08
- 関連: research/1980s-neurophysiology-observation-boundary.md
- メモ: ラット自由行動時の海馬・歯状回unit activityを位置・方向・速度の条件と比較。課題外の運動変数を無視してmemory stateを同定することはできない。

## 現在

- REF-001: Hopfield 1982 — associative-memory dynamicsの基礎
- REF-002: Hopfield / Feinstein / Palmer 1983 — spurious memory / unlearningと16-neurone掲載例
- REF-003〜007: 1971〜1983年の神経生理学の記録手法と課題条件。直接のmodel stateとの対応は未確定

story-side人物が参照できるかは各EVTのstory time / knowledge boundaryで別途判定する。
