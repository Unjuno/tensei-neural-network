# 現在の状態

このファイルは詳細な正本ではなく、現在位置を示す索引です。

更新: 2026-08-21

## フェーズ

- 主目的: 小説
- 物語段階: `起 / 承 / 転`
- 本文: 第1話ドラフト `novel/chapters/001.md` 成立。採用範囲はEVT-001〜004のまま
- 学習段階: CATCH_UP
- 研究段階: Hopfield系EXP-001〜005まで実施
- 生成方式検証: **PARTIAL PASS**。state recovery / 情報境界 / state同期 / NarrativeProjection / resolver pre-lock / cue-set pre-lock / finite state-space全列挙を確認。action selectorの完全なcontext isolationは未検証
- 公開段階: GitHub Pagesは `main /docs`。今回のBootstrap / EVT / 第1話ドラフト / EXP-003以降は未公開

## branch

現在のwork branch:

`work/story-bootstrap`

`main` には反映していない。PRも作成しない。

## 1980年代側の現在位置

開始同期点:

`BOOT-002 @ T0-1980S @ none`

current event head:

`EVT-007`

active personas:

- PER-005 — 1980年代研究者
- PER-006 — 実験神経科学寄りの同僚

### EVT-001〜004

- EVT-001: PER-005が「止まることと、戻ることは同じか」「保存していないところで止まるなら、その状態は何からできている？」と記録
- EVT-002: PER-006が`correct recall`のtargetを誰が定義するか問い返す
- EVT-003: A/Bへ等距離なcueを作り、距離 / final state / update条件 / A/B以外のstateを別記録するprotocolを作成
- EVT-004: 6-unit toy networkで、同一cue・weightsからupdate orderだけの差でA/Bへ分岐する例を観測

EVT-004は数理的一貫性は確認済みだが、具体pattern/cue/orderがoutcome前にlockされていなかったため生成方式検証上は `UNBLINDED`。第1話材料・物語eventとして保持するが、clean resolver validationには数えない。

### EVT-005 — update order集合を結果前にlock

同じ6-unit network / cueについて、自然順序 `(1,2,3,4,5,6)` の全6 cyclic rotationsを結果前に固定し、その後すべてを解決した。

Action-lock commit:

`59ff6530d202b79834afbe8ffdceee1256437315`

結果:

```text
r1 -> A
r2 -> D
r3 -> B
r4 -> B
r5 -> D
r6 -> D
```

この時点ではDをA/B/Cのどれとも一致しないstable stateとして記録した。

Resolution provenance: `LOCKED`。

### EVT-006 — balanced cue集合も結果前に全列挙

A/Bが異なる4 unitから作れるA/B等距離cue全6種類を結果前に固定した。

Action-lock commit:

`97ee4b3d322d367468258775443d6f2aa3551ef1`

6 cues × 6 cyclic orders = 36 trialsをすべて解決。

```text
A_EXACT        11
B_EXACT        11
C_EXACT         2
OTHER_STABLE   12
NONCONVERGED    0
```

- q16はA/B/CすべてへHamming distance 2で、2 ordersからCへ到達
- q24はA/Bへdistance 2ずつだが、initial cue自体がD
- pairwiseな`A/Bの間`という記述だけではnetwork全体の関係を隠し得る

PER-005:

> AとBの間、と書いた時点で、ほかの戻り先を消していたのかもしれない。
>
> 手掛かりは二つの原像だけでは定義できない。

Resolution provenance: `LOCKED`。

### EVT-007 — 6-unit state spaceを全列挙

EVT-006でsubset選択自体が盲点になり得ると分かったため、現在の6-unit networkについて全64 binary initial statesを結果前に固定した。

Action-lock commit:

`3c1034c70853c5704d4064f71ef4e989b4dc296f`

64 states × 6 cyclic orders = 384 trialsを全て解決。

結果:

- 384 / 384 trialが2 sweeps以内にstable
- initial fixed pointsは6個
- unique stable final statesは `A / B / C / -A / -B / -C`
- EVT-005 / EVT-006でDと呼んだ `(+1,+1,+1,+1,-1,+1)` は **`-C`**
- 18 / 64 initial statesは6 ordersすべてで同じfinal
- 46 / 64 initial statesはorderによって2種類以上のfinalへ分岐

46/64を一般的なHopfield networkの頻度へ一般化しない。

row-level結果:

`novel/events/EVT-007-state-space.csv`

PER-005:

> 保存していない、だけでは足りない。
>
> Cを裏返したものまで、別の記憶と呼んでいた。

Resolution provenance: `LOCKED`。

## 第1話ドラフト

`novel/chapters/001.md`

採用event範囲:

`EVT-001`〜`EVT-004`

EVT-005〜EVT-007が後から成立したことを理由に第1話へ自動追加しない。

