# 現在の状態

このファイルは詳細な正本ではなく、現在位置を示す索引です。

更新: 2026-08-20

## フェーズ

- 主目的: 小説
- 物語段階: `起 / 起`
- 本文: 0話。まだ公開本文は作っていない
- 学習段階: CATCH_UP
- 研究段階: Hopfield系EXP-001〜003まで実施
- 公開段階: GitHub Pagesは `main /docs`。今回のBootstrap / EVT / research reportは未公開

## branch

現在のwork branch:

`work/story-bootstrap`

`main` にはまだ反映していない。

## 1980年代側の現在位置

開始同期点:

`BOOT-002 @ T0-1980S @ none`

現在のevent head:

`EVT-001`

### EVT-001

`novel/events/EVT-001-stopping-is-not-returning.md`

PER-005が当時の連想記憶・spurious memoryをめぐる問題設定を比較し、研究ノートに次の問いを残した。

- 「止まることと、戻ることは同じか」
- 「保存していないところで止まるなら、その状態は何からできている？」

これは最初の意味のある物語状態差分。

まだ具体的な実験条件、実験結果、共同研究者との相互作用は物語世界で成立していない。

PER-005の更新状態:

`novel/state/personas/PER-005.md`

世界状態:

`novel/state/world.md`

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

## 物語由来の最初の研究分岐

EVT-001の「その状態は何からできている？」からQ-003 / H-003 / EXP-003を現実研究側へ切り出した。

### EXP-003

`experiments/EXP-003-hopfield-mixture-structure/`

状態: COMPLETED

判定: PASS

EXP-002の960 trialsを再生成し、`NONSTORED_CONVERGED` 510件を再確認。

事前判定対象:

- 3-pattern majority mixture exact match: **1件**

探索的観測:

- 363 / 510件（約71.2%）でnearest stored patternよりnearest 3-pattern mixtureの方が近かった

この71.2%は事前PASS条件ではなく、mixture attractorとしての同定でもない。

研究レポート:

`research/reports/EXP-003.md`

Finding:

`F-003: PROVISIONAL`

重要: EXP-003の結果は1980年代のPER-005へ直接与えていない。PER-005の物語内KnowledgeはEVT-001で本人が観測した範囲だけ。

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

## 背景調査

- `research/pre-hopfield-background.md`
- `research/1980s-research-environment.md`

1984年後半は開始時期の有力候補だが、具体月・機関・人物名・計算機環境はまだCanon固定していない。

## 次に物語側で行うこと

研究側の次候補を自動で実行しない。

まずEVT-001後のPER-005を動かす。

候補となる行動はPER-005自身の現在状態から生成する。

- 自分の問いを実行可能な操作へ落とそうとする
- 文献上のspurious state / unlearningをさらに確認する
- 計算を始めるため具体的な研究環境が必要になる
- 他者の独立判断が必要になった場合のみPER-006以降を生成する

そこで実際に新しい言葉・観測・問題が生じた場合だけ、次の研究分岐を作る。

## 未確定

- PER-005の氏名・年齢
- 国・都市・所属機関
- 具体年月日
- 具体的な計算機・言語
- 最初に相互作用する他者
- 第1話の終了点
- 現代側最初のevent

これらは必要になるまで一括固定しない。
