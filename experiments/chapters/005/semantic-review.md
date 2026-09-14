# 第5話 Semantic Review

状態: `PASS`

レビュー種別: 本制作セッションでのAI再読。独立した実読者・別担当・盲検レビューではない。
対象本文: `novel/chapters/005.md`
採用event: EVT-014 -> EVT-018。

## Evidence inputs

本文、outline、EVT-014〜018、そこまでのpersona/world state、chapter verification、terminologyを照合した。

## Knowledge boundary

本文中の高橋・佐伯が使う情報はEVT-018までに二人自身が観測・再計算したものだけ。

作者側EXP-006〜011の一般化実験、反例、解析証明は本文へ入れていない。

特に、P=3でcoordinate-minority escapeが一般条件下で証明できるという作者側知識を人物の台詞・地の文へ注入していない。

## NarrativeProjection fidelity

本文は次の成立済みfactsだけを使用する。

- 16 one-bit states × 16 cyclic orders = 256
- aggregate Q=112, M1=M2=M3=48
- unanimity 4 positionsは16/16 Q
- split 12 positionsはorder-dependent
- split flipでminority memoryだけdistance 4→3、他二つ4→5
- split 192 trialでrepair-first 48→Q、other-first 144→minority
- repair branchは実flip1、minority branchは実flip3
- 12/12でinitial unstable set = Qとminority memoryの4-bit difference set
- cyclic gap countがobserved Q-return countを全12位置で再現

本文都合でEVTの数値・順序を変更していない。

## Interpretation boundary

本文末の112/256は自然確率・random basin volumeとして提示しない。

むしろ、cyclic schedule familyと4点配置から作られた比率であることを人物自身が認識する。

「最初の実flipがbranchを分ける」も固定192 trialについての記述であり、一般のHopfield networkの法則とは書かない。

人間の記憶・偽記憶・人格・輪廻への対応を提示しない。

## History / terminology

具体的な計算機、OS、言語、端末を本文に導入していないため、1984〜85年研究環境の未固定事項を勝手にCanon化していない。

専門語は日本語中心で、数理ラベルQ/M1/M2/M3以外の英語読解を要求しない。

## 文学面

第5話の読書上の中心は256 trialの手続きではなく、

`数字 → 距離 → first flip → 4 unstable units → circular gaps`

と説明が圧縮されていくこと。

佐伯を単なる「注意する役」にせず、結果欄・分類欄を先に作る共同研究者として配置した。

高橋も佐伯に止められる前に「距離だけではfinalを決められない」と自分で修正し、前話までの学習を保持している。

ただし人物の生活上の利害がまだ薄いというシリーズ全体の課題は残る。未成立の私生活設定をこの話へ後付けして解消しない。

## Verdict

現対象版でblockingなEVT矛盾、knowledge leakage、過剰一般化を検出しなかったため`PASS`。

これは文学的完成、独立読者の理解、Human Review、公​​開承認を意味しない。
