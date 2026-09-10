# 現在の状態

更新: 2026-09-11
このファイルは索引。直接のEVT・state・検証結果を優先する。

## 作業と公開の境界

- 作業branch: `work/story-bootstrap`
- story head: `EVT-013`
- 現代側event head: none
- mainへの反映、PR作成、docs同期、公開は行っていない
- 今回の主作業: 第1〜4話を読者として連続読解し、読書速度を失う箇所を抽出してNarrativeProjectionを改稿

## 第1〜4話

| 話 | 採用EVT | 状態 | 2026-09-11読者ロス対応 |
|---|---|---|---|
| 1 戻る先 | EVT-001〜004 | PREPUBLICATION_GATE_PASSED | ロス低〜中。現在の導線を維持し本文変更なし |
| 2 選ばなかった答え | EVT-005〜008 | PREPUBLICATION_GATE_PASSED | 6→36→384の手続き反復を圧縮し、D→C→D=-Cを前景化 |
| 3 表の外 | EVT-009〜011 | PREPUBLICATION_GATE_PASSED | 文献説明を圧縮し、六素子の空白→十六素子Qを一本化 |
| 4 五と二十一 | EVT-012〜013 | PREPUBLICATION_GATE_PASSED | 5/21を先に謎として置き、成分関係と一つの式で解く構成へ変更 |

読者ロス監査: `notes/reader-loss-audit-2026-09-11.md`。

これは実在読者の離脱率測定ではなく、研究資料を見ずに本文を読む編集simulation。独立試読は未実施。

第2〜4話は旧gateを一度 `IN_PROGRESS` へ戻し、改稿後の本文blobを `review-lock.json` へ固定して `GATE_CANDIDATE` へ進めた。candidate commit `bdc69e9f91ba08428c556e488fa66eccb9d97668`、GitHub Actions run `34503727557` / job `102960602443` はsuccess。既存4話の実行可能verification、保存結果照合、workflow検査が成功した後にgateへ戻した。

## 現在世界の復元

起点は `BOOT-002 @ T0-1980S @ none`。時代は1984〜85年前後を候補とし、具体年月日は未確定。

active: PER-005 高橋修一、PER-006 佐伯玲子、ORG-001 光陵化学生命科学研究所。

`world.md`と人物snapshotの一部はEVT-007まで。EVT-008〜013と対応deltaを適用して復元し、古いsnapshotへ巻き戻さない。同じ差分をEVTとdeltaから二重加算しない。

現在の局所問題は、Q以外の初期状態からQへ到達するか。EVT-013までで説明できたのは掲載例Qの安定性であり、到達頻度ではない。

## 読者として見えた主要ロス

- 専門性そのものより、検証手続きが発見より前景化すると読書速度を失う
- 高橋が広げ、佐伯が止める会話を反復すると、人物が二つの検査機能に見える
- 数字は削るより「何を解く数字か」を先に置いた方が追いやすい
- 正確さの限定を毎行発話せず、表・空欄・別紙・照合等の行動で維持する

今回、新しいEVT・研究EXP・persona・organizationは追加していない。既存event/stateの数学的結果も変更していない。

## 次の優先

1. 実在読者の小規模試読で、各話の読書速度低下箇所を記録する
2. 今回のsimulationと実読者のロスが衝突した場合、具体的な実読者反応を優先して再評価する
3. 世界進行を再開する場合はEVT-013から行動を選び、Qのaccessibilityについて初期状態集合・更新順・停止条件を結果前固定する

## 残る未確定

研究所の所在地・部門・職位・設立細部、具体年月日、共用計算機・OS・言語、人物の生活史、研究所の将来、現代側最初のevent、第5話以降。必要前に一括固定しない。

## 検証系

`WORKFLOW.md` を参照。review-lockの鮮度、個別checks、保存JSONとの一致を検査する。Human ReviewはCIとは別である。
