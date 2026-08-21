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
- current event head: `EVT-005`
- active personas: PER-005 / PER-006
- current structure: `起 / 承 / 転`
- 第1話ドラフト: `novel/chapters/001.md`
- 第1話採用範囲: `EVT-001`〜`EVT-004`

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

人物への現代EXP結果漏洩はない。

ただし生成方式検証上、具体条件がoutcome前にlockされていないためResolution provenanceは `UNBLINDED`。cleanなresolver独立性の証拠には数えない。

### EVT-005

EVT-004の弱点を踏まえ、同じ6-unit networkについてunit番号の自然順序 `(1,2,3,4,5,6)` の全6 cyclic rotationsを結果前に固定した。

Action-lock commit:

`59ff6530d202b79834afbe8ffdceee1256437315`

locked条件を変えず6本をすべて解決:

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

PER-005:

- 「二つの原像のどちらへ戻るか、では足りない」
- 「戻り先そのものが、原像の一覧の外にもある」

PER-006はDをmemoryと呼ばず、nonstored stable stateとして扱う。

Resolution provenance: `LOCKED`。

## 第1話

`novel/chapters/001.md`

採用event範囲は `EVT-001`〜`EVT-004` のまま。

EVT-005が後から成立したことを理由に第1話へ追加しない。

本文は現在のNarrativeProjection規則に合わせ、未確定だったPER-005の性別を「彼」と補っていた箇所を修正済み。

本文では:

- 研究レポート形式にしない
- event/stateにない未来因果を追加しない
- 氏名、年齢、性別・性別代名詞、国籍、所属、具体機材等の未確定な恒常属性を補わない

## 生成方式検証

詳細:

`notes/generation-validation.md`

### Test-001

PASS:

- repoからstate recovery
- stale index検出
- persona情報境界
- world / persona state同期
- persona必要時生成
- 一話=一実験回避
- 小説 / research report分離
- NarrativeProjection
- EVT-004の数理的一貫性

INCONCLUSIVE:

- EVT-004のresolver結果独立性

理由: 生成側が同種現象を既知で、具体pattern / cue / order / selection ruleが結果前にlockされていなかった。

### Test-002

EVT-005で初めて、

```text
ACTION_LOCKED
→ commit
→ resolver
→ locked条件を変えず全結果を受理
```

を実行。

判定:

- resolver pre-lock mechanism: PASS
- 不都合・非期待結果保持: PASS
- state同期: PASS

ただし、action selector自体を作者側EXP知識から隔離したcontext isolationは未検証。

## 次の重要ルール

outcome-sensitiveな重要eventは、結果前に:

1. personaのstory-visible stateから行動を決める
2. 具体条件またはdeterministic selection ruleを固定
3. trial / stopping / inclusion ruleを固定
4. `ACTION_LOCKED` としてcommit
5. commit後にresolverで解決
6. 結果を見て条件を差し替えない

さらに強い検証が必要なら、action / parameter selection自体を作者側研究結果を見ない別contextで行う。

成功条件は「面白い結果」ではなく、**どんな結果でも差し替えず、その結果から次状態へ進めること**。

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

EVT-003 / EVT-004 / EVT-005から重複EXPは作っていない。

EVT-005のDは、nonstored stable stateとしてQ-003 / EXP-003、update-order依存としてQ-004 / EXP-004と重なるため、現時点では新規research targetにしない。

## 次の物語側作業

EXP-005を研究都合で自動生成しない。

EVT-005後のPER-005 / PER-006を現在stateから動かす。

現在の自然な局所問題:

- DがA/Bの単純な中間なのか、別種の安定構造なのか
- stored集合外のstateが存在するとき「戻る」を何と定義するか
- 紙上計算から計算機実装へ進む必要が本当に生じるか
- 次の比較で何を固定し何を変えるか

## 未確定

- 具体年月日
- 国・都市・所属研究機関
- PER-005 / PER-006の氏名・年齢・性別
- 計算機・言語・端末
- 二人の正式な所属関係・上下関係
- 次に実行する具体的計算
- 現代側最初のevent
- 第2話以降の終了点

必要になる前に一括固定しない。

## 長期探索仮説

輪廻・同一認識主体・NNによる顕在化・情報量による出現確率等はCanonでも現実科学のFindingでもない。

競合説明として模倣、統計的再構成、一般的認知収束、selection bias、pattern over-detection等を残す。

## セキュリティ境界

生のAI内部推論、内部指示、credential、token、秘密値、公開不能な個人情報を保存しない。