# 現在の状態

このファイルはプロジェクトの詳細な記憶ではなく、現在位置を示す索引です。詳細は各正本ファイルを参照します。

更新: 2026-08-20

## フェーズ

- プロジェクト段階: 小説・研究・Pagesの基本骨格と、ペルソナ駆動・世界状態・時系列eventの創発生成方式は `main` に受理済み
- 物語段階: `起 / 起`。本文0話。導入背景から1980年代側を同期初期化する候補状態まで到達
- 学習段階: CATCH_UP
- 研究段階: Hopfield 1982のReplication + Extension完了。Hopfield以前の哲学・思想・技術史背景を `research/pre-hopfield-background.md` で調査中
- 公開段階: GitHub Pagesは `main /docs` から公開中。今回の導入原型はPages本文へ公開していない

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

## Bootstrap候補

D-018は `PROPOSED`。

Bootstrapは、物語として読めるOpening / Background frameを含み得る同期初期化層として運用候補になっている。

BOOT IDは作成順の識別子であり、story time / narrative orderではない。

### 1980年代側

```text
BOOT-002 @ T0-1980S @ none
```

- `BOOT-002`: `novel/bootstrap/BOOT-002-1980s-opening.md`
- Narrative role: 物語最初の実働開始点候補
- Target story time: `T0-1980S`
- 時代: 1984〜1985年前後を中心候補
- World: `novel/state/world.md` の `T0-1980S`
- Persona: `novel/state/personas/PER-005.md`
- 最初の1980年代event: 未発生

BOOT-002のOpening frameには、記憶・想起・自己同一性をめぐる古い問いから、20世紀のnetwork・feedback・安定状態、1980年代初頭のcollective dynamicsへ接続する導入原型を置いた。

これは哲学史と技術史を一本の直接系譜だと断定するものではなく、作品上の共鳴と実際の技術継承を分離する。

### 現代側

```text
BOOT-001 @ T0-MODERN @ none
```

- `BOOT-001`: `novel/bootstrap/BOOT-001-modern-opening.md`
- Target story time: `T0-MODERN`
- World: `novel/state/world.md` の `T0-MODERN`
- Personas: PER-001〜004

現代側は後の時代同期点として保持する。1980年代側のPER-005状態を混ぜない。

## PER-005 初期化状態

`novel/state/personas/PER-005.md`

状態: `ACTIVE / PROVISIONAL`

PER-005は現在、次の初期条件を持つ。

- 記憶を静的な保存だけでなくnetwork全体の状態・相互作用・安定性から捉える可能性を考える
- 不完全な状態から安定状態へ移る現象に研究価値を見る
- 「収束した」と「正しい原像へ戻った」を分けて考える
- これを意識・人格・魂・転生と直ちに同一視しない
- 第一目的は「記憶が戻るとはnetwork上で何が起きることか」を実験可能な形へ落とすこと
- 現代AI、輪廻仮説、自分の将来を知らない

氏名、所属、年齢、具体的な計算環境、読了済み一次文献はまだ固定していない。

## ペルソナ増加・増殖・再初期化

- 現時点では1980年代側の新規ペルソナを追加していない
- 最初の相互作用に独立した観測・目的・判断が必要になった時点で `PER-006` 以降を追加する
- 同じstateから複数主体が独立経験を持ち始めた場合は別`PER-xxx`へforkする
- 再初期化時は `BOOT + story time + parent event head + state` から再構成する
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

## 背景調査

`research/pre-hopfield-background.md` を作業台帳とする。

現在の調査軸:

- 哲学的・概念的背景: 記憶、想起、personal identity
- 神経・情報処理の形式化: McCulloch–Pitts、Hebb、Wiener、Ashby等
- network上の学習・連想記憶: Rosenblatt、Anderson、Amari、Kohonen等
- persistent state / statistical physics: LittleからHopfieldへ

直接系譜と物語上の思想的共鳴を混同しない。

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

現在、`novel/chapters/001.md` と `docs/novel/001.html` はまだ存在しない。本文0話。

今回のOpening frameはBootstrap内部の制作原型であり、Pages本文へ同期していない。

## 次に行うこと

### 最優先

1. PER-005が `T0-1980S` で実際に知っている一次文献・用語の範囲を必要最小限調査する
2. 1984〜1985の研究環境で最初の実験を実行可能にするため、計算機・研究室条件を必要範囲だけ具体化する
3. その結果からPER-005の最初の研究行動を生成する
4. 他者との独立相互作用が必要なら、その時点で `PER-006` を追加・初期化する
5. 意味のある状態変化が成立した場合のみ、1980年代側の最初の `EVT-xxx` を記録する
6. event群が読書単位を形成した段階で第1話本文へ投影する

### branch review

`work/story-bootstrap` はまだ `main` に未反映。D-018は人間受理・main反映までは `PROPOSED` のままとする。

## リポジトリ衛生の保留事項

- `work/first-hopfield-replication` の監査・整理
- obsoleteな旧Pages/work branchの整理
- `work/persona-environment-fractal-policy` の削除
- Public / Privateの最終方針
- main branch protection

## 現在のwork branch

`work/story-bootstrap`

Bootstrap同期層、1980年代導入原型、BOOT-002、PER-005と1980年代worldの初期状態を整備中。`main` にはまだ反映していない。
