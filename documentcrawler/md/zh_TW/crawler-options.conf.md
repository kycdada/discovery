# 配置搜索選項
資料搜索器所收集的原始資料，最終會用於形成「IBM Watson 擷取和分級」服務的搜尋結果。

資料搜索器目前提供連接器來支援來自下列儲存庫的資料集合：

*	檔案系統
*	資料庫，透過 JDBC
*	CMIS（內容管理交互作業能力服務）
*	SMB（伺服器訊息區塊）、CIFS（一般網際網路檔案系統）或 Samba 檔案共用
*	SharePoint 與 SharePoint Online
*	Box

也會提供連接器配置範本，可讓您自訂連接器。

## 開始使用：
搜索資料儲存庫時，搜索器會在使用者指定的起始種子 URL 開始，並開始下載資訊的頁面。搜索器也會尋找所下載頁面中的鏈結，並將新探索到的頁面排定進行進一步搜索。

配置資訊可用來判斷需要搜索哪些頁面，以及如何搜索它們。這個檔案說明您可以對每一個連接器配置的選項。

**附註**：每一個連接器也會有對應的種子配置檔；種子配置選項將個別說明。

### 配置檔案系統連接器
「檔案系統」連接器可讓您搜索資料搜索器安裝的本端檔案。下列是使用「檔案系統」連接器所需的基本配置選項。若要設定這些值，請開啟檔案 `config/connectors/filesystem.conf`，並修改您的使用案例特定的下列值：

*  **protocol** - 用於搜索的連接器通訊協定的名稱。對此連接器使用 `sdk-fs`。
*  **collection** - 此屬性是用來解壓縮暫存檔。
*  **logging-config** - 指定用於配置記載選項的檔案；必須以 `log4j` XML 字串的形式將它格式化。
*  **classname** - 連接器的 Java 類別名稱。用來使用此連接器的值必須是 `plugin:filesystem.plugin@filesystem`。

### 配置資料庫連接器
資料庫連接器可讓您藉由執行自訂的 SQL 指令，並每一列（記錄）建立一個文件與每一直欄（欄位）建立一個內容元素來搜索資料庫。您可以指定要作為唯一金鑰的直欄，以及包含代表每一筆記錄前次修改日期的時間戳記直欄。連接器會從指定的資料庫擷取所有記錄，也可以在 SQL 陳述式中限制於特定的表格、結合等等。

「資料庫」連接器可讓您搜索下列資料庫：

*  IBM DB2
*  MySQL
*  Oracle
*  PostgreSQL
*  Microsoft SQL Server
*  Sybase
*  透過 JDBC 3.0 相容驅動程式的其他 SQL 相容資料庫

連接器會從指定的資料庫和表格擷取所有記錄。

**JDBC 驅動程式**
「資料庫」連接器隨附於 Oracle JDBC（Java 資料庫連線功能）驅動程式 1.5 版。隨附於資料搜索器的所有協力廠商 JDBC 驅動程式位於資料搜索器安裝的 `/lib/java/database` 目錄中，必要時您可以在其中新增、移除及修改它們。您也可以使用 `crawler.conf` 檔案中的 `extra_jars_dir` 設定來指定其他位置。

***DB2 JDBC 驅動程式***
由於授權問題，資料搜索器並未隨附 DB2 的 JDBC 驅動程式。不過，為了能夠搜索 DB2 安裝，已安裝 JDBC 支援的所有 DB2 安裝中包括搜索器需要資料的 JAR 檔。若要搜索 DB2 實例，您必須將這些檔案複製到資料搜索器安裝的適當目錄中，使得「資料庫」連接器能夠使用它們。

若要讓資料搜索器搜索 DB2 安裝，請找到 DB2 安裝中的 JAR 檔 `db2jcc.jar` 和授權（通常是 `db2jcc_license_cu.jar`），並將這些檔案複製到資料搜索器安裝目錄的 `lib/java` 子目錄中，或您可以使用 `crawler.conf` 檔案中的 `extra_jars_dir` 設定來指定其他位置。

***MySQL JDBC Drivers***
資料搜索器不會隨附 MySQL 適用的 JDBC 驅動程式，因為如果產品隨附 JDBC 驅動程式，則可能會發生授權問題。但是，下載包含 MySQL JDBC 驅動程式的 JAR 檔，並將該 JAR 檔整合到您的資料搜索器安裝很容易：

1.	使用 Web 瀏覽器來造訪 MySQL 下載網站，並找出您要使用的保存格式的原始檔及二進位下載鏈結（Microsoft Windows 系統通常是 zip，或 Linux 系統則是 gzip Tarball）。按一下該鏈結來起始下載程序。可能需要登錄。

2.	根據和您下載的保存檔的類型和名稱，使用適當的 `unzip archive-file-name` 或 `tar zxf archive-file-name` 指令來解壓縮該保存的內容。

