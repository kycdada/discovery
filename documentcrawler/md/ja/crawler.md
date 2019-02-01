crawler(1) - A 地点から B 地点にデータを移動するクローラー
====================================================================

## 概要

使用法: crawler [ crawl | testit | restart | resume | refresh | summary ][ options ]

## 説明

Data Crawler を使用して、さまざまなデータ・リポジトリー (コンテンツ管理システム、ファイル・システムなど) を
クロールし、生成した結果文書をリモート・サービスにプッシュします。

## グローバル・オプション

    --version
        プログラム・バージョンを表示します
    --help
        この使用法のテキストを表示します

## コマンド

### crawl [ options ]

現在の構成でクロールを実行します。

    -c <value> | --config <value>  # 使用する構成ファイルを指定します。デフォルトは "config/crawler.conf" です。
    --pii-checking <value>         # PII チェックを切り替えます。

### testit [ options ]

テスト・クロールを実行します (シード URL だけをクロールし、エンキューされた URL を表示します)。シード URL の
処理結果がインデックス付け可能なコンテンツ (文書など) になる場合は、そのコンテンツが出力アダプターに送信され、
画面に出力されます。シード URL の取得によって URL がエンキューされる場合、それらの URL が表示され、
コンテンツは出力アダプターに送信されません。デフォルトでは、5 つのエンキューされた URL が表示されます。

    -c <value> | --config <value>  # 使用する構成ファイルを指定します。デフォルトは "config/crawler.conf" です。
    -l <n> | --limit <n>           # エンキューされた URL の表示数を制限します。
    --pii-checking <value>         # PII チェックを切り替えます。

### restart [ options ]

クロール再始動を実行します (現在の構成で新しいクロールを開始します)。

    -c <value> | --config <value>  # 使用する構成ファイルを指定します。
    --pii-checking <value>         # PII チェックを切り替えます。

### resume [ options ]

停止地点からクロールを再開します。

    -c <value> | --config <value>  # 使用する構成ファイルを指定します。
    --pii-checking <value>         # PII チェックを切り替えます。

### refresh [ options ]

前のクロールをリフレッシュします。

    -c <value> | --config <value>  # 使用する構成ファイルを指定します。
    --pii-checking <value>         # PII チェックを切り替えます。

### summary [ options ]

クロールのレポートを生成します。

    --submitted                    # 送信された文書をすべて照会します。
    --processed                    # 正常に処理された文書だけを照会します。
    --failed                       # 正常に処理されなかった文書だけを照会します。
    --group-id <value>             # 指定のグループのクロール実行を照会します。グループには、初期クロールのほかに、初期クロールの再開、リフレッシュ、再始動が含まれます。値が未指定の場合は、デフォルトで、最後にクロールされたグループを照会します。
    --show-content                 # 照会に関連した追加のコンテンツを表示します。
    --filter                       # URL や hashID のフィルターで照会結果を絞り込みます。

## 例

`config/crawler.conf` の構成ファイルを使用してクロールを実行します。

    crawler crawl

`config/crawler.conf` の構成ファイルを使用してテストを実行します。

    crawler testit

`/home/watson/office-share.conf` の構成ファイルを使用してクロールを実行します。

    crawler crawl --config /home/watson/office-share.conf

`/home/watson/office-share.conf` の構成ファイルを使用してクロールを再始動します。

    crawler restart --config /home/watson/office-share.conf

グループ ID `2` の失敗文書の要約情報を取得します。

    crawler summary --failed --group-id 2 --show-content

使用法とバージョン情報を表示します。

    crawler --help

## 構成

`crawler` を実行するには、オプションを指定した構成ファイルが必要です。構成ファイルのサンプルが `crawler` のインストール・ディレクトリーの
`share` ディレクトリーに用意されています。それらのサンプルをコピーして変更してください。*サンプル自体は変更しないでください。*

`--config | -c` オプションを指定しないで `crawler` を実行すると、`crawler` を開始したディレクトリーの
`config` ディレクトリーにある構成が使用されます。つまり、`config/crawler.conf` に基づいて `crawler` を実行することになります。

## 診断

以下の機能を使用して問題を診断します。

### デバッグ

デバッグ・モードをアクティブにします。`crawler.conf` ファイルで以下のように設定します。

    debugging.full_node_debugging = true

### ロギング

ロギングを有効にします。`log4j_custom.properties` ファイルで以下のように設定します。

    log4j.rootLogger=INFO, Console, Log

これは、ファイル出力の場合のデフォルトのロギング・レベルです。コンソール・ログの場合のデフォルトは以下のとおりです。

    log4j.appender.Console.Threshold=WARN

ロギング・レベルを以下の値に設定できます。

    OFF - 最高ランク。ロギングをオフにする設定です。
    FATAL - アプリケーションの異常終了につながるおそれがある非常に重大なエラー・イベントを取り込みます。
    ERROR - アプリケーションの実行は続けられると考えられるエラー・イベントを取り込みます。
    WARN - 悪影響が及びそうな状態を取り込みます。
    INFO - 粗視化レベルでアプリケーションの進行状況を確認するための通知メッセージを取り込みます。
    DEBUG - アプリケーションのデバッグにとってもっとも有用な微細化レベルの通知イベントを取り込みます。
    TRACE - DEBUG よりも微細化レベルを高めて通知イベントを取り込みます。
    ALL - 最低ランク。すべてのロギングをオンにする設定です。

## スロットル

サイズ変更の制限値を定義して、スループットの管理に役立てます。`crawler.conf` ファイルで以下のように設定します。

