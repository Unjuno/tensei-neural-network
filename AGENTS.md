# AI作業規則

このリポジトリでAIが作業するときの最低限の手順です。

## 作業開始

1. `README.md` を読み、プロジェクトの目的を確認する
2. `AGENTS.md` を読む
3. `STATUS.md` を読み、現在位置とactiveな作業を確認する
4. `notes/working-context.md` を読み、現在の探索状態・有力仮説・未解決点を確認する
5. `POLICY.md` を読み、正本・優先順位・研究判定・安全境界を確認する
6. 作業種類に応じて必要な正本だけを読む

リポジトリ全体を毎回無差別に読み込む必要はありません。

`main` は人間が受理した現在の正本です。その他のbranchは候補状態として扱い、`main`へ反映される前に正本へ確定したとみなしてはいけません。

`notes/working-context.md` は高速な作業記憶であり正本ではありません。そこにある仮説や案を採用するときは、対応する正本へ明示的に反映します。

## GitHubへの書き込み

このrepoでは、PRイベントにCodex / Cursor等の外部GitHub Appが反応することが確認されています。内部のAI作業では、不要な自動レビューを起動しないため、**PRを通常の作業・レビュー手段として使いません**。

AIによるまとまった変更は次の順で扱います。

1. `main` からwork branchを作る
2. branch上で関連変更をまとめる
3. `STATUS.md` を含む必要な記録を更新する
4. branch内で自己確認する
5. `main...work branch` のcompare結果を人間へ提示する
6. 人間が明示的に承認した場合のみ、`main` をwork branchの確認済みcommitへfast-forwardする
7. 反映後、不要になったwork branchは削除する

Pull Requestは、外部Contribution、GitHub上で公開レビューを残す必要がある場合、または人間が明示的に要求した場合にだけ使用します。

人間が明示的に指示した低リスクの状態修正・運用修正は、必要に応じて直接 `main` へ反映できます。ただし物語Canon、研究Finding、公開済み本文、権利方針など重要な正本変更ではこの例外を使いません。

GitHub ActionsとCodex等の外部GitHub App / 自動PRレビューは別物です。`.github/workflows/` やActions runが存在しない場合、自動起動を「CI」と決めつけず、PRレビュー連携など別トリガーを確認します。

### 安定IDを採番する前にcurrent branchを確認する

`EVT-xxx`, `PER-xxx`, `BOOT-xxx`, `Q-xxx`, `H-xxx`, `EXP-xxx`, `F-xxx`, `REF-xxx`, `L-xxx` を新しく割り当てる前に、**`main`だけでなく現在書き込み中のwork branch上の同種IDも確認します。**

長く続くwork branchにはmain未反映のIDが存在するため、mainの最大番号だけを見て次番号を決めてはいけません。

標準:

1. 現在書き込むbranchを確認する
2. そのbranch上の同種IDを検索・列挙する
3. `main`上の同種IDも必要に応じて確認する
4. 両方に存在する最大番号より大きい未使用番号を使う
5. IDを作った直後に同一branch内の重複がないか確認する

別work branchとの衝突が後で判明した場合は、mainへ反映する前に採番し直します。

一度正当に割り当てたIDを、内容を差し替える目的で再利用しません。

## 小説作業

本プロジェクトでは**小説を主目的**とします。研究を先に積み上げるのではなく、物語を書き、技術的な確認が必要になった箇所で研究へ戻ります。

小説生成・ペルソナ相互作用を行うときは、次を優先して参照します。

1. `novel/canon.md`
2. 対象story timeの `novel/bootstrap/BOOT-*.md`
3. `novel/environment.md`
4. `novel/state/world.md`
5. `novel/personas/README.md`
6. その場面でactiveな `novel/personas/PER-*.md`
7. activeな人物の `novel/state/personas/PER-*.md`
8. 関連する `novel/events/EVT-*.md`
9. `novel/timeline.md`
10. `novel/characters.md`
11. `novel/structure.md`
12. `notes/working-context.md`
13. 関連する章と `novel/chapters/README.md`
14. 必要な研究・実験・参考文献

物語の客観的事実について `canon.md` と他の物語ファイルが食い違う場合は `canon.md` を優先します。

人物の信念や発言を、世界の客観的事実へ自動的に昇格させてはいけません。

`notes/working-context.md` にある輪廻・同一認識主体・顕在化等の案は、明示的にCanonへ採用されるまでは探索仮説です。

### 定義・Bootstrap・時系列状態を混同しない

- `novel/bootstrap/BOOT-*.md` は、あるstory timeへworld/persona stateを同期生成する背景Frame
- `novel/personas/PER-*.md` はペルソナの定義・baseline
- `novel/state/personas/PER-*.md` は時間に依存する人物状態
- `novel/environment.md` は世界・環境の定義と解決規則
- `novel/state/world.md` は時間に依存する客観世界状態
- `novel/events/` は両者を同じstory time上で結合する出来事
- `novel/timeline.md` はstory timeの索引

ペルソナや世界を一つの巨大な状態ファイルへ統合しません。一方、時系列状態をそれぞれ勝手に進めてもいけません。

