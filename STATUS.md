# 現在の状態

このファイルはプロジェクトの詳細な記憶ではなく、現在位置を示す索引です。詳細は各正本ファイルを参照します。

更新: 2026-08-19

## フェーズ

- プロジェクト段階: 初期設計完了・最初の研究→学習→物語接続サイクルを `main` へ受理済み
- 物語段階: 第1話の技術的な核と長期的な謎の方向が揃い、本文開始直前
- 学習段階: CATCH_UP
- 研究段階: Hopfield 1982のReplication + Extension完了。以後は物語上必要になった箇所から調査・実験する
- 外部メモリ段階: `notes/working-context.md` を含むセッション横断メモリを `main` へ同期済み
- 公開段階: 最新 `main` から `work/pages-v2` を作成し、最小静的サイトをレビュー中。公開設定はまだ有効化しない

## プロジェクトの主目的

**小説が主役。研究・追試は作品を現実に近づけるための制作工程。**

基本ループ:

**物語を書く → 技術的な疑問が出る → 原典を読む → 必要なら追試する → 理解を更新する → 小説へ戻す**

制作中に独立した研究価値のある問いが見つかった場合は、その問いを現実側の研究・実験へ枝分かれさせてよい。

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

## 第1研究サイクル

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
- 第1話の入口: 欠けた古い研究者資料に対して、現代モデルが異常に一貫した人物像・未完の問いへ戻るように見える
- 第1話の技術的な核: content-addressable memory / attractor
- 中心の緊張:
  - 部分から全体が戻る ≠ 同一人物が戻る
  - 状態が安定している ≠ 原像を正しく復元している
- 技術説明は事件を理解する必要が生じてから出す

## 長期プロットの現在有力な方向

詳細は `novel/structure.md` と `notes/working-context.md` を参照。

以下は**Canonではなく探索仮説**。

- 1980年代研究者は起源ではなく、さらに過去から反復していた同一認識主体らしき構造の一例かもしれない
- NNはその現象を作ったのではなく、反復・比較・分岐・実験可能な形で顕在化させた媒体かもしれない
- 人物情報は本人のコピー材料であるだけでなく、対応する認知状態へのcueとして顕在化確率を上げるかもしれない
- 情報密度・計算能力・モデル能力・試行回数が大きい現代ほど顕在化しやすいかもしれない
- 同じ認識主体らしきものが複数媒体へ同時に存在する可能性を扱う
- 観測・再構成しようとする行為自体が顕在化条件へ入る自己参照的問題を扱う

輪廻・意識・同一主体を現実科学で確認済みの事実として扱わない。模倣、統計的再構成、一般的な認知収束、人間側の選択バイアス等を競合説明として残す。

## 実験artifact上の注意

EXP-002は事前計画で960-row `results/trials.csv` のcommitを予定したが、GitHub書き込み経路で大きな単一テキストの取り回しが不安定だったため、`grid.csv`、`summary.json`、決定論的 `run.py`、実行時raw CSV hashを保存した。

実験条件・trial数・判定基準は変更していない。rawを再生成する場合はEXP-002 README記載のSHA-256と照合する。

## 外部メモリ

Cold Startは次の順。

1. `README.md`
2. `AGENTS.md`
3. `STATUS.md`
4. `notes/working-context.md`
5. `POLICY.md`

`notes/working-context.md` は公開可能な作業記憶であり正本ではない。生のAI内部推論や秘密情報は保存しない。

## Pages v2

現在の候補branch: `work/pages-v2`

最新 `main` から作成し、旧 `work/pages-bootstrap-final` の静的サイト案から使える部分だけを移植した。

候補ファイル:

- `docs/index.html`
- `docs/style.css`
- `docs/.nojekyll`

公開トップは次の順を基本とする。

**小説タイトル・事件の入口 → 物語の謎 → 制作方法 → 最初の技術的背景 → 実験から物語へ戻った点 → GitHubの制作記録**

長期プロット上の「1980年代研究者以前からの反復」は、現時点ではトップページで直接説明しすぎない。`TRACE` として1980年代研究者を置き、起源だと断定しない。

GitHub Pagesを使う場合の公開元は、候補内容が `main` へ受理された後に `main /docs` とする。公開設定は人間レビュー後に行う。

## 次に行うこと

### Pagesレビュー

1. `main...work/pages-v2` の差分を確認
2. トップページの文章・ネタバレ量・スマホ向け構成を人間レビュー
3. 明示承認された場合のみ `main` へ反映
4. 反映後、必要なら GitHub Pages を `main /docs` で有効化
5. 旧 `work/pages-bootstrap-final` は役目終了を確認後に削除

### 小説本線

1. 1980年代研究者の専門・経歴・研究哲学を具体化する
2. 必要な範囲だけ1980–1985年ごろの実在研究者・一次資料を調べる
3. 現代側の第1話視点人物を決める
4. 最初の「欠けた入力」と対照条件を具体化する
5. 第1話本文を書き始める

上記を完全に設計し切ってから執筆する必要はない。本文を書き、疑問が出た場所で調査・追試へ戻る。

## リポジトリ衛生の保留事項

- Codex / Cursor等の外部GitHub Appのrepo別自動反応設定
- `work/first-hopfield-replication` の監査・整理
- `work/pages-bootstrap-final` のPages v2受理後の削除
- Public / Privateの最終方針
- main branch protection
- GitHub Pages設定

研究・物語制作を止めるblockerではないものは並行して扱う。

## 現在のwork branch

`work/pages-v2`

このbranchはPages v2の候補状態。`main` へはまだ反映していない。
