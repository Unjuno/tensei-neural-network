# 固定制作ワークフロー

状態: `ACTIVE / PROVISIONAL`

この文書は、物語を生成し、検証し、公開候補へ進めるまでの固定工程を定義する。

上位規則は `POLICY.md`。世界進行は `novel/WORLD_POLICY.md`、state lifecycleは `novel/state/LIFECYCLE.md`、研究実験は `experiments/README.md`、話別検証は `experiments/chapters/README.md`、文体投影は `novel/STYLE_WEBNOVEL.md` に従う。

優先順位:

```text
POLICY.md
  > domain policy / workflow
  > event / state / experiment / research evidence
  > style rule
  > chapter draft
```

本文や文体規則は、event/state/evidenceを上書きしない。

## 1. 制作の一本道

```text
A. Restore
   story time / event head / relevant statesを復元
        ↓
B. Advance World
   scope → observation → action → resolve → EVT → state delta
        ↓
C. Detect Reading Unit
   成立済みEVT群から自然な読書単位を発見
        ↓
D. Minimum Causal Outline
   採用EVTだけで最小因果骨格を作る
        ↓
E. Narrative Projection
   EVT/stateを章本文へ投影
        ↓
F. Mandatory Verification
   章の最も壊れやすい依存点を最低1回検証
        ↓
G. Feedback
   evidenceと本文が衝突すれば本文を修正
        ↓
H. Semantic Review
   knowledge / history / provenance / projectionを意味レビュー
        ↓
I. Style Pass
   読みやすさを改善。事実は変更しない
        ↓
J. Prepublication Gate
   static + executable + semantic checks
        ↓
K. Human Review
   Canon昇格・main反映・公開は人間が受理
```

この順序は原則固定する。

## 2. 最重要原則

### 物語を検証へ従属させない

必須なのは「毎話に科学実験を登場させること」ではない。

```text
1 chapter != 1 research EXP
1 chapter >= 1 mandatory verification
```

先にEVT/stateから章が成立する。その後で、その章が依存する最も壊れやすい主張を選んで検証する。

検証方式は章に応じて変えてよい。

- 数理・コード → executable reproduction
- 歴史 → historical source check
- 文書・物 → provenance trace
- 会話・秘密 → knowledge-boundary trace
- 組織・制度 → institutional constraint check

「検証するものが必要だから」という理由でeventを発生させない。

### 追跡可能性を主目的にする

このsystemが保証する中心は「作品が絶対に正しいこと」ではなく、

- どのEVT/stateから本文が作られたか
- どのevidenceで何を確認したか
- 何が未確定か
- どの判断・限界が残っているか

を後から辿れることである。

正しさは新しい史料・研究で更新され得る。provenanceと再現可能性は残す。

## 3. 禁止されるショートカット

- 完成プロットへpersona/worldを誘導する
- 章の結末から過去EVT/stateを書き換える
- 章本文だけを書いて検証を省略する
- Mandatory Verificationのために物語へ実験現象を追加する
- 既存EXPを参照しただけで話別検証済みとする
- 研究結果を未観測人物へ逆流させる
- 文体都合でevidenceを変更する
- `起承転結`、話数、EXP番号をevent発生原因にする
- CI greenを内容の真理保証とみなす
- `PREPUBLICATION_GATE_PASSED`をCanon/公開承認とみなす

## 4. 各工程

### A. Restore

入力:
- `STATUS.md`
- `notes/working-context.md`
- 対象BOOT
- relevant state / event

出力:
- current story time
- event head
- active states
- dormant statesのうち再展開が必要なもの
- unresolved items

DORMANT/REACTIVATED/checkpointは `novel/state/LIFECYCLE.md` に従う。

### B. Advance World

`novel/WORLD_POLICY.md` に従い、現在因果へ届くresolution scopeだけを解決する。

必要なら`ACTION_LOCKED`を行い、EVTとaffected state deltaを保存する。

### C-D. Reading Unit / Outline

成立済みEVTのみから `novel/chapters/NNN-outline.md` を作る。未来eventを混ぜない。

### E. Narrative Projection

`novel/chapters/NNN.md` はEVT/stateのprojectionであり、新しい客観factの発生源ではない。

### F. Mandatory Verification

各話に `experiments/chapters/NNN/verification.md` を置く。

最低限:
- target
- selection rationale
- verification type
- evidence
- pass/fail criteria
- result
- limitations
- chapter feedback

コード化可能なら `run.py` と機械可読結果を保存する。コード化不能でも第三者が追跡できる資料・手順・判定を残す。

### G. Feedback

検証結果と本文が衝突した場合は、原則として本文を修正する。必要ならevent/state/researchへ戻るが、本文都合でevidenceを曲げない。

### H. Semantic Review

各公開候補話に `semantic-review.md` を置き、少なくとも次を確認する。

- knowledge boundary
- unresolved fact invention
- historical / technical anachronism
- NarrativeProjection fidelity
- plot conditioning / provenance

テンプレート: `experiments/chapters/SEMANTIC_REVIEW_TEMPLATE.md`

semantic reviewは自動真理判定ではない。review inputs・判断・uncertaintyを固定し、後から再検討可能にするための記録である。

### I. Style Pass

読みやすさ、段落、会話、専門語提示順を改善する。この工程で技術条件・historical fact・stateを変更しない。

### J. Prepublication Gate

最低条件:

- adopted EVT/stateと本文が整合
- `verification.md`: PASS
- executable verificationがある場合は再実行PASS
- `semantic-review.md`: PASS
- blockingな未検証用語なし
- 未来知識漏洩なし
- 数値・手順・条件がevidenceと一致
- 重要な歴史・制度描写に根拠あり
- unresolved事項を本文だけでCanon固定していない
- strict validator PASS

通過状態:

`PREPUBLICATION_GATE_PASSED`

これは工程gate通過を意味するだけで、科学的完全性、歴史的完全性、文学的完成、Canon昇格、公開承認を意味しない。

## 5. 検証システム

静的検査:

```bash
python tools/validate_workflow.py
python tools/validate_workflow.py --strict
```

コード化された話別検証:

```bash
python tools/run_chapter_experiments.py
```

GitHub Actionsはpush時に、

1. validator unit tests
2. executable chapter verifications
3. strict workflow validator

を実行する。

CIが証明するのは**機械化した工程条件が通ったこと**であり、作品内容そのものの真理ではない。

## 6. State lifecycle

一度詳細化したentityを永続的にactiveへ固定しない。

- 現在因果へ必要 → ACTIVE
- 現在scope外で復元可能 → DORMANT
- 再び因果へ届く → trusted snapshot + relevant deltasからREACTIVATE

過去EVT/stateを削除せず、checkpointは圧縮キャッシュとして使う。

詳細: `novel/state/LIFECYCLE.md`

## 7. 実行タイミング

最低限、次で検証する。

1. 新しいEVT/state群をまとめた後
2. 章本文を作成・大幅改稿した後
3. Mandatory Verificationを追加・変更した後
4. semantic review後
5. `PREPUBLICATION_GATE_PASSED`へ変更する前
6. `main...work branch`を人間へ提示する前
