# 第1話「戻る先」公開前検証

状態: `PREPUBLICATION_GATE_PASSED`

対象本文:

- `novel/chapters/001.md`
- 比較稿: `novel/chapters/001-webnovel-draft.md`
- 最小因果骨格: `novel/chapters/001-outline.md`

採用event:

`EVT-001 -> EVT-002 -> EVT-003 -> EVT-004`

## 目的

第1話を公開する前に、本文の技術・歴史・用語・人物knowledge boundaryを、成立済みevent/stateと研究・検証証拠へ照合する。

必須なのは「毎話で新しい科学実験を作ること」ではなく、**その話が依存する最も壊れやすい主張を最低1回、再現可能な形で検証すること**である。

第1話では中心主張が数理的なので、実行可能な再現実験を採用した。

## 必須検証

- `verification.md` — 第1話のMandatory Verification正本
- `experiment.md` — EVT-004最小再現の条件・判定
- `run.py` — 再実行可能コード
- `results.json` — 保存済み結果
- `semantic-review.md` — 機械validatorでは判定できない意味レビュー
- `terminology.md` — 話別用語検証

## 参照した研究・event

- `EXP-003-hopfield-mixture-structure`
- `EXP-004-hopfield-ambiguous-cue`
- `research/1980s-research-environment.md`
- `research/pre-hopfield-background.md`
- `EVT-001`〜`EVT-004`

作者側EXP結果を1980年代人物へ未来知識として渡さない。

## 1. Mandatory Verification

判定: `PASS`

検証対象はEVT-004の6要素例。

固定条件:

- A/B/Cの三つの記憶パターン
- 同じ初期状態
- 同じ結合
- 自己結合なし
- 要素を一つずつ更新
- 入力総和0では現在値を保持
- 更新する順番だけalpha/betaで変更

再実行結果:

```text
alpha -> A
beta  -> B
```

両方とも到達後の次の一巡で変化なし。

このPASSは数理的再現性を確認するもので、EVT-004生成時の`UNBLINDED` provenanceやselection biasを解消しない。

## 2. 用語・歴史・技術

詳細は `terminology.md` と関連researchを参照する。

主要結果:

- `連想記憶 / 想起 / 手掛かり`は1984年資料へ照合
- `local field`等の史料根拠が弱い専門ラベルは操作説明へ置換
- 具体機種、OS、所在地、詳細職位は未検証のまま固定していない
- `ハミング距離`と`素子`にはより強い同時代用例を追加する余地があるが、章の核心事実として年代依存させていない

## 3. Semantic Review

詳細: `semantic-review.md`

判定: `PASS`

確認済み:

- knowledge leakageなし
- unresolved factの本文都合固定なし
- EVT-005以降の知識逆流なし
- 私的記録とinstitutional memoryの混同なし
- NarrativeProjectionがEVT-001〜004を超えて新factを生成していない
- EVT-004の`UNBLINDED` provenanceを隠していない

## 4. ALLOWED_UNRESOLVED

具体story dateは、現在の因果に不要なので固定しない。

- 正確な年月日
- 具体計算機
- 所在地
- 詳細職位

は今後必要になった時点でworld/event側から解決する。

## 5. 公開前gate

- [x] 採用EVT/stateと本文が矛盾しない
- [x] `verification.md` がPASS
- [x] コード化された検証が再実行時もPASS
- [x] `semantic-review.md` がPASS
- [x] 重要な技術主張が検証済み、または限界が本文へ反映されている
- [x] 未来知識漏洩がない
- [x] 話別用語検証と本文が一致する
- [x] 数値・手順がEVT-004と一致する
- [x] 重要な歴史・制度描写を未検証の具体値まで広げていない
- [x] unresolved事項を本文だけでCanon固定していない

## 最終判定

`PREPUBLICATION_GATE_PASSED`

意味:

- 現在のevidenceとworkflowに対して公開前gateを通過した
- 「科学的・歴史的に完全に正しい」という保証ではない
- Canon昇格ではない
- 公開・main受理には人間レビューを別途必要とする
