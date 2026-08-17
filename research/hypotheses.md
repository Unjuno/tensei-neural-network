# 仮説

研究上の問いに対する、反証可能な仮説を管理します。

## 状態

- `PROPOSED`: 提案段階
- `TESTING`: 検証中
- `SUPPORTED`: 現在の証拠が支持している
- `NOT_SUPPORTED`: 現在の証拠では支持されない
- `INCONCLUSIVE`: 証拠が不足・矛盾し、現時点では判定できない

`SUPPORTED` は「真である」と同義ではありません。

## 推奨記録形式

必要に応じて H/T/D/C/U 形式を使います。

- **H (Hypothesis)**: 反証可能な仮説。測定対象・条件・閾値・環境を明示する
- **T (Test)**: 最小の検証。関連する `EXP-...`、データ、環境、必要サンプル数、停止条件、判定基準を明示する
- **D (Decision)**: 関連実験の PASS / FAIL / UNCERTAIN を記録する
- **C (Counter / Alternative)**: 失敗モード、代替仮説
- **U (Uncertainty)**: 誤差要因、不確実性

## 実験判定との関係

実験の `PASS / FAIL / UNCERTAIN` は仮説の真偽ではなく、その実験の事前判定基準に対する判定です。

仮説に実験を紐付けるときは、実行前に「その実験結果を仮説へどう解釈するか」を記録します。この対応を結果を見た後で黙って変更してはいけません。

## 状態遷移

1. 仮説を登録した時点: `PROPOSED`
2. 最初の事前定義済みテストを開始した時点: `TESTING`
3. テスト完了後、まだ予定した検証が残る場合: `TESTING` のまま証拠を追記
4. 現在の有効な証拠が全体として仮説を支持し、未解決の決定的矛盾がない場合: `SUPPORTED`
5. 事前に定めた反証条件を満たす有効な証拠が得られ、実験設計上の重大な欠陥で説明できない場合: `NOT_SUPPORTED`
6. 証拠不足、`UNCERTAIN`、相互に矛盾する有効な結果などで決められない場合: `INCONCLUSIVE`

単一の `PASS` だけを理由に自動で `SUPPORTED` へ変更しません。状態更新時には、どの `EXP-...` / `F-...` を根拠にしたかを記録します。

## H-001 低負荷Hopfield networkでは中程度のbit反転から高率にexact recallできる

状態: SUPPORTED

### H
100ユニットに5個のランダムな二値パターンをHebbian ruleで保存した対称Hopfield networkを非同期更新すると、保存パターンから10%または20%のbitを反転したcueに対して、十分高い割合で元パターンへexact recallする。

この仮説はHopfield (1982) の一般的主張そのものではなく、EXP-001の現代的・簡略化した条件に対する操作的仮説である。

### T
- 実験: EXP-001
- ユニット数: N = 100
- 保存パターン数: P = 5（負荷 P/N = 0.05）
- パターン: seed 1982で生成した独立な±1二値パターン
- 学習: Hebbian outer-product、自己結合なし
- 更新: 非同期、各sweepで更新順をshuffle
- cue: 各保存パターンについて10%または20%のbitを反転
- 試行: 各noise条件につき 5 patterns × 20 trials = 100 trials
- 最大更新: 20 sweeps
- EXP-001のPASS条件: 10% noiseでexact recall率 >= 0.95、かつ20% noiseでexact recall率 >= 0.80

### 実験判定からH-001への事前解釈
- EXP-001 PASS: H-001を支持する証拠として扱う。ただし単一実装・単一pattern setなので自動的に `SUPPORTED` へ確定しない
- EXP-001 FAIL: H-001を支持しない証拠として扱い、実装妥当性を確認したうえで `NOT_SUPPORTED` または追加検証を判断する
- EXP-001 UNCERTAIN: H-001の支持・不支持には使わず、条件修正または再実行を行う

### D
- EXP-001: PASS
  - 10% noise: 100/100 exact recall = 1.00
  - 20% noise: 100/100 exact recall = 1.00
  - 200/200 trialsが収束
  - 最大observed sweeps: 2

