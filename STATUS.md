# 現在の状態

このファイルは詳細な正本ではなく、現在位置を示す索引です。矛盾時は直接のevent / state / verification正本を優先します。

更新: 2026-09-06

## フェーズ

- 主目的: 小説
- active work branch: `work/story-bootstrap`
- `main`: human-accepted canonicalのみ。work branchは未反映、PR未作成
- 1980年代側current event head: `EVT-013`
- 現代側current event head: none
- World model: typed hierarchical entity/state graph
- fixed workflow: `IN_PROGRESS -> GATE_CANDIDATE -> strict CI PASS -> PREPUBLICATION_GATE_PASSED -> Human Review`

## Chapters

| 話 | 本文 | adopted events | gate |
|---|---|---|---|
| 第1話「戻る先」 | `novel/chapters/001.md` | EVT-001〜004 | prepublication verification済み |
| 第2話「選ばなかった答え」 | `novel/chapters/002.md` | EVT-005〜008 | `PREPUBLICATION_GATE_PASSED` |
| 第3話「表の外」 | `novel/chapters/003.md` | EVT-009〜011 | `PREPUBLICATION_GATE_PASSED` |
| 第4話「五と二十一」 | `novel/chapters/004.md` | EVT-012〜013 | `PREPUBLICATION_GATE_PASSED` |

第3話candidate CI: run `33995822802` success。

第4話candidate CI: run `33996369324` success。

Canon昇格・main反映・実公開はまだHuman Review前。

## 1980年代側

開始同期点: `BOOT-002 @ T0-1980S @ none`

### Active personas

- PER-005 — **高橋修一**。数理工学・理論物理寄りから神経回路・連想記憶へ越境
- PER-006 — **佐伯玲子**。神経生理学・biophysics寄り

### Active organization

- ORG-001 — **光陵化学生命科学研究所**。1970〜80年代日本の企業基礎研究所文化をモデルにした架空研究所

具体所在地、職位、部門名、機種、親会社詳細は必要になるまで固定しない。

## Event chain summary

- EVT-001: 「止まる」と「戻る」を分離
- EVT-002: correct recallのtargetを誰が定義するか
- EVT-003: A/B等距離cueと観測protocol
- EVT-004: 同一cue / weights / ruleでもupdate orderだけでA/Bへ分岐。`UNBLINDED`
- EVT-005: 6 cyclic update ordersをpre-lock。A/B/Dへ分岐
- EVT-006: balanced cue全6種類 × 6 orders = 36 trials
- EVT-007: 全64 states × 6 orders = 384 trials。fixed=`A/B/C/-A/-B/-C`、D=`-C`
- EVT-008: global sign-inversion symmetryを導出
- EVT-009: current toyのresidual `R = F \ (S ∪ -S) = ∅`。`LOCK_NOT_REQUIRED`
- EVT-010: 文献選択規則をpre-lockしHopfield / Feinstein / Palmer 1983を選択
- EVT-011: 1983論文掲載16-neurone example Qをpre-lock再計算。Qはstableかつstored / negation外
- EVT-012: Qを16位置全件分類。Qはcomponentwise majorityと16/16一致。Q-Ms distance=4/4/4、Ms間=8/8/8
- EVT-013: overlap=8/8/8から `h_i(Q)=8(M1_i+M2_i+M3_i)-3Q_i` を導出。unanimity=`21Q_i`、2:1 split=`5Q_i`、EVT-011と16/16一致

EVT-010〜013は1985年以降のmixture-state / spin-glass理論を人物Knowledgeへ逆流させていない。

## Current local question

EVT-013で「なぜQがstableか」はこの掲載例について説明できた。

次に自然に成立している問い:

> **stableであるQは、実際の初期状態から到達されるのか。**

すなわちstabilityとreachability / accessibilityを分離する。

次eventで計算実験へ進む場合の制約:

- starting-state集合を結果前に固定する
- update schedule / order集合を結果前に固定する
- trial数 / stopping ruleを固定する
- random samplingを使うならseedまたはsampling ruleを固定する
- 1983論文のFigure 1を「同じ条件」と偽装しない。掲載32-neurone/5-memoryの具体patternsは論文本文に与えられていない
- 16-neurone掲載例を使う新規accessibility検査は、原論文のFigure 1再現ではなくstory-side follow-upとして区別する
- 紙上追跡を超える計算量が因果上必要になった時点で、ORG-001の共用計算資源を必要な粒度へ展開する

## Research / evidence boundary

### Real-world primary references

- REF-001 — Hopfield (1982), DOI `10.1073/pnas.79.8.2554`
- REF-002 — Hopfield / Feinstein / Palmer (1983), DOI `10.1038/304158a0`, published 1983-07-14

REF-002は30〜1,000 neuronesのmodelling、spurious memories、unlearning、16-neurone / 3-memoryの具体例を扱う。

### Author-side experiments

- EXP-001〜005まで実施
- その数値集計・seed・仮説判定はPER-005 / PER-006へ自動共有しない

## Workflow notes

第3話運転中にgate循環を修正済み。

```text
IN_PROGRESS
-> GATE_CANDIDATE
-> strict CI PASS
-> PREPUBLICATION_GATE_PASSED
```

`GATE_CANDIDATE`にも本番gateと同じ静的条件を適用する。

第4話初稿では制作側メタ表現「第3話」が本文へ混入したため、semantic review前に削除した。本文はstory-world internalな参照だけに修正済み。

## 未確定

- ORG-001の具体所在地・設立年・所長・研究グループ構成
- 高橋・佐伯の具体職位・正確な年齢
- 具体年月日
- 共用計算機の具体機種・OS・programming language
- 二人の正式な上下関係
- ORG-001の将来の再編・閉鎖過程
- 現代側最初のevent
- EVT-014以降
- 第5話以降の切れ目

必要になるまで一括固定しない。
