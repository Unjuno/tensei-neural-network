# 制作・検証ワークフロー

状態: `ACTIVE / PROVISIONAL`

上位運用規則は `POLICY.md`。世界進行は `novel/WORLD_POLICY.md`、状態復元は `novel/state/README.md` と `novel/state/LIFECYCLE.md`、研究は `experiments/README.md`、話別検証は `experiments/chapters/README.md`、文体は `novel/STYLE_WEBNOVEL.md` に従う。

## 1. 工程と証拠の権威を分ける

ポリシーは作業の許可・順序を定める。科学的事実を決める根拠ではない。

物語はCanonの制約下で成立したEVTと各時点のstateから復元する。現実の技術的主張は一次資料と実験記録へ戻る。文体・本文・索引が証拠を上書きしない。

復元では、同じ状態変化をEVTと対応deltaから二回加算しない。EVTは因果・客観結果の記録、entity deltaはその出来事による投影である。checkpointには適用済みevent headを残し、それ以後の差分だけを取り込む。Markdownの意味整合を自動証明できたとは扱わない。

## 2. 標準経路

復元 → 世界進行 → 自然な読書単位の判定 → 成立済みEVTの最小あらすじ → 本文 → 話別検証 → 本文への修正 → 意味レビュー → 文体調整 → 再レビュー・対象版記録 → 候補CI → 人間レビュー。

固定するのは前提条件と責任の境界であり、手戻りを禁止する一方向工程ではない。文体調整後も意味・観測・条件が変われば検証へ戻す。

### 復元と世界進行

現在branch、story time、解決済みevent head、active entity、関連snapshot/delta、未確定事項を確認する。古い索引やsnapshotへ巻き戻さない。

各主体は観測済みの局所状態から行動する。結果に影響する選択自由度は必要時にACTION_LOCKEDとしてcommitする。結果判明後に都合のよい条件へ差し替えない。

LOCKEDは「選択規則を後で変えていない」という履歴であって、独立した盲検、選択規則自体の無偏性、創発の証明ではない。文献掲載例の追試は、予告された結果の再確認として記録する。

### 読書単位と本文

EVT数、話数、実験番号、起承転結を出来事の原因にしない。成立した状態変化を見てから章を切る。

人物の会話をポリシーの読み上げにしない。科学的限定は必要だが、同じ注意を毎回往復させる義務はない。専門語の意味を変えず、行動・比較・観測で読める文章へ投影する。

### 話別検証

各話に最低一回、依存する主張を検証する。新しい研究EXPや実験場面を毎話強制しない。

コード再現、史料照合、情報境界追跡、物の来歴追跡、制度制約検査等から、その話に適した方式を選ぶ。

`verification.md`には対象、方式、選択理由、証拠、合否基準、実施結果、限界、本文への修正を残す。失敗・非再現も保存する。コードがある場合は`run.py`と`results.json`を保持する。

### 意味レビュー

`semantic-review.md`は、知識漏洩、未確定事実の創作、時代不整合、EVTと本文の対応、結果誘導、解釈の射程を記録する。旧レビューの見逃しは修正履歴へ明示する。

意味レビューのPASSは、記録した入力・対象に対してblockingな矛盾を検出しなかったという限定判断。読者評価、独立評価、科学的真理、文学的完成の代わりにしない。

## 3. レビューの対象版

候補・通過済み章には `experiments/chapters/NNN/review-lock.json` を置く。

最低限、章本文、outline、verification、semantic review、terminology、採用EVT、主要ポリシー、存在する実験コード・保存結果のGit blob IDを記録する。先行EVT・persona/state・史料等の追加依存もレビュー担当者が列挙する。

形式は`schema_version: 1`、`algorithm: git-blob-sha1`、`chapter`、`files`。これはGitの内容識別子を利用した鮮度検査であり、電子署名や改ざん耐性の保証ではない。未申告の依存を機械がすべて発見する仕組みでもない。

ファイルが変更されたらWF081で再レビューを要求する。内容を読まずにhashだけ再生成してはならない。

明示的レビュー後の記録例:

```bash
python tools/validate_workflow.py --record-review 001 --evidence novel/canon.md
```

この操作は章の状態を昇格しない。CIは対象版も保存結果も自動更新しない。packageのREADMEは状態昇格時に変化する索引なので、この最低限の対象版記録からは除く。

## 4. Gateの状態遷移

`IN_PROGRESS` → `GATE_CANDIDATE` → 対象版に対するCI成功 → `PREPUBLICATION_GATE_PASSED` → 別途Human Review。

候補にも通過済み章と同じ内容前提を課す。候補時点のcommitとCI runをpackage READMEへ記録する。

必要条件は、EVT/stateとの整合、話別検証PASS、意味レビューPASS、blockingな未検証・未置換用語なし、有効なreview-lock、コード再実行と保存結果の一致、厳格検査通過。

未知・欠落・重複した状態、未解決ACTION_LOCKEDの採用、outline欠落は成功扱いにしない。単に`result: PASS`と書かれたJSONも、個別checksや章IDが不正なら受理しない。

数理検証、意味レビュー、読者評価、人間の公開承認は別々に記録する。未確定の所在地・年月日等を、gateのために捏造しない。

## 5. 開発CIと公開前検査

```bash
python -m unittest discover -s tests -p 'test_*.py' -v
python tools/run_chapter_experiments.py
python tools/validate_workflow.py --strict --allow-drafts
```

作業branchのCIは未完成章の存在だけを失敗理由にしない。`--allow-drafts`が免除するのはWF060のみ。候補・通過済み章の必須条件や、未完成章の構造欠落を免除しない。

公開前およびmainでは免除しない:

```bash
python tools/validate_workflow.py --strict
```

コード再実行は標準出力のJSONを読み、章ID、総合結果、空でない個別checks、保存済みJSONとの全項目一致を確認する。終了コード0だけでは成功にしない。timeout、非JSON、保存結果の書換えも不合格とする。

現在の章別コードはCPythonの整数演算、標準ライブラリ、固定入力で動作する。確率的実験や浮動小数点backendを導入する場合、同じ全項目一致規則を黙って緩めず、測定条件・許容差・保存する結果を先に定義する。

### 実装変数表

| 記号・識別子 | 意味 | SI単位 | 定義 | 範囲・前提 | 型 |
|---|---|---|---|---|---|
| root | 検査対象repoの根 | 非該当 | 明示指定またはscriptの親 | ローカルの既存directory | Path |
| num / chapter | 話識別子 | 1・無次元 | 3桁の文字列 | 対応する本文が存在 | 文字列 |
| files | 検証入力の内容識別子表 | 非該当 | repo相対pathからGit blob IDへの対応 | 必須依存を含む。repo外pathは禁止 | 辞書 |
| checks | 個別判定 | 1・無次元 | 名前からboolへの対応 | 空でなく、成功には全項目がtrue | 辞書 |
| timeout | 1コードの実行上限 | s | runnerの引数。既定30秒 | 正数。速度benchmarkではない | 実数 |

単位確認: 内容識別子・件数・boolは物理量ではない。実行上限だけが時間量。モデル内の結合入力を電圧や発火頻度へ読み替えない。

## 6. 変更・長期目標

評価と改善目標は `notes/assessment-and-roadmap.md`。これは制作上の受入基準であり、人物へ渡す未来プロットではない。

新機能は実際の失敗に対応するときだけ追加する。復元・本文修正・検証のコストを今後の制作単位で記録し、閾値は実測後に調整する。checkpointやDORMANT化で過去EVTを消さない。

関連変更は可能な範囲で一つの整合したcommitにまとめ、未完の中間ファイルごとに成功を報告しない。mainへのmerge/fast-forward、PR、docs同期、公開は明示的な人間承認を別途必要とする。