`shutdown_timeout` では、アプリケーションをシャットダウンするまでのタイムアウト値 (分) を指定します。デフォルト値は 10 です。

    shutdown_timeout = <n>

`output_limit` は、ポータブル・クローラーが出力アダプターに同時に送信して戻りを待機する
インデックス付け可能項目の最大数です。デフォルト値は 10 です。処理に使用できるコアの数によってさらに制限される場合もあります。

    output_limit = <n>

`input_limit` コネクターから一度に要求できる URL の数を制限します。デフォルト値は 3 です。

    input_limit = <n>

`output_timeout` は、ポータブル・クローラーが出力アダプターへの要求を中止し、後続の処理のために
制限キューから項目を削除するまでの時間の長さ (秒) です。デフォルト値は 150 です。

    output_timeout = <n>

出力アダプターによる制約を考慮してください。その制約は、ここで定義する制限値に関係する場合が
あるからです。前述の定義された `output_limit` は、出力アダプターに一度に送信できるインデックス付け可能なオブジェクト数にのみ関係があります。インデックス付け可能なオブジェクトが出力アダプターに送信されると、`output_timeout` 変数で定義されている「クロックによるカウント」が開始されます。
出力アダプター自体にスロットルがあり、受け取った数と同数の入力が処理されないようになっている場合があります。例えば、オーケストレーション出力アダプターには、サービスへの HTTP 接続用に構成できる接続プールがある場合があります。例えば、デフォルト値が 8 の場合に
`output_limit` をその接続プールでの構成値より大きい数値に設定すると、実行の順番を待っている状態でクロックによるカウントが
開始されるプロセスが出てきます。その後、タイムアウトになる場合があります。

`num_threads` は、一度に実行できる並行スレッドの数です。この値は、整数 (並行スレッドの数を直接指定)、またはストリング (`"xNUM"` というフォーマットで、使用可能なプロセッサー数の倍数を指定) のいずれかになります。デフォルト値は "x1.5" です。つまり、`Runtime.availableProcessors` で取得する使用可能なプロセッサー数の 1.5 倍です。

    num_threads = <n>

Data Crawler プール内の並列処理を計算するための数式は、`min(maxThreads, max(minThreads, numThreads))` です。

## `CRAWLER_OPTS` 環境変数 

`CRAWLER_OPTS` 環境変数によって `crawler` に渡すことができるプロパティーとそれぞれのデフォルト値を以下にまとめます。

以下のようにして渡します。

    CRAWLER_OPTS="-Dproperty=value -Dproperty=value" crawler

この値を変更するのは、IBM サポートの指示のもとでデバッグを行う場合に限ってください。

### cfa.java_bin

`cfa.java_bin` によって、コネクター・フレームワークの入力アダプターを開始するために使用する `java` コマンドを変更できます。デフォルトで `crawler` は、
`crawler` 自体の起動に使用されたのと同じ `java` バイナリーを使用します。

その変更を `java.home` プロパティーの設定によって行うこともできます。その設定を使用して `java` 実行可能プログラムのパスが計算されます。

### cfa.lib_dir

`cfa.lib_dir` によって、コネクター・フレームワークの `lib` ディレクトリーのパスを変更できます。この変更が必要になるケースはほとんどありません。デフォルトの場合、
`crawler` は、計算されたコネクター・フレームワークのパス (通常は単に `connectorFramework`) にある `lib` ディレクトリーを使用します。

### cfa.framework_jars_dir

`cfa.framework_jars_dir` によって、コネクター・フレームワークの jar ディレクトリー (デフォルトでは `connectorFramework/<version>/lib/java` 内) のパスを変更できます。

### cfa.plugins_dir

`cfa.plugins_dir` によって、コネクター・フレームワークのプラグイン・ディレクトリー (実際のコネクターの保管場所) のパスを指定できます。
デフォルトでは、`framework_jars_dir` からビルドされ、`connectorFramework/<version>/lib/java/plugins` になります。

## 既知の制限事項

Data Crawler の現行リリースの既知の制限事項を詳しく取り上げます。

* 無効または欠落した URL を使用してファイル・システム・コネクターを実行した場合、Data Crawler がハングすることがあります。
* `config/crawler.conf` ファイルの `urls_to_filter` 値の構成で、すべてのホワイトリスト URL または RegEx を 1 つの RegEx 式に含めてください。
* `--config | -c` オプション内に渡される構成ファイルへのパスは、修飾されたパスでなければなりません。
つまり、これは相対形式 (`config/crawler.conf` や `./crawler.conf`)、または絶対パス (`/path/to/config/crawler.conf`) でなければなりません。単に `crawler.conf` を指定できるのは、`crawler.conf` ファイルで `include` を使用して参照するファイルを `include` で指定する代わりにインラインで書き込む場合に限られます。例えば、構成ファイルを読みやすくするために、`discovery/discovery_service.conf` を `include` で参照するとします。config オプションで非修飾パスを使用するには、参照先のファイルの内容を `crawler.conf` の `output_adapter.discovery_service` キーにコピーする必要があります。

## 変更ログ

このリリースの変更点のリストについては、インストール・ディレクトリーにある `changelog.txt` ファイルを参照してください。

## 作成者

IBM Watson - https://www.ibm.com/smarterplanet/us/en/ibmwatson/

ピッツバーグの yinz が作成しました。

## 関連資料

vcrypt(1)

crawler.conf(5)

crawler-options.conf(5)

crawler-seed.conf(5)

orchestration_service.conf(5)
