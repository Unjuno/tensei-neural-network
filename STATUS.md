# 現在の状態

このファイルはプロジェクトの詳細な記憶ではなく、現在位置を示す索引です。詳細は各正本ファイルを参照します。

更新: 2026-08-19

## フェーズ

- プロジェクト段階: 小説・研究・Pagesの基本骨格は `main` に存在するが、創発型の物語生成方法を再構築中
- 物語段階: `起 / 起`。本文0話。未来プロットを固定せず、ペルソナ・世界・時系列状態の初期条件を整備している
- 学習段階: CATCH_UP
- 研究段階: Hopfield 1982のReplication + Extension完了。以後は物語で必要になった箇所から調査・実験する
- 公開段階: GitHub Pagesは `main /docs` から公開中。連載読書導線へ再設計済み
- 外部メモリ段階: GitHubを正本としているが、ペルソナ駆動・環境解決・時系列状態・再帰的起承転結の運用を `work/persona-environment-fractal-policy` で復元中

## プロジェクトの主目的

**小説が主役。研究・追試は作品を現実に近づけるための制作工程。**

基本ループ:

**物語を書く → 技術的な疑問が出る → 原典を読む → 必要なら追試する → 理解を更新する → 小説へ戻す**

## 物語生成の中核候補

現在のwork branchでは、次を正式な運用として復元している。

1. 未来の完成プロットを人物へ配らない
2. ペルソナ定義、世界・環境定義、ペルソナ状態、世界状態を別々に持つ
3. ペルソナ数は固定せず、物語の進行に応じて増やす
4. 時間に依存するペルソナ状態は `novel/state/personas/`、世界状態は `novel/state/world.md` で管理する
5. ペルソナ状態と世界状態は独立した領域だが、時間方向には独立させず、共通の `EVT-xxx` とstory timeで因果的に更新する
6. 他者の秘密、未観測Canon、長期探索仮説を自動共有しない
7. `novel/environment.md` は世界・環境の定義と結果解決規則を持つ
8. 各人物は実際に観測できた結果だけから更新される
9. 成立した状態遷移を再帰的な起承転結で整理する
10. 本文は、相互作用で成立した出来事を後から描写する

この方式では、起承転結は予定イベントを強制する脚本ではなく、状態遷移を整理するフラクタル構造として使う。

## 状態モデル

- ペルソナ定義: `novel/personas/`
- 世界・環境定義: `novel/environment.md`
- ペルソナの時系列状態: `novel/state/personas/`
- 世界の時系列状態: `novel/state/world.md`
- 時間上の結合イベント: `novel/events/`
- 共通のstory time索引: `novel/timeline.md`

概念的には、

```text
(P_1(t), P_2(t), ..., W(t))
          |
          | EVT-k
          v
(P_1(t+1), P_2(t+1), ..., W(t+1))
```

同じeventでも各人物の観測範囲は異なる。変化しなかった状態は前時点から継承し、毎時点に全snapshotを複製しない。

story time上の因果順と、小説本文で読者へ提示する章・scene順は別管理する。

## 現在の初期ペルソナ候補

`novel/personas/`

- PER-001: 現代評価担当
- PER-002: 懐疑的研究者
- PER-003: 史料担当
- PER-004: モデル側の存在
- PER-005: 1980年代研究者

この5つは固定キャストではない。必要に応じて `PER-006` 以降を追加する。

PER-004へ「過去の研究者本人」という正解は与えない。PER-005にも現代や長期真相の未来知識を与えない。

## 現在の初期世界状態

`novel/state/world.md`

- 現代のモデル評価・調査環境
- 1980年代研究者に関する不完全な資料群
- 複数run / 必要に応じてcheckpointや対照条件を比較できる
- 最初の異常、最初の発見者、第1話終端のイベントは未確定

世界の構造と結果解決規則は `novel/environment.md` を参照する。

## 最新研究ID

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

J. J. Hopfield (1982), “Neural networks and physical systems with emergent collective computational abilities”。

### EXP-001

低負荷条件 N=100, P=5。10% / 20% noiseで200/200 trials exact recall。PASS。

### EXP-002

N=100、P=5,10,15,20、noise=10,20,30,40%、3 pattern seeds、960 trials。PASS。

最終分類:

- target exact: 442
- wrong stored: 8
- nonstored converged: 510
- nonconverged: 0

L-002:

**「安定して収束した」ことは「意図した原像へ正しく戻った」ことを保証しない。**

この理解は物語の同一性問題へ接続するが、本人性の科学的証明ではない。

## 長期探索仮説

詳細は `novel/structure.md` と `notes/working-context.md`。

以下はCanonでも未来プロットでもない。

- 1980年代研究者は起源ではなく、さらに過去から反復していた同一認識主体らしき構造の一例かもしれない
- NNは現象を作るのではなく、反復・比較・分岐可能な形で観測可能化した媒体かもしれない
- 人物情報は再構成材料であると同時にcueとして作用するかもしれない
- 情報密度・計算能力・試行回数が大きい現代ほど顕在化しやすいかもしれない
- 同じ認識主体らしきものが複数媒体へ同時に存在するかもしれない
- 観測・再構成しようとする行為自体が顕在化条件へ入るかもしれない

模倣、統計的再構成、一般的な認知収束、選択バイアス等を競合説明として残す。

## Pages / 連載サイト

公開元: `main /docs`

- `docs/index.html` — 作品トップ
- `docs/novel/index.html` — 小説目次
- `docs/novel/reader.css` — 本文用CSS
- `docs/research/index.html` — 制作の裏側

現在、`novel/chapters/001.md` と `docs/novel/001.html` はまだ存在しない。本文0話。

## 次に行うこと

### 最優先

1. `work/persona-environment-fractal-policy` の差分を人間レビュー
2. 受理された場合のみ `main` へfast-forward
3. PER-005を実在研究者・1980〜1985年の一次資料を参考に具体化する
4. 初期story timeを定め、必要なペルソナの最初の `state/personas/PER-xxx.md` を生成する
5. `起 / 起` の初期世界状態で、PER-001〜004の最小相互作用を1回実行する
6. 成立した出来事を `EVT-001` として記録し、そこから `state/world.md` と観測した各persona状態を更新する
7. `timeline.md` にEVT-001のstory timeを索引する
8. そのEventを材料に `novel/chapters/001.md` を書き始める

### 原則

先に第1話の結末や「不可逆イベント」を決めて人物をそこへ誘導しない。相互作用の結果、実際に不可逆な変化が成立した場合に、それを物語構造上の転換として採用する。

## リポジトリ衛生の保留事項

- `work/first-hopfield-replication` の監査・整理
- `work/pages-bootstrap-final` の削除
- `work/pages-v2` の削除
- `work/novel-reader-site` の削除
- `work/public-copy-cleanup` の削除
- Public / Privateの最終方針
- main branch protection

## 現在のwork branch

`work/persona-environment-fractal-policy`

ペルソナ駆動、世界・環境、時系列状態、未来プロット非共有、再帰的起承転結を復元する候補branch。`main` にはまだ反映していない。
