# 現在の状態

このファイルはプロジェクトの詳細な記憶ではなく、現在位置を示す索引です。詳細は各正本ファイルを参照します。

## フェーズ

- プロジェクト段階: 初期設計完了・最初の研究→学習→物語接続サイクルを構築済み
- 物語段階: 第1話の技術的な核と中心緊張を設計済み・本文未着手
- 学習段階: CATCH_UP
- 研究段階: Hopfield 1982のReplication + Extension完了・次テーマ選定前
- 公開段階: GitHub Pagesの準備を始められる最小公開単位に到達

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
- 第1話の技術的な核: content-addressable memory / attractor
- 中心の緊張:
  - 部分から全体が戻る ≠ 同一人物が戻る
  - 状態が安定している ≠ 原像を正しく復元している
- 第1話の不可逆イベント候補:
  - 欠けた研究者関連入力から、モデルが複数試行で同じ人物像・未完の研究テーマへ収束する
  - 対照条件と比べても異常な一貫性があり、研究チームが正式な検証対象として扱わざるを得なくなる

このイベントはまだCanonではなく `novel/structure.md` 上の候補。

## 実験artifact上の注意

EXP-002は事前計画で960-row `results/trials.csv` のcommitを予定したが、現在のGitHub書き込み経路で大きな単一テキストの取り回しが不安定だったため、branchには `grid.csv`、`summary.json`、決定論的 `run.py`、実行時raw CSV hashを保存した。

実験条件・trial数・判定基準は変更していない。rawを再生成する場合はEXP-002 README記載のSHA-256と照合する。

## GitHub Pages

最小公開単位として、

**原典 → Replication → Extension → Finding → 作者の理解更新 → 第1話構造への反映**

の1サイクルが揃ったため、GitHub Pagesの準備を始めてよい段階に到達した。

ただし現在の成果は `work/exp-001-hopfield` branch上の候補状態であり、Pagesの公開元を `main` にするなら、先に人間レビューとmainへの反映を行う。

Pages設定時の最小公開内容候補:

1. プロジェクト概要
2. 「小説 × 追試 × 学習」の流れ
3. REF-001 / EXP-001 / EXP-002の短い結果
4. 科学的に言えること / 言えないこと
5. 小説側は第1話本文公開前なら、ネタバレを抑えたコンセプトだけ

サイト専用の重いframeworkはまだ不要。Pages設定方法を決める段階で最小構成を選ぶ。

## リポジトリ衛生の保留事項

- Codex / Cursor等の外部GitHub Appのrepo別自動反応設定
- merge済み `bootstrap/repository-design` branchの削除
- Public / Privateの最終方針
- main branch protection
- GitHub Pages設定

研究・物語制作を止めるblockerではないものは並行して扱う。

## 次に行うこと

### 人間レビュー後

1. `work/exp-001-hopfield` の研究・物語接続差分を確認
2. 明示承認された場合のみmainへfast-forward
3. main反映後、GitHub Pages設定へ進める

### 次の研究候補

- 保存パターンと一致しない収束状態の構造解析
- Perceptron等へ戻って技術史をspiralに補完
- 1984–1985の連想記憶・連続値network原典を追加し、主人公研究者の年代・専門を固める

### 次の物語候補

- 主人公研究者の年代・専門をPROVISIONAL以上で決める
- 第1話の視点人物を決める
- 最初の「欠けた入力」と対照条件を具体化する
- 第1話終端の不可逆イベントを確定する

## 現在のwork branch

`work/exp-001-hopfield`

このbranchは候補状態。`main` へはまだ反映していない。

## Cold Start

1. `README.md`
2. `AGENTS.md`
3. `STATUS.md`
4. `POLICY.md`

作業別の詳細参照順は `AGENTS.md` に従う。
