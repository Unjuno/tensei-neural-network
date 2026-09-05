# EVT-011 論文の16素子例をそのまま試す

状態: `ACTION_LOCKED / PROVISIONAL`

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

以下を結果計算前に固定する。

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

## Resolver may use

- 上記locked patterns
- 上記Hebbian connection rule
- exact integer arithmetic
- EVT-010までの人物knowledge

## Resolver must not use for condition selection

- 1985年以降のmixture-state理論
- 現代側EXP-003〜005
- 第3話で望む結末
- 結果を見て別pattern / N / tie ruleへ差し替えること

## Resolution provenance target

`LOCKED`
