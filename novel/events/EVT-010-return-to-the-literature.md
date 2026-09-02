# EVT-010 自分たちの表の外へ戻る

状態: `RESOLVED / PROVISIONAL`

Resolution provenance: `LOCKED`

Action-lock commit: `ae441628d1d8af925144f9ec8bca0336b7d0f315`

## Story time

`T0-1980S + literature check after EVT-009`

Exact date: 未確定。ただし現在のT0候補は1984〜1985年前後であり、今回採用した資料は1983年7月14日公刊なのでstory time以前に利用可能。

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

- 図書室・書架・複写機等のLOC/OBJ
- 共用計算機SYS
- 文献の物理コピーOBJ

## World before

EVT-009で、現在の6-unit toy networkについて、

`R = F \ (S ∪ -S) = ∅`

が成立した。

PER-005はmodel条件を変える前に当時利用可能な文献を確認すること、PER-006は見たい結果からmodelを逆算しないことを局所目標としている。

## Story-visible action selection

高橋は新しいnetworkを作る前に文献へ戻る。

佐伯は、後から都合のよい論文だけを拾わないため、読む資料の選択規則を先に固定させた。

---

# ACTION LOCK

commit `ae441628d1d8af925144f9ec8bca0336b7d0f315` で次を結果確認前に固定した。

1. story time以前に公刊済み
2. Hopfield 1982のcollective / content-addressable memory modelを直接継承または明示参照
3. stored pattern以外のstable / spurious memoryを明示的に問題化
4. 条件を満たす候補のうち刊行日が最も早いものを主対象
5. 同日ならHopfield自身を著者に含むものを優先し、さらに同率ならtitle辞書順
6. story time後の1985年以降の結果を人物行動の根拠にしない

停止条件は主対象一次文献が一意に決まった時点。

---

# RESOLUTION

## 1. 選択された一次文献

selection ruleにより主対象となったのは、

J. J. Hopfield, D. I. Feinstein, R. G. Palmer, “‘Unlearning’ has a stabilizing effect in collective memories,” *Nature* 304, 158–159 (1983).

DOI: `10.1038/304158a0`

公刊日: 1983-07-14。

一次出版元のabstract / bibliographic recordで、Hopfield 1982のassociative-memory modelを参照し、30〜1,000 neuronesのmathematical / computer modellingを行い、memory learningに伴ってspurious memoriesも作られevokedされ得ること、noise inputからの逆符号learningによる“unlearning”がreal memoriesへのaccessを改善しspurious onesを減らすことを確認した。

## 2. 人物がここから知ってよいこと

高橋と佐伯が今回の読解から得るのは次まで。

- 1983年時点ですでに、Hopfield型のcollective associative memoryでstored memory以外のspurious memoryが問題として明示されている
- その研究では30〜1,000 neurones規模のmathematical / computer modellingが使われている
- spurious memoryは単なる著者側の後世分類ではなく、当時の一次文献で扱われている
- “unlearning”という操作でspurious memoriesを減らす方向まで研究されている

今回この文献だけから人物Knowledgeへ入れないもの:

- 1985年Amit–Gutfreund–Sompolinskyのmixture-state / spin-glass解析
- `α_c ≈ 0.14`等の後続統計力学結果
- 現代側EXP-003〜005の結果
- 「spurious memory = 必ず特定のmixture式」という同一視

## 3. Persona interaction

高橋は、自分たちの6-unit toyで残差が空だったことと、1983年論文がより大きいnetworkでspurious memoriesを問題にしていることを並べる。

彼の結論は、

> 小さい模型で出なかったことと、現象がないことは別だ。

までに留まる。

佐伯はさらに、論文にspurious memoryと書いてあること自体を、自分たちの次のmodelでそれが必ず出る保証にはしないよう求める。

二人は「文献にある現象を再現する」ことと「自分たちの都合のよい例を作る」ことを分離する必要を共有する。

## Resolved consequence

