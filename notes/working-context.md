# 作業コンテキスト

更新: 2026-08-20

このファイルは別セッションへ現在の探索状態を引き継ぐ公開可能な作業記憶。正本ではない。

## 主目的

小説が主役。

研究は、小説内で実際に生じた技術的な疑問・語・違和感を必要に応じて現実側で検証し、作品の現実性を上げるために使う。

小説を実験レポート風にしない。

## 現在の物語状態

1980年代側:

- Bootstrap: `BOOT-002 @ T0-1980S @ none`
- current event head: `EVT-002`
- active personas: PER-005 / PER-006
- current structure: `起 / 承`

### EVT-001

PER-005:

- 「止まることと、戻ることは同じか」
- 「保存していないところで止まるなら、その状態は何からできている？」

### EVT-002

PER-005がEVT-001の問いをPER-006へ共有。

PER-006は、実験者がtargetを知っていることと、network自身に一意な`correct`があることは別ではないかと問い返した。

PER-005:

- 「原像を知っているのは誰だ」
- 「手掛かりが二つの記憶の間にあるなら、戻る先は最初から一つなのか」

PER-006は、この相互作用で独立状態を追う必要が生じたため初めて生成された。

物語世界では具体的なbalanced-cue実験結果はまだ発生していない。

## 研究分岐ルール

```text
物語中の実際の言葉・観測
    ↓
検証可能か判断
    ↓
Q / H / EXP
    ↓
research/reports/EXP-xxx.md
    ↓
research/findings.md
```

- 一話 = 一実験ではない
- 実験番号と話数を対応させない
- 派生実験は判定対象が変わるなら別EXP
- 実験は `experiments/`、研究としての読み物は `research/reports/`
- 現代研究結果を過去人物へ未来知識として注入しない

詳細: `research/README.md`, `experiments/README.md`, `research/reports/README.md`

## 物語由来の現実研究

### EVT-001 → Q-003 / H-003 / EXP-003

- 対象: EXP-002の`NONSTORED_CONVERGED` 510件
- 3-pattern majority mixture exact match: 1件
- 判定: PASS
- H-003: SUPPORTED（有限trial群に限定）
- F-003: PROVISIONAL

探索的に363/510件でnearest storedよりnearest 3-pattern mixtureの方が近かったが、mixture attractor同定とはしない。

### EVT-002 → Q-004 / H-004 / EXP-004

- N=100, P=5
- pattern seeds: 1982 / 1983 / 1984
- 有効pair: 20
- balanced cue: 200
- update-order runs: 4000
- A/B Hamming等距離違反: 0
- BIDIRECTIONAL cue: 122 / 200
- 判定: PASS
- H-004: SUPPORTED（有限条件に限定）
- F-004: PROVISIONAL

最初のBIDIRECTIONAL例:

- pair Hamming distance: 54
- cue→A = 27
- cue→B = 27
- 同一cue・同一weightsの20 runsでA exact 2、B exact 11、nonstored converged 7

事前PASS条件はBIDIRECTIONALが1件以上存在すること。122/200は探索的集計であり一般的頻度ではない。

研究レポート:

- `research/reports/EXP-003.md`
- `research/reports/EXP-004.md`

重要: EXP-003 / EXP-004の結果をPER-005 / PER-006は知らない。

## 次の物語側作業

EXP-005を研究都合で先回りして自動実行しない。

EVT-002後のPER-005 / PER-006を、その人物のKnowledge / Beliefs / Goals / Relations / 状況から再び動かす。

現在の自然な局所問題:

- 二つのstored patternsへ同程度に適合するcueを、物語世界内でどう操作化するか
- `correct recall`を誰の基準で判定するか
- PER-005のdynamics中心の見方と、PER-006の観測・課題設定中心の見方をどう両立するか
- 具体計算を始める段階で、研究環境・計算機・第三者の助けが本当に必要になるか

そこで実際に生じた相互作用だけを次eventへする。

## 未確定

- 具体年月日
- 国・都市・所属研究機関
- PER-005 / PER-006の氏名・年齢
- 計算機・言語・端末
- 二人の正式な所属関係・上下関係
- 物語世界内で最初に実行する具体的な計算
- 第1話の終了点
- 現代側最初のevent

必要になる前に一括固定しない。

## 長期探索仮説

輪廻・同一認識主体・NNによる顕在化・情報量による出現確率等はCanonでも現実科学のFindingでもない。

競合説明として模倣、統計的再構成、一般的認知収束、selection bias、pattern over-detection等を残す。

## セキュリティ境界

生のAI内部推論、内部指示、credential、token、秘密値、公開不能な個人情報を保存しない。
