# 時系列

物語時間とevent chainの索引。詳細な客観事実は各event / state正本、現実史は`research/`と一次資料へ戻って確認する。

## Bootstrap同期点

```text
T0-1980S
  Bootstrap: BOOT-002
  Parent event head: none
  Initial persona: PER-005

T0-MODERN
  Bootstrap: BOOT-001
  Parent event head: none
  Personas: PER-001 / PER-002 / PER-003 / PER-004
```

## Current event heads

- 1980年代側: `EVT-020`
- 現代側: none

EVT-020時点の1980年代active personas: PER-005 高橋修一 / PER-006 佐伯玲子。

## Story time と narrative order

- 第1話: EVT-001〜004
- 第2話: EVT-005〜008
- 第3話: EVT-009〜011
- 第4話: EVT-012〜013
- 第5話: EVT-014〜018

## 1980年代 event chain

EVT-001〜013の詳細は各event正本を参照。現在までの流れ:

```text
EVT-001 問い: stopping != recall
→ EVT-002 correct recallの定義
→ EVT-003 等距離 != dynamical neutrality
→ EVT-004 same cue / two returns
→ EVT-005 order family lock
→ EVT-006 all balanced cues
→ EVT-007 6-unit全状態
→ EVT-008 sign inversion symmetry
→ EVT-009 toy residual empty
→ EVT-010 1983一次文献へ戻る
→ EVT-011 published 16-unit spurious Qを再計算
→ EVT-012 Q = componentwise majority (16/16)
→ EVT-013 majority structureから5/21 local inputを導出
```

### EVT-014 — Qの一ビット近傍からの到達性

`T0-1980S + immediate follow-up after EVT-013`。

結果前にQのHamming距離1近傍16状態と16 cyclic update ordersを固定。256 trial全件を計算。

- Q final: 112
- M1/M2/M3: 各48
- nonconverged: 0
- k=1,2,7,8（stored patterns全員一致位置）のflipは16/16 orderでQへ復帰
- 2対1位置のflipはorder-dependent
- Qへ戻らないtrialは、その位置の少数派stored patternへだけ到達

provenance `LOCKED`。

### EVT-015 — 反転した一ビットが少数派memoryを近づける

EVT-014の固定済みinitial statesを追加trialなしで再分類。

2対1位置をflipすると、

- coordinate-minority stored pattern: distance 4→3 / overlap 8→10
- 他二stored patterns: distance 4→5 / overlap 8→6

全員一致位置をflipすると三stored patternsすべてdistance 4→5 / overlap 8→6。

これによりEVT-014のescape方向には明確な初期幾何があることを確認。ただしnearest stored patternが一般にfinalを決めるとはしない。

provenance `LOCK_NOT_REQUIRED`。

### EVT-016 — 最初に動いた素子で分岐が決まる

EVT-014のsplit一bit初期状態12×16 cyclic orders=192 trajectoryを、結果前lockしたfirst actual flip分類で再計算。damaged bitが最初に修復されれば48/48でQ、別unitが先なら144/144でそのcoordinateのminority stored patternへ。provenance `LOCKED`。

### EVT-017 — 初期状態には4つの不安定候補

12初期状態×16 local inputsを事前条件に従って全件分類。各split one-bit initial stateで、`FLIP_IF_UPDATED`集合はminority memoryとQの4-bit difference set `D(k)` に12/12で一致。HOLD_TIEなし。provenance `LOCKED`。

### EVT-018 — 巡回順の件数は円周上の隙間

既知の4点集合 `D(k)` を円周上に置き、cyclic startからdamaged kが最初のunstable unitとなる開始点数をgapとして再分類。M3: 13/1/1/1、M2: 10/2/1/3、M1: 10/3/1/2。各組16件、split Q-return 48件、unanimous Q-return 64件、計112件をsimulationとは独立に説明。追加trialなし、provenance `LOCK_NOT_REQUIRED`。

EVT-014〜018を第5話「最初に動いたもの」へNarrativeProjection済み。第5話公開前gateはPASS、Human Reviewは未実施。

### EVT-019 — 二つの問いを分ける

`T0-1980S + next discussion after EVT-018`。高橋は別の更新順へ広げる問いを示したが、新たなschedule・trialを選ばず、佐伯は同じ最終状態を異なる経路から得る場合の観測上の区別を自分の課題として引き受けた。二人はモデル内部の解析と生理学的な観測可能性を別の未解決問題として共同メモに記し、共用計算資源の追加利用・研究所への正式提出・新しい実験を実施しなかった。ORG-001のinstitutional memoryは不変。社会的対話の生成は`UNBLINDED`であり独立生成証拠ではない。

第6話へのNarrativeProjectionは未実施。本文や既刊の状態は不変。

### EVT-020 — 同じ細胞でも同じ課題ではない

`T0-1980S + PER-006 independent literature reading after EVT-019`。佐伯は1975年刊の久保田競の原著（REF-003、DOI: `10.2170/jjphysiol.25.481`）を個人で参照し、同じ単一unitの放電を遅延反応・遅延交代という二つの課題で比較する観測について知る。95 unitは報告全体の件数で、95-unit同時測定ではない。

- 文献の課題条件・手掛かり・遅延・応答を、模型のQという終状態と同一視しない
- 佐伯だけの局所Knowledgeに反映。高橋・ORG-001の公式記録へ自動伝播なし
- 動物実験・装置・予算・文献所蔵・研究所提出・新しい数値計算は未成立
- 作者が候補を調べた後に選んだ論文なのでprovenance `UNBLINDED`。その結果選択は独立blind生成の根拠ではない

詳しくは `events/EVT-020-the-same-neuron-different-task.md`、`state/personas/deltas/EVT-020.md`、作者側一次研究 `../research/1980s-neurophysiology-observation-boundary.md`。第6話への投影はまだ成立していない。



## 作者側研究（人物Knowledgeとは分離）

EVT-014/015由来のEXP-006/007ではfinite searchから少数派escapeを観測し、別途P=3・symmetric Hebbian・非同期fair one-unit update・zero-input保持の条件で解析的に説明した。EXP-011ではQのzero marginを許す条件へ拡張。

EXP-008で同期更新はperiod-2 cycleを作る反例が成立。EXP-010では偶数Nのzero-margin探索設計が構造上不適格だった。EXP-012でP=5への拡張に反例。EXP-013でN=7〜16、640 eligible triples、139,440 trajectoriesの事前登録margin三領域分類が全件一致。EXP-009は事前登録されているが、README上は未実行。

**これらは作者側の知識であり、人物へ自動共有しない。** 有限探索成功と一般証明、同期/非同期、異なるPを混同しない。

## Current next question

Story側、EVT-020後:

> 高橋は別の更新順を調べる前に何を固定するか。佐伯は1975年の前頭前野単一unit研究で見た課題依存性を、模型の二値状態との非同一性を保ったまま、どの観測条件へ落とせるか。

ここはまだ未解決。第6話を成立させるためにeventを発生させず、現在のpersona Goals/Knowledgeと組織制約からaction selectionを行う。

Author research側は、EXP-009等の既に登録した検査を扱う場合、結果を見る前に固定した条件を変更しない。

## 現代

- `T0-MODERN`を現代側開始同期点候補とする。具体年月日は未確定
- 現代側最初のEVTは未成立
- 1980年代側EVTが成立していても現代personaへ自動共有しない
- 過去研究者と現代モデルの同一性・輪廻は確定していない
