# EXP-003 Hopfield非保存収束状態の3-pattern mixture解析

状態: `COMPLETED`

判定: **PASS**

## 実験ID

`EXP-003`

## 由来

- Parent experiment: `EXP-002`
- Story trigger: `EVT-001`

PER-005が物語上で残した、

> 保存していないところで止まるなら、その状態は何からできている？

という問いから、現実側で検証可能な最小問題として切り出した。

小説の展開をこの実験の結果へ合わせない。実験・結果・解釈は研究側の独立記録として扱う。

## 目的

EXP-002で `NONSTORED_CONVERGED` と分類された最終状態に、単純なodd mixtureのうち、3つのstored patternsのbit-wise majority mixtureと完全一致する状態が含まれるかを確認する。

## 判定対象

EXP-002と同じ決定論的trial群を再生成し、`NONSTORED_CONVERGED` の最終stateを保持する。

各trialについて、その条件で保存されているpatternsから3つを選ぶ全combinationを列挙し、

`m = sign(ξ^a + ξ^b + ξ^c)`

を生成する。3項和なので各bitで0は生じない。

`m` または `-m` と最終stateが完全一致するかを判定する。

## 関連

- Q-003
- H-003
- EXP-002
- F-002
- F-003
- EVT-001
- 対応研究レポート: `research/reports/EXP-003.md`

## 種別

Extension / deterministic re-analysis

## 実行前に固定した条件

### EXP-002再生成条件

- `N = 100`
- `P ∈ {5, 10, 15, 20}`
- noise率: `0.10, 0.20, 0.30, 0.40`
- pattern seeds: `1982, 1983, 1984`
- 各 `seed × P × noise` で20 trials
- 合計960 trials
- Hebbian outer-product、自己結合なし
- 非同期shuffle更新
- 最大20 sweeps
- trial seed生成はEXP-002と同一

### 対象state

EXP-002と同じ分類規則で `NONSTORED_CONVERGED` になったstateのみ。

期待再生成数は `510`。

### mixture生成

各対象trialについて、stored patterns `P` 個から3個を選ぶ全組合せを列挙する。

各組合せ `(a,b,c)` について、

`m_i = +1 if ξ^a_i + ξ^b_i + ξ^c_i > 0 else -1`

とする。

`m` と `-m` の双方をcandidateとする。

## 事前判定基準

### PASS

次をすべて満たす。

1. EXP-002の960 trialsを条件差なく再生成できる
2. `NONSTORED_CONVERGED` が510件再生成される
3. 510件のうち少なくとも1件が、対応条件の3-pattern majority mixture `m` または `-m` とexact matchする

### FAIL

1と2を満たす有効な再生成ができたが、exact mixture matchが0件。

### UNCERTAIN

EXP-002との再生成不一致、またはmixture集計の実装上の疑義により有効判定できない場合。

# 実行後記録

## 再生成確認

- total trials: `960 / 960`
- `TARGET_EXACT`: 442
- `WRONG_STORED`: 8
- `NONSTORED_CONVERGED`: `510 / 510`
- `NONCONVERGED`: 0

EXP-002の分類数と一致した。

## 事前判定対象の結果

3-pattern majority mixture `m` または `-m` とのexact match:

- **1 trial**

一致trial:

- pattern seed: `1983`
- `P = 5`
- noise: `0.40`
- trial index: `2`
- target index: `4`
- trial seed: `3005002`
- convergence: `3 sweeps`
- nearest stored Hamming distance: `21`
- nearest 3-pattern mixture Hamming distance: `0`
- mixture構成pattern index（0-based）: `[1, 2, 4]`
- sign: `+1`

## 判定

**PASS**

事前に固定した3条件をすべて満たした。

このPASSが示すのは、EXP-002の有限trial群の非保存収束状態の中に、単純な3-pattern majority mixtureと完全一致する例が少なくとも1件存在したことだけである。

「非保存収束状態の大半がmixture stateである」とは判定していない。

## 探索的結果

事前PASS条件には使用しない追加集計:

- 510件中363件で、nearest stored patternよりnearest 3-pattern mixtureの方がHamming distanceが小さかった
- 比率: `363 / 510 = 0.7117647059`
- tie: 8件
- nearest 3-pattern mixtureの方が遠い: 139件
- nearest mixture distance: mean `14.2922`, median `15`, min `0`, max `31`
- nearest stored distance: mean `19.3118`, median `21`, min `1`, max `49`

この71.2%という値は結果を見た後の探索的観測であり、H-003の事前判定基準ではない。

## 実行前計画からの逸脱

重大な逸脱なし。

## 保存結果

- `run.py`
- `results/summary.json`

## 既知の限界

- EXP-002と同一trial系列の決定論的再解析であり独立再現ではない
- 3-pattern majority mixtureだけを扱う
- 5-pattern以上のodd mixtureや他種のspurious minimaは判定対象外
- exact matchしないmixture-like stateの解釈は探索的
- N=100、3 pattern seeds、bit-flip noiseに限定

## 小説との境界

この結果をPER-005へ未来知識として直接与えない。

EVT-001はこの実験結果より先に、PER-005自身の時代内の知識・問題意識から成立している。EXP-003はその問いを現実側で独立検証した研究記録である。
