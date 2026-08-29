# 話別検証パッケージ

このディレクトリは、小説の**各話ごとの公開前検証**を管理する。

研究実験 `EXP-xxx` と話数は一致させない。各話で必須なのは新しい科学実験ではなく、**その話が依存する最も壊れやすい主張を最低1回、再現可能な形で検証すること**である。

上位の固定工程はroot `WORKFLOW.md` に従う。

## 目的

各話の本文を、公開前に次の要素と相互照合する。

- 採用EVT / World State / persona・organization state
- その話から派生・参照する `EXP-xxx`
- 歴史・技術資料
- その話で実際に使う専門用語
- 時代・人物のknowledge boundary
- 数値・実装条件・装置・制度描写
- 話ごとのMandatory Verification
- semantic review

## 基本構造

```text
experiments/chapters/
├─ README.md
├─ SEMANTIC_REVIEW_TEMPLATE.md
├─ 001/
│  ├─ README.md
│  ├─ verification.md        # 必須。検証の入口・判定正本
│  ├─ semantic-review.md     # 公開前gateでは必須
│  ├─ experiment.md          # 数理/コード実験を選んだ場合
│  ├─ run.py                 # コード化できる場合
│  ├─ results.json           # コード結果
│  └─ terminology.md
└─ 002/
```

## Mandatory Verification

各章は公開前に最低1回、章本文が依存する内容を実際に検証する。

`verification.md` に最低限、

- 検証対象
- なぜその対象を選んだか
- verification type
- evidence
- 事前または明示的な判定条件
- 結果
- 限界
- 本文への影響

を残す。

### verification typeの例

- `EXECUTABLE_REPRODUCTION`: 数理・コード・計算の再実行
- `HISTORICAL_SOURCE_CHECK`: 一次資料・同時代資料の照合
- `PROVENANCE_TRACE`: 文書・物・所有・場所の来歴検証
- `KNOWLEDGE_BOUNDARY_TRACE`: 誰がいつ何を知り得たかの検証
- `INSTITUTIONAL_CONSTRAINT_CHECK`: 制度・組織・設備条件の照合
- `MIXED`: 複数方式

したがって、

```text
1 chapter != 1 research EXP
1 chapter >= 1 mandatory verification
```

である。

**話別検証のために物語へ実験現象を追加してはいけない。** 先にEVT/stateから章が成立し、その後で章の壊れやすい依存点を選んで検証する。

既存 `experiment.md` / `run.py` / EXPを利用してよいが、参照だけで済ませず、その章の公開前条件として何を再確認したかを `verification.md` に残す。

## Semantic Review

機械validatorだけでは、歴史的自然さ、knowledge leakage、plot conditioning、NarrativeProjectionの忠実性を証明できない。

公開前gateでは `semantic-review.md` を作り、`SEMANTIC_REVIEW_TEMPLATE.md` の項目を最低限確認する。

最低対象:

- knowledge boundary
- unresolved fact invention
- historical / technical anachronism
- NarrativeProjection fidelity
- plot conditioning / provenance

判定は `PASS / FAIL / UNCERTAIN`。

`PASS`は真理保証ではなく、使用したevidenceとreview時点で公開を妨げる意味論上の矛盾が見つからないことを意味する。

## 話別検証ループ

```text
成立済みEVT / state
        ↓
chapter draft
        ↓
壊れやすい依存点を選定
        ↓
Mandatory Verification
        ↓
必要ならQ / H / EXP / researchへ分岐
        ↓
結果・一次資料・Findingを回収
        ↓
本文へfeedback
        ↓
semantic review
        ↓
style pass
        ↓
static / executable checks
        ↓
PREPUBLICATION_GATE_PASSED
```

## 用語

全作品共通Glossaryを先に作らない。

各話で実際に登場した語だけを、その話の `terminology.md` に置く。未検証語は `UNVERIFIED` のまま残し、gate通過時にはblockingな未検証語を残さない。

## 公開前相互作用

検証結果が本文と衝突した場合、原則として本文を修正する。

- 当時使われていない訳語 → 時代に合う表現へ変更
- 数式・条件が証拠と違う → 本文を証拠へ合わせる
- 人物が知り得ない語・情報 → 発話/描写を変更
- 史実不確実性 → 断定を弱めるかUNRESOLVEDへ戻す

公開都合で検証結果を曲げない。

## 機械検査

通常:

```bash
python tools/validate_workflow.py
```

公開前・main比較前:

```bash
python tools/validate_workflow.py --strict
```

コード化された話別検証:

```bash
python tools/run_chapter_experiments.py
```

validatorは構造・traceabilityを検査する。semantic reviewを置いたこと自体は確認できるが、その内容の真偽を自動証明しない。

## 公開判定

各話は少なくとも次を確認してから公開候補とする。

- [ ] 採用EVT/stateと本文が矛盾しない
- [ ] `verification.md` が存在しPASS
- [ ] コード化された検証は再実行してPASS
- [ ] `semantic-review.md` が存在しPASS
- [ ] 重要な技術主張が検証済み、または不確実性が適切に表現されている
- [ ] story time上で不可能な未来用語・未来知識が人物へ漏れていない
- [ ] 用語表記がその話の検証結果と一致している
- [ ] 数値・手順・条件が参照EVT/EXP/evidenceと一致している
- [ ] 史実・制度・設備の重要描写に根拠がある
- [ ] unresolved事項を本文都合だけでCanon固定していない
- [ ] `python tools/validate_workflow.py --strict` がPASS

通過状態は `PREPUBLICATION_GATE_PASSED` とする。

この状態は**工程gate通過**を意味する。科学的・歴史的完全性、文学的完成、Canon昇格、公開承認を意味しない。
