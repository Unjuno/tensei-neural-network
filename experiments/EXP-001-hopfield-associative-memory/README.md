# EXP-001 Hopfield連想記憶の追試

状態: COMPLETED

判定: **PASS**

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
- F-001
- L-001
- 小説章: 未定

## 種別

Replication

## 原典

- REF-001: J. J. Hopfield, “Neural networks and physical systems with emergent collective computational abilities,” PNAS 79(8), 2554–2558 (1982). DOI: 10.1073/pnas.79.8.2554

## 実行前に固定した条件

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

### 実行環境の想定

- Python 3.11以上
- NumPy 1.26以上、3未満
- CPUのみで実行可能

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

# 実行後記録

## 実行環境

- Python: `3.13.5`
- NumPy: `2.3.5`
- Platform: `Linux-6.18.35-x86_64-with-glibc2.41`
- CPU実行

## 観測された結果

| noise | trials | exact recall | exact recall率 | 収束率 | 平均sweeps | 平均最終Hamming distance |
|---|---:|---:|---:|---:|---:|---:|
| 10% | 100 | 100 | 1.00 | 1.00 | 2.0 | 0.0 |
| 20% | 100 | 100 | 1.00 | 1.00 | 2.0 | 0.0 |

200/200 trialsが実行され、全trialが20 sweeps以内に収束した。観測上の最大sweep数は2だった。

## 判定

**PASS**

事前条件の両方を満たした。

- 10% noise: `1.00 >= 0.95`
- 20% noise: `1.00 >= 0.80`

このPASSは「EXP-001の事前判定基準を満たした」という意味であり、Hopfield network一般やH-001が普遍的に真であることを意味しない。

## 実行前計画からの逸脱

重大な逸脱なし。

実行環境のPython / NumPyは事前に想定した範囲内だった。

## raw result検証

`results/trials.csv` を集計と独立に確認した。

- raw rows: 200
- 10% noise: 100 rows、初期Hamming distanceはすべて10、exact recall 100
- 20% noise: 100 rows、初期Hamming distanceはすべて20、exact recall 100
- convergence: 200/200
- 最大observed sweeps: 2

保存ファイル:

- `results/summary.json`
- `results/trials.csv`
- `results/patterns.csv`

実行時のSHA-256:

- summary: `cbb5bd49ab690de054d3af13c2d2e331d9ae812c673122e8128b713241ec2265`
- trials: `8539e9de587ec2597bb2acbe0bf3ab11e545ff5ffeb9b6101d437cb90fdf1cac`
- patterns: `2f86dff96ca675b39d1c3e4a46dda37f073486b7c0b138f11415d8fa014462cb`

注: `summary.json` には検証メタデータを追記してrepositoryへ保存しているため、保存後のファイルhashは上記の実行直後hashと一致しない。上記hashは実行直後のraw artifactsを識別するための記録として残す。

## 既知の限界・不確実性

- 単一の固定pattern setのみ
- pattern loadは0.05と低く、容量限界付近を検証していない
- noiseはbit反転のみで、欠損cueや構造化noiseを試していない
- 原論文の全条件の再現ではない
- 同一コードの別実装による独立再現はまだない
- 今回100%だったことから、事前閾値はこの低負荷条件では容易すぎた可能性がある。結果を受けて閾値を変更せず、次のExtensionで負荷・noiseを広げて境界を測る

## 関連Finding

- F-001

## 小説への示唆

「記憶」を静的な保存場所としてではなく、乱れた現在状態が更新によって特定の安定状態へ戻る**状態遷移・attractor**として描ける。ただし、人間の記憶やLLMの記憶機構そのものがHopfield networkと同一だと主張してはいけない。
