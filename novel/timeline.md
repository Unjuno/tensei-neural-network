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

Bootstrapはeventではなく、あるstory timeの状態を同じ背景から再構成できる制作上の同期点です。

現在の同期点:

```text
T0-MODERN
  Bootstrap: BOOT-001
  Parent event head: none
  World: state/world.md
  Personas: PER-001 / PER-002 / PER-003 / PER-004
```

`BOOT-001 @ T0-MODERN @ none` を現代開始時点の同期キーとする。

PER-005は1980年代側に属するため、この同期点へ状態を混ぜない。1980年代sceneを実際に動かす場合は、その時代をtarget story timeにした別Bootstrapを作る。

### Story time と narrative order

物語世界で実際に起きた時刻・因果順と、小説本文で読者へ提示する順番を分離します。

たとえば現代の場面の後に1984年の場面を描写しても、1984年の状態は時系列上の1984年へ属します。章・sceneの提示順、起承転結上の配置は `structure.md` で扱います。

## 物語上の時系列

### 1980年代

- 主人公研究者がニューラルネットワーク、記憶、連想、状態再構成に近い研究へ関わる。
- 具体的な年・所属・研究テーマは未確定。
- この時代を動かすBootstrapは未作成。

### 現代

- `T0-MODERN`を現在の物語開始同期点とする。具体年月日は未確定。
- `BOOT-001`により、現代の世界状態とPER-001〜004の初期状態を同じ背景から同期する。
- 大規模モデルの学習・評価過程で、過去の研究者に似た特徴を持つ挙動が作品内で観測されることはCanonに含まれるが、`T0-MODERN`ですでに観測済みとはしない。
- checkpoint比較やpost-trainingによる変化は長期的な同一性問題へ接続しうるが、未来eventとして初期状態へ書き込まない。

具体的な `EVT-xxx` が成立した後は、event IDとstory timeをこの索引から辿れるようにします。

## 現実技術史との接点

### 1982 — Hopfieldのcontent-addressable memory

REF-001で、J. J. Hopfieldが相互結合した単純なユニットの集団ダイナミクスとしてcontent-addressable memoryを記述した。部分的・不完全な状態から記憶全体へ戻るという考え方が、本プロジェクトの第1追試EXP-001と、人物が後に現象を理解しようとするときの有力な技術的手掛かりになっている。

**第1話の冒頭をHopfieldの説明から始めるとは決めない。** 物語開始はBOOT-001で同期した背景・人物・世界から行い、Hopfieldやその前史は人物が必要とした時点で調査・説明へ入れる。

この項目は現実技術史の索引であり、詳細な科学的主張の正本は `references/bibliography.md`、`research/findings.md`、`experiments/EXP-001-hopfield-associative-memory/` を参照する。

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

最初の実研究・追試はHopfield networkから開始したが、これは小説第1話の冒頭順や、学習系列1→13を固定するものではない。物語上必要になった地点から、Perceptron以前を含む前史へ戻り、spiralに理解を補完する。

## フェーズ境界

### CATCH_UP

既知の技術史を、原典確認・追試・理解・物語化によって辿る。

### FRONTIER

現在の技術水準へ追いついた後、現実の新技術と独自の仮説・実験を探索する。

FRONTIERへの移行時点は固定せず、その時点での現実の技術状況を再確認する。
