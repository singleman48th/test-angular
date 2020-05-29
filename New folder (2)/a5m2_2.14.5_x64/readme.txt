-------------------------------------------------------------------
【ソフト名】 A5:SQL Mk-2 Version 2.14.4
【制作者名】 松原正和
【動作環境】 Windows XP
             Windows Vista
             Windows 7
             Windows 8
             Windows 8.1
             Windows 10
             Windows Server 2003
             Windows Server 2008
             Windows Server 2012 (GUI 使用サーバー)

             ※ x86版は 64bit OLE DB, ODBCには接続出来ません。
             ※ x64版は 32bit OSでは動作しません。
             ※ x64版は 32bit OLE DB, ODBCには接続出来ません。
【  種別  】 ビジネス/データベース関連ソフトウェア
【 連絡先 】 下記URLにアクセスしてトップページに記載されるメール
              アドレスにメールを送信してください。
【 ＵＲＬ 】 https://a5m2.mmatsubara.com/
【ファイル】x86版 : a5m2_2.14.4_x86.zip
            x64版 : a5m2_2.14.4_x64.zip
            x86版(読み取り専用版) : a5m2_2.14.4_x86_r.zip
            x64版(読み取り専用版) : a5m2_2.14.4_x64_r.zip
            Microsoft Store x64版：A5M2.x64.appx 
-------------------------------------------------------------------

■概要
    A5:SQL Mk-2は複雑化するデータベース開発を支援するために開発されたフリー
  のSQL開発環境&ER図開発ツールです。
    高機能かつ軽量で、使い方が分かりやすいことを目標に開発されています。
    SQLを実行したり、テーブルを編集するほかに、SQLの実行計画を取得したり、ER
  図を作成したりするなど多彩な機能を持ちます。


■ファイル
  アーカイブファイルには以下のファイルが含まれます。
  ・A5M2.exe                          A5:SQL Mk-2 実行ファイル
  ・A5M2.ENU                          英語(アメリカ)言語リソース
  ・A5M2.ENG                          英語(イギリス)言語リソース
  ・history.txt                       変更履歴
  ・license.txt                       ライセンス定義ファイル
  ・license_en.txt                    ライセンス定義ファイル
  ・readme.txt                        このファイル
  ・readme_en.txt                     英語版 readme
  ・sampledb\*                        サンプルデータベース(Microsoft Access, ER図)
  ・sample\*                          各種サンプル（スクリプト類）
  ・scripts\*                         スクリプトファイル
  ・VirusCheck.txt                    アンチウイルスソフトにおける各ファイルのチェック結果ファイル


■OS、配布ファイル以外に必要なソフト
    なし


■インストール
【ZIPファイル版】
    インストール作業は必要ありません。
    ZIPファイルを展開し、A5M2.exeを起動することで使用できます。
    ポータブルモード(後述)で利用する場合は、事前にA5M2.exeと同じフォルダに 
    "Portable" フォルダを作成してから実行してください。

【Microsoft Store版】
    Microsoft Storeからインストールします。

■アップグレード
【ZIPファイル版】
    インストールと同様にZIPファイルを展開し、A5M2.exeを起動することで使用で
  きます。
    ZIPファイルの展開は古いバージョンとは別のフォルダに展開してください。

【Microsoft Store版】
    Microsoft Storeからアップグレードします。


■アンインストール
【ZIPファイル x86版 または x86版(読み取り専用版)】
    ZIPファイルを展開したフォルダを削除します。
    レジストリエディタから\\HKEY_CURRENT_USER\Software\mmatsubara\a5m2(x86)
  を削除してください。
    %APPDATA%\a5m2(x86) で表されるディレクトリ(%APPDATA%は環境変数)を削除し
  てください
    （ディレクトリ・レジストリの削除は必須ではありません）
　その後、A5M2.exeのあるフォルダを削除します。

【ZIPファイル x64版 または x64版(読み取り専用版)】
    ZIPファイルを展開したフォルダを削除します。
    レジストリエディタから\\HKEY_CURRENT_USER\Software\mmatsubara\a5m2(x64)
  を削除してください。
    %APPDATA%\a5m2(x64) で表されるディレクトリ(%APPDATA%は環境変数)を削除し
  てください
    （ディレクトリ・レジストリの削除は必須ではありません）
  その後、A5M2.exeのあるフォルダを削除します。

【ポータブルモードで利用している場合】
  A5M2.exeのあるフォルダを削除します。

  ※ポータブルモードでなく、一度でも通常モードで起動したことがある場合は、
    【x86版・x86版(読み取り専用版)】または、【x64版・x64版(読み取り専用版)】
     に従ってアンインストール作業を行ってください。

【Microsoft Store版】
    スタートメニューでA5:SQL Mk-2のアイコンを右クリックし、「アンインストール」
  を選択します。


