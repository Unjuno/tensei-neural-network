# EXP-004 Hopfield等距離cueの更新順依存

状態: `COMPLETED`

判定: **PASS**

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
- F-004
- EVT-002
- 対応研究レポート: `research/reports/EXP-004.md`

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

- 有効pair / cueが1件も生成できない
- balanced距離条件が破れる
- run数、update rule、pattern生成等に重大な逸脱がある
- raw集計とsummaryが一致しない

## H-004への事前解釈

- PASS: H-004を支持する証拠。ただし今回の有限random patternsにおける存在確認に限定
- FAIL: 今回の有限条件では、update orderだけでA/B両方へ分岐する同一cueを確認できなかった証拠
- UNCERTAIN: H-004の支持・不支持へ使わない

# 実行後記録

## 実行環境

- Python: `3.13.5`
- NumPy: `2.3.5`
- Platform: `Linux-6.18.35-x86_64-with-glibc2.41`

## 観測結果

- 有効pair: `20`
- balanced cue: `200`
- update-order runs: `4000 / 4000`
- balanced距離違反: `0`
- `BIDIRECTIONAL` cue: `122 / 200 = 0.61`

全run分類:

- `A_EXACT`: 632
- `B_EXACT`: 630
- `OTHER_STORED`: 1
- `NONSTORED_CONVERGED`: 2737
- `NONCONVERGED`: 0

## 最初のBIDIRECTIONAL例

- pattern seed: 1982
- pair: A=0, B=1
- pair Hamming distance: 54
- cue index: 0
- cue→A: 27
- cue→B: 27
- 20 update-order runs:
  - A_EXACT: 2
  - B_EXACT: 11
  - NONSTORED_CONVERGED: 7

同一weights・同一cueで、update-order seedだけを変えた結果としてA/B両方へのexact recallが観測された。

## 判定

**PASS**

事前条件の `BIDIRECTIONAL >= 1` を満たした。

122/200という割合は探索的集計であり、事前PASS条件ではない。この値を見て判定基準は変更していない。

## 保存結果

- `results/summary.json`
- `results/cues.csv`
- `run.py`

`runs.csv` は4000 rowsとなるためcommitせず、`run.py` で決定論的に再生成可能とする。

保存した `cues.csv` の実行時SHA-256:

`3b03e9aa66b50b7371a43e236cb14a339bee383da8711f55e85a097baf59c982`

## 解釈上の注意

Hamming等距離なcueでも、energy landscapeやbasin geometry上でA/Bに等しいとは限らない。

したがって今回確認したのは、

**今回の有限条件では、cueだけから一意なtargetを指定できない具体例があり、非同期更新順の差だけで複数の候補記憶へexact recallし得る**

ということに限定する。

人間の曖昧な記憶や意思決定が同じ機構であるとは言えない。

## 小説との分離

この結果は現実研究側の記録であり、1980年代のPER-005 / PER-006へ自動的に与えない。

物語世界で本人たちが同様の現象を時代内の手段で観測した場合のみ、その観測を別eventとして状態へ反映する。
