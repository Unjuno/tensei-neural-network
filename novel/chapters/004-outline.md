# 第4話 Minimum Causal Outline

状態: `DRAFT / PROVISIONAL`

対象event:

`EVT-012 -> EVT-013`

## 読書単位

第3話でstableかつstored / stored-negation外と確認した16-neurone candidate Qについて、二人が意味づけを避け、まずM1/M2/M3とのcomponentwise関係を全件記録する。その結果Qは三patternの成分多数と全16位置で一致し、さらにその静的構造がなぜHebbian connectionの下でstableになるかをoverlapから導出する。

## 最小因果骨格

1. 高橋と佐伯はQとM1/M2/M3を16位置すべて横に並べる（EVT-012）。
2. 各位置で三stored patternsが全一致か2対1かを記録し、結果後にruleを追加しない。
3. Qは16/16位置で三patternのcomponentwise majorityと一致する。
4. 12個の2対1位置ではM1/M2/M3が各4回ずつminorityになり、特定patternへ偏らない。
5. Qから三stored patternsへのHamming distanceは4/4/4、stored patterns相互は8/8/8。
6. 佐伯は「多数側に見える」という静的記述と「なぜstableか」という機構説明を分ける。
7. 二人はbipolar vectorの `x·y=N-2d_H(x,y)` を使い、Qと各stored patternのoverlapが8であることを確認する（EVT-013）。
8. Hebbian connectionとself-connection=0から、`h_i(Q)=8(M1_i+M2_i+M3_i)-3Q_i` を導く。
9. 三pattern全一致位置では `h_i=21Q_i`、2対1位置では `h_i=5Q_i` となり、EVT-011のlocal-input vectorを16/16で再現する。
10. 第4話は「多数決だから記憶になった」という意味づけではなく、少なくともこの掲載例ではstored memories同士の重なりがstored外stable stateを自己支持する仕組みまで追えた、という局所的説明で終える。

## 本文で新規に成立させてはいけないfact

- EVT-014以降の結果
- random-start accessibility / basin sizeの新しい結果
- unlearningを実行した結果
- 1985年以降のmixture-state formula / spin-glass理論
- componentwise majorityが一般のspurious memory全てに成立するという一般化
- 生物学的な多数決機構
- 新しい計算機・OS・language・設備
- ORG-001への正式報告

## Narrative focus

- 16位置の表を全文列挙せず、規則と代表位置、集計で読者が追えるようにする。
- `4/4/4` と `8/8/8` の対称性を、Qが誰か一つの記憶へ近いわけではないことの説明に使う。
- 数式は`overlap=8`と`h_i=8c_i-3Q_i`の二段階へ絞る。
- 佐伯は「多数決」という比喩を機構や生物学へ拡張させない役割を維持する。