■使用方法
    初回起動時にデータベース登録画面が表示されます。そこから利用する
  データベースを登録します。
    それが終わったら、左側のツリーより各データベースへ接続し、テーブル・
  ビュー・シノニム及びストアドプロシージャへアクセスできます。
    SQL(S) のメニューより新規作成を選ぶことでSQL文がテストできるように
  なります。このウインドウではselect文、やその他のDML文(Insert, Update, 
  Delete)が実行できます。接続先のRDBMSが提供する構文でDDL文も実行可能です。
  
  以下に大まかな機能一覧を示します。
  ・様々なDBへの接続
    （Oracle, PostgreSQL, MySQL, SQLiteへは直接接続できます）
  ・SQL入力補完機能（共通表式やサブクエリも解析）
  ・SQLをGUIで作成・編集する機能
  ・実行計画取得機能
  ・SQL整形機能
  ・";"(セミコロン)または行頭の"/"(スラッシュ)や"GO"で区切ったSQLの連続実行
  ・複数の結果セットをまとめて Excel へ出力
  ・SQLを２回実行して差を Excel へ出力（複数結果セットの比較も可能）
  ・パラメータを使ったSQLの実行
  ・テーブルやクエリー結果セットのフィルタリング（絞込み）
  ・クエリーのコメント中にカラム名や結果セットのタイトルなどを指定する擬似命  
    令を埋め込む機能
  ・Excelと連携可能なテーブルエディタ
  ・テーブルのプロパティ（RDBMSごとの追加情報）を表示
  ・テーブルのソースを表示
  ・テーブル内容のエクスポート・インポート
  ・テーブルに大量のテスト用ダミーデータをインサートする機能
  ・ER図を作成する機能
  ・データベースからER図を作成する機能
  ・ER図からデータベースのDDLを作成する機能
  ・スクリプト言語機能

  詳しくは以下のサイトを参照してください。
  http://a5m2.mmatsubara.com/


■ポータブルモード
  通常、A5:SQL Mk-2はレジストリ及び、%APPDATA%\a5m2(x86)（または %APPDATA%\a5m2(x64)）
配下に設定や一時ファイルを保存しますが、あらかじめ、A5M2.exeと同じフォルダに 
"Portable" フォルダを作成しておくことで全ての設定および一時ファイル・SQLログ
ファイルを "Portable" フォルダに配置するようになる「ポータブルモード」で動作
させることができます。
　これにより、USBメモリなどに配置してA5:SQL Mk-2を持ち運び、各PCで設定を共有
することができるようになります。

　ポータブルモードは以下の特徴を備えます。

　・レジストリに書き込みを行わない
　・"Portable" フォルダ以外に一時ファイルを作成しない
　・設定や一時ファイル・SQLログファイルはすべてAES(256bit)で暗号化される
　・起動パスワードを設定することができる
　・ファイルの関連付けは行えない

　ポータブルモードは上述の通り、設定や一時ファイル・SQLログファイルをすべて
AES(キー長:256bit)で暗号化します。このため、起動パスワードを設定すれば、万一
A5:SQL Mk-2 の入ったUSBメモリ等を紛失しても、DBの設定情報や一時保存されたSQL・
ER図・スクリプト、SQLの実行を記録したログファイルが流出する可能性を最小限に
することができます。

　もちろん、USBメモリ等に入れなくとも、レジストリに書き込みを行わない目的で
ポータブルモードを利用することもできます。

　Microsoft Store版はポータブルモードで利用できません。

■利用しているプログラム部品について
    A5:SQL Mk-2では以下のプログラム部品（コンポーネント・ライブラリ）を利用
  させていただいております。作者の皆様に心より感謝いたします。

  ・ActiveQueryBuilder Ver 1.17
      Active Database Software
      Commercial License
  ・DCPcrypt 2016/10/26(r13)版
      Copyright © 1999-2002 David Barton
      MIT License
        http://a5m2.mmatsubara.com/open_source_license/DCPcrypt/MIT_license.txt
        https://opensource.org/licenses/mit-license.php
  ・DMonkey Version: 0.3.9
      Project DMonkey
      独自ライセンス
  ・GDI+ API, GDI+ Class, GDI+ Util
      http://www.progdigy.com
      Mozilla Public License Version 1.1
      ソースのヘッダ（Licenseに関する記述）: http://a5m2.mmatsubara.com/open_source_license/progdigy.com/source_header.txt
      ソース : http://a5m2.mmatsubara.com/open_source_license/progdigy.com/gdiplus.zip
  ・NkPrinter(0.53)
      T.Nakamura
  ・SecureBridge Ver 9.0.2
      Devart
      Commercial License
  ・Syntax Editor SDK v 2.6.0
      EControl
      Commercial License
  ・TCtrlGridコンポーネント  Ver 2.10
      ＳＵＮ
  ・UniDAC Ver 7.3.9
      Devart
      Commercial License
  ・フォント名コンボボックス(＆リストボックス) Version 1.2.1
      CQN11335 加藤太朗
  ・MongoDB C クライアントライブラリ(DLL)
      https://github.com/mongodb/mongo-c-driver
      Apache License : https://www.apache.org/licenses/LICENSE-2.0
