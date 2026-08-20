# Hopfield以前の背景調査

状態: `IN_PROGRESS`

このファイルは、第1話の導入と1980年代側のBootstrapを作るために、Hopfield 1982以前の**理論・アイデア・哲学的背景**を調べる作業台帳です。

目的は「ニューラルネットワーク史を最初から全部説明する」ことではありません。

**記憶・想起・自己同一性・連想・学習・安定状態・自己組織化・feedback・動的系といった問いが、どのように別の語彙と分野を通って1980年代まで来たか**を確認し、そのうち物語開始に必要なものだけを背景へ圧縮します。

## 調査上の分離

### A. 哲学的・概念的背景

Hopfieldへの直接の技術系譜とは限らないが、作品の中心問題を長い時間軸へ置くために調べる。

- Aristotle, *On Memory and Reminiscence* — 記憶と想起、過去との関係
- John Locke, *An Essay Concerning Human Understanding*, Book II, Chapter XXVII — 時間をまたぐidentity / diversity
- David Hume, *A Treatise of Human Nature*, Book I, Part IV, Section VI — personal identity、知覚の連鎖、memory / imagination

ここでは「現代のニューラルネット理論を予言していた」と読まない。後世の概念を遡及的に投影せず、当時の問いと語彙を確認する。

## B. 神経・情報処理の形式化

- McCulloch & Pitts (1943), “A Logical Calculus of the Ideas Immanent in Nervous Activity” — 神経活動を論理的networkとして扱う形式化
- Donald O. Hebb (1949), *The Organization of Behavior* — cell assembly / 学習・結合変化。一次資料を改めて確認する
- Norbert Wiener (1948), *Cybernetics or Control and Communication in the Animal and the Machine* — information、feedback、生物と機械、時間
- W. Ross Ashby (1952), *Design for a Brain* — dynamic systems、stability、adaptation、ultrastability

## C. 学習・記憶をnetworkへ置く流れ

- Frank Rosenblatt (1958), “The Perceptron: A Probabilistic Model for Information Storage and Organization in the Brain”
- James A. Anderson (1972), “A Simple Neural Network Generating an Interactive Memory”
- Shun-ichi Amari (1972), “Learning Patterns and Pattern Sequences by Self-Organizing Nets of Threshold Elements”
- Teuvo Kohonen (1972), correlation-matrix memory関連。一次資料を確認する

特に、

- 何を「memory」と呼ぶか
- 保存と再生をどう区別するか
- 部分的・関連した入力から何が戻るのか
- noiseと誤再生をどう扱うか
- stable stateをどう解釈するか

を比較する。

## D. 統計物理・動的系への接続

- W. A. Little (1974), “The Existence of Persistent States in the Brain” — persistent statesとIsing systemのlong-range orderとの類比
- J. J. Hopfield (1982), “Neural Networks and Physical Systems with Emergent Collective Computational Abilities” — content-addressable memoryをphase-space flowとして記述

ここでは、Hopfieldを「連想記憶を最初に考えた人物」と単純化しない。

調査対象は、既にあった記憶・network・安定状態の問題が、Hopfieldでどのように整理・再表現されたのかである。

## 現時点で確認した一次・準一次ソース

- Aristotle, *On Memory and Reminiscence*: MIT Classics Archive
  - https://classics.mit.edu/Aristotle/memory.html
- Locke, *An Essay Concerning Human Understanding*, Ch. XXVII
  - https://historyofeconomicthought.mcmaster.ca/locke/Essay.htm
- Hume, *A Treatise of Human Nature*, 1.4.6
  - https://davidhume.org/texts/t/1/4/6
- McCulloch & Pitts (1943)
  - DOI: `10.1007/BF02478259`
- Wiener (1948), *Cybernetics*
  - MIT Press open-access edition: https://direct.mit.edu/books/oa-monograph/4581/Cybernetics-or-Control-and-Communication-in-the
- Ashby (1952), *Design for a Brain*
  - Springer: https://link.springer.com/book/10.1007/978-94-015-1320-3
- Rosenblatt (1958)
  - DOI: `10.1037/h0042519`
- Anderson (1972)
  - DOI: `10.1016/0025-5564(72)90075-2`
- Amari (1972)
  - DOI: `10.1109/T-C.1972.223477`
- Little (1974)
  - DOI: `10.1016/0025-5564(74)90031-5`
- Hopfield (1982)
  - DOI: `10.1073/pnas.79.8.2554`

## 調査マトリクス

各資料について、最低限次を記録する。

| 項目 | 内容 |
|---|---|
| 時代 | その文献が置かれた歴史的状況 |
| 分野 | 哲学 / 心理 / 神経科学 / 数理 / 工学 / 物理など |
| 中心の問い | 著者が実際に解こうとしていた問題 |
| memoryの意味 | 記憶を何として扱うか |
| identityの意味 | 同一性を扱う場合、その意味 |
| state / dynamics | 状態・時間変化・安定性をどう考えるか |
| association | 部分・類似・連想から何が導かれるか |
| 1980年代から見た位置 | PER-005が知り得る／参照し得るか |
| 後知恵リスク | 現代概念を遡及的に投影していないか |
| 物語への圧縮 | 導入に残すなら一文で何を残すか |

## 物語への変換

調査結果はそのまま第1話へ列挙しない。

まず、

```text
歴史・哲学・技術調査
        ↓
「同じ問いがどう変形してきたか」を抽出
        ↓
導入用の背景文脈
        ↓
1980年代Bootstrap
        ↓
PER-005および当時必要なペルソナの初期化
        ↓
1980年代の実験・相互作用
```

の順で使う。

導入は「昔から全部同じことを考えていた」という一本線にはしない。異なる時代・分野で異なる問いがあり、後から見ると一部が共鳴して見える、という程度から始める。

## 次に確認するもの

1. Hebb 1949の一次資料と、cell assembly / phase sequenceを当時の記述で確認する
2. Kohonen 1972の原論文を確認する
3. Hopfield 1982の参考文献・本文から、本人がどの先行研究をどう位置付けているか確認する
4. 1980〜1982年当時の研究者が実際に触れ得た語彙・問題設定を確認する
5. 哲学的背景は直接系譜と混同せず、導入に必要な部分だけ抽出する
6. その結果から1980年代側BootstrapのBackground frameを作る
