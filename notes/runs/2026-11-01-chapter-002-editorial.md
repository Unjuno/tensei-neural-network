# 2026-11-01 第2話編集レビューと公開ゲート障害

## 変更前の確認

- 開始work HEAD: `1b20820efac67cdf9bcefe33fa5306509a2b0533`。前回索引commitから新しい作品変更なし。
- main/publication/policy.json: `enabled=true`、公開範囲は連載版のみ。mainの既刊台帳は第1話のみ。
- 前回の公開確認: Serial Publication run `41176991908` success、既刊のlive URL/hash照合済み。
- story head: `EVT-018`（変更前後同一）。PER-005/PER-006/ORG-001。現代側eventなし。
- 既存章: 第1〜5話技術gate通過。第2話は当初、公開用編集レビュー未作成。

## 第2話を実際に確認した内容

対象は `novel/chapters/002.md`（blob `c3b4cbb11e52a729fc336f7c701128f0cd1073f5`）、outline、EVT-005〜008、`experiments/chapters/002/` のsemantic-review/verification/terminology/results/review-lock、既存の研究・物語境界。下記5観点の具体的な判断と限界は `publication/reviews/002.json` に保存。

- 冒頭の「その二本だけで、どこまで言えますか」が起点。選んだorderから全64初期状態へ観測範囲を広げ、Dが-Cと分かるところで「答えの名前」を修正する流れ。
- 佐伯が結果を残す欄と条件を定め、高橋は全件を選択し、Dの名前を消さず新分類を併記する。対立のための未成立事件を足していない。
- 6本→36件→384件の数値説明には読解負荷があるが、反転という具体形で終盤の焦点を回収する。
- EVT-005: A/D/B/B/D/D、EVT-006: A11/B11/C2/D12、EVT-007: 64×6=384・固定点6つ・D=-C、EVT-008: zero-holdも含む符号反転可換性。本文上の存在例を一般頻度へ拡張しない。
- 最終段落は解釈・分類の修正で閉じ、以降の16素子例や作者側一般定理を人物へ漏らしていない。

5観点の編集評価: `PASS / AI_EDITORIAL_NOT_EXTERNAL_READER`、blocking_issues空。本文とEVTは未変更。レビューは人間の文学的承認ではない。

## 数理的再照合

元の`results.json`は個別check 15個すべてtrue、総合PASS。

さらに独立に書いた短いPython標準ライブラリ実装（CPython 3.13.5 / Linux x86_64 / 整数exact / 固定列挙 / RNGなし）で、6巡回順のA,-C,B,B,-C,-C、balanced cue36件の11/11/2/12、全64初期状態×6順の384件、fixed point6個、order-invariant 18 / dependent 46、one-unit sign-inversion可換性を再確認した。これは数理的な別実装照合であり、別人による文学レビューや盲検生成ではない。単位は無次元符号・整数件数のみで、物理単位の混在・浮動小数丸めなし。

レビューcommit: `18e34614b1ec0e0ff15779e9cfa375e47788208d`。
Story Workflow Validation run: `41252392042` **completed/success**。章再実行・研究再実行・EXP-013結果JSON照合・workflow validatorがすべてsuccess。

## 公開結果と障害

Serial Publication run `41252464100` は **failure**。
エンジンの29テスト、main側権限・Pages source確認、source CI照合は成功。次の「Prepare one episode」で
`{"status":"BLOCKED","reason":"unresolved event: EVT-005"}` により停止した。
main docs/serialの第2話生成・配信・URL/hash照合は**未実施**。既刊は第1話のみ。

原因は、EVT-005冒頭が `状態: PROVISIONAL / RESOLVED` であるのに、信頼済みゲートの`event_resolved`が厳密に `RESOLVED` または `RESOLVED / PROVISIONAL` 形式だけを認めること。EVT-005には事前lock commitと実行後の結果・deltaがあるが、本文内容だけでgateを迂回しない。連載の欠番は飛ばさない。

## 継続判断

- main・PR・Canon昇格・既刊本文・公開機構/権限/ゲートは変更しない。
- 次回は作業branch上でEVT-005の状態ラベルの意味を保った正規化と、その変更が第2〜5話review-lockの依存版へ及ぼす影響を検証する。影響全話の根拠・意味レビューを読まずにhashだけ更新しない。難しければ人間の認可を要するmain側の信頼済みゲート修正を明確な代替案として報告する。
- 本記録・STATUS・working-contextの同期コミット自体には新しいCIが必要。次の具体作業はstatusの現行値・ロック依存と採用済みEVTの内容同一性を監査すること。
- 実読者5名試読、独立restore、Human Review、Canon受理は未実施。公開阻止を「公開済み」に書き換えない。
