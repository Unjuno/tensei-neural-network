# 作業コンテキスト

更新: 2026-08-21

このファイルは別セッションへ現在の探索状態を引き継ぐ公開可能な作業記憶。正本ではない。

## 主目的

小説が主役。

研究は、小説内で実際に生じた技術的な疑問・語・違和感を必要に応じて現実側で検証し、作品の現実性を上げるために使う。

小説を実験レポート風にしない。

## 現在の物語状態

1980年代側:

- Bootstrap: `BOOT-002 @ T0-1980S @ none`
- current event head: `EVT-004`
- active personas: PER-005 / PER-006
- current structure: `起 / 承 / 転`
- 第1話ドラフト: `novel/chapters/001.md`

### EVT-001

PER-005:

- 「止まることと、戻ることは同じか」
- 「保存していないところで止まるなら、その状態は何からできている？」

### EVT-002

PER-006が、実験者がtargetを知っていることとnetwork自身に一意な`correct`があることは別ではないかと問い返した。

PER-005:

- 「原像を知っているのは誰だ」
- 「手掛かりが二つの記憶の間にあるなら、戻る先は最初から一つなのか」

PER-006はこの相互作用で初めて独立persona化。

### EVT-003

PER-005 / PER-006はA/Bへ同じbit差数を持つcueのprotocol sketchを作った。

- 等距離 = dynamics上の中立、とは扱わない
- cueからA/Bへの距離
- final state
- update条件
- A/B以外のstate

を分けて記録する方針が成立。

### EVT-004

6-unit・3-patternの紙上networkで、同一cue・同一weights・同一非同期更新規則から、update orderだけを変えてA/Bへ別々にstable到達する例をPER-005 / PER-006が観測した。

PER-005:

- 「手掛かりが同じでも、戻り先は一つとは限らない」
- 「想起の結果だけを見て原像を逆算してよいのか」

現代側EXP-004の122/200、4000 runs等を人物へ与えていない。

## 第1話

`novel/chapters/001.md`

採用event範囲:

`EVT-001`〜`EVT-004`

2026-08-21、`BOOT-002`の導入背景と成立済みeventだけを材料に、現在のNarrativeProjection規則で本文を再構成した。

- 研究レポート形式にしない
- event/stateにない未来因果を追加しない
- 氏名、年齢、性別・性別代名詞、国籍、所属、具体機材等の未確定な恒常属性を補わない
- 第1話本文の再投影によってworld/persona stateやevent headは動かさない

## 生成方式検証

詳細:

`notes/generation-validation.md`

第1話生成テストは **PARTIAL PASS**。

確認できた:

- repoからのstate recovery
- stale indexの検出
- personaごとの情報境界
- world / persona state同期
- personaを必要時だけ追加
- 一話=一実験を回避
- 小説 / research reportを分離
- event群から第1話へ投影
- EVT-004の記載計算自体の数理的一貫性

未確認:

**environment resolverの結果独立性**。

EVT-004より前に生成側はEXP-004でupdate-order依存を知っていた。一方、EVT-004のA/B/C、cue、order α/β、selection / stopping ruleは結果を見る前にrepoへlockされていない。

したがって、人物への未来知識漏洩とは別に、resolver側のselection biasを排除できない。

EVT-004 Resolution provenance:

`UNBLINDED`

EVT-004は物語event・数理例・第1話材料として保持するが、cleanなresolver独立性の証拠には数えない。

## 次の重要ルール: ACTION_LOCKED

次の重要なoutcomeを解決するときは `novel/events/README.md` と `novel/environment.md` に従う。

1. 現在のpersona stateとstory-visible情報だけから行動を生成
2. outcome-sensitiveな具体条件または選択規則をeventへ書く
3. trial集合 / update rule / stopping / inclusion ruleも固定
4. resolverが使ってよい情報と、action selectionへ使ってはいけない作者側情報を明記
5. event状態を `ACTION_LOCKED` として**結果を書く前にcommit**
6. そのcommit後にresolverが結果を解決
7. locked条件を結果を見て変更しない
8. 平凡・失敗・不都合な結果も採用する

生成contextがpersonaには見えないEXP結果を既に知っている場合、具体条件はstory-visible情報だけからのdeterministic ruleで固定するか、結果知識を与えない別contextで選ぶ。

clean validationの成功条件は「面白い結果」ではなく、**どんな結果でも差し替えず、その結果から次状態へ進めること**。

## 研究分岐

### EVT-001 → Q-003 / H-003 / EXP-003

- 3-pattern majority mixture exact match: 1件
- 判定: PASS
- F-003: PROVISIONAL

### EVT-002 → Q-004 / H-004 / EXP-004

- N=100, P=5
- balanced cue: 200
- update-order runs: 4000
- BIDIRECTIONAL cue: 122 / 200
- 判定: PASS
- F-004: PROVISIONAL

EVT-003 / EVT-004から重複EXPは作っていない。

## 次の物語側作業

EXP-005を研究都合で自動生成しない。

EVT-004後のPER-005 / PER-006を現在状態から動かす。

現在の自然な局所問題:

- 6-unitの一例をどこまで一般化してよいか
- `correct recall`をfinal state以外の何と結び付けるか
- A/B以外のstable stateをどう扱うか
- 紙上計算から計算機実装へ進む必要が本当に生じるか

重要なoutcomeを伴う次eventは、上記ACTION_LOCKED手順を使う。

## 未確定

- 具体年月日
- 国・都市・所属研究機関
- PER-005 / PER-006の氏名・年齢・性別
- 計算機・言語・端末
- 二人の正式な所属関係・上下関係
- 紙上例の次に実行する具体的計算
- 現代側最初のevent
- 第2話以降の終了点

必要になる前に一括固定しない。

## 長期探索仮説

輪廻・同一認識主体・NNによる顕在化・情報量による出現確率等はCanonでも現実科学のFindingでもない。

競合説明として模倣、統計的再構成、一般的認知収束、selection bias、pattern over-detection等を残す。

## セキュリティ境界

生のAI内部推論、内部指示、credential、token、秘密値、公開不能な個人情報を保存しない。