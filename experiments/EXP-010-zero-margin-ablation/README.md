# EXP-010 — nonzero-margin仮定を外す反例探索

状態: `COMPLETED / UNCERTAIN (DESIGN INELIGIBLE)`

事前登録commit: `712856a0b3f44cc5eaac8422b510b612402ed32d`

由来: EXP-007解析証明の仮定アブレーション。

## Q-010

P=3 / symmetric Hebbian / asynchronous one-unit updateは維持し、Qのstabilityを`h_i Q_i > 0`から、zero-field保持規則の下での`h_i Q_i >= 0`へ弱めた場合、split one-bit perturbationのcoordinate-minority escape制約は維持されるか。

## Result

事前登録した最初のN=8で200,000 candidate triplesを固定seed順に生成したが、eligible tripleは**0**だった。

事前停止規則に従い、N=12以降へ都合よく進まず`UNCERTAIN / INSUFFICIENT_ELIGIBLE`で停止した。

## Why the design failed

結果後の解析で、事前登録したNがすべて偶数だったことが重要と分かった。

P=3 majority Qに対し、各stored patternとのoverlap `m_s = ξ^s·Q` はNと同じparityを持つ。

局所marginは

```text
Q_i h_i(Q) = Σ_s (Q_i ξ_i^s) m_s - 3
```

である。

Nが偶数なら各`m_s`は偶数。右辺は「偶数3項の符号付き和 - 3」なので必ず奇数となり、**0にはなれない**。

したがってN=`8,12,16,20,24`だけを選んだEXP-010では、zero-margin exampleを探す設計そのものが不可能だった。

## Interpretation

これは仮説の支持でも棄却でもない。**実験設計のFAIL**である。

この失敗を結果後にNを差し替えて救済しない。奇数Nを使う再検査は新しいEXPとして事前登録する。

副次的な解析結果:

> P=3 majority Qでは、Nが偶数ならlocal margin `Q_i h_i(Q)` は全coordinateで奇数であり、zero marginは構造的に不可能。

このparity observationはEXP-010結果後に得たもので、事前仮説ではない。

実装: `run.py`
保存結果: `results.json`
作者側研究。人物stateへ自動注入しない。
