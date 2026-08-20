# EXP-003 Hopfield非保存収束状態の3-pattern mixture解析

状態: `PLANNED`

判定: 未実行

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

EXP-002で `NONSTORED_CONVERGED` と分類された最終状態に、Hopfield networkで典型的に検討される単純なodd mixtureのうち、3つのstored patternsのbit-wise majority mixtureと完全一致する状態が含まれるかを確認する。

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
- EVT-001
- 対応研究レポート: `research/reports/EXP-003.md`（実行後作成）

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

重複candidateがある場合、exact match trial数の判定には重複して数えない。どのcombinationに一致したかは別途記録してよい。

## 事前判定基準

### PASS

次をすべて満たす。

1. EXP-002の960 trialsを条件差なく再生成できる
2. `NONSTORED_CONVERGED` が510件再生成される
3. 510件のうち少なくとも1件が、対応条件の3-pattern majority mixture `m` または `-m` とexact matchする

### FAIL

1と2を満たす有効な再生成ができたが、exact mixture matchが0件。

### UNCERTAIN

次のいずれかにより事前基準へ有効に判定できない場合。

- EXP-002とtrial数・分類数が一致しない
- pattern / noise / update / seed生成がEXP-002から逸脱する
- mixture生成またはexact match集計に実装上の疑義がある

## H-003への事前解釈

- PASS: H-003を支持する証拠。ただし少なくとも1件の存在確認に限定する
- FAIL: 今回のEXP-002条件では単純3-pattern majority mixtureのexact matchを確認できなかった証拠
- UNCERTAIN: H-003の支持・不支持へ使わない

## 探索的に記録してよい項目

PASS/FAIL判定には使わないが、次を結果として保存してよい。

- exact match trial数・割合
- `m` と `-m` の内訳
- P / noise / seed別match数
- mixtureまでの最小Hamming distance
- nearest stored patternまでのdistanceとの比較

これらを見て事前PASS基準を変更しない。

## 既知の限界

- EXP-002と同じtrial群の再解析であり独立再現ではない
- 3-pattern majority mixtureだけを扱う
- 5-pattern以上のodd mixtureや他のspurious minimaは判定対象外
- exact matchしないmixture-like stateの解釈は探索的
- N=100、3 pattern seeds、bit-flip noiseに限定
