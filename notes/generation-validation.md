# 物語生成方式の検証

このファイルは、ペルソナ駆動・world resolver・event sourcing・episode projectionによる物語生成方式そのものの検証結果を記録する。

小説本文やCanonの正本ではない。生成方式について何が確認でき、何がまだ確認できていないかを分離するための検証台帳。

## Test-001 別セッションから第1話ドラフトまで再開

実施日: 2026-08-21

対象branch: `work/story-bootstrap`

対象範囲:

- repoから1980年代側の状態を復元
- stale indexがあれば直接event/stateからcurrent headを復元
- PER-005 / PER-006とworldを進める
- 成立済みeventを第1話へNarrativeProjectionする

### 確認できたこと

| 項目 | 判定 | 備考 |
| --- | --- | --- |
| repoだけから状態復元 | PASS | stale indexから巻き戻さずEVT-003を開始headとして復元できた |
| persona情報境界 | PASS | PER-005 / 006へ現代側EXP-004の統計値を直接与えていない |
| world / persona state同期 | PASS | EVT-004までstate / timeline / structureを同期できた |
| personaを必要時だけ追加 | PASS | PER-007を機械的に追加しなかった |
| 小説と研究の分離 | PASS | EVT-003 / 004から重複EXPを自動生成しなかった |
| 一話=一実験の回避 | PASS | 第1話はEVT-001〜004を材料に成立 |
| NarrativeProjection | PASS | event/stateから研究レポート形式ではない第1話ドラフトを作成できた |
| EVT-004の数理的一貫性 | PASS | 記載されたHebbian結合・cue・update orderを再計算し、order α→A、order β→Bを再確認 |
| environment resolverの結果独立性 | INCONCLUSIVE | 下記selection biasを排除できない |

### Test-001で見つかった重要な弱点

EVT-004より前に、作者側・生成側はすでにEXP-004で「等距離cueがupdate orderだけでA/Bへ分岐し得る」ことを知っていた。

しかしEVT-004では、次の自由度が結果を見る前にrepo上で固定された記録がない。

- A / B / Cの具体pattern
- balanced cueの具体値
- order α / βの具体順序
- どの候補例を採用するかというselection rule
- 何回試し、どの結果をevent化するかというstopping / inclusion rule

したがって、EVT-004の計算結果自体は正しいが、**この反例がunbiasedなenvironment resolutionから自然に出たことの証拠にはならない**。

これは人物への未来知識漏洩とは別問題である。

### EVT-004の検証上の扱い

- 物語event候補として: 有効
- 数理的な具体例として: 有効
- 第1話ドラフトの材料として: 有効
- 「完成プロットなしでresolverも結果非依存に動いた」ことの証拠として: **INCONCLUSIVE**
- Resolution provenance: `UNBLINDED`

EVT-004を削除したり、結果を無効化したりはしない。

---

## 解決前ロックの規則

物語上の結果に複数の自由度があり、生成者が作者側の研究結果・未来候補を既に知っている場合、重要eventは二段階で処理する。

### Phase 1: ACTION_LOCKED

結果を計算・検索・観測する前に、同じ `EVT-xxx` ファイルを `ACTION_LOCKED` としてcommitする。

最低限固定する:

- parent event head / story time
- 各personaが実際に観測している入力
- personaが選んだ行動
- 結果へ影響する具体条件またはその選択規則
- trial集合 / update rule / stopping rule / inclusion rule
- resolverが利用してよい情報源
- personaには見えない作者側研究結果など、action selectionへ使ってはいけない情報
- 結果解決方法

この段階ではoutcomeを書かない。

### Phase 2: RESOLVED

ACTION_LOCKEDのcommit後にenvironment resolverが結果を解決する。

- locked条件を結果を見て変更しない
- 規定したtrialは都合の悪いものも含めて全て扱う
- 望ましい結果が出なければ、その結果をそのまま採用する
- 結果を見て別条件へ差し替えた場合は、そのeventをclean validationとして数えない

## 生成側が既知の研究結果を持っている場合

同じAI/sessionが、personaには見えないEXP結果を既に読んでいること自体はあり得る。

