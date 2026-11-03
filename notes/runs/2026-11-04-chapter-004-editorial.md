# 2026-11-04 第4話「五と二十一」公開用編集評価

状態: DEPLOYED_VERIFIED（後追いでsource CIと配信まで実測）

## 起点と権限

- repo: Unjuno/tensei-neural-network
- 作業branch起点HEAD: `d75879ec212090f496cffb8b36cc1a149cdb7607`
- main観測HEAD: `b5eae78d02c3d5a7e2cde9d06b2297ed19631e11`
- main/publication/policy.json: enabled=true。公開先はSerial Publicationだけで、work全体のmain反映・Canon昇格・PRは対象外。
- main公開台帳: 001=2026-10-31、002=2026-11-02、003=2026-11-03。第4話は未公開。
- 最終確認のSerial Publication run: `41612940743` completed/success（2026-11-03 UTC開始）。このrunのjobは新規snapshot commitをskipし、既刊のlive照合はsuccess。公開3話まで。
- source起点HEADのStory Workflow Validation run: `41547333219` completed/success。全unit tests、章別再実行、研究、EXP-013保存JSON、workflow validatorがsuccess。

## 今回の制作単位

- story resolved head: EVT-018→EVT-018。新規EVT・人物state・研究実験・本文改稿なし。
- 最古の未公開章、第4話 `novel/chapters/004.md` を通読。参照した直接event: EVT-012 / EVT-013。対象のoutline、話別README・verification・semantic-review・terminology・results・review-lockも直接確認。
- 本文blob: `c215811ded93e9f05fce8864fceb9f996f767709`。review-lock blob: `7d7810800b308ebe7f23fff382677465c6f9dc71`。既刊のファイルやreview-lockは変更しない。
- 5観点の具体箇所を `publication/reviews/004.json` に保存。判定は当該版に限るAI編集PASS、blocking_issues空。AI_EDITORIAL_NOT_EXTERNAL_READER。
- 整数再計算（標準Python、16成分、固定入力・乱数なし）: Qが多数側16/16、unanimity4/split12、Q距離4/4/4、記憶間距離8/8/8、overlap各8、直接入力16件と8c−3Qの16件全一致、最小符号付き余裕5。保存results.jsonと一致。これは速度測定・独立試読ではない。

## 確認と次の一手

- 新commitのCI、およびSerial Publicationの実配信確認はこの記録の作成時点では未実施。報告時は新しい実測を別途確認する。READY/manifest更新だけでDEPLOYEDと断言しない。
- 実読者5名、真に独立した意味復元、Human Review、Canon受理は未実施。
- 次は新HEADのCI・公開workflow・live URL/hashを確認する。配信前なら未公開と報告する。第4話が確認できた後、第5話を独立に通読して編集評価する。章数目標から新事件を作らない。


## 実行後追記：2026-11-04 08:25 JSTごろの公開照合

- 準備commit: `3832df3279b718c9ed222b65aff6fad55a87a7bd`。Story Workflow Validation run `41738589401` completed/success。unit tests、章別実行と保存結果照合、研究再実行、EXP-013保存JSON、workflow validatorの全step success。
- Serial Publication run `41738736750` **第1attemptはfailure**。ゲートは第4話をREADYと判定し（source SHA/CI一致）、mainへの生成スナップショットpushで `remote: fatal error in commit_refs` となった。CI/本文の不一致ではないが、このremote内部エラーの深い原因は未確定。第1attemptで公開済みとは扱わない。
- 同じ公開workflowの**failed jobsを1回だけ再実行**。attempt 2はcompleted/success。生成した第4話をmainにcommit、Pages buildを要求し、live manifest/004.htmlの内容hash一致を検査した。初期live probeは遅延でBLOCKED、同run終盤の再検査で `DEPLOYED` を観測。job `126274931514` のlogにも `DEPLOYED chapter 004` を記録。ソースや公開ゲートの緩和・mainへの手動原稿pushはしていない。
- URL: https://unjuno.github.io/tensei-neural-network/serial/004.html
- mainの公開台帳（2026-11-04）: chapter=004、source SHA=`3832df3279b718c9ed222b65aff6fad55a87a7bd`、source CI=`41738589401`、md SHA-256=`0a6a038aa89eff4ae9a3066d2cb51808e1732993be180beb3fc5ce01bad3f379`、html SHA-256=`65b2b117df4e6e1d7266521888dcf1d4c361d7e98f376928596f347e84638192`。公開workflowによるmain HEADを `1603f717630d8a7d1b71cc84c63c0479ce9cfa91` として観測。
- 本追記の新source commitに対するCIと自動公開再評価は別途確認する。すでに公開した004は改変せず、次回は第5話の本文とEVT-014〜018を通読して編集レビューする。実読者5名・独立復元・Human Review・Canon受理はなおOPEN。
