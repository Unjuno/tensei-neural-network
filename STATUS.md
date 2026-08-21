# 現在の状態

このファイルは詳細な正本ではなく、現在位置を示す索引です。

更新: 2026-08-21

## フェーズ

- 主目的: 小説
- 物語段階: `起 / 承 / 転`
- 本文: 第1話ドラフト `novel/chapters/001.md` 成立。採用範囲はEVT-001〜004のまま
- 学習段階: CATCH_UP
- 研究段階: Hopfield系EXP-001〜004まで実施
- 生成方式検証: **PARTIAL PASS**。state recovery / 情報境界 / state同期 / NarrativeProjection / resolver pre-lockは確認。action selectorのcontext isolationは未検証
- 公開段階: GitHub Pagesは `main /docs`。今回のBootstrap / EVT / 第1話ドラフトは未公開

## branch

現在のwork branch:

`work/story-bootstrap`

`main` には反映していない。PRも作成しない。

## 1980年代側の現在位置

開始同期点:

`BOOT-002 @ T0-1980S @ none`

current event head:

`EVT-005`

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

人物は現代側EXP-004の122/200、4000 runs等を知らない。

ただし生成方式検証上、EVT-004は具体pattern / cue / orderをoutcome前にlockした記録がないため `Resolution provenance: UNBLINDED`。数理例・物語event・第1話材料として保持するが、cleanなresolver独立性の証拠には数えない。

### EVT-005

EVT-004と同じ6-unit networkについて、PER-005 / PER-006はorder選択を後から都合よく変えないため、自然順序 `(1,2,3,4,5,6)` の全6 cyclic rotationsを結果前に固定した。

Action-lock commit:

`59ff6530d202b79834afbe8ffdceee1256437315`

固定後に6本をすべて解決した結果:

- r1 → A
- r2 → D
- r3 → B
- r4 → B
- r5 → D
- r6 → D

D:

```text
(+1, +1, +1, +1, -1, +1)
```

DはA/B/Cのどれとも一致しないstable state。

- Hamming(D, A) = 2
- Hamming(D, B) = 2
- Hamming(D, C) = 6

PER-005は、

- 「二つの原像のどちらへ戻るか、では足りない」
- 「戻り先そのものが、原像の一覧の外にもある」

という局所問題へ進んだ。

PER-006はDをmemoryとは呼ばず、`nonstored stable state`として扱うよう要求した。

Resolution provenance: `LOCKED`。

## 第1話ドラフト

`novel/chapters/001.md`

採用event範囲:

`EVT-001`〜`EVT-004`

EVT-005が後から成立したことを理由に、第1話へ自動追加していない。

`BOOT-002`の導入背景と成立済みeventだけを材料に、現在のNarrativeProjection規則で再構成済み。

- 研究レポート形式にしない
- event/stateにない未来因果を追加しない
- 氏名、年齢、性別・性別代名詞、国籍、所属、具体機材等の未確定な恒常属性を補わない
- 本文の再投影によってworld/persona stateやevent headを動かさない

## 生成方式検証

詳細:

`notes/generation-validation.md`

### Test-001

確認できた:

- repoからのstate recovery: PASS
- stale indexから直接event/stateへの復元: PASS
- persona情報境界: PASS
- world / persona state同期: PASS
- personaを必要時だけ追加: PASS
- 小説 / 研究レポート分離: PASS
- 一話=一実験の回避: PASS
- event群から第1話へのNarrativeProjection: PASS
- EVT-004の記載計算の数理的一貫性: PASS

未確認だった:

- EVT-004 resolver結果独立性: `INCONCLUSIVE / UNBLINDED`

### Test-002

`EVT-005` で `ACTION_LOCKED → commit → resolver → RESOLVED` を実行。

確認:

- outcome前のaction/condition外部化: PASS
- 6 cyclic ordersの事前固定: PASS
- stopping / inclusion rule固定: PASS
- lock後の条件差し替えなし: PASS
- A/B以外のDを削除せず保持: PASS
- world / PER-005 / PER-006へ結果を同期: PASS
- resolver pre-lock mechanism: **PASS**

ただしTest-002は、action selectorそのものが作者側既知情報から完全に隔離されていたことまでは証明しない。

## 次の生成方式テスト

より強い検証を行う場合、次の重要なaction / parameter selectionを、

- 作者側EXP結果を読まない別contextで決める

または

- story-visible情報から一意に決まるdeterministic ruleだけで決める

ようにし、selector-levelの独立性を確認する。

成功条件は「面白い結果が出る」ではなく、**結果を知らずに選んだactionから生じたoutcomeを、そのまま物語へ受け入れること**。

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

EVT-003 / EVT-004 / EVT-005から重複する新しいQ / H / EXPは追加していない。

EVT-005のDは、nonstored stable stateとしてQ-003 / EXP-003、update-order依存としてQ-004 / EXP-004と論点が重なるため、現時点では新規EXPを作らない。

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

EVT-005後のPER-005 / PER-006を現在状態から動かす。

現在の局所問題:

- DがA/Bの単純な中間なのか、別種の安定構造なのか
- stored集合外のstateが存在するとき`correct recall`をどう記述するか
- 紙上計算から計算機実装へ進む必要が実際に生じるか
- 次の比較で何を固定し、何を変えるか

outcome-sensitiveな次eventではACTION_LOCKEDを維持する。

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