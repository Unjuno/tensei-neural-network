# 物語イベント

このディレクトリは、ペルソナ状態と世界状態を**同じ時系列上で結び付けるイベント**を管理します。

ペルソナと世界は別の状態領域です。イベントはそれらを混ぜるのではなく、同じ出来事が各領域へどのような差分を与えたかを追跡するための結合点です。

## イベントID

物語上の重要イベントには安定ID `EVT-001`, `EVT-002`, ... を使います。

IDは発生順または採番順の識別子であり、必ずしも小説の章順とは一致しません。

## 最低限の記録

```text
# EVT-xxx <短い名前>

Story time:
Timeline position:
Participants:
World before:
Observations available to each participant:
Actions:
Resolved consequence:
World delta:
Persona deltas:
Who observed what:
Canon candidate:
Structure impact:
```

## 原則

- `Story time` は物語世界の時刻。読者へ見せる順番ではない
- event前後の状態を因果的につなぐ
- 世界の客観変化と、人物がどう理解したかを分ける
- 一人が観測した事実を、他の全ペルソナへ自動共有しない
- 世界が人物の行動なしに変化した場合も、時間経過・外部出来事としてevent化できる
- 同時に複数の出来事が起きる場合、必要なら同一時刻に複数eventを置き、因果順が必要なものだけ順序を明示する
- 歴史場面と現代場面が小説上交互に描かれても、Story time上の位置は混同しない

## 状態更新

イベント `EVT-k` により、概念的には次のように更新します。

```text
W(t+1)   = ResolveWorld(W(t), EVT-k)
P_i(t+1) = UpdatePersona(P_i(t), Observed_i(EVT-k))
```

同じeventでも、ペルソナごとに `Observed_i(EVT-k)` は異なります。

したがって、世界状態が変化していても人物がそれを知らないこと、同じ出来事から複数人物が異なる信念へ更新されることを許容します。

## 保存粒度

すべての会話や動作をeventファイルへ分解しません。

後続の因果関係、人物状態、世界状態、起承転結上の遷移を説明するために必要な出来事だけを安定イベントとして残します。
