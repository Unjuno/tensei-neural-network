# 2026-11-08 定期制作の再開 — 神経生理学の観測可能性

## 前提と開始状態

- repo: `Unjuno/tensei-neural-network`
- 開始work HEAD: `06113306510f159662746946ea9955132d74b536`
- main source branchの既刊: 001〜005。main `publication/policy.json` の `enabled=true`
- 開始story head: EVT-019、現代側none。最新source CI run `42313531252` completed/success
- 直近Serial Publication run `42357384020` completed/successで、未公開の新章なし
- 日次ChatGPT automationは `enabled=false`, latest recorded run `failed`。しかし同じ回のGitHub成果とCIは成功しており、配信・後処理の具体的失敗原因は未判定。作業実行とautomationの成否を別管理する

## 史料調査（作者側、事後選定）

佐伯がEVT-019で選んだ神経生理学的観測可能性に関して、1985年より前に公刊済みの一次論文を検討。

- 久保田競 1975（REF-003, DOI: 10.2170/jjphysiol.25.481）: 同じ前頭前野単一unitを二つの遅延課題で比較、95 unitは総記録件数であり同時測定unit数ではない
- Fuster & Alexander 1971（REF-004）: delayed-response中のunit activity
- McNaughton, O'Keefe & Barnes 1983（REF-005）: ラット海馬の最大5 unit同時弁別
- Barrionuevo & Brown 1983（REF-006）: 海馬切片の二入力経路に伴う連合性LTP
- McNaughton, Barnes & O'Keefe 1983（REF-007）: 放電活動の位置・方向・速度への依存

史料の発表年代は物語候補時点より前だが、ORG-001の所蔵・実験設備・動物実験可能性を示す根拠ではない。論文が存在することと、登場人物が読んだことは別。

詳細は `research/1980s-neurophysiology-observation-boundary.md`。物理単位・観測量・作業仮説と認識上の限界を区別。

## 物語進行

- 新event: `EVT-020 同じ細胞でも同じ課題ではない`。佐伯はREF-003を個人で読み、課題の手掛かり/遅延/応答区間と単一unitの発火を分けて理解した
- Event provenance: `UNBLINDED`。作者が文献の候補を検索してから具体論文を選んだことを隠さず、盲検のpersona action選択と主張しない
- State: `novel/state/personas/deltas/EVT-020.md` はPER-006だけを更新。PER-005へ読解内容を共有しない。ORG-001のequipment/budget/institutional memory不変
- 1980年代head: EVT-019→EVT-020。現代側none
- 話別: 第1〜5話の既刊・canon・review-lock・公開用コード/台帳は不変。第6話・新数値実験は未成立。自然な読書単位を話数の都合で作らない

## 実施したGit変更

- 作者側一次研究ノート
- 参考文献REF-003〜007
- EVT-020および佐伯だけのpersona delta
- timeline / structure / STATUS / working-contextの索引更新
- 本runログ

## 検証と未完事項

- 文献: すべて1985年以前の原著を用い、1975年原論文・PubMed・出版社/PMCの書誌・方法内容で確認。文献内容の選択は結果前lock済みではない
- 既刊章: 本文やそのdependency blobは変更していない。既刊の機械検証と実読者評価を混同しない
- GitHub Actions: 後続source HEADのCIを確認し、別途実行記録に最終結果を追記する
- GitHub公開workflow: 新章がないのでNO_READY_CHAPTERが適切。既刊の重複公開・強制main統合をしない

## 次の一手

高橋側はEVT-019の別schedule familyという未固定の問いを保持。佐伯側はREF-003を読んだが、高橋はそれをまだ知らない。次に二人が何を観測・共有・選択したかを各personaの局所stateだけから解決する。歴史史料から直接模型の更新則や人格・記憶の生物学的同一性を導かない。

独立の5名実読者試読、独立restore、人間のCanon受理は未実施。日次automationが再び有効になるかと次回run状態は、別の観測として確認する。
