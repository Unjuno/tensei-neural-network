# EVT-004 同じ手掛かりから二つの戻り先

状態: `PROVISIONAL`

## Story time

`T0-1980S + first paper calculation after EVT-003`

具体年月日は固定しない。EVT-003で作ったprotocol sketchを、PER-005とPER-006が計算機実装へ進む前に紙上で検査した研究時間。

## Timeline position

- Parent: `EVT-003`
- Previous event: `EVT-003`
- Next event: 未成立

## Participants

- PER-005 — 1980年代研究者
- PER-006 — 実験神経科学寄りの同僚

新しい独立主体は必要にならなかった。

## World before

- A/Bへのbit差数が等しいcueを構成する手順は成立済み
- 二人は「等距離」と「dynamics上の中立」を区別している
- 次の計算では、距離、final state、update条件、A/B以外のstateを分けて記録する方針がある
- 具体的な計算機、programming language、大規模simulation条件は未確定
- 現代側EXP-004の結果は二人とも知らない

## Observations available

### PER-005

- EVT-001〜003で自分が観測・記録した内容
- 自分の時代に利用可能なHopfield型のbinary networkと非同期更新に関する数理知識
- 紙と筆記具で追える小規模な計算

### PER-006

- EVT-002〜003で共有された説明と共同メモ
- PER-005がその場で示す小規模計算
- 自分の観測基準・操作的定義への要求

## Actions

PER-005は、計算機の条件を先に固定する代わりに、まず手で追える6 unitのbinary networkを作る。

保存候補として三つのpatternを置く。

```text
A = (-1, +1, +1, +1, -1, -1)
B = (+1, -1, +1, -1, -1, +1)
C = (-1, -1, -1, -1, +1, -1)
```

三つを同じHebbian ruleで結合へ入れ、自己結合は0とする。全体の正の定数倍は符号判定を変えないため、紙上では整数和のまま扱う。

AとBが異なるunitは4個ある。PER-005はその半分ずつを取って、

```text
cue = (+1, -1, +1, +1, -1, -1)
```

を作る。

このcueはAから2 bit、Bから2 bit異なる。

PER-006は、EVT-003の共同メモに従い、結果欄の前にupdate orderを書かせる。

PER-005は、各unitを一つずつ更新し、局所場が0ならそのunitの現在値を保持するという同じ規則を使って、二つの順序を追う。

```text
order α = 1, 3, 6, 4, 5, 2
order β = 4, 6, 1, 3, 5, 2
```

同じcue、同じ三つの保存pattern、同じ結合、同じ更新規則で、異なるのは一巡内の更新順だけである。

紙上計算では、

```text
order α -> A
order β -> B
```

となり、どちらもその後の同じ順序で変化しないstable stateになる。

PER-005は最初、計算を取り違えた可能性を疑い、A/Bがそれぞれ実際にstableであることと、cueからのbit差が2対2であることを別に再確認する。

PER-006は結果を見て、これは「どちらが正しい記憶か」を決めたのではなく、むしろ**同じ手掛かりへ一意の正解を置く前提が、この小さな系では維持できない**と指摘する。

PER-005はノートに、

> 手掛かりが同じでも、戻り先は一つとは限らない。
>
> ならば、想起の結果だけを見て原像を逆算してよいのか。

と追記する。

## Resolved consequence

- EVT-003のprotocolが、物語世界内で初めて具体的な計算へ進んだ
- 同一cue・同一weightsでもupdate orderだけの差でA/Bという異なるstored patternへ到達する具体例を二人が観測した
- 「等距離だが中立とは限らない」は抽象的注意から観測済みの問題へ変わった
- `correct recall`をfinal stateだけで一意に定義する方針は、この例に対して維持できなくなった
- ただし、6-unitの一構成例をmemory一般や生物学的記憶へ一般化していない
- 大規模simulation、頻度推定、計算機実装はまだ発生していない

## World delta

客観的に成立したもの:

- 共同メモに6-unitの三つのpattern、等距離cue、二つのupdate order、A/Bへの異なる到達結果が記録された
- A/Bへの距離とfinal stateを別欄で記録する方針が実際に使われた
- 具体的な計算機・language・所属環境を固定せずに、最初のnetwork計算が紙上で成立した

## Persona deltas

### PER-005

Beliefs:
- 同じinitial stateとweightsからでも、非同期更新順の違いで異なるstored stateへ戻り得る小さな例を自分で確認した
- final stateだけから「唯一の原像」を逆算することには追加条件が必要である
- dynamicsを記述するならupdate protocolは補助条件ではなく観測対象の一部である

Goals:
- この現象が小さな作為的例だけなのか、より広い条件でも現れるのかを区別したい
- A/B以外のstable stateも含め、結果を分類する方法を考えたい

Relations:
- PER-006が結果を出す前に観測欄を分けさせたことの価値を認める

Memory:
- 同じcueからorder αでA、order βでBへ到達した紙上計算を保持する
- 「想起の結果だけを見て原像を逆算してよいのか」という問いを保持する

### PER-006

Beliefs:
- `correct`を一意に置く前にupdate protocolを明示すべきだという要求が、具体例で必要になった
- このmodel内の結果は興味深いが、生物学的memoryの複数性を直接示したわけではない

Goals:
- 例を一般化する前に、同じ観測手順で再現範囲を確かめさせたい
- model内の非一意性とmemory一般についての主張を分離したい

Relations:
- PER-005が反例を隠さず研究問題として受け入れたため、共同検討を続ける価値が高まった

Memory:
- 同じcue・同じweightsからupdate orderの違いだけでA/Bへ分かれた計算を保持する

## Who observed what

- PER-005 / PER-006: 全紙上計算、二つのupdate order、A/Bへの到達結果、相互の発言
- 他ペルソナ: 未観測

## Research branch

新しいQ / H / EXPは作成しない。

理由:

- 現代側ではEVT-002から派生したQ-004 / H-004 / EXP-004が、同じ種類の「等距離cueとupdate-order依存」を既に独立研究として扱っている
- ここで同内容を別IDへ重複登録する必要はない
- EXP-004の数値結果をPER-005 / PER-006へ共有したわけではなく、二人が物語世界内で独立に得たのは上記6-unitの一例だけである

この6-unit例を現代側研究の追加データへ組み込むかは、別途研究上の必要が生じた場合に判断する。

## Canon candidate

- PER-005 / PER-006が最初の具体計算として6-unitの紙上例を扱ったこと
- 同一cueからupdate orderだけの違いでA/Bへ分岐する例を観測したこと
- PER-005が「想起結果から唯一の原像を逆算できるか」を新しい局所問題として持ったこと

人間受理前に`canon.md`へ自動昇格させない。

## Structure impact

EVT-004は、EVT-001〜003で蓄積した問いに対して最初の観測反例が出たため、現在の局所構造を `起 / 承 / 転` と整理できる。

これは「第1話に転が必要だから」起こしたものではない。EVT-003で成立済みだったprotocolを、PER-005の局所目標に従って最小の紙上計算へ落とした結果、従来の「一つのcueには一つの正解を置ける」という暗黙前提が維持できなくなったためである。

この地点では、次の大規模計算や結論はまだ成立していない。