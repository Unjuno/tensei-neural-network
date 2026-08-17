# 現在の状態

このファイルはプロジェクトの詳細な記憶ではなく、現在位置を示す索引です。詳細は各正本ファイルを参照します。

## フェーズ

- プロジェクト段階: 初期設計完了・第1研究サイクル完了候補をレビュー待ち
- 物語段階: 第1話の技術的な核を設計済み・本文未着手
- 学習段階: CATCH_UP
- 研究段階: Hopfield 1982の第1追試完了・次Extension設計前

## Active ID

- Q: Q-001 — ANSWERED
- H: H-001 — SUPPORTED（宣言条件に限定）
- EXP: EXP-001 — PASS
- F: F-001 — PROVISIONAL
- L: L-001 — 一部反映

## 現在の成果

### REF-001
J. J. Hopfield (1982), “Neural networks and physical systems with emergent collective computational abilities” を第1原典として登録。

### Q-001
低負荷Hopfield networkで、乱されたcueから保存パターンへのcontent-addressable recallを再現できるかを問い、EXP-001の宣言条件の範囲で `ANSWERED` とした。

### H-001
N=100、P=5、10% / 20% bit反転という操作条件で高率にexact recallできるという仮説。EXP-001の有効な事前登録結果を根拠に、宣言条件へ限定して `SUPPORTED` とした。

### EXP-001
`experiments/EXP-001-hopfield-associative-memory/`

- 事前登録後に実行
- 10% noise: 100/100 exact recall
- 20% noise: 100/100 exact recall
- 200/200 trialsが収束
- 最大observed sweeps: 2
- 事前判定: PASS
- `results/summary.json`, `trials.csv`, `patterns.csv` を保存

### F-001
低負荷・固定pattern setの条件では、保存パターンがattractorとして働き、乱れたcueから元状態へ戻るcontent-addressable recallを実装上確認した、という範囲に限定した `PROVISIONAL` Finding。

### L-001
作者の理解を「記憶を保存場所から検索する」から「乱れた現在状態が重みで定められた地形を動き、安定状態へ戻る」という状態遷移中心の理解へ更新。

この理解は `novel/structure.md` の第1話設計へ一部反映済み。

## 物語側の現在位置

- 再帰的起承転結: `起 / 起`
- 第1話の技術的な核: attractor / content-addressable memory
- 中心の緊張: **「部分から全体が戻る」ことと「同一人物が戻った」ことは同じではない**
- 次の不可逆イベント候補: 欠けた研究者関連入力から、モデルが複数試行で同じ人物像・研究テーマへ収束する異常を観測する

上記イベントはまだCanonではなく、`novel/structure.md` 上の制作候補。

## リポジトリ衛生状況

### 完了

- 初期設計PR #1は `main` へmerge済み
- `main` を人間が受理した正本として定義済み
- `.github/workflows/` は存在しない
- GitHub Actions workflow run は確認時点で0件
- PRイベントに反応した処理はGitHub Actions CIではなく外部GitHub Appと確認済み
- 内部AI作業はPRではなくwork branch比較でレビューする運用へ変更済み
- open PRは0件

### 要対応・保留

- Codex自動Code Review / GitHub Appアクセスのrepo別無効化または対象外化
- Cursor GitHub Appのrepo別PRフック無効化または対象外化
- merge済み `bootstrap/repository-design` branchの削除
- Public / Privateの最終方針
- main branch protection方針
- GitHub Pages設定

これらのうちUI設定が必要なものは、研究・作品の制作を止めるblockerではない限り並行して扱う。

## 次の研究候補

EXP-001は低負荷条件で100% recallとなり、attractor basinの境界を見るには容易すぎた。

次は別IDで、少なくとも次のどれかをExtensionとして事前登録する。

1. 記憶負荷 `P/N` を増やす
2. bit反転noiseを20%より増やす
3. 複数pattern seedsで再確認する
4. spurious attractorへの収束率を測る

第1候補は、**負荷とnoiseの2軸を粗く掃引して回復境界を可視化する軽量Extension**。

## 次の物語作業

1. 主人公研究者の専門を連想記憶 / attractor周辺でPROVISIONALにするか判断
2. 1982–1985のどの時点を主人公の研究史の核にするか原典を追加確認
3. 第1話の視点人物を決める
4. 「通常の補完」と「異常な一貫性」をどう比較するか物語内の観測条件を作る
5. 第1話の不可逆イベントを確定して本文へ進む

## GitHub Pagesへ進む目安

次のどちらかを満たしたら、公開導線を作る価値がある。

- 第1話または公開可能な導入本文が1本できる
- EXP-001に加えてExtension 1本が揃い、「原典 → 追試 → 学び → 物語」の1サイクルを読者へ見せられる

現時点でもPagesの技術設定は可能だが、空のサイトを先に作るより、上記の最小公開単位を揃えてから設定する方針を推奨する。

## 現在のwork branch

`work/exp-001-hopfield`

このbranchは候補状態。`main...work/exp-001-hopfield` の比較を人間が確認し、明示承認された場合のみmainへfast-forwardする。

## 参照順

1. `README.md` — プロジェクト目的
2. `AGENTS.md` — AI作業規則
3. `STATUS.md` — 現在位置
4. `POLICY.md` — 正本・優先順位・研究判定

作業別の詳細な参照順は `AGENTS.md` に従います。
