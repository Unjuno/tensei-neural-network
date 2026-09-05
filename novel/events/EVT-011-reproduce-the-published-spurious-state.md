# EVT-011 論文の16素子例をそのまま試す

状態: `RESOLVED / PROVISIONAL`

Resolution provenance: `LOCKED`

Action-lock commit: `28cc5684955a3dae3ccf73af28c1433328ab15a4`

## Story time

`T0-1980S + published-example check after EVT-010`

## Timeline position

- Parent: `EVT-010`
- Previous event: `EVT-010`
- Next event: 未成立

## Resolution scope

- PER-005 高橋修一
- PER-006 佐伯玲子
- EVT-010で二人が読解したHopfield / Feinstein / Palmer (1983)
- 同論文が本文中に掲載した16-neurone / 3-memoryの具体例
- ORG-001が既に許容している紙上計算・共同検討環境

今回まだ独立entity化しないもの:

- 共用計算機SYS/OBJ: 今回は16成分のfixed-point stabilityを一度確認するだけで、紙上でも完全追跡可能
- 文献コピーOBJ: 保存・貸出・来歴が今回の結果を左右さない

## World before

EVT-009で、二人の6-unit toy networkではstored patternsとその全符号反転以外のstable finalが存在しないことを全状態列挙から確認した。

EVT-010で、1983年の一次文献にはstored memory以外のspurious stable statesが明示的に扱われていることを二人が確認した。

高橋の局所目標は「文献に掲載された例を、見たい結果に合わせて別modelへ改変せず再確認する」こと。佐伯の局所目標は、文献記載と自分たちの再計算を分離し、失敗もそのまま記録すること。

## Story-visible action selection

二人は、論文の32-neurone random-start simulationや30〜1,000 neuroneの一般的computer modellingをいきなり再現しない。

代わりに、同論文がspurious stateの具体例として**明示的に掲載している16-neurone / 3-memory例**をそのまま用い、その候補stateが同論文のHebbian connection ruleの下で本当にstored patternでもその符号反転でもないstable stateかだけを最初に検査する。

この選択では新しいN、pattern、seed、initial-state distributionを作者側で作らない。

---

# ACTION LOCK

以下を結果計算前にcommit `28cc5684955a3dae3ccf73af28c1433328ab15a4` で固定した。

## Source

J. J. Hopfield, D. I. Feinstein, R. G. Palmer, “‘Unlearning’ has a stabilizing effect in collective memories,” *Nature* 304, 158–159 (1983), DOI `10.1038/304158a0`。

同論文本文は、binary state `μ_i = ±1`、

```text
T_ij = Σ_s μ_i^s μ_j^s
T_ii = 0
```

というconnection ruleを記載し、16 neuronesについて三つのmemoryと一つのspurious-memory candidateを具体的に掲載している。

## Locked patterns

論文掲載の順序をそのまま1〜16番とする。

```text
M1 = (+,+,+,+,-,-,-,-, +,+,-,+,-,+,-,-)
M2 = (+,+,+,+,-,-,-,-, -,-,+,-,+,-,+,+)
M3 = (+,+,-,-,+,+,-,-, +,-,-,+,+,-,-,+)
Q  = (+,+,+,+,-,-,-,-, +,-,-,+,+,-,-,+)
```

計算では `+ = +1`, `- = -1` とする。

Qは論文がspurious memoryとして掲載したcandidateである。二人にとって今回の目的は「未知のspurious stateを発見する」ことではなく、掲載例のmodel-level主張を再計算すること。

## Locked weights

```text
T_ij = M1_i M1_j + M2_i M2_j + M3_i M3_j   (i != j)
T_ii = 0
```

正規化係数は符号判定を変えない正の全体scaleなので用いない。

## Locked stability check

Qについて各unitのlocal input

```text
h_i(Q) = Σ_j T_ij Q_j
```

をexact integer arithmeticで求める。

今回の判定では1983論文のzero-input記述の曖昧さを結果都合で補完しない。

- 全16 unitで `h_i != 0` かつ `sign(h_i) = Q_i` なら、tie conventionに依存せずQはstable
- 一つでも `h_i != 0` で `sign(h_i) != Q_i` ならQはnot stable
- `h_i = 0` が一つでもあれば、zero-input ruleの追加解釈が必要になるため今回のstability判定は`UNCERTAIN`

## Locked residual check

Qが次の6状態のどれとも一致しないことを確認する。

```text
M1, M2, M3, -M1, -M2, -M3
```

## Predeclared outcome

`PASS`:

- 全local inputがnonzeroでQの符号と一致し、Qがstable
- Qがstored patternおよびstored-pattern negationのいずれでもない

`FAIL`:

- nonzero local inputのどれかがQの符号と不一致
- またはQがstored pattern / negationのいずれかだった

`UNCERTAIN`:

- local input 0が存在し、論文のzero-input conventionを追加固定しないとstableか判定できない

## Inclusion / stopping rule

- 16 unitをすべて確認する
- 不都合なunitを除外しない
- Q以外の別candidateを結果後に追加しない
- 上記PASS / FAIL / UNCERTAINが決まった時点でこのeventを停止する
- 今回はbasin size、random starting states、unlearningの効果までは調べない

---

# RESOLUTION

locked patternsとconnection ruleだけから、16 unitすべてのlocal inputをexact integer arithmeticで計算した。

