# Policy Index

状態: `ACTIVE / PROVISIONAL`

このファイルはポリシーそのものではなく、**どの規則をどこで管理するか**を一枚で示す索引である。

## 優先順位

```text
1. POLICY.md
2. domain policy / fixed workflow
3. event / state / experiment / research evidence
4. style rules
5. chapter draft
```

同じlevelで矛盾する場合は、より具体的で新しい正本を確認し、必要ならroot policyに反しない形へ統合する。

## 正本の役割

| ファイル | 役割 | 書かないもの |
|---|---|---|
| `POLICY.md` | repo全体の憲法。正本、branch、研究、小説、情報境界、人間レビュー | 個別sceneの手順、細かい文体例 |
| `WORKFLOW.md` | Restoreから公開前gateまでの固定工程 | 世界モデル詳細、個別研究結果 |
| `novel/WORLD_POLICY.md` | 階層World State、entity、resolution scope、world advancement | 公開用文体 |
| `novel/state/LIFECYCLE.md` | ACTIVE/DORMANT/REACTIVATED、checkpoint、state復元コスト管理 | 個別eventの内容 |
| `novel/bootstrap/README.md` | 時点初期化・再初期化 | 未来plot |
| `experiments/README.md` | Q/H/EXP、実験判定、再現性 | 話数構造 |
| `experiments/chapters/README.md` | 各話のMandatory Verificationと公開前gate | 全作品Glossary |
| `experiments/chapters/SEMANTIC_REVIEW_TEMPLATE.md` | 意味レビューの固定入力・確認項目・判定形式 | 自動真理判定 |
| `novel/STYLE_WEBNOVEL.md` | NarrativeProjectionの読みやすさ・表記 | 技術事実の上書き |
| `AGENTS.md` | AIが作業するときの読み順・実行手順 | Canonそのもの |

## Entity ID class

- `PER-xxx`: person / artificial cognitive agent
- `ANI-xxx`: animal
- `OBJ-xxx`: object / document / device / sample
- `ORG-xxx`: organization / institution
- `GRP-xxx`: group / laboratory / household / team
- `LOC-xxx`: tracked location
- `POL-xxx`: polity / jurisdiction
- `ENV-xxx`: independently tracked environment
- `SYS-xxx`: infrastructure / market / computing system
- `PHY-xxx`: exceptional tracked physical/cosmological regime

`PHY`は通常ID化せずconstraintとして扱う。ID発行条件・lazy expansionは `novel/WORLD_POLICY.md`、追跡解像度は `novel/state/LIFECYCLE.md` に従う。

## Research / story ID class

- `Q-xxx`: question
- `H-xxx`: hypothesis
- `EXP-xxx`: research experiment
- `F-xxx`: finding
- `REF-xxx`: reference
- `L-xxx`: learning record
- `EVT-xxx`: story event
- `BOOT-xxx`: bootstrap frame

話別Mandatory Verificationには新しいstable IDを必須としない。話数directoryと `verification.md` でtraceabilityを持たせ、研究として独立した場合だけQ/H/EXPへ分岐する。

## 公開前状態

`PREPUBLICATION_GATE_PASSED` は固定workflowの公開前gateを通過した状態である。

これは、

- 科学的・歴史的完全性
- 文学的完成
- Canon昇格
- 公開承認

を意味しない。

旧称 `PREPUBLICATION_VERIFIED` は使用しない。

## Workflow validation

```bash
python tools/validate_workflow.py
python tools/validate_workflow.py --strict
python tools/run_chapter_experiments.py
```

validatorは構造・traceabilityを検査する。semantic reviewは入力・判断・uncertaintyを追跡可能にするが、AI/人間レビューの内容そのものを機械的に真と証明しない。
