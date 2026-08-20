# 1980年代研究環境調査

状態: `IN_PROGRESS`

更新: 2026-08-20

このファイルは、PER-005を1984〜85年の研究者として実際に動かすために、当時の**研究文化・学際性・計算環境・実験可能性**を確認する。

理論系譜は `pre-hopfield-background.md` を参照する。

---

## 1. Hopfield本人の1980年前後の計算環境

John Hopfield自身の2018年の回想 “Now What?” によれば、1980年2月のCaltechでは量子化学用のcomputing facilityを使ってneural modelを試していた。

本人の記述から確認できる特徴:

- multi-user real-time computing
- CRT display
- direct keyboard input
- compilation delayをほぼ感じずに試行できる環境

したがって、1984年頃の研究者を一律に

- punch cardを提出する
- 翌日まで結果を待つ
- 紙の出力だけを見る

という像で描くのは不正確。

施設によって差は大きいが、少なくとも一部の先端研究施設では**対話的にcodeを変更し、その場でsimulationを繰り返す研究スタイル**が成立していた。

Hopfieldはこの環境で、前年まで考えていたcellular-automata的な案がうまくないと判断し、spin-systemとの数学的対応へ問題を切り替えたと回想している。

Source:
- John J. Hopfield, “Now What?”, Princeton Neuroscience Institute, 2018.

---

## 2. 1980〜85年のHopfieldの所属・学際性

PrincetonのCVによればHopfieldは、

- 1973–1989: Bell Laboratories, Member of Technical Staff
- 1980–1996: California Institute of Technology, Professor of Chemistry and Biology

であり、1982 / 1984のneural-network論文にもCaltechとBell Labsの affiliation が記載されている。

元来はtheoretical / condensed-matter physics出身で、biology / chemistry側へ越境した。

この履歴は、1984年代のfictional researcherを

> 「最初からAI専攻だった人」

にしなくてもよいことを強く支持する。

むしろ、

- physics
- applied mathematics
- electrical engineering
- control / systems
- neurobiology / biophysics

のどこかを母分野とし、memory / brain computationへ越境している人物の方が時代に自然。

Sources:
- Princeton Neuroscience Institute, John J. Hopfield CV.
- Princeton, “Princeton’s John Hopfield receives Nobel Prize in physics”.

---

## 3. Caltechで実際に存在した学際的な空気

Caltechの機関史料では、1981〜1983年に

- John Hopfield
- Carver Mead
- Richard Feynman

がgraduate-level course **The Physics of Computation** を断続的に共同担当したとされる。

当時はcomputer scienceと他分野のinteraction自体がまだ弱く、このcourseの承認にも障害があったというHopfieldの回想が紹介されている。

1986年にはCaltechのComputation and Neural Systems programが成立するが、1984時点ではまだ制度化の途中。

### 物語上の意味

1984年のPER-005を置く世界は、

- 完成した「ニューラルネット研究コミュニティ」の中

というより、

- physics / engineering / neurobiology / computer scienceの境界で、少人数が共通語彙を作っている途中

として描く方が自然。

会話で分野間の言葉が噛み合わない、研究費・所属・査読先の選択が曖昧、という摩擦も自然に置ける。

Source:
- Caltech Magazine, “The Roots of Neural Networks: How Caltech Research Paved the Way to Modern AI”, 2025 retrospective.

---

## 4. 1982〜84のsimulation規模から見た必要計算量

Hopfield 1982:

- `N = 30` / `N = 100` のsimulation
- `N = 100` はmuch slowerで、定量的追跡を十分には行わなかったと本文に記載

Hopfield, Feinstein & Palmer 1983:

- 30〜1,000 neuronsのmathematical / computer modelling

Nakano 1972:

- 180 bits未満のAssociatronをcomputer simulation

これらから、1984年のPER-005に必要な初期実験は、現代的な巨大計算ではなく、**数十〜数百unit程度を何度も回し、初期状態・load・noise・update ruleを変えて挙動を見る**程度で十分に時代整合的。

大きな計算機そのものをドラマの中心にしなくてもよい。

---

## 5. software / machineの具体化について

現時点ではfictional institutionを固定していないため、以下をCanonにはしない。

- VAXの具体型番
- UNIXの具体version
- FORTRAN / C / Lispのどれを使うか
- terminal機種
- printer / plotter
- shared machineの利用規則

ただしBell Labs史料では1970年代末にVAX-11/780上のUNIX / C環境が成立しており、1980年代半ばの研究組織でVAX / UNIX系の対話的計算環境を置くこと自体は不自然ではない。

fictional institutionが決まった後、その機関に近い実在環境を一次・機関史料で再調査する。

---

## 6. PER-005の出自候補

### A. 物理出身

特徴:
- Ising model / spin glass / phase transitionを自然な言語として持つ
- networkを脳の精密simulationよりcollective systemとして見る
- Hopfield / Amit系の展開と強く接続

長所:
- 作品のattractor / stable state / false minimumの問題へ最短で入れる
- 1984〜85のphysics流入と整合

弱点:
- 心理学的なmemoryや個人identityまで自然に関心が広がる理由が別途必要

### B. 数理工学・systems出身

特徴:
- stability / dynamics / control / self-organizationを中心に見る
- Amari / Kohonen / Grossberg系と相性がよい
- memoryをsystem propertyとして扱いやすい

長所:
- 日本・欧州・米国のどこにも配置しやすい
- 「正しく収束する条件」と「誤ったstable state」を研究問題として自然に持てる

弱点:
- spin-glassとの接続は学習・共同研究経由にした方が自然な場合がある

### C. neurobiology / biophysics出身

特徴:
- cell assembly、persistent activity、biological plausibilityを重視
- binary neuronからgraded-responseへの違和感を強く持てる

長所:
- 「これは本当にbrain modelなのか」という批判を人物内部に持てる
- memory問題そのものへ自然に接続

弱点:
- 数理・simulation能力をどこで獲得したかの経歴設計が必要

### 現在の推奨

**物理または数理工学を主背景とし、neurobiologyを後から学んでいる越境研究者**。

これはHopfield本人のコピーではなく、当時実際に存在した学際的移動を合成したfictional personaにする。

---

## 7. 物語開始時期の候補

### 推奨: 1984年後半

この時点ならPER-005が知り得る:

- Hopfield 1982
- Hopfield / Feinstein / Palmer 1983のspurious memory / unlearning
- Hopfield 1984 graded-response model
- Amari / Little / Kohonen / Anderson等の前史

まだ未来側に置ける:

- 1985 Boltzmann-machine learning
- 1985 Hopfield & Tank optimization
- 1985 Amit–Gutfreund–Sompolinskyのspin-glass解析 / capacity
- 1986以降のbackpropagation boom

したがって、**既に十分な材料があるが、分野の次の展開は本人にも見えていない**という開始条件を作れる。

具体月はまだCanonへ固定しない。

---

## 8. 次に必要な調査

1. fictional institutionを米国 / 日本 / 欧州のどの文化圏に置くか比較
2. 各候補に対応する1984年のmachine / OS / language / journal accessを確認
3. PER-005の年齢・職位による研究裁量を比較
4. 同僚・学生・技術職員のうち、最初に独立persona化すべき主体を決める
5. 最初の実験を「論文追試」「境界探索」「独自変更」のどこから始めるか、当時の研究者として自然か比較
