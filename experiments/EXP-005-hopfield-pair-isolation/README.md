# EXP-005 Hopfield pairwise balanced cueのstored-set距離再解析

状態: `COMPLETED`

判定: **FAIL**

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
- F-005
- EVT-006
- 対応研究レポート: `research/reports/EXP-005.md`

## 種別

Extension / deterministic reanalysis

## 実行前に固定した条件

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
- 再生成条件に説明できない不一致がある

## H-005への事前解釈

- PASS: H-005を支持する証拠。ただしEXP-004の有限cue集合に限定
- FAIL: H-005を `NOT_SUPPORTED` へ更新する根拠。EVT-006の第三stored pattern geometryが、このEXP-004 random N=100/P=5集合では距離上再現されなかったことを示す
- UNCERTAIN: H-005の支持・不支持へ使わない

## 探索的解析

PASS/FAIL判定には使わないが、実行後に次を保存してよい。

- `d_other_min - d_pair` の最小値・分布
- EXP-004のfinal categoryとの関係
- `OTHER_STORED` runがある場合、その到達patternとinitial cueの距離

探索結果を事後的にPASS基準へ変更しない。

# 実行後記録

## 実行環境

- Python: `3.13.5`
- NumPy: `2.3.5`
- Platform: `Linux-6.18.35-x86_64-with-glibc2.41`

## 観測結果

- 有効pair: `20`
- balanced cue: `200`
- A/B等距離違反: `0`
- `PAIR_ISOLATED`: **200**
- `THIRD_TIED`: **0**
- `THIRD_CLOSER`: **0**

したがって事前PASS条件 `THIRD_TIED + THIRD_CLOSER >= 1` は満たさず、事前FAIL条件「200 cueすべてPAIR_ISOLATED」を満たした。

## 判定

**FAIL**

結果を見てH-005やPASS基準は変更しない。

今回のN=100、P=5、3 seeds、EXP-004で生成した200 cueという有限集合では、EVT-006のN=6 toy networkで観測した「selected pair以外のstored patternも同じHamming距離にいる」というgeometryは再現されなかった。

## 距離margin

`margin = d_other_min - d_pair` とすると、

- 最小margin: `11`
- 最大margin: `30`

最も第三stored patternが近かったcueでも、

- pattern seed: `1984`
- selected pair: `2 / 4`
- pair Hamming distance: `54`
- cue index: `8`
- `d_pair = 27`
- `d_other_min = 38`
- margin: `11`

だった。

したがって、少なくともinitial Hamming geometry上ではselected A/Bが残りstored patternsより明確に近かった。

## 探索的観測

EXP-004の4000 runsを同じ決定論的条件で再生成してfinal分類も確認した。

- `A_EXACT`: 632
- `B_EXACT`: 630
- `OTHER_STORED`: 1
- `NONSTORED_CONVERGED`: 2737
- `NONCONVERGED`: 0

これはEXP-004の既存集計と一致した。

唯一の `OTHER_STORED` runでは、

- pattern seed: `1982`
- selected pair: `0 / 2`
- cue index: `5`
- run index: `12`
- selected pairへのcue距離: `28`
- 到達した第三stored pattern index: `1`
- cueからその第三patternへの距離: `44`
- `d_other_min = 44`
- margin: `16`
- convergence: `6 sweeps`

だった。

つまり、**initial Hamming distance上ではselected pairが第三stored patternより16 bit近いにもかかわらず、非同期dynamicsは第三stored patternへexactに到達したrunが1件存在した。**

これは探索的観測であり、H-005の事前判定をPASSへ変更する根拠には使わない。

## 解釈

今回区別すべきなのは次の二つ。

1. **pair isolation in Hamming geometry**
   - EXP-005の200 cueでは成立した。
2. **pair isolation in dynamics / basin geometry**
   - Hamming isolationだけからは保証できない。EXP-004のOTHER_STORED runが反例候補になる。

したがって、EVT-006のN=6 toy exampleから得た「pairwise記述だけではnetwork全体を隠す」という問題意識自体は有効だが、その具体的理由をN=100 random setへそのまま移してはいけない。

## 保存結果

- `run.py`
- `results/summary.json`
- `results/cue_geometry.csv` — 200 cueすべてのpair距離、第三stored pattern最小距離、margin、分類を保存したrow-level監査データ

`run.py` を再実行すると、同じseed規則から `summary.json` と `cue_geometry.csv` を再生成する。

## 逸脱

事前PASS/FAIL対象について重大な逸脱なし。

保存済みEXP-004 `cues.csv` の全vector自体は保持していないため、同一seed規則で200 cueを再生成した。cue件数・A/B等距離条件・EXP-004探索的run分類が既存集計と一致することを確認した。

## 小説との分離

このFAILと探索的OTHER_STORED結果は現実研究側の知見である。

PER-005 / PER-006の1980年代Knowledgeへ自動的に与えない。本人たちはEVT-006で自分たちが観測した6-unit / 36 trialまでしか知らない。