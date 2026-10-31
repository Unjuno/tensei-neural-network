# 定期制作・公開ループの初回運転

実施: 2026-10-31。開始work HEAD: eb548e8058bb2ab05e3ed1061c01d0d63221a32c。
依頼: 定期実行で公開し、制作/検証/次話へ進む継続システムを実装する。過去の制限に対する限定的な連載公開の委任として扱った。

## 実施

- 既存日次タスクの実行履歴を読み、実際に場面試作・CI確認を行っていたことを確認。重複タスクを増やさずpromptを制作・検証・連載用へ更新
- workに公開エンジン、29回帰テスト、publication policy、初回第1話の編集レビュー、設計計画を追加
- mainへ公開機構だけ導入。親はmainの旧HEAD7e9f6745であり、workのmerge/fast-forwardはしていない。機構導入commit0091b44d、互換修正754a076c
- main上の公開workflowだけがdocs/serialへ1話を生成しbotでcommit。Canon、本文正本、実験、既存docsの置換なし
- 生成した第1話の公開manifestと最新HTMLを実際のPages URLから取得し、hash一致を確認してDEPLOYEDと判定

## テスト・故障からの修正

ローカルCPython3.13.5で未実装の23テスト失敗から開始し、配信再試行/巻き戻し禁止3件を追加。26件成功。

初回実運転run41176298501は、EVT-004をunresolvedとしてBLOCKED。原文を読んだところ初期EVT-001〜004はPROVISIONALと記す旧形式だが、Resolved consequence・world/persona deltaを持つ成立済み記録だった。本文やeventをゲートのために改変せず、レビュー済み旧blob4件だけを許容するadapterにした。未知のPROVISIONAL、既知blobの改変、ACTION_LOCKED、RESOLVED_LATERを拒否する3件をRED→GREENで検証。

最終の追加testsは29件。ActionsではCPython3.12.15 / Ubuntu26.04.1、標準ライブラリで成功。速度benchmarkではない。テストには章欠番、重複公開、日次上限、古いCI/lock/editorial版、未検証語、改変済み公開物、script入力、symlink/path traversal、配信未確認の新規公開禁止、remote台帳ahead/divergenceのrollback拒否を含む。

## 対象版と実行証拠

source: 7820573205f29e6d626952f914d469f0f9982802
Story Workflow Validation: https://github.com/Unjuno/tensei-neural-network/actions/runs/41176570607
source CI: success（既存5話、研究、EXP-013再計算JSON照合、構造検査）

Serial Publication: https://github.com/Unjuno/tensei-neural-network/actions/runs/41176658296
publish job:124465509267、conclusion:success
準備→公開物だけcommit→既存main/docs Pages build要求→live manifest/最新HTML照合まで成功。

第1話公開URL: https://unjuno.github.io/tensei-neural-network/serial/001.html
公開日:2026-10-31
本文SHA-256:36cbbc4a978a044ae6b19933f9e956ebb595ee6c0a65c470dea32eca1d250ac2
HTML SHA-256:59f33403defa1ce1409af3d7e39f2d5533f48c7933d4eae644af92fdf89eb7b2
review-lock blob:a8e64559df11a231cf974e831e2c662e3860cff2
editorial-review blob:37a01b5214f692f0a42cde125b4160d016712518

チャットのweb取得ツールは当該Pages URLの取得に失敗したため、それをサイト停止の証拠とはしない。公開成功の根拠はGitHub runnerからの内容一致観測と実行結果である。

## 引継ぎと限界

物語headはEVT-018のまま。新EVT、新persona、新EXP、新章は今回増やしていない。第1話も過去EVTに合わせた既存の検証済み本文を使い、新規に改変していない。次の制作単位は第2話の5観点編集レビュー。第2〜5話を一括で公開承認したとはしない。

機械ゲートは作品の面白さを保証しない。AI編集レビューと独立試読は別。main/publication/policy.jsonのenabled=falseで停止する。配信失敗なら新章番号を消費せず前の配信を再試行。今後の再起動で同日の追加commitが発生しないことは、実運転の後続runでも確認する。

## 関連

設計: notes/plans/2026-10-31-serial-loop.md
公開契約: main/publication/README.md
実装: tools/serial_publish.py
テスト: tests/test_serial_publish.py / tests/test_serial_legacy.py
