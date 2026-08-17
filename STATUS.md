# 現在の状態

このファイルはプロジェクトの詳細な記憶ではなく、現在位置を示す索引です。詳細は各正本ファイルを参照します。

## フェーズ

- プロジェクト段階: CATCH_UP実作業開始
- 物語段階: 第1話設計前
- 学習段階: CATCH_UP — 第1テーマの原典確認・追試完了
- 研究段階: Hopfield型連想記憶の第1追試完了

## 現在のwork branch

- `work/first-hopfield-replication`
- PRは作成しない
- `main` とのcompareを人間が確認後、承認された場合のみ `main` へfast-forwardする

## Active ID

- Q: `Q-001` — ANSWERED
- H: `H-001` — SUPPORTED（限定条件）
- EXP: `EXP-001` — PASS
- F: `F-001` — PROVISIONAL
- L: `L-001` — 未反映

## 第1テーマ

**Hopfield型連想記憶 / attractor dynamics**

選定理由:

- 1980年代から始める作品・学習構造に合う
- 主人公候補の研究年代1984–1985と強く接続する
- 部分状態から全体を再構成するという物語の中心概念に直結する
- 一般的なPCで軽量に追試できる
- 後のgraded-response、RNN、attention、現代的associative memoryとの比較基準になる

## 第1テーマで追加したもの

### 原典

- `REF-001`: Hopfield (1982), *Neural networks and physical systems with emergent collective computational abilities*
- `REF-002`: Hopfield (1984), *Neurons with graded response have collective computational properties like those of two-state neurons*

### 問い・仮説

- `Q-001`: Hopfield型連想記憶の中核挙動は単純な現代実装で再現できるか → ANSWERED
- `H-001`: N=100, P=3, 20%破損cue等の事前条件で固定点・95%以上の復元・非増加energyが得られる → SUPPORTED

### 実験

- `EXP-001`: `experiments/EXP-001-hopfield-core/`
- 種別: core-mechanism Replication
- 判定: **PASS**

初回結果:

- 保存パターン固定点: 3 / 3
- exact recovery: 150 / 150 (100%)
- energy increase (`ΔE > 1e-10`): 0回
- 全trial収束: 150 / 150
- 最大sweeps: 2
- 実行環境: Python 3.13.5 / NumPy 2.3.5 / Linux x86_64

### Finding

- `F-001`: 低負荷の二状態Hopfield実装で中核的な連想記憶挙動を再現した
- 状態: PROVISIONAL
- 独立環境・別seed・高負荷条件への一般化はまだしない

### 作者学習

- `L-001`: 「アトラクタへ戻る」を比喩だけでなく実装として理解する
- 重要点: Hopfieldのenergyは無次元Lyapunov関数であり、物理的エネルギー[J]や現代NNのtraining lossと同一ではない
- 作品への反映: 未反映

## リポジトリ衛生状況

### 完了

- 初期設計PR #1は `main` へmerge済み
- `main` を人間が受理した正本として定義済み
- `.github/workflows/` は存在しない
- GitHub Actions workflow run は確認時点で0件
- 自動起動はGitHub Actions CIではなく、PRイベントに反応した外部GitHub Appであることを確認
- 内部作業は `work branch → compare → 人間承認 → main fast-forward` とし、通常の内部作業ではPRを使わない

### 非ブロッキングの要対応

- Codex / Cursorのrepo別自動レビュー設定を必要に応じて整理する
- merge済みの `bootstrap/repository-design` branchを削除する
- repository visibilityが現在Publicのため、このまま公開運用するかPrivateへ戻すか決める
- `main` のbranch protectionは未設定

これらは現在の研究・小説制作開始をブロックしない。

## 次に行うこと

1. `work/first-hopfield-replication` と `main` の差分を確認する
2. 承認後、このbranchを `main` へfast-forwardする
3. `L-001` を使い、主人公研究者の専門・1984–1985前後の位置づけを具体化する
4. `novel/structure.md` で第1話の最初の状態遷移を設計する
5. 第1話に必要な範囲で、次の技術調査またはExtensionを選ぶ

実験を増やすこと自体を目的にせず、研究結果を物語へ接続してから次へ進む。

## 参照順

1. `README.md` — プロジェクト目的
2. `AGENTS.md` — AI作業規則
3. `STATUS.md` — 現在位置
4. `POLICY.md` — 正本・優先順位・研究判定

作業別の詳細な参照順は `AGENTS.md` に従います。
