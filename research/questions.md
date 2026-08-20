# 研究上の問い

現実世界について、まだ答えが確定していない問いを管理します。

## 状態

- `OPEN`: 調査・検証対象
- `ANSWERED`: 現時点で十分な回答が得られた
- `CLOSED`: 現在は追わない

## Q-001 低負荷Hopfield networkは乱されたcueから保存パターンを回復できるか

状態: ANSWERED

### 問い
Hopfield (1982) の二値相互結合ネットワークを簡略化して実装したとき、低い記憶負荷の条件で、一部のbitを変えた入力から元の保存パターンへ収束するcontent-addressable recallを再現できるか。

### 現時点の回答
EXP-001の宣言条件 N=100、P=5では、noise 10%と20%の双方で100/100 trialsが元パターンへexact recallし、事前判定はPASSとなった。この条件の範囲ではcontent-addressable recallを再現できた。

### 関連
- REF-001
- H-001
- EXP-001
- F-001
- L-001

## Q-002 記憶負荷とcueの乱れを増やすとHopfield recallはどこで崩れるか

状態: ANSWERED

### 問い
N=100の同じ実装で保存パターン数 `P` とnoise率を増やしたとき、exact recall率はどの領域で大きく低下するか。また失敗時の最終状態はどの種類として観測されるか。

### 現時点の回答
EXP-002の3 pattern seeds、960 trialsでは、今回の有限grid内に高回復領域と低回復領域の明確な差を観測した。

- P=5: noise 10/20/30/40%で 1.000 / 1.000 / 0.967 / 0.433
- P=10: 0.917 / 0.850 / 0.600 / 0.083
- P=15: 0.567 / 0.383 / 0.167 / 0.017
- P=20: 0.267 / 0.117 / 0.000 / 0.000

全960 trialsの最終分類は、target exact 442、wrong stored 8、nonstored converged 510、nonconverged 0だった。今回の失敗の大半は、別の保存パターンへの完全一致ではなく、保存パターンと一致しない収束状態だった。

この結果は今回の実装・N=100・3 seeds・noise操作の範囲に限定する。

### 関連
- REF-001
- H-002
- EXP-002
- F-002
- L-002

## Q-003 EXP-002の非保存収束状態に単純な3-pattern mixtureは含まれるか

状態: OPEN

### 由来

`novel/events/EVT-001-stopping-is-not-returning.md` でPER-005が残した、

> 保存していないところで止まるなら、その状態は何からできている？

という物語上の問いから、現実側で検証可能な最小問題として切り出した。

小説の展開をこの問いへ合わせるのではなく、研究側で独立に検証する。

### 問い

EXP-002で `NONSTORED_CONVERGED` と分類された最終状態の中に、同じtrialのstored patternsから3つを選び、各bitで多数決を取った単純な3-pattern majority mixture、またはその全bit反転と完全一致する状態が含まれるか。

ここで3-pattern majority mixtureは、3つの `{-1,+1}` pattern `ξ^a, ξ^b, ξ^c` に対して

`m = sign(ξ^a + ξ^b + ξ^c)`

と定義する。3項和なので0は生じない。

### 現時点の回答

未実行。EXP-003で検証する。

### 関連
- Q-002
- H-003
- EXP-002
- EXP-003
- EVT-001

## 現在

- Q-001: `ANSWERED`
- Q-002: `ANSWERED`
- Q-003: `OPEN` — 非保存収束状態と単純3-pattern mixtureの一致を検証する
