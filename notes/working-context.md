# 作業コンテキスト

更新: 2026-09-06

このファイルは別セッションへ探索状態を引き継ぐ公開可能な作業記憶。正本ではない。矛盾時はevent / state / verificationを優先する。

## 主目的

小説が主役。

研究・再現は、小説内で実際に成立した疑問を現実史・数理・実験で検証し、NarrativeProjectionへfeedbackするために使う。

## Branch / workflow

- work branch: `work/story-bootstrap`
- `main`: human-accepted canonicalのみ
- PR未作成
- gate: `IN_PROGRESS -> GATE_CANDIDATE -> strict CI PASS -> PREPUBLICATION_GATE_PASSED`
- Human Review前にCanon/mainへ昇格しない

## Current story state

1980年代側:

- Bootstrap: `BOOT-002 @ T0-1980S @ none`
- event head: `EVT-013`
- active personas: PER-005 高橋修一 / PER-006 佐伯玲子
- active organization: ORG-001 光陵化学生命科学研究所

現代側:

- Bootstrap候補: `BOOT-001 @ T0-MODERN @ none`
- event head: none

## Chapters

- 第1話「戻る先」: EVT-001〜004
- 第2話「選ばなかった答え」: EVT-005〜008 / gate passed
- 第3話「表の外」: EVT-009〜011 / gate passed
- 第4話「五と二十一」: EVT-012〜013 / gate passed

第3話candidate CI run: `33995822802` success。

第4話candidate CI run: `33996369324` success。

## EVT-009〜013

### EVT-009

current 6-unit toyのfixed set:

```text
F={A,B,C,-A,-B,-C}
S={A,B,C}
R=F\(S∪-S)=∅
```

全64 states列挙済みなので、このtoyについてはstored / negation外stable finalが存在しない。

一般のHopfield型networkへの不存在主張ではない。

### EVT-010

文献選択規則をpre-lockし、Hopfield / Feinstein / Palmer (1983), DOI `10.1038/304158a0` を主対象にした。

人物が知った範囲:

- spurious memoriesは1983時点で明示的研究対象
- random initial statesからのaccessibilityを論文が定義
- unlearningはnoise/random startから到達したfinal stateのconnectionを弱く逆更新する

1985年以降のmixture-state理論は未観測。

### EVT-011

1983論文掲載16-neurone / 3-memory exampleをそのままpre-lock再計算。

```text
h(Q)=
(+21,+21,+5,+5,-5,-5,-21,-21,
 +5,-5,-5,+5,+5,-5,-5,+5)
```

16/16 nonzero、16/16 Qと同符号。

QはM1/M2/M3でも、そのglobal negationでもない。

### EVT-012

M1/M2/M3/Qの16位置を全件分類。

- Qはcomponentwise majorityと16/16一致
- unanimity 4
- 2:1 split 12
- minority count M1/M2/M3 = 4/4/4
- Q-Ms distances = 4/4/4
- Ms間distances = 8/8/8

### EVT-013

Hamming/inner-product identityとHebbian ruleだけでQのstabilityを導出。

```text
M1·Q=M2·Q=M3·Q=8
h_i(Q)=8(M1_i+M2_i+M3_i)-3Q_i
```

- unanimity: `21Q_i`
- split: `5Q_i`
- EVT-011 direct local inputsと16/16一致

一具体例のexact explanationであり、一般のspurious-state theoryではない。

## Primary references

- REF-001: Hopfield 1982, DOI `10.1073/pnas.79.8.2554`
- REF-002: Hopfield / Feinstein / Palmer 1983, Nature 304, 158–159, DOI `10.1038/304158a0`, published 1983-07-14

REF-002本文には16-neurone / 3-memory / spurious candidateが具体的に掲載される。

## Current local question

EVT-013後:

> **Qはstableだが、実際の初期状態からQへ到達されるのか。**

次に扱うのはstabilityではなくreachability / accessibility。

## Next world-advancement constraints

accessibilityへ進む場合、結果を見る前に最低限固定する。

- starting-state set
- update order / schedule
- stopping rule
- trial count
- classification rule
- randomness / seed（使用する場合）

注意:

- 1983論文Figure 1は32 neurones / 5 nominal memoriesだが、本文にその5 patternsの具体bit列は掲載されていない
- したがって16-neurone掲載exampleを使うfollow-upをFigure 1のexact reproductionと呼ばない
- 16-neurone Qのlocal accessibilityを調べるならstory-side follow-upとして明記する

## Computing-resource boundary

EVT-013までは紙上で完全追跡可能だったため共用計算機を独立SYS/OBJ化していない。

multi-trial accessibilityで紙上追跡が合理的でなくなった時点で、初めてORG-001の共用計算資源をresolution scopeへ入れる。

その際は実在1980年代日本の研究用計算環境を調べ、因果に必要な範囲だけ機種 / OS / language /利用形態を固定する。

## Known workflow lessons

- Mandatory Verificationは物語の後に選ぶ。verificationのためにeventを発生させない
- `PREPUBLICATION_GATE_PASSED`を本文中の説明文substringで判定しない
- outlineの禁止未来EVTをdependencyと誤認しない
- provisional label Dとcanonical label -Cを同一時点の分類として扱わない
- chapter本文へ「第3話」等の制作側metaを漏らさない

## Unresolved

- exact story date
- ORG-001所在地・具体部門・所長
- 高橋/佐伯の具体職位
- shared computerの具体機種 / OS / language
- EVT-014以降
- modern-side first event

必要になる前に固定しない。
