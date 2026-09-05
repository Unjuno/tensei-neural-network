# 第3話 用語検証

状態: `PASS`

第3話本文で実際に使用した語だけを対象とする。

## 参照資料

### S001 — 渡辺武良「分布型連想記憶モデル」1984

- `連想記憶モデル`
- `ユニット`
- `パタン`
- `想起過程`
- `手掛かりパタン`

を1984年日本語資料で確認。第1話用語検証と同じ一次資料を再利用する。

### S004 — Hopfield / Feinstein / Palmer (1983)

J. J. Hopfield, D. I. Feinstein, R. G. Palmer, “‘Unlearning’ has a stabilizing effect in collective memories,” *Nature* 304, 158–159 (1983), DOI `10.1038/304158a0`。

本文・abstractで、

- `associative memory`
- `spurious memories`
- `unlearning`
- binary neurone state `±1`
- asynchronous update
- synaptic connection matrix
- stable state

を確認。

## 検証表

| 原概念 | 第3話での表記 | 人物発話での扱い | 状態 | 根拠・判断 |
|---|---|---|---|---|
| associative memory | 連想記憶 | 使用可 | APPLIED | S001で1984年日本語用例あり |
| stored pattern / memory | 記憶パターン / 保存した記憶 | A/B/C等のラベルを優先 | APPLIED | S001のパタン語彙と本文の既存用法に整合 |
| stable state | 安定状態 / 止まる | 使用可 | APPLIED | 技術的にはstable、会話では操作結果を直接記述 |
| local input / field | 各素子へ入る結合入力の総和 | `局所場`を使わない | APPLIED | 第1話方針を継承。1983原文の`input to neurone i`とも意味整合 |
| spurious memory | 原文引用時のみ `spurious memory / memories`、説明は「保存していない安定状態」 | 原文の呼称としてのみ英語を許容 | APPLIED | S004の実語。日本語の「偽記憶」は心理学的意味を強く誘発するため本文では採用しない |
| unlearning | 原文の題名・概念として`unlearning` | 「忘れさせる？」程度の暫定説明に留める | APPLIED | S004の論文タイトル・本文語。確定的な和訳語を人物へ固定しない |
| neurone / unit | 素子 / ニューロン | 文献規模説明では「ニューロン」、計算操作では「素子」 | APPLIED | S004はneurone、S001はユニット。本文では読者理解を優先し使い分け |
| Hebbian outer-product connection | 三つの記憶パターンから結合を作る / 符号の積を足す | `Hebbian`という英語ラベルを必須にしない | APPLIED | 操作内容を本文で直接説明。正確な式はEVT-011/verification側に保持 |
| global sign inversion | 全部の符号を反転した状態 / 裏返し | 使用可 | APPLIED | 第2話から継続する作品内説明語。後世専門語を追加しない |
| residual | それ以外 / 残り / 三つ目の欄 | `residual`は本文に出さない | APPLIED | event内部の分類語を読者向け日本語へ投影 |
| mixture state | 使用しない | 使用不可 | APPLIED | 1985年以降の理論をEVT-011時点へ逆流させない |

## 重要判断

### `spurious memory`を「偽記憶」としない

1983論文が用いているのはnetworkのstable stateに対するmodel-levelの呼称である。

日本語本文で「偽記憶」と固定すると、心理学・臨床・人間の記憶現象まで同一概念であるように読めるため、第3話では採用しない。

本文では、

> 論文では、それをspurious memoriesと呼んでいる。

と原文のラベルであることを明示し、その後は「保存していない安定状態」等で意味を限定する。

### `unlearning`も無理に定訳化しない

第3話の中心はunlearning効果の再現ではない。論文タイトルに出る語として提示するだけなので、人物が「忘れさせる？」と暫定的に反応する形を維持する。

## Blocking uncertainty

なし。

具体story dateは未固定だが、S004は1983-07-14公刊、S001は1984刊行であり、現在の1984〜1985年前後という候補範囲と矛盾しない。
