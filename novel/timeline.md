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

- 1980年代側: `EVT-002`
- 現代側: none

EVT-002時点の1980年代active personas:

- PER-005
- PER-006

### Story time と narrative order

物語世界で実際に起きた時刻・因果順と、小説本文で読者へ提示する順番を分離します。

現時点では、**哲学・技術史を圧縮した導入から1980年代側へ入り、PER-005の研究・思考が動き、PER-006との相互作用へ進む**ことをnarrative entry候補とする。ただし、第1話のscene境界や終了点までは固定しない。

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

PER-005は当時利用可能なcontent-addressable memoryとspurious memoryをめぐる問題設定を比較し、研究ノートに、

- 「止まることと、戻ることは同じか」
- 「保存していないところで止まるなら、その状態は何からできている？」

という問いを残した。

研究側ではこの問いからQ-003 / H-003 / EXP-003が独立に派生したが、その現代的な解析結果をPER-005が知ったことにはしない。

#### EVT-002 — 正しい想起は誰が決める

Story time: `T0-1980S + second research interaction`

PER-005がEVT-001の問題を、実験神経科学・観測基準の側から考えるPER-006へ共有した。

PER-006は、実験者がtargetを知っていることと、曖昧なcueに対してnetwork自身に一意な「正解」があることは別ではないかと問い返した。

PER-005はノートへ、

- 「原像を知っているのは誰だ」
- 「手掛かりが二つの記憶の間にあるなら、戻る先は最初から一つなのか」

という問いを追記した。

このeventでPER-006が初めて独立ペルソナとして成立した。

研究側ではこの問いからQ-004 / H-004 / EXP-004が独立に派生し、等距離cueのupdate-order依存を検証した。ただし、その結果をPER-005 / PER-006が知ったことにはしない。

### 現代

- `T0-MODERN`を現代側の開始同期点候補とする。具体年月日は未確定。
- `BOOT-001`により、現代の世界状態とPER-001〜004の初期状態を同じ背景から同期する。
- 大規模モデルの学習・評価過程で、過去の研究者に似た特徴を持つ挙動が作品内で観測されることはCanonに含まれるが、`T0-MODERN`ですでに観測済みとはしない。
- checkpoint比較やpost-trainingによる変化は長期的な同一性問題へ接続しうるが、未来eventとして初期状態へ書き込まない。

具体的な現代側 `EVT-xxx` が成立した後は、event IDとstory timeをこの索引から辿れるようにします。

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
