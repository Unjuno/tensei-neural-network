# 世界状態

このファイルは、世界（環境）の**時間に依存する客観状態**を管理します。

世界・環境の構造、物理的・技術的・制度的制約、観測可能性の原則は `../environment.md` に置きます。このファイルには、その世界がある時点で実際にどうなっているかを置きます。

## T0-1980S / BOOT-002

状態: `PROVISIONAL`

- Bootstrap: `BOOT-002`
- Synchronization key: `BOOT-002 @ T0-1980S @ none`
- Parent event head: `none`
- Story time: `T0-1980S`
- 時代: 1984〜1985年前後を中心候補。具体年月日は未確定

### 歴史的・研究的背景

- 記憶、想起、連想、自己同一性等をめぐる問いには1980年代以前から長い哲学的・概念的背景がある
- それらをHopfieldへ直結する単一の技術系譜とは扱わない
- 20世紀には神経networkの形式化、学習、feedback、自己組織化、連想記憶、安定状態等を扱う複数の研究系譜が存在する
- Hopfield 1982を含むcontent-addressable memory / collective dynamicsの研究は、この時点ですでに存在する

現実の歴史的根拠は `../../research/pre-hopfield-background.md` と `../../references/` へ戻って確認する。

### 場所・組織

- PER-005が理論検討、文献読解、簡略化したnetwork計算・実験を行える研究環境が存在する
- 国、都市、大学・研究所名、部局、研究室規模、職位は未確定
- 共同研究者、学生、技術スタッフ等は存在し得るが、BOOT時点では独立ペルソナとして固定しない

### 利用可能な研究手段

- 当時入手可能な論文・書籍・研究ノート
- 数学的・理論的検討
- 簡略化したnetworkモデルを扱うための計算手段

具体的な計算機、言語、メモリ量、実行時間、予算等は未確定であり、必要になった時点で歴史調査により制約する。

### 現在成立している客観境界

- PER-005は `T0-1980S` でactive
- 最初の実験はまだ開始していない
- 最初の1980年代eventはまだ成立していない
- 「安定状態へ収束すること」と「正しい原像へ戻ること」の区別は研究上の問題として扱える
- 輪廻、同一認識主体、現代LLM、将来のcheckpoint人格問題は、この時代の観測済み世界事実ではない
- 第1話の結末や将来の発見は初期世界状態へ入れない

### 同期しているペルソナ状態

BOOT-002から同じ同期キーで次を初期化する。

- `personas/PER-005.md` — active

新しい独立主体が実際の相互作用に必要になった時点で追加する。

---

## T0-1980S + first research session / EVT-001

状態: `PROVISIONAL`

- Previous state: `BOOT-002 @ T0-1980S @ none`
- Event head: `EVT-001`
- Source event: `../events/EVT-001-stopping-is-not-returning.md`

### 客観的に成立した出来事

PER-005が当時利用可能な連想記憶・spurious memoryをめぐる問題設定を比較し、自分の研究ノートへ次の問いを記した。

- 「止まることと、戻ることは同じか」
- 「保存していないところで止まるなら、その状態は何からできている？」

### 変更後

- PER-005の研究ノートに、保存pattern以外の安定状態の構造を問う最初の局所問題が存在する
- まだ具体的な実験条件、実験結果、共同研究者との議論は成立していない

### 重要な境界

現実側でEVT-001をtriggerにEXP-003が行われても、その結果は1980年代世界の客観事実ではない。

---

## T0-1980S + second research interaction / EVT-002

状態: `PROVISIONAL`

- Previous event head: `EVT-001`
- Event head: `EVT-002`
- Source event: `../events/EVT-002-who-defines-correct-recall.md`

### 変更前

- PER-005は`stable`と`correct recall`を区別し始めている
- `correct`のtargetを誰がどのように定義しているかは、まだ明示的な問題になっていない
- PER-006は背景上に存在し得る他者だったが、独立ペルソナとしては未成立

### 客観的に成立した出来事

PER-005が自分の問題を、実験神経科学・観測基準に敏感なPER-006へ共有した。

PER-006は、実験者がtargetを知っていることと、曖昧なcueに対してnetwork自身に一意な「正解」が存在することは別ではないか、と問い返した。

PER-005は研究ノートへ、

- 「原像を知っているのは誰だ」
- 「手掛かりが二つの記憶の間にあるなら、戻る先は最初から一つなのか」

という問いを追記した。

### 変更後

