# 時系列

物語時間とAI技術史の接続を管理します。

## 正本との関係

物語上の客観的事実について、このファイルは `novel/canon.md` の**時系列上の投影・索引**です。`canon.md` と食い違う場合は `canon.md` を正本として優先し、このファイルを修正します。

人物そのものの定義は `novel/personas/`、人物の時間依存状態は `novel/state/personas/`、世界・環境の定義は `novel/environment.md`、世界の時間依存状態は `novel/state/world.md` で管理します。

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

### Story time と narrative order

物語世界で実際に起きた時刻・因果順と、小説本文で読者へ提示する順番を分離します。

たとえば現代の場面の後に1984年の場面を描写しても、1984年の状態は時系列上の1984年へ属します。章・sceneの提示順、起承転結上の配置は `structure.md` で扱います。

## 物語上の時系列

### 1980年代

- 主人公研究者がニューラルネットワーク、記憶、連想、状態再構成に近い研究へ関わる。
- 具体的な年・所属・研究テーマは未確定。

### 現代

- 大規模モデルの学習・評価過程で、過去の研究者に似た特徴を持つ挙動が観測される。
- その後、checkpoint比較やpost-trainingによる変化が同一性問題へ発展する。

具体的な `EVT-xxx` が成立した後は、上記の粗い時代項目だけでなく、event IDとstory timeをこの索引から辿れるようにします。

## 現実技術史との接点

### 1982 — Hopfieldのcontent-addressable memory

REF-001で、J. J. Hopfieldが相互結合した単純なユニットの集団ダイナミクスとしてcontent-addressable memoryを記述した。部分的・不完全な状態から記憶全体へ戻るという考え方が、本プロジェクトの第1追試EXP-001と第1話設計の技術的な入口になっている。

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

物語上の1980年代設定との接続を優先し、最初の実作業は3のHopfield networkから開始した。これは学習系列1→13を必ず順番に消化するという意味ではない。必要に応じてPerceptron等へ戻り、spiralに理解を補完する。

## フェーズ境界

### CATCH_UP

既知の技術史を、原典確認・追試・理解・物語化によって辿る。

### FRONTIER

現在の技術水準へ追いついた後、現実の新技術と独自の仮説・実験を探索する。

FRONTIERへの移行時点は固定せず、その時点での現実の技術状況を再確認する。
