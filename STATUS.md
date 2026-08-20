# 現在の状態

このファイルは詳細な正本ではなく、現在位置を示す索引です。

更新: 2026-08-21

## フェーズ

- 主目的: 小説
- 物語段階: `起 / 承 / 転`
- 本文: 第1話ドラフト `novel/chapters/001.md` が成立
- 学習段階: CATCH_UP
- 研究段階: Hopfield系EXP-001〜004まで実施
- 公開段階: GitHub Pagesは `main /docs`。今回のBootstrap / EVT / 第1話ドラフトは未公開

## branch

現在のwork branch:

`work/story-bootstrap`

`main` には反映していない。PRも作成しない。

## 1980年代側の現在位置

開始同期点:

`BOOT-002 @ T0-1980S @ none`

現在のevent head:

`EVT-004`

現在active:

- PER-005 — 1980年代研究者
- PER-006 — 実験神経科学寄りの同僚

### EVT-001

PER-005が、

- 「止まることと、戻ることは同じか」
- 「保存していないところで止まるなら、その状態は何からできている？」

という問いを研究ノートへ残した。

### EVT-002

PER-005がEVT-001の問題をPER-006へ共有。

PER-006は、実験者がtargetを知っていることと、network自身に一意な`correct`があることは別ではないかと問い返した。

PER-005は、

- 「原像を知っているのは誰だ」
- 「手掛かりが二つの記憶の間にあるなら、戻る先は最初から一つなのか」

という問いを追加した。

このeventでPER-006を、必要になった時点から独立ペルソナとして生成した。

### EVT-003

PER-005 / PER-006は、二つのstored patterns A/Bで異なるunitの半分ずつを使い、A/Bへ同じbit差数を持つcueを作るprotocol sketchを成立させた。

同時に、

- `等距離` と `dynamics上の中立` を同一視しない
- cueからA/Bへの距離
- final state
- update条件
- A/B以外へ停止したstate

を分けて記録する方針を成立させた。

### EVT-004

PER-005 / PER-006は、6 unit・3 stored patternsの紙上networkでEVT-003のprotocolを初めて具体計算へ適用した。

A/Bへ2 bitずつ離れた同一cue、同一weights、同一の非同期更新規則を使い、update orderだけを変えたところ、

- order α → A
- order β → B

となり、双方がstable stateであることを確認した。

PER-005は、

- 「手掛かりが同じでも、戻り先は一つとは限らない」
- 「想起の結果だけを見て原像を逆算してよいのか」

という問いを追加した。

これは6-unitの一例であり、memory一般・生物学的記憶・頻度一般へ一般化していない。

物語人物は現代側EXP-004の122/200、4000 runs等を知らない。

## 第1話ドラフト

`novel/chapters/001.md`

採用event範囲:

`EVT-001`〜`EVT-004`

EVT-004で、EVT-001〜003まで蓄積した「correct recall」の前提が具体例によって維持できなくなり、新しい問いが次の初期条件として立ち上がったため、一つの読書単位として自然な切れ目が成立した。

第1話を成立させるためにEVT-004を起こしたのではない。EVT-003時点のPER-005のGoalsとPER-006の観測要求から、最小の紙上計算を行った結果としてEVT-004が成立した。

## 小説と研究の分離

小説を実験レポート風にしない。

運用:

```text
人物と世界が動く
    ↓
実際に出た言葉・観測・違和感
    ↓
検証可能なら研究側へ分岐
    ↓
Q / H / EXP
    ↓
research/reports/EXP-xxx.md
```

- 実験実行正本: `experiments/`
- 研究レポート: `research/reports/`
- 研究入口: `research/README.md`
- 知見: `research/findings.md`
- 小説状態: `novel/`

一話 = 一実験とはしない。

研究結果は、物語内人物がその時代・環境で実際に観測した場合だけ、その人物状態へ戻す。

## 物語由来の研究分岐

### EVT-001 → EXP-003

問い:

「保存していないところで止まるなら、その状態は何からできている？」

`EXP-003-hopfield-mixture-structure`

- 判定: PASS
- EXP-002の`NONSTORED_CONVERGED` 510件を再解析
- 3-pattern majority mixture exact match: 1件
- F-003: PROVISIONAL

### EVT-002 → EXP-004

問い:

「二つの記憶が同じくらいもっともらしいcueなら、どちらが正解なのか」

`EXP-004-hopfield-ambiguous-cue`

- 判定: PASS
- N=100, P=5
- pattern seeds: 1982 / 1983 / 1984
- 有効pair: 20
- balanced cue: 200
- update-order runs: 4000
- A/B等距離違反: 0
- 同じcueからA/B両方へexact recallしたBIDIRECTIONAL cue: 122 / 200
- F-004: PROVISIONAL

EVT-003 / EVT-004から新しいQ / H / EXPは追加していない。

EVT-004はQ-004と同種の論点に重なるが、物語人物が独立に得た6-unit紙上例であり、現代EXP-004の結果を未来知識として注入していない。

## 最新研究ID

- Q-001: ANSWERED
- H-001: SUPPORTED（宣言条件に限定）
- EXP-001: PASS
- F-001: PROVISIONAL
- Q-002: ANSWERED
- H-002: SUPPORTED（有限gridに限定）
- EXP-002: PASS
- F-002: PROVISIONAL
- Q-003: ANSWERED
- H-003: SUPPORTED（EXP-002有限trial群に限定）
- EXP-003: PASS
- F-003: PROVISIONAL
- Q-004: ANSWERED
- H-004: SUPPORTED（EXP-004有限条件に限定）
- EXP-004: PASS
- F-004: PROVISIONAL

## 背景調査

- `research/pre-hopfield-background.md`
- `research/1980s-research-environment.md`

1984年後半は開始時期の有力候補だが、具体月・機関・人物名・計算機環境はまだCanon固定していない。

## 次に物語側で行うこと

EXP-005を研究都合で自動生成しない。

EVT-004後のPER-005 / PER-006を、その現在状態から再び動かす。

現在の局所問題:

- 6-unitの一例をどこまで一般化してよいか
- `correct recall`をfinal state以外の何と結び付けるか
- A/B以外のstable stateをどう分類するか
- 紙上計算から計算機実装へ進む必要が実際に生じるか
- その場合、1980年代の具体的計算環境をどこまで固定する必要があるか

次のeventで実際に新しい言葉・観測・制約が生じた場合だけ、次の研究分岐を作る。

## 未確定

- PER-005 / PER-006の氏名・年齢
- 国・都市・所属機関
- 具体年月日
- 具体的な計算機・言語
- 二人の正式な所属関係・上下関係
- 紙上例の次に行う具体的な計算・実験
- 現代側最初のevent
- 第2話以降の切れ目

これらは必要になるまで一括固定しない。