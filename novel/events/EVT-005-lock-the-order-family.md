# EVT-005 更新順の選び方を先に固定する

状態: `PROVISIONAL / RESOLVED`

Resolution provenance: `LOCKED`

Action-lock commit: `59ff6530d202b79834afbe8ffdceee1256437315`

## Story time

`T0-1980S + next joint paper check after EVT-004`

具体年月日は固定しない。

## Timeline position

- Parent: `EVT-004`
- Previous event: `EVT-004`
- Next event: 未成立

## Participants

- PER-005 — 1980年代研究者
- PER-006 — 実験神経科学寄りの同僚

新しい独立主体は必要としない。

## World before

- EVT-004で、6 unit・3 stored patternsの紙上networkについて、同一cue・同一weightsから二つの手選択されたupdate orderでA/Bへ分かれる例が成立している
- PER-005 / PER-006は、その一例だけから頻度一般やmemory一般へ一般化してはいない
- PER-005は「この現象が作為的な小例だけなのか」を区別したい
- PER-006は、一般化する前に同じ観測手順で再現範囲を確かめたい
- 現代側EXP-004の統計結果は二人のKnowledgeではない

## Observations available before action selection

### PER-005

- EVT-001〜004で自分が観測・記録した内容
- EVT-004のA / B / C、cue、order α / βとその紙上結果
- 自分の時代に利用可能なHopfield型binary networkと非同期更新の数理知識

### PER-006

- EVT-002〜004で共有された内容
- EVT-004で二つのupdate orderが人手で選ばれていたこと
- 同じ観測手順で、結果の選別を減らしたいという自分の現在goal

## Action selection

PER-006は、EVT-004の二つのorderだけを追加で選び続けると、「面白いorderを拾っただけ」という疑いが残ると指摘する。

PER-005は、紙で追える範囲を保ちながらupdate orderの選び方を機械化するため、unit番号の自然順序

```text
(1, 2, 3, 4, 5, 6)
```

の**全6 cyclic rotations**だけを次の検査集合にする。

この集合では各unitが一度ずつ先頭になる。結果を見てorderを追加・削除しない。

## Locked network conditions

EVT-004と同じものをそのまま使う。

```text
A = (-1, +1, +1, +1, -1, -1)
B = (+1, -1, +1, -1, -1, +1)
C = (-1, -1, -1, -1, +1, -1)

cue = (+1, -1, +1, +1, -1, -1)
```

結合:

- A / B / Cを同じHebbian outer-product ruleで加算
- self-connectionは0
- 正の全体定数倍は省略し、紙上では整数和を使う

unit update:

- 一つずつ非同期更新
- local field > 0 なら +1
- local field < 0 なら -1
- local field = 0 なら現在値を保持

## Locked order set

次の6本を**すべて**実行する。

```text
r1 = (1, 2, 3, 4, 5, 6)
r2 = (2, 3, 4, 5, 6, 1)
r3 = (3, 4, 5, 6, 1, 2)
r4 = (4, 5, 6, 1, 2, 3)
r5 = (5, 6, 1, 2, 3, 4)
r6 = (6, 1, 2, 3, 4, 5)
```

## Locked trial / stopping / inclusion rule

各orderについて:

1. 必ず同じ `cue` から開始する
2. そのorderを1 sweepとして繰り返す
3. 1 sweep中に一つもunitが変化しなければstableと判定して停止する
4. 最大20 sweepsまで実行する
5. 20 sweepsでstableにならなければ `NONCONVERGED` と記録する
6. 6 orderすべてを結果表へ残す
7. A / Bへ行かなかった結果も削除しない
8. 結果が単調・平凡でも別orderへ差し替えない

final state分類:

- `A`
- `B`
- `C`
- `OTHER_STABLE`
- `NONCONVERGED`

## Resolver allowed information

resolverは次だけを使ってよい。

- このファイルにlockされたA / B / C / cue
- Hebbian結合規則
- zero-field rule
- 6 cyclic orders
- stopping / inclusion rule
- 整数演算によるexact update

## Resolver forbidden for action selection

次は、このeventの条件選択・order選択へ使ってはいけない。

- EXP-004の122/200、4000 runs、個別cue結果
- 「AとBの両方をもう一度出したい」という作者側の期待
- 第2話や次の`転`に必要な展開
- 長期的な輪廻・本人性プロット
- outcomeを見てからのorder追加・削除

この禁止はpersonaのKnowledge境界とは別に、生成方式のresolver selection biasを抑えるためのもの。

## Resolution method

Action-lock commit後、上記6 trialだけを整数演算でexactに解決した。

locked条件、order集合、stopping / inclusion ruleは変更していない。

## Resolved results

6本すべてが2 sweeps目でstable判定になった。

```text
r1 -> (-1, +1, +1, +1, -1, -1) = A             / 2 sweeps
r2 -> (+1, +1, +1, +1, -1, +1) = OTHER_STABLE  / 2 sweeps
r3 -> (+1, -1, +1, -1, -1, +1) = B             / 2 sweeps
r4 -> (+1, -1, +1, -1, -1, +1) = B             / 2 sweeps
r5 -> (+1, +1, +1, +1, -1, +1) = OTHER_STABLE  / 2 sweeps
r6 -> (+1, +1, +1, +1, -1, +1) = OTHER_STABLE  / 2 sweeps
```

結果分類:

- A: 1 / 6
- B: 2 / 6
- C: 0 / 6
- OTHER_STABLE: 3 / 6
- NONCONVERGED: 0 / 6

`OTHER_STABLE`として現れた状態をDと呼ぶ。

```text
D = (+1, +1, +1, +1, -1, +1)
```

