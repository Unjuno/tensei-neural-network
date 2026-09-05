# 物語構造

このファイルは未来脚本ではなく、**成立済みeventから見た現在の構造・局所的緊張・遷移条件**を管理する索引である。

客観事実は`events/`と`state/`、章本文は`chapters/`、実在史・科学は`research/` / `references/`を正本として確認する。

## 原則

起承転結はeventを発生させる命令ではない。

- 次が`転`だから事件を起こさない
- 章数に技術概念や実験を一対一対応させない
- personaは未来構造を知らない
- event成立後にのみ構造ラベルを付ける
- chapter endingから過去event/stateを逆算しない

## Current event head

`EVT-013`

1980年代active personas:

- PER-005 高橋修一
- PER-006 佐伯玲子

active organization:

- ORG-001 光陵化学生命科学研究所

## 成立済みNarrativeProjection

| 読書単位 | adopted events | 認識遷移 |
|---|---|---|
| 第1話「戻る先」 | EVT-001〜004 | stableであることとcorrect recallを分離し、同じcueから戻り先が一意とは限らないと知る |
| 第2話「選ばなかった答え」 | EVT-005〜008 | selection freedomを減らし、全状態列挙からstored / nonstored二分類の粗さとglobal sign-inversion symmetryを知る |
| 第3話「表の外」 | EVT-009〜011 | current toyのresidualが空であることを受け、当時の一次文献へ戻り、stored / negation外のstable Qを掲載例で再現する |
| 第4話「五と二十一」 | EVT-012〜013 | Qのcomponentwise structureを全件分類し、その構造がHebbian weightsの下でstableになる理由をexactに導出する |

## 現在までの局所構造

### 起 — 「止まる」は「戻る」か

EVT-001〜003で、安定状態・correct recall・cueの公平さを別々の問題として立てた。

### 承 — 選択条件を固定して観測範囲を広げる

EVT-004〜007でupdate order、balanced cue、全64 statesへ検査範囲を広げた。

EVT-004は`UNBLINDED`。EVT-005以降はoutcome-sensitive条件をpre-lockしてselection biasを減らした。

### 転 — `nonstored`という箱が壊れる

EVT-007〜009でD=`-C`、sign-inversion symmetry、current toyのresidual `R=∅`が成立した。

「保存したか否か」だけではmechanismを分類できない状態になった。

### 局所的な結 — 一つのspurious stateを構造から説明する

EVT-010〜013で、

```text
current toyではstored/negation外が残らない
→ 1983一次文献へ戻る
→ 掲載Qをstable / stored-negation外として再現
→ Qは三patternのcomponentwise majority
→ overlap=8/8/8
→ h_i(Q)=8(M1_i+M2_i+M3_i)-3Q_i
→ unanimity 21 / split 5
```

まで一具体例を閉じた。

この`結`は全体物語の解決ではない。次の問題の初期条件になっただけである。

## 現在の次の「起」候補

EVT-013後、人物stateから自然に成立している問題:

> **stableであることと、実際にそこへ到達できることは同じか。**

これはすでに結果が決まったplotではない。

次のworld advancementでaccessibilityを扱う場合、次を結果前に固定する必要がある。

- starting-state set
- update schedule / order set
- stopping rule
- trial count
- randomness / seed rule（使う場合）
- stored / spurious / otherのclassification

## 計算資源に関する遷移条件

EVT-013までは紙上の有限計算・代数で完全追跡できたため、共用計算機を独立SYS/OBJ化していない。

次eventがmulti-trial accessibilityへ進み、紙上追跡が合理的でなくなった場合、初めてORG-001の共用計算資源をresolution scopeへ入れる。

その時点で、

- story timeに実在可能な機種/環境
- 利用形態
- programming language
- 実行可能なtrial規模

のうち因果へ必要なものだけ歴史調査で固定する。

## Interpretation boundary

現時点で言えること:

- current 6-unit toyではstored / negation外stable finalはない
- 1983掲載16-neurone exampleではstored / negation外stable Qがある
- Qはこの例でcomponentwise majority
- QのstabilityはoverlapとHebbian weightsから説明できる

現時点で言えないこと:

- 一般のspurious memoriesが全てcomponentwise majorityである
- Qが人間の偽記憶・夢・人格混合を表す
- 1985年以降のmixture-state理論を人物が知っている
- Qのbasin / accessibilityがどの程度か
- unlearningがこの具体例でどう働くか

## Generation validation

- EVT-004: `UNBLINDED`
- EVT-005〜008: `LOCKED`
- EVT-009: `LOCK_NOT_REQUIRED`
- EVT-010〜013: `LOCKED`

EVT-010以降は文献選択、掲載例再計算、component classification、derivation routeの各段階を結果前に固定している。

生成方式全体を完全に作者知識から隔離したわけではないため、長期的なgeneration validationは引き続き`PARTIAL PASS`として扱う。
