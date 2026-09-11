# 作業コンテキスト

更新: 2026-09-12
公開可能な引継ぎ用索引。内部推論や秘密情報は保存しない。

## 現在位置

- branch: `work/story-bootstrap`
- 1980年代側head: `EVT-015`
- active: PER-005 高橋修一 / PER-006 佐伯玲子 / ORG-001
- 現代側event: none
- main / PR / docs / 公開には触れていない

第1〜4話はEVT-001〜013をNarrativeProjection済みで `PREPUBLICATION_GATE_PASSED`。EVT-014〜015は未投影。

## 読者ロス監査

`reader-loss-audit-2026-09-11.md`。実読者データではなく編集simulation。

第1話は据え置き。第2〜4話は、手続き説明より発見を前景化する改稿を行い、candidate CI成功後にgateへ戻した。

## EVT-014 / EVT-015

EVT-014は結果前lock済みのQ one-bit accessibility check。

- 16 one-bit initial states × 16 cyclic orders = 256
- Q=112
- M1=M2=M3=48
- nonconverged=0
- unanimous 4 positionsのflipは全orderでQへ復帰
- split 12 positionsはorder-dependent
- Qへ戻らないtrialはcoordinate-minority stored patternへだけ到達

EVT-015で幾何を分類。

- split flip: minority memory distance 4→3 / overlap 8→10、他二つ distance 4→5 / overlap 8→6
- unanimous flip: 三つすべて distance 4→5 / overlap 8→6

人物はここまで知る。

## 作者側研究 — 人物へ漏洩禁止

EXP-006: N=16/P=3、256 eligible triples、65,536 trajectories。primary Hは弱いSUPPORT。secondaryでsplit non-Q 17,488/17,488がcoordinate-minority stored patternへ到達。

EXP-007: 反例探索。N=8,12,16,20,24、640 eligible triples、362,704 trajectories。non-Q 111,680件、counterexample 0。`NO_COUNTEREXAMPLE_IN_SEARCH`。proofではない。

この結果はPER-005/PER-006のKnowledgeへ入れない。

## 再開時の注意

world/persona snapshotがEVT-007で止まって見えても、EVT-008〜015とdeltaをoverlayする。同じ差分を二重加算しない。

LOCKEDは盲検ではない。作者側EXP結果をstory人物へ自動共有しない。trial数を増やすこと自体を目的にしない。

## ロードマップ

自律的に実施可能だった既存4話の整合・検証、読者ロスsimulation、world advancement、story-derived research branchは進行済み。

外部主体が必要な5人以上の実読者試読、Human Review、完全独立な別主体restore/action-selectionは未実施。AI内simulationで代替済みとは扱わない。

次の作者側研究はEXP-007 findingの解析的証明/反例構成。story側はEVT-015現在stateからのみ進める。
