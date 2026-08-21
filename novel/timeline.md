# 時系列

物語時間とAI技術史の接続を管理します。

## 正本との関係

物語上の客観的事実について、このファイルは `novel/canon.md` の**時系列上の投影・索引**です。`canon.md` と食い違う場合は `canon.md` を正本として優先し、このファイルを修正します。

初期化・再初期化の同期点は `novel/bootstrap/`、人物そのものの定義は `novel/personas/`、人物の時間依存状態は `novel/state/personas/`、世界・環境の定義は `novel/environment.md`、世界の時間依存状態は `novel/state/world.md` で管理します。

現実の技術史の事実は必ず `references/` と `research/` の根拠へ戻って確認し、このファイルだけを科学的出典として扱わないでください。

## 共通の時間軸

ペルソナと世界は別々の状態領域ですが、**時系列上の状態遷移は独立させません。**

`events/` に記録された同じ出来事を共通の時間上の結合点として、世界状態と関係するペルソナ状態を更新します。

```text
story time t
  ├─ world: W(t)
  ├─ PER-001: P_001(t)
  ├─ PER-002: P_002(t)
  └─ ...
       |
       | EVT-k
       v
story time t+1
  ├─ world: W(t+1)
  ├─ PER-001: P_001(t+1)
  ├─ PER-002: P_002(t+1)
  └─ ...
```

変化しなかったペルソナは前状態を継承してよく、全員のsnapshotを毎回複製する必要はありません。

新しいペルソナが途中から登場する場合、その主体が物語上で成立した時点から状態履歴を開始します。

### Bootstrap同期点

Bootstrapはeventではなく、あるstory timeの状態を同じ背景から再構成できる制作上の同期点です。BOOT IDは作成順の識別子であり、story timeやnarrative orderを表しません。

現在の同期点:

```text
T0-1980S
  Bootstrap: BOOT-002
  Parent event head: none
  World: state/world.md
  Initial personas: PER-005

T0-MODERN
  Bootstrap: BOOT-001
  Parent event head: none
  World: state/world.md
  Personas: PER-001 / PER-002 / PER-003 / PER-004
```

- `BOOT-002 @ T0-1980S @ none` — 1980年代側の物語最初の実働開始同期点
- `BOOT-001 @ T0-MODERN @ none` — 現代側へ移った際の開始同期点候補

異なるstory timeのペルソナ状態を一つのBootstrapへ混ぜない。

### Current event heads

- 1980年代側: `EVT-006`
- 現代側: none

EVT-006時点の1980年代active personas:

- PER-005
- PER-006

### Story time と narrative order

物語世界で実際に起きた時刻・因果順と、小説本文で読者へ提示する順番を分離します。

現時点では、哲学・技術史を圧縮した導入から1980年代側へ入り、PER-005の研究・思考が動き、PER-006との相互作用と最初の紙上計算へ進む流れが第1話ドラフト `chapters/001.md` として成立している。

第1話の採用event範囲は `EVT-001`〜`EVT-004` のままにする。EVT-005 / EVT-006が後から成立したことを理由に、第1話へ自動追加しない。

EVT-004は第1話のNarrativeProjection上の切れ目として有効だが、具体条件の解決前lockがないためResolution provenanceは `UNBLINDED`。EVT-005 / EVT-006はその後のstory timeで `ACTION_LOCKED → commit → RESOLVED` を通したeventである。

将来、現代場面の後に1980年代を回想する等の構成へ変更しても、story time上の状態位置は変えない。

## 物語上の時系列

### 1980年代以前 — 導入背景

- 記憶、想起、自己同一性、連想等の問いには長い哲学的・概念的背景がある。
- 20世紀には神経networkの形式化、学習、feedback、自己組織化、連想記憶、安定状態等を扱う複数の研究系譜が成立する。
- これらを一本の必然的な技術系譜とは扱わず、直接関係と作品上の共鳴を分ける。
- 詳細調査は `research/pre-hopfield-background.md` を参照する。

### 1980年代

- `T0-1980S`をPER-005の最初の実働同期点とする。
- `BOOT-002`により1980年代側の世界状態とPER-005を同じ背景から同期する。
- 1984〜1985年前後を中心候補とするが、具体年月日は未確定。
- PER-005はニューラルネットワーク、記憶、連想、状態再構成に近い問題へ関わる。
- 所属環境の細部はまだ未確定。

#### EVT-001 — 止まることと戻ることは同じではない

Story time: `T0-1980S + first research session`

PER-005はcontent-addressable memoryとspurious memoryをめぐる問題設定を比較し、

- 「止まることと、戻ることは同じか」
- 「保存していないところで止まるなら、その状態は何からできている？」

という問いを残した。

研究側ではこの問いからQ-003 / H-003 / EXP-003が独立に派生したが、その現代的解析結果をPER-005が知ったことにはしない。

#### EVT-002 — 正しい想起は誰が決める

Story time: `T0-1980S + second research interaction`

PER-006は、実験者がtargetを知っていることと、曖昧cueに対してnetwork自身に一意な「正解」があることは別ではないかと問い返した。

PER-005は、

- 「原像を知っているのは誰だ」
- 「手掛かりが二つの記憶の間にあるなら、戻る先は最初から一つなのか」

という問いを追記した。

このeventでPER-006が初めて独立ペルソナとして成立した。

研究側ではこの問いからQ-004 / H-004 / EXP-004が派生したが、その結果をPER-005 / PER-006へ逆流させない。

#### EVT-003 — 公平な手掛かりは中立ではない

Story time: `T0-1980S + protocol sketch after EVT-002`

PER-005 / PER-006は、A/Bで異なるunitの半分ずつを使い、A/Bへ同じbit差数を持つcueを作る手順を共同メモへ記録した。

