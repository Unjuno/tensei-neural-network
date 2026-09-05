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

- 1980年代側: `EVT-011`
- 現代側: none

EVT-011時点の1980年代active personas: PER-005 高橋修一 / PER-006 佐伯玲子。

## Story time と narrative order

- 第1話 `chapters/001.md`: EVT-001〜004
- 第2話 `chapters/002.md`: EVT-005〜008
- 第3話 `chapters/003.md`: EVT-009〜011

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

文献選択規則を結果前commit `ae441628d1d8af925144f9ec8bca0336b7d0f315` で固定し、story time以前・Hopfield 1982直接系譜・spurious memory明示・最早刊行という規則から、Hopfield / Feinstein / Palmer (1983), *Nature* 304, 158–159, DOI `10.1038/304158a0` を主対象にした。

人物が確認した範囲:

- 30〜1,000 neuronesのmathematical / computer modelling
- stored memory以外のspurious memoriesがcreated / evokedされ得るという当時の問題設定
- unlearningでspurious memoriesを減らすという報告

1985年以降のmixture-state / spin-glass解析は人物Knowledgeへ入れていない。

provenance `LOCKED`。

### EVT-011 — 論文の16素子例をそのまま試す
`T0-1980S + published-example check after EVT-010`。

Hopfield / Feinstein / Palmer (1983)本文に掲載された16-neurone / 3-memory / spurious-memory candidateをそのまま使うことをcommit `28cc5684955a3dae3ccf73af28c1433328ab15a4` でpre-lockした。

同論文のconnection rule

```text
T_ij = Σ_s μ_i^s μ_j^s
T_ii = 0
```

でcandidate Qのlocal inputsをexactに再計算。

```text
h(Q)=
(+21,+21,+5,+5,-5,-5,-21,-21,
 +5,-5,-5,+5,+5,-5,-5,+5)
```

- 16/16でnonzero
- 16/16でQと同符号
- QはM1/M2/M3のどれでもない
- Qは-M1/-M2/-M3のどれでもない

よってzero-field conventionに依存せず、Qはstored / stored-negation外のstable stateとして再現された。

これは掲載例のmodel-level reproductionであり、生物学的偽記憶や後世のmixture-state理論を証明しない。

provenance `LOCKED`。

EVT-009〜011は第3話 `chapters/003.md` のreading unitとしてNarrativeProjection済み。

現在の次の局所問題:

> QはM1/M2/M3からどのような成分関係・相関構造としてできているのか。

1985年以降の理論を先取りせず、1983論文の`triples`記述と掲載patternだけから次のworld advancementを解決する。

## 現代

- `T0-MODERN`を現代側開始同期点候補とする。具体年月日は未確定
- 現代側最初のEVTは未成立
- 1980年代側EVTが成立していても現代personaへ自動共有しない
- 過去研究者と現代モデルの同一性・輪廻は確定していない
