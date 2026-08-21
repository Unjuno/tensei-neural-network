# EVT-005 更新順の選び方を先に固定する

状態: `ACTION_LOCKED`

Resolution provenance: `LOCKED_PENDING_RESOLUTION`

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

このcommit後に、上記6 trialをexactに解決する。

outcomeはこの`ACTION_LOCKED`版には書かない。

解決後、同じファイルを更新して:

- 各r1〜r6のfinal state
- sweeps数
- classification
- 客観的なworld delta
- PER-005 / PER-006が実際に観測した内容
- persona delta
- Structure impact

を記録する。

## Research branch before resolution

新しいQ / H / EXPは作成しない。

このeventの第一目的は、既存の物語問題を人物側で続けることと、`ACTION_LOCKED → RESOLVED` の生成方式を実際に検証すること。

結果が新しい独立研究価値を持つかどうかは、結果解決後に別途判断する。

## Validation target

成功条件はA/B分岐が再現することではない。

**このlock後にどの結果が出ても、条件を差し替えず、その結果を物語状態として受け入れること。**