その場合、personaの具体的な実験条件・入力値を選ぶ自由度が結果へ効くなら、次のどちらかを使う。

1. story-visibleな情報だけから導出できるdeterministic selection ruleを事前固定する
2. 結果知識を与えない別contextでaction / parameter selectionを行い、commitしてからresolverへ渡す

例:

- event IDから固定seedを導出する
- 候補を辞書順で最初から使う
- personaが明示したruleで全候補を列挙し、都合のよい例だけを選ばない

「反例が出るものを探す」は、人物がその探索目的を実際に持ち、探索範囲・停止条件を事前に固定している場合を除き、cleanなresolver検証には使わない。

## Resolution provenance

重要eventには、生成方式の検証用に次のprovenanceを記録できる。

- `LOCKED`: outcome-sensitiveな選択を解決前に固定し、その後変更していない
- `UNBLINDED`: 結果知識を持つ生成contextで条件選択が行われ、解決前lockがない。物語eventとしては使えるがclean validationには数えない
- `AUTHOR_CONDITIONED`: 人間作者または生成側が望む結果・演出へ向けて条件を意図的に固定した。介入として明記し、創発eventと偽装しない

---

## Test-002 ACTION_LOCKED → resolver → RESOLVEDを実行

実施日: 2026-08-21

対象event: `EVT-005-lock-the-order-family.md`

Action-lock commit:

`59ff6530d202b79834afbe8ffdceee1256437315`

### 検証目的

Test-001で未確認だったenvironment resolverの結果独立性について、少なくとも一つの重要eventを

```text
persona action selection
→ outcome-sensitive conditionsを外部化
→ commit
→ resolver
→ 全結果をそのまま受理
```

の順で処理できるか確認する。

成功条件はA/B分岐や面白い結果が出ることではない。

**lock後にどのoutcomeが出ても条件を差し替えず、その結果をworld/persona stateへ返せること。**

### Action lockで固定したもの

EVT-004で成立済みの6-unit networkをそのまま使い、update orderだけについて、unit番号の自然順序 `(1,2,3,4,5,6)` の全6 cyclic rotationsを検査集合として固定した。

あわせて、同じcue / weights / update rule、zero field保持、最大20 sweeps、全6本を含むこと、A/B以外も削除しないことを結果前に固定した。

### Resolution結果

```text
r1 -> A
r2 -> D
r3 -> B
r4 -> B
r5 -> D
r6 -> D
```

D:

```text
(+1,+1,+1,+1,-1,+1)
```

- A: 1 / 6
- B: 2 / 6
- OTHER_STABLE D: 3 / 6
- NONCONVERGED: 0 / 6

### Test-002判定

| 項目 | 判定 |
| --- | --- |
| actionをoutcome前に外部化 | PASS |
| outcome-sensitiveなorder集合の固定 | PASS |
| stopping / inclusion ruleの固定 | PASS |
| lock後の条件差し替え回避 | PASS |
| 不都合・非期待結果の保持 | PASS |
| world/persona stateへの反映 | PASS |
| cleanなresolver手順の実行 | PASS |

### 限界

確認できたのは、**一つの重要eventについて、結果前に条件をcommitし、結果を選別せず受け入れる制作手順が機能した**こと。

action ruleそのものは同じ生成contextで作られているため、action selectorの完全なcontext isolationはまだ未検証。

---

## Test-003 cue selection freedomまでdeterministicに縮小

実施日: 2026-08-21

対象event: `EVT-006-all-balanced-cues-locked.md`

Action-lock commit:

`97ee4b3d322d367468258775443d6f2aa3551ef1`

### 検証目的

EVT-005ではupdate order集合をlockしたが、balanced cue自体はEVT-004で一つだけ選ばれたものだった。

そこでTest-003では、story-visibleなA/Bと「両者へbit数で等距離」という既存protocolから**候補cue集合を全列挙**し、initial-state selection freedomも減らせるか検証した。

### Action lock

A/Bが異なるunitは `{1,2,4,6}`。

その4位置のうち2位置をAから、残り2位置をBから取る全組合せを採用した。

```text
C(4,2) = 6 cues
```

