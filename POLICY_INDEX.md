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
| `novel/bootstrap/README.md` | 時点初期化・再初期化 | 未来plot |
| `experiments/README.md` | Q/H/EXP、実験判定、再現性 | 話数構造 |
| `experiments/chapters/README.md` | 各話の公開前integration verification | 全作品Glossary |
| `novel/STYLE_WEBNOVEL.md` | NarrativeProjectionの読みやすさ・表記 | 技術事実の上書き |
| `AGENTS.md` | AIが作業するときの読み順・実行手順 | Canonそのもの |

## Entity ID class

研究IDとは別に、World Stateの独立entityが必要になった場合は次を使用する。

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

`PHY`は通常ID化せずconstraintとして扱う。

ID発行条件・lazy expansionは `novel/WORLD_POLICY.md` に従う。

## Research / story ID class

- `Q-xxx`: question
- `H-xxx`: hypothesis
- `EXP-xxx`: experiment
- `F-xxx`: finding
- `REF-xxx`: reference
- `L-xxx`: learning record
- `EVT-xxx`: story event
- `BOOT-xxx`: bootstrap frame

一度割り当てたstable IDは意味を差し替えず再利用しない。

## Workflow validation

`WORKFLOW.md` の固定工程は次で静的検査する。

```bash
python tools/validate_workflow.py
```

公開前またはmain比較前の厳格確認:

```bash
python tools/validate_workflow.py --strict
```

validatorは構造・traceabilityを検査する。歴史的正しさ、personaの心理的自然さ、数学的正しさ、小説品質は別の意味レビューが必要である。
