# 現在の状態

このファイルはプロジェクトの詳細な記憶ではなく、現在位置を示す索引です。詳細は各正本ファイルを参照します。

## フェーズ

- プロジェクト段階: 初期設計完了・リポジトリ衛生確認中
- 物語段階: 未着手
- 学習段階: CATCH_UP
- 研究段階: 最初の古典研究と追試対象を選定する前

## Active ID

- Q: なし
- H: なし
- EXP: なし
- F: なし
- L: なし

## 現在の目標

1. 制作開始前にリポジトリをクリーンな運用状態へする
2. 不要な自動PRレビューを止める
3. 不要branchと設定上の残骸を整理する
4. Public / Private と main保護方針を確定する
5. 衛生確認後、第1技術テーマの選定へ進む

## リポジトリ衛生状況

### 完了

- 初期設計PR #1は `main` へmerge済み
- `main` を人間が受理した正本として定義済み
- `.github/workflows/` は存在しない
- GitHub Actions workflow run は確認時点で0件
- 自動起動はGitHub Actions CIではなく、PRイベントに反応した外部GitHub Appであることを確認
- PR #1で `chatgpt-codex-connector[bot]` と `cursor[bot]` の反応を確認
- work branch上で作業を完了してから、必要な場合のみレビュー境界でPRを作る運用へ変更済み
- open PRは0件

### 要対応

- Codexの自動Code Review / GitHub Appアクセスを、このrepoで無効化または対象外にする
- Cursor GitHub AppのこのrepoへのPRフックを無効化または対象外にする
- merge済みの `bootstrap/repository-design` branchを削除する
- repository visibilityが現在Publicのため、このまま公開運用するかPrivateへ戻すか決める
- `main` は現在branch protectionなし。外部自動レビュー問題を解消した後、必要な保護方式を決める

外部GitHub Appのrepo別アクセス設定とbranch削除は、現在利用しているGitHub接続から直接変更できない場合がある。その場合はGitHub UI側で処理する。

## 設計監査結果

初回監査では外部長期記憶としての意味論に不足があり `NO-GO` となったため、PR #1内で修正しました。

修正後の再監査では、次を運用開始可能と判定しました。

- `main` = 人間が受理した正本、branch / PR = 候補状態
- cold-start: `README.md` → `AGENTS.md` → `STATUS.md` → `POLICY.md`
- `novel/canon.md` と `novel/timeline.md` の権威関係
- Q / H / EXP / F / REF / L の安定ID規則
- `PASS / FAIL / UNCERTAIN` の実験判定規則
- Experiment → Hypothesis の状態更新
- Findingの競合・置換処理
- 作者の学習内容と作品反映の追跡
- アイデア採用時の正本への反映
- 人物の重要な信念更新履歴

## 作品・研究上の未解決

- 主人公研究者の専門分野と年代の最終確定
- 第1話で扱う最初の技術テーマ
- 第1追試の対象
- 公開後のContribution / Credit / Licenseの詳細

これらは意図的な未決定事項であり、現在のリポジトリ衛生問題とは分離する。

## 衛生確認後に行うこと

1. 第1テーマ候補を比較する
2. 採用テーマの原典を `references/bibliography.md` に `REF-001` として登録する
3. `Q-001` を作成する
4. 必要なら `H-001` を作成する
5. `EXP-001-.../` を作り、実行前条件を固定する
6. 追試結果と理解を物語設計へ反映する

## 参照順

1. `README.md` — プロジェクト目的
2. `AGENTS.md` — AI作業規則
3. `STATUS.md` — 現在位置
4. `POLICY.md` — 正本・優先順位・研究判定

作業別の詳細な参照順は `AGENTS.md` に従います。