3.	變更至從保存檔解壓縮的目錄，然後將 JAR 檔從此目錄複製到資料搜索器安裝目錄的 `lib/java` 子目錄中，也可以使用 `crawler.conf` 檔案中的 `extra_jars_dir` 設定來指定其他位置。

下列是使用「資料庫」連接器所需的基本配置選項。若要設定這些值，請開啟檔案 `config/connectors/database.conf`，並修改您的使用案例特定的下列值：

*  **protocol** - 用於搜索的連接器通訊協定的名稱。此連接器的值是根據要存取的資料庫系統。
*  **collection** - 此屬性是用來解壓縮暫存檔。
*  **classname** - 連接器的 Java 類別名稱。用來使用此連接器的值必須是 `plugin:database.plugin@database`。
*  **logging-config** - 指定用於配置記載選項的檔案；必須以 `log4j` XML 字串的形式將它格式化。

### 配置 CMIS 連接器
CMIS（內容管理交互作業能力服務）連接器可讓您搜索啟用 CMIS 的 CMS（內容管理系統）儲存庫，例如 Alfresco、Documentum 或 IBM Content Manager，並將它們包含的資料建立索引。

下列是使用 CMIS 連接器所需的基本配置選項。若要設定這些值，請開啟檔案 `config/connectors/cmis.conf`，並修改您的使用案例特定的下列值：

*  **protocol** - 用於搜索的連接器通訊協定的名稱。對此連接器使用 `cmis`。
*  **collection** - 此屬性是用來解壓縮暫存檔。
*  **dns** - 未使用的選項。
*  **classname** - 連接器的 Java 類別名稱。用來使用此連接器的值必須是 `plugin:cmis-v1.1.plugin@connector`。
*  **logging-config** - 指定用於配置記載選項的檔案；必須以 `log4j` XML 字串的形式將它格式化。
*  **endpoint** - CMIS 相容儲存庫的服務端點 URL。例如，SharePoint 的 URL 結構是：
   *  若為 AtomPub 連結：   
      http://<server>:<port>/_vti_bin/cmis/rest?getRepositories
   *  若為 WebServices 連結：   
      http://<server>:<port>/_vti_bin/cmissoapwsdl.aspx

*  **username** - 用來存取內容的 CMIS 儲存庫使用者的使用者名稱。此使用者必須可存取要搜索及建立索引的所有目標資料夾和文件。
*  **password** - 用來存取內容的 CMIS 儲存庫的密碼。密碼「不能」加密；必須以純文字提供。
*  **repositoryid** - 用來存取該特定儲存庫內容的 CMIS 儲存庫的 ID。
*  **bindingtype** - 識別要用於連接 CMIS 儲存庫的連結類型。值為 `AtomPub` 或 `WebServices`。
*  **authentication** - 識別在聯絡 CMIS 相容儲存庫時要使用的鑑別機制的類型：`Basic HTTP Authentication`、`NTLM` 或 `WS-Security(Username token)`。
*  **enable-acl** - 啟用擷取已搜索資料的 ACL。如果您對於這個集合中文件的安全沒有疑慮，則停用此選項將會增加效能，因為不會向文件要求此資訊，且不會擷取和編碼此資訊。值為 `true` 或 `false`。
*  **user-agent** - 搜索文件時傳送至伺服器的標頭。
*  **method** - 將藉以傳遞參數的方法（`GET` 或 `POST`）。
*  **url-logging** - 記載搜索的 URL 到何種程度。可能的值是：

   *  ***full-logging*** - 記載 URL 的所有相關資訊。
   *  ***refined-logging*** - 僅記載瀏覽搜索器日誌以及讓連接器正確運作所需的資訊；這是預設值。
   *  ***minimal-logging*** - 僅記載讓連接器正確運作所需的資訊量下限。

   將此選項設定為 minimal-logging 將減少日誌的大小，且由於與減少要記載的資料量相關聯的 I/O 較小，將稍微增加效能。
*  **ssl-version** - 指定要用於 HTTPS 連線的 SSL 版本。預設會使用最強大的通訊協定。