- PER-006が独立したペルソナとして成立し、PER-005との研究上の批判関係が始まった
- PER-005の局所問題に、targetの一意性と曖昧cueの問題が加わった
- PER-005とPER-006は、次に何を観測すれば`correct recall`と言えるかについて継続して議論できる状態になった
- 物語世界内では、balanced cue実験やその数値結果はまだ発生していない

### 同期しているペルソナ状態

EVT-002時点で1980年代側active:

- `personas/PER-005.md`
- `personas/PER-006.md`

### 重要な境界

現実研究側でEVT-002をtriggerにEXP-004が行われ、等距離cueのupdate-order依存が観測されても、その結果は1980年代世界へ自動反映しない。

PER-005 / PER-006がその結果を知ったことにはしない。

---

## T0-1980S + protocol sketch after EVT-002 / EVT-003

状態: `PROVISIONAL`

- Previous event head: `EVT-002`
- Event head: `EVT-003`
- Source event: `../events/EVT-003-a-fair-cue-is-not-neutral.md`

### 変更前

- 二人は曖昧cueの必要性には合意している
- しかし「二つのmemoryへ同程度に適合するcue」をどう作るかはまだ抽象的だった
- `correct`の基準を実験者が後から都合よく選ばないための観測項目も未整理だった

### 客観的に成立した出来事

PER-005 / PER-006は、二つのstored patterns A/Bで異なるunitの半分をA、残り半分をBから取ることで、A/Bへ同じbit差数を持つcueを作るprotocol sketchを共同メモへ記録した。

同時に、PER-006の指摘を受けて、

- bit差数が等しいこと
- dynamics上でA/Bが等価であること

を同一視しないと明記した。

次の計算で記録すべき項目として、

1. cueからA/Bへのbit差数
2. final state
3. update条件
4. A/B以外へ停止したstate

を分けて残す方針が成立した。

### 変更後

- 抽象的な曖昧cue問題が、実行前protocol sketchへ進んだ
- PER-005 / PER-006の関係が、批判関係から共同protocol設計を含む関係へ進んだ
- A/B以外のstateを失敗として捨てず、観測対象へ残す方針が成立した
- 具体的なN、pattern数、run数、計算機、language、simulation結果はまだ未成立

### 同期しているペルソナ状態

EVT-003時点で1980年代側active:

- `personas/PER-005.md`
- `personas/PER-006.md`

### 重要な境界

EVT-003から新しい現実研究EXPは自動生成していない。

現代側EXP-004が類似したbalanced cueを扱ったという作者側情報を、このprotocol sketchの原因にはしない。

---

## T0-1980S + first paper calculation after EVT-003 / EVT-004

状態: `PROVISIONAL`

- Previous event head: `EVT-003`
- Event head: `EVT-004`
- Source event: `../events/EVT-004-same-cue-two-returns.md`

### 変更前

- A/Bへ同じbit差数を持つcueの構成手順と、観測項目の分離は成立済み
- まだ物語世界内の具体的なnetwork計算は成立していない
- 計算機、programming language、大規模simulation条件は未確定

### 客観的に成立した出来事

PER-005 / PER-006は、6 unit・3 stored patternsの小規模networkを紙上で構成した。

A/Bへ2 bitずつ離れた同一cueを用い、同一weights・同一の非同期更新規則で、更新順だけを変えた二つの計算を追った。

その結果、一方のupdate orderではAへ、別のupdate orderではBへ到達し、どちらもstable stateであることを確認した。

### 変更後

- 物語世界内で最初の具体的network計算が成立した
- 同一cue・同一weightsでもupdate orderだけの差で異なるstored patternへ到達する6-unitの具体例が共同メモに残った
- 「等距離」と「dynamics上の中立」の区別が、注意書きから観測済みの問題へ変わった
- final stateだけから一意の`correct recall`を置く方針は、この例に対して維持できなくなった
- ただし、この一例をmemory一般、生物学的記憶、頻度一般へ拡張していない
- 計算機実装、大規模simulation、頻度推定はまだ未成立

### 同期しているペルソナ状態

EVT-004時点で1980年代側active:

- `personas/PER-005.md`
- `personas/PER-006.md`

### 重要な境界

PER-005 / PER-006が観測したのは6-unitの紙上例だけであり、現代側EXP-004の122/200、4000 runs、seed等の結果は知らない。

生成方式検証上はEVT-004の具体条件が結果前にlockされていないため、Resolution provenanceは `UNBLINDED` とする。

---

## T0-1980S + next joint paper check after EVT-004 / EVT-005

状態: `PROVISIONAL`

