# EXP-007 — split one-bit escapeの反例探索

状態: `COMPLETED / NO COUNTEREXAMPLE; FOLLOW-UP PROOF FOUND`

由来: EXP-006 secondary finding。

事前登録commit: `55cdc474161877efb25aab53d183ca53f4f90d1c`

## Q-007

3-pattern componentwise-majority mixture Qがstored / negation外のnonzero-margin stable stateであるとき、split coordinateを一つ反転した初期状態から非同期更新し、Qへ戻らなかったtrajectoryは必ずそのcoordinateのminority stored patternへ行くのか。

## Locked falsification search

N=`8,12,16,20,24`、各Nで最初の128 eligible triples。

各split one-bit initial stateにcyclic rotations N本と固定seed random permutations 32本を適用。最初の反例で停止するよう事前登録した。

## Result

| N | generated | eligible | trajectories | non-Q |
|---:|---:|---:|---:|---:|
| 8 | 1568 | 128 | 24,240 | 8,880 |
| 12 | 628 | 128 | 45,144 | 22,088 |
| 16 | 323 | 128 | 68,976 | 24,912 |
| 20 | 270 | 128 | 96,720 | 28,080 |
| 24 | 206 | 128 | 127,624 | 27,720 |
| total | — | 640 | **362,704** | **111,680** |

counterexample: 0。

111,680件のnon-Q trajectoryすべてがcoordinate-minority stored patternへ収束。

実験結果: `NO_COUNTEREXAMPLE_IN_SEARCH`。

## Analytic follow-up

有限探索後、trial数を増やす代わりに構造を解析した。`research/reports/EXP-007.md` に完全な証明を保存。

証明の要点:

1. majority Qをgauge変換して全`+1`にする
2. coordinateは `U=(+++), A=(-++), B=(+-+), C=(++-)` の4typeだけ
3. A-typeを1bit反転したtrajectoryでは、Qのnonzero-margin stabilityからB/C/U typeのlocal fieldが常に正と示せる
4. よって変化できるのはA-typeだけ
5. A-typeに正負が混在するstateはlocal-field条件が6だけずれてfixed pointになれない
6. symmetric Hopfield energyは実flipごとにstrictly減少するためasync trajectoryはfixed pointへ停止
7. finalはQまたはA-type全部が反転したstored pattern Aのみ

従って、**Q以外へ収束するならcoordinate-minority stored patternに限られる**。

このproofにより、EXP-006/007で観測したescape先制約は、記載した仮定内では経験則から解析結果へ昇格した。

## Limits

proofの仮定:

- P=3
- Qはcomponentwise majority
- Qは3 stored patternsのどれとも一致しない
- Qは全unitでnonzero-margin stable
- symmetric Hebbian weights / zero self coupling
- asynchronous one-unit update
- zero local inputでは保持

P>3、別spurious state、同期更新、非対称結合等には適用しない。

作者側結果であり、1980年代人物へ自動注入しない。

実装: `run.py`
保存結果: `results.json`
解析証明: `../../research/reports/EXP-007.md`
