# 物語構造

このファイルは未来脚本ではなく、成立済みeventから見た現在の構造・局所的緊張・遷移条件を管理する索引である。客観事実は`events/`と`state/`、章本文は`chapters/`を正本として確認する。

## 原則

- 起承転結をevent発生の原因にしない
- 章数と実験を一対一対応させない
- personaは未来構造を知らない
- event成立後にのみ構造ラベルを付ける
- chapter endingから過去event/stateを逆算しない

## Current event head

`EVT-015`

active: PER-005 高橋修一 / PER-006 佐伯玲子 / ORG-001 光陵化学生命科学研究所。

## 成立済みNarrativeProjection

| 読書単位 | adopted events | 認識遷移 |
|---|---|---|
| 第1話「戻る先」 | EVT-001〜004 | stableとcorrect recallを分離し、同じcueから戻り先が一意とは限らないと知る |
| 第2話「選ばなかった答え」 | EVT-005〜008 | selection freedomを減らし、stored/nonstored二分類の粗さとsign-inversion symmetryを知る |
| 第3話「表の外」 | EVT-009〜011 | toyの残差が空→一次文献へ戻る→stored/negation外stable Qを掲載例で再現 |
| 第4話「五と二十一」 | EVT-012〜013 | Qのmajority structureと5/21 local inputを接続し、stableな理由を説明 |

EVT-014〜015は未投影。ここを第5話にするため追加eventを起こさない。

## EVT-014〜015で成立した新しい局所構造

EVT-013の問い「stableであることと到達可能であることは同じか」から、結果前lockした一ビット近傍検査へ進んだ。

```text
Qはstable
→ Qの16 one-bit neighbors × 16 cyclic ordersを全件
→ Q 112 / M1=M2=M3 48 / nonconverged 0
→ unanimous positionsのflipは全orderでQへ戻る
→ split positionsはorder-dependent
→ escape先はcoordinate-minority stored patternだけ
```

EVT-015ではその初期幾何を追加trialなしで説明した。

```text
split flip
→ minority memory: distance 4→3, overlap 8→10
→ other two: distance 4→5, overlap 8→6

unanimous flip
→ all three: distance 4→5, overlap 8→6
```

これで「Hamming距離1の近傍」は内部的に同質ではないことが人物にとって明確になった。

## 現在の局所的な緊張

高橋は、近さと力学を再び混同せず、order dependenceをこの具体例の代数から説明したい。

佐伯は、EVT-014で結果後に見えた規則を事前仮説へ偽装せず、距離の説明とactual trajectoryを分離したい。

自然な次の問い:

> **少数派stored patternへのescapeは、この具体例で更新途中のどの条件から決まるのか。**

この問いに必要な新trialがなければ、まず解析を優先する。

## 作者側研究との境界

EVT-014/015から作者側EXP-006/007が分岐し、より広い固定探索でcoordinate-minority escapeの反例を探したが見つからなかった。

この作者側結果は人物Knowledgeではない。story eventをEXP-007の結果へ誘導しない。

## 計算資源に関する遷移条件

EVT-014は256反復を含むため、将来これを本文へ投影して実行場面を具体化するなら、1984〜85年のORG-001で利用可能な共用計算機・programming environmentを調査する必要がある。

ただしmachine / OS / languageを雰囲気だけで先にCanon固定しない。因果へ必要になった範囲だけ具体化する。

## Interpretation boundary

現在人物が言える:

- Qはstableで、固定した一ビット近傍の一部から実際に到達される
- その局所到達性はpositionとupdate orderに依存する
- split coordinateをflipするとminority stored patternが距離3まで近づく
- 今回Qへ戻らないtrialはそのminority patternへ行った

まだ言えない:

- 43.75%が自然なbasin probability
- 全state-space basin size
- 一般のP=3 majority mixtureでも同じescape ruleが必ず成立
- 人間の記憶への対応
- 作者側EXP-006/007の結果

## Generation validation

- EVT-004: `UNBLINDED`
- EVT-005〜008: `LOCKED`
- EVT-009: `LOCK_NOT_REQUIRED`
- EVT-010〜014: `LOCKED`
- EVT-015: `LOCK_NOT_REQUIRED`

生成方式全体の作者知識からの独立性は未実証。`PARTIAL PASS`を維持する。
