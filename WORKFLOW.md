# 固定制作ワークフロー

状態: `ACTIVE / PROVISIONAL`

この文書は、このrepoで物語を生成し、研究・実験で検証し、章を公開候補へ進めるまでの**固定的な工程順序**を定義する。

上位規則は `POLICY.md`。世界進行の詳細は `novel/WORLD_POLICY.md`。実験一般は `experiments/README.md`。話別公開前検証は `experiments/chapters/README.md`。文体投影は `novel/STYLE_WEBNOVEL.md` に従う。

矛盾時の優先順位:

```text
POLICY.md
  > domain policy / workflow
  > event / state / experiment evidence
  > narrative style rule
  > chapter draft
```

ただし、歴史・科学・数理上の事実判定では、文体規則や本文がevent/state/experiment/research evidenceを上書きしない。

---

## 1. 制作の一本道

```text
A. Restore
   repo正本からstory time / event head / entity statesを復元
        ↓
B. Advance World
   resolution scope → observation → action → resolve → EVT → state delta
        ↓
C. Detect Reading Unit
   成立済みEVT群に自然な読書単位があるか判定
        ↓
D. Minimum Causal Outline
   採用EVTだけから最小因果骨格を作る
        ↓
E. Narrative Projection
   state/eventを章本文へ投影する
        ↓
F. Chapter Verification Package
   experiments/chapters/NNN/ を作る
        ↓
G. Mandatory Chapter Experiment
   各話最低1回、章が依存する内容を実際に再現・検証する
        ↓
H. Feedback
   検証結果と本文を相互照合し、誤りは本文側を修正
        ↓
I. Style Pass
   読みやすさを改善。ただし事実・stateを変更しない
        ↓
J. Prepublication Gate
   必須検査を通した場合だけ公開候補化
        ↓
K. Human Review
   Canon昇格・main反映・公開は人間の受理を必要とする
```

この順序は原則固定する。

## 2. 禁止されるショートカット

- 完成プロットを先に作り、persona/worldをそこへ誘導する
- 章の結末から過去EVT/stateを書き換える
- 章本文だけを書いて話別検証を省略し、公開候補にする
- **話別実験を一度も実行せず章を公開候補にする**
- 既存EXPを参照しただけで「実験済み」とみなす
- 用語を作品全体Glossaryで先回り固定する
- 研究結果をstory time上で未観測の人物へ逆流させる
- 文体上の都合でevent/state/experiment evidenceを変更する
- `起承転結`、話数、EXP番号をevent発生原因にする
- `PREPUBLICATION_VERIFIED` を人間確認なしの最終公開承認とみなす

## 3. 各工程の入力と出力

### A. Restore

入力:
- `POLICY.md`
- `STATUS.md`
- `notes/working-context.md`
- 対象 `BOOT-*`
- `novel/state/`
- `novel/events/`
- `novel/timeline.md`

出力:
- current story time
- current event head
- active entity states
- unresolved items
- local questions

### B. Advance World

入力:
- current states
- entity relations
- physical / historical / institutional constraints

出力:
- 必要なら `ACTION_LOCKED`
- `EVT-xxx`
- affected state deltas
- index sync

### C-D. Reading Unit / Outline

入力:
- 成立済みEVTのみ

出力:
- `novel/chapters/NNN-outline.md`

未来eventをoutlineへ混ぜない。

### E. Narrative Projection

入力:
- 採用EVT
- 対応state
- persona / organization definitions
- style policy

出力:
- `novel/chapters/NNN.md`

本文は新しい客観factの発生源ではない。

### F-G-H. Chapter Verification / Mandatory Experiment / Feedback

入力:
- chapter draft
- EVT/state
- EXP/research/reference

必須出力:
- `experiments/chapters/NNN/README.md`
- `experiments/chapters/NNN/experiment.md`
- 必要な話別検証ファイル
- コード化可能なら `run.py` と機械可読な結果
- 検証結果に応じた本文修正

各話は最低1回、章本文が依存する内容を実際に再現・検証する。

```text
1 chapter != 1 research EXP
1 chapter >= 1 chapter-level experiment
```

研究上の新規性がなくてもよい。既存EVTやEXPの中心結果を、その章の公開前integration testとして再実行してよい。

用語はその話で使う語だけを話別package内で検証する。

### I. Style Pass

読みやすさ、段落、会話、専門語の提示順を調整する。

この工程で技術条件やhistorical factを変更しない。

### J. Prepublication Gate

最低条件:

- 採用EVT/stateと本文が矛盾しない
- `experiment.md` が存在し、話別実験がPASSしている
- コード化された話別実験は再実行してPASSする
- 重要な技術主張が検証済み、または不確実性が本文へ反映済み
- 未来知識漏洩がない
- 話別用語検証と本文が一致する
- 数値・手順が参照EXP/eventと一致する
- 重要な歴史・制度・設備描写に根拠がある
- unresolved事項を本文だけでCanon固定していない

`PREPUBLICATION_VERIFIED` はこのgate通過を意味するだけで、Canon昇格や公開承認ではない。

---

## 4. 検証システム

固定ワークフローは二種類の機械検証を使う。

### 静的workflow検査

```bash
python tools/validate_workflow.py
python tools/validate_workflow.py --strict
```

- `ERROR`: ワークフローの構造違反。exit code 1
- `WARN`: 人間/AIの意味レビューが必要。通常modeではexit code 0、`--strict`では1
- `PASS`: 静的検査上問題なし

### コード化された話別実験の再実行

```bash
python tools/run_chapter_experiments.py
```

`experiments/chapters/NNN/run.py` が存在する章を発見し、`--check`で再実行する。

### 自動検査するもの

- 必須policy/workflowファイルの存在
- chapterと話別verification packageの対応
- **各chapterに `experiment.md` が存在すること**
- `PREPUBLICATION_VERIFIED`章の話別実験がPASSであること
- コード実験がある場合の`results.json`とPASS状態
- chapter outlineが参照するEVTの存在
- `PREPUBLICATION_VERIFIED`章に未検証用語が残っていないか
- 主要ID定義ファイル/ディレクトリの重複番号
- 第1話で検証により廃止した古い英語ルビ表現の再混入
- root policy / domain policy参照の最低限の整合

### 自動検査しないもの

次は意味論なので静的scriptだけでPASS判定しない。

- personaが本当にその情報を知り得たか
- 歴史資料の品質
- 数理モデルそのものの科学的妥当性
- 小説として自然か
- plot誘導が本当に無かったか
- Canonへ昇格すべきか

これらは話別検証とhuman reviewで扱う。

---

## 5. GitHub Actions

`.github/workflows/story-workflow-validation.yml` で、`main`と`work/**`へのpush時に次を自動実行する。

1. workflow validatorのunit tests
2. コード化された話別実験の再実行
3. `python tools/validate_workflow.py --strict`

GitHub Actionsの追加は人間指示を受けて導入済みである。

---

## 6. 実行タイミング

最低限、次の時点で検証する。

1. 新しいEVT/state群をまとめた後
2. 章本文を作成・大幅改稿した後
3. 話別実験を追加・変更した後
4. `PREPUBLICATION_VERIFIED`へ変更する前
5. `main...work branch`を人間へ提示する前

章を公開候補へ進める際は、**話別実験の実行とCI PASSの両方**を確認する。
