# 第4話 用語検証

状態: `PASS`

第4話本文で実際に使う語だけを対象とする。

## 検証表

| 原概念 | 第4話での表記 | 人物発話での扱い | 状態 | 判断 |
|---|---|---|---|---|
| componentwise majority | 成分多数 / 多数側 | 「位置ごとに二つある方」から説明して使用 | APPLIED | `多数決`をmechanism名にせず、三patternの符号比較という操作的記述に限定 |
| Hamming distance | ハミング距離 / 違う符号の数 | 意味を先に示して使用 | APPLIED | 第1話で検証済みの表記を継承 |
| inner product | 内積 | 数学語として使用可 | APPLIED | 十六個の±1の積和として場面内で意味を説明するため専門語だけに依存しない |
| overlap | 本文では主に内積8として記述 | `overlap`を必須語にしない | APPLIED | event/verification内部ではoverlapを使用可 |
| local input / field | 素子へ入る結合入力の総和 / 入力 | `局所場`を使わない | APPLIED | 第1〜3話方針を継承 |
| Hebbian connection | 三つの記憶パターンから作った結合 | `Hebbian`ラベルを前面に出さない | APPLIED | 操作・式を直接説明する |
| stable state | 安定状態 / 止まる | 使用可 | APPLIED | stabilityとreachabilityを本文末で明示的に分離 |
| reachability / accessibility | 到達可能性 / そこへ戻ってこられるか | 次の問いとしてのみ使用 | APPLIED | 第4話では結果を成立させず、未検証問題として置く |
| mixture state | 使用しない | 使用不可 | APPLIED | 1985年以降の理論を人物へ逆流させない |

## 重要判断

### `多数決`を機構名にしない

Qが16/16位置で三stored patternsのcomponentwise majorityと一致することはEVT-012の観測事実。

しかしnetwork内に投票過程があるわけではないため、本文では佐伯が「誰も投票してません」と修正し、以後`多数側`または`成分多数`とする。

### stabilityとreachabilityを分離する

第4話末の「到達可能性」はEVT-013後に成立した次の研究問いであり、到達可能であるという結果ではない。

## Blocking uncertainty

なし。

新しい時代依存専門語を導入していない。`内積`等は一般数学語で、本文内の操作説明だけでも理解できる構造にしている。
