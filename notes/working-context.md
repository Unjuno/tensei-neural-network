# 作業コンテキスト

更新: 2026-08-21

このファイルは別セッションへ現在の探索状態を引き継ぐ公開可能な作業記憶。正本ではない。

## 主目的

小説が主役。

研究は、小説内で実際に生じた技術的な疑問・語・違和感を必要に応じて現実側で検証し、作品の現実性を上げるために使う。

小説を実験レポート風にしない。

## 現在の物語状態

1980年代側:

- Bootstrap: `BOOT-002 @ T0-1980S @ none`
- current event head: `EVT-007`
- active personas: PER-005 / PER-006
- current structure: `起 / 承 / 転`
- 第1話ドラフト: `novel/chapters/001.md`
- 第1話採用範囲: `EVT-001`〜`EVT-004`

### EVT-004まで

- EVT-001: 「止まることと、戻ることは同じか」「保存していないところで止まるなら、その状態は何からできている？」
- EVT-002: `correct recall`のtargetを誰が定義するか
- EVT-003: A/B等距離cueと観測項目のprotocol
- EVT-004: 同一cue・weightsからupdate orderだけの差でA/Bへ分岐する6-unit例

EVT-004は数理的には有効だが、具体条件をoutcome前にlockしていなかったため生成検証上は `UNBLINDED`。

### EVT-005 / EVT-006

EVT-005では同じ6-unit network / cueについて全6 cyclic update ordersを結果前に固定し、A / B / Dを観測した。

EVT-006ではA/B-balanced cue全6種類も結果前に全列挙し、36 trialsを全て受理した。

- A: 11
- B: 11
- C: 2
- D: 12
- nonconverged: 0

この段階でpairwiseな`A/Bの間`だけでは第三stored patternやnonstored stateとの関係を隠し得ると分かった。

### EVT-007

EVT-006後の局所Goalから、特定cueの選択をやめ、6-unit binary state space全体を調べた。

Action-lock commit:

`3c1034c70853c5704d4064f71ef4e989b4dc296f`

locked:

- 全64 initial states
- 既存6 cyclic update orders
- 64 × 6 = 384 trials全部
- zero field保持
- max 20 sweeps
- 全結果を含む

結果:

- 384 / 384 trialが2 sweeps以内にstable
- fixed points / unique finalsは `A / B / C / -A / -B / -C`
- EVT-005 / 006のD `(+1,+1,+1,+1,-1,+1)` は **`-C`**
- 18 / 64 initial statesはorder-invariant
- 46 / 64 initial statesは2種類以上のfinalへorder-dependentに分岐

row-level:

`novel/events/EVT-007-state-space.csv`

重要な更新:

`nonstored stable`は観測カテゴリとしては正しいが、符号反転対称性・mixture・その他を同じ箱へ入れる粗い分類になり得る。

PER-005:

> 保存していない、だけでは足りない。
>
> Cを裏返したものまで、別の記憶と呼んでいた。

46/64を一般的なHopfield networkの頻度へ一般化しない。

## 第1話

`novel/chapters/001.md`

採用範囲はEVT-001〜004のまま。EVT-005〜007を後から自動追加しない。

本文では未確定の氏名・年齢・性別・国籍・所属・具体機材等を勝手に固定しない。

## 生成方式検証

詳細: `notes/generation-validation.md`

- Test-001: state recovery / persona境界 / state同期 / NarrativeProjection PASS。EVT-004 resolver独立性はINCONCLUSIVE
- Test-002: EVT-005でACTION_LOCKED→commit→resolveを実行
- Test-003: EVT-006でbalanced cue集合をdeterministicに全列挙
- Test-004: EVT-007で有限state space全体を結果前lock。`D=-C`という既存分類を弱める非予定結果も選別せず受理

生成方式は `PARTIAL PASS`。

未検証:

- action selector自体を作者側research結果から完全隔離したcontext isolation

## 物語由来の現実研究

### EVT-001 → EXP-003

- PASS
- 3-pattern majority mixture exact match 1件
- F-003 PROVISIONAL

### EVT-002 → EXP-004

- PASS
- balanced cue 200
- update-order runs 4000
- BIDIRECTIONAL 122/200
- F-004 PROVISIONAL

### EVT-006 → EXP-005

- Q-005: pairwise balanced cueのstored-set Hamming isolation
- PAIR_ISOLATED: 200/200
- THIRD_TIED: 0
- THIRD_CLOSER: 0
- 判定: FAIL
- H-005: NOT_SUPPORTED
- F-005: `Hamming距離上のpair isolationは、dynamics / basin上のpair isolationを保証しない。` PROVISIONAL

### EVT-007から生じた研究候補

既存EXP-002 / EXP-003の `NONSTORED_CONVERGED` のうち、stored patternのexact negationに一致するstateを分離すべきか。

これはEXP-003のmixture判定とは別の判定対象になり得る。

ただし、この候補だけを理由にEXP-006を自動作成しない。

## stable ID採番の注意

stable IDを追加する前に、`main`だけでなく**現在のwork branch上の同種IDも確認する**。

## 次の物語側作業

EVT-007後のPER-005 / PER-006を現在stateから動かす。

現在の自然な局所問題:

- なぜA/B/Cの符号反転もfixed pointになるのか
- `nonstored stable`を符号反転・mixture・その他へどう分けるか
- modelの対称性とmemoryとしての意味をどう分離するか
- toy modelからより大きな計算へ進む必要が実際に生じるか

次のoutcome-sensitive eventではACTION_LOCKEDを使う。

生成方式の次の厳密な検証では、action selector自体を作者側研究結果から隔離した別context、または事前に固定したstory-visibleな一般ruleを用いる。

## 未確定

- 具体年月日
- 国・都市・所属研究機関
- PER-005 / PER-006の氏名・年齢・性別
- 計算機・言語・端末
- 二人の正式な所属関係・上下関係
- 現代側最初のevent
- 第2話以降の終了点

必要になる前に一括固定しない。

## 長期探索仮説

輪廻・同一認識主体・NNによる顕在化・情報量による出現確率等はCanonでも現実科学のFindingでもない。

競合説明として模倣、統計的再構成、一般的認知収束、selection bias、pattern over-detection等を残す。

## セキュリティ境界

生のAI内部推論、内部指示、credential、token、秘密値、公開不能な個人情報を保存しない。