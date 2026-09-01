# 第2話 Semantic Review

状態: `PASS`

## Evidence boundary

- Narrative source: `novel/chapters/002.md`
- Adopted events: EVT-005〜EVT-008
- Mandatory Verification: `verification.md` / `run.py` / `results.json`
- Historical background: `research/pre-hopfield-background.md`
- Persona knowledge: PER-005 / PER-006 state through EVT-008

## Knowledge leakage

PASS。

本文に出る6 cyclic orders、36 trials、384 trials、D=-C、符号反転対称性は、すべてEVT-005〜008で二人が観測・導出した範囲にある。現代EXP-003〜005の統計値や後世の研究結果は人物へ流入していない。

## Unresolved fact invention

PASS。

具体年月日、計算機機種、OS、プログラミング言語を本文で固定していない。ORG-001の将来も描いていない。

## Historical / technical anachronism

PASS WITH BOUNDARY。

1982〜84年にはcontent-addressable memory、stable/spurious states、binary threshold network、statistical-physics的解析が既に研究対象であり、人物がこのtoy networkの安定状態と更新則を検討すること自体は時代範囲内。

ただし本文は後世の一般的なニューラルネットワーク語彙を人物に過剰付与しない。専門語は章別terminology reviewで別途管理する。

## NarrativeProjection fidelity

PASS。

EVT-005→006→007→008の因果順を維持している。特にDを最初から`-C`と知っている形にせず、EVT-005/006では暫定名Dとして扱い、全状態列挙後にD=-Cへ再分類する認識転換を保存している。

## Plot conditioning

PASS WITH PROVENANCE NOTE。

採用eventは既にLOCKED provenanceを持つ。本文は章末のために結果を変更していない。Mandatory Verification初回FAILも隠さず、D/-Cの時点別label衝突として記録した。

## Generalization boundary

PASS。

本文中の佐伯の「少なくとも、この結合と更新規則では」が一般化を抑制している。有限6-unit toy networkの結果を、生物学的記憶やHopfield network一般の性質として断定していない。

## Required fixes

公開前gateを止めるsemantic fixなし。

## Verdict

第2話は、現在のEVT/state/evidenceに対するNarrativeProjectionとして意味論上PASS。
