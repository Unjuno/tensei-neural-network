# EXP-002 Hopfield回復境界の探索

状態: PRE-REGISTERED

## 実験ID

`EXP-002`

## 目的

EXP-001で低負荷・低noiseのcontent-addressable recallを確認した後、保存パターン数とcueのbit反転noiseを増やし、今回の有限grid内でexact recallが大きく低下する領域を観測する。

失敗時の最終状態を「別の保存パターン」「保存されていない収束状態」「未収束」に分け、単なる成功率だけでなく失敗の形も残す。

## 判定対象

今回固定する `P × noise` gridに、高いexact recallを維持するbaselineと、明確に低いexact recallを示すchallenging条件の両方が存在するか。

これはHopfield networkの理論的な臨界容量を推定する判定ではない。

## 関連

- Q-002
- H-002
- REF-001
- EXP-001 / F-001
- Finding: 実行後に必要ならF-002
- Learning: 実行後に必要ならL-002
- 小説章: 未定

## 種別

Extension

## 原典

- REF-001: J. J. Hopfield (1982)

## EXP-001から変える条件

- 保存パターン数を `P = 5, 10, 15, 20` へ拡張
- bit反転noiseを `0.10, 0.20, 0.30, 0.40` へ拡張
- pattern ensembleをseed `1982, 1983, 1984` の3組へ拡張
- failureの最終状態を4分類する

学習則・更新則・N=100はEXP-001と同じ。

## 実行前に固定する条件

### ネットワーク

- ユニット数: `N = 100`
- 保存パターン数: `P ∈ {5, 10, 15, 20}`
- load: `0.05, 0.10, 0.15, 0.20`
- pattern ensemble seed: `1982, 1983, 1984`
- 各seedでは最大20個の独立な±1 patternを1回生成し、P条件ごとに先頭P個を使う。したがって同一seed内ではload条件がnestedになる

### 学習則

`W = (1/N) * Σ_p ξ^p (ξ^p)^T`

- 自己結合 `W_ii = 0`
- 対称重み

### cue

- bit反転noise率: `0.10, 0.20, 0.30, 0.40`
- 各 `seed × P × noise` 条件で20 trials
- target pattern indexは `trial_index` とseed indexから決定論的に割り当てる
- flip位置と更新順にはtrial固有の決定論的seedを使う

### trial数

`3 seeds × 4 P × 4 noise × 20 trials = 960 trials`

結果を見た後でtrial数を増減しない。

### 更新則

- 非同期更新
- 1 sweepで全Nユニットをshuffle順で1回ずつ更新
- `h_i > 0 → +1`, `h_i < 0 → -1`, `h_i = 0 → 現在値維持`
- 1 sweepで状態変化がなければ収束
- 最大 `20 sweeps`

## failure分類

各trialの最終状態を次の順で分類する。

1. `TARGET_EXACT`: target保存パターンと完全一致
2. `WRONG_STORED`: target以外の保存パターンと完全一致
3. `NONSTORED_CONVERGED`: 収束したが、どの保存パターンとも完全一致しない
4. `NONCONVERGED`: 20 sweeps以内に収束しない

`NONSTORED_CONVERGED` をこの実験だけで理論上の「spurious attractor」と断定しない。観測された非保存の安定状態として扱う。

補助値としてtargetへの最終Hamming distanceと、保存パターン集合への最小Hamming distanceも保存する。

## 事前判定基準

### PASS

960 trialsが有効に完了し、次の両方を満たす。

1. baseline `P=5, noise=0.10` の3 seeds集約exact recall率 `>= 0.95`
2. challenging領域 `P>=15, noise>=0.30` の4条件のうち少なくとも1条件で、3 seeds集約exact recall率 `<= 0.50`

PASSは「今回のgrid内で、高回復領域と明確に低い回復領域の両方を観測できた」という意味。

### FAIL

960 trialsが有効に完了したが、上記PASS条件のどちらかを満たさない。

### UNCERTAIN

- 実装バグが疑われる
- 960 trialsが有効に完了しない
- pre-registered grid、seeds、trial割当、更新則から重大に逸脱した
- final-state分類またはraw集計に矛盾がある
- 実行環境上の問題で結果を信頼できない

## H-002への事前解釈

- PASS: H-002を支持する主要証拠。grid形状とseed差を確認して最終状態を判断
- FAIL: 今回のgridではH-002の操作的境界を確認できなかった証拠。結果後に閾値を変更しない
- UNCERTAIN: H-002の支持・不支持には使わない

## 保存する結果

- `results/trials.csv`: 960 trialのraw data
- `results/grid.csv`: seed集約したP×noise各条件の指標
- `results/summary.json`: 判定と主要集計

### gridごとの指標

- exact recall率
- wrong stored率
- nonstored converged率
- nonconverged率
- 平均final Hamming distance to target
- 平均nearest-stored Hamming distance
- seedごとのexact recall率

## 実行環境

- Python 3.11以上
- NumPy 1.26以上、3未満
- CPUのみで実行可能
- 実際のversionを実行後に記録

## 実行後記録

未実行。Q-002 / H-002 / このREADMEを結果を見る前にbranchへ固定した。