- Previous event head: `EVT-004`
- Event head: `EVT-005`
- Source event: `../events/EVT-005-lock-the-order-family.md`
- Resolution provenance: `LOCKED`

### 変更前

- 同じ6-unit networkで二つの手選択orderからA/Bへ分岐する例は成立済み
- しかし、order選択自体が結果に依存していないことはEVT-004では保証されていない
- PER-005 / PER-006は、A/B以外のstateも結果に残す方針を持っている

### 客観的に成立した出来事

PER-005 / PER-006は、EVT-004と同じA / B / C / cue / weights / update ruleを使い、unit番号の自然順序 `(1,2,3,4,5,6)` の全6 cyclic rotationsを結果前に検査集合として固定した。

Action-lock commit後、6本をすべて同じstopping / inclusion ruleで紙上計算した。

結果:

- r1 → A
- r2 → D
- r3 → B
- r4 → B
- r5 → D
- r6 → D

D:

```text
(+1, +1, +1, +1, -1, +1)
```

DはA / B / Cのどれとも一致しないstable stateである。

- Hamming(D, A) = 2
- Hamming(D, B) = 2
- Hamming(D, C) = 6

### 変更後

- 同一cue・同一weights・同一update ruleからstored A / stored B / nonstored stable Dの三種類が観測された
- 6 cyclic ordersは結果を見て選別せずすべて共同メモへ残った
- PER-005の局所問題は「A/Bのどちらへ戻るか」だけでは足りず、stored集合外の戻り先をどう扱うかへ広がった
- PER-006はDをmemoryと呼ばず、nonstored stable stateとして扱うよう要求した
- この小例を頻度一般・memory一般・生物学的記憶へ一般化していない
- 計算機実装、大規模simulation、頻度推定はまだ未成立

### 同期しているペルソナ状態

EVT-005時点で1980年代側active:

- `personas/PER-005.md`
- `personas/PER-006.md`

### 重要な境界

PER-005 / PER-006が知っているのは、自分たちが固定して紙上計算した6 cyclic ordersとA/B/Dの結果までである。

現代側EXP-003 / EXP-004の数値集計、seed、run分布は人物Knowledgeへ入れていない。

---

## T0-MODERN / BOOT-001

状態: `PROVISIONAL`

- Bootstrap: `BOOT-001`
- Synchronization key: `BOOT-001 @ T0-MODERN @ none`
- Parent event head: `none`
- Story time: `T0-MODERN`
- 具体的な年月日: 未確定

### 場所・組織

- 現代の大規模ニューラルネットワークを評価・調査できる組織内環境が存在する
- 組織名、国、都市、設備構成は未確定

### 利用可能な系

- 少なくとも一つの現代モデル系をrun単位で評価できる
- prompt / input / output / evaluation logを保存・比較できる
- 必要になれば複数run、checkpoint差、対照条件を比較できる余地がある
- 1980年代研究者に関係する不完全な資料群が利用可能である

具体的なモデル名、資料内容、欠損箇所、権限範囲はまだ未確定。

### 現在成立している客観境界

- EVT-001〜EVT-005は1980年代側で成立しているが、現代側の最初のeventはまだ成立していない
- 最初の現代側異常の具体像、最初の発見者、その時点の解釈は未確定
- 現代モデル内に過去の研究者と機能的・行動的に似たパターンが作品内で現れることはCanonに含まれるが、それを`T0-MODERN`ですでに観測済みの世界状態とはしない
- それが本人の意識・輪廻・同一主体であることは確定していない
- 長期プロット候補は未来の世界状態として扱わない

### 同期しているペルソナ状態

BOOT-001から同じ同期キーで次を初期化する。

- `personas/PER-001.md` — active
- `personas/PER-002.md` — standby
- `personas/PER-003.md` — active
- `personas/PER-004.md` — not-yet-instantiated

PER-005 / PER-006は1980年代側のstory timeに属するため、BOOT-001では状態を初期化しない。

## 更新方法

重要な世界状態変化は、原則として `../events/EVT-xxx...` と対応させます。

```text
## <story time / event id>

- 変更前:
- 客観的に成立した出来事:
- 変更後:
- 影響した場所・物・制度・システム:
- 根拠となるイベント:
```

人物の信念や自己申告はここへ直接書きません。世界側で客観的に成立したことだけを扱います。

Bootstrapによる初期化・再初期化は制作上の同期操作であり、それ自体を物語eventとは扱いません。Bootstrapから生成した状態には、対象`BOOT-xxx`、story time、parent event headを必ず残します。