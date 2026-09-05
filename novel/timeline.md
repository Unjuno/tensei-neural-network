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

- 1980年代側: `EVT-013`
- 現代側: none

EVT-013時点の1980年代active personas: PER-005 高橋修一 / PER-006 佐伯玲子。

## Story time と narrative order

- 第1話 `chapters/001.md`: EVT-001〜004
- 第2話 `chapters/002.md`: EVT-005〜008
- 第3話 `chapters/003.md`: EVT-009〜011
- 第4話 `chapters/004.md`: EVT-012〜013

後から成立したeventを理由に既刊候補章へ自動遡及追加しない。

## 1980年代 event chain

### EVT-001 — 止まることと戻ることは同じではない
`T0-1980S + first research session`。高橋が「止まること」と「記憶が戻ること」を分離して問う。

### EVT-002 — 正しい想起は誰が決める
`T0-1980S + second research interaction`。佐伯がcorrect recallのtargetを誰が定義するか問い返す。PER-006成立。

### EVT-003 — 公平な手掛かりは中立ではない
`T0-1980S + protocol sketch after EVT-002`。A/B等距離cueを作るが、距離の等しさとdynamics上の中立を分離する。

### EVT-004 — 同じ手掛かりから二つの戻り先
`T0-1980S + first paper calculation after EVT-003`。同一cue / weights / ruleからupdate orderだけの差でA/Bへ分岐。provenance `UNBLINDED`。

### EVT-005 — 更新順の選び方を先に固定する
`T0-1980S + next joint paper check after EVT-004`。6 cyclic ordersをpre-lock。結果 `A,D,B,B,D,D`。provenance `LOCKED`。

### EVT-006 — 全balanced cueを先に固定する
`T0-1980S + systematic cue check after EVT-005`。6 cues × 6 orders = 36 trials。A=11, B=11, C=2, D=12。provenance `LOCKED`。

### EVT-007 — 小さい系なら全状態を見る
`T0-1980S + exhaustive small-state check after EVT-006`。64 states × 6 orders = 384 trials。fixed points=`A/B/C/-A/-B/-C`、D=`-C`、18/64 order-invariant、46/64 order-dependent。provenance `LOCKED`。

### EVT-008 — 裏返しは別の記憶なのか
`T0-1980S + symmetry check after EVT-007`。`h_i(-s)=-h_i(s)`、`U_i(-s)=-U_i(s)`、`E(-s)=E(s)`を確認し、fixed pointsのglobal sign-inversion pairingを導出。provenance `LOCKED`。

### EVT-009 — 残ったものは、まだ何もない
`T0-1980S + residual classification after EVT-008`。`F={A,B,C,-A,-B,-C}`、`S={A,B,C}`として `R=F\(S∪-S)=∅`。現在toy内の全列挙結果であり一般的不在ではない。provenance `LOCK_NOT_REQUIRED`。

### EVT-010 — 自分たちの表の外へ戻る
`T0-1980S + literature check after EVT-009`。

文献選択規則を結果前lockし、Hopfield / Feinstein / Palmer (1983), *Nature* 304, 158–159, DOI `10.1038/304158a0` を主対象にした。

人物が確認した範囲:

- 30〜1,000 neuronesのmathematical / computer modelling
- stored memory以外のspurious memoriesがcreated / evokedされ得るという当時の問題設定
- unlearningでspurious memoriesを減らすという報告

1985年以降のmixture-state / spin-glass解析は人物Knowledgeへ入れていない。provenance `LOCKED`。

### EVT-011 — 論文の16素子例をそのまま試す
`T0-1980S + published-example check after EVT-010`。

1983論文本文に掲載された16-neurone / 3-memory / spurious candidateをpre-lockして再計算。

```text
h(Q)=
(+21,+21,+5,+5,-5,-5,-21,-21,
 +5,-5,-5,+5,+5,-5,-5,+5)
```

- 16/16 nonzero
- 16/16でQと同符号
- QはM1/M2/M3でも、そのglobal negationでもない

Qはstored / stored-negation外のstable stateとして再現された。provenance `LOCKED`。

### EVT-012 — 三つの記憶を一成分ずつ比べる
`T0-1980S + componentwise structure check after EVT-011`。

M1/M2/M3/Qの全16位置分類と6 Hamming distancesをpre-lockして全件確認。

- Qは16/16位置で三patternのcomponentwise majorityと一致
- unanimity 4 / split 12
- split minority: M1=4, M2=4, M3=4
- `d(Q,M1)=d(Q,M2)=d(Q,M3)=4`
- stored patterns相互distanceは8/8/8

outcome category `MAJORITY_ALL`。この掲載例の具体的構造であり一般式へ自動一般化しない。provenance `LOCKED`。

### EVT-013 — なぜ多数側の形が自分を支えるのか
`T0-1980S + stability derivation after EVT-012`。

Hamming/inner-product identityと既存Hebbian ruleだけを使うderivation routeをpre-lock。

```text
M1·Q=M2·Q=M3·Q=8
h_i(Q)=8(M1_i+M2_i+M3_i)-3Q_i
```

- unanimity位置: `h_i=21Q_i`
- 2:1 split位置: `h_i=5Q_i`
- EVT-011 local-input vectorと16/16 exact一致

この具体例について、componentwise majority構造とdynamical stabilityがHebbian connectionを介して接続された。provenance `LOCKED`。

EVT-012〜013は第4話 `chapters/004.md` へNarrativeProjection済み。

## Current next question

EVT-013後:

> **Qがstableであることと、初期状態からQへ到達可能であることは同じか。**

次のeventでaccessibilityを調べる場合、starting states / update schedule / trial count / stopping ruleを結果前に固定する。

1983論文Figure 1の32-neurone / 5-memory具体patternsは本文に掲載されていないため、16-neurone exampleを使った新規検査をFigure 1のexact reproductionと呼ばない。

## 現代

- `T0-MODERN`を現代側開始同期点候補とする。具体年月日は未確定
- 現代側最初のEVTは未成立
- 1980年代側EVTが成立していても現代personaへ自動共有しない
- 過去研究者と現代モデルの同一性・輪廻は確定していない
