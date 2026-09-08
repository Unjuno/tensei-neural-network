# 現在の状態

更新: 2026-09-08
このファイルは索引。直接のEVT・state・検証結果を優先する。

## 作業と公開の境界

- 作業branch: `work/story-bootstrap`
- story head: `EVT-013`。今回の評価・改稿で新EVTは作成していない
- 現代側event head: none
- mainへの反映、PR作成、docs同期、公開は行わない
- 今回の主作業: 既存4話の再評価・修正と、検証対象版の追跡強化

## 第1〜4話

| 話 | 本文 | 採用EVT | 今回の状態 |
|---|---|---|---|
| 1 戻る先 | novel/chapters/001.md | EVT-001〜004 | GATE_CANDIDATE |
| 2 選ばなかった答え | novel/chapters/002.md | EVT-005〜008 | GATE_CANDIDATE |
| 3 表の外 | novel/chapters/003.md | EVT-009〜011 | GATE_CANDIDATE |
| 4 五と二十一 | novel/chapters/004.md | EVT-012〜013 | GATE_CANDIDATE |

旧稿へのgate成功を今回の改稿へ自動流用しない。話別packageのREADMEとreview-lockが対象版とCIを示す。

## 現在世界の復元

起点は `BOOT-002 @ T0-1980S @ none`。時代は1984〜85年前後を候補とし具体年月日は未確定。

active: PER-005 高橋修一、PER-006 佐伯玲子、ORG-001 光陵化学生命科学研究所。

`world.md`と人物snapshotの一部はEVT-007まで。後続EVT-008〜013と対応persona/organization deltaを適用し、古いsnapshotへ巻き戻さない。EVTとdeltaの同じ差分を二重加算しない。

現在の局所的な問いは、Q以外の初期状態からQに到達するか。EVT-013までに説明できたのは掲載例のQの安定性であり、到達頻度ではない。

## 今回の評価

`notes/assessment-and-roadmap.md` に根拠・修正・長期目標を保存。

数学の有限再現は支持されたが、旧意味レビューには本文の未成立実験・数値経路・過剰解釈の見逃しがあった。人物が研究手続きの説明役に寄る点、組織の独立判断、独立試読・別コンテキストでの復元/行動選択は未検証。

今回の改稿では過去EVT・personaの恒常設定を変更せず、本文を修正した。新persona/ORG/研究EXPはゼロ。

## 次の制作上の優先

本文を読者として確認し、独立した試読・復元評価を行う。長期目標は話数や未来事件ではなく理解・来歴・再現性の受入基準とする。

その後に世界進行を再開する場合は現在headから行動を選択する。accessibility検査は初期集合・更新順・停止条件を結果前固定し、1983年論文Figure 1の未掲載の条件を捏造しない。

## 残る未確定

研究所の所在地・部門・職位・設立の細部、具体年月日、共用計算機・OS・言語、人物の生活史、研究所の将来、現代側最初のevent、第5話以降。必要前に一括固定しない。

## 検証系

`WORKFLOW.md` を参照。review-lockの鮮度、個別checks、全保存JSONとの一致を検査する。作業CIでは未完成章があるだけなら許容するが、候補/通過済み章の条件は免除しない。Human ReviewはCIとは別である。
