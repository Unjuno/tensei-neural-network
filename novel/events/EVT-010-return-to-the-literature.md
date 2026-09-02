# EVT-010 自分たちの表の外へ戻る

状態: `ACTION_LOCKED / PROVISIONAL`

## Story time

`T0-1980S + literature check after EVT-009`

Exact date: 未確定。ただし現在のT0候補は1984〜1985年前後であり、今回の選択規則ではstory time以前に刊行済みの資料だけを許可する。

## Timeline position

- Parent: `EVT-009`
- Previous event: `EVT-009`
- Next event: 未成立

## Resolution scope

- PER-005 高橋修一
- PER-006 佐伯玲子
- ORG-001の既定resourceである論文・書籍へのアクセス環境
- EVT-009後に成立した「現在toyでは別種stable finalを観測できない」という共有knowledge
- story time以前に公刊された連想記憶networkの一次文献

今回まだ独立entity化しないもの:

- 図書室・書架・複写機等のLOC/OBJ: 具体的な物理的来歴が結果を左右しない
- 共用計算機SYS: 文献確認だけなら不要
- 文献の物理コピーOBJ: 所有・貸出・保存状態が後続因果へ効くまではreferenceとして扱う

## World before

EVT-009で、現在の6-unit toy networkについて、

`R = F \ (S ∪ -S) = ∅`

が成立した。

PER-005は次にmodel条件を変える前に、当時利用可能な理論・文献でspurious / mixture structureの扱いを確認することを目標としている。

PER-006は、新しいmodelを「見たい結果」から逆算して選ばず、問い・変更変数・停止条件・観測量を先に明示することを要求している。

## Story-visible action selection

高橋は新しいnetworkを作る前に文献へ戻る。

佐伯は、後から都合のよい論文だけを拾わないため、今回読む資料の選択規則を先に決めるよう求める。

## ACTION LOCK

今回の文献選択規則を次で固定する。

1. story time以前に公刊済みであること
2. Hopfield 1982のcollective / content-addressable memory modelを直接継承または明示参照する一次文献であること
3. stored pattern以外のstable / spurious memoryを本文またはabstractで明示的に問題化していること
4. 上記を満たす候補のうち、**刊行日が最も早いもの**を今回の主対象にする
5. 同日候補が複数ならbibliographic record上でHopfield自身を著者に含むものを優先し、それでも複数ならtitleの辞書順で一件に固定する
6. story time後の1985年以降の結果を、今回の人物行動の根拠として使用しない

現在repoで既に作者側調査として把握している候補一覧を結果に合わせて増減せず、必要なら一次文献の書誌と本文/abstractを外部一次情報で再確認する。

## Resolver may use

- `research/pre-hopfield-background.md` に既に記録された1982〜1985年の文献候補
- 各候補の一次出版元・DOI・公刊日
- story time以前かどうか
- 上記selection ruleへの適合性

## Resolver must not use for action selection

- 現代側EXP-003〜005の結果
- 1985年以降のAmit–Gutfreund–Sompolinsky等の結果
- 第3話で望ましい展開
- 将来の現代AI plot
- 「mixture stateを出したい」等、望むoutcomeからの逆算

## Stopping rule

selection ruleで主対象一次文献が一意に決まった時点で選択を停止する。

その文献から人物が取得できるknowledgeは、story time時点で公刊済みの記載内容に限定して解決する。

## Resolution provenance target

`LOCKED`

このcommit以後、主対象文献を結果都合で差し替えない。
