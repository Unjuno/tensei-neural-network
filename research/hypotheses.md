# 仮説

研究上の問いに対する反証可能な仮説を管理します。

## 状態

- `PROPOSED`: 提案段階
- `TESTING`: 検証中
- `SUPPORTED`: 現在の証拠が支持している
- `NOT_SUPPORTED`: 現在の証拠では支持されない
- `INCONCLUSIVE`: 証拠不足・矛盾などで現時点では決められない

`SUPPORTED` は「真である」と同義ではありません。

## H/T/D/C/U

- **H**: 反証可能な仮説。測定対象・条件・閾値・環境を明示する
- **T**: 最小の検証。関連EXP、データ、環境、試行数、停止条件、判定基準を明示する
- **D**: 関連実験のPASS / FAIL / UNCERTAINを個別に記録する
- **C**: 失敗モード、代替仮説
- **U**: 誤差要因、不確実性

実験のPASS / FAIL / UNCERTAINは、その実験で事前に定めた判定対象・判定基準に対する判定であり、仮説そのものの真偽ではありません。EXPからHへの解釈対応も実行前に記録します。

## H-001 低負荷Hopfield networkでは中程度のnoiseから高率にexact recallできる

状態: SUPPORTED

### H
N=100、P=5のHebbian Hopfield networkを非同期更新すると、10%または20%のbitを変えたcueに対して高い割合で元の保存パターンへexact recallする。

### T
- EXP-001
- N=100、P=5
- noise 10% / 20%
- 各100 trials
- PASS条件: 10%でexact recall率 >=0.95、かつ20%で >=0.80

### D
- EXP-001: PASS
- 10%: 100/100 exact recall
- 20%: 100/100 exact recall

### 状態判断
EXP-001の宣言条件を満たした有効な結果があり、raw集計との不整合や決定的な反証がないため、**この狭い操作条件に限定して** `SUPPORTED` とする。Hopfield network一般へは拡張しない。

### C / U
- 固定pattern setが容易だった可能性
- 低負荷のため回復境界を見ていない
- bit操作以外のcueを見ていない
- 原論文の全条件の再現ではない

### 関連
- Q-001
- REF-001
- EXP-001
- F-001
- L-001

---

## H-002 負荷とnoiseを増やした探索領域には高回復領域から低回復領域への差が現れる

状態: SUPPORTED

### H
N=100の同じ実装で保存負荷とnoiseを広げると、低負荷・低noiseでは高いexact recallを維持する一方、高負荷かつ高noiseの条件の少なくとも一部ではexact recall率が大きく低下し、EXP-002の探索grid内に回復しやすい領域と回復困難な領域の差が現れる。

これは理論的な臨界容量を推定する主張ではなく、EXP-002で固定した有限gridに対する操作的仮説である。

### T
- EXP-002
- N=100
- P = 5, 10, 15, 20
- noise = 10%, 20%, 30%, 40%
- pattern seeds = 1982, 1983, 1984
- 各seed × P × noiseで20 trials、合計960
- baseline PASS条件: P=5, noise=10% の集約exact recall率 >=0.95
- challenging PASS条件: P>=15, noise>=30% の4条件の少なくとも1つで集約exact recall率 <=0.50

### D
- EXP-002: PASS
- baseline P=5, noise=10%: 1.000
- challenging:
  - P=15, noise=30%: 0.167
  - P=15, noise=40%: 0.017
  - P=20, noise=30%: 0.000
  - P=20, noise=40%: 0.000

### 状態判断
事前判定のbaselineとchallengingの両条件を満たし、grid全体でも負荷・noise増加に伴う大きな性能低下を観測した。3 seedsの差はあるが、challenging領域で低回復となる傾向は明瞭だったため、**EXP-002の有限gridに限定して** `SUPPORTED` とする。

### C
- pattern ensemble差により局所的な回復率は変わる
- 高負荷では一部の保存パターン自体の安定性が弱い可能性
- 保存パターンと一致しない収束状態の構造は未解析

### U
- N=100固定
- seedsは3つ
- bit操作のみ
- exact recallは離散的で厳しい指標
- gridの観測境界は理論的臨界値ではない

### 関連
- Q-002
- REF-001
- EXP-002
- F-002
- L-002

---

## H-003 EXP-002の非保存収束状態には単純3-pattern mixtureが少なくとも一つ含まれる

状態: TESTING

### H
EXP-002で `NONSTORED_CONVERGED` と分類された最終状態510件のうち、少なくとも1件は、その条件で保存されている3 patternsのbit-wise majority mixture

`m = sign(ξ^a + ξ^b + ξ^c)`

またはその全bit反転 `-m` と完全一致する。

この仮説は「非保存収束状態の大半がmixture stateである」とは主張しない。単純な3-pattern mixtureが実際の失敗先として少なくとも一つ現れるかだけを最小に問う。

### T
- EXP-003
- Parent experiment: EXP-002
- EXP-002と同じ決定論的pattern / trial生成を再実行する
- `NONSTORED_CONVERGED` の最終stateを保持する
- 各trialのstored patternsから全ての3-combinationを列挙する
- 各3-combinationについてbit-wise majority mixture `m` と `-m` を生成する
- 最終stateとのexact matchを数える
- PASS: 有効な `NONSTORED_CONVERGED` 510件が再生成され、そのうちexact mixture matchが1件以上
- FAIL: 510件が有効に再生成されたがexact mixture matchが0件
- UNCERTAIN: EXP-002の再生成条件・分類・trial数が一致せず有効判定できない

### D
未実行。

### C
- 3-pattern majority mixture以外の高次mixture
- stored patternの部分変形や局所minimum
- finite-size effect
- update order依存の安定状態
- mixtureと関係しない別種のspurious state

### U
- EXP-002と同一コード系列からの再解析であり独立再現ではない
- N=100、特定seed群、特定noise操作に限定
- exact matchのみでは「近いが一致しないmixture-like state」を拾わない
- 3-pattern mixtureだけを対象とし、5-pattern以上のodd mixtureは今回の判定対象外

### 由来
- EVT-001 — PER-005の「保存していないところで止まるなら、その状態は何からできている？」

### 関連
- Q-003
- EXP-002
- EXP-003
- F-002
- EVT-001

## 現在

- H-001: `SUPPORTED`（EXP-001の宣言条件に限定）
- H-002: `SUPPORTED`（EXP-002の有限gridに限定）
- H-003: `TESTING` — 単純3-pattern mixtureのexact matchを検証中
