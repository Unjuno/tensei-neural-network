# 第1話「戻る先」公開前検証

状態: `IN_PROGRESS`

対象本文:

- `novel/chapters/001.md`
- 比較稿: `novel/chapters/001-webnovel-draft.md`
- 最小因果骨格: `novel/chapters/001-outline.md`

採用event:

`EVT-001 -> EVT-002 -> EVT-003 -> EVT-004`

## 目的

第1話を公開する前に、本文の技術・歴史・用語・人物knowledge boundaryを、成立済みevent/stateと研究実験へ照合する。

これは「第1話 = 一実験」という意味ではない。

第1話は複数eventからできており、既存研究実験のうち必要なものだけを参照する。

## 参照する研究・実験

現在の主要参照:

- `EXP-003-hopfield-mixture-structure`
- `EXP-004-hopfield-ambiguous-cue`
- 必要に応じて `research/1980s-research-environment.md`
- 必要に応じて `research/pre-hopfield-background.md`

ただし、作者側EXP結果を1980年代人物へ未来知識として渡さない。

## 検証対象

### 1. 数理・実験

- 6素子toy networkの定義
- 保存状態A/B/C
- 結合規則
- 自己結合なし
- 非同期更新
- 局所場0で現在値保持
- 更新順序だけでA/Bへ分岐すること
- 「二本のorderで観測した」以上へ一般化していないこと

### 2. 用語

`terminology.md` で管理する。

現在、特に検証が必要:

- neural network / 神経回路網 / ニューラル・ネットワーク
- associative memory / 連想記憶
- unit / 素子
- configuration / 状態 / 保存状態
- Hamming distance / ハミング距離
- local field / 局所場
- asynchronous update / 非同期更新
- fixed point / 固定点
- update order / 更新順序

### 3. 歴史・制度

- 1980年代半ばの日本企業基礎研究所で境界領域研究が成立し得るか
- 数理系研究者と神経生理系研究者が同一組織で継続議論できる設定
- 共用計算資源の存在をどこまで具体化できるか
- 論文別刷・図書室等の描写

具体機種・所在地等が未確定なら、公開本文でも無理に固定しない。

### 4. NarrativeProjection

- 英語語彙を読者の前提にしない
- 技術説明を研究レポート化しない
- 高橋と佐伯のpersona差が会話・行動に出ている
- EVT-005以降の知識を遡及させない
- ORG-001の将来の閉鎖・再編を予告情報として人物へ漏らさない

## 公開前ワークフロー

1. `001.md` の本文表現を抽出
2. `terminology.md` と数理検証項目へ対応付ける
3. 未検証の重要語・主張だけ調査または実験する
4. 既存EXP / Finding / 一次資料と照合
5. 衝突があれば本文を修正
6. 再度本文を読み、置換による不自然さを修正
7. EVT/state整合を再確認
8. 全必須項目が通ったら状態を `PREPUBLICATION_VERIFIED` へ変更

## 現在判定

`NOT READY FOR PUBLICATION`

理由:

- 第1話の技術的な中心結果自体はevent側で再現可能だが、読者向け日本語専門語の歴史的妥当性はまだ一括検証していない
- 研究所環境の重要描写には一定の研究根拠があるが、本文で使う語彙と1980年代人物語彙の境界をさらに確認する必要がある

本文の完成度と公開検証の完了を同一視しない。