同時に、bit差数が等しいこととdynamics上でA/Bが等価であることを同一視せず、距離、final state、update条件、A/B以外へ停止したstateを別々に記録する方針を成立させた。

#### EVT-004 — 同じ手掛かりから二つの戻り先

Story time: `T0-1980S + first paper calculation after EVT-003`

6 unit・3 stored patternsの紙上networkで、同一cue・weights・非同期更新規則から、更新順だけを変えてA/Bへ別々にstable到達する例を観測した。

PER-005:

- 「手掛かりが同じでも、戻り先は一つとは限らない」
- 「想起の結果だけを見て原像を逆算してよいのか」

現代側EXP-004の統計値は二人へ共有していない。

Resolution provenance: `UNBLINDED`。数理例・物語eventとして保持するが、clean resolver validationには使わない。

#### EVT-005 — 更新順の選び方を先に固定する

Story time: `T0-1980S + next joint paper check after EVT-004`

EVT-004と同じnetwork / cueについて、自然順序 `(1,2,3,4,5,6)` の全6 cyclic rotationsを結果前に固定した。

Action-lock commit:

`59ff6530d202b79834afbe8ffdceee1256437315`

全6本を同じruleで解決した結果:

```text
r1 -> A
r2 -> D
r3 -> B
r4 -> B
r5 -> D
r6 -> D
```

DはA/B/Cのどれとも一致しないnonstored stable state。

PER-005:

- 「二つの原像のどちらへ戻るか、では足りない」
- 「戻り先そのものが、原像の一覧の外にもある」

Resolution provenance: `LOCKED`。

#### EVT-006 — 全balanced cueを先に固定する

Story time: `T0-1980S + systematic cue check after EVT-005`

EVT-005でupdate-order selectionを固定した後、initial cue自体のselection freedomを減らすため、A/Bが異なる4 unitから作れるA/B等距離cue全6種類を結果前に固定した。

Action-lock commit:

`97ee4b3d322d367468258775443d6f2aa3551ef1`

各cueへEVT-005と同じ6 cyclic ordersをすべて適用し、36 trialを全て記録した。

結果:

- A exact: 11
- B exact: 11
- C exact: 2
- nonstored stable D: 12
- nonconverged: 0

q16はA/B/CすべてへHamming distance 2で、2 ordersからCへ到達した。

q24はA/Bへdistance 2ずつだが、initial cue自体がDだった。

PER-005:

- 「AとBの間、と書いた時点で、ほかの戻り先を消していたのかもしれない」
- 「手掛かりは二つの原像だけでは定義できない」

Resolution provenance: `LOCKED`。

このeventから現実研究側ではQ-005 / H-005 / EXP-005が派生した。EXP-005はN=100/P=5の200 balanced cuesで第三stored patternとのHamming同距離/近距離を検証し、全200 cueがPAIR_ISOLATEDだったためFAIL。これは現代研究側の結果であり、PER-005 / PER-006のKnowledgeへは入れない。

### 現代

- `T0-MODERN`を現代側の開始同期点候補とする。具体年月日は未確定。
- `BOOT-001`により、現代の世界状態とPER-001〜004の初期状態を同じ背景から同期する。
- 大規模モデルの学習・評価過程で、過去の研究者に似た特徴を持つ挙動が作品内で観測されることはCanonに含まれるが、`T0-MODERN`ですでに観測済みとはしない。
- checkpoint比較やpost-trainingによる変化は長期的な同一性問題へ接続しうるが、未来eventとして初期状態へ書き込まない。

具体的な現代側 `EVT-xxx` が成立した後は、event IDとstory timeをこの索引から辿れるようにする。

## 現実技術史との接点

### 1982 — Hopfieldのcontent-addressable memory

REF-001で、J. J. Hopfieldが相互結合した単純なユニットの集団ダイナミクスとしてcontent-addressable memoryを記述した。部分的・不完全な状態から記憶全体へ戻るという考え方が、本プロジェクトの第1追試EXP-001とPER-005の研究背景へ接続する。

Hopfieldを「連想記憶を最初に考えた人物」とは扱わない。前史には複数の研究系譜があり、どの先行研究がどう接続するかは `research/pre-hopfield-background.md` で調査する。

また、**第1話をHopfield論文の解説から始めるのではなく、記憶・再構成という古い問いが1980年代に実験可能な形へ近づく導入から入る。**

この項目は現実技術史の索引であり、詳細な科学的主張の正本は `references/bibliography.md`、`research/findings.md`、`experiments/` を参照する。

主人公研究者がHopfield本人またはHopfield論文そのものに直接関与する設定は、現時点ではCanonではない。

## 学習上の技術系列

以下は作品と追試で辿る候補であり、厳密な章順ではない。

1. Perceptron
2. 多層ネットワークとXOR
3. 連想記憶 / Hopfield network
4. Backpropagation
5. RNN / LSTM
6. Attention
7. Transformer
8. 大規模pretraining
9. Instruction tuning / preference training
10. LoRAなどのparameter-efficient tuning
11. MoE / routing
12. tool use / agent
13. 現在のfrontier

### 現在の入口

最初の実研究・追試はHopfield networkから開始したが、物語上はその前史を導入背景として確認してから `T0-1980S` へ入る。

これは学習系列1→13を固定するものではない。物語上必要になった地点から、Perceptron以前を含む前史へ戻り、spiralに理解を補完する。

## フェーズ境界

### CATCH_UP

既知の技術史を、原典確認・追試・理解・物語化によって辿る。

### FRONTIER

現在の技術水準へ追いついた後、現実の新技術と独自の仮説・実験を探索する。

FRONTIERへの移行時点は固定せず、その時点での現実の技術状況を再確認する。
