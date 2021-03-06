# クロール・シードの構成

シードはクロールの開始点です。データ・クローラーは、そのシードで指定されているリソースからデータを取得します。通常、シードでは、プロトコル・ベースのリソース (ファイル共有、SMB 共有、データベース、各種の Web プロトコルでアクセスできるその他のデータ・リポジトリーなど) にアクセスするための URL を構成します。また、シード URL が異なれば、機能も異なります。

シードをリポジトリー固有にして、特定のサード・パーティー・アプリケーション (カスタマー・リレーションシップ・マネジメント (CRM) システム、製品ライフサイクル (PLC) システム、コンテンツ管理システム (CMS)、クラウド・ベースのアプリケーション、および Web データベース・アプリケーションなど) をクロールできるようにすることも可能です。

データ・クローラーには、以下のリポジトリー・タイプのファイル・コネクターをサポートするクロール・シードが現在用意されています。

*	ファイル・システム
*	データベース (JDBC 経由)
*	CMIS (Content Management Interoperability Services)
*	SMB (Server Message Block)、CIFS (Common Internet Filesystem)、Samba のファイル共有
*	SharePoint および SharePoint Online
*	BOX

クロール・シード構成テンプレートも用意されています。そのテンプレートを使用して、カスタム・コネクターのクロール・シードをカスタマイズできます。

## はじめに:

クローラーは、データ・リポジトリーをクロールする時に、ユーザー指定のシード URL から処理を始めて、情報のページをダウンロードしていきます。クローラーは、ダウンロードしたページに含まれているリンクも見つけて、新しくディスカバーしたページをさらにクロールするためのスケジュールを設定します。

構成情報を使用して、クロールする必要のあるページやクロールの方法が決定されます。コネクターのクロール・シード・ファイルごとに構成できるオプションをこのファイルで説明します。

**注**: 各クロール・シード構成ファイルは、対応するファイル・コネクター構成ファイルと連携して使用されます。ファイル・コネクター・オプションについては、別途説明します。

### ファイル・システム・クロール・シードの構成

以下に、ファイル・システム・クロール・シード・ファイル用に構成できる値を示します。これらの値を設定するには、`config/seeds/filesystem-seed.conf` ファイルを開き、それぞれのユース・ケースに合わせて以下の値を指定します。

*  **url** - クロールするファイルとフォルダーの改行で区切られたリスト。UNIX ユーザーは、`/usr/local/` などのパスを使用できます。
URL は、`sdk-fs://` で始まる必要があります。したがって、例えば、`/home/watson/mydocs` をクロールするには、この URL の値は `sdk-fs:///home/watson/mydocs` になります。3 番目の `/` が必要です。**注**: ファイル・システム・コネクターは、カスタム・プロトコル `sdk-fs://` を使用して有効な URL を作成します。リストされているパスの前に `file://` を付加しないでください。URL は `sdk-fs://` で始まる必要があります。
*  **hops** - 内部使用のみ。
*  **default-allow** - 内部使用のみ。

### データベース・クロール・シードの構成

以下に、データベース・クロール・シード・ファイル用に構成できる値を示します。これらの値を設定するには、`config/seeds/database-seed.conf` ファイルを開き、それぞれのユース・ケースに合わせて以下の値を指定します。

*  **url** - 取得するテーブルまたはビューの URL。カスタムの SQL データベース・シード URL を定義します。構造は、以下のとおりです。

   	`database-system://host:port/database?[per=num]&[sql=SQL]`

   シード URL をテストすると、エンキューされた URL がすべて表示されます。例えば、次のような、200 のレコードが含まれているデータベースの URL をテストします。


   	`sqlserver://test.mycompany.com:1433/WWII_Navy/?per=100&sql=select%20*%20from%20vessel&`

   以下のようなエンキューされた URL が表示されます。

   	`sqlserver://test.mycompany.com:1433/WWII_Navy/?key-val=0&`

   	`sqlserver://test.mycompany.com:1433/WWII_Navy/?key-val=100&`

   	`sqlserver://test.mycompany.com:1433/WWII_Navy/?key-val=200&`

   次の URL のテスト中に、行 43 から取得したデータが表示されます。

   	`sqlserver://test.mycompany.com:1433/WWII_Navy/?per=1&key-val=43`
