# 現在の状態

このファイルはプロジェクトの詳細な記憶ではなく、現在位置を示す索引です。詳細は各正本ファイルを参照します。

## フェーズ

- プロジェクト段階: 初期設計完了・最初の研究→学習→物語接続サイクルを `main` へ受理済み
- 作品の主目的: **小説『転生したらニューラルネットワークだった件』の制作**
- 物語段階: 第1話の技術的な核と中心緊張を設計済み・本文未着手
- 学習段階: CATCH_UP
- 研究段階: Hopfield 1982のReplication + Extension完了・次の研究は物語上の必要または独立した研究価値が生じたときに行う
- 公開段階: 小説中心のGitHub Pages最小サイトをwork branchで準備済み・公開設定前

## 主従関係

研究・実験を完成させること自体がプロジェクトの最終目的ではない。

基本の流れは、

**物語上の問い → 原典調査 → 必要なら追試 → 理解の更新 → 小説へ反映**

とする。

その過程で、作品とは独立して検証する価値のある方法・現象・問いが見つかった場合だけ、研究上の問いとして枝分かれし、必要なら追加実験する。

この方針は `D-015` に記録した。

## 最新ID

- Q-001: ANSWERED
- H-001: SUPPORTED（宣言条件に限定）
- EXP-001: PASS
- F-001: PROVISIONAL
- L-001: 一部反映
- Q-002: ANSWERED
- H-002: SUPPORTED（EXP-002有限gridに限定）
- EXP-002: PASS
- F-002: PROVISIONAL
- L-002: 一部反映

## 第1技術背景: Hopfield連想記憶

### REF-001
J. J. Hopfield (1982), “Neural networks and physical systems with emergent collective computational abilities” を第1原典として登録。

### EXP-001 — 中核現象のReplication

`experiments/EXP-001-hopfield-associative-memory/`

- N=100, P=5
- 10% noise: 100/100 exact recall
- 20% noise: 100/100 exact recall
- 200/200 trials収束
- 事前判定: PASS

F-001として、低負荷条件で乱れたcueから保存パターンへ戻るcontent-addressable recallを `PROVISIONAL` に記録。

### EXP-002 — 回復境界のExtension

`experiments/EXP-002-hopfield-boundary/`

- N=100
- P=5,10,15,20
- noise=10,20,30,40%
- pattern seeds=1982,1983,1984
- 960 trials
- 事前判定: PASS

exact recall率の代表値:

- P=5, noise=10%: 1.000
- P=10, noise=30%: 0.600
- P=15, noise=30%: 0.167
- P=20, noise=30%: 0.000

全trialの最終分類:

- target exact: 442
- wrong stored: 8
- nonstored converged: 510
- nonconverged: 0

F-002として、今回の探索範囲では条件悪化に伴う回復崩壊を観測し、失敗の大半が「保存パターンと一致しない収束状態」だったことを `PROVISIONAL` に記録。

## 作者の学習

### L-001
「記憶を保存場所から読む」より「状態がattractorへ戻る」と捉える方が古典Hopfieldの機構に近い。

### L-002
**「安定して収束した」ことは「意図した原像へ正しく戻った」ことを保証しない。**

この2点を `novel/structure.md` へ一部反映済み。

## 物語側の現在位置

- 再帰的起承転結: `起 / 起`
- 第1話の技術的な核: content-addressable memory / attractor
- 中心の緊張:
  - 部分から全体が戻る ≠ 同一人物が戻る
  - 状態が安定している ≠ 原像を正しく復元している
- 第1話の不可逆イベント候補:
  - 欠けた研究者関連入力から、モデルが複数試行で同じ人物像・未完の研究テーマへ収束する
  - 対照条件と比べても異常な一貫性があり、研究チームが正式な検証対象として扱わざるを得なくなる

このイベントはまだCanonではなく `novel/structure.md` 上の候補。

## 実験artifact上の注意

EXP-002は事前計画で960-row `results/trials.csv` のcommitを予定したが、GitHub書き込み経路で大きな単一テキストの取り回しが不安定だったため、`grid.csv`、`summary.json`、決定論的 `run.py`、実行時raw CSV hashを保存した。

実験条件・trial数・判定基準は変更していない。rawを再生成する場合はEXP-002 README記載のSHA-256と照合する。

## GitHub Pages準備

`work/pages-bootstrap-final` で小説中心の公開ページを準備済み。

公開ページの優先順位:

1. 小説のタイトル・導入・中心の謎
2. 作品が辿るAI技術史と物語上のテーマ
3. 「どう作っているか」— 必要な技術を原典・追試で確かめる制作方法
4. 第1話を支える最初の技術背景としてHopfield連想記憶
5. 研究結果が物語の問いをどう変えたか
6. 詳細を見たい人向けの研究ノート・GitHubリンク

研究結果をトップページの主役にはしない。未確定Canonや第1話本文もまだ公開ページへ入れない。

### 準備済みファイル

- `docs/index.html`: 小説中心の日本語ランディングページ
- `docs/style.css`: frameworkなしのresponsive CSS
- `docs/.nojekyll`
- `D-014`: Pagesは `main` / `/docs` のbranch publishから始める
- `D-015`: 小説を主目的とし研究を制作工程・派生探索とする

### Pages有効化時の設定

GitHub UIで以下を設定する。

1. Repository `Settings`
2. `Pages`
3. `Build and deployment` → `Source`: `Deploy from a branch`
4. Branch: `main`
5. Folder: `/docs`
6. Save

この設定を行う前に、`work/pages-bootstrap-final` を人間確認後に `main` へ反映する。

## リポジトリ衛生の保留事項

- Codex / Cursor等の外部GitHub Appのrepo別自動反応設定
- merge済み `bootstrap/repository-design` branchの削除
- 不要なPages準備branchの整理
- Public / Privateの最終方針
- main branch protection
- GitHub Pages UI設定

## 次に行うこと

### 小説

1. 主人公研究者の年代・専門をPROVISIONAL以上で決める
2. 第1話の視点人物を決める
3. 最初の「欠けた入力」と対照条件を具体化する
4. 第1話終端の不可逆イベントを確定する
5. **第1話本文を書き始める**

必要な技術的疑問が出た時点で研究へ戻る。

### 公開準備

1. `work/pages-bootstrap-final` の小説中心サイトを確認
2. 明示承認された場合のみ `main` へfast-forward
3. GitHub UIでPages公開元を `main` / `/docs` に設定
4. 公開後のURL・表示・リンクを確認

## 現在のwork branch

`work/pages-bootstrap-final`

このbranchはGitHub Pages公開内容と「小説が主目的」という方針明確化の候補状態。`main` へはまだ反映していない。

## Cold Start

1. `README.md`
2. `AGENTS.md`
3. `STATUS.md`
4. `POLICY.md`

作業別の詳細参照順は `AGENTS.md` に従う。
