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

状態: ANSWERED

### 由来

`novel/events/EVT-001-stopping-is-not-returning.md` でPER-005が残した、

> 保存していないところで止まるなら、その状態は何からできている？

という物語上の問いから、現実側で検証可能な最小問題として切り出した。

小説の展開をこの問いへ合わせるのではなく、研究側で独立に検証した。

### 問い

EXP-002で `NONSTORED_CONVERGED` と分類された最終状態の中に、同じtrialのstored patternsから3つを選び、各bitで多数決を取った単純な3-pattern majority mixture、またはその全bit反転と完全一致する状態が含まれるか。

ここで3-pattern majority mixtureは、3つの `{-1,+1}` pattern `ξ^a, ξ^b, ξ^c` に対して

`m = sign(ξ^a + ξ^b + ξ^c)`

と定義する。3項和なので0は生じない。

### 現時点の回答

EXP-003でEXP-002の960 trialsを決定論的に再生成し、`NONSTORED_CONVERGED` 510件を再確認した。

この510件のうち **1件** が、対応条件の3-pattern majority mixtureとexact matchした。

該当条件:

- pattern seed: 1983
- P=5
- noise=0.40
- trial index=2
- mixture pattern index（0-based）=[1, 2, 4]

したがって、今回の有限trial群では「単純な3-pattern mixtureが少なくとも一つ含まれる」に対する答えは **yes**。

ただし510件の大半を3-pattern mixtureと同定したわけではない。探索的には363/510件でnearest stored patternよりnearest 3-pattern mixtureの方が近かったが、これは生成機構の同定ではない。

### 関連
- Q-002
- H-003
- EXP-002
- EXP-003
- F-003
- EVT-001

## Q-004 等距離の曖昧cueは更新順だけで異なる記憶へ解決され得るか

状態: ANSWERED

### 由来

`novel/events/EVT-002-who-defines-correct-recall.md` で、PER-006がPER-005へ、

> 手掛かりだけを見たときに二つの記憶が同じくらいもっともらしかったら、networkはどちらを「正解」だと知る？

と問い返したことから、現実側で検証可能な問題として切り出した。

### 問い

低負荷の二値Hopfield networkで、二つのstored patterns A/BからHamming distanceが等しい同一cueを固定したとき、非同期更新順だけを変える複数runの中で、同じcueがAにもBにもexact recallする例は存在するか。

### 現時点の回答

EXP-004ではN=100、P=5、pattern seeds 1982/1983/1984から、A/Bへ厳密にHamming等距離となるbalanced cueを200件生成し、各cueを20種類の非同期update orderで実行した。

- 有効pair: 20
- balanced cue: 200
- runs: 4000
- 距離条件違反: 0
- 同一cueからA/B両方へexact recallした`BIDIRECTIONAL`: **122 / 200**

したがって今回の有限条件では、答えは **yes**。

ただしHamming等距離はenergy landscape上の等距離を意味せず、122/200を一般的な発生率として扱わない。また人間の曖昧な記憶へ直接一般化しない。

### 関連
- H-004
- EXP-004
- F-004
- EVT-002

## Q-005 pairwise balanced cueは選択したA/Bをstored-pattern距離上で孤立させるか

状態: ANSWERED

### 由来

`novel/events/EVT-006-all-balanced-cues-locked.md` で、PER-005 / PER-006が6-unit toy networkのA/B等距離cue全6種類を固定して調べたところ、

- A/B/Cへ同距離のcueからCへ到達する例
- A/B等距離cueそのものがnonstored fixed pointである例

を観測した。

この小規模例を一般化せず、既存EXP-004のN=100/P=5 balanced cuesで、まず**stored patternsへのHamming距離だけ**を独立に確認した。

### 問い

EXP-004で生成済みの200 balanced cuesについて、selected pair A/Bへの共通距離 `d_pair` と、同じnetwork内の残り3 stored patternsへの最小Hamming距離 `d_other_min` を比較したとき、

`d_other_min <= d_pair`

となるcueは存在するか。

### 現時点の回答

EXP-005でEXP-004と同じ200 balanced cuesを決定論的に再生成し、全5 stored patternsへのHamming distanceを計算した。

結果は、

- `PAIR_ISOLATED`: **200**
- `THIRD_TIED`: **0**
- `THIRD_CLOSER`: **0**
- A/B等距離違反: 0

だった。

したがって今回のN=100、P=5、pattern seeds 1982/1983/1984、EXP-004で生成した200 cueという有限集合では、問いへの答えは **no**。第三stored patternがA/Bと同距離以下になるcueは確認できなかった。

`d_other_min - d_pair` のmarginは最小でも11だった。

ただし探索的にEXP-004の4000 runsを再確認すると、initial cueからselected pairは各28 bit、第三stored patternは44 bit離れていたにもかかわらず、その第三patternへexactに到達したrunが1件あった。

したがって、**Hamming距離上でpairが孤立していることは、dynamics / basin上でもpairだけに孤立していることを保証しない**。これはQ-005のPASS/FAIL判定とは別の探索的観測である。

### 関連
- H-005
- EXP-004
- EXP-005
- F-005
- EVT-006

## 現在

- Q-001: `ANSWERED`
- Q-002: `ANSWERED`
- Q-003: `ANSWERED` — EXP-002の有限trial群で3-pattern mixture exact matchを1件確認
- Q-004: `ANSWERED` — 同一の等距離cueからupdate order差だけでA/B両方へのexact recallを確認
- Q-005: `ANSWERED` — EXP-004の200 balanced cuesは全てstored-pattern Hamming距離上PAIR_ISOLATED。第三stored patternへの同距離/近距離は0件
