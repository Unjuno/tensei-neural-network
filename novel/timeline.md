# 時系列

物語時間とAI技術史の接続を管理します。

## 正本との関係

物語上の客観的事実について、このファイルは `novel/canon.md` の**時系列上の投影・索引**です。`canon.md` と食い違う場合は `canon.md` を正本として優先し、このファイルを修正します。

登場人物が何を知っているか・どう誤認しているかは `novel/characters.md` で管理します。

現実の技術史の事実は必ず `references/` と `research/` の根拠へ戻って確認し、このファイルだけを科学的出典として扱わないでください。

## 物語上の時系列

### 1980年代

- 主人公研究者がニューラルネットワーク、記憶、連想、状態再構成に近い研究へ関わる。
- 具体的な年・所属・研究テーマは未確定。

### 現代

- 大規模モデルの学習・評価過程で、過去の研究者に似た特徴を持つ挙動が観測される。
- その後、checkpoint比較やpost-trainingによる変化が同一性問題へ発展する。

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

## フェーズ境界

### CATCH_UP

既知の技術史を、原典確認・追試・理解・物語化によって辿る。

### FRONTIER

現在の技術水準へ追いついた後、現実の新技術と独自の仮説・実験を探索する。

FRONTIERへの移行時点は固定せず、その時点での現実の技術状況を再確認する。
