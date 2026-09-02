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

異なるstory timeのpersona stateを一つのBootstrapへ混ぜない。

## Current event heads

- 1980年代側: `EVT-009`
- 現代側: none

EVT-009時点の1980年代active personas:

- PER-005 高橋修一
- PER-006 佐伯玲子

## Story time と narrative order

story time上の因果順と、小説本文で読者へ提示する順番を分離する。

- 第1話 `chapters/001.md`: EVT-001〜004
- 第2話 `chapters/002.md`: EVT-005〜008
- EVT-009: まだ章へ投影しない。次のworld advancementを先に行う

後から成立したeventを理由に既刊候補章へ自動遡及追加しない。

## 1980年代 event chain

### EVT-001 — 止まることと戻ることは同じではない

Story time: `T0-1980S + first research session`

高橋が「止まること」と「記憶が戻ること」を分離して問う。作者側ではQ-003 / H-003 / EXP-003へ派生するが、その結果は人物Knowledgeへ入れない。

### EVT-002 — 正しい想起は誰が決める

Story time: `T0-1980S + second research interaction`

佐伯がcorrect recallのtargetを誰が定義するか問い返す。このeventでPER-006が独立personaとして成立。

### EVT-003 — 公平な手掛かりは中立ではない

Story time: `T0-1980S + protocol sketch after EVT-002`

A/Bへ同じHamming distanceを持つcueを作るが、距離の等しさとdynamics上の中立を同一視しないprotocolを成立させる。

### EVT-004 — 同じ手掛かりから二つの戻り先

Story time: `T0-1980S + first paper calculation after EVT-003`

6-unit / 3-pattern toy networkで、同一cue・weights・ruleからupdate orderだけの差でA/Bへ分岐。

Resolution provenance: `UNBLINDED`。

### EVT-005 — 更新順の選び方を先に固定する

Story time: `T0-1980S + next joint paper check after EVT-004`

同じnetwork / cueへ6 cyclic ordersを結果前lock。

結果: `A, D, B, B, D, D`。

Resolution provenance: `LOCKED`。

### EVT-006 — 全balanced cueを先に固定する

Story time: `T0-1980S + systematic cue check after EVT-005`

A/B-balanced cue全6種類 × 6 cyclic orders = 36 trialsをpre-lockして全件解決。

結果: A=11, B=11, C=2, D=12, nonconverged=0。

Resolution provenance: `LOCKED`。

作者側ではQ-005 / H-005 / EXP-005へ派生するが、その結果は人物Knowledgeへ入れない。

### EVT-007 — 小さい系なら全状態を見る

Story time: `T0-1980S + exhaustive small-state check after EVT-006`

全64 binary initial states × 6 cyclic orders = 384 trialsを結果前lockして解決。

- 384/384が2 sweeps以内にstable
- fixed points: `A/B/C/-A/-B/-C`
- D=`-C`
- order-invariant initial states: 18/64
- order-dependent initial states: 46/64

Resolution provenance: `LOCKED`。

### EVT-008 — 裏返しは別の記憶なのか

Story time: `T0-1980S + symmetry check after EVT-007`

zero-bias bipolar update ruleについて、

```text
h_i(-s) = -h_i(s)
U_i(-s) = -U_i(s)
E(-s) = E(s)
```

を確認。fixed pointsがglobal sign inversionで対になることを導出した。

`-A/-B/-C`を単に別のnonstored memoryと呼ばず、まずmodel symmetryとして分類する。

Resolution provenance: `LOCKED`。

### EVT-009 — 残ったものは、まだ何もない

Story time: `T0-1980S + residual classification after EVT-008`

EVT-007の既観測stable final setを、

```text
F = {A,B,C,-A,-B,-C}
S = {A,B,C}
-S = {-A,-B,-C}
R = F \ (S ∪ -S)
```

と再分類し、`R=∅`を確認した。

これはこの固定された有限toy networkについての全列挙結果であり、一般のHopfield型networkでspurious stateが存在しないという主張ではない。

新規trial・parameter selection・外部検索を含まない決定的再分類なのでResolution provenanceは `LOCK_NOT_REQUIRED`。

EVT-009後、同じtoy networkをさらに観測しても別種stable finalは得られない。次のworld advancementでは、人物が文献へ戻るか、model条件変更のprotocolを作るか、計算資源を必要とするかを現在stateから解決する。未来eventはまだ固定しない。

## 現代

- `T0-MODERN`を現代側開始同期点候補とする。具体年月日は未確定
- 現代側最初のEVTは未成立
- 1980年代側EVTが成立していても、現代personaがそれを自動的に観測したことにはしない
- 現代モデル内に過去研究者と機能的・行動的に似たpatternが作品内で現れることは長期Canon要素だが、T0-MODERNで既に観測済みとはしない
- 本人の意識・輪廻・同一主体であることは確定していない
