# 内容
医者にかかる際に使うことを想定した簡易的な予約システムをつくってみる
（余裕があれば改良を重ねて、他の用途で使える様にしてみたい）

参考文献：[【Python】オブジェクト指向の練習問題【診療支援アプリ作成】](https://obgynai.com/object-orientation-exercises/)

<br>

# Classの構成
- Human Class(親クラス)
  - Patient Class(子クラス)

<br>

- Clinic Class（上記2クラスとは別で定義）

<br>

# 実現したい機能（仕様）
[HumanClass(Object)]
- 人がもつ基本情報で今回のシステムに必要なものを定義（名前、年齢、性別etc）

[PatientClass(Human)]
- Human Classを継承し、診察券のIDや症状を伝える機能を持たせる

[ClinicClass(Object)]
- 患者のリストを管理し、各患者の予約や診察を取り扱えるようにする
- また、待ち時間や、待っている人の人数の増減を表示する機能もつける

<br>

# 具体化
[HumanClass]
## attribute

|変数名|想定している型|内容|
|--:|--:|--:|
|name|str|名前|
|age|int|年齢|
|gender|str|性別|

<br>

[PatientClass(Human)]
## attribute

|変数名|想定している型|内容|
|--:|--:|--:|
|symptoms|list|症状の内容（熱、気分、いつからetc）|
|patient_id|int|診察券ID|
|desired_date|str|予約希望日時|

<br>

[ClinicClass(Object)]
## attribute

|変数名|想定している型|内容|
|--:|--:|--:|
|patient_list|list|患者一覧（予約、当日含む）|
|clinic_name|str|病院名|

<br>

## メソッド
|メソッド名|処理内容|引数|戻り値|種類|
|--:|--:|--:|--:|--:|
|show_waiting_count()|現在の診察待ち人数を表示する|-|-|instance|
|reserve()|患者の予約処理を行う（予約、取り消し、変更、確認）|patient_id|-|instance|
|diagnosis()|患者の診察処理、いったん予約のみで考える|patient_id|-|instance|
|_check_reserved()|予約状況の確認を結果を表示する|patient_id|-|static|