- EVT-009の`R=∅`は現在toy固有の結果として維持される
- story time以前の一次文献に、より大きいHopfield型networkでspurious memoriesが明示的研究対象になっていることを人物が確認した
- 次のmodel変更には歴史的・科学的根拠が生じたが、具体的なN / pattern数 / pattern生成法 / update scheduleはまだ決めていない
- mixture stateの具体構造は今回まだ人物Knowledgeとして成立していない
- 紙上6-unit modelからcomputer modellingへ進む可能性が高まったが、具体的SYS/OBJはまだ成立していない

## Persona deltas

### PER-005 高橋修一

Beliefs:

- 現在toyで残差が空でも、1983年時点の一次研究ではより大きなcollective associative-memory networkにspurious memoriesが報告されている
- 次に条件を変える科学的理由はある
- ただしspurious stateの形を先に決めつけてはいけない

Goals:

- 1983論文のmodel条件を、自分たちが再現可能な最小protocolへ落とせるか確認する
- N / stored patterns / pattern生成 / update / initial-state selection / stopping ruleを結果前に固定する
- 紙上追跡では不足する場合、ORG-001の共用計算資源を利用するために必要な具体条件だけを次eventで解像する

Memory:

- Hopfield / Feinstein / Palmer 1983, DOI `10.1038/304158a0`
- 30〜1,000 neuronesのmathematical / computer modelling
- spurious memoriesがcreated / evokedされ得るという当時の問題設定
- unlearningでspurious memoriesを減らすという報告

### PER-006 佐伯玲子

Beliefs:

- 文献上spurious memoryが存在することと、次に二人が選ぶmodelでそれを観測できることは別
- 文献再現を名目に、結果が出る条件だけを後付け選択してはいけない
- 1983論文が生物学的高次機能そのものを証明したわけではない

Goals:

- 次の再現protocolでは変更変数と観測量を事前に固定する
- 文献記載、二人の再現結果、生物学的解釈を三層に分ける

Memory:

- 1983論文のspurious-memory / unlearning問題設定
- network規模が30〜1,000 neuronesと現在toyより大きいこと

## Organization / world delta

ORG-001のResources baselineに既に「論文・書籍へアクセスできる文献環境」があるため、今回の文献入手のために新しい組織設定は追加しない。

研究所のinstitutional memoryへこの読解内容が正式登録された事実は未成立。

共用計算資源はまだ使用していない。次にcomputer modellingが実行行動として成立した時点で、必要ならSYS / OBJ stateを展開する。

Fact level:

- real-world evidence: Hopfield et al. 1983の書誌・abstract内容
- local story fact: PER-005 / PER-006が当該文献を共同検討した
- institutional fact: 未成立
- public story fact: 未成立
- canon fact: 未昇格

## Who observed what

- PER-005 / PER-006: 上記文献内容と解釈境界を共有
- ORG-001: 文献アクセス環境を提供するが、組織として読解内容を承認したとは扱わない
- 他persona: 未観測
- 現代側persona: 未観測

## Research branch after resolution

新しい作者側EXPはまだ作らない。

次eventで人物が1983論文のmodelを再現する具体protocolへ進むなら、一次本文から実装条件を抽出し、story-side ACTION_LOCKの前提資料として使う。その際、1985年以降の知見を条件選択へ混入させない。

## Structure impact

EVT-009で「このtoyでは残差がない」と分かったため止まっていた問いが、当時の一次文献によって、

> 文献にあるspurious memoryを、自分たちは結果を選ばず再現できるか。

へ進んだ。

これは次eventの候補問題であり、まだ結果やchapter endingを固定しない。

## Generation validation

- EVT-009後のpersona goalから文献確認を選択した
- 文献の選択規則をcommitしてから主対象を解決した
- 主対象は1983 Hopfield / Feinstein / Palmerで固定し、結果都合で差し替えなかった
- 1985年以降のmixture-state理論を人物へ漏洩させなかった
- ORG-001の既存文献resourceで足りるため不要なLOC/OBJを追加しなかった
- computer modellingをまだ実行していないためSYS/OBJを先取りしなかった
