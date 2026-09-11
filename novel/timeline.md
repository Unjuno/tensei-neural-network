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

- 1980年代側: `EVT-015`
- 現代側: none

EVT-015時点の1980年代active personas: PER-005 高橋修一 / PER-006 佐伯玲子。

## Story time と narrative order

- 第1話: EVT-001〜004
- 第2話: EVT-005〜008
- 第3話: EVT-009〜011
- 第4話: EVT-012〜013
- EVT-014〜015: 未投影。第5話を成立させるためにeventを追加しない

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

## 作者側研究（人物Knowledgeとは分離）

EVT-014/015からEXP-006を分岐。N=16/P=3の256 eligible majority mixtures、65,536 trajectoriesを事前登録条件で検証。

primary H-006は弱いSUPPORT。一方secondaryで、split one-bitからQへ戻らなかった17,488/17,488 trajectoriesがcoordinate-minority stored patternへ到達。

これを受けEXP-007で反例探索を事前登録。N=8,12,16,20,24、640 eligible triples、362,704 trajectoriesを探索し、111,680 non-Q trajectoriesすべてで同じ規則が成立。counterexample 0。

**これは作者側結果でありPER-005/PER-006へ自動共有しない。一般定理でもない。**

## Current next question

Story側、EVT-015後:

> 一ビット近傍で見えたorder dependenceを、二人が知るこの具体例の代数だけからどこまで説明できるか。

Author research側:

> EXP-006/007で反例が見つからないcoordinate-minority escapeを、P=3 majority mixtureの代数から証明できるか。それとも固定探索外の反例を構成できるか。

trial数を無目的に増やすより解析を優先する。

## 現代

- `T0-MODERN`を現代側開始同期点候補とする。具体年月日は未確定
- 現代側最初のEVTは未成立
- 1980年代側EVTが成立していても現代personaへ自動共有しない
- 過去研究者と現代モデルの同一性・輪廻は確定していない
