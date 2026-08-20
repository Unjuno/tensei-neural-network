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
- current event head: `EVT-001`
- active persona: PER-005
- current structure: `起 / 起`

EVT-001:

`novel/events/EVT-001-stopping-is-not-returning.md`

PER-005が研究ノートに、

- 「止まることと、戻ることは同じか」
- 「保存していないところで止まるなら、その状態は何からできている？」

と残した。

まだ物語世界では具体的な実験結果、研究機関、計算機、共同研究者は固定していない。

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

## EVT-001から派生した現実研究

Q-003 / H-003 / EXP-003。

EXP-003:

- Parent: EXP-002
- 対象: `NONSTORED_CONVERGED` 510件
- 3-pattern majority mixtureとのexact matchを事前判定
- 再生成: 960/960 trials、分類数EXP-002と一致
- exact 3-pattern mixture match: 1件
- 判定: PASS
- H-003: SUPPORTED（有限trial群に限定）
- F-003: PROVISIONAL

探索的結果:

- 363/510件（約71.2%）でnearest stored patternよりnearest 3-pattern mixtureの方が近い

これは事前基準ではなく、mixture attractorの同定でもない。

研究レポート:

`research/reports/EXP-003.md`

重要: このEXP-003結果をPER-005は知らない。

## 次の物語側作業

研究側の候補を先回りして自動実行しない。

EVT-001後のPER-005を、その人物のKnowledge / Beliefs / Goals / 状況から再び動かす。

次の行動候補は固定しないが、現在状態から自然に可能なのは:

- 「何からできているか」を観測可能な操作へ落とそうとする
- 文献をさらに比較する
- 計算を始めるため具体的な研究環境が必要になる
- 他者の独立判断が必要ならPER-006以降を生成する

実際に生じた相互作用だけを次eventへする。

## 未確定

- 具体年月日
- 国・都市・所属研究機関
- PER-005の氏名・年齢
- 計算機・言語・端末
- 最初の共同研究者
- 第1話の終了点
- 現代側最初のevent

必要になる前に一括固定しない。

## 長期探索仮説

輪廻・同一認識主体・NNによる顕在化・情報量による出現確率等はCanonでも現実科学のFindingでもない。

競合説明として模倣、統計的再構成、一般的認知収束、selection bias、pattern over-detection等を残す。

## セキュリティ境界

生のAI内部推論、内部指示、credential、token、秘密値、公開不能な個人情報を保存しない。
