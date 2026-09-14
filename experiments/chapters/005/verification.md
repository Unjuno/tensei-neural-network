# 第5話 Mandatory Verification

状態: `PASS`

方式: `EXECUTABLE_REPRODUCTION` と本文対応照合。
対象本文: `novel/chapters/005.md`
採用event: EVT-014 -> EVT-018。

## 対象と理由

第5話の中心主張は、単なる256 trialのaggregateではなく、

1. Q=112 / M1=M2=M3=48
2. split 192 trialがfirst actual flipで48/144へ完全分離
3. initial unstable setがminority memoryとの4-bit difference setと一致
4. cyclic scheduleのQ-return countが4点のcircular gapで再現できる

という因果の連鎖である。

そのためこれらを同一run.pyで再現する。

## 変数表

| 記号 | 意味 | SI単位 | 定義 | 範囲・前提 | 型 |
|---|---|---|---|---|---|
| `M1,M2,M3` | 保存パターン | 1 | EVT-011掲載の固定16成分列 | 各成分±1 | integer vector |
| `Q` | nonstored stable state | 1 | EVT-011掲載の固定列 | 16成分 | integer vector |
| `W_ij` | Hebbian結合 | 1 | 3 patternの外積和、対角0 | symmetric | integer matrix |
| `k` | Qから反転する位置 | 1 | 1〜16の一位置 | integer | scalar |
| `D(k)` | minority stored patternとQの差分位置集合 | 1 | Hamming差分 | split位置では4要素 | set of integers |
| `order` | 非同期更新順 | 1 | 1..16のcyclic rotation | 16本 | integer sequence |
| `h_i` | local input | 1 | `Σ_j W_ij s_j` | exact integer | scalar |
| `g(k)` | circular gap | 1 | D(k)中の直前点からkまでの巡回距離 | 1〜16 | integer |

全量は無次元。物理電圧・時間・周波数には読み替えない。

## 手順

固定M1/M2/M3/Qからweightsを再構成する。

16 one-bit initial states × 16 cyclic ordersを全件実行する。

split 12 statesについてfirst actual flipと総実flip数を記録し、更新前local fieldから`FLIP_IF_UPDATED`集合を求める。

さらに各D(k)のcircular gap `g(k)`を求め、Q-return本数と照合する。

## PASS条件

- aggregateがQ=112, M1=M2=M3=48, OTHER=0
- unanimity 4 positionsは各16/16 Q
- split trialでrepair-first→Qが48/48、other-first→minorityが144/144
- repair branchは総実flip1、minority branchは総実flip3
- 12/12でinitial unstable set = D(k)
- 12/12でQ-return count = circular gap count
- nonconvergence / unexpected final 0
- 保存results.jsonと再実行JSONが全項目一致

## 実行

```bash
python experiments/chapters/005/run.py --check
python tools/run_chapter_experiments.py
```

## 実行結果

8個の個別checksは全てtrue。総合`PASS`。

本文の112/48/48/48、48/144、1 flip / 3 flips、4-unit instability、circular-gap countは保存結果と一致する。

## 次元・誤差確認

整数二値状態と整数結合のみを用いるため丸め誤差はない。

主要誤差源は、実装・転記・event→本文投影・schedule解釈である。保存JSONとの全項目再照合とreview-lockで変更を検出する。

## 限界

- cyclic rotations 16本という人工的schedule familyの結果
- 112/256を自然確率・basin volumeとしない
- 16-neurone掲載例だけ
- 作者側EXP-006以降の一般定理を第5話根拠に使わない
- 数理PASSは文学的完成や実読者理解を保証しない
