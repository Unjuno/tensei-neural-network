# EXP-005 Hopfield pairwise balanced cueのstored-set距離再解析

状態: `PREREGISTERED`

判定: 未実行

## 実験ID

`EXP-005`

## 由来

- Story trigger: `EVT-006`
- Parent experiment: `EXP-004`
- Related: `Q-005`, `H-005`

EVT-006の6-unit toy networkでは、A/Bへ等距離なcueを全列挙したところ、第三stored pattern Cへ到達する例と、cue自体がnonstored fixed point Dである例が観測された。

このsmall-N結果を一般化せず、既存EXP-004のN=100/P=5 balanced cuesについて、**initial cueとstored set全体のHamming距離**だけを独立に再解析する。

## 目的

EXP-004でselected pair A/Bへ厳密にHamming等距離となるよう生成した200 cueについて、残り3 stored patternsの中にA/Bと同距離またはそれより近いpatternが存在するcueが少なくとも1件あるか確認する。

## 判定対象

各balanced cueについて、

- selected Aへの距離 `d_A`
- selected Bへの距離 `d_B`
- `d_pair = d_A = d_B`
- 残り3 stored patternsへの距離
- `d_other_min`

を計算する。

分類:

- `PAIR_ISOLATED`: `d_other_min > d_pair`
- `THIRD_TIED`: `d_other_min == d_pair`
- `THIRD_CLOSER`: `d_other_min < d_pair`

## 関連

- Q-005
- H-005
- EXP-004
- EVT-006
- 対応研究レポート: `research/reports/EXP-005.md`（実行後作成）

## 種別

Extension / deterministic reanalysis

## 実行前に固定する条件

### network / pattern ensemble

EXP-004を変更せず使用する。

- `N = 100`
- `P = 5`
- pattern seeds: `1982, 1983, 1984`
- random bipolar patterns `{-1,+1}`

pattern生成規則はEXP-004 `run.py` と一致させる。

### cue集合

EXP-004の有効pairとbalanced cue生成規則をそのまま再現する。

- 各seedの5 stored patternsから全unordered pairを列挙
- A/B間Hamming distanceが正の偶数のpairのみ有効
- 各有効pairについて10 balanced cues
- A/Bが異なるbitのちょうど半数をB側、残りをA側から取る
- cue生成seed / 順序はEXP-004と一致させる
- 期待件数はEXP-004と同じ `200 cues`

保存済み `results/cues.csv` と再生成結果を照合する。

### 距離計算

各cueについて全5 stored patternsへのHamming distanceを整数で計算する。

selected pair indexを除いた3 patternsの最小値を `d_other_min` とする。

### sample size

固定200 cues。

結果を見てcueを追加・削除しない。

### stopping rule

200 cuesすべての距離計算と分類を完了した時点で終了する。

追加seed、追加N、追加Pへ自動拡張しない。

## 事前判定基準

### PASS

次をすべて満たす。

- EXP-004と同じ200 balanced cuesを有効に復元できる
- 全cueで `d_A == d_B` を確認する
- `THIRD_TIED + THIRD_CLOSER >= 1`

### FAIL

- EXP-004と同じ200 balanced cuesを有効に復元できる
- 全cueで `d_A == d_B`
- 全200 cueが `PAIR_ISOLATED`

### UNCERTAIN

- cue件数が200と一致しない
- stored patterns / selected pair / cueの対応がEXP-004と再現できない
- A/B等距離条件に違反がある
- 保存済みcues.csvと再生成結果に説明できない不一致がある

## H-005への事前解釈

- PASS: H-005を支持する証拠。ただしEXP-004の有限cue集合に限定
- FAIL: H-005を `NOT_SUPPORTED` へ更新する根拠。EVT-006の第三stored pattern geometryが、このEXP-004 random N=100/P=5集合では距離上再現されなかったことを示す
- UNCERTAIN: H-005の支持・不支持へ使わない

## 探索的解析

PASS/FAIL判定には使わないが、実行後に次を保存してよい。

- `d_other_min - d_pair` の最小値・分布
- EXP-004のfinal category (`A_EXACT`, `B_EXACT`, `OTHER_STORED`, `NONSTORED_CONVERGED`)との関係
- `OTHER_STORED` runがある場合、その到達patternとinitial cueの距離

探索結果を事後的にPASS基準へ変更しない。

## 逸脱

実行前: なし。

実行後に条件変更が必要になった場合は、変更理由を明記し、必要なら判定をUNCERTAINとする。
