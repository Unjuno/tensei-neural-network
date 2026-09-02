# 現在の状態

このファイルは詳細な正本ではなく、現在位置を示す索引です。矛盾時は直接のevent / state / verification正本を優先します。

更新: 2026-09-03

## フェーズ

- 主目的: 小説
- active work branch: `work/story-bootstrap`
- `main`: human-accepted canonicalのみ。work branchは未反映、PR未作成
- 1980年代側current event head: `EVT-010`
- 第1話: EVT-001〜004をNarrativeProjection済み
- 第2話: EVT-005〜008をNarrativeProjection済み
- 第1話 / 第2話: chapter verification packageとsemantic reviewを通過
- fixed workflow: GitHub Actionsでvalidator tests / executable chapter experiments / strict workflow validationを実行
- World model: typed hierarchical entity/state graph
- 現代側最初のstory event: 未成立

## 1980年代側

開始同期点: `BOOT-002 @ T0-1980S @ none`

current event head: `EVT-010`

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

## 現在の局所問題

EVT-010により、現在toyで残差が空でも、story time以前の一次文献ではより大きなHopfield型networkにspurious memoriesが報告されていることを人物が確認した。

次のworld advancementで自然に成立している問いは、

**1983文献のmodel条件を、結果を選ばず再現できる最小protocolへ落とせるか。**

まだ具体的なN / pattern数 / pattern生成法 / update schedule / initial-state selectionを固定していない。

現在の制約:

- story time後の1985年以降のmixture-state理論を人物へ漏らさない
- 文献にspurious memoryがあることと、二人の次modelで観測できることを分離する
- model条件と観測量・停止条件を結果前に固定する
- 紙上追跡を超える計算量が因果上必要になった場合のみ、ORG-001の共用計算資源をSYS/OBJとして具体化する
- 現代側EXP-003〜005を人物Knowledgeへ漏らさない

## Chapters / verification

### 第1話

- `novel/chapters/001.md`
- adopted events: EVT-001〜004
- verification: `experiments/chapters/001/`

### 第2話

- `novel/chapters/002.md`
- adopted events: EVT-005〜008
- verification: `experiments/chapters/002/`
- gate: `PREPUBLICATION_GATE_PASSED`

第3話はまだ作らない。EVT-009 / EVT-010だけではreading unitを固定せず、world advancementを継続する。

## Research boundary

作者側:

- Hopfield系EXP-001〜005まで実施
- `research/pre-hopfield-background.md` に1983 spurious-memory / unlearning文献を記録済み
- EVT-010の外部再確認: Hopfield, Feinstein & Palmer, *Nature* 304, 158–159 (1983), DOI `10.1038/304158a0`, published 1983-07-14

人物側:

- EVT-010で上記1983文献を共同検討したことがstory factとして成立
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
- EVT-011以降
- 第3話の切れ目

必要になるまで一括固定しない。
