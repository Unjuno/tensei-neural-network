# 第4話 Mandatory Verification

状態: `PASS`

Verification type: `EXECUTABLE_REPRODUCTION + ALGEBRAIC_CHECK`

## Fragile claims

第4話が依存する最も壊れやすい主張は次。

1. 1983論文掲載QがM1/M2/M3のcomponentwise majorityと16/16位置で一致する。
2. unanimity位置は4、2:1 split位置は12で、splitのminorityはM1/M2/M3が各4回。
3. `d(Q,M1)=d(Q,M2)=d(Q,M3)=4`、stored patterns相互は全て8。
4. bipolar identity `x·y=N-2d_H(x,y)` から `M1·Q=M2·Q=M3·Q=8`。
5. Hebbian connectionと`T_ii=0`から

```text
h_i(Q)=8(M1_i+M2_i+M3_i)-3Q_i
```

を導ける。
6. その式はEVT-011の16 local inputsを完全再現し、unanimity位置で`21Q_i`、2:1位置で`5Q_i`となる。

## Procedure

`run.py`でM1/M2/M3/Qを固定値として独立再計算する。

- 16 component sumsを計算
- componentwise majorityとQを全件比較
- unanimity / 2:1 splitを集計
- splitのminority patternを集計
- 6 Hamming distancesを計算
- Qと各stored patternの内積を直接計算
- Hebbian weightsを再構成しQのlocal inputを直接計算
- `8c_i-3Q_i`による導出値を別計算
- direct / derived / EVT-011 expected vectorを全件比較

実行:

```bash
python experiments/chapters/004/run.py --check
```

## PASS condition

上記6主張を全てexactに再現する。

## Actual result

- majority match: 16 / 16
- unanimity: 4
- split: 12
- minority counts: M1=4, M2=4, M3=4
- Q distances: 4 / 4 / 4
- pair distances: 8 / 8 / 8
- overlaps: 8 / 8 / 8
- direct local inputsとderived local inputs: 16 / 16一致
- minimum signed margin: 5

判定: `PASS`

## Chapter feedback

本文で使った数値・式・因果順はverificationと一致した。

本文中に当初混入した「第3話」という制作側メタ表現2か所は、verification package作成前にworld-internal表現へ修正済み。

## Limitations

このPASSは、

- componentwise-majority formulaが一般のspurious states全てに成り立つことを証明しない
- random-start accessibilityを測らない
- basin sizeを測らない
- unlearning効果を再現しない
- biological memoryのmechanismを証明しない

EVT-012/013と第4話のintegration checkとしてのみ有効。
