# EVT-006 全balanced cueを先に固定する

状態: `ACTION_LOCKED`

Resolution provenance: `LOCKED`

## Story time

`T0-1980S + systematic cue check after EVT-005`

## Timeline position

- Parent: `EVT-005`
- Previous event: `EVT-005`
- Next event: 未成立

## Participants

- PER-005
- PER-006

新しい独立主体は、このactionの選択・実行には必要ない。

## World before

- EVT-005で、EVT-004と同じ6-unit network・同じ一つのbalanced cueについて、結果前に固定した6 cyclic update ordersをすべて調べた
- 結果はA / B / nonstored stable Dへ分かれた
- PER-005はDがA/B/Cとどう関係するstateかを問題にしている
- PER-006は条件を変えるなら、変更条件と検査集合を結果前に固定することを要求している
- 現代側EXP-003 / EXP-004の統計結果は二人のKnowledgeではない

## Action selection

PER-006は、EVT-005でorder選択の自由度は減ったが、balanced cue自体はEVT-004で一つだけ選ばれたものだと指摘する。

PER-005は、新しいcueを一つずつ都合よく試すのではなく、A/Bが異なる4 unitから作れる**A/B等距離cueをすべて列挙する**ことを選ぶ。

その全cueに対して、EVT-005と同じ6 cyclic update ordersをすべて適用する。

結果を見てcueやorderを追加・削除しない。

## Locked network

EVT-004 / EVT-005と同じnetworkを使う。

```text
A = (-1, +1, +1, +1, -1, -1)
B = (+1, -1, +1, -1, -1, +1)
C = (-1, -1, -1, -1, +1, -1)
```

Hebbian outer-product和、self connection=0。

unit update:

- asynchronous
- local field > 0 -> +1
- local field < 0 -> -1
- local field = 0 -> current valueを保持

## Locked balanced-cue construction

A/Bが異なるunit indexは、

```text
{1, 2, 4, 6}
```

である。

この4位置のうち、ちょうど2位置ではAの値を取り、残り2位置ではBの値を取る。

A/Bが同じ位置 `3, 5` は共通値をそのまま使う。

したがってbalanced cue集合は、`{1,2,4,6}`からA側に取る2位置を選ぶ全組合せ

```text
C(4,2) = 6
```

を**すべて**使う。

cue IDはA側に取る位置集合を昇順で表す。

```text
q12
q14
q16
q24
q26
q46
```

この6 cueを結果前に全て検査対象として固定する。

EVT-004 / EVT-005で使ったcueは `q46` に対応する。

## Locked update-order set

EVT-005で使用した自然順序 `(1,2,3,4,5,6)` の全6 cyclic rotationsを、各cueへすべて適用する。

```text
r1 = (1,2,3,4,5,6)
r2 = (2,3,4,5,6,1)
r3 = (3,4,5,6,1,2)
r4 = (4,5,6,1,2,3)
r5 = (5,6,1,2,3,4)
r6 = (6,1,2,3,4,5)
```

## Locked trial set

```text
6 balanced cues x 6 cyclic orders = 36 trials
```

36 trialをすべて含める。

各trialは、対応するcueから新しく開始する。

## Locked stopping rule

各trialで:

1. 指定orderを1 sweepとして繰り返す
2. sweep終了時にstateがsweep開始時と同一ならstableとして停止
3. 最大20 sweeps
4. 20 sweepsでstableでなければ`NONCONVERGED`

## Locked outcome categories

- `A_EXACT`
- `B_EXACT`
- `C_EXACT`
- `OTHER_STABLE`
- `NONCONVERGED`

OTHER_STABLEは具体final stateも保持する。

## Locked output

最低限:

- total trials = 36
- cueごとの6 order結果
- category別総件数
- distinct stable final states
- q46の結果がEVT-005のA / D / B / B / D / Dと一致するか

を記録する。

## Inclusion / exclusion rule

- 36 trialを全て含める
- A/Bへ行かなかったtrialも削除しない
- cue単位で結果が平凡でも除外しない
- outcomeを見てcue construction、order集合、stopping ruleを変更しない
- 「面白いcue」を追加探索しない

## Resolver boundary

resolverはこのlocked条件から36 trialをexactに計算する。

条件選択へ使ってはいけないもの:

- 現代側EXP-003 / EXP-004の結果
- 第2話の望ましい展開
- 起承転結上の望ましいラベル
- 長期的な輪廻・本人性プロット
- outcomeを見た後のcue/order選別

## Acceptance of any result

- 全cueが同じfinal stateになっても受理する
- cueごとに異なる結果でも受理する
- OTHER_STABLEが0でも多数でも受理する
- NONCONVERGEDが出ても受理する

結果の面白さを理由に条件を差し替えない。

## Research branch

ACTION_LOCKED時点では新しいQ / H / EXPを作らない。

既存Q-003 / Q-004と異なる新しい検証可能な問題が、解決結果を観測したPER-005 / PER-006から実際に生じた場合だけ後続で判断する。

## Structure impact

未判定。

結果を見る前に起承転結ラベルや話の切れ目を指定しない。
