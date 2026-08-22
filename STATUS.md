# 現在の状態

このファイルは詳細な正本ではなく、現在位置を示す索引です。

更新: 2026-08-23

## フェーズ

- 主目的: 小説
- 物語段階: `起 / 承 / 転`
- 本文: 第1話ドラフト `novel/chapters/001.md` 成立。採用範囲はEVT-001〜004
- 学習段階: CATCH_UP
- 研究段階: Hopfield系EXP-001〜005まで実施
- 生成方式検証: **PARTIAL PASS**。state recovery / 情報境界 / state同期 / NarrativeProjection / resolver pre-lock / cue-set pre-lock / finite state-space全列挙を確認。action selectorの完全なcontext isolationは未検証
- 公開段階: GitHub Pagesは `main /docs`。今回のBootstrap / EVT / 第1話ドラフト / EXP-003以降は未公開

## branch

現在のwork branch:

`work/story-bootstrap`

`main` には反映していない。PRも作成しない。

## 1980年代側の現在位置

開始同期点:

`BOOT-002 @ T0-1980S @ none`

current event head:

`EVT-007`

active personas:

- PER-005 — **高橋修一**。日本人、30代後半、数理工学・理論物理寄りから神経回路・連想記憶へ越境
- PER-006 — **佐伯玲子**。日本人、30代半ば〜後半、神経生理学・biophysics寄り

二人の具体的な所属機関・職位・具体年齢は未固定。研究上は互いを「高橋さん」「佐伯さん」と呼ぶ。

### EVT-001〜004

- EVT-001: 高橋が「止まることと、戻ることは同じか」「保存していないところで止まるなら、その状態は何からできている？」と記録
- EVT-002: 佐伯が`correct recall`のtargetを誰が定義するか問い返す
- EVT-003: A/Bへ等距離なcueを作り、距離 / final state / update条件 / A/B以外のstateを別記録するprotocolを作成
- EVT-004: 6-unit toy networkで、同一cue・weightsからupdate orderだけの差でA/Bへ分岐する例を観測

EVT-004は数理的一貫性は確認済みだが、具体pattern/cue/orderがoutcome前にlockされていなかったため生成方式検証上は `UNBLINDED`。第1話材料・物語eventとして保持するが、clean resolver validationには数えない。

### EVT-005〜007

- EVT-005: 6 cyclic update ordersを結果前にlock。A / B / nonstored stable Dへ分岐
- EVT-006: A/B-balanced cue全6種類 × 6 orders = 36 trialsを結果前lock。A/B/C/Dへ分岐
- EVT-007: 6-unit全64 initial states × 6 orders = 384 trialsを全列挙。Dは `-C` と再分類され、fixed pointsは `A/B/C/-A/-B/-C` の6種類だった

これらは第1話へ遡及追加しない。

## 第1話ドラフト

`novel/chapters/001.md`

採用event範囲:

`EVT-001`〜`EVT-004`

2026-08-23の改稿で、匿名の「研究者 / 同僚」表現を廃止し、

- 高橋修一
- 佐伯玲子

を本文へ反映した。

単なる名前置換ではなく、

- 高橋: dynamics、state、失敗例から考える
- 佐伯: 観測可能量、用語の射程、手続きの先行固定を要求する

という既存persona差が会話上で反復して見えるよう改稿した。

具体機関名・機種・OS・programming languageは第1話だけの都合で固定していない。

## 技術史上の人物配置

二人を日本人研究者とすること自体は、1960〜70年代から日本で神経回路・連想記憶の数理研究が存在したことと整合する。

ただし、**第1話の研究場所そのものを日本国内とはまだ固定していない**。海外滞在・共同研究環境も含め、具体的な国・都市・機関は後続の歴史調査で決める。

高橋・佐伯はいずれも実在研究者のコピーではなく、1980年代の学際的研究文化を背景にしたfictional personasとして扱う。

詳細根拠は `research/1980s-research-environment.md` と `research/pre-hopfield-background.md` を参照する。

## 生成方式検証

詳細: `notes/generation-validation.md`

- Test-001: 第1話までのstate recovery / persona境界 / NarrativeProjectionはPASS。EVT-004 resolver独立性はUNBLINDEDでINCONCLUSIVE
- Test-002: EVT-005で `ACTION_LOCKED -> commit -> RESOLVED` を実行
- Test-003: EVT-006でinitial cue集合をdeterministicに全列挙
- Test-004: EVT-007で全64 states × 6 ordersを結果前lockし、予期していなかった`D=-C`という分類修正も受理

生成方式全体はFULL PASSではなく `PARTIAL PASS` を維持する。

## 物語由来の研究分岐

- EVT-001 → Q-003 / H-003 / EXP-003 / F-003
- EVT-002 → Q-004 / H-004 / EXP-004 / F-004
- EVT-006 → Q-005 / H-005 / EXP-005 / F-005

EXP-005はFAIL、H-005はNOT_SUPPORTED。pairwise Hamming isolationがdynamics上のpair isolationを保証しないというF-005をPROVISIONALで保持する。

EVT-007からは、既存のNONSTORED_CONVERGEDにstored patternのexact negationが含まれるかという研究候補があるが、自動的にEXP-006へ進めない。

## 次に物語側で行うこと

第1話の人物密度をさらに上げる場合、次に固定すべきは名前ではなく、**所属研究環境と二人の制度上の関係**。

ただし章の都合だけで機関名を決めず、1984〜85年の実在研究文化・計算環境と照合する。

EVT-007後の局所問題:

- `x`と`-x`のfixed-point対称性をweight/update ruleからどう説明するか
- `nonstored stable`を符号反転・mixture・その他へどう分けるか
- modelの構造上の対称性とmemoryとしての意味をどう分離するか
- toy modelから計算機実装・より大きな条件へ進む必要が実際に生じるか

## 未確定

- 高橋修一 / 佐伯玲子の具体年齢
- 二人は日本人として固定したが、第1話時点の国・都市・所属機関は未確定
- 具体年月日
- 具体的な計算機・言語
- 二人の正式な所属関係・上下関係
- 現代側最初のevent
- 第2話以降の切れ目

必要になるまで一括固定しない。
