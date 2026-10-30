# 作業コンテキスト

更新: 2026-10-30。高速引継ぎ用索引であり、正本は直接のEVT / state / evidence。内部指示・秘密情報は記録しない。

## 復元先

- repo: `Unjuno/tensei-neural-network`
- work branch: `work/story-bootstrap`。main、PR、公開、Canon昇格には人間承認が必要
- 1980年代側resolved head: **EVT-018**。現代側: none
- active: PER-005 高橋修一 / PER-006 佐伯玲子 / ORG-001
- 第1〜5話は `PREPUBLICATION_GATE_PASSED`。第5話はEVT-014〜018を採用
- 古いsnapshotを正史と取り違えず、EVT-008〜018および対応deltaを一度だけ適用する

## 現在の物語上の理解

Qは1983年掲載16-unit/3-stored pattern例のnonstored stable majority。EVT-014でQから1bit反転した16初期状態×16 cyclic order=256をlockして実行し、Q=112、M1=M2=M3=48。EVT-015でsplit位置の少数派storedとの距離が4→3と判明。EVT-016〜018では最初のflip、initial unstable集合4個、円環gapが256件のカウントを説明。第5話「最初に動いたもの」へ投影済み。

次のstory eventは未成立。第6話を作るための事件や研究結果を先に選ばず、EVT-018時点で人物が持つGoals/Beliefs/ObservationsとORGの制約から進める。

## 作者側研究の境界

- EXP-007 P=3 nonnegative-stable majority Q / symmetric Hebbian / asynchronous fair one-unit / zero-holdに限る少数派escape定理（EXP-011でzero-margin拡張）
- EXP-008 同期更新のperiod-2反例
- EXP-010 偶数Nのzero-margin探索は事前設計の不適格で終了
- EXP-011 奇数Nで304,038試行、反例なし
- EXP-012 P=5は別のnonstored stable状態へのescapeが発生
- EXP-013 margin三領域の固定予測、640 eligible models・139,440 trajectoriesが一致。2026-10-30に保存データを別実装でも照合し、CIへ追加
- EXP-009はREADME上事前登録。実行前に同一repo内の実装/結果有無を確認

これらの作者側一般化・証明は高橋と佐伯へ漏らさない。

## 自律実行手順

GitHubの最新HEADを必ず確認し、`STATUS.md`→関連event→個別実験条件/結果→CIを読む。最新状態と索引が食い違えばdirect EVTを優先して索引を直す。研究を進めるなら事前登録と結果を分離し、失敗・不都合な結果も残す。実装コードが既にある場合は先にその有無と実行状態を調査する。変更はwork branchのみ、保存JSON照合とCIを行う。本文・検証・review-lock変更時にはgateを再実施する。

読者評価と数理評価を混同しない。最低5名の外部試読・Human Review・独立した別主体の意味復元は未完。AI編集simulationを実読者と数えない。

## 作業優先

- EXP-013新CIの成功確認
- 独立復元と最新story状態の整合
- 人物/世界から生じる次の問いの探索（結果の先取り禁止）
- EXP-009の既存事前登録に基づく検証（必要な計算予算・時間を確認）
- 外部試読者の回答が来たときに集計し再改稿

未確定の具体年・場所・machine/OS/言語・組織職位・未来プロットは必要になるまで固定しない。

## 2026-10-31 次場面の試作（未採用）

起点HEAD `d4fb65f7f0f3757f4e4b616303f5b4e60b016523` のEVT-018までを読んだ。新trial・新EVTを作らず、二人の現在のGoalsから「説明を円環gapへ圧縮したあと、検証可能な原票をどう残し、誰に見せるのか」を一つの問いとして選択。

`novel/scene-probes/2026-10-31-circle-and-original-records.md` に二人の役割を一度入れ替える短い場面を試作。**発言も筆記もまだstory factではない**。研究所への提出、資料保存、機種、研究所の判断、第6話を確定させていない。第5話の章索引は補正。

次回はこの場面が既存のPersona/EVT/ORGの境界に収まるか確認し、独立読者評価がない以上、文学的成功とせず採否を保留する。新しい実験を選ぶなら事前登録を先に行う。
