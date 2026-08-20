# 現在の状態

このファイルは詳細な正本ではなく、現在位置を示す索引です。

更新: 2026-08-20

## フェーズ

- 主目的: 小説
- 物語段階: `起 / 承`
- 本文: 0話。まだ公開本文は作っていない
- 学習段階: CATCH_UP
- 研究段階: Hopfield系EXP-001〜004まで実施
- 公開段階: GitHub Pagesは `main /docs`。今回のBootstrap / EVT / research reportは未公開

## branch

現在のwork branch:

`work/story-bootstrap`

`main` にはまだ反映していない。

## 1980年代側の現在位置

開始同期点:

`BOOT-002 @ T0-1980S @ none`

現在のevent head:

`EVT-002`

現在active:

- PER-005 — 1980年代研究者
- PER-006 — 実験神経科学寄りの同僚

### EVT-001

`novel/events/EVT-001-stopping-is-not-returning.md`

PER-005が、

- 「止まることと、戻ることは同じか」
- 「保存していないところで止まるなら、その状態は何からできている？」

という問いを研究ノートへ残した。

### EVT-002

`novel/events/EVT-002-who-defines-correct-recall.md`

PER-005がEVT-001の問題をPER-006へ共有。

PER-006は、実験者がtargetを知っていることと、network自身に一意な`correct`があることは別ではないかと問い返した。

PER-005は、

- 「原像を知っているのは誰だ」
- 「手掛かりが二つの記憶の間にあるなら、戻る先は最初から一つなのか」

という問いを追加した。

このeventでPER-006を、必要になった時点から独立ペルソナとして生成した。

物語世界内では、balanced cueの具体実験やEXP-004の数値結果はまだ観測されていない。

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
独立した研究レポート
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

探索的な363/510 near-mixtureは生成機構の同定とは扱わない。

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

事前PASS条件はBIDIRECTIONALが1件以上存在すること。122/200は探索的集計であり一般的頻度とは扱わない。

研究レポート:

- `research/reports/EXP-003.md`
- `research/reports/EXP-004.md`

重要: EXP-003 / EXP-004の結果をPER-005 / PER-006へ直接与えていない。

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

EVT-002後のPER-005 / PER-006を、その現在状態から再び動かす。

現在の局所問題:

- 曖昧なcueを物語世界内でどう定義するか
- `correct recall`を誰の基準で判定するか
- PER-006が要求する観測可能な基準と、PER-005のdynamics中心の見方をどう両立するか

次のeventで実際に新しい言葉・観測・制約が生じた場合だけ、次の研究分岐を作る。

## 未確定

- PER-005 / PER-006の氏名・年齢
- 国・都市・所属機関
- 具体年月日
- 具体的な計算機・言語
- 二人の正式な所属関係・上下関係
- 物語世界内で最初に実行する具体的な計算・実験
- 第1話の終了点
- 現代側最初のevent

これらは必要になるまで一括固定しない。
