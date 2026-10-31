# 現在の状態

更新: 2026-10-31。これは索引。直接のEVT・state・実験記録・公開台帳・実際のCIを優先する。

## 現在位置と公開

- 制作branch: `work/story-bootstrap`
- 1980年代側resolved head: **EVT-018**。現代側: none
- active: PER-005 高橋修一 / PER-006 佐伯玲子 / ORG-001 光陵化学生命科学研究所
- 第1〜5話はPREPUBLICATION_GATE_PASSED。独立試読・Human Reviewは未実施
- **連載版の第1話「戻る先」を2026-10-31に公開済み。** 第2〜5話は未公開で、公開用の読者視点レビューが必要
- 公開目次: https://unjuno.github.io/tensei-neural-network/serial/
- 第1話: https://unjuno.github.io/tensei-neural-network/serial/001.html

## 今回の継続委任の境界

ユーザーは2026-10-31に、定期制作・検証・連載版公開のループを明示依頼した。この限定範囲の公開は毎回の承認待ちにしない。詳細と停止スイッチの正本は**mainのpublication/README.md / publication/policy.json**。

mainへ追加したのは公開機構とdocs/serialの生成物だけ。work全体のmerge/fast-forward、研究/本文原稿/Canonの一括受理、PR、他サイト投稿は行っていない。公開とCanon受理は別。既存docs/novel・docs/researchはそのまま保持した。

## 定期ループ

制作: 既存ChatGPTタスク「研究小説の制作・検証・連載」を更新して有効化。毎日午前8時ごろ（Asia/Tokyo）。最も古い未公開章を実読・改稿・検証し、publication/reviews/NNN.jsonへ対象版付き編集評価を記録する。未読の一括PASSは禁止。

公開: mainのSerial Publication workflow。毎日UTC 02:17（日本時間11:17）とsource CI完了等で確認。最新work SHAのCI、話別gate、review-lock、用語・EVT・編集レビューを照合し、既刊直後の1話だけを最大1日1話で出力。配信未確認時は新話を足さず前回配信を再試行する。

停止: main/publication/policy.jsonのenabled=false。機構の権限・ゲートを制作タスク自身で緩めない。

## 初回の実測検証

- work候補commit: `7820573205f29e6d626952f914d469f0f9982802`
- Story Workflow Validation: run `41176570607` success。既存5話・研究実験・EXP-013結果照合・構造検査を通過
- 追加公開エンジンのunit tests: 29件成功（ローカルCPython 3.13.5、Actions CPython 3.12.15）
- Serial Publication: run `41176658296` / job `124465509267` success
- 公開先manifestと最新HTMLのSHA-256一致を同jobで確認しDEPLOYEDとした。GitにHTMLが存在するだけでは公開成功としない
- 失敗履歴: 初回run `41176298501` は旧EVTのPROVISIONAL表記を拒否して停止。成立済み旧EVT-001〜004だけを正確なblob hashで識別する互換修正と回帰テストを追加。過去EVTや本文の書換え、未確認PROVISIONALの一括容認はしていない

今回の記録: `notes/runs/2026-10-31-publication-loop.md`。公開原稿と根拠の版はmainの`docs/serial/manifest.json`を参照。

## 小説・未採用案

| 話 | 採用EVT | 状態 |
|---|---|---|
| 1 戻る先 | EVT-001〜004 | 技術gate済み、編集レビュー済み、連載公開済み |
| 2 選ばなかった答え | EVT-005〜008 | 技術gate済み、公開前の追加編集レビュー待ち |
| 3 表の外 | EVT-009〜011 | 同上 |
| 4 五と二十一 | EVT-012〜013 | 同上 |
| 5 最初に動いたもの | EVT-014〜018 | 同上 |

`novel/scene-probes/2026-10-31-circle-and-original-records.md`は未採用。そこに書いた会話・保存・組織への提出は未成立のまま。今回新EVT・新personaは追加していない。

## 状態復元・研究

BOOT-002 / T0-1980S起点。具体年月日は未確定。古いworld/persona snapshotへ巻き戻さずEVT-008〜018と対応deltaを一度だけ適用する。人物は作者側の一般定理・EXP結果を自動的には知らない。

EVT-018までの局所結果は、16素子Qの一bit近傍と16巡回順の256件がQ112・保存記憶各48となり、first-flip・4点の不安定集合・円環gapで説明できたこと。112/256を自然確率へ一般化しない。

作者側EXP-006〜013の研究状況は`notes/roadmap-progress-2026-10-30.md`と各実験正本へ。EXP-013は640適格模型・139440軌道が保存結果と一致、CI組込済み。EXP-009は事前登録された条件を確認して扱い、未実行と実行済みを混同しない。

## 次回の一手・残課題

最も古い未公開の第2話を本文から読み、5観点の具体的なpublication/reviews/002.jsonを作る。問題があれば本文を直し話別検証へ戻す。その後も既存公開待ちを先に整え、自然な必要がある場合だけEVT-018以降を進める。章数ノルマ・公開日から未来eventを発生させない。

実読者5名のpilot、真に独立した別主体の意味復元、人間によるCanon受理はOPEN。AI編集評価をこれらの代用として報告しない。研究所の具体所在地・職位・機種/OS/言語・私生活史・未来事件は因果に必要になるまで固定しない。
