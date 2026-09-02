# 現在の状態

このファイルは詳細な正本ではなく、現在位置を示す索引です。矛盾時は直接のevent / state / verification正本を優先します。

更新: 2026-09-03

## フェーズ

- 主目的: 小説
- active work branch: `work/story-bootstrap`
- `main`: human-accepted canonicalのみ。work branchは未反映、PR未作成
- 1980年代側current event head: `EVT-009`
- 第1話: EVT-001〜004をNarrativeProjection済み
- 第2話: EVT-005〜008をNarrativeProjection済み
- 第1話 / 第2話: chapter verification packageとsemantic reviewを通過
- fixed workflow: GitHub Actionsでvalidator tests / executable chapter experiments / strict workflow validationを実行
- World model: typed hierarchical entity/state graph
- 現代側最初のstory event: 未成立

## 1980年代側

開始同期点:

`BOOT-002 @ T0-1980S @ none`

current event head:

`EVT-009`

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
- EVT-009: 既観測final setをstored / stored-negation / residualへ再分類。現在toyでは `R = F \ (S ∪ -S) = ∅`

EVT-009は新規trialやparameter selectionを含まない決定的再分類なのでprovenance `LOCK_NOT_REQUIRED`。一般のHopfield型networkにspurious stateが存在しないという主張ではない。

## 現在の局所問題

EVT-009により、現在の6-unit toy networkをさらに観測しても、stored patternとその符号反転以外のstable finalは出ないことが有限全列挙から確定した。

次のworld advancementで解決すべきなのは、**別種のnonstored stable structureを調べるために、人物が次に何をするか**である。

候補を未来plotとして固定しない。EVT-009後のpersona stateと1980年代環境から選択する。

現在の制約:

- 高橋はmodel条件を変える前に、当時利用可能な理論・文献を確認したい
- 佐伯は問い・変更変数・停止条件・観測量の事前明示を要求する
- 見たい結果から逆算したmodel選択を避ける
- 紙上追跡を超える計算量が因果上必要になった場合のみ、ORG-001の共用計算資源をSYS/OBJとして具体化する
- 現代側EXP-003〜005や後世の研究結果を人物Knowledgeへ漏らさない

## Chapters / verification

### 第1話

- 本文: `novel/chapters/001.md`
- outline: `novel/chapters/001-outline.md`
- adopted events: EVT-001〜004
- verification: `experiments/chapters/001/`

### 第2話

- 本文: `novel/chapters/002.md`
- outline: `novel/chapters/002-outline.md`
- adopted events: EVT-005〜008
- verification: `experiments/chapters/002/`
- executable reproduction: EVT-005〜008を独立再現
- gate: `PREPUBLICATION_GATE_PASSED`

第3話はまだ作らない。まずEVT-009後のworld advancementを続け、自然なreading unitが成立してからNarrativeProjectionする。

## Research boundary

作者側:

- Hopfield系EXP-001〜005まで実施
- EVT-001 → Q-003 / H-003 / EXP-003 / F-003
- EVT-002 → Q-004 / H-004 / EXP-004 / F-004
- EVT-006 → Q-005 / H-005 / EXP-005 / F-005

人物側:

- 現代側EXPの数値集計・seed・仮説判定は未観測
- 後世の研究結果も未観測
- 次の文献行動ではstory time時点で利用可能な資料だけを候補にする

## 未確定

- ORG-001の具体所在地・設立年・所長・研究グループ構成
- 高橋・佐伯の具体職位・正確な年齢
- 具体年月日
- 計算機・OS・programming language
- 二人の正式な上下関係
- ORG-001の将来の再編・閉鎖過程
- 現代側最初のevent
- EVT-010以降
- 第3話の切れ目

必要になるまで一括固定しない。
