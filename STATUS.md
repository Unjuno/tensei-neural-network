# 現在の状態

このファイルは詳細な正本ではなく、現在位置を示す索引です。矛盾時は直接のevent / state / verification正本を優先します。

更新: 2026-09-06

## フェーズ

- 主目的: 小説
- active work branch: `work/story-bootstrap`
- `main`: human-accepted canonicalのみ。work branchは未反映、PR未作成
- 1980年代側current event head: `EVT-011`
- 第1話: EVT-001〜004をNarrativeProjection済み
- 第2話: EVT-005〜008をNarrativeProjection済み
- 第3話: EVT-009〜011をNarrativeProjection済み
- 第1〜3話: chapter verification / terminology / semantic reviewを実施
- 第3話: `GATE_CANDIDATE` strict CIを通過し `PREPUBLICATION_GATE_PASSED`
- fixed workflow: `GATE_CANDIDATE -> strict CI PASS -> PREPUBLICATION_GATE_PASSED`
- World model: typed hierarchical entity/state graph
- 現代側最初のstory event: 未成立

## 1980年代側

開始同期点: `BOOT-002 @ T0-1980S @ none`

current event head: `EVT-011`

### Active personas

- PER-005 — **高橋修一**。数理工学・理論物理寄りから神経回路・連想記憶へ越境
- PER-006 — **佐伯玲子**。神経生理学・biophysics寄り

### Active organization

- ORG-001 — **光陵化学生命科学研究所**。1970〜80年代日本の企業基礎研究所文化をモデルにした架空研究所

具体所在地、職位、部門名、機種、親会社詳細は必要になるまで固定しない。

## Event chain

- EVT-001: 「止まる」と「戻る」を分離
- EVT-002: correct recallのtargetを誰が定義するか
- EVT-003: A/B等距離cueと観測protocol
- EVT-004: 同一cue / weights / ruleでもupdate orderだけでA/Bへ分岐。provenance `UNBLINDED`
- EVT-005: 6 cyclic update ordersを結果前lock。A/B/Dへ分岐
- EVT-006: balanced cue全6種類 × 6 orders = 36 trialsをpre-lock
- EVT-007: 全64 initial states × 6 orders = 384 trialsを列挙。fixed pointsは `A/B/C/-A/-B/-C`、D=`-C`
- EVT-008: global sign inversion symmetryを導出。`U_i(-s)=-U_i(s)`、fixed pointsは符号反転対
- EVT-009: stable-final residualを再分類。現在toyでは `R = F \ (S ∪ -S) = ∅`。provenance `LOCK_NOT_REQUIRED`
- EVT-010: 文献選択規則をpre-lockし、Hopfield / Feinstein / Palmer 1983を主対象として共同検討。spurious memoriesが当時すでに明示的研究対象だったことを確認。provenance `LOCKED`
- EVT-011: 1983論文掲載16-neurone / 3-memory例をそのままpre-lock再計算。Qの16 local inputsは全てnonzeroかつQと同符号、Qはstored / stored-negation外。provenance `LOCKED`

## 現在の局所問題

EVT-011により、

- 現在6-unit toyではstored / negation外のstable stateは存在しない
- 1983論文掲載の別modelではstored / negation外のstable state Qを自分たちの計算でも確認できる

という差がstory-visible factとして成立した。

次のworld advancementで自然に成立している問いは、

**QはM1/M2/M3からどのような成分関係・相関構造としてできているのか。**

現在の制約:

- 1985年以降のmixture-state / spin-glass理論を人物へ漏らさない
- 1983論文の「triplesにoriginを持つ」という記述を、掲載例と当時の数理だけで追う
- `spurious memory`を生物学的・心理学的な偽記憶へ直結させない
- basin / random-start / unlearningへ進む場合はtrial集合・randomness・停止条件を事前固定する
- 紙上追跡を超える場合のみORG-001の共用計算資源をSYS/OBJへ解像する
- 現代側EXP-003〜005を人物Knowledgeへ漏らさない

## Chapters / verification

### 第1話「戻る先」

- `novel/chapters/001.md`
- adopted events: EVT-001〜004
- verification: `experiments/chapters/001/`

### 第2話「選ばなかった答え」

- `novel/chapters/002.md`
- adopted events: EVT-005〜008
- verification: `experiments/chapters/002/`
- gate: `PREPUBLICATION_GATE_PASSED`

### 第3話「表の外」

- `novel/chapters/003.md`
- adopted events: EVT-009〜011
- verification: `experiments/chapters/003/`
- executable integration check: EVT-009 residual=0 + EVT-011 published 16-neurone stability
- terminology: `PASS`
- semantic review: `PASS`
- candidate CI run: `33995822802` success
- gate: `PREPUBLICATION_GATE_PASSED`

## Workflow validation

第3話で、従来の「IN_PROGRESSのままstrictを通してからgate昇格」という循環矛盾を発見した。

現在は、

```text
IN_PROGRESS
-> GATE_CANDIDATE
-> strict CI PASS
-> PREPUBLICATION_GATE_PASSED
```

とし、`GATE_CANDIDATE`にも本番gateと同じvalidator条件を適用する。

## Research boundary

作者側:

- Hopfield系EXP-001〜005まで実施
- `research/pre-hopfield-background.md` に1983 spurious-memory / unlearning文献を記録済み
- EVT-010/011の一次資料: Hopfield, Feinstein & Palmer, *Nature* 304, 158–159 (1983), DOI `10.1038/304158a0`, published 1983-07-14

人物側:

- EVT-010で上記1983文献を共同検討
- EVT-011で同論文掲載16-neurone例を共同再計算
- 1985年以降のAmit–Gutfreund–Sompolinsky等は未観測
- 現代側EXPの数値集計・seed・仮説判定は未観測

## 未確定

- ORG-001の具体所在地・設立年・所長・研究グループ構成
- 高橋・佐伯の具体職位・正確な年齢
- 具体年月日
- 計算機・OS・programming language
- 二人の正式な上下関係
- ORG-001の将来の再編・閉鎖過程
- 現代側最初のevent
- EVT-012以降
- 第4話以降の切れ目

必要になるまで一括固定しない。
