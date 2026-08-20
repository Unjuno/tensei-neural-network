# Hopfield以前の背景調査

状態: `IN_PROGRESS`

更新: 2026-08-20

このファイルは、第1話の導入と1980年代側のBootstrapを作るために、Hopfield 1982以前から1985年頃までの**理論・アイデア・心理学・神経科学・哲学的背景**を調べる作業台帳です。

目的は「ニューラルネットワーク史を最初から全部説明する」ことではありません。

**記憶・想起・自己同一性・連想・学習・安定状態・分散表現・feedback・動的系といった問いが、どのように別の語彙と分野を通って1980年代まで来たか**を確認し、そのうち物語開始に必要なものだけを背景へ圧縮します。

---

## 調査上の分離

背景は少なくとも次の3層に分ける。

1. **直接的な技術・研究系譜** — 1984〜85年の研究者が実際の研究として参照しうるもの
2. **隣接する記憶・認知の背景** — 研究上の問題意識を形成しうる心理学・神経科学
3. **哲学的な長期背景** — 作品の問いと共鳴するが、Hopfieldへの直接系譜とはみなさないもの

この3層を混ぜて「古代からHopfieldまで一直線に発展した」と書かない。

---

# 1. 直接的な技術・研究系譜

## Hopfield 1982自身の参考文献から確認できること

Hopfield 1982の本文・参考文献を確認すると、少なくとも次が本人の論文内で明示的に参照されている。

- S.-I. Amari (1977), neural association / concept formation
- Amariの関連研究 (1978)
- W. A. Little (1974), persistent states
- Teuvo Kohonen (1980), *Content Addressable Memories*
- G. Palm (1980), associative-memory関連
- McCulloch & Pitts (1943)
- Minsky & Papert (1969)
- Rosenblatt (1962)
- Cooper, Liberman & Oja (1979)
- Longuet-Higgins (1968)
- Anderson (1977)
- Hebb (1949)
- Eccles (1953)
- spin-glass / statistical-mechanics側のKirkpatrick & Sherrington (1978)

したがって、Hopfield 1982を「連想記憶という発想の発明」と描くのは不正確。

より適切なのは、**既存のassociation / distributed memory / Hebbian learning / persistent stateの研究を、phase-space flowとIsing / spin-glassに接続し、collective computationとして非常に明瞭に再構成した仕事**とみること。

### Hopfield 1982で確認できるモデル上の特徴

- content-addressable memoryをphase-space flowとして記述する
- 対称結合の場合、単調に低下する量 `E` を定義でき、状態更新がlocal minimumへ向かう
- Ising modelとの同型性を明示する
- random symmetric couplingの場合、spin glassの多数の局所安定状態との対応を述べる
- Monte Carlo / computer simulationで `N=30` と `N=100` を扱う
- 論文中では `N=100` のsimulationは遅く、定量的には十分追わなかったと記述されている
- nominal memoriesが増えると正しい記憶状態が不安定化し、別のstable stateへ落ちる場合がある
- 約 `0.15 N` 程度を、重大なrecall errorが出る前の経験的な目安として述べる
- 入力の一部分から全体を再構成するcontent-addressable recallだけでなく、generalization / familiarity / categorization / error correction / sequenceへの拡張も議論する

本プロジェクトのEXP-001 / EXP-002で見た「安定したが元のpatternではない」という現象は、この時代の問題設定から逸脱した現代的後付けではなく、1982〜83年の研究文脈に十分置ける。

## 1960年代以前〜1970年代の主要な先行線

### McCulloch & Pitts (1943)

神経活動をthreshold-likeな論理素子networkとして形式化する重要な初期例。

ただし、Hopfield networkと同じmemory dynamicsを提案した仕事ではない。

DOI: `10.1007/BF02478259`

### Hebb (1949)

*The Organization of Behavior* ではcell assemblyと、その時間的な連鎖としてのphase sequenceを提案する。

一次資料では、反復刺激によってassociation-area cellsのassemblyが形成され、刺激後もしばらくclosed systemのように活動できるという仮説が述べられている。

Hopfield 1982も、synaptic modificationの一般的背景としてHebbを明示的に参照する。

### Willshaw, Buneman & Longuet-Higgins (1969)

“Non-Holographic Associative Memory”。associative memoryを分散的なmemory deviceとして扱う。

DOI: `10.1038/222960a0`

### Grossberg (1969〜)

continuous-time nonlinear systemsとしてlearning / neural dynamicsを研究していた流れがある。

1969 “Embedding fields”ではpsychological postulatesからcontinuous-time learning theoryを構築し、neurophysiological interpretationを与えている。

