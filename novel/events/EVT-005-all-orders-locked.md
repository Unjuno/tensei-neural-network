# EVT-005 全更新順序を固定して確かめる

状態: `ACTION_LOCKED`

Resolution provenance: `LOCKED`

このファイルは、結果を計算・検索・観測する前に、人物の行動とenvironment resolverの条件を固定する。

## Story time

`T0-1980S + systematic check after EVT-004`

## Timeline position

- Parent: `EVT-004`
- Previous event: `EVT-004`
- Next event: 未成立

## Participants

- PER-005
- PER-006

新しい独立主体は、このactionを行うためには必要ない。

## Observations available before resolution

PER-005 / PER-006が知っているのは物語世界内で成立したEVT-001〜004まで。

特にEVT-004で、同じ6-unit network・同じcueから、二つのupdate orderの一方ではA、他方ではBへstableに到達したことを知っている。

二人は現代側EXP-004の122/200、4000 runs、seed、頻度集計を知らない。

## Persona action

PER-006は、二つのupdate orderだけでは「順序依存がどの程度あるか」は分からず、選んだ二順序が特殊だった可能性を除けないと指摘する。

PER-005は、EVT-004で使った同じ小規模networkを変更せず、まず**可能なupdate orderを全部調べる**ことを選ぶ。

これは新しいpatternを探すことではなく、すでに観測した一つの系についてselection freedomを減らすための確認である。

## Locked network

EVT-004と同一条件を使う。

```text
A = (-1, +1, +1, +1, -1, -1)
B = (+1, -1, +1, -1, -1, +1)
C = (-1, -1, -1, -1, +1, -1)

cue = (+1, -1, +1, +1, -1, -1)
```

結合:

- A/B/CのHebbian outer-product和
- self connection = 0
- 正の定数倍によるnormalizationは符号を変えないので省略可能

unit update:

- asynchronous
- 一つのunitを更新する時点での現在stateを用いる
- local field > 0なら +1
- local field < 0なら -1
- local field = 0なら現在値を保持

## Locked trial set

unit index `1..6` の**全 permutation 720通り**を対象とする。

- 各permutationをちょうど1回trialとして扱う
- permutationの生成順は辞書順
- 都合のよいorderだけを抽出しない
- EVT-004で使ったorder α / βも720通りの一部として含める

各trialは必ず同じ`cue`から開始する。

## Locked stopping rule

各trialでは、そのpermutationを一巡のupdate orderとして繰り返す。

- 1 sweep = permutationに従って6 unitを各1回更新
- sweep終了時にstateがsweep開始時と同一ならstableとして停止
- 最大20 sweeps
- 20 sweepsでstableにならなければ`NONCONVERGED`

## Locked outcome categories

各trialを次のいずれかへ分類する。

- `A_EXACT`
- `B_EXACT`
- `C_EXACT`
- `OTHER_STABLE`
- `NONCONVERGED`

`OTHER_STABLE`の場合はfinal stateも保持する。

## Locked output

最低限、次を集計する。

- total trials = 720であること
- category別件数
- distinct final stable states数
- EVT-004のorder α / βがそれぞれA / Bへ到達することを再確認できるか

## Inclusion / exclusion rule

- 720 trialsをすべて結果へ含める
- 「面白い」結果だけをevent化しない
- 期待と反する結果を削除しない
- outcomeを見てnetwork、cue、update rule、stopping ruleを変更しない

## Resolver boundary

resolverは、このlocked fileとEVT-004の既存network定義を使って計算してよい。

resolverは結果を選ぶために、

- 現代側EXP-004の頻度結果
- 第2話の望ましい展開
- 起承転結上の望ましい位置
- 長期的な輪廻・本人性プロット

を使用しない。

同じsessionがそれらの情報を知っていても、条件選択はこのcommitで既に固定済みなので変更しない。

## Acceptance of any result

次のいずれでも、そのまま物語世界の観測として受理する。

- 720通りすべてAへ行く
- 720通りすべてBへ行く
- A/Bの両方へ分かれる
- A/B以外が多数になる
- 非収束が出る

結果がドラマ上弱くても別条件へ差し替えない。

## Research branch

このACTION_LOCKED段階では新しいQ / H / EXPを作らない。

論点は既存Q-004 / H-004 / EXP-004と重なる。物語内の観測結果が既存研究と異なる新しい検証可能問題を生んだ場合にのみ、解決後に研究分岐を判断する。

## Structure impact

未判定。

結果を見る前に`起 / 承 / 転 / 結`を指定しない。
