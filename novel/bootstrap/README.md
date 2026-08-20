# 物語Bootstrap

このディレクトリは、あるstory timeで**世界とペルソナ群を同じ背景から同期初期化・再初期化するためのBootstrap Frame**を管理します。

Bootstrapは未来の筋書きではありません。物語開始時や大きな時代・環境の切替時に、その時点までに成立している背景を一つの初期化源へまとめ、世界状態と各ペルソナ状態へ異なる情報境界で射影するための制作上の同期点です。

Bootstrapの中心には、必要に応じて**物語として読める導入原型（Opening frame）**を置けます。これは読者向け公開本文そのものとは限らず、歴史・思想・技術背景を一つの文脈へ圧縮して、その時点の世界と人物を同時に立ち上げるための入力として使います。

## IDと物語順

`BOOT-001`, `BOOT-002` ... は安定識別子であり、**story timeやnarrative orderを表しません。**

後から作成した `BOOT-002` が、物語上は `BOOT-001` より前の時代を初期化しても構いません。

## 基本モデル

Bootstrap Frameを `B_k`、対象story timeを `t` とします。

```text
B_k
 ├─ opening/background frame
 ├─ world projection          -> W(t)
 ├─ persona discovery        -> PER-xxx definitions as needed
 ├─ PER-001 projection       -> P_001(t)
 ├─ PER-002 projection       -> P_002(t)
 └─ ...
```

概念的には、

```text
W(t)     = InitWorld(B_k)
P_i(t)   = InitPersona_i(Project_i(B_k))
```

同じBootstrapを使っても、各ペルソナが同じ情報を知るわけではありません。`Project_i` は、その人物の時代、立場、権限、観測可能性、既存記憶に応じて情報を制限します。

## Bootstrapが保持するもの

各 `BOOT-xxx` は最低限、次を持ちます。

- `Target story time`: 初期化対象の物語時刻
- `Parent event head`: その時点までに成立済みの最後のevent。物語開始時は `none`
- `Authority inputs`: Canon、既存world/persona state、timeline、必要な研究根拠
- `Opening / Background frame`: その時点までに成立している背景を圧縮した導入
- `World projection`: 世界状態へ反映する客観情報
- `Persona discovery`: 独立状態を持つ主体として必要なペルソナ
- `Persona projections`: 各ペルソナへ渡せる情報
- `Forbidden leakage`: 各ペルソナへ渡してはいけない情報
- `Outputs`: 初期化・再初期化したstateファイル
- `Unresolved slots`: まだ決めなくてよい事項

Opening frameは歴史的・哲学的背景を含められますが、**作品上の共鳴と現実の直接的な学説系譜を混同しません。** 技術史として重要な主張は `research/` と `references/` へ戻って確認します。

## Bootstrapに入れないもの

- まだ成立していない未来event
- 第1話や長期プロットの予定された結末
- 「この人物は後でこう考える」のような未来の信念状態
- 読者を驚かせるためだけの演出指示
- ペルソナ自身が知り得ない作者側の探索仮説を、そのペルソナ向けprojectionへ混ぜたもの

Canonに将来扱うことが記録されていても、それを現在世界で既に成立済みの事実へ変換しません。

## 初期化手順

1. 対象story timeと`Parent event head`を確定する。
2. `canon.md`、`timeline.md`、対象時点までのevent/state、必要な研究根拠と矛盾しないOpening / Background frameを作る。
3. 背景から世界状態へ反映すべき客観情報を抽出する。
4. 独立した目的・認知・観測境界・状態履歴が必要な主体を抽出し、必要なら新しい`PER-xxx`を作る。
5. 各ペルソナについて、その人物が対象時点で知り得る情報だけをprojectionする。
6. `state/world.md` と `state/personas/PER-xxx.md` を同じ同期キーで初期化する。
7. 未来知識、他者の秘密、異なるstory timeの状態が漏れていないか検査する。

同期キーは概念的に次で扱います。

```text
BOOT-xxx @ <story time> @ <parent event head>
```

## ペルソナの増加

Bootstrapから新しい人物・モデルinstance・組織的主体の必要性が見つかった場合、既存キャストへ無理に役割を押し込まず、新しい`PER-xxx`を追加できます。

ただし、背景に名前が出るだけの人物や組織をすべてペルソナ化しません。独立した局所知識、目的、観測、判断、状態履歴を追跡する必要がある主体だけをペルソナにします。

## 増殖・fork

同じモデルinstance、checkpoint、人物状態等が物語上で複数へ分岐する場合、同時に独立した経験を持ち始める時点から別の`PER-xxx`として扱います。

```text
P_A(t)
  ├─ PER-A at t+
  └─ PER-B at t+
```

分岐した二つへ同じIDを使い続けません。各子ペルソナは、どの親状態・story time・event headから分岐したかを記録します。

## 再初期化

長い中断、別AIセッション、モデル交換等でペルソナを再生成するときは、現在の設定を寄せ集めて作り直しません。

必ず、

- 対象Bootstrap
- 対象story time
- parent event head
- その時点までのpersona state
- world state

を揃えて再構成します。

再初期化は物語世界で起きた出来事ではないため、それ自体を`EVT-xxx`にはしません。再初期化によって過去のstate履歴を書き換えることも禁止します。

## 時代をまたぐ場合

一つのBootstrapには原則として**一つのtarget story time**を置きます。

現代の開始状態を作る`BOOT-001`の背景に1980年代の事実が含まれていても、1980年代のPER-005の状態を現代時点へ初期化するわけではありません。1980年代側は `BOOT-002` のように、その時代をtarget story timeにした別Bootstrapから初期化します。

これにより、背景知識として過去を参照することと、過去時点の人物状態を現在へ混ぜることを分離します。
