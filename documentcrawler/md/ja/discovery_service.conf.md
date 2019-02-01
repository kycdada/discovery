# ディスカバリー・サービスの構成
ディスカバリー・サービスでは、IBM Watson ディスカバリー・サービスを使用する場合にクロール済みのファイルをどう管理するかをクローラーに対して指定します。デフォルト・オプションを直接変更する場合は、`config/discovery/discovery_service.conf` ファイルを開いて、それぞれのユース・ケースに合わせて以下の値を変更します。

*  **http_timeout** - 文書の読み取り/インデックス付け操作のタイムアウト (秒単位)。デフォルトは `125` です。
*  **concurrent_upload_connection_limit** - 文書のアップロード時に可能な同時接続の数。デフォルトは `2` です。オーケストレーション・サービス出力アダプターを使用する場合は、クロール・オプションの構成時に設定した `output_limit` の値以上の数でなければなりません。
*  **base_url** - クロールする文書の送信先の URL。現行リリースのディスカバリー・サービスの場合は、`https://gateway.watsonplatform.net/discovery/api` という値になります。
*  **environment_id** - `base-url` でクロールする文書コレクションの場所。
*  **collection_id** - ディスカバリー・サービスでセットアップした文書コレクションの名前。
*  **configuration_id** - ディスカバリー・サービスで使用する構成ファイルのファイル名。
*  **check_for_completion** - 文書がエンドポイントで正常に処理されたかどうかを検査します。この検査によって、クローラーのパフォーマンスは落ちるとしても、文書のアップロードや変換が成功したという信頼性の高い通知を生成できます。値は、`true` または `false` のいずれかです。  
**重要** - このパラメーターを有効にする場合は、利用できるリソースをフルに活用するために、`concurrent_upload_connection_limit` の値を大きくして、クロール・オプションの構成時に設定した `output_limit` の値以上にしてください。

ディスカバリー・サービスの資格情報を指定します。
*  **username** - クロールする文書コレクションの場所で認証を行うためのユーザー名。
*  **password** - クロールする文書コレクションの場所で認証を行うためのパスワード。

ディスカバリー・サービス出力アダプターは、IBM がユーザーに対する理解を深めてサービスを向上させるための統計を送信できます。`send_stats` 変数に対して以下のオプションを設定できます。
*  **jvm** - 送信される Java 仮想マシン (JVM) 統計に、Data Crawler の実行に使用する JVM から報告された Java のベンダーとバージョンが含まれます。値は、`true` または `false` のいずれかです。
*  **os** - 送信されるオペレーティング・システム (OS) 統計には、Data Crawler の実行に使用する JVM から報告された OS 名、バージョン、およびアーキテクチャーが含まれます。値は、`true` または `false` のいずれかです。

*  **api_version** - 内部使用のみ。API バージョンの最終変更日。

# URL トラッキング・ストレージの構成
`config/discovery` フォルダーには、クローラー URL と文書 ID の内部マッピングのために使用できる構成ファイルも入っています。デフォルト・オプションを直接変更する場合は、`config/discovery/uri_tracking_storage.conf` ファイルを開いて、それぞれのユース・ケースに合わせて以下の値を変更します。

*  **driver** - データベースの JDBC H2 ドライバー・クラス。デフォルト値は `org.h2.Driver` です。
*  **url** - これは JDBC 接続ストリングの URL 接頭部です。形式は `jdbc:h2:[file:]` です。**注**: 接頭部 `file:` はオプションです。`database_location` で相対パスのみを使用する場合や値を何も指定しない場合は、現行作業ディレクトリーが開始点として使用されます。デフォルトは `jdbc:h2:file:` です。
*  **database_location** - データベースを保管するディスク上の場所 (`./storage/database` や `~/storage/database` など)。デフォルト値は `./storage/database` です。
*  **database_name** - データベースの名前。デフォルト値は `ActivityDB` です。
*  **table_name** - 使用するテーブルの名前。デフォルト値は `UriTracker` です。
*  **username** - データベースに接続するユーザー名。
*  **password** - データベースに接続するパスワード。

## 関連資料

crawler(1)

vcrypt(1)

crawler.conf(5)

crawler-options.conf(5)

crawler-seed.conf(5)
