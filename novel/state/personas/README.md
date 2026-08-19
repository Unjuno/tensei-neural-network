# ペルソナ状態履歴

ここには、各ペルソナの**時間に依存する可変状態**を保存します。

`../../personas/PER-*.md` は人物の定義・初期条件です。このディレクトリは、その人物が物語中でどう変化したかを記録します。

## 初期化と同期

ペルソナ状態を新しく作る、長い中断後に再生成する、別AIセッションで復元する場合は、`../../bootstrap/` のBootstrap Frameを使います。

初期状態には最低限、次を記録します。

```text
- Bootstrap: BOOT-xxx
- Synchronization key: BOOT-xxx @ <story time> @ <parent event head>
- Parent event head:
- Active:
```

同じstory timeで同期する世界状態とペルソナ状態は、同じBootstrap / story time / parent event headを参照します。

Bootstrap本文をペルソナへ丸ごと与えてはいけません。各人物の時代・立場・権限・観測境界に応じたprojectionだけをKnowledge等へ反映します。

## 形式

各人物ごとに `PER-xxx.md` を作り、重要な状態変化を時系列で追記します。

```text
## <story time / event id>

- Knowledge:
- Beliefs:
- Goals:
- Cognitive style:
- Relations:
- Memory:
- Situational state:
- 根拠となるイベント:
```

全項目を毎回複製する必要はありません。変更のない項目は前状態から継承できます。

ただし後から状態を復元できなくなるほど省略してはいけません。

## 原則

- 状態変更は、原則としてイベントまたは明示された時間経過から生じる
- 他者の秘密を、観測イベントなしにKnowledgeへ追加しない
- 誤認が訂正されても、過去に誤認していた事実は履歴から消さない
- persona definitionを書き換えて過去の状態変化を隠さない
- 人格・認知スタイル自体が長期的に変化した場合も、定義を無言で上書きせず時系列変化として残す
- 死亡、離脱、休眠、checkpoint分岐等でactiveでなくなっても履歴は残す
- 再初期化で過去stateを上書きしない

## 新規ペルソナ

ペルソナ数は固定しません。

新しい人物・モデルinstance・組織的主体などが物語上必要になったら、新しい安定ID `PER-xxx` を割り当てます。状態履歴は、その主体が時系列上で実際に登場・成立した時点から開始します。

Bootstrapの背景から新しい主体が必要だと分かった場合は、`../../bootstrap/README.md` のPersona discovery規則に従います。

## fork / 増殖

一つのpersona stateから、複数の主体が同時に独立した経験を持ち始める場合は別`PER-xxx`へ分岐します。

子ペルソナの最初のstateには最低限、

- 親`PER-xxx`
- 親stateのstory time
- 分岐時のevent head
- 共通して継承したstate

を残します。

分岐後の二つへ同じペルソナIDを使い続けません。
