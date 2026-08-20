# EXP-004 Hopfield等距離cueの更新順依存

状態: `PLANNED`

判定: 未実行

## 実験ID

`EXP-004`

## 由来

- Story trigger: `EVT-002`
- Related prior experiments: `EXP-001`, `EXP-002`

PER-006が物語上で、

> 手掛かりだけを見たときに二つの記憶が同じくらいもっともらしかったら、networkはどちらを「正解」だと知る？

と問い返したことから、現実側で検証可能な最小問題へ切り出した。

## 目的

二つのstored patterns A/BからHamming distanceが等しい同一cueを固定したとき、Hebbian Hopfield networkの非同期更新順だけを変えることで、同じcueがAにもBにもexact recallする具体例が存在するかを確認する。

## 判定対象

同じweights・同じinitial cueに対してupdate-order seedだけを変えた20 runsを行う。

一つのcueについて、20 runsの中に

- Aへのexact recallが1回以上
- Bへのexact recallが1回以上

の両方が存在した場合、そのcueを `BIDIRECTIONAL` と分類する。

## 関連

- Q-004
- H-004
- EVT-002
- 対応研究レポート: `research/reports/EXP-004.md`（実行後作成）

## 種別

Extension

## 実行前に固定した条件

### network

- `N = 100`
- `P = 5`
- pattern seeds: `1982, 1983, 1984`
- pattern生成はEXP-002と同じ `{-1,+1}` random pattern生成
- Hebbian outer-product
- `W_ii = 0`

### pair選択

各pattern seedの5 stored patternsから全unordered pair `(A,B)` を列挙する。

A/B間のHamming distance `d(A,B)` が正の偶数であるpairだけを有効pairとする。

奇数distanceではbinary cueをA/Bへ厳密な等距離にできないため、この実験では除外する。

### balanced cue生成

各有効pairについて10個のcueを決定論的seedで生成する。

AとBが異なる`d`個のbitのうち、ちょうど`d/2`個をB側の値、残りをA側の値とする。A/Bが同じbitはその共通値を保持する。

したがって各cueで

`Hamming(cue, A) = Hamming(cue, B) = d/2`

を必須検証する。

### update-order runs

各cueについて20 runs。

- initial cue、weightsは固定
- runごとに非同期更新のshuffle順だけを別seedにする
- 最大20 sweeps
- 1 sweepで変化がなければ収束
- local fieldが0なら現在値を維持

### final分類

各runを次へ分類する。

1. `A_EXACT`
2. `B_EXACT`
3. `OTHER_STORED`
4. `NONSTORED_CONVERGED`
5. `NONCONVERGED`

一つのcueの20 runsに `A_EXACT >= 1` かつ `B_EXACT >= 1` があれば `BIDIRECTIONAL`。

## 事前判定基準

### PASS

- 1件以上の有効balanced cueを生成できる
- 全有効cueで20 update-order runsを完了する
- balanced cueのA/B距離検証に違反がない
- `BIDIRECTIONAL` cueが **1件以上** 観測される

### FAIL

有効balanced cueを1件以上生成し、全runを条件どおり完了したが、`BIDIRECTIONAL` cueが0件。

### UNCERTAIN

次のいずれかの場合。

- 有効pair / cueが1件も生成できない
- balanced距離条件が破れる
- run数、update rule、pattern生成等に重大な逸脱がある
- raw集計とsummaryが一致しない

## H-004への事前解釈

- PASS: H-004を支持する証拠。ただし今回の有限random patternsにおける存在確認に限定
- FAIL: 今回の有限条件では、update orderだけでA/B両方へ分岐する同一cueを確認できなかった証拠
- UNCERTAIN: H-004の支持・不支持へ使わない

## 探索的に記録してよい項目

事前判定には使わないが、次を保存してよい。

- 有効pair数 / cue数 / total runs
- A / B / other / nonstored / nonconvergedの総数
- `BIDIRECTIONAL` cue数・割合
- pair別・seed別の分岐頻度
- 同一cueでのA/B割合

これらを見てPASS基準を変更しない。

## 既知の限界

- Hamming等距離はenergy landscape上の等距離を意味しない
- N=100、P=5、random patternsだけ
- asynchronous shuffled updateだけ
- existence testであり、一般的な頻度推定ではない
- 人間の曖昧な記憶・意思決定と同じ機構だとは言えない