### 状態判断
H-001は固定seed・固定pattern set・低負荷という狭い操作条件に対する仮説である。EXP-001は事前登録した全200 trialsを有効に完了し、raw resultと集計の整合も確認され、事前閾値を十分に上回った。未解決の決定的矛盾もないため、この限定条件に対する現在の証拠はH-001を支持していると判断し `SUPPORTED` とする。

### C
- 今回のpattern setが容易だった可能性
- 低負荷だったためspurious attractorの影響が観測されにくかった可能性
- 別pattern ensembleや更新順では結果が変わる可能性

### U
- 1つの固定pattern setのみ
- noiseはbit反転のみ
- 原論文の全条件の再現ではない
- 判定閾値は本プロジェクトの操作的基準

### 関連
- Q-001
- REF-001
- EXP-001
- F-001
- L-001

---

## H-002 負荷とnoiseを増やした探索領域には高回復領域から低回復領域への境界が現れる

状態: TESTING

### H
N=100のHebbian Hopfield networkで保存負荷とbit反転noiseを広げると、EXP-001に近い低負荷・低noise条件では高いexact recallを維持する一方、高負荷かつ高noiseの条件の少なくとも一部ではexact recall率が大きく低下し、今回の探索grid内に回復可能領域と回復困難領域の差が観測される。

この仮説は理論的な臨界容量を推定する主張ではなく、EXP-002で固定する有限gridに対する操作的仮説である。

### T
- 実験: EXP-002
- N: 100
- 保存パターン数 P: 5, 10, 15, 20
- load P/N: 0.05, 0.10, 0.15, 0.20
- noise率: 0.10, 0.20, 0.30, 0.40
- pattern ensemble seeds: 1982, 1983, 1984
- 各 seed × P × noise 条件につき20 trials
- 合計: 3 × 4 × 4 × 20 = 960 trials
- 学習・更新則はEXP-001と同じHebbian outer-product / 自己結合なし / 非同期shuffle更新
- 最大20 sweeps
- failure分類: target exact / wrong stored pattern / converged nonstored state / nonconverged

### EXP-002の事前判定基準
PASSは次の両方を満たすこと。

1. baseline `P=5, noise=0.10` の3 seeds集約exact recall率が `>= 0.95`
2. challenging領域 `P>=15, noise>=0.30` の4条件のうち少なくとも1条件で、3 seeds集約exact recall率が `<= 0.50`

このPASSは「今回のgrid内で、高回復領域と明確に低い回復領域の両方を観測できた」という実験判定である。

### 実験判定からH-002への事前解釈
- EXP-002 PASS: H-002を支持する主要証拠として扱う。grid全体の形とseed間ばらつきを確認して状態を判断する
- EXP-002 FAIL: 今回のgridではH-002の操作的境界を確認できなかった証拠として扱う。理由を結果後に閾値変更で救済しない
- EXP-002 UNCERTAIN: 実装、trial数、分類、raw集計等の問題で有効判定できないためH-002の支持・不支持に使わない

### D
- EXP-002: 実行前

### C
- Pとnoiseの効果が単純な単調減少にならず、pattern ensembleごとの相関で局所的な逆転が起きる可能性
- 高負荷では保存パターン自体が安定状態でなくなる可能性
- nonstoredな収束先を「spurious attractor」と呼ぶには追加解析が必要であり、EXP-002では観測分類として扱う

### U
- N=100固定でサイズ依存性は見ない
- seedsは3つのみ
- bit反転noiseのみ
- exact recallは厳しい指標であり、near recallの連続的な品質は補助値として別に見る
- gridの境界は理論的臨界値ではなく、この実装・条件での観測範囲

### 関連
- Q-002
- REF-001
- EXP-002
- F-001

## 現在

- H-001: 宣言条件の範囲で `SUPPORTED`
- H-002: `TESTING`。EXP-002の事前条件を固定し、結果を見る前に実行する
