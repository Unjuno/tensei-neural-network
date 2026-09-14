# EXP-011 — 奇数Nでzero-margin仮定を外す

状態: `COMPLETED / NO COUNTEREXAMPLE IN SEARCH`

事前登録commit: `c81a1de1975c389b061a7a056df4921ad9b1d6d4`

由来: EXP-010のdesign-ineligible結果。偶数NではP=3 majority Qのlocal marginが奇数となりzeroが不可能だったため、奇数Nで改めて検査した。

## Q-011

P=3 / symmetric Hebbian / asynchronous one-unit update / zero-field保持の下で、componentwise-majority Qがstored / negation外かつzero local marginを含むfixed pointであるとき、split one-bit perturbationのcoordinate-minority escape制約は維持されるか。

## Locked hypothesis

nonzero-margin仮定は実質的であり、奇数Nのzero-margin stable Qでは、固定探索範囲内に旧制約の反例が存在する。

## Result

事前登録範囲を完走し、反例は0だった。

| N | generated candidates | eligible | trajectories |
|---:|---:|---:|---:|
| 7 | 1136 | 128 | 23,478 |
| 9 | 805 | 128 | 32,472 |
| 11 | 624 | 128 | 43,946 |
| 13 | 639 | 128 | 55,800 |
| 15 | 685 | 128 | 67,492 |
| 17 | 648 | 128 | 80,850 |
| total | — | 768 | **304,038** |

すべてのtrajectoryがQまたは反転coordinateのminority stored patternへ収束した。

結果: `NO_COUNTEREXAMPLE_IN_SEARCH`。

## Interpretation

事前仮説H-011は支持されなかった。

EXP-010で見つかったparity構造と合わせると、strict positive marginは旧定理に不要である可能性が高い。

実際、`research/reports/EXP-011.md`でEXP-007の解析を見直すと、Q stabilityを

```text
Q_i h_i(Q) >= 0
```

まで弱めても、zero-field保持規則の下で同じescape theoremを証明できる。

したがって、旧EXP-007 reportの`nonzero-margin stable`は**十分条件ではあったが必要条件ではなかった**。

副次的に、P=3 majority QではNが偶数ならlocal marginは奇数なのでzero margin自体が起こらない。zero-margin caseは奇数Nでのみ問題になる。

## Limits

拡張証明でも、

- P=3
- componentwise-majority Q
- Qがstored patternと異なる
- symmetric Hebbian weights / zero self coupling
- asynchronous one-unit update
- zero local fieldでcurrent value保持

は必要。

EXP-008で同期更新、EXP-012でP=5へ外すと反例が既に成立している。

実装: `run.py`
保存結果: `results.json`
作者側研究であり人物へ自動注入しない。
