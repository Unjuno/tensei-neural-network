# EVT-005 全更新順序を固定して確かめる

状態: `RESOLVED / PROVISIONAL`

Resolution provenance: `LOCKED`

Action lock commit: `c910d2fe9d2578e4c796aeb152a9b111aa1edc03`

このeventは、結果を計算・検索・観測する前に人物の行動とenvironment resolverの条件を固定し、そのcommit後に結果を解決した。

## Story time

`T0-1980S + systematic check after EVT-004`

## Timeline position

- Parent: `EVT-004`
- Previous event: `EVT-004`
- Next event: 未成立

## Participants

- PER-005
- PER-006

新しい独立主体は、このactionを行うためには必要なかった。

## Observations available before resolution

PER-005 / PER-006が知っていたのは物語世界内で成立したEVT-001〜004まで。

特にEVT-004で、同じ6-unit network・同じcueから、二つのupdate orderの一方ではA、他方ではBへstableに到達したことを知っていた。

二人は現代側EXP-004の122/200、4000 runs、seed、頻度集計を知らない。

## Persona action

PER-006は、二つのupdate orderだけでは「順序依存がどの程度あるか」は分からず、選んだ二順序が特殊だった可能性を除けないと指摘した。

PER-005は、EVT-004で使った同じ小規模networkを変更せず、まず**可能なupdate orderを全部調べる**ことを選んだ。

これは新しいpatternを探すことではなく、すでに観測した一つの系についてselection freedomを減らすための確認である。

---

# ACTION LOCK

以下は結果解決前にcommit `c910d2fe9d2578e4c796aeb152a9b111aa1edc03` で固定した条件。

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

resolverは、このlocked fileとEVT-004の既存network定義だけから計算する。

結果を選ぶために、

- 現代側EXP-004の頻度結果
- 第2話の望ましい展開
- 起承転結上の望ましい位置
- 長期的な輪廻・本人性プロット

を使用しない。

## Acceptance of any result

次のいずれでも、そのまま物語世界の観測として受理すると事前固定した。

- 720通りすべてAへ行く
- 720通りすべてBへ行く
- A/Bの両方へ分かれる
- A/B以外が多数になる
- 非収束が出る

結果がドラマ上弱くても別条件へ差し替えない。

---

# RESOLUTION

Action lock後、上記720通りを全て解決した。

## Resolved result

```text
TOTAL          720
A_EXACT        270
B_EXACT        270
C_EXACT          0
OTHER_STABLE   180
NONCONVERGED     0
```

割合はこの**一つの6-unit系・一つのcue・全update order集合**に限れば、

- A: 37.5%
- B: 37.5%
- other stable: 25.0%

である。

一般的なHopfield networkやmemory一般の頻度とは扱わない。

全720 trialsが2 sweepsでstability判定に達した。

stable final stateは3種類だった。

```text
A = (-1, +1, +1, +1, -1, -1) : 270 orders
B = (+1, -1, +1, -1, -1, +1) : 270 orders
D = (+1, +1, +1, +1, -1, +1) : 180 orders
```

`D` は保存したA/B/Cのいずれとも一致しない。

Dにおける各unitのlocal fieldは、

```text
(+3, +3, +7, +3, -7, +3)
```

であり、Dの各unitの符号と一致するため、単なるsweep停止判定上の偶然ではなく、このupdate ruleで一つずつunitを更新しても変化しないfixed pointである。

## Locked checks

EVT-004で使用したorderも全720通りの中で再確認した。

```text
order α = 1, 3, 6, 4, 5, 2 -> A
order β = 4, 6, 1, 3, 5, 2 -> B
```

いずれもEVT-004と一致した。

## Resolved consequence

- EVT-004のA/B分岐は、選ばれた2順序だけの計算ミスではなかった
- 同じcue・weights・update ruleでも、全720 orderの中でAとBの双方へ到達する
- さらに、保存されていない第三のfixed point Dへ到達するorderも180通り存在した
- したがって、この具体系では「戻り先はA/Bの二択」とする理解も維持できない
- ただし、これは一つの作為的な6-unit構成を全orderで調べた結果であり、network一般への一般化ではない

## Persona deltas

### PER-005

Beliefs:

- update order依存はEVT-004で偶然選んだ二つの順序だけの現象ではないと、この系の全order確認から判断する
- 同じcueから保存pattern A/Bだけでなく、保存していないfixed pointへも到達することを観測した
- 「正しい原像はどちらか」という問いだけでは不足し、**そもそも戻り先が保存された原像であるとは限らない**ことを再び問題にする必要がある

Goals:

- DがA/B/Cとどう関係するstateなのか記述したい
- この一例だけを一般化せず、どの条件が三つのbasinを分けているか考えたい

Memory:

- 全720 orderを同じ条件で調べ、270/270/180へ分かれた結果を保持する
- Dがstored patternではないfixed pointだったことを保持する

### PER-006

Beliefs:

- 二つの選択例だけでなく全orderを含めても複数の結果へ分かれたため、update protocolを観測条件として明示する必要性が強まった
- A/B以外のfixed pointが出たことで、`correct recall`の操作的定義はさらに慎重であるべき
- それでも、このtoy modelの現象を生物学的memoryへ直接一般化してはいけない

Goals:

- stored / nonstoredを結果記録で明示的に分けさせる
- 次に条件を変えるなら、変更条件と選択規則を先に固定させる

Memory:

- 720 orderを全て含めた集計と第三のfixed point Dを保持する

## World delta

共同記録に、

- 全720 update order
- A/B/Dへの分類結果
- Dがnonstored fixed pointであること

が成立した。

具体的な計算機機種、programming language、所属機関はこのeventでも固定しない。小規模な全列挙を実行できる計算手段が研究環境内に存在するというBOOT-002の既存制約だけを使う。

## Who observed what

- PER-005 / PER-006: 上記720-order結果とDのfixed-point確認
- 他ペルソナ: 未観測
- 現代側persona: このstory-time eventを自動的には観測しない

## Research branch

新しいQ / H / EXPはこのeventだけでは作成しない。

理由:

- update-order依存は既存Q-004 / H-004 / EXP-004と重なる
- nonstored stable stateの構造は既存Q-003 / H-003 / EXP-003と重なる
- EVT-005は物語世界で二つの既存問題が同じ具体例に同時に現れた観測であり、それだけで重複EXPを作らない

PER-005 / PER-006がDについて既存Q-003とは異なる新しい検証可能な問いを実際に立てた場合に、後続eventから研究分岐を再判断する。

## Structure impact

結果を見てから整理すると、EVT-004で成立した`転`を取り消すものではない。

むしろ「AかBか」という二択自体も不十分になり、EVT-001で最初に出た「保存していないところで止まるなら、その状態は何からできている？」という問いが、別経路から具体的に戻ってきた。

ただし、これを予定された`結`や次話の転換点として自動指定しない。

## Generation validation

このeventのoutcome-sensitive条件はAction lock commitで結果解決前に固定され、その後変更していない。

したがって、Test-001のEVT-004と異なり、EVT-005は**environment resolverの結果独立性を検証するclean validation candidate**として扱える。