### 配置 SMB/CIFS/Samba 連接器
Samba 連接器可讓您搜索「伺服器訊息區塊 (SMB)」及「一般網際網路檔案系統 (CIFS)」檔案共用。此類型的檔案共用在 Windows 網路上很常見，並且也可以透過開放程式碼專案 [Samba](https://www.samba.org/) 提供。

下列是使用 Samba 連接器所需的基本配置選項。若要設定這些值，請開啟檔案 `config/connectors/samba.conf`，並修改您的使用案例特定的下列值：

*  **protocol** - 用於搜索的連接器通訊協定的名稱。用來使用此連接器的值是 `smb`。
*  **collection** - 此屬性是用來解壓縮暫存檔。
*  **classname** - 連接器的 Java 類別名稱。用來使用此連接器的值必須是 `plugin:smb.plugin@connector`。
*  **logging-config** - 指定用於配置記載選項的檔案；必須以 `log4j` XML 字串的形式將它格式化。
*  **username** - 用來進行鑑別的 Samba 使用者名稱。如果提供，也必須提供網域和密碼。如果未提供，則會使用來賓帳戶。
*  **password** - 用來進行鑑別的 Samba 密碼。如果提供使用者名稱，這是必要項目。必須使用「資料搜索器」隨附的 VCrypt 程式庫來加密密碼。
*  **archive** - 讓 Samba 連接器可搜索及為保存檔內壓縮的檔案建立索引。值為 `true` 或 `false`；預設值是 `false`。
*  **max-policies-per-handle** - 指定可針對單一 RPC 控點開放的「本端安全權限 (LSA)」原則的數量上限。這些原則可定義在各種情況下查詢或修改特定系統所需的存取權。此選項的預設值是 `255`。
*  **crawl-fs-metadata** - 開啟此選項將造成資料搜索器新增 VXML 文件，其含有關於檔案的可用檔案系統的 meta 資料（建立日期、前次修改日期、檔案屬性等）
*  **enable-arc-connector** - 未使用的選項。
*  **disable-indexes** - 要停用的以換行區隔索引清單，這可會使搜索速度更快，例如：

   *  disable-url-index
   *  disable-error-state-index
   *  disable-crawl-time-index
*  **exact-duplicates-hash-size** - 設定用來解析確切複製的雜湊表大小。修改此數量時請務必小心。選取的值應該是質數，較大的大小可以提供更快速的查閱，但會需要更多的記憶體，而較小的大小可能會降低搜索速度，但實質上可減少記憶體用量。
*  **user-agent** - 未使用的選項。
*  **timeout** - 未使用的選項。
*  **n-concurrent-requests** - 將平行傳送至單一 IP 位址的要求數量。預設值是 `1`。
*  **enqueue-persistence** - 未使用的選項。

### 配置 SharePoint 連接器
SharePoint 連接器可讓您搜索 SharePoint 伺服器及 SharePoint Online 物件，並將其包含的資訊建立索引。諸如文件、使用者設定檔、網站集合、部落格、清單項目、成員資格清單、目錄頁面等物件，都可以使用其關聯的 meta 資料建立索引。對於清單項目和文件，索引可以包括附件。

**附註**：SharePoint 連接器在所有 SharePoint 物件上會遵守 `noindex` 屬性，不論其特定類型（部落格、文件、使用者設定檔等等）為何。每一個結果會傳回單一文件。

**重要事項**：您用來搜索 SharePoint 網站的 SharePoint 帳戶必須至少具備完整的讀取存取權。

下列是使用 SharePoint 連接器所需的基本配置選項。若要設定這些值，請開啟檔案 `config/connectors/sharepoint.conf`，並修改您的使用案例特定的下列值：

*  **protocol** - 用於搜索的連接器通訊協定的名稱。對此連接器使用 `io-sp`。
*  **collection** - 此屬性是用來解壓縮暫存檔。
*  **classname** - 連接器的 Java 類別名稱。用來使用此連接器的值必須是 `plugin:io-sharepoint.plugin@connector`。
*  **logging-config** - 指定用於配置記載選項的檔案；必須以 `log4j` XML 字串的形式將它格式化。
*  **seed-url-type** - 識別提供的種子 URL 指向的 SharePoint 物件的類型：網站集合或 Web 應用程式（亦稱為虛擬伺服器）。

   *  ***網站集合*** - 如果「種子 URL 類型」設為 `Site Collections`，則只會搜索 URL 所參照的網站集合的子項。
   *  ***Web 應用程式*** - 如果「種子 URL 類型」設為 `Web Applications`，則會搜索屬於每一個 URL 所參照的 Web 應用程式（及其子項）的所有網站集合。
*  **auth-type** - 聯絡 SharePoint 伺服器時要使用的鑑別機制：`BASIC`、`NTLM2`、`KERBEROS` 或 `CBA`。預設鑑別類型是 `NTLM2`。
*  **spUser** - 用來存取內容的 SharePoint 使用者的使用者名稱。此使用者必須可存取要搜索及建立索引的所有目標網站和清單，並且必須能擷取及解析相關聯的許可權。建議您使用網域名稱輸入它，像是：`MYDOMAIN\\Administrator`。
*  **spPassword** - 用來存取內容的 SharePoint 使用者的密碼。必須使用「資料搜索器」隨附的 vcrypt 程式加密密碼。
*  **cba-sts** - 用來嘗試對搜索使用者進行鑑別的「安全記號服務 (STS)」端點的 URL。對於 ADFS 的 SharePoint 內部部署，這應該是 ADFS 端點。如果「鑑別類型」設為 `CBA`（「宣告型鑑別」），則此為必要欄位。
*  **cba-realm** - 從 STS 要求安全記號時要使用的中繼方信任 ID。這有時稱為 "AppliesTo" 值，或「領域」。針對 SharePoint Online，這應該是 SharePoint Online 實例根目錄的 URL（例如，`https://mycompany.sharepoint.com`）。針對 ADFS，這是介於 SharePoint 與 ADFS 之間「依賴方信任」的 ID 值（例如，`"urn:SHAREPOINT:adfs"`）。
*  **everyone-group** - 若指定，在應該提供每個人存取時，會在 ACL 中使用此群組名稱。啟用搜索使用者設定檔時，這是必要欄位。**附註** -「擷取和分級」服務尚未遵守安全。
*  **user-profile-master-url** - 連接器用來建置使用者設定檔鏈結的基本 URL。應該配置此項目，以指向使用者設定檔的顯示表單。如果發現記號 `%FIRST_SEED%`，會將它以第一個種子 URL 取代。啟用搜索使用者設定檔時，這是必要欄位。
*  **urls** - 要搜索的 SharePoint Web 應用程式或網站集合的 HTTP URL 以換行區隔清單。
*  **ehcache-config** - 未使用的選項。
*  **method** - 將藉以傳遞參數的方法（`GET` 或 `POST`）。
*  **cache-types** - 未使用的選項。
*  **cache-size** - 未使用的選項。
*  **enable-acl** - 啟用搜索 SharePoint 使用者設定檔；值為 `true` 或 `false`。預設值是 `false`。

### 配置 Box 連接器
「Box 連接器」可讓您搜索您的「企業 Box」實例，並將它所包含的資訊建立索引。下列是使用 Box 連接器所需的基本配置選項。若要設定這些值，請開啟檔案 `config/connectors/box.conf`，並修改您的使用案例特定的下列值：

*  **protocol** - 用於搜索的連接器通訊協定的名稱。對此連接器使用 `box`。
*  **classname** - 連接器的 Java 類別名稱。用來使用此連接器的值必須是 `plugin:box.plugin@connector`。
*  **logging-config** - 指定用於配置記載選項的檔案；必須以 `log4j` XML 字串的形式將它格式化。
*  **box-crawl-seed-url** - Box 的基本 URL。此連接器的值是 `box://app.box.com/`。您也可以搜索不同類型的 URL，例如：

   *  ***若要搜索整個企業***：`box://app.box.com/`
   *  ***若要搜索特定資料夾***：`box://app.box.com/user/USER_ID/folder/FOLDER_ID/FolderName`
   *  ***若要搜索特定使用者***：`box://app.box.com/user/USER_ID/`
*  **client-id** - 輸入建立 Box 應用程式時 Box 所提供的用戶端 ID。
*  **client-secret** - 輸入建立 Box 應用程式時 Box 所提供的用戶端機密。
*  **path-to-private-key** - 這是在您的本端檔案系統上私密金鑰的位置，該金鑰屬於產生用來與 Box 進行通訊的私密-公開金鑰組的一部分。
*  **kid** - 指定公開金鑰 ID。這是產生用來與 Box 進行通訊的私密-公開金鑰組的另一半。
*  **enterprise-id** - 應用程式獲授權所在的企業。「企業 ID」會列在「Box 管理者主控台」的主頁面。
*  **enable-acl** - 僅供內部使用。啟用擷取已搜索資料的 ACL。
*  **user-agent** - 搜索文件時傳送至伺服器的標頭。
*  **method** - 將藉以傳遞參數的方法（`GET` 或 `POST`）。
*  **url-logging** - 記載搜索的 URL 到何種程度。可能的值是：

   *  ***full-logging*** - 記載 URL 的所有相關資訊。
   *  ***refined-logging*** - 僅記載瀏覽搜索器日誌以及讓連接器正確運作所需的資訊；這是預設值。
   *  ***minimal-logging*** - 僅記載讓連接器正確運作所需的資訊量下限。

   將此選項設定為 minimal-logging 將減少日誌的大小，且由於與減少要記載的資料量相關聯的 I/O 較小，將稍微增加效能。
*  **ssl-version** - 指定要用於 HTTPS 連線的 SSL 版本。預設會使用最強大的通訊協定。

Box 連接器具有部分限制：

* 不會擷取檔案上的「評論」或「作業」。
* 會將附註內容主體擷取為 JSON。可能需要進一步轉換「附註」資料。
* 無法透過 TestIt 擷取個別文件。只可以透過 TestIt 擷取種子 URL、資料夾 URL，以及使用者 URL。


## 另請參閱

crawler(1)

vcrypt(1)

crawler.conf(5)

crawler-seed.conf(5)

orchestration_service.conf(5)