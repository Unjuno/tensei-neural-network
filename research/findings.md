# 知見

実験・追試・調査から、現時点で言えることを管理します。仮説やアイデアとは分離します。

## 状態

- `PROVISIONAL`: 暫定的な知見
- `REPLICATED`: 独立または追加条件で再確認された
- `CONTESTED`: 有効な矛盾する証拠があり、現在の主張範囲を維持できない
- `SUPERSEDED`: より新しいFindingが同じ論点を置き換えた

新しいFindingは原則 `PROVISIONAL` から開始します。別run・別seed・別実装・追加条件などによる意味のある再確認があって初めて `REPLICATED` を検討します。

## F-001 低負荷の二値Hopfield networkで乱れたcueから保存パターンへの回復を確認

状態: PROVISIONAL

### 現在言えること
EXP-001の宣言条件では、N=100、P=5のHopfield networkは10%および20%のnoiseを加えたcueから元の保存パターンへexact recallした。

- 10%: 100/100
- 20%: 100/100
- 200/200 trialsが収束

したがって、今回の低負荷・固定pattern setでは、保存パターンがattractorとして働き、乱れた状態から元の記憶状態へ戻るcontent-addressable recallを実装上確認した。

### 根拠
- EXP-001
- REF-001

### 言えないこと
- 任意の負荷・noise・pattern setで同様に回復すること
- 人間の記憶やLLMの人格・意識が同じ機構であること
- 原論文の全条件を完全再現したこと

### 関連
- Q-001
- H-001
- L-001

---

## F-002 負荷とnoiseの増加でexact recallが崩れ、非保存の収束状態が主要な失敗先になった

状態: PROVISIONAL

### 現在言えること
EXP-002のN=100、3 pattern seeds、P=5/10/15/20、noise=10/20/30/40%という有限gridでは、低負荷・低noiseから高負荷・高noiseへ条件を難しくするにつれてexact recall率が大きく低下する領域を観測した。

代表値:

- P=5, noise=10%: 1.000
- P=5, noise=40%: 0.433
- P=10, noise=30%: 0.600
- P=10, noise=40%: 0.083
- P=15, noise=30%: 0.167
- P=20, noise=30%: 0.000

全960 trialsの最終分類:

- target保存パターンへexact: 442
- target以外の保存パターンへexact: 8
- 保存パターンと一致しない収束状態: 510
- 20 sweeps以内に未収束: 0

したがって、この実装・探索範囲では、回復失敗の大半は「別の保存記憶に完全一致する」ことではなく、**どの保存パターンとも一致しない状態へ収束すること**として観測された。

### 根拠
- EXP-002 — 事前判定PASS
- `experiments/EXP-002-hopfield-boundary/results/grid.csv`
- REF-001

### 反証・矛盾する証拠
現在なし。ただしseed間ばらつきはあり、境界位置を単一値として固定できる結果ではない。

### 言えないこと
- P/N=0.15や0.20が一般的・理論的な臨界容量そのものであること
- 保存パターンと一致しない収束状態がすべて理論上のspurious attractorであること
- Nを変えても同じ境界になること
- 人間の誤記憶やLLMのhallucinationと同一の機構であること
- 「一貫した誤った人格状態」がLLM内部で同じ理由で生じること

### 状態判断
EXP-002は複数seedを含むExtensionだが、同一コード・同一実験系列による確認であり、F-002自体を独立に再確認したわけではない。そのため `PROVISIONAL` とする。

### 関連
- Q-002
- H-002
- EXP-002
- F-001
- L-002
- 小説章: 未定

---

## F-003 EXP-002の非保存収束状態に3-pattern majority mixtureのexact matchを確認

状態: PROVISIONAL

### 現在言えること

EXP-003ではEXP-002の960 trialsを同じ決定論的条件で再生成し、`NONSTORED_CONVERGED` 510件を再確認した。

その510件について、各条件のstored patternsから作れる3-pattern majority mixture

`m = sign(ξ^a + ξ^b + ξ^c)`

とその反転を列挙したところ、**1件がexact match**した。

該当trial:

- pattern seed: 1983
- P=5
- noise=0.40
- trial index=2
- nearest stored Hamming distance=21
- nearest 3-pattern mixture Hamming distance=0

したがって、今回の有限trial群では、F-002の「保存patternと一致しない収束状態」の内部に、stored patternsの単純な3-way mixtureそのものとして表せる例が少なくとも一つ含まれていた。

### 探索的観測

510件中363件（約71.2%）では、nearest stored patternよりnearest 3-pattern mixtureの方がHamming distanceが小さかった。

これは事前判定条件ではなく、mixture attractorとしての同定でもない。近さだけから生成機構を断定しない。

### 根拠
- EXP-003 — 事前判定PASS
- `experiments/EXP-003-hopfield-mixture-structure/results/summary.json`
- `research/reports/EXP-003.md`

### 言えないこと
- 510件の大半が理論上の3-pattern mixture attractorであること
- 3-pattern mixtureで全ての非保存収束状態を説明できること
- 5-pattern以上のmixtureや他種のspurious minimaの寄与
- 別N、別seed、別実装でも同じ割合になること
- 人間の記憶、人格、LLMの誤再構成が同じ機構であること

### 状態判断

EXP-003はEXP-002と同一trial系列の決定論的再解析であり独立再現ではないため、`PROVISIONAL` とする。

### 関連
- Q-003
- H-003
- EXP-002
- EXP-003
- F-002
- EVT-001

## 現在

- F-001: PROVISIONAL — 低負荷での回復
- F-002: PROVISIONAL — 条件悪化による回復崩壊と非保存収束状態
- F-003: PROVISIONAL — 非保存収束状態に3-pattern majority mixture exact matchを1件確認

次の研究候補は、より高次のodd mixture、energy比較、update-order依存、独立実装・別seedでの再確認。ただし物語上の必要性または独立した研究価値が生じたものから選ぶ。