本文は研究レポート形式にせず、未確定の氏名・年齢・性別・国籍・所属・具体機材等を本文だけで固定しない。

## 生成方式検証

詳細: `notes/generation-validation.md`

- Test-001: 第1話までのstate recovery / persona境界 / NarrativeProjectionはPASS。EVT-004 resolver独立性はUNBLINDEDでINCONCLUSIVE
- Test-002: EVT-005で `ACTION_LOCKED -> commit -> RESOLVED` を実行し、order集合・stopping/inclusion ruleのpre-lockを確認
- Test-003: EVT-006でinitial cue集合もdeterministicに全列挙し、36 trialを選別せず受理
- Test-004: EVT-007でsubset samplingをやめ、全64 states × 6 ordersを結果前lock。予期していなかった`D=-C`という分類修正もそのまま受理

まだ未検証:

- action selectorそのものを作者側研究結果から完全に隔離した別contextで生成しても同様に進められるか

したがって生成方式全体はFULL PASSではなく `PARTIAL PASS` を維持する。

## 物語由来の研究分岐

### EVT-001 → EXP-003

- 判定: PASS
- 3-pattern majority mixture exact match: 1件
- F-003: PROVISIONAL

### EVT-002 → EXP-004

- 判定: PASS
- N=100, P=5
- balanced cue: 200
- update-order runs: 4000
- BIDIRECTIONAL cue: 122 / 200
- F-004: PROVISIONAL

### EVT-006 → EXP-005

Q-005:

> EXP-004のpairwise balanced cueで、selected A/B以外のstored patternがA/BとHamming同距離以下にいる例は存在するか。

EXP-005は結果前に事前登録してEXP-004の200 cuesを再解析した。

結果:

- `PAIR_ISOLATED`: 200 / 200
- `THIRD_TIED`: 0
- `THIRD_CLOSER`: 0
- margin `d_other_min - d_pair`: min 11 / max 30
- 判定: **FAIL**

H-005は `NOT_SUPPORTED`。

F-005:

> **Hamming距離上のpair isolationは、dynamics / basin上のpair isolationを保証しない。**

PROVISIONAL。

### EVT-007からの研究候補

EVT-007では、Dが `-C` だったため、既存EXP-002 / EXP-003の `NONSTORED_CONVERGED` にもstored patternのexact negationが含まれているかという検証可能な問いが生じた。

ただし、これだけを理由にEXP-006を自動生成しない。判定対象と独立研究価値を確認してから必要なら切り出す。

## 最新研究ID

- Q-001: ANSWERED / H-001: SUPPORTED / EXP-001: PASS / F-001: PROVISIONAL
- Q-002: ANSWERED / H-002: SUPPORTED / EXP-002: PASS / F-002: PROVISIONAL
- Q-003: ANSWERED / H-003: SUPPORTED / EXP-003: PASS / F-003: PROVISIONAL
- Q-004: ANSWERED / H-004: SUPPORTED / EXP-004: PASS / F-004: PROVISIONAL
- Q-005: ANSWERED / H-005: NOT_SUPPORTED / EXP-005: FAIL / F-005: PROVISIONAL

研究レポート:

- `research/reports/EXP-001.md`
- `research/reports/EXP-002.md`
- `research/reports/EXP-003.md`
- `research/reports/EXP-004.md`
- `research/reports/EXP-005.md`

## 運用上の修正

Test-003中、current work branch上の既存EVT-005を確認せず一時的に別EVT-005を作る重複が発生した。重複ファイルは検出後に削除し、正しい先行EVT-005を保持した。

再発防止として、stable ID採番前に**`main`だけでなく現在のwork branch上の同種IDも確認する**規則を `AGENTS.md` と `POLICY.md` の双方へ同期済み。

## 次に物語側で行うこと

研究レポートの「次候補」だけを理由にEXP-006を自動生成しない。

EVT-007後のPER-005 / PER-006を現在状態から動かす。

現在の局所問題:

- `x`と`-x`のfixed-point対称性をweight/update ruleからどう説明するか
- `nonstored stable`を符号反転・mixture・その他へどう分けるか
- modelの構造上の対称性とmemoryとしての意味をどう分離するか
- toy modelから計算機実装・より大きな条件へ進む必要が実際に生じるか

outcome-sensitiveな次eventではACTION_LOCKEDを維持する。

生成方式の次の厳密なテストは、action selector自体を作者側研究結果から隔離した別context、または事前に固定したstory-visibleな一般ruleで選ぶこと。

## 未確定

- PER-005 / PER-006の氏名・年齢・性別
- 国・都市・所属機関
- 具体年月日
- 具体的な計算機・言語
- 二人の正式な所属関係・上下関係
- 現代側最初のevent
- 第2話以降の切れ目

必要になるまで一括固定しない。