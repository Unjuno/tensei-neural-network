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

状態: SUPPORTED

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
- EXP-003: PASS
- EXP-002の960 trialsを再生成
- NONSTORED_CONVERGED: 510/510再現
- 3-pattern majority mixture exact match: 1件
- 該当: pattern seed 1983, P=5, noise=0.40, trial index=2
- 探索的には363/510件でnearest stored patternよりnearest 3-pattern mixtureの方が近かった

### 状態判断
事前PASS条件である「510件中に少なくとも1件のexact 3-pattern mixture match」を満たしたため、**EXP-002の有限trial群に限定して** `SUPPORTED` とする。

この状態更新は、残り509件をmixture stateと同定するものではない。探索的な363/510という近接結果もH-003の事前判定には使わない。

### C
- 3-pattern majority mixture以外の高次mixture
- stored patternの部分変形や局所minimum
- finite-size effect
- update order依存の安定状態
- mixtureと関係しない別種のspurious state

### U
- EXP-002と同一コード系列からの再解析であり独立再現ではない
- N=100、特定seed群、特定noise操作に限定
- exact matchのみでは「近いが一致しないmixture-like state」を同定できない
- 3-pattern mixtureだけを対象とし、5-pattern以上のodd mixtureは今回の判定対象外

### 由来
- EVT-001 — PER-005の「保存していないところで止まるなら、その状態は何からできている？」

### 関連
- Q-003
- EXP-002
- EXP-003
- F-002
- F-003
- EVT-001

---

## H-004 同一の等距離cueは更新順だけで二つの候補記憶へ分岐し得る

状態: SUPPORTED

### H
N=100、P=5の低負荷Hopfield networkで、二つのstored patterns A/BからHamming distanceが等しい一つのcueを固定し、重みとcueを変えずに非同期更新順だけを変えた複数runを行うと、少なくとも一つのcueについてAへのexact recallとBへのexact recallの両方が観測される。

### T
- EXP-004
- N=100、P=5
- pattern seeds: 1982, 1983, 1984
- 各seedの5 patternsから全pairを候補化
- pair間Hamming distanceが偶数のpairだけを使い、異なるbitの半数をA、残り半数をBから取ることで両者へ等距離なcueを作る
- pairごとに10個のbalanced cueを決定論的に生成する
- 各cueについて20個のupdate-order seedで非同期更新する
- 同一cueでA exactとB exactの双方が1回以上出れば、そのcueを`BIDIRECTIONAL`とする
- PASS: 有効cueのうち`BIDIRECTIONAL`が1件以上
- FAIL: 有効cueを全て実行したが`BIDIRECTIONAL`が0件
- UNCERTAIN: 有効cueを生成できない、または条件・分類・実装に重大な疑義がある

### D
- EXP-004: PASS
- 有効pair: 20
- balanced cue: 200
- update-order runs: 4000 / 4000
- balanced距離違反: 0
- BIDIRECTIONAL cue: 122 / 200
- 最初の例: seed 1982, pair 0/1, cue→A=27, cue→B=27, A_EXACT=2, B_EXACT=11, NONSTORED_CONVERGED=7

### 状態判断
事前PASS条件は`BIDIRECTIONAL >= 1`だった。122件を確認したため、**今回のN=100、P=5、3 pattern seeds、balanced-cue構成に限定して** `SUPPORTED` とする。

122/200という探索的割合を、H-004の一般的な頻度主張へ拡張しない。

### C
- Hamming等距離でもenergy landscapeがA/Bに非対称であり得る
- cueが他のstored patternやspurious stateのbasinへ入る
- asynchronous order以外の更新則では結果が変わり得る

### U
- random pattern、N=100、P=5に限定
- 「等距離」はHamming distance上の定義であり、energyやbasin境界の等距離を意味しない
- existence testであり、一般的頻度を推定しない
- 人間の曖昧な記憶へ直接一般化しない

### 由来
- EVT-002 — PER-006の「二つの記憶が同じくらいもっともらしかったら、networkはどちらを正解だと知る？」

### 関連
- Q-004
- EXP-004
- F-004
- EVT-002

