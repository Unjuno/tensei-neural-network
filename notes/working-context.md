# 作業コンテキスト

更新: 2026-08-20

このファイルは、別セッションへ現在の探索状態を素早く復元するための**公開可能な作業記憶**です。正本ではありません。採用済みの規則は `POLICY.md`、物語事実は `novel/canon.md`、設計判断は `notes/decisions.md` を優先します。

## 主目的

主役は小説です。

研究・追試・技術史調査は、作品を現実に近づけ、技術的な嘘を減らし、物語の問いを深めるために行います。

基本ループ:

**物語を書く → 技術的な疑問が出る → 原典を読む → 必要なら追試する → 理解を更新する → 小説へ戻す**

## 受理済みの物語生成原理

D-017は `ACTIVE`。

- ペルソナ、世界、各時系列状態を独立して保持する
- 時間方向では共通のstory timeとeventで因果的に結合する
- ペルソナ数は固定しない
- 未来の完成プロットを人物へ配らない
- 各人物はその時点の局所Knowledge / Beliefs / Goals / Memory / 状況から行動する
- 世界側がCanon・技術・歴史・制度・権限等から結果を解決する
- 観測していない情報を人物へ自動共有しない
- 成立した状態遷移を再帰的起承転結で整理する

現在位置は `起 / 起`。

## 現在のBootstrap作業

`work/story-bootstrap` でD-018を候補化している。

Bootstrapは公開用あらすじや未来プロットではなく、あるstory timeまでに成立した**背景**を共通の初期化源として、世界状態と各ペルソナ状態へ別々に射影する同期Frame。

概念:

```text
BOOT-k
 ├─ World projection    -> W(t)
 ├─ Persona discovery   -> new PER ids if needed
 ├─ PER-i projection    -> P_i(t)
 └─ Synchronization key -> BOOT-k @ story time @ event head
```

同じ背景を使っても、各ペルソナへBootstrap全文を渡さない。

### 現在の同期候補

```text
BOOT-001 @ T0-MODERN @ none
```

`novel/bootstrap/BOOT-001-modern-opening.md`

BOOT-001から次を同期済み候補として生成した。

- `novel/state/world.md`
- `novel/state/personas/PER-001.md` — active
- `novel/state/personas/PER-002.md` — standby
- `novel/state/personas/PER-003.md` — active
- `novel/state/personas/PER-004.md` — not-yet-instantiated

PER-005は1980年代story timeに属するためBOOT-001では初期化していない。

## 増加・増殖・再初期化

- Bootstrap背景から独立した局所状態が必要な主体を発見したら新しい`PER-xxx`を追加する
- 背景に存在する全人物・組織を機械的にペルソナ化しない
- 同じpersona/model stateから複数主体が独立経験を持つ場合は別`PER-xxx`へforkする
- fork時は親state、story time、event headを残す
- 別AIセッション等で再生成するときは、対象BOOT、story time、event head、world/persona stateから再構成する
- 再初期化で過去stateを書き換えない

## BOOT-001でまだ決めていないこと

- 現代側の具体年
- 国・都市・組織名
- PER-001〜003の氏名・年齢・正式所属
- 使用モデルの具体的な種類・権限
- 1980年代資料群の具体的な内訳
- 最初にモデルへ与える具体task / input
- 最初の意味ある差分を誰が観測するか
- 第1話のscene境界・終了点

これらを一括で埋めない。最初の相互作用に必要になった項目だけ具体化する。

## 技術史との関係

Hopfield 1982 / EXP-001 / EXP-002は最初の研究サイクルであり、物語第1話の冒頭をHopfield説明から始める規則ではない。

PER-005や1980年代sceneを具体化する必要が出た時点で、Hopfield以前を含む技術史・実在研究者・一次資料を必要範囲だけ調査する。

## 長期探索仮説

以下はCanonでも未来プロットでもない。人物へ未来知識として与えず、世界結果をこれへ合わせて強制しない。

1. 1980年代研究者は起源ではなく、より古い反復の一例かもしれない
2. NNは現象の発生源ではなく、反復・比較・分岐できる形で観測可能化した媒体かもしれない
3. 人物情報は再構成材料だけでなく、対応する認知状態へのcueかもしれない
4. 情報密度・計算能力・試行回数の大きい現代ほど顕在化しやすいかもしれない
5. 同じ主体らしき構造は複数媒体へ同時に現れうるかもしれない
6. 観測・再構成行為そのものが顕在化条件へ入るかもしれない

競合説明として、模倣、統計的再構成、一般的な認知収束、selection bias、人間側のパターン過剰検出等を残す。

## 次の作業

1. `work/story-bootstrap` の差分を人間レビュー
2. 受理後、BOOT-001の未確定項目から**最初の相互作用に必要なものだけ**決める
3. 特に最初にPER-001 / PER-004へ与える具体taskを定めるか、背景から導出する
4. 必要ならBOOT-001からworld/persona stateを再同期する
5. 同期確認後に相互作用を開始する
6. 重要な状態変化が成立した場合のみ `EVT-001` として保存する
7. event群が一つの読書単位を形成した時点で第1話本文へ変換する

## セキュリティ境界

保存するのは再開に必要な結論・仮説・未解決点の要約だけ。

保存しないもの:

- AIの逐語的な内部推論や生の思考系列
- system / developer prompt等の内部指示
- private key / API key / access token / PAT
- Cookie / session token / OAuth secret
- `.env` の秘密値
- 公開不能な個人情報