DはA / B / Cのどれとも一致しない。

- Hamming(D, A) = 2
- Hamming(D, B) = 2
- Hamming(D, C) = 6

Dでは各unitのlocal fieldの符号が現在値と一致しており、paper model上のstable stateである。

## Actions after observing results

PER-005は、EVT-004で二つだけ選んだorderの結果を増やすのではなく、先に決めた6本の欄を最後まで埋める。

AとBだけでなく、保存していないDが3本で現れたため、ノート上の分類をA/Bの二択から、少なくとも

- stored A
- stored B
- nonstored stable D

へ書き換える。

PER-006は、Dを「第三の記憶」と呼ぶことを止める。保存したpatternではない以上、まずは`保存していない安定状態`として記録し、memory一般の語へ広げないよう求める。

PER-005は、

> 二つの原像のどちらへ戻るか、では足りない。
>
> 戻り先そのものが、原像の一覧の外にもある。

と追記する。

## Resolved consequence

- EVT-004の二つの手選択orderだけに依存せず、結果前に固定した6 cyclic ordersでも複数のfinal stateが観測された
- 同一cue・同一weights・同一update ruleから、A / B / nonstored stable Dの三種類へ分かれた
- PER-005の局所問題は「AとBのどちらが正しいか」だけでは足りなくなった
- final stateから唯一のstored原像を逆算する作業前提は、少なくともこのpaper modelではさらに弱くなった
- 6 unit・一つのpattern集合・6 ordersだけの観測であり、頻度一般や生物学的memoryへ一般化しない

## World delta

客観的に成立したもの:

- 共同メモに、結果前に固定した6 cyclic ordersと全結果が残った
- r1〜r6を選別せずすべて記録した
- stored A / stored B / nonstored stable Dという三分類が同一cueから観測された
- Dの具体状態とA/B/CへのHamming距離が記録された
- 具体的な計算機・language・所属環境はまだ固定していない

## Persona deltas

### PER-005

Beliefs:
- update orderが異なると、同じcueから複数のstored stateだけでなくnonstored stable stateへも到達し得る小例を自分で確認した
- `correct recall`を「AかBのどちらへ戻ったか」だけで定義するのは不十分
- final stateから原像を逆向きに一意推定するには、初期条件・update protocol・保存集合との関係を分ける必要がある

Goals:
- DがA/Bの単純な中間なのか、別種の安定構造なのかを記述したい
- 一つの小例から一般化せず、何を固定し何を変えたかを先に記録する方法を続けたい

Relations:
- PER-006の「先に検査集合を固定する」要求を、結果選別を減らす研究上の手続きとして評価する

Memory:
- cyclic rotations全6本の結果A / D / B / B / D / Dを保持する
- Dが保存patternではないことを保持する

### PER-006

Beliefs:
- 結果を見てorderを選ぶより、検査集合を先に固定した方がmodel内の主張を狭くできる
- Dをmemoryと呼ぶ根拠はなく、nonstored stable stateとして扱うべき
- update-order依存はA/Bの二者択一だけの問題ではない

Goals:
- Dの構造を述べる場合も、model内の事実と生物学的memoryの主張を分けさせる
- 次の比較でも観測項目・変更条件・停止条件を先に決めさせる

Relations:
- PER-005がA/B以外の結果を捨てずに記録したため、共同検討を継続する価値が高まった

Memory:
- 6 cyclic ordersすべてを先に固定し、A / B / Dの三種が出たことを保持する

## Who observed what

- PER-005 / PER-006: lockedした6 orders、全紙上計算、A/B/Dへの分類、相互の発言
- 他ペルソナ: 未観測

## Research branch after resolution

新しいQ / H / EXPはこのeventだけでは作成しない。

理由:

- `nonstored stable state`の構造は既存のQ-003 / EXP-003と論点が重なる
- `same cue + update-order dependence`は既存のQ-004 / EXP-004と論点が重なる
- EVT-005は両論点が同一の小規模paper modelで同時に現れたが、それだけで新しい独立research targetを作る必要はない

PER-005 / PER-006が後続eventでDについて既存問いとは異なる検証可能な問題を実際に立てた場合に、改めて研究分岐を判断する。

## Canon candidate

- PER-005 / PER-006がEVT-004の小規模networkに対し、結果前に固定した6 cyclic update ordersをすべて検査したこと
- 同一cueからA / B / nonstored stable Dの三種を観測したこと
- PER-005の問いが「どのstored原像か」から「stored集合外の戻り先をどう扱うか」へ広がったこと

人間受理前に`canon.md`へ自動昇格させない。

## Structure impact

EVT-005は、EVT-004で成立した局所的な`転`を結果前lockされた追加観測で補強した。

ただし、`転`が強くなったからという理由で`結`へ進めない。

現在の新しい局所問題は、

**同じcueからstored A / stored B / nonstored stable Dへ到達し得るとき、「戻る」という語は何を指しているのか。**

である。

次のeventは、この問いに予定された答えを与えるのではなく、PER-005 / PER-006の現在stateと環境から改めて生成する。

## Validation result

生成方式のTest-002として、このeventは `PASS` とする。

確認できたこと:

- outcome-sensitiveな条件を結果前にexternalizeできた
- action-lock commit後にだけ結果を解決した
- locked order集合を変更しなかった
- A/B以外の結果も削除しなかった
- 結果が三種類へ分かれても、そのまま物語状態へ採用した

このPASSは「A/B/Dという結果が一般的である」ことを意味しない。

**ACTION_LOCKED → resolver → outcomeを差し替えず受理する手順が実際に動いた**ことに対する生成方式上の判定である。