## Local inputs

```text
h(Q) =
(+21,+21,+5,+5,-5,-5,-21,-21,
  +5, -5,-5,+5,+5,-5,-5,+5)
```

各unitについて `Q_i * h_i` は、

```text
(21,21,5,5,5,5,21,21,5,5,5,5,5,5,5,5)
```

となった。

したがって、

- 16 / 16 unitで `h_i != 0`
- 16 / 16 unitで `sign(h_i) = Q_i`
- 最小marginは `|h_i| = 5`

である。

zero-inputは一つもないため、zero-field tie conventionを追加せずQのstabilityを判定できる。

## Residual check

Qは、

```text
M1, M2, M3, -M1, -M2, -M3
```

のどれとも一致しなかった。

したがってQは、今回のstored setとそのglobal sign inversionだけでは説明できないstable stateである。

## Outcome

`PASS`

## Resolved consequence

- 1983論文掲載の16-neurone / 3-memory例を同論文のHebbian connection ruleで再計算すると、掲載されたQは確かにstableだった
- Qはstored patternでもその全符号反転でもない
- EVT-009で現在6-unit toyのresidualが空だったことと矛盾しない。model条件が異なる
- 二人は、少なくとも一つの当時公刊済み具体例について「stored / stored-negation以外のstable state」がmodel-levelで成立することを自分たちの計算でも確認した
- ただしQがどの一般的構造classに属するか、どれほど典型的か、basinがどれほど大きいか、unlearningでどう変わるかは今回まだ未解決
- 1985年以降のmixture-state理論はこのeventの説明に使用しない

## Persona deltas

### PER-005 高橋修一

Beliefs:

- 6-unit toyでresidualが空だったのは、spurious stable structure一般の不存在ではなく、そのtoyの有限構造による結果だった
- 文献掲載の16-unit例では、stored patternとその符号反転を除いてもstable stateが残る
- 次に問うべきなのは、Qへ意味を与えることではなく、Qが三つのstored patternsからどのような構造として作られているかを、当時の文献記述と自分たちの計算の範囲で分解すること

Goals:

- QとM1/M2/M3の成分関係を記述し、論文がいう「triplesにoriginを持つ」という記述を自分たちの例で追えるか確認する
- basin sizeやunlearningへ進む前に、まず一つのspurious stateの構造を完全に説明できるか確かめる

Memory:

- 16個のlocal input値
- 全unitでnonzeroかつQと同符号
- Qがstored / negationのいずれでもないこと

### PER-006 佐伯玲子

Beliefs:

- 文献に「spurious」と書かれているだけでなく、二人自身のstability checkでもQはstableだった
- ただし「stableでnonstored」であることと、生物学的に偽記憶・混同・創作等を意味することは別
- Qの由来を説明する前に、pattern間の相関と成分関係を操作的に分けて記録する必要がある

Goals:

- Qを心理学的ラベルへ飛躍させず、M1/M2/M3との関係を数理的に記述させる
- 「論文がそう呼ぶ」「二人が再計算した」「生物学的に解釈する」の三層を引き続き分離する

Memory:

- Qのstabilityはzero-field conventionに依存しなかったこと
- Qはstored / global-negation classの外にあること

## Organization / world delta

ORG-001のmission / governanceに変更なし。

今回も紙上で完全追跡可能だったため、共用計算資源を独立SYS/OBJへ展開しない。

共同検討記録としては、1983論文掲載例の再計算結果がPER-005 / PER-006間で共有された。研究所のinstitutional memoryへ正式提出されたとはまだ扱わない。

Fact level:

- real-world evidence: 1983論文が16-neuroneのspurious-memory candidateを掲載している
- local story fact: 二人が同じ掲載patternを同じconnection ruleで再計算し、stableかつstored/negation外と確認した
- institutional fact: 未成立
- public story fact: 未成立
- canon fact: 未昇格

## Who observed what

- PER-005 / PER-006: patterns、local-input計算、PASS判定を共有
- ORG-001: 内容を組織として承認したとは扱わない
- 他persona: 未観測
- 現代側persona: 未観測

## Research branch after resolution

新しい作者側EXPはまだ必須ではない。

今回のQは一次文献に明示された有限例をexactに再計算したため、次のstory-side問いはまずpattern structureの説明である。

将来、random-start accessibility、より大きいnetwork、unlearning効果まで人物が進む場合は、その時点で計算資源・randomness・trial数を事前固定し、必要なら新しいauthor-side EXPと分離する。

## Structure impact

EVT-009〜011で一つの認識遷移が成立した。

```text
自分たちのtoyでは残差が空
→ 当時の一次文献へ戻る
→ 掲載例をそのまま再計算
→ stored / negation以外のstable stateを確認
```

この範囲は自然なreading unit候補になり得る。

ただしchapter化する場合も、このEVT-011より先の構造説明や将来の実験結果を先取りしない。

## Generation validation

- 16-neurone例は結果後に作者側で探索したpatternではなく、EVT-010で選択済みの1983一次文献に明示された例をそのまま採用した
- patterns / weights /判定規則をcommitしてからlocal inputsを計算した
- zero inputが出た場合はUNCERTAINとする規則を先に固定し、結果後にtie ruleを足していない
- 1985年以降のmixture-state理論を条件選択・解釈へ使わなかった
- 第3話の結末を理由にQやmodelを差し替えなかった