*  **hops** - 内部使用のみ。
*  **default-allow** - 内部使用のみ。
*  **user-password** - データベース・システムの資格情報。ユーザー名とパスワードは `:` で区切る必要があり、パスワードは Data Crawler 付属の vcrypt プログラムで暗号化する必要があります。例えば、`username:[[vcrypt/3]]passwordstring` のようになります。
*  **max-data-size** - 文書のデータの最大サイズ。これは、一度にロードされるメモリーの最大ブロックです。コンピューター上に十分なメモリーがある場合に限り、この限度を増やしてください。
*  **filter-exact-duplicates** - 内部使用のみ。
*  **jdbc-class** (エクステンダー・オプション) - 指定すると、データベース・システムとして `(other)` が選択されている場合に、コネクターで使用される JDBC クラスがこのストリングによってオーバーライドされます。
*  **connection-string** (エクステンダー・オプション) - 指定すると、自動生成された JDBC 接続ストリングがこのストリングによってオーバーライドされます。これにより、ロード・バランシングや SSL 接続など、データベース接続に関するより詳細な構成を指定できます。例えば、`jdbc:netezza://127.0.0.1:5480/databasename` のようになります。
*  **save-frequency-for-resume** (エクステンダー・オプション) - クロールの再開や、部分的なリフレッシュを可能にするために、列または関連付けられているラベルの名前を指定します。シードでクロールが進行するときに、シードによってこの列の名前が定期的な間隔で保存され、データベースの最後の行がクロールされると、この列の名前が再度保存されます。クロールを再開したり、リフレッシュしたりする場合、クロールはこのフィールドの保存値で指定された行から処理を開始します。

### CMIS クロール・シードの構成

以下に、CMIS クロール・シード・ファイル用に構成できる値を示します。これらの値を設定するには、`config/seeds/cmis-seed.conf` ファイルを開き、それぞれのユース・ケースに合わせて以下の値を変更します。

*  **url** - クロールの開始点として使用する CMIS リポジトリーのフォルダーの URL。以下に例を示します。

   *  `cmis://alfresco.test.com:8080/alfresco/cmisatom?folderToProcess=workspace://SpacesStore/guid`
   ルート・フォルダーからクロールする場合は、以下のように URL を指定する必要があります。

   *  `cmis://alfresco.test.com:8080/alfresco/cmisatom?folderToProcess=`
*  **at** - このオプションは使用されません。
*  **default-allow** - 内部使用のみ。

### Samba クロール・シードの構成

以下に、Samba クロール・シード・ファイル用に構成できる値を示します。これらの値を設定するには、`config/seeds/samba-seed.conf` ファイルを開き、それぞれのユース・ケースに合わせて以下の値を変更します。

*  **url** - クロールする共有の改行で区切られたリスト。以下に例を示します。


   *  `smb://share.test.com/office`
   *  `smb://share.test.com/cash/money/change`
   *  `smb://share.test.com/C$/Program Files`

*  **hops** - 内部使用のみ。
*  **default-allow** - 内部使用のみ。

### SharePoint クロール・シードの構成

以下に、SharePoint クロール・シード・ファイル用に構成できる追加の値を示します。これらの値を設定するには、`config/seeds/sharepoint-seed.conf` ファイルを開き、それぞれのユース・ケースに合わせて以下の値を変更します。

*  **url** - クロールする SharePoint Web アプリケーションまたはサイト・コレクションのリスト。改行で区切ります。以下に例を示します。

   *  `io-sp://a.com`
   *  `io-sp://b.com:83/site`
   *  `io-sp://c.com/site2`

   これらのサイトのサブサイトもクロールされます (ただし、他のクロール・ルールによって除外されている場合を除きます)。
*  **filter-url** - クロールする SharePoint Web アプリケーションまたはサイト・コレクションのリスト。改行で区切ります。以下に例を示します。

   *  `http://a.com`
   *  `http://b.com:83/site`
   *  `http://c.com/site2`

*  **hops** - 内部使用のみ。
*  **n-concurrent-requests** - 内部使用のみ。
*  **delay** - 内部使用のみ。
*  **default-allow** - 内部使用のみ。
*  **seed-protocol** - サイト・コレクションの子のシード・プロトコルを設定します。
サイト・コレクションのプロトコルが SSL、HTTP、または HTTPS である場合に必要です。この値は、サイト・コレクションのプロトコルと同じものに設定する必要があります。

### Box シードの構成

以下に、Box クロール・シード・ファイル用に構成できる値を示します。これらの値を設定するには、`config/seeds/box-seed.conf` ファイルを開き、それぞれのユース・ケースに合わせて以下の値を指定します。

*  **url** - クロールの開始点として使用する URL。デフォルト値は `box://app.box.com/` です。
*  **default-allow** - 内部使用のみ。

## 関連資料

crawler(1)

vcrypt(1)

crawler.conf(5)

crawler-options.conf(5)

orchestration_service.conf(5)