- q12
- q14
- q16
- q24
- q26
- q46

各cueへ、EVT-005で固定済みの6 cyclic update ordersをすべて適用。

```text
6 cues x 6 orders = 36 trials
```

36 trialを全て含め、結果を見てcue/orderを追加・削除しないことを事前固定した。

### Resolution結果

```text
        r1   r2   r3   r4   r5   r6
q12      B    B    A    A    A    A
q14      D    A    B    B    A    A
q16      B    A    C    A    C    B
q24      D    D    D    D    D    D
q26      A    B    D    D    B    B
q46      A    D    B    B    D    D
```

Aggregate:

- A: 11
- B: 11
- C: 2
- D: 12
- NONCONVERGED: 0

期待していたA/Bだけでなく、第三stored pattern Cとnonstored fixed point Dを含む結果をそのまま保持した。

### Test-003判定

| 項目 | 判定 | 備考 |
| --- | --- | --- |
| cue集合をoutcome前に固定 | PASS | 全組合せというdeterministic rule |
| update order集合を固定 | PASS | EVT-005の全6 cyclic orders |
| trial inclusionを固定 | PASS | 36/36を含めた |
| outcome後のcue/order差し替えなし | PASS | 追加探索なし |
| 第三stored/nonstored結果の保持 | PASS | C/Dを削除しなかった |
| world/persona state同期 | PASS | EVT-006、PER-005/006、worldへ反映 |
| initial-condition selection freedomの縮小 | PASS | 「面白いcue」を選ばず全候補を使用 |

### 解釈

Test-003はTest-002より強い。

update orderだけでなく、pairwise balanced cueの選択もstory-visibleなruleから全列挙したため、特定outcomeへ寄せる自由度をさらに減らせた。

ただし、

- 「次にbalanced cue集合を全部調べる」というaction自体を選ぶselector
- 6-unit toy network自体の由来

は作者側研究結果と完全に隔離した別contextで選ばれたわけではない。

したがって、action selectorの完全なbias-free性を証明したわけではない。

---

## Test-004 subset選択をやめ、有限state spaceを全列挙

実施日: 2026-08-21

対象event: `EVT-007-enumerate-the-whole-small-state-space.md`

Action-lock commit:

`3c1034c70853c5704d4064f71ef4e989b4dc296f`

### 検証目的

EVT-006ではbalanced cueの候補を全列挙したが、そもそも「A/Bへ等距離」というsubset自体を選んでいた。

EVT-006後のstory-visibleな状態では、PER-005 / PER-006自身が「pairwiseな選び方がnetwork全体の関係を隠す」と認識している。

現在のnetworkは6 unitしかないため、binary state space全体は `2^6 = 64` statesで有限かつ全列挙可能である。

そこでTest-004では、特定のcueや反例を選ぶ代わりに、**全64 initial states × 既存6 cyclic update orders = 384 trials**を結果前に固定した。

成功条件は特定のattractorや意外な結果が出ることではない。

**全有限state spaceを固定条件で解決し、どのoutcomeでも選別せず物語状態へ返すこと。**

### Action lock

結果解決前に次を固定した。

- 既存A/B/CとHebbian weights
- `{-1,+1}^6` の64 initial states全部
- 辞書順の列挙規則
- EVT-005/006と同じ6 cyclic update orders
- 64 × 6 = 384 trials全部
- zero local fieldではcurrent value保持
- 最大20 sweeps
- initial fixed stateも除外しない
- stored patternへ行かない結果も除外しない
- outcome後に別state/order/networkを追加しない

row-level結果は `novel/events/EVT-007-state-space.csv` に保存した。

### Resolution結果

全384 trialが2 sweeps以内にstableとなった。

fixed points / unique stable finalsは6種類:

```text
A, B, C, -A, -B, -C
```

重要な非予定観測:

EVT-005 / EVT-006で `D` と呼んでいた

```text
(+1,+1,+1,+1,-1,+1)
```

は、実際には

```text
-C
```

そのものだった。

全384 trialのfinal count:

```text
A   62
B   66
C   64
-A  62
-B  66
-C  64
```

64 initial statesについて:

