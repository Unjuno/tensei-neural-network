# EXP-001 Hopfield連想記憶の追試

状態: PRE-REGISTERED

## 実験ID

`EXP-001`

## 目的

Hopfield (1982) が示したcontent-addressable memoryの中核現象について、低負荷の二値Hopfield networkを現代の小規模な数値実装で再現する。

原論文の全図表・全条件の完全再現ではない。原典との差異を明示し、「乱されたcueから保存パターンへ収束する」現象を追試対象とする。

## 判定対象

N=100、P=5の低負荷条件で、Hebbian ruleにより保存した二値パターンが、10%または20%のbitを反転したcueから非同期更新によって元パターンへexact recallされるか。

## 関連

- Q-001
- H-001
- REF-001
- Finding: 実行後に作成する場合はF-001
- 小説章: 未定

## 種別

Replication

## 原典

- REF-001: J. J. Hopfield, “Neural networks and physical systems with emergent collective computational abilities,” PNAS 79(8), 2554–2558 (1982). DOI: 10.1073/pnas.79.8.2554

## 実行前に固定する条件

### データ・入力条件

- ユニット数 `N = 100`
- 保存パターン数 `P = 5`
- 記憶負荷 `P/N = 0.05`
- 各パターンは `{-1, +1}` の100次元ベクトル
- pattern生成seed: `1982`
- noise条件: `0.10`, `0.20`
- noiseはtarget patternのbitを重複なしで指定割合だけ反転する
- 各noise条件で `5 patterns × 20 trials = 100 trials`
- trialごとに独立した決定論的seedを使い、更新回数によって後続trialの乱数列が変わらないようにする

### 学習則

Hebbian outer-productを使う。

`W = (1/N) * Σ_p ξ^p (ξ^p)^T`

自己結合は `W_ii = 0` とする。

### 更新則

- 非同期更新
- 1 sweepにつき全Nユニットをランダム順で1回ずつ更新
- local field `h_i = Σ_j W_ij s_j`
- `h_i > 0` なら `+1`、`h_i < 0` なら `-1`
- `h_i = 0` の場合は現在値を維持
- 1 sweepで状態変化がなければ収束とする

### 最大更新と停止条件

- 最大 `20 sweeps`
- 20 sweepsより前に状態変化がなくなれば停止
- 20 sweepsで停止しないtrialも実験結果として保持し、exact recallしていなければ未回復として数える

### 実行環境

- Python 3.11以上を想定
- NumPy 1.26以上、3未満
- CPUのみで実行可能
- OSや実際に使ったPython / NumPy versionは実行後に記録する

## 必要試行数

各noise条件100 trials、合計200 trials。

この初回追試は統計的な母集団推定を目的とせず、固定pattern set・固定trial seedsに対する再現性のある機構確認を目的とする。したがって追加trialは結果を見て恣意的に増減しない。

## 期待される結果

低負荷条件では、10% noiseのcueの大半、20% noiseでも相当割合が元の保存パターンへ収束すると期待する。

これは原論文の具体的数値をそのまま予測するものではない。

## 事前判定基準

### PASS

実行条件に重大な逸脱がなく、200 trialsが有効に完了し、以下を両方満たす。

1. 10% noise: exact recall率 `>= 0.95`
2. 20% noise: exact recall率 `>= 0.80`

### FAIL

実行条件に重大な逸脱がなく200 trialsが有効に完了したが、上記PASS条件の少なくとも1つを満たさない。

### UNCERTAIN

次のいずれかにより事前基準に対する有効な判断ができない場合。

- 実装バグが疑われる
- 指定trial数が完了しない
- pattern生成・noise生成・更新則が事前条件から逸脱した
- raw outputと集計が整合しない
- 実行環境の問題で結果が信頼できない

## 測定値

noise条件ごとに以下を保存する。

- exact recall数 / trial数
- exact recall率
- 収束trial数 / trial数
- 平均sweep数
- 初期Hamming distance
- 最終Hamming distance

trial単位のraw dataを `results/trials.csv`、集計を `results/summary.json` に保存する。

## H-001への事前解釈

- EXP-001 PASS: H-001を支持する証拠。ただし単一実装・単一pattern setのため、PASSだけでH-001を自動的にSUPPORTEDへしない
- EXP-001 FAIL: H-001を支持しない証拠。実装妥当性確認後に仮説状態を判断する
- EXP-001 UNCERTAIN: H-001の支持・不支持には使わない

## 原条件からの主な差異

- 原論文の全実験条件・図表を完全に再現しない
- 現代的な±1表現と明示的なouter-product実装を用いる
- N=100、P=5、固定seedという本プロジェクト独自の操作条件を使う
- cueの不完全性をbit反転noiseとして操作する
- exact recall率の0.95 / 0.80閾値は本プロジェクトが事前に置く判定基準であり、原論文の閾値ではない

## 実行後記録

未実行。結果を見る前にこのREADME、Q-001、H-001をbranchへ記録した。
