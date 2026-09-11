# 現在の状態

更新: 2026-09-12
このファイルは索引。直接のEVT・state・検証結果を優先する。

## 作業と公開の境界

- 作業branch: `work/story-bootstrap`
- story head: `EVT-015`
- 現代側event head: none
- mainへの反映、PR作成、docs同期、公開は行っていない
- 第1〜4話は `PREPUBLICATION_GATE_PASSED`。独立実読者試読・Human Reviewは未実施

## 第1〜4話

| 話 | 採用EVT | 状態 |
|---|---|---|
| 1 戻る先 | EVT-001〜004 | PREPUBLICATION_GATE_PASSED |
| 2 選ばなかった答え | EVT-005〜008 | PREPUBLICATION_GATE_PASSED |
| 3 表の外 | EVT-009〜011 | PREPUBLICATION_GATE_PASSED |
| 4 五と二十一 | EVT-012〜013 | PREPUBLICATION_GATE_PASSED |

読者ロス監査: `notes/reader-loss-audit-2026-09-11.md`。これは編集simulationで、実読者データではない。

## 現在世界の復元

起点は `BOOT-002 @ T0-1980S @ none`。時代は1984〜85年前後を候補とし具体年月日は未確定。

active: PER-005 高橋修一、PER-006 佐伯玲子、ORG-001 光陵化学生命科学研究所。

`world.md`と人物snapshotの一部はEVT-007まで。EVT-008〜015と対応deltaを適用して復元し、古いsnapshotへ巻き戻さない。同じ差分をEVTとdeltaから二重加算しない。

## EVT-014〜015

EVT-014では結果前に、QのHamming距離1近傍16状態 × `1..16` cyclic rotation 16本 = 256 trialを固定した。

結果:

- Q: 112
- M1/M2/M3: 各48
- nonconverged: 0
- 全員一致位置k=1,2,7,8のflipは16/16 orderでQへ復帰
- 2対1位置のflipはorder-dependentで、Qへ戻らない場合はその位置の少数派stored patternへだけ到達

EVT-015では追加trialなしで距離を分類。2対1位置をflipすると少数派stored patternだけがQからの距離4→3、他二つは4→5。全員一致位置では三つとも4→5。

この結果は第5話へまだ投影していない。

## 作者側研究 EXP-006 / EXP-007

物語から派生した作者側研究として、EVT-014の一例を一般化せず検証した。

### EXP-006

N=16/P=3のstable nonstored majority mixtureを固定seedから256例採用し、65,536 trajectoriesを事前登録条件で実行。

primary H-006は事前規則上SUPPORTだが、mean(`r_u-r_s`)≈0.00128で効果はheterogeneous。

重要なsecondary finding:

- Q以外final 23,444件はすべてstored pattern
- split one-bit trialでQへ戻らなかった17,488 / 17,488件がcoordinate-minority stored patternへ到達

### EXP-007

上記secondary findingの反例探索を事前登録。N=8,12,16,20,24、640 eligible triples、362,704 trajectoriesを固定条件で探索。

- non-Q trajectories: 111,680
- counterexample: 0
- 結果: `NO_COUNTEREXAMPLE_IN_SEARCH`

これは一般定理の証明ではない。次に価値があるのはtrial数を増やすことではなく、P=3 majority mixtureの代数から証明または反例を構成すること。

作者側EXP-006/007の結果をPER-005/PER-006へ自動注入していない。人物が知るのはEVT-015まで。

## ロードマップ進捗

自律的に解決可能な項目:

- 既存4話の対象版・数理再現・workflow integrity: 実施済み
- 読者ロスの編集simulation: 実施済み
- EVT-013後のworld advancement: EVT-015まで進行
- story observationからの新研究分岐: EXP-006/007まで実施

外部入力が必要で未解決:

- 5人以上の独立実読者試読
- 人間による公開受理
- 別主体による完全独立restore / action-selection評価

これらをAI内simulationで「解決済み」と偽装しない。

## 次の優先

1. EXP-007の規則を解析的に証明または反例構成できるか検討する
2. story側ではEVT-015現在stateから自然な次行動を選ぶ。作者側EXP-006/007を未来知識として使わない
3. 256 trialを本文へ投影する必要が生じた場合、1984〜85年の共用計算機・OS・言語を一次/機関史料で具体化する
4. 実読者試読が得られたら、reader-loss simulationと照合する

## 残る未確定

研究所の所在地・部門・職位・設立細部、具体年月日、共用計算機・OS・言語、人物の生活史、研究所の将来、現代側最初のevent、第5話以降。必要前に一括固定しない。

## 検証系

`WORKFLOW.md` を参照。chapter verificationに加え、EXP-006/007の保存結果をCIで再計算照合する。Human ReviewはCIとは別である。
