# BOOT-002 1980年代側の導入

状態: `PROVISIONAL`

このBootstrapは、1980年代側のworld / persona / organizationを同じstory timeへ同期する開始点です。

## Target story time

`T0-1980S`

1984〜1985年前後を中心候補とする、高橋修一（PER-005）が最初の研究行動を開始する直前。

具体年月日、都市、具体的計算機環境はまだ確定しない。

## Parent event head

`none`

## Authority inputs

- `../canon.md`
- `../environment.md`
- `../timeline.md`
- `../personas/PER-005-1980s-researcher.md`
- `../organizations/ORG-001-koryo-chemical-life-science-institute.md`
- `../../research/pre-hopfield-background.md`
- `../../research/1980s-research-environment.md`
- `../../references/`

BootstrapはCanonや現実史を上書きしない。未確認の細部は `UNRESOLVED` のまま残す。

## Opening frame / 導入原型

1980年代半ば、日本では企業による基礎研究への投資が拡大し、物理・工学・生命科学・情報処理の境界を越える研究が企業研究所でも可能になっていた。

その制度的余裕が永続することを、当時の研究者が知っているわけではない。

光陵化学生命科学研究所は、その時代に存在する架空の企業系基礎研究所である。実在した1970〜80年代日本の企業基礎研究所を史実上の制約として参照するが、特定実在研究所の別名ではない。

高橋修一が調べているのは、まだ魂でも転生でもない。

記憶を、静的な保存場所ではなく、多数の要素が相互作用してある安定状態へ移る過程として理解できるか。

そして、系が安定したことと、正しい記憶へ戻ったことを同じと呼んでよいか。

## World projection

`state/world.md` の `T0-1980S` へ次を初期化する。

- 1984〜1985年前後を中心候補とする
- Hopfield 1982を含む連想記憶・network・stable stateをめぐる研究が存在する
- 日本で企業基礎研究が拡大する制度的背景がある
- ORG-001 光陵化学生命科学研究所が存在する
- 高橋が理論検討・文献読解・簡略network計算を行える
- 神経生理・生命科学側の研究者とも接触可能
- 具体的機種、予算、都市、研究棟等は未確定
- 将来のバブル崩壊、組織再編、研究所閉鎖は現在の観測済み世界事実ではない
- 輪廻、同一認識主体、現代AIは観測されていない

## Organization discovery

### ORG-001 光陵化学生命科学研究所

独立ORGとして初期化する理由:

- 高橋・佐伯とは別のMission / Resources / Governanceを持つ
- 設備・文献・予算・発表・人員を制度として制約し得る
- 後続で再編・閉鎖・資料移管等が物語因果へ影響し得る
- 組織記録が個人記憶とは別のInstitutional memoryになる

親会社「光陵化学株式会社」は現時点では独立した意思決定をevent内で必要としないため、world entityのままにする。親会社固有の判断が必要になった時点で新しいORGを検討する。

### ORG-001 projection

`state/organizations/ORG-001.md` へ次を同期する。

- 基礎生命科学を長期視点で扱うMission
- 分野横断研究を許容する文化
- 文献、生命科学設備、共用計算資源
- 親会社資金による企業研究所としての制度的制約
- 高橋・佐伯の所属候補
- 公式記録と私的ノートを区別するInstitutional memory境界

渡さないもの:

- 将来の合併・縮小・閉鎖
- バブル崩壊後の企業研究再編
- 現代側の史料利用
- 作者側の長期プロット

## Persona discovery

### PER-005 高橋修一

`T0-1980S`でactive。

- 日本人男性、30代後半
- 数理工学・理論物理寄りの背景から神経回路・連想記憶へ越境
- ORG-001で理論検討・簡略network計算を行える

### PER-006 佐伯玲子

BOOT時点では背景上に存在し得るが、独立personaとしてのstate履歴はEVT-002で開始する。

- 日本人女性、30代半ば〜後半
- 神経生理学・biophysics寄り
- ORG-001内または近接グループで高橋と議論できる

BOOT段階で未来の会話内容を与えない。

### その他

所長、管理者、技術職員、学生等は背景上に存在し得るが、独立Knowledge / Goal / observation boundaryが因果上必要になった時点でのみ新PERを作る。

## PER-005 projection

高橋へ渡せるもの:

- 1980年代半ばまでに入手し得る記憶・連想記憶・network・動的系研究
- Hopfield 1982を研究対象として検討できること
- ORG-001で文献・数理検討・小規模計算が可能であること
- 所属研究所の公開された規則・設備・同僚の存在

渡さないもの:

- ORG-001の将来の再編・閉鎖
- 経営側の未公表方針
- 佐伯の未共有内面
- 現代AI、Transformer、checkpoint
- 自分の資料が将来利用されるという未来
- 輪廻・同一認識主体に関する作者側仮説
- 将来の実験結果・第1話の予定展開

## Initial synchronization key

`BOOT-002 @ T0-1980S @ none`

同じキーで同期する:

- `state/world.md`
- `state/organizations/ORG-001.md`
- `state/personas/PER-005.md`

PER-006の独立stateはEVT-002から開始する。

## Bootstrap validation

- [x] future plotを初期化していない
- [x] 組織と個人を同一stateへ統合していない
- [x] ORG-001を独立主体にする因果上の理由がある
- [x] 親会社を必要前にORG化していない
- [x] 組織の未来の再編・閉鎖を高橋へ漏らしていない
- [x] 高橋へ現代知識を漏らしていない
- [x] 佐伯をBOOT時点の独立行動主体として先回り生成していない
- [ ] 具体所在地・機種・職位は後続の歴史調査が必要
- [ ] 高橋が実際に読了済みの一次文献範囲は必要時に限定する
