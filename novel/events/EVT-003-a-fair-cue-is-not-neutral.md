# EVT-003 公平な手掛かりは中立ではない

状態: `PROVISIONAL`

## Story time

`T0-1980S + protocol sketch after EVT-002`

具体年月日はまだ固定しない。EVT-002の会話後、PER-005とPER-006が「二つの記憶の間にある手掛かり」を実際にどう作るか検討した研究時間。

## Timeline position

- Parent: `EVT-002`
- Previous event: `EVT-002`
- Next event: 未成立

## Participants

- PER-005 — 1980年代研究者
- PER-006 — 実験神経科学寄りの同僚

新しい独立主体は、このeventでは必要にならない。

## World before

- PER-005は`correct recall`のtargetが常に一意とは限らないと考え始めている
- PER-006は、実験者が「正解」を先に決めること自体を問題視している
- 二人はまだ曖昧cueを具体的な操作へ落としていない
- 物語世界内でbalanced-cue計算はまだ実行されていない
- 現代側EXP-004の結果は二人とも知らない

## Observations available

### PER-005

- 自分のEVT-001 / EVT-002のノート
- PER-006とのこれまでの会話
- 1980年代半ばまでに本人が利用できるnetwork / memoryの文献と数理知識

### PER-006

- PER-005が共有したstored pattern / cue / stable stateの説明
- EVT-002で共有されたtarget定義の問題
- 自分の実験・観測に関する問題意識

## Actions

PER-005は、二つの保存pattern `A` と `B` の間にあるcueを、まず最も単純な形で作ろうとする。

二つのpatternで値が異なるunitだけを取り出し、その半分をA側、残り半分をB側から取る。両者が同じunitはそのまま残す。

PER-005はこれを、少なくとも**異なるunit数だけを数えればAとBへ同じ距離にある手掛かり**として扱えると考える。

PER-006は、その構成自体には同意するが、「公平」という言葉には同意しない。

会話上、次の趣旨を指摘する。

> 数が半分ずつでも、同じ意味で半分とは限らない。
>
> 君のnetworkの中で、すべての違いが同じ重さを持つのか。

PER-005は、異なるunit数が等しいことと、dynamics上でA/Bが等しく有利であることを自分が混同しかけていたと認識する。

二人はノート上で、少なくとも次を別々に記録することにする。

1. cueからA/Bへの**bit差の数**
2. 同じcueを与えた後に**どのstateへ移ったか**
3. 同じ初期stateでも更新の仕方を変えたときに結果が変わるか
4. A/B以外へ止まった場合、それを失敗として捨てず別に残す

## Resolved consequence

- 「二つの記憶の間にあるcue」が、抽象的な比喩から操作可能な構成へ一段具体化した
- PER-005 / PER-006は、bit差が等しいことを`neutral`や`fair`の十分条件とは扱わないことで一致した
- 次に計算を行う場合、A/Bへの距離、最終state、更新条件を分けて記録するという最低限の観測項目が成立した
- まだ具体的なN、保存pattern数、run数、計算機、programming language、実行結果は決めていない

## World delta

客観的に成立したもの:

- PER-005 / PER-006の共同メモに、二つの保存patternからbit差数が等しいcueを作る手順が記録された
- 「等しいbit差」と「dynamics上の中立性」を別概念として扱う注意書きが残った
- 次の計算で記録すべき観測項目が4点に整理された

まだ計算機資源の利用、programの実装、simulation結果は発生していない。

## Persona deltas

### PER-005

Beliefs:
- cueがA/Bへ同じbit差を持つことは、A/Bがdynamics上で等価であることを保証しない
- `correct`を議論する前に、初期条件・更新条件・最終stateを別々に記録する必要がある

Goals:
- この最小protocolを実行可能なnetwork規模・計算手段へ落としたい
- A/B以外へ止まった場合も観測対象として残したい

Relations:
- PER-006の批判は、理論を否定するものではなく、測定語彙を明確にする役割を持つと理解が深まる

Memory:
- 「半分ずつ作ったcueでも中立とは限らない」という指摘を保持する

### PER-006

Beliefs:
- PER-005は`correct`の定義を固定して結果を選別するのではなく、観測項目を分ける方向へ修正できる
- bit数による距離は一つの操作的指標としては使えるが、memoryの意味そのものではない

Goals:
- 次に実際の計算結果を見る場合、A/B以外のstateを除外しないことを確認したい
- 数理的な距離と、memoryについての解釈を分離したまま進めたい

Relations:
- PER-005との共同作業が、単なる批判からprotocol設計へ進んだ

## Who observed what

- PER-005 / PER-006: 共同で作ったprotocol sketchと会話
- 他ペルソナ: 未観測

## Research branch

**このeventから新しいQ / H / EXPを自動作成しない。**

理由:

- 現在成立したのは物語世界内のprotocol sketchであり、まだ新しい観測結果はない
- 「bit差が等しいこととdynamics上の中立性は別」という論点は重要だが、現時点で独立した次実験を自動開始する必要はない
- 次の研究分岐は、後続eventで実際の計算・観測・新しい言葉が生じるか、独立した研究価値が明確になった場合に判断する

現代側EXP-004がすでに類似したbalanced cueを扱っていることは作者側の情報であり、PER-005 / PER-006のこのeventの原因にはしない。

## Canon candidate

- PER-005 / PER-006が最初の共同protocolとして、二つのstored patternsへbit差が等しいcueを構成する案を作ったこと
- 二人が「等距離」と「中立」を区別したこと

人間受理前に`canon.md`へ自動昇格させない。

## Structure impact

現在位置は引き続き `起 / 承`。

EVT-003では問いが解決したのではなく、相互作用によって操作的制約が一つ増えた。

- 抽象的な曖昧cue → 作れるcue
- 等距離 → 中立とは限らない
- 成功/失敗の二分 → A / B / その他を観測する

という形で`承`の証拠・制約蓄積が進んだと整理する。