---

## H-005 EXP-004のpairwise balanced cueには第三stored patternがA/Bと同距離以下の例が少なくとも一つある

状態: NOT_SUPPORTED

### H
EXP-004で生成済みの200 balanced cuesのうち少なくとも1件について、selected pair A/Bへの共通Hamming距離を `d_pair`、残り3 stored patternsへの最小Hamming距離を `d_other_min` としたとき、

`d_other_min <= d_pair`

となる。

これは「第三stored patternへ実際に収束する」とは主張しない。pairwise balanced cueの**initial-state geometry**だけを対象にする。

### T
- EXP-005
- Parent experiment: EXP-004
- EXP-004のN=100、P=5、pattern seeds 1982/1983/1984をそのまま使う
- EXP-004で生成した200 balanced cuesを同一条件で再生成する
- 各cueについてselected A/Bへの距離が等しいことを再確認する
- 残り3 stored patternsへのHamming距離を全て計算する
- `PAIR_ISOLATED`: `d_other_min > d_pair`
- `THIRD_TIED`: `d_other_min == d_pair`
- `THIRD_CLOSER`: `d_other_min < d_pair`
- PASS: `THIRD_TIED + THIRD_CLOSER >= 1`
- FAIL: 有効200 cueを再現し、全て`PAIR_ISOLATED`
- UNCERTAIN: EXP-004のcue/pattern/pair対応を再現できない、距離条件違反、件数不一致

### D
- EXP-005: **FAIL**
- 有効pair: 20
- balanced cue: 200
- A/B等距離違反: 0
- `PAIR_ISOLATED`: 200
- `THIRD_TIED`: 0
- `THIRD_CLOSER`: 0
- `d_other_min - d_pair`: min 11, max 30

探索的にEXP-004の4000 runsを再生成すると既存分類と一致し、`OTHER_STORED`が1 run存在した。そのrunではselected pairへのinitial cue距離が28、到達した第三stored patternへの距離が44だった。

この探索結果はH-005の事前判定を変更しない。

### 状態判断
事前FAIL条件である「200 cueすべてPAIR_ISOLATED」を満たしたため、**EXP-004のN=100、P=5、3 seeds、200 balanced cueという有限集合に限定して** `NOT_SUPPORTED` とする。

EVT-006のN=6 toy networkで観測された「第三stored patternがselected A/Bと同距離にいる」というgeometryを、今回のN=100 random setへ一般化する証拠は得られなかった。

一方、探索的OTHER_STORED runは、Hamming距離上のpair isolationとdynamics / basin isolationが別問題である可能性を示す。これはH-005を救済するものではなく、別の仮説候補である。

### C
- high-dimensional random patternsでは第三patternがA/Bと同距離以下になる確率が非常に低い可能性
- EVT-006の第三stored pattern CはN=6というsmall finite-size geometryに依存する可能性
- 第三patternが距離上遠くてもdynamics上はそのbasinへ入る可能性があり、このHだけではbasin geometryを判定できない

### U
- EXP-004と同じdata/code系列の再解析であり独立再現ではない
- Hamming distanceだけを測り、energyやbasin boundaryは測らない
- N=100/P=5/random patterns/3 seedsに限定
- OTHER_STOREDは1 runだけで、dynamicalな第三pattern到達の一般的頻度は分からない

### 由来
- EVT-006 — pairwise balanced cue全列挙で、第三stored pattern Cとnonstored fixed point Dが候補になった観測

### 関連
- Q-005
- EXP-004
- EXP-005
- F-005
- EVT-006

## 現在

- H-001: `SUPPORTED`（EXP-001の宣言条件に限定）
- H-002: `SUPPORTED`（EXP-002の有限gridに限定）
- H-003: `SUPPORTED`（EXP-002の有限trial群でexact 3-pattern mixtureを1件確認）
- H-004: `SUPPORTED`（EXP-004有限条件でupdate-orderのみのA/B分岐を確認）
- H-005: `NOT_SUPPORTED`（EXP-004の200 balanced cuesは全てstored-pattern Hamming距離上PAIR_ISOLATED）
