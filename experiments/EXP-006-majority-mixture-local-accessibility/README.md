# EXP-006 — 3-pattern majority mixtureの局所到達性

状態: `COMPLETED / SUPPORT WITH IMPORTANT SECONDARY FINDING`

由来: EVT-014 / EVT-015。

事前登録commit: `1ca63fe5779bd0c5474394442c182137d9f23218`

## Q-006

ランダムな3-pattern Hebbian networkで、3-pattern componentwise-majority mixture Qがstored / negation外のstable stateになる例に限定したとき、Qの一ビット近傍からの局所到達性は、三pattern全員一致coordinateと2対1coordinateで系統的に異なるか。

## H-006

対象例の平均で、全員一致coordinateを反転したinitial stateのQ-return fractionは、2対1coordinateを反転した場合より高い。

これはEVT-014の一例を見た後に立てた作者側仮説であり、1980年代人物の事前知識ではない。

## Locked protocol

事前登録commitで以下を固定した。

- N=16, P=3
- independent uniform binary patterns
- componentwise-majority Q
- Qがstored / negation外かつnonzero-margin stableで、unanimous/split coordinateの両方を持つ最初の256 eligible triples
- RNG `random.Random(19830914)`
- 各Qの16 one-bit neighbors
- 各initial stateに16 cyclic update orders
- 1 tripleあたり256 trajectories
- 最大100 sweeps
- primary decision: `median(r_u-r_s)>0` かつ `count(r_u>r_s)>count(r_u<r_s)`

## Result

683 candidate triplesを生成した時点で256 eligible triplesに到達した。

総trajectory数: `256 × 256 = 65,536`。

nonconverged: 0。

### Primary

- mean(`r_u-r_s`) = `0.0012796868`
- median(`r_u-r_s`) = `0.1111111111`
- `r_u > r_s`: 135 triples
- `r_u = r_s`: 8 triples
- `r_u < r_s`: 113 triples

事前判定規則では `SUPPORT`。

ただし**平均差はほぼ0**で、135対113も圧倒的ではない。したがって「unanimous flipは一般に大幅にrobust」という強い解釈は支持しない。

pooled trialでは、

- unanimous: 13,292 / 19,248 = 0.690565
- split: 28,800 / 46,288 = 0.622191

だったが、coordinate数の違うtripleをpoolした値なのでprimary measureより強く扱わない。

## Important secondary finding

Q以外へ収束した23,444 trajectoriesは**すべてstored pattern**だった。stored-negation / other-nonstored finalは0。

さらにsplit-coordinateを反転したtrialでQへ戻らなかった17,488 trajectoriesは、**17,488 / 17,488すべて、そのcoordinateでQと反対側にいたminority stored patternへ収束した**。

これは事前のprimary hypothesisではなくsecondary descriptive outputである。

EVT-015の一例で見えた、

```text
split coordinateをflip
→ minority stored patternだけがQから見た距離4→3
→ majority側二patternは4→5
→ Qへ戻らない場合はminority stored patternへescape
```

という対応が、今回の256 eligible triples / 17,488 split non-Q trajectoriesでは例外なく再現した。

これは強い経験的規則だが、**一般定理とはまだ扱わない**。次に進める価値があるのはprimary H-006よりこちらである。

## Decision

`SUPPORT`, ただしeffectはheterogeneousでprimary mean差はほぼ0。

より重要な新規finding:

`F-006-candidate: split one-bit escape -> coordinate-minority stored pattern (17,488/17,488 in fixed experiment)`

## Limits

- N=16/P=3のみ
- Qがstable nonstored majority mixtureになる条件へselectionしている
- cyclic rotation 16本のみで、16! update permutationsではない
- RNG/sampleは固定された一系列
- 17,488/17,488でも数学的必然性を証明しない
- 自然な確率、人間の記憶、一般のニューラルネットワークへ一般化しない

## Implementation assumptions

- CPython標準ライブラリ
- exact integer arithmetic
- RNG: Python `random.Random`, seed固定
- NumPy / BLAS / GPUなし
- performance benchmarkなし

実装: `run.py`
保存結果: `results.json`
