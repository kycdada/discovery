# オーケストレーション・サービスの構成
オーケストレーション・サービスは、Crawler に対して、クロールされたファイルの管理方法を示します。デフォルト・オプションを直接変更する場合は、`config/orchestration/orchestration-service.conf` ファイルを開いて、それぞれのユース・ケースに合わせて以下の値を変更します。

*  **http_timeout** - 文書の読み取り/インデックス付け操作に対する秒単位のタイムアウト。デフォルトは `585` です。
*  **concurrent_upload_connection_limit** - 文書のアップロードで許可される同時接続の数。デフォルトは `10` です。通常は、この数はクロール・オプションの構成時に設定した `output_limit` の値以上でなければなりません。
*  **base_url** - クロールする文書の送信先の URL。
*  **endpoint** - `base-url` でクロールする文書コレクションの場所。
*  **username** - `endpoint` の場所で認証を行うためのユーザー名。
*  **password** - `endpoint` の場所で認証を行うためのパスワード。**重要** - このパスワードは、Data Crawler 付属の vcrypt プログラムを使用して暗号化**しないでください**。
*  **config_file** - オーケストレーション・サービスで使用される構成ファイル。

オーケストレーション・サービスの出力アダプターは、IBM がそのユーザーに対する理解を深め、サービスを向上するための統計を送信できます。
`send_stats` 変数に対して以下のオプションを設定できます。
*  **jvm** - 送信される Java 仮想マシン (JVM) 統計に、Data Crawler の実行に使用する JVM から報告された Java のベンダーとバージョンが含まれます。値は、`true` または `false` のいずれかです。
*  **os** - 送信されるオペレーティング・システム (OS) 統計には、Data Crawler の実行に使用する JVM から報告された OS 名、バージョン、およびアーキテクチャーが含まれます。値は、`true` または `false` のいずれかです。

## 関連資料

crawler(1)

vcrypt(1)

crawler.conf(5)

crawler-options.conf(5)

crawler-seed.conf(5)
