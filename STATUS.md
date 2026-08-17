# 現在の状態

このファイルはプロジェクトの詳細な記憶ではなく、現在位置を示す索引です。詳細は各正本ファイルを参照します。

## フェーズ

- プロジェクト段階: 初期設計完了・第1追試準備中（リポジトリ衛生の一部は保留）
- 物語段階: 第1技術テーマ選定済み・本文未着手
- 学習段階: CATCH_UP
- 研究段階: Hopfield 1982の第1追試を事前登録済み・実行前

## Active ID

- Q: Q-001
- H: H-001
- EXP: EXP-001
- F: なし
- L: なし

## 現在の目標

1. REF-001 / Q-001 / H-001 / EXP-001の事前条件を維持したまま第1追試を実行する
2. raw resultと集計を検証し、EXP-001をPASS / FAIL / UNCERTAINで判定する
3. 結果からF-001とL-001を必要に応じて作成する
4. 「状態ダイナミクスとしての記憶」を第1話・主人公研究者設計へ接続する
5. ある程度の研究・作品内容が揃った段階でGitHub Pagesの公開設定を行う

## 第1テーマ

- テーマ: Hopfield network / content-addressable memory
- 原典: REF-001 — J. J. Hopfield (1982), “Neural networks and physical systems with emergent collective computational abilities”
- 問い: Q-001 — 低負荷Hopfield networkは乱されたcueから保存パターンを回復できるか
- 仮説: H-001 — N=100, P=5の操作条件で10% / 20% bit反転から高率にexact recallできる
- 実験: EXP-001 — `experiments/EXP-001-hopfield-associative-memory/`

EXP-001の判定基準は結果を見る前にbranchへ記録済み。結果を見てから閾値を変更しない。

## リポジトリ衛生状況

### 完了

- 初期設計PR #1は `main` へmerge済み
- `main` を人間が受理した正本として定義済み
- `.github/workflows/` は存在しない
- GitHub Actions workflow run は確認時点で0件
- 自動起動はGitHub Actions CIではなく、PRイベントに反応した外部GitHub Appであることを確認
- PR #1で `chatgpt-codex-connector[bot]` と `cursor[bot]` の反応を確認
- 内部AI作業はPRではなくwork branch比較でレビューする運用へ変更済み
- open PRは0件

### 要対応・保留

- Codexの自動Code Review / GitHub Appアクセスを、このrepoで無効化または対象外にする
- Cursor GitHub AppのこのrepoへのPRフックを無効化または対象外にする
- merge済みの `bootstrap/repository-design` branchを削除する
- repository visibilityが現在Publicのため、このまま公開運用するかPrivateへ戻すか決める
- `main` は現在branch protectionなし。外部自動レビュー問題を解消した後、必要な保護方式を決める
- GitHub Pagesは研究・作品の最初の公開単位が揃った段階で設定する

外部GitHub Appのrepo別アクセス設定、branch削除、Pages等はGitHub UI側で処理する可能性がある。研究作業を止めるblockerではないものは制作と並行して扱う。

## 設計監査結果

初回監査では外部長期記憶としての意味論に不足があり `NO-GO` となったため、PR #1内で修正した。修正後の再監査では、cold-start、正本関係、安定ID、実験判定、Experiment→Hypothesis、Finding競合、学習履歴の追跡を運用開始可能と判定した。

## 作品・研究上の未解決

- 主人公研究者の専門分野・所属・年の最終確定
- 第1話の具体的な事件・視点人物・シーン構成
- Hopfield追試の次にPerceptronへ戻るか、1984 graded-responseへ進むか
- 公開後のContribution / Credit / Licenseの詳細

## 次に行うこと

1. EXP-001を実行する
2. raw resultとsummaryの整合を確認する
3. EXP-001 READMEを実行後状態へ更新する
4. Q-001 / H-001 / F-001 / L-001を結果に合わせて更新する
5. `novel/structure.md` へ第1話の技術的な核を反映する
6. `main...work/exp-001-hopfield` を比較し、人間レビューへ提示する

## 参照順

1. `README.md` — プロジェクト目的
2. `AGENTS.md` — AI作業規則
3. `STATUS.md` — 現在位置
4. `POLICY.md` — 正本・優先順位・研究判定

作業別の詳細な参照順は `AGENTS.md` に従います。
