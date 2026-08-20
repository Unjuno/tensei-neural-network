# 現在の状態

このファイルは詳細な正本ではなく、現在位置を示す索引です。

更新: 2026-08-21

## フェーズ

- 主目的: 小説
- 物語段階: `起 / 承 / 転`
- 本文: 第1話ドラフト `novel/chapters/001.md` を現在のポリシーで再投影済み
- 学習段階: CATCH_UP
- 研究段階: Hopfield系EXP-001〜004まで実施
- 生成方式検証: **PARTIAL PASS**。状態復元・情報境界・state同期・NarrativeProjectionは確認、resolver結果独立性は未確認
- 公開段階: GitHub Pagesは `main /docs`。今回のBootstrap / EVT / 第1話ドラフトは未公開

## branch

現在のwork branch:

`work/story-bootstrap`

`main` には反映していない。PRも作成しない。

## 1980年代側の現在位置

開始同期点:

`BOOT-002 @ T0-1980S @ none`

current event head:

`EVT-004`

active personas:

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

同時に、`等距離` と `dynamics上の中立` を同一視せず、距離・final state・update条件・A/B以外のstateを分けて記録する方針を成立させた。

### EVT-004

PER-005 / PER-006は、6 unit・3 stored patternsの紙上networkでEVT-003のprotocolを具体計算へ適用した。

同一cue・同一weights・同一の非同期更新規則でupdate orderだけを変え、

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

`BOOT-002`の導入背景と成立済みeventだけを材料に、現在のNarrativeProjection規則で再構成した。新しいeventやpersona stateは追加していない。

研究レポート形式ではなく、人物の問い・会話・protocol・紙上計算を小説として描写する。

氏名、年齢、性別・性別代名詞、国籍、所属、具体機材等の未確定な恒常属性は本文で補っていない。

## 第1話生成テストの評価

詳細:

`notes/generation-validation.md`

### 確認できたもの

- repoからのstate recovery: PASS
- stale indexから直接event/stateへの復元: PASS
- persona情報境界: PASS
- world / persona state同期: PASS
- personaを必要時だけ追加: PASS
- 小説 / 研究レポート分離: PASS
- 一話=一実験の回避: PASS
- event群から第1話へのNarrativeProjection: PASS
- EVT-004の記載計算の数理的一貫性: PASS

### 未確認のもの

**environment resolverの結果独立性: INCONCLUSIVE**

理由:

EVT-004より前に作者側・生成側はEXP-004で同種のupdate-order依存を知っていたが、EVT-004のA/B/C、cue、order α/β、selection / stopping ruleは結果解決前にrepo上でlockされていない。

したがって、人物への未来知識漏洩は防げていても、resolver側が反例の出る条件を選んだselection biasは排除できない。

EVT-004は `Resolution provenance: UNBLINDED` とする。

- 物語eventとしては保持
- 数理的具体例としては保持
- 第1話ドラフトの材料としては保持
- cleanなresolver独立性の検証証拠には数えない

## 次の生成方式テスト

次の重要なoutcomeを解決するときは、`novel/events/README.md` の二段階手順を使う。

1. personaの現在状態だけから次の行動を生成
2. outcome-sensitiveな具体条件・選択規則・trial範囲・stopping ruleを `ACTION_LOCKED` としてeventへ記録
3. **結果を書く前にcommit**
4. locked条件をworld resolverへ渡して解決
5. 平凡・失敗・不都合な結果も含め、そのままeventへ記録
6. 結果を見て条件を差し替えない

生成contextがpersonaには見えないEXP結果を既に知っている場合、具体条件はstory-visibleな情報だけからのdeterministic ruleで固定するか、結果知識を与えない別contextで選択する。

成功条件は「面白い結果が出る」ではなく、**どの結果でもそのまま受け入れて次状態へ進めること**。

## 小説と研究の分離

- 実験実行正本: `experiments/`
- 研究レポート: `research/reports/`
- 研究入口: `research/README.md`
- 知見: `research/findings.md`
- 小説状態: `novel/`

一話 = 一実験とはしない。

研究結果は、物語内人物がそのstory timeで実際に観測した場合だけ、その人物状態へ戻す。

## 物語由来の研究分岐

### EVT-001 → EXP-003

- 判定: PASS
- 3-pattern majority mixture exact match: 1件
- F-003: PROVISIONAL

### EVT-002 → EXP-004

- 判定: PASS
- N=100, P=5
- balanced cue: 200
- update-order runs: 4000
- BIDIRECTIONAL cue: 122 / 200
- F-004: PROVISIONAL

EVT-003 / EVT-004から重複する新しいQ / H / EXPは追加していない。

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

EVT-004後のPER-005 / PER-006を現在状態から動かす。ただし、次の重要な結果解決は上記 `ACTION_LOCKED` 手順を必須とする。

現在の局所問題:

- 6-unitの一例をどこまで一般化してよいか
- `correct recall`をfinal state以外の何と結び付けるか
- A/B以外のstable stateをどう分類するか
- 紙上計算から計算機実装へ進む必要が実際に生じるか

## 未確定

- PER-005 / PER-006の氏名・年齢・性別
- 国・都市・所属機関
- 具体年月日
- 具体的な計算機・言語
- 二人の正式な所属関係・上下関係
- 紙上例の次に行う具体的な計算・実験
- 現代側最初のevent
- 第2話以降の切れ目

これらは必要になるまで一括固定しない。