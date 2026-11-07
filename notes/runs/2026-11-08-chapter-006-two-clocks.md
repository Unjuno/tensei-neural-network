# 2026-11-08 制作 — 二つの時計（第6話）

## 開始時の権限・Git正本

- repo: `Unjuno/tensei-neural-network`
- main HEAD `919e1b8541c2627ad2210c086b9861892cb250bc`、`publication/policy.json`の`enabled=true`、許可はSerial Publicationによるmain/docs/serialの限定公開のみ
- work開始HEAD `3cac67761ffbc80b392eb75bfdef09cbc478cde5`
- 直接story head: 1980年代`EVT-020`、現代側none。既刊は001〜005。
- source HEADのStory Workflow Validation `42402441114` completed/success（units, chapter re-run, EXP-013保存値, validator）。Serial Publication最新観測 `42402513886` completed/success、公開commitなし・既刊005のlive manifest/HTMLの照合step成功。main台帳は001〜005。

## 一つの有限制作単位

EVT-019、EVT-020と二人の個別状態・ORG-001の制度/資源を復元。高橋の理論側問と、1975年久保田原著を佐伯だけが読んだ局所情報を混同しなかった。

- 新しい`EVT-021`: 佐伯が自らREF-003の限定要約を口頭で高橋へ共有。モデル更新順と生理の課題区間・発火時刻の対応は**未定義**として私的共同メモに空欄を残す。誰も新trialや動物実験を開始しない。`UNBLINDED`創作で独立blind生成の証拠ではない。
- 前後story head: `EVT-020 -> EVT-021`。佐伯・高橋両personaの観測更新を`novel/state/personas/deltas/EVT-021.md`に分離。ORG-001とglobal worldは重要な変化なし。現代側へ漏洩なし。
- EVT-019〜021で、離れた二つの問い→佐伯の個人読解→情報の共有と境界の合意、という読者にとって自然な変化が成立したため、**第6話「二つの時計」**へ投影。先に第6話の筋を指定して事件を作ったのではない。
- `experiments/chapters/006`のmandatory verification（一次文献・情報境界）、semantic review、terminology、review-lockと`publication/reviews/006.json`の5観点を同じ本文版で作成。**新規研究EXP・新数値試行なし**。既刊001〜005とその公開スナップショットには触れない。

## 検証/commit/公開の観測境界

制作時に読了した第1〜5話の本文・話別検証と意味レビュー・各publication/reviewsのPASS、本文/lock blob整合を確認。第6話は本文→採用EVT→久保田1975（DOI 10.2170/jjphysiol.25.481、報告95 unitは同時95-channelではない）の順に反例と知識境界を照合。model index（無次元）と神経発火時刻（秒）を同一視しない。

新source commit・GitHub CIは本記録を含むatomic commit後に実測する。**この段階では新commitのsuccess、Serial Publicationでの公開、Pages配信は未確認（PENDING）**。mainへのwork merge/PR/Canon昇格/外部投稿なし。条件の緩和なし。

## 残課題・再開点

最新work SHAを取り直して競合がないことを確認し、候補のunit tests・既刊話別再実行/保存JSON・workflow validator・全対象commitのGitHub CIを確認する。次にSerial Publicationの新runとlive manifest/006.htmlのhash照合が成功した**場合だけ**公開済みと報告する。第6話が未配信なら理由を公開履歴として保持する。

今後の物語: 高橋が別schedule familyの何を事前に固定するか、佐伯が課題・時間窓・記録unitのどれを実際の提案として操作的に選ぶかを、各人物の観測可能な知識から選ぶ。新生理実験・新数値結果を後付けしない。独立試読5名、独立復元、Human Review、Canon受理は引き続きOPEN。
