# EXP-002 Hopfield回復境界の探索

状態: COMPLETED

判定: **PASS**

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
- F-002
- L-002
- 小説章: 未定

## 種別

Extension

## 実行前に固定した条件

### ネットワーク

- `N = 100`
- `P ∈ {5, 10, 15, 20}`
- load: `0.05, 0.10, 0.15, 0.20`
- pattern ensemble seed: `1982, 1983, 1984`
- 同一seed内では最大20 patternを生成して先頭P個を使い、load条件をnestedにする
- Hebbian outer-product
- 自己結合なし、対称重み

### cue / trial

- bit反転noise率: `0.10, 0.20, 0.30, 0.40`
- 各 `seed × P × noise` で20 trials
- 合計 `960 trials`
- target割当、flip位置、更新順は決定論的に再現可能
- 非同期shuffle更新
- 最大 `20 sweeps`

### failure分類

1. `TARGET_EXACT`: target保存パターンと完全一致
2. `WRONG_STORED`: target以外の保存パターンと完全一致
3. `NONSTORED_CONVERGED`: 収束したが、どの保存パターンとも完全一致しない
4. `NONCONVERGED`: 20 sweeps以内に収束しない

`NONSTORED_CONVERGED` をこの実験だけで理論上のspurious attractorと断定しない。

## 事前判定基準

### PASS

960 trialsが有効に完了し、次の両方を満たす。

1. baseline `P=5, noise=0.10` の3 seeds集約exact recall率 `>= 0.95`
2. challenging領域 `P>=15, noise>=0.30` の4条件のうち少なくとも1条件で、3 seeds集約exact recall率 `<= 0.50`

### FAIL

有効な960 trialsを完了したがPASS条件のどちらかを満たさない。

### UNCERTAIN

実装、trial数、grid条件、分類、raw集計などに重大な問題があり、事前基準に対する判断ができない場合。

## H-002への事前解釈

- PASS: H-002を支持する主要証拠。grid形状とseed差を確認して状態を判断
- FAIL: 今回のgridではH-002の操作的境界を確認できなかった証拠
- UNCERTAIN: H-002の支持・不支持に使わない

# 実行後記録

## 実行環境

- Python: `3.13.5`
- NumPy: `2.3.5`
- Platform: `Linux-6.18.35-x86_64-with-glibc2.41`

## 判定

**PASS**

- 有効trial: `960 / 960`
- baseline `P=5, noise=0.10`: exact recall `1.00 >= 0.95`
- challenging:
  - `P=15, noise=0.30`: `0.167`
  - `P=15, noise=0.40`: `0.017`
  - `P=20, noise=0.30`: `0.000`
  - `P=20, noise=0.40`: `0.000`

事前基準の両方を満たした。

## exact recall grid

| P / load | noise 10% | 20% | 30% | 40% |
|---|---:|---:|---:|---:|
| 5 / 0.05 | 1.000 | 1.000 | 0.967 | 0.433 |
| 10 / 0.10 | 0.917 | 0.850 | 0.600 | 0.083 |
| 15 / 0.15 | 0.567 | 0.383 | 0.167 | 0.017 |
| 20 / 0.20 | 0.267 | 0.117 | 0.000 | 0.000 |

今回の有限gridでは、保存負荷とnoiseを増やすにつれてexact recallが大きく低下する領域を明瞭に観測した。

## 失敗の形

全960 trialsの最終分類:

- `TARGET_EXACT`: 442
- `WRONG_STORED`: 8
- `NONSTORED_CONVERGED`: 510
- `NONCONVERGED`: 0

この実装・gridでは、失敗の大半は「別の保存パターンへ完全一致」ではなく、**どの保存パターンとも一致しないが収束した状態**だった。

特に:

- `P=15, noise=0.30`: 50/60が `NONSTORED_CONVERGED`
- `P=15, noise=0.40`: 59/60が `NONSTORED_CONVERGED`
- `P=20, noise=0.30`: 60/60が `NONSTORED_CONVERGED`
- `P=20, noise=0.40`: 60/60が `NONSTORED_CONVERGED`

ただし、これをそのまま理論上のspurious attractorと同定しない。EXP-002では観測分類に留める。

## seed差

低〜中負荷ではseed間ばらつきが見られた。

例:

- `P=10, noise=0.10`: seed別 0.75 / 1.00 / 1.00
- `P=15, noise=0.30`: 0.05 / 0.15 / 0.30
- `P=20, noise=0.30`: 全seed 0.00

したがって、単一pattern ensembleだけで境界位置を固定的に語るべきではない。

## 保存結果

- `results/grid.csv`: 16条件のseed集約値
- `results/summary.json`: 判定・主要集計
- `run.py`: 960 trialのraw CSVを決定論的に再生成するコード

### raw保存に関する実行後の差異

事前計画では `results/trials.csv` を直接commitする予定だったが、現在のGitHub書き込み経路では大きな単一テキストの取り回しが不安定なため、今回はraw CSV本体をcommitせず、**実行時SHA-256と決定論的生成コード**を保存する。

- 実行時 `trials.csv` SHA-256: `b7c7d014a27e2b1675632ec73d2d99e7e6a431d43f28c775ab765c94d700dc26`
- `grid.csv` SHA-256: `ea5363b63651589e33b228ed6a39aeb6fb4ba3262e765ed116fdfb16147cd03b`

これは実験条件・trial数・判定基準の変更ではなく、結果artifactの保存形式上の差異である。rawを再生成した場合は上記hashとの一致を確認する。

## 既知の限界

- N=100固定
- pattern seedsは3つ
- bit反転noiseのみ
- exact recallは厳しい離散指標
- 今回のgridは理論的臨界値の推定ではない
- `NONSTORED_CONVERGED` の内部構造は未解析

## 小説への示唆

EXP-001だけを見ると「乱れた状態から元の記憶へ戻る」印象が強い。しかしEXP-002では、条件が厳しくなると**系は安定していても、意図した原像へ戻っていない**ケースが多数出た。

したがって物語では、

**「一貫して再構成されたこと」と「本物が復元されたこと」は別問題である**

という緊張を強められる。