Hopfield 1982の参考文献にはGrossberg名は見当たらないため、**重要な並行系譜ではあるがHopfield 1982の直接参照として扱わない**。

### 1972年前後 — associative memoryが複数地点で具体化

#### Shun-ichi Amari (1972)

外部から与えられたpattern / pattern sequenceをstable equilibrium statesまたはstate-transition sequencesとして記憶するself-organizing threshold networkを扱い、noise下のrecall stabilityを理論的に検討した。

DOI: `10.1109/T-C.1972.223477`

#### Kaoru Nakano (1972)

“Associatron”。bit patternをdistributed mannerで保存し、entityの一部からwholeをrecallするモデルを提案。

stored entity数が増えるとrecall accuracyが下がること、180 bit未満の例をcomputer simulationしたこともabstractで確認できる。

DOI: `10.1109/TSMC.1972.4309133`

#### James A. Anderson (1972 / 1977)

interactive / distributed memoryの線を発展させる。1977のBrain-State-in-a-Box系は後にequilibrium / gradient dynamicsとして分析される。

### Little (1974)

“The Existence of Persistent States in the Brain”。

- neural networkのpersistent states
- Ising spin systemのlong-range orderとの直接的analog
- persistent stateをshort-term memory、transfer matrixのeigenvectorsをlong-term memory representationに対応させる提案

を含む。

これはHopfield以前に、neural networkのmemoryとstatistical physicsを結ぶかなり直接的な先行例。

DOI: `10.1016/0025-5564(74)90031-5`

### Amari (1977)

“Neural theory of association and concept-formation”。

association / concept formationのneural mechanismを、distributed and multiply superposed manner of retaining knowledgeとして扱い、orthogonal / covariance learningとnoise immunityを分析する。

Hopfield 1982が明示的に引用している。

DOI: `10.1007/BF00365229`

### Kohonen (1977 / 1980)

1977 *Associative Memory—A System-Theoretic Approach*、1980 *Content-Addressable Memories*。

1980本ではassociative recallだけでなく、software / logic / hardware / processorsまで含むcontent-addressable memoryの広い工学的文脈が整理されている。

Hopfield 1982が1980本を明示的に引用している。

---

# 2. 1982〜1985年の研究現場で何が動いていたか

## 1982 Hopfield

J. J. Hopfield, “Neural Networks and Physical Systems with Emergent Collective Computational Abilities”。

- Caltech Division of Chemistry and Biology
- Bell Laboratories, Murray Hill
- NSF DMR-8107494の支援記載あり

物理学・神経モデル・計算の境界をまたぐ研究として成立している。

DOI: `10.1073/pnas.79.8.2554`

## 1983 spurious memory / unlearningが既に問題化

Hopfield, Feinstein & Palmer (1983), “‘Unlearning’ has a stabilizing effect in collective memories”。

30〜1,000 neuronsのnetworkでmathematical and computer modellingを行い、**stored memory以外のspurious memoriesも生成・想起されうる**ことを明示する。

noise inputから逆符号のlearningを行う“unlearning”によってreal memoriesへのaccessを改善しspurious memoriesを減らすという結果を報告。

これは本プロジェクトにとって重要で、1984〜85年のPER-005が

> 「安定した状態だから正しい記憶とは限らない」

という問題を持つことは十分時代整合的。

DOI: `10.1038/304158a0`

## 1983 Cohen & Grossberg

“Absolute stability of global pattern formation and parallel memory storage by competitive neural networks”。

competitive neural systemsのglobal convergence / pattern formation / memory storageをLyapunov的観点から扱う。

Hopfield系と完全に同一ではないが、**neural networkの長時間挙動、equilibrium、stabilityを数学的に問うこと自体が当時の活発な研究テーマ**だったことを示す。

DOI: `10.1109/TSMC.1983.6313075`

## 1984 Hopfield graded-response model

Hopfield (1984)はbinary threshold neuronだけでなく、graded / sigmoid responseを持つdeterministic systemでもcollective propertiesとcontent-addressable memoryが維持されることを示した。

論文は、operational amplifiersとresistorsによるcollective analog circuitが機能すると述べ、よりbiologicalなneuronへの接続を強調する。

所属はCaltech Divisions of Chemistry and BiologyおよびBell Laboratories。

DOI: `10.1073/pnas.81.10.3088`

## 1984 statistical physics側からの展開

P. Peretto, “Collective properties of neural networks: a statistical physics approach”。

Little / Hopfield modelをstatistical mechanicsで解析できる点を中心に扱い、Hebbian plasticityの場合のspin-glass analogyを議論する。

DOI: `10.1007/BF00317939`

## 1985には分野がさらに拡大する

### Ackley, Hinton & Sejnowski (1985)

“A Learning Algorithm for Boltzmann Machines”。

statistical mechanicsを使ったparallel searchとlearning ruleへ進み、internal representationを学習で形成する方向が明確になる。

DOI: `10.1016/S0364-0213(85)80012-4`

### Hopfield & Tank (1985)

neural dynamicsをcombinatorial optimizationへ用いる方向へ拡張し、Traveling Salesman Problemのcomputer simulationsを提示する。

DOI: `10.1007/BF00339943`

### Amit, Gutfreund & Sompolinsky (1985)

Hopfield / Little modelをspin-glass statistical mechanicsとして詳細解析。

- stable / metastable states
- stored patternsのmixture states
- storage loadを `p = αN` とした解析
- associative memoryが維持されるcritical loadを約 `α_c ≳ 0.14` とする結果

を示す。

DOI: `10.1103/PhysRevA.32.1007`
DOI: `10.1103/PhysRevLett.55.1530`

### 物語上の意味

したがって、**1984後半を開始点にすると非常に使いやすい**。

その時点でPER-005は、

- Hopfield 1982
- 1983 unlearning / spurious memories
- Hopfield 1984 graded-response
- Little / Amari / Kohonen等の前史

を知り得る。

一方、1985に出るBoltzmann machine、Hopfield & Tank、Amit–Gutfreund–Sompolinsky等は、物語時間の進行とともに新しい研究として現れうる。

これは現在の推奨であり、具体的な開始月をCanonにはまだ固定しない。

---

# 3. 隣接する記憶・認知の背景

## Bartlett (1932) — remembering as reconstruction

Frederic Bartlett, *Remembering*。

記憶を単純な忠実コピーの再生ではなく、schemaや文化的背景に依存する**reconstruction**として扱う心理学的背景。

これはHopfieldの数学的attractor theoryへの直接系譜ではないが、本作品の

> 「戻ったように見えるものは、保存物の読出しか、再構成か」

という問いの強い背景になる。

## Lashley (1950) — engramの局在失敗とdistributed memory

“In Search of the Engram”。長期にわたるlesion研究のまとめから、単純な局所memory traceでは説明できないことを論じ、memoryがfunctional cortical areasにdistributedであるという結論へ向かう。

これもHopfield modelへの直接の数理系譜ではないが、**記憶を一点の保存場所として探す発想への歴史的反証**として重要。

## Hebb (1949) — cell assembly / phase sequence

心理学・神経科学とnetwork learningをつなぐ橋として重要。

PER-005が記憶を「ある場所に置かれた物」ではなく、相互作用するcell populationの状態・時間的連鎖として考える背景に使える。

---

# 4. 哲学的・概念的背景

以下はHopfieldへの直接技術系譜とは扱わない。

- Aristotle, *On Memory and Reminiscence* — 記憶と想起、過去との関係
- John Locke, *An Essay Concerning Human Understanding*, Book II, Chapter XXVII — 時間をまたぐidentity / diversity
- David Hume, *A Treatise of Human Nature*, Book I, Part IV, Section VI — personal identity、知覚の連鎖、memory / imagination

作品の中心問題である

- 過去との連続性
- 記憶と本人性
- 同じ主体とは何か

の長期背景には使える。

ただしPER-005がこれらの哲学者を実際に読んでいる設定にするかは人物造形上の別判断であり、Bootstrapへ自動注入しない。

---

# 5. 1984〜85年の計算環境について現在言えること

具体的な研究室を固定していないため、ハードウェア名をCanonにするのはまだ早い。

ただし、時代上の実現可能性については次が確認できる。

- Hopfield 1982自身が `N=30` / `N=100` のcomputer simulationを実施している
- 1983 unlearning論文では30〜1,000 neuronsのmathematical / computer modellingを報告している
- 1984 graded-response論文ではcomputer simulationだけでなくop-amp / resistorによるanalog implementation可能性まで議論している
- Bell Labsでは1970年代末までにVAX-11/780上のUNIX / C環境が実装され、1980年代半ばにはVAX系を含むUNIX研究環境が一般的に使われていたことがBell Labs史料から確認できる

したがってPER-005が数十〜数百unit規模のnetworkをFORTRAN / C等の通常の研究用計算環境でsimulationすること自体は時代的に十分成立する。

ただし、具体的なmachine / language / terminal / turnaround timeは、所属機関を決めてから別調査する。

---

