# 2026-11-03 第3話の公開前AI編集レビュー

## 入口と差分

- source branch: `work/story-bootstrap`; 開始HEAD: `0dcbcaffadaed8f837d8b56a9dcd4d8142731a4f`。直近の2026-11-02最終commitから新しいwork変更なし。
- main/publication/policy.json: `enabled=true`; 委任対象は連載版の自動公開に限定。work全体のmain統合・PR・Canon昇格は許可されていない。
- 開始HEADのStory Workflow Validation `41361158391`: completed/success。main/docs/serial/manifest.jsonは001（10月31日）、002（11月2日）のみ。直近Serial Publication `41422224575`: completed/success、DAILY_LIMITかつ既刊002のlive URL/hashをDEPLOYEDとして確認。今回の第3話は未公開。
- story headはEVT-018。PER-005/006・ORG-001がactive。新EVT・新研究EXPを開始しない。

## ひとつの制作単位

- 最も古い未公開の第3話『表の外』を全文読了。EVT-009〜011と先行EVT-005の表記正規化、003-outline、003 verification、terminology、semantic-review、results.json、review-lockを直接比較。
- 読者の追う問いは『六素子の空白』から『別の16素子Qの存在』、さらに『Qの構成』へ進む。高橋は後付けの規模変更をやめて文献へ戻り、佐伯はゼロ入力があれば保留すると条件を固定する。人数を増やすために架空の事件や組織判断は作らない。
- 数理と史実: Hopfield, Feinstein & Palmer (1983), Nature 304, 158–159, DOI 10.1038/304158a0。世界最早の論文を網羅的に立証したとは扱わない。EVT-009の6素子は残差空、EVT-011の文献掲載16素子はQがstored/negation外。モデルを混同しない。
- 当日、EVT-011で固定したM1/M2/M3/Qと自己結合ゼロの整数Hebbian重みから16局所入力を別に計算。保存results.jsonの `[21,21,5,5,-5,-5,-21,-21,5,-5,-5,5,5,-5,-5,5]` と16/16一致、ゼロ0、最小符号付き余裕5、Qはstored/negation外。最初の手入力に転記誤りがあり、一次EVTのパターン列に戻して修正した上で再計算・一致を確認。これは独立した別主体の意味復元ではない。
- 公開用レビュー `publication/reviews/003.json` を作成、verdict=PASS（AIによる限定的編集評価）、review_kind=AI_EDITORIAL_NOT_EXTERNAL_READER、5観点と具体本文箇所を記録。対象chapter blob `802424a3fc3504e766a6fdb24a791a455151900a`、review-lock blob `339a92b80ea84c604384ee0353b98e78f00f493f`。blocking_issues空。本文改稿なし。
- 非blockingな弱点は、記号・数理説明が密で、人物の行動が研究内に閉じている点。実読者の評価ではない。

## 検証と公開（初回記録時点）

- 今回のGit commit、source CI、公開workflowの成否は、この初回記録を作成した時点では未観測。過去CIを新HEADへ流用しない。
- 公開権限/ゲートを変更しない。main・既刊HTML・台帳は制作側から変更しない。
- 実読者5名、Human Review、真に独立した意味復元、人間のCanon受理はOPEN。

## 再開手順

新HEADに対するunit tests、話別実行/保存JSON一致、研究再実行、workflow validator、CIを確認。公開runが発火した場合はlive manifestと003.htmlのSHA-256が一致したときだけDEPLOYEDと記録する。失敗なら理由をそのまま保存。公開済みであれば次は第4話を通読して個別に公開用編集評価を行う。新しい実験を必要としていない。
