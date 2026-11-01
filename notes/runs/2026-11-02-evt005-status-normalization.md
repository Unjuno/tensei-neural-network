# 2026-11-02 連載第2話の公開阻止原因を修正（検証待ち）

## 出発点・委任
- 作業branch: `work/story-bootstrap`、開始HEAD `90f78ef3b311130ee28fb101af3dabcb9d457f4a`。前回の日次成果後に別のwork変更は観測されなかった。
- main公開policy: `enabled=true`。公開先は `main/docs/serial` のみでSerial Publication workflowが管理。作業側はmainへ書かない。
- main公開台帳: 第1話 `001` のみ。第2話は未公開。2026-11-01 09:22 UTCのSerial Publication run `41292885268` は `BLOCKED: unresolved event: EVT-005` により失敗。
- 開始HEADのStory Workflow Validation run `41252588000` はcompleted/success。変更後の新HEADには旧CIの成功を流用しない。
- 物語head: EVT-018（前後同一）。1980年代側はPER-005、PER-006、ORG-001。新EVT・新章・新研究実験を発生させない。

## 原因の分解
- EVT-005は見出し `状態: PROVISIONAL / RESOLVED` だが、mainのtrusted publisherは厳密に `RESOLVED` / `RESOLVED / PROVISIONAL` だけを通常許可。初期EVT-001〜004にしか固定blob互換はない。
- EVT-005には結果前ACTION LOCK commit `59ff6530d202b79834afbe8ffdceee1256437315`、固定6 cyclic rotations、紙上exact更新と全結果A/D/B/B/D/D、world/persona delta、生成方式の限界が既に存在する。未解決イベントを解決済みへ捏造したものではない。
- 対処はソースの見出し一行の順序正規化のみ。main側ゲートを変更・緩和せず、過去のaction lock・結果・本文・Canonを変更しない。元のblob `a71693f26cb25054d292b76a994fd2b27613f3bc` と新blob `83565790180f3d8af2402a9f6c7914fb8cb6366f` は同じ一行以外不変と確認。

## 波及範囲と読み直し
- 第2話（EVT-005〜008）：6順A/D/B/B/D/D、36件A11/B11/C2/D12、全64状態×6順384件、D=-C、符号反転ゼロ入力保持を本文・semantic review・verificationと照合。佐伯の事前記録欄要求と高橋の分類修正が同じ観測範囲に留まる。
- 第3話（EVT-009〜011）：六素子に他のfixed pointなしという全列挙結果と、1983年の十六素子Qという別模型を混ぜていない。論文の選択を網羅的な最早性調査と断言しない。
- 第4話（EVT-012〜013）：16位置で多数側、一致4/分割12、保存形まで距離各4、結合入力絶対値5/21という検算は変更なし。固定点到達性と安定性を区別している。
- 第5話のreview-lockはEVT-014〜018のみを列挙し、EVT-005のblobを含まないため影響しない。章本文も変更しない。
- 第2〜4話のsemantic-reviewに限定再評価を記録し、当該EVTとreview文書のblobを各話review-lockへ更新。第2話の公開用編集レビューは同一本文blob `c3b4cbb11e52a729fc336f7c701128f0cd1073f5` と新lockを対応させた。独立試読/意味復元やHuman Reviewとは区別する。

## 変更対象と検証予定
- 変更対象: EVT-005（1行）、話別semantic-reviewとreview-lock（002〜004）、publication/reviews/002.json、test追加、STATUS/working-context、本記録。
- 回帰検査はEVT-005の状態・事前LOCK/解決結果、影響三話のgit-blob SHA、編集レビューの対象本文/lock一致を照合。
- この記録を書いた時点で新HEADのCI、再実行JSON、Pages配信の照合は未実施。成功値を事前記入しない。後続の実測に基づき追記する。

## 残課題・具体的な次の一手
- 新HEADでunittest、chapter再実行、EXP-013保存結果照合、workflow validatorをGitHub Actionsで再実行し、新規CIが成功した場合にのみ公開側の判断を確認。
- mainの公開台帳と実配信URLを照合し、最新話が配信されたときだけDEPLOYEDと記録。BLOCKEDなら理由を特定しゲートは緩めない。
- 第3〜5話の公開用AI編集レビューは未実施。実読者最低5名、真に独立した復元、Human Review、Canon昇格も未実施。

## 実行後の実測結果（2026-11-02追記）

- 正規化・三話再監査commit: `3e363989f25fccdfb3c4b75dd6a169f48f85da16`。GitHubから新EVT-005 blob `83565790180f3d8af2402a9f6c7914fb8cb6366f`、第2話lock `9b84e480123f78df3456370a429d8ff895683650` を再取得して一致確認。
- Story Workflow Validation: run `41360865674` **completed/success**。Python 3.12 GitHub Actionsでunit tests（今回追加の3テストを含む）、全話の保存JSONとの再実行照合、研究実験、EXP-013再実行JSON完全比較、workflow validatorが成功。
- Serial Publication: run `41360920516` **completed/success**、job `125010888141`。`READY` で第2話1本のみを生成し、mainの `docs/serial/002.md`・`002.html`・目次・manifestを更新。実配信の確認stepは `DEPLOYED`、2026-11-01 23:12:50 UTC（日本時間11月2日08:12:50）にURLと内容を照合した。失敗した最初のURL照合はデプロイ遅延で、その後同一run内で成功した。
- 公開URL: https://unjuno.github.io/tensei-neural-network/serial/002.html 。main台帳の第2話 `released_on=2026-11-02`、`source_sha=3e363989f25fccdfb3c4b75dd6a169f48f85da16`、`ci_run=41360865674`、`html_sha256=d661ae28255972fd623a0ff7e1e0e8fac3caf709826215ac6cf87000bdcb7f35`、`md_sha256=669e8becb76c0899a96a351ed5a9b8890b70fd4430dc061fbd801a5094e81989`。
- この更新は作業側の報告・索引のみで、mainへはエージェントから書き込んでいない。既刊001は変更していない。新たなEVT、実験、本文変更はなし。公開側の回帰を緩和していない。
- 次に最古の未公開章003の本文/EVT-009〜011/検証と文学的読者視点5観点を個別に点検し、`publication/reviews/003.json` を作る。実読者試読、独立復元、Human Review/Canon受理は未実施。

この実測追記自体を含む最終文書commitのCIは別runで確認する。先行commitのCI成功を、後続文書commitへ流用しない。
