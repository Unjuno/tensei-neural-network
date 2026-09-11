# EXP-007 — split one-bit escapeの反例探索

状態: `COMPLETED / NO COUNTEREXAMPLE IN PREREGISTERED SEARCH`

由来: EXP-006 secondary finding。

事前登録commit: `55cdc474161877efb25aab53d183ca53f4f90d1c`

## Q-007

3-pattern componentwise-majority mixture Qがstored / negation外のnonzero-margin stable stateであるとき、split coordinateを一つ反転した初期状態から非同期更新し、Qへ戻らなかったtrajectoryは必ずそのcoordinateのminority stored patternへ行くのか。

## Locked falsification search

N=`8,12,16,20,24`、各Nで最初の128 eligible triples。

各split one-bit initial stateに、

- cyclic rotations N本
- 固定seedからのrandom permutations 32本

を適用。最初の反例で停止するよう事前登録した。

反例は、Q以外へ行ったtrajectoryがcoordinate-minority stored pattern以外へ到達すること、またはnonconvergence。

## Result

全固定探索範囲を完走し、反例は0。

| N | generated candidates | eligible | trajectories | non-Q trajectories |
|---:|---:|---:|---:|---:|
| 8 | 1568 | 128 | 24,240 | 8,880 |
| 12 | 628 | 128 | 45,144 | 22,088 |
| 16 | 323 | 128 | 68,976 | 24,912 |
| 20 | 270 | 128 | 96,720 | 28,080 |
| 24 | 206 | 128 | 127,624 | 27,720 |
| total | — | 640 | **362,704** | **111,680** |

111,680件のnon-Q trajectoryすべてが、その反転coordinateのminority stored patternへ収束した。

結果: `NO_COUNTEREXAMPLE_IN_SEARCH`。

## Interpretation

EXP-006の17,488件に続き、Nとschedule familyを広げた事前登録反例探索でも同じ規則が破れなかった。

これは一般定理の証明ではない。しかし、単なるN=16掲載例固有の偶然という説明はかなり弱くなった。

次の合理的な作業はtrial数をさらに増やすことではなく、**P=3 majority mixture + Hebbian weights + one-bit split perturbationの代数から、このescape先制約を証明または反証すること**。

作者側finding候補:

`F-007-candidate: no counterexample to coordinate-minority escape in 362,704 preregistered trajectories across N=8..24.`

## Limits

- P=3固定
- stable nonstored majority Qへconditionしている
- schedulesは全順列ではない
- zero-input保持rule
- finite deterministic search
- proofではない
- 1980年代人物へこの結果を自動注入しない

実装: `run.py`
保存結果: `results.json`
