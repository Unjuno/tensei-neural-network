# 第2話 Mandatory Verification

状態: `PASS`

Verification type: `EXECUTABLE_REPRODUCTION`

## Fragile claim

第2話が依存する最も壊れやすい主張は、同一の6-unit / 3-pattern networkについて、EVT-005〜008で成立した結果が相互に整合していることである。

## Procedure

`run.py` で第1話コードをimportせず独立再構成した。

- A/B/CからHebbian weight matrixを再構成
- EVT-005の6 cyclic ordersを生成
- q46について6 runsを再現
- A/B balanced cuesを規則から全6件生成し36 runsを再現
- `{-1,+1}^6` 全64 states × 6 orders = 384 trialsを再現
- fixed points / basin counts / order dependenceを集計
- D=-Cをassert
- 全64 states × 全6 one-unit updatesについて符号反転可換性をassert

## Result

GitHub Actions上の独立再実行で全checkがPASSした。

- EVT-005: `A / D / B / B / D / D`、aggregate A:1 / B:2 / D:3
- EVT-006: 6 balanced cues × 6 orders = 36、aggregate A:11 / B:11 / C:2 / D:12
- EVT-007: 64 states × 6 orders = 384、全trialが2 sweeps以内に収束
- fixed points: `A/B/C/-A/-B/-C`
- basin total: A 62 / B 66 / C 64 / -A 62 / -B 66 / -C 64
- order-invariant initial states: 18
- order-dependent initial states: 46
- D = -C
- EVT-008: one-unit updateについて全64 statesで `U_i(-s) = -U_i(s)`

## Important verification incident

初回の検証コードは、EVT-005/006の暫定ラベル `D` をEVT-007集計にも流用したため、canonical final-set checkだけFAILした。数理結果の不一致ではなく、**同じstate `D=-C` に時点別の二つの名称があることを検証コードが区別していなかった**。

修正後は、EVT-005/006のhistorical labelとして `D` を保持し、EVT-007以降のcanonical classificationでは `-C` を使用する。これは第2話本文の認識転換そのものでもある。

## Evidence

- executable: `run.py`
- saved result: `results.json`
- CI reproduction: Story Workflow Validation run after canonical-label fix

## Verdict boundary

PASSが意味するのは、EVT-005〜008の有限toy networkの数理結果と第2話が依存する数値が再現したことだけである。

Hopfield network一般、生物学的記憶、1980年代の研究文化一般についての真理を保証しない。