```text
6 ordersですべて同じfinal   18
2種類以上のfinalへ分岐      46
```

distinct-final-count distribution:

```text
1 final : 18 states
2 finals: 16 states
3 finals: 22 states
4 finals:  4 states
5 finals:  4 states
6 finals:  0 states
```

46/64はこのtoy networkと6 cyclic ordersに限定し、一般的頻度へ拡張しない。

### Test-004判定

| 項目 | 判定 | 備考 |
| --- | --- | --- |
| actionをstory-visibleな問題から導出 | PASS | pairwise subsetが盲点というEVT-006後Goalから全状態列挙へ |
| initial-state selection freedom除去 | PASS | 64/64 statesを全列挙 |
| update-order集合のpre-lock | PASS | 既存6 cyclic ordersを固定 |
| stopping / inclusion ruleのpre-lock | PASS | 384/384を対象化 |
| outcome後の条件差し替えなし | PASS | 別state/order/networkを追加せず |
| 非予定の分類修正を受理 | PASS | Dを守らず `D=-C` と再分類 |
| world / persona stateへ反映 | PASS | EVT-007 / PER-005 / PER-006 / worldへ同期 |
| selector context isolation | INCONCLUSIVE | 同じ生成contextがaction rule自体を書いている |

### 解釈

Test-004は、Test-003よりさらにoutcome-sensitiveな自由度を減らした。

特に `D=-C` は、期待した「新しいspurious state」を保持する方向ではなく、以前の分類を弱める結果だった。それでも結果をそのまま受理し、人物状態の分類を修正できた。

これは「都合のよいoutcomeだけを選ぶ」ことへの耐性を示す実例になる。

ただし、これでも**action selectorそのものの完全な独立性を証明したわけではない**。生成contextは作者側研究を知っており、「全64 statesを見る」というaction ruleを選んだ主体でもある。

したがってTest-004をもって生成方式全体をFULL PASSにはしない。

---

## Test中に見つかった運用障害: stable ID重複

Test-003開始時、current branchに既存のEVT-005があることを再確認せず、一時的に別の`EVT-005`を作成した。

途中で重複を検出し、誤って追加したEVT-005を削除した。正しい既存EVT-005は保持し、その後の新eventをEVT-006として結果前lockからやり直した。

### 原因

長期work branchにmain未反映のstable IDが存在するのに、main側の最大番号または会話上の古い状態だけを採番根拠にすると衝突する。

### 修正

`AGENTS.md` と `POLICY.md` に、stable ID採番前に

- current work branch
- main

双方の同種IDを確認し、current branch上の未マージIDを必ず含める規則を追加した。

この障害は物語生成の理論ではなく、event-sourced repoを長期branchで運用する際の実装上の問題として扱う。

## 現在の総合評価

- state recovery: PASS
- persona information boundary: PASS
- world/persona同期: PASS
- persona必要時生成: PASS
- 小説/研究分離: PASS
- 一話=一実験回避: PASS
- NarrativeProjection: PASS
- 未確定恒常属性を本文で勝手に固定しない規則: 導入済み
- resolver pre-lock mechanism: PASS on Test-002
- initial-condition deterministic enumeration: PASS on Test-003
- finite state-space exhaustive locked resolution: PASS on Test-004
- outcomeが既存分類を崩しても受理できること: PASS on Test-004 (`D=-C`)
- action selector自体のcontext isolation: **未検証**

生成方式は`PARTIAL PASS`を維持する。

Test-004までで、「outcome-sensitiveな自由度を外部化・固定し、都合の悪い結果も受理する」仕組みは実際に機能した。

一方、selectorそのものが作者側知識から独立していることはまだ実証していない。この点は、単にdeterministic ruleを増やすだけでは完全には解消しない。

## 次の検証課題

次の重要なaction selectionを、

- 作者側research結果を読まない別contextで決める

または、action候補が複数ある場合に

- story-visibleな状態だけから事前に固定した一般ruleで一意に選ぶ

ことでselector-levelの独立性を検証する。

成功条件は「面白い結果」ではなく、**結果を知らずに選んだactionから生じたoutcomeを、そのまま物語へ受け入れられること**とする。
