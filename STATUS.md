# 現在の状態

このファイルはプロジェクトの詳細な記憶ではなく、現在位置を示す索引です。詳細は各正本ファイルを参照します。

更新: 2026-08-20

## フェーズ

- プロジェクト段階: 小説・研究・Pagesの基本骨格と、ペルソナ駆動・世界状態・時系列eventの創発生成方式は `main` に受理済み
- 物語段階: `起 / 起`。本文0話。物語開始状態をBootstrapから同期生成する層を `work/story-bootstrap` で整備中
- 学習段階: CATCH_UP
- 研究段階: Hopfield 1982のReplication + Extension完了。以後は物語で必要になった箇所から前史調査・追加実験へ戻る
- 公開段階: GitHub Pagesは `main /docs` から公開中。連載読書導線へ再設計済み

## 主目的

**小説が主役。研究・追試は作品を現実に近づけるための制作工程。**

基本ループ:

**物語を書く → 技術的な疑問が出る → 原典を読む → 必要なら追試する → 理解を更新する → 小説へ戻す**

## 受理済みの物語生成方式

D-017は `ACTIVE`。

- ペルソナ定義: `novel/personas/`
- 世界・環境定義: `novel/environment.md`
- ペルソナの時系列状態: `novel/state/personas/`
- 世界の時系列状態: `novel/state/world.md`
- 時間上の結合event: `novel/events/`
- story time索引: `novel/timeline.md`
- 再帰的起承転結: `novel/structure.md`

ペルソナと世界は実体・状態領域として独立するが、時間方向には独立して進めず、共通eventとstory timeで因果的に更新する。

未来の完成プロットを各ペルソナへ配らない。各人物はその時点で知り得る局所状態から行動し、世界側が結果を解決する。

## 現在のBootstrap候補

D-018は `PROPOSED`。

`novel/bootstrap/` を、世界とペルソナ群を同じ背景から同期初期化・再初期化する層として追加している。

現在の候補同期点:

```text
BOOT-001 @ T0-MODERN @ none
```

- `BOOT-001`: `novel/bootstrap/BOOT-001-modern-opening.md`
- Target story time: `T0-MODERN`
- Parent event head: `none`
- `EVT-001`: まだ未発生

BOOT本文は全ペルソナへ共有しない。各人物の時代・立場・観測境界に応じて別々にprojectionする。

## BOOT-001から生成した初期状態

### World

`novel/state/world.md`

- 現代のモデル評価・調査環境
- run / prompt / output / logを扱える
- 必要になればcheckpoint差・対照条件を比較できる余地
- 1980年代研究者に関係する不完全な資料群
- 最初の異常・発見者・第1話終端は未確定

### Personas

同じ同期キーで次を生成済み。

- `state/personas/PER-001.md` — active
- `state/personas/PER-002.md` — standby
- `state/personas/PER-003.md` — active
- `state/personas/PER-004.md` — not-yet-instantiated

PER-005は1980年代側のstory timeに属するため、BOOT-001では状態を初期化していない。1980年代場面を実際に動かす際は別Bootstrapを作る。

## ペルソナ増加・増殖・再初期化

- 新しい独立主体が必要になれば `PER-006` 以降を追加する
- 背景に存在する全人物・組織を機械的にペルソナ化しない
- 同じstateから複数主体が独立経験を持ち始めた場合は別`PER-xxx`へforkする
- 再初期化時は `BOOT + story time + parent event head + state` から再構成し、設定の寄せ集めで作り直さない
- 再初期化は物語eventではなく、過去stateを上書きしない

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

L-002:

**「安定して収束した」ことは「意図した原像へ正しく戻った」ことを保証しない。**

Hopfieldは最初の研究・追試入口だが、第1話の冒頭をHopfield説明から始めるとは決めない。Hopfield以前の技術史も、PER-005や物語上の必要性が生じた時点で調査する。

## 長期探索仮説

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

### このbranchのレビュー後

1. `work/story-bootstrap` を人間レビューし、受理された場合 `main` へfast-forward
2. BOOT-001の`Unresolved slots`から、最初の相互作用に本当に必要な項目だけ具体化する
3. 特に「最初にPER-001 / PER-004へ与えられる具体task」を決めるか、背景から自然に導出する
4. 必要ならBOOT-001を更新し、world / persona stateを同じ同期キーで再生成する
5. 同期が成立した状態で最初の相互作用を実行する
6. 重要な状態変化が成立した場合のみ `EVT-001` として記録する
7. event群が読書単位を形成した段階で `novel/chapters/001.md` を書く

### 1980年代側

PER-005の具体化や1980年代sceneが必要になった時点で、Hopfield以前を含む実在研究者・一次資料を必要範囲だけ調査し、1980年代用Bootstrapを作る。

## リポジトリ衛生の保留事項

- `work/first-hopfield-replication` の監査・整理
- `work/pages-bootstrap-final` の削除
- `work/pages-v2` の削除
- `work/novel-reader-site` の削除
- `work/public-copy-cleanup` の削除
- `work/persona-environment-fractal-policy` の削除
- Public / Privateの最終方針
- main branch protection

## 現在のwork branch

`work/story-bootstrap`

Bootstrap同期層、BOOT-001、現代側初期world/persona stateを整備する候補branch。`main` にはまだ反映していない。
