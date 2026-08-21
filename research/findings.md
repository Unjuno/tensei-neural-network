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

---

## F-004 等距離cueから更新順の違いだけで複数の候補記憶へexact recallする例を確認

状態: PROVISIONAL

### 現在言えること

EXP-004のN=100、P=5、pattern seeds 1982/1983/1984では、二つのstored patterns A/BへHamming distanceが等しいbalanced cueを200件生成した。

各cueについてweightsとinitial stateを固定し、非同期update orderだけを20通り変えたところ、**122 / 200 cues**でAへのexact recallとBへのexact recallの双方が同一cueから観測された。

全4000 runs:

- A_EXACT: 632
- B_EXACT: 630
- OTHER_STORED: 1
- NONSTORED_CONVERGED: 2737
- NONCONVERGED: 0

最初のBIDIRECTIONAL例では、A/B間Hamming distance 54、cueからA/Bはいずれも27だった。同一cueの20 runsでAへ2回、Bへ11回、非保存stateへ7回収束した。

したがって、今回の有限条件では、**cueだけを固定しても、そのcueから一意なstored targetへ必ず決まるわけではなく、非同期更新順の差だけで複数の候補記憶へexact recallする具体例がある**。

### 根拠

- EXP-004 — 事前判定PASS
- `experiments/EXP-004-hopfield-ambiguous-cue/results/summary.json`
- `experiments/EXP-004-hopfield-ambiguous-cue/results/cues.csv`
- `research/reports/EXP-004.md`

### 言えないこと

- Hamming等距離がenergyやbasin境界上でも等距離であること
- 122/200がHopfield network一般の分岐率であること
- synchronous updateや他のN/Pでも同じになること
- 人間の曖昧な記憶・選択・自己同一性が同じ機構であること

### 状態判断

単一実装・有限pattern setのExtensionであり、独立実装による再確認ではないため `PROVISIONAL` とする。

### 関連

- Q-004
- H-004
- EXP-004
- EVT-002

---

## F-005 EXP-004のbalanced cueはHamming距離上pair-isolatedだったが、dynamics上のpair isolationは保証されない

状態: PROVISIONAL

### 現在言えること

EXP-005では、EXP-004のN=100、P=5、pattern seeds 1982/1983/1984で生成した200 balanced cuesをstored set全体へのHamming distanceから再解析した。

selected pair A/Bへの共通距離を `d_pair`、残り3 stored patternsへの最小距離を `d_other_min` とすると、

- `PAIR_ISOLATED` (`d_other_min > d_pair`): **200 / 200**
- `THIRD_TIED`: 0
- `THIRD_CLOSER`: 0

だった。

margin `d_other_min - d_pair` は最小11、最大30だった。

したがって、この有限cue集合では、pairwise balanced cueは**initial Hamming geometry上ではselected A/Bを残りstored patternsから明確に孤立させていた**。

一方、探索的にEXP-004の4000 runsを再確認すると、`OTHER_STORED`が1 run存在した。そのrunでは、

- selected A/Bへのinitial cue距離: 28
- 到達した第三stored patternへのinitial cue距離: 44
- Hamming margin: 16
- 6 sweepsで第三stored patternへexact到達

だった。

したがって今回の有限条件では、**Hamming距離上のpair isolationは、dynamics / basin geometry上でもselected pairだけに孤立していることを保証しない。**

### 根拠

- EXP-005 — 事前判定FAIL
- `experiments/EXP-005-hopfield-pair-isolation/results/summary.json`
- `research/reports/EXP-005.md`
- EXP-004 — 探索的OTHER_STORED runの再確認

### 重要な負の結果

H-005は「200 balanced cuesの少なくとも1件で第三stored patternがA/Bと同距離以下」と予測したが、該当cueは0件だった。

したがって、EVT-006のN=6 toy networkで観測した第三patternとの同距離geometryを、N=100 random-pattern条件へそのまま一般化してはいけない。

このFAILは削除せず、small-N toy exampleとN=100 random setの差として保持する。

### 言えないこと

- Hamming pair-isolated cueが一般に第三stored patternへ到達しやすいこと
- OTHER_STOREDの頻度。今回のEXP-004では1/4000 runのみ
- その1 runの原因が特定のbasin geometryであること
- energy、local field margin、basin volumeのどれが第三pattern到達を説明するか
- 他のN/P/pattern ensembleでも同じになること
- 人間の記憶が同じ機構であること

### 状態判断

EXP-005はEXP-004と同じcode/data系列の決定論的再解析であり独立再現ではない。さらにdynamicalな第三pattern到達は探索的1 runだけなので、`PROVISIONAL` とする。

### 関連

- Q-005
- H-005
- EXP-004
- EXP-005
- EVT-006

## 現在

- F-001: PROVISIONAL — 低負荷での回復
- F-002: PROVISIONAL — 条件悪化による回復崩壊と非保存収束状態
- F-003: PROVISIONAL — 非保存収束状態に3-pattern majority mixture exact matchを1件確認
- F-004: PROVISIONAL — 等距離cueからupdate order差だけで複数候補へのexact recallを確認
- F-005: PROVISIONAL — balanced cueはHamming距離上pair-isolatedでも、dynamics上のpair isolationは保証されない

次の研究候補は、energy/basin非対称性の定量化、別N/P・別実装での再確認、synchronous/asynchronous差など。ただし物語上の必要性または独立した研究価値が生じたものから選ぶ。