BootstrapはeventでもCanonでもありません。Canonに従い、その時点の状態を同期生成する入力です。

### Bootstrapで初期化・再初期化する場合

新しい物語開始時、大きな時代切替、長い中断、別AIセッションでの再構成では次を行います。

1. 対象story timeを決める
2. その時点までの`parent event head`を確認する
3. 対象`BOOT-xxx`を読む。なければCanon・timeline・既存stateと矛盾しないBootstrapを候補として作る
4. Bootstrapのworld projectionから`state/world.md`を同期する
5. Persona discoveryで独立状態が必要な主体を確認し、必要なら新しい`PER-xxx`を作る
6. 各persona projectionから、本人が知り得る情報だけで`state/personas/PER-xxx.md`を同期する
7. world/persona stateの`BOOT / story time / parent event head`が一致することを確認する
8. 未来event、他者の秘密、別時代の状態が漏れていないか確認する

再初期化によって過去stateを上書きしません。Bootstrap本文を全ペルソナへそのまま与えません。

一つのpersona stateから複数主体が独立経験を持ち始める場合は別`PER-xxx`へforkし、親state・story time・event headを追跡可能にします。

### ペルソナ駆動で進める場合

完成済みの未来プロットを人物へ与えません。各ペルソナは、自分に許された局所状態だけから行動させます。

1. `timeline.md` で対象場面のstory timeを確認する
2. 対象Bootstrapとworld/persona stateの同期キーを確認する
3. `state/world.md` でその時点の客観世界状態を確認する
4. activeな各ペルソナについて、定義ファイルと、その時点までのstateを個別に読む
5. 各ペルソナへ、その人物が観測できる情報だけを与える
6. 各ペルソナの発言・行動を、その人物の現在の目的・信念・状況から生成する
7. 人物の意図と結果を分離し、`environment.md` の規則でCanon・技術・歴史・制度・権限等の制約からeventを解決する
8. 重要な出来事なら `EVT-xxx` として記録する
9. `state/world.md` をeventの客観結果で更新する
10. 各人物へ、実際に観測できた結果だけを返し、観測した人物の `state/personas/PER-xxx.md` だけを必要に応じて更新する
11. `timeline.md` にstory timeとeventを索引する
12. 発生した状態変化を `structure.md` の再帰的な起承転結で整理する
13. 相互作用ログを材料に本文を書く

変化しなかったペルソナは前状態を継承してよく、毎eventごとに全員のsnapshotを作る必要はありません。

新しい人物が物語へ入った場合は新しい `PER-xxx` を追加します。既存キャスト数を固定しません。

### 結果へ影響する自由度がある場合のACTION_LOCKED

生成者・resolverがpersonaには見えない作者側研究結果を既に知っており、具体pattern、seed、update order、trial選択等の自由度でoutcomeを寄せられる場合、上の手順7の前に `novel/events/README.md` の二段階手順を使います。

1. personaのstory-visibleなKnowledge / Beliefs / Goals / 状況だけから行動を生成する
2. outcome-sensitiveな具体条件、または条件を選ぶdeterministic ruleを固定する
3. trial集合、update rule、stopping / inclusion ruleを固定する
4. resolverが使ってよい情報と、action selectionへ使ってはいけない作者側情報を記録する
5. eventを `ACTION_LOCKED` として**outcomeを書く前にcommitする**
6. commit後にresolverが結果を解決する
7. locked条件を結果を見て変更しない
8. 平凡・失敗・不都合な結果もそのまま採用する

同じAI/sessionが作者側研究結果を読んでいる場合、具体条件を自由選択してclean validationと主張しません。story-visibleな情報だけから導出する固定ruleを使うか、結果知識を与えない別contextで条件を選びます。

解決前lockがないeventは物語として保持できますが、resolver独立性の検証では `UNBLINDED` として扱います。

詳細: `novel/environment.md`, `novel/events/README.md`, `notes/generation-validation.md`

禁止事項:

- 「次に転が必要だから」という理由で人物に不自然な行動をさせる
- 一人のペルソナへ他者の秘密・未来プロット・作者側の真相候補を漏らす
- 世界状態が変わっただけで、全人物がその変化を知ったことにする
- 人物の現在状態を定義ファイルへ上書きして、過去の状態変化を消す
- 現在の設定を寄せ集め、同期点を確認せずペルソナを再生成する
- PER-004の自己申告を、そのまま本人性の証拠にする
- ナレーターが予定した結論に合わせて、環境側の因果結果を書き換える
- 実験予定やEXP番号に合わせて人物の発言・行動を生成する
- 小説本文をQ / H / EXP / PASS / FAILの研究レポート形式へ変換する
- 既知の研究結果と同じ現象を出すために、結果解決前にlockしていない具体条件を選び、そのeventをcleanな創発生成の証拠とする

起承転結は原因ではなく、成立した状態遷移を認識・整理するための再帰構造です。

story time上の因果順と、本文で読者へ見せる章・scene順を混同しません。

### 本文へNarrativeProjectionする場合

本文は成立済みevent / stateの読者向け表現です。

状態を変えない一時的な動作・描写は補ってよい一方、未確定の恒常属性を本文だけで確定しません。

