# 現在の状態

更新: 2026-10-31。これは索引であり、直接のEVT・state・実験記録・CIを優先する。会話内の要約よりGitHub正本を参照する。

## 作業と承認の境界

- 作業branch: `work/story-bootstrap`
- 1980年代story側のresolved event head: **`EVT-018`**
- 現代側event head: none
- active: PER-005 高橋修一 / PER-006 佐伯玲子 / ORG-001 光陵化学生命科学研究所
- `main`反映、PR作成、公開・Canon昇格は未承認。自律実行時にも行わない
- 実読者試読・Human Review・別主体の完全独立restoreは未実施。AIの模擬を実測値にしない

## 小説

| 本文 | 採用EVT | 事前公開検証 |
|---|---|---|
| 第1話「戻る先」 | EVT-001〜004 | PREPUBLICATION_GATE_PASSED |
| 第2話「選ばなかった答え」 | EVT-005〜008 | PREPUBLICATION_GATE_PASSED |
| 第3話「表の外」 | EVT-009〜011 | PREPUBLICATION_GATE_PASSED |
| 第4話「五と二十一」 | EVT-012〜013 | PREPUBLICATION_GATE_PASSED |
| **第5話「最初に動いたもの」** | **EVT-014〜018** | **PREPUBLICATION_GATE_PASSED** |

第5話はEVT-014の256 locked trials（Q=112、M1/M2/M3各48）、EVT-015の距離分類、EVT-016の最初の実flip、EVT-017のinitial unstable集合、EVT-018のcyclic gap数え上げに基づく。112/256を自然確率・一般的basin確率へ読み替えない。

第5話candidate CIは `34817720509` success。2026-10-30の修正を含むHEAD `80c1fc57de3c2eb08200a5780d99613f78764a04` に対して、GitHub Actions run `41073506726` がsuccess。第1〜5話、既存研究実験、EXP-013再実行と保存JSON完全照合、workflow検査が全step成功。後続編集では新しいHEADのCIを改めて確認する。

## 状態復元

起点 `BOOT-002 @ T0-1980S @ none`。1984〜85年前後の具体年月日はまだ固定しない。古い`novel/state/world.md`やpersona snapshotはmaterialized checkpointであり、EVT-008〜018の直接記録と存在するentity deltasで復元する。EVTとdeltaを二重加算しない。本人が観測したことだけをpersona Knowledgeへ投影する。現代側は未進行。

## 作者側研究（1980年代人物への知識漏洩禁止）

- **EXP-006 / 007:** P=3 majority Qの一bit摂動に対する少数派記憶へのescapeを有限探索し、後に記載条件下で証明。非同期の公平な更新が必要
- **EXP-008:** 同期一括更新に替えるとN=8でperiod-2 cycleが出る反例を確認。収束保証と、固定点に至った際の分類を混同しない
- **EXP-009:** 更新方式の厳密な境界について事前登録済み。READMEの実施状態を先に照合してから進める
- **EXP-010:** 偶数Nでzero marginを探索した設計は構造的に不適格でUNCERTAINとして終了
- **EXP-011:** 奇数Nで304,038 trajectoriesに反例なし。解析ではP=3 majority Qにnonnegative stability（ゼロ入力保持）まで条件を緩めて証明
- **EXP-012:** P=5では別のnonstored fixed pointへ逃げる反例を確認
- **EXP-013:** N=7〜16、640 eligible triples、**139,440 trajectories**で事前登録のmargin三領域予測が全件一致。別実装で集計を再現。2026-10-30にREADMEを完了へ更新し、結果照合のCI stepも成功した

これらは作者側の検証・解析であり、PER-005/PER-006へ自動注入しない。研究上の定理、実験、物語内の観測、文学的評価を分ける。

## ロードマップと次の作業

`notes/assessment-and-roadmap.md` を長期目標、`notes/roadmap-progress-2026-10-30.md` を最新の進捗として参照。先の`notes/roadmap-progress-2026-09-12.md`はその時点の履歴であり現在地ではない。

直近の優先順は、(1)独立restoreが古いheadを採用しないことの検証、(2)人物側EVT-018からの自然な行動・読書上の緊張の評価、(3)事前登録済みEXP-009の可否判定、(4)実読者データを得た際のpilot集計。

外部承認が必要なまま残す項目: 実読者最低5名、Human Review、公開、main反映、真に独立な別主体による意味復元。

未確定: 研究所の詳細所在地・職位・具体年月日・共用計算機/OS/言語・現代側最初のEVT・人物の未成立の私生活史。プロットの都合で先に固定しない。

## 2026-10-31 小説優先の探索（未採用）

確認起点: `d4fb65f7f0f3757f4e4b616303f5b4e60b016523`（work branch）。前回の自動実行履歴はまだ存在しないため、比較可能な直前commitは `d960d960773904dea1e1927c3615ad9380e4f35d`。その差分は `notes/roadmap-progress-2026-10-30.md` のEXP-013状態索引補正のみ。起点HEADのCI run `41073799005` は全step成功。

EVT-018後の二人のGoalから、「組合せ的な説明と元の観測記録を、他者が検査できるようにどう残すか」を一つの次の問いとして選んだ。 `novel/scene-probes/2026-10-31-circle-and-original-records.md` に**未採用の場面試作**を保存。第5話本文と既存EVTは変更せず、EVT-019・第6話・新研究結果を成立させない。読者・Human Review・独立restoreも未実施のまま。

直近の一手: 場面試作を人物の既知事項とORGのInstitutional memory境界に照合し、採用するなら新たな人物行動を先に解決する。既存第5話の章索引漏れは `novel/chapters/README.md` に補正。CIは今回の新HEADを別途確認する。
