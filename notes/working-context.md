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
- current event head: `EVT-006`
- active personas: PER-005 / PER-006
- current structure: `起 / 承 / 転`
- 第1話ドラフト: `novel/chapters/001.md`
- 第1話採用範囲: `EVT-001`〜`EVT-004`

### EVT-004まで

- EVT-001: 「止まることと、戻ることは同じか」「保存していないところで止まるなら、その状態は何からできている？」
- EVT-002: `correct recall`のtargetを誰が定義するか
- EVT-003: A/B等距離cueと観測項目のprotocol
- EVT-004: 同一cue・weightsからupdate orderだけの差でA/Bへ分岐する6-unit例

EVT-004は数理的には有効だが、具体条件をoutcome前にlockしていなかったため生成検証上は `UNBLINDED`。

### EVT-005

同じ6-unit network / cueについて、自然順序の全6 cyclic update ordersを結果前に固定。

Action-lock commit:

`59ff6530d202b79834afbe8ffdceee1256437315`

結果:

```text
A / D / B / B / D / D
```

D:

```text
(+1, +1, +1, +1, -1, +1)
```

Dはnonstored fixed point。

Resolution provenance: `LOCKED`。

### EVT-006

EVT-005後、update orderだけでなくbalanced cue自体のselection freedomも減らすため、A/Bが異なる4位置から作れるA/B等距離cue全6種類を結果前に全列挙した。

Action-lock commit:

`97ee4b3d322d367468258775443d6f2aa3551ef1`

6 cues × 6 cyclic orders = 36 trials。

結果:

- A: 11
- B: 11
- C: 2
- nonstored D: 12
- nonconverged: 0

重要:

- q16はA/B/Cすべてへdistance 2で、2 ordersからCへ到達
- q24はA/Bへdistance 2ずつだが、initial cue自体がD

PER-005:

> AとBの間、と書いた時点で、ほかの戻り先を消していたのかもしれない。
>
> 手掛かりは二つの原像だけでは定義できない。

Resolution provenance: `LOCKED`。

## 第1話

`novel/chapters/001.md`

採用範囲はEVT-001〜004のまま。EVT-005/006を後から自動追加しない。

本文では未確定の氏名・年齢・性別・国籍・所属・具体機材等を勝手に固定しない。

## 生成方式検証

詳細: `notes/generation-validation.md`

- Test-001: state recovery / persona境界 / state同期 / NarrativeProjection PASS。EVT-004 resolver独立性はINCONCLUSIVE
- Test-002: EVT-005でACTION_LOCKED→commit→resolveを実行し、order selectionのpre-lockを確認
- Test-003: EVT-006でinitial cue集合もdeterministicに全列挙し、36 trialを選別せず受理

未検証:

- action selector自体を作者側研究結果から完全隔離したcontext isolation

## 物語由来の現実研究

### EVT-001 → EXP-003

- PASS
- 3-pattern majority mixture exact match 1件
- F-003 PROVISIONAL

### EVT-002 → EXP-004

- PASS
- balanced cue 200
- update-order runs 4000
- BIDIRECTIONAL 122/200
- F-004 PROVISIONAL

### EVT-006 → EXP-005

Q-005:

> pairwise balanced cueは、selected A/Bをstored-pattern Hamming距離上で残りstored patternsから孤立させるか。

EXP-005を結果前に事前登録して、EXP-004の200 balanced cuesをstored set全体へのHamming距離で再解析。

結果:

- PAIR_ISOLATED: 200
- THIRD_TIED: 0
- THIRD_CLOSER: 0
- margin `d_other_min - d_pair`: min 11 / max 30
- 判定: **FAIL**

H-005: `NOT_SUPPORTED`。

つまりEVT-006のN=6 toy networkにあった「第三stored patternもA/Bと同距離」というgeometryは、今回のN=100 random-pattern cue集合では再現しなかった。

ただし探索的にEXP-004では、selected pairがcueから各28 bit、第三stored patternが44 bit離れているのに、その第三patternへexact到達したrunが1件あった。

F-005:

> **Hamming距離上のpair isolationは、dynamics / basin上のpair isolationを保証しない。**

PROVISIONAL。

研究レポート: `research/reports/EXP-005.md`

## stable ID採番の注意

今回、current work branchの既存EVT-005を確認せず、一時的に別EVT-005を作る重複が発生した。重複は検出して削除済み。

再発防止として `AGENTS.md` に、stable ID採番前にmainだけでなく**現在のwork branch上の同種IDを確認する**規則を追加した。

`POLICY.md` の旧い「main上の最大番号」文言もbranch-awareへ同期する必要がある。

## 次の物語側作業

研究レポートの派生候補だけを理由にEXP-006を自動作成しない。

EVT-006後のPER-005 / PER-006を現在stateから動かす。

現在の自然な局所問題:

- pairwiseな`A/Bの間`をstored set全体に対してどう記述するか
- initial cue自体がfixed pointの場合とdynamicsで移動した場合をどう分けるか
- Dのようなnonstored fixed pointの扱い
- 紙上toy networkから計算機実装へ進む必要が実際に生じるか

outcome-sensitiveな次eventではACTION_LOCKEDを使う。

## 未確定

- 具体年月日
- 国・都市・所属研究機関
- PER-005 / PER-006の氏名・年齢・性別
- 計算機・言語・端末
- 二人の正式な所属関係・上下関係
- 現代側最初のevent
- 第2話以降の終了点

必要になる前に一括固定しない。

## 長期探索仮説

輪廻・同一認識主体・NNによる顕在化・情報量による出現確率等はCanonでも現実科学のFindingでもない。

競合説明として模倣、統計的再構成、一般的認知収束、selection bias、pattern over-detection等を残す。

## セキュリティ境界

生のAI内部推論、内部指示、credential、token、秘密値、公開不能な個人情報を保存しない。
