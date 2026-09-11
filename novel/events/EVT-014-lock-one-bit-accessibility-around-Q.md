# EVT-014 Qの一ビット近傍からの到達性を調べる

状態: `RESOLVED / PROVISIONAL`

Resolution provenance: `LOCKED`

Action-lock commit: `cc3aac0fb28b31c1df79e7afd0932ebb8e41bcec`

## Story time

`T0-1980S + immediate follow-up after EVT-013`

## Timeline position

- Parent: `EVT-013`
- Previous event: `EVT-013`
- Next event: 未成立

## Resolution scope

- PER-005 高橋修一
- PER-006 佐伯玲子
- EVT-011〜013で共有済みの16素子 / 3記憶 / Q
- ORG-001が許容する共同計算環境

## World before

EVT-013までにQはstableであり、その局所入力が三つの保存パターンとの重なりから説明できた。しかしQそのものを初期状態として置いただけであり、Q以外からQへ到達できるかは未確認だった。

## Locked protocol

結果計算前commit `cc3aac0fb28b31c1df79e7afd0932ebb8e41bcec` で次を固定した。

- model: EVT-011のM1/M2/M3/QとHebbian結合
- initial states: QからHamming距離1にある16状態を全件
- schedules: `1..16` の巡回回転16本を全件
- trials: `16 × 16 = 256`
- asynchronous one-unit update
- `h_i > 0 -> +1`, `h_i < 0 -> -1`, `h_i = 0 -> current value`
- sweep前後が同一なら停止、最大100巡
- 結果後のinitial state / orderの追加削除なし

これは全state-space basin sizeやrandom-start probabilityの推定ではない。

## Resolution

256 trialをexact integer arithmeticで全件計算した。

### Aggregate

| final | trials |
|---|---:|
| Q | 112 |
| M1 | 48 |
| M2 | 48 |
| M3 | 48 |
| other | 0 |
| nonconverged | 0 |

Q到達率はこの固定trial family内で `112 / 256 = 43.75%`。

全trialは2巡以内に停止した。

### By flipped position

Qのk番目だけを反転した初期状態について、16 cyclic ordersのfinalを集計した。

| k | Q | M1 | M2 | M3 |
|---:|---:|---:|---:|---:|
| 1 | 16 | 0 | 0 | 0 |
| 2 | 16 | 0 | 0 | 0 |
| 3 | 13 | 0 | 0 | 3 |
| 4 | 1 | 0 | 0 | 15 |
| 5 | 1 | 0 | 0 | 15 |
| 6 | 1 | 0 | 0 | 15 |
| 7 | 16 | 0 | 0 | 0 |
| 8 | 16 | 0 | 0 | 0 |
| 9 | 10 | 0 | 6 | 0 |
| 10 | 10 | 6 | 0 | 0 |
| 11 | 2 | 0 | 14 | 0 |
| 12 | 1 | 0 | 15 | 0 |
| 13 | 3 | 13 | 0 | 0 |
| 14 | 1 | 15 | 0 | 0 |
| 15 | 3 | 0 | 13 | 0 |
| 16 | 2 | 14 | 0 | 0 |

### Predeclared category

`ORDER_DEPENDENT_LOCAL_ATTRACTION`

理由:

- Qへ到達するtrialとstored patternへ到達するtrialが混在
- nonconvergedなし
- 16 initial states中4状態（k=1,2,7,8）は16/16 orderでQへ戻る
- 残る12状態はorderによりQ到達可否が変わる

## Immediate observation

結果後の分類として、k=1,2,7,8はEVT-012で三つのstored patternsが全員一致していた4位置と一致する。

残る12位置はEVT-012の2対1位置である。さらに、Qへ戻らなかったtrialのfinalは、その反転位置でQと反対側にいた**少数派のstored pattern**だけだった。

例:

- k=3,4,5,6では少数派M3へだけ逃げる
- k=9,11,12,15では少数派M2へだけ逃げる
- k=10,13,14,16では少数派M1へだけ逃げる

M1/M2/M3へのfinalが各48 trialで完全に同数になった。

これはprotocol前に判定条件として置いていなかったため、EVT-014では**post-resolution observation**として記録し、一般則には昇格させない。

## Resolved consequence

- Qはstableなだけでなく、この固定した一ビット近傍の一部から実際に到達される
- しかし局所的な到達性は一様ではない
- EVT-013でlocal marginが21だった全員一致4位置の一ビット反転は、今回の16 cyclic ordersすべてでQへ戻った
- marginが5だった2対1の12位置では、更新順序によってQまたはその位置の少数派stored patternへ分岐した
- stabilityとreachabilityを分ける必要が実際のtrialで確認された
- 43.75%はこの人工的な256 trial familyの比率であり、random-start probabilityではない

## Persona deltas

### PER-005 高橋修一

Beliefs:

- Qの安定性を示す5/21という局所margin差が、近傍からの戻り方の違いとも対応している可能性がある
- 「Qは偽の安定状態」と一語でまとめるより、どの方向から崩すかでstored patternとの競合が露出する

Goals:

- post-hocに見えた「少数派stored patternへ逃げる」対応を、既知のM1/M2/M3/Qの構造から説明できるか調べる
- その説明ができるまでは全state-space basinや頻度へ進まない

### PER-006 佐伯玲子

Beliefs:

- Qへ戻るかどうかは一ビット近傍でも更新順序に依存する
- 256件の比率を自然な確率として読んではならない
- 全員一致位置と2対1位置の差は、EVT-012/013で事前に記録済みの構造と対応している

Goals:

- post-resolution observationと事前仮説を区別して記録する
- 少数派patternへの分岐がこの具体例の代数から必然か、単なる今回のschedule familyの特徴かを分ける

## Organization / world delta

ORG-001のmission / governanceに変更なし。

256 trialは反復的であり、今後本文で実行場面を具体化する場合は共用計算資源・プログラム・出力媒体の実在可能性を別途調査する。今回のeventだけからVAX / UNIX / FORTRAN等をCanon固定しない。

Fact level:

- local story fact: 256 trialの結果と上記分類をPER-005 / PER-006が共有
- institutional fact: 未成立
- public story fact: 未成立
- canon fact: 未昇格

## Research branch after resolution

新しい一般研究EXPはまだ作らない。まずこの掲載例内部で、少数派patternへのescapeと5/21 marginの関係を説明する。

## Generation validation

- initial states / schedules / stopping ruleを結果前commitで固定
- 256件全件を使用
- 結果後に都合のよいscheduleを追加削除していない
- 43.75%をrandom probabilityへ一般化していない
- post-hocに発見したminority-pattern対応を事前仮説として偽装していない