# 6. 1984〜85年PER-005へ初期投入してよい知識候補

高確度で時代整合的:

- Hebbian synaptic modificationの考え
- distributed / associative memoryという研究領域
- content-addressable memory
- partial cueからwhole patternをrecallするモデル
- stable equilibrium / persistent state
- noiseに対するrecall stability
- Ising / spin-glass analogy
- local minima / metastability
- spurious memories
- network loadが増えるとrecallが悪化する問題
- binary threshold modelとgraded-response modelの違い
- computer simulationでnetwork dynamicsを調べる方法

自動投入しないもの:

- 1986以降のstandard backprop boomを知っている状態
- modern “attractor network”用語体系を完全に持っている状態
- LSTM / Transformer / deep learning / large-scale pretraining
- 現代的なLLM persona reconstruction研究
- 自分の研究が将来のAI identity問題へつながるという知識
- 輪廻・同一認識主体が真だという知識

---

# 7. 物語への圧縮

調査結果をそのまま第1話へ列挙しない。

使う流れは、

```text
哲学・心理・神経・技術史
        ↓
「記憶は保存物なのか、再構成される状態なのか」という問いを抽出
        ↓
1984年前後の研究状況へ着地
        ↓
PER-005が当時の語彙だけで問題を定義
        ↓
最初の実験を選ぶ
        ↓
実験結果で本人の理解が変わる
```

とする。

導入で重要なのは、「古代から全員が同じ問題を研究していた」と一本線にすることではない。

**異なる分野が別の問いとして積み上がり、1980年代になって一部が同じ数理的対象上で交差して見える**、という描き方を優先する。

---

# 8. 次に調べるもの

1. 1984後半を仮の開始時点とした場合の、具体的な研究機関候補と計算環境
2. PER-005を物理出身 / 数理出身 / 神経科学寄りのどれにするか比較
3. 1984時点で本人が入手しやすい論文・書籍・学会経路
4. Hopfield 1984 graded-response論文の本文を精読し、当時の実験・回路語彙を抽出
5. 1983 unlearning論文をEXP-002のfalse-attractor問題と比較
6. 最初のstory experimentとして何を選ぶと、当時の研究者として自然かを決める
7. 所属が決まった後、machine / language / terminal / research workflowを一次・機関史料で具体化する

---

## 現時点の主要ソース

- J. J. Hopfield (1982), PNAS 79, 2554–2558. DOI `10.1073/pnas.79.8.2554`
- J. J. Hopfield, D. I. Feinstein, R. G. Palmer (1983), Nature 304, 158–159. DOI `10.1038/304158a0`
- J. J. Hopfield (1984), PNAS 81, 3088–3092. DOI `10.1073/pnas.81.10.3088`
- W. A. Little (1974), Mathematical Biosciences 19, 101–120. DOI `10.1016/0025-5564(74)90031-5`
- S.-I. Amari (1972), IEEE Transactions on Computers. DOI `10.1109/T-C.1972.223477`
- S.-I. Amari (1977), Biological Cybernetics 26, 175–185. DOI `10.1007/BF00365229`
- K. Nakano (1972), IEEE Transactions on Systems, Man, and Cybernetics 2, 380–388. DOI `10.1109/TSMC.1972.4309133`
- D. J. Willshaw, O. P. Buneman, H. C. Longuet-Higgins (1969), Nature 222, 960–962. DOI `10.1038/222960a0`
- M. A. Cohen, S. Grossberg (1983), IEEE Transactions on Systems, Man, and Cybernetics 13, 815–826. DOI `10.1109/TSMC.1983.6313075`
- P. Peretto (1984), Biological Cybernetics 50, 51–62. DOI `10.1007/BF00317939`
- D. H. Ackley, G. E. Hinton, T. J. Sejnowski (1985), Cognitive Science 9, 147–169. DOI `10.1016/S0364-0213(85)80012-4`
- J. J. Hopfield, D. W. Tank (1985), Biological Cybernetics 52, 141–152. DOI `10.1007/BF00339943`
- D. J. Amit, H. Gutfreund, H. Sompolinsky (1985), Physical Review A 32, 1007–1018. DOI `10.1103/PhysRevA.32.1007`
- D. J. Amit, H. Gutfreund, H. Sompolinsky (1985), Physical Review Letters 55, 1530–1533. DOI `10.1103/PhysRevLett.55.1530`
- D. O. Hebb (1949), *The Organization of Behavior*
- F. C. Bartlett (1932), *Remembering*
- K. S. Lashley (1950), “In Search of the Engram”
- T. Kohonen (1980), *Content-Addressable Memories*
