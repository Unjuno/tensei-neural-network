# Semantic Review Template

このテンプレートは、機械validatorでは判定できない話別の意味レビューを再現可能な形で残すために使う。

各話では `experiments/chapters/NNN/semantic-review.md` として保存する。

状態: `IN_PROGRESS | PASS | FAIL | UNCERTAIN`

## Evidence inputs

- Chapter:
- Adopted EVT range:
- World/persona/organization state:
- Chapter verification:
- Research / references:
- Story time:

## Checks

### 1. Knowledge boundary

確認対象:
- 人物が未観測情報を知っていないか
- author-side researchがstory timeへ逆流していないか
- 組織知と個人知を混同していないか

判定:

根拠:

### 2. Unresolved fact invention

確認対象:
- 本文だけで年月日、機種、職位、所在地、関係等を新しい客観factとして固定していないか

判定:

根拠:

### 3. Historical / technical anachronism

確認対象:
- 時代に存在しない用語・制度・装置・論文知識を使っていないか
- 不確実な史実を断定していないか

判定:

根拠:

### 4. NarrativeProjection fidelity

確認対象:
- 本文が採用EVT/stateの範囲を超えていないか
- 意図とworld resultを混同していないか
- 本文が新しいworld factの発生源になっていないか

判定:

根拠:

### 5. Plot conditioning / provenance

確認対象:
- 望ましい章展開を理由に過去EVT/stateを変更していないか
- `LOCKED / UNBLINDED / AUTHOR_CONDITIONED` 等のprovenanceを隠していないか

判定:

根拠:

## Findings

- Blocking:
- Non-blocking:
- Allowed unresolved:

## Required fixes

- なし / 修正内容

## Verdict

`PASS | FAIL | UNCERTAIN`

この判定は、科学的・歴史的真理の最終保証ではない。使用したevidenceとreview時点で、公開前gateを妨げる意味論上の矛盾が見つかったかを表す。