特に氏名、年齢、性別・性別代名詞、国籍、所属・職位、家族関係、具体地域、後続因果へ効く技術環境がstate/eventで未確定なら、本文でも未確定のまま書きます。

本文とevent/stateが矛盾した場合は、本文の都合で過去stateを後付け変更せず、まず本文を修正します。

詳細: `novel/chapters/README.md`

## 研究作業

次を優先して参照します。

1. `research/README.md`
2. `research/questions.md`
3. `research/hypotheses.md`
4. 関連する `experiments/`
5. 関連する `research/reports/`
6. `research/findings.md`
7. `references/bibliography.md`

仮説を事実として記述してはいけません。実行していない実験を「再現した」と記録してはいけません。

実験開始前に、少なくとも判定対象・判定基準・データ・環境・必要サンプル数またはその代替根拠・停止条件を記録します。結果を見た後で判定基準を黙って変更してはいけません。

物語上の「輪廻」「同一主体」「人格復元」等の仮説を、現実科学で実証済みの事実として扱ってはいけません。現実側で調査・実験する場合は、観測可能な代理指標と競合説明を明示します。

### 物語から研究を分岐させる場合

物語中で実際に成立したevent・発言・観測を先に確認します。

1. `EVT-xxx` と該当persona stateを読み、本人が実際に言ったこと・観測したことを特定する
2. そこから現実側で検証可能な問いだけを `Q-xxx` として切り出す
3. 必要なら反証可能な `H-xxx` を作る
4. 結果を見る前に `EXP-xxx` の条件・判定基準を事前登録する
5. 実験を独立実行し、`experiments/EXP-xxx-*/` に証拠を保存する
6. `research/reports/EXP-xxx.md` に背景・問い・結果・解釈・限界・派生候補を整理する
7. 必要なら `research/findings.md` を更新する
8. 研究結果を物語人物へ自動共有しない

一つの研究レポートに次の実験候補が書かれていても、それだけを理由に次のEXPを自動生成しません。後続の物語で新しい問いが実際に生じるか、独立研究として進める価値が明確になった場合に改めて開始します。

### 研究結果を物語へ戻す場合

研究結果をpersona stateへ反映する前に、その人物がstory time内でその情報をどう観測したかを確認します。

- その時代に入手可能な論文を読んだ
- 会話で共有された
- 自分で計算・実験して観測した
- 装置出力や記録を確認した

等の因果経路がなければ、その研究結果をKnowledge / Beliefsへ加えません。

特に現代の作者側実験を1980年代人物へ逆流させません。

## 作者の学習整理

理解が変わった場合は `notes/learning.md` に、初期理解・問題・根拠・更新後の理解・作品への影響を記録します。作品へ実際に反映した場合は、対象ファイルと反映状態も更新します。

## 作業コンテキスト

`notes/working-context.md` には、別セッションで再開するために必要な**公開可能な状態要約**だけを保存します。

保存してよいもの:

- 現在の有力仮説
- 競合する説明
- 未解決の問い
- 採用前の物語方向
- 次の作業
- 参照すべき正本

保存してはいけないもの:

- AIの逐語的な内部推論、生の思考系列
- system / developer prompt等の内部指示
- private key、API key、access token、PAT
- Cookie、session token、OAuth secret
- `.env` の秘密値
- 公開不能な個人情報

秘密情報が誤ってGit履歴へ入った場合、ファイル削除だけで安全になったと判断せず、原則としてcredentialを無効化・再発行します。

## 矛盾を見つけた場合

自動的に片方を削除しません。

1. 情報の種類を確認する
2. `POLICY.md` の正本優先順位を確認する
3. 両立する矛盾か確認する（例: 正史と人物の誤認）
4. 研究証拠の矛盾なら、必要に応じて仮説を `INCONCLUSIVE`、Findingを `CONTESTED` として保持する
5. 解消が必要なら正本を更新する
6. 重要な判断なら `notes/decisions.md` に理由を残す
7. 最後に `STATUS.md` を更新する

不整合を隠すためにraw result、過去Finding、過去の学習記録を削除してはいけません。

## アイデアを採用する場合

`notes/ideas.md` や `notes/working-context.md` の案は未確定です。採用するときは、実際の正本（`novel/canon.md`、`novel/structure.md`、研究ファイル等）へ明示的に反映し、必要なら元の案側に採用先を残します。

## 作業終了

1. 成果物を保存する
2. 必要なら正史・研究知見・学習記録・判断記録を更新する
3. `notes/working-context.md` を、次セッションが再開できる状態へ要約更新する
4. 関連ID・参照先を更新する
5. 最後に `STATUS.md` を現在状態へ更新する

`STATUS.md` の更新を、セッションを安全に終了できるチェックポイントとして扱います。

## 書き込み方針

- 文書は原則として日本語で書く
- 不確かな事項は不確かなまま記録する
- 重要な出典は追跡可能にする
- 既存の履歴を不用意に消さない
- 大きな方針変更は人間の確認なしに確定しない
- GitHubを共有メモリとして使うほど、公開境界・credential・個人情報を厳格に扱う